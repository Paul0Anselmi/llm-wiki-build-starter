#!/usr/bin/env python3
"""Check the vault is safe to publish before a commit.

Fails (exit code 1) on obvious secrets, private keys, machine-local paths,
and Obsidian plugin/cache state or raw files that should not be in git.
Uses only the Python standard library.

    python3 scripts/audit_public.py      # macOS / Linux
    python scripts/audit_public.py       # Windows (or: py scripts/audit_public.py)

To keep a line that is a known false alarm, add the text `audit-public: ignore` to it.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IGNORE_MARKER = "audit-public: ignore"
MAX_BYTES = 2_000_000

# The patterns are split into pieces so this file does not flag itself.
CONTENT_RULES = [
    ("private key", re.compile("-----BEGIN [A-Z ]*" + "PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\bAKIA" + r"[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_" + r"[A-Za-z0-9]{36,}|\bgithub_pat_" + r"[A-Za-z0-9_]{20,}")),
    ("API key (sk-...)", re.compile(r"\bsk-" + r"(?:ant-|proj-)?[A-Za-z0-9_-]{20,}")),
    ("Slack token", re.compile(r"\bxox[abprs]-" + r"[A-Za-z0-9-]{10,}")),
    ("Google API key", re.compile(r"\bAIza" + r"[0-9A-Za-z_-]{35}\b")),
    ("password or secret assigned in text", re.compile(
        r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\b"
        + r"\s*[:=]\s*[\"']?[^\s\"'<>]{8,}")),
    ("machine-local path (Windows)", re.compile(r"\b[A-Za-z]:[\\/]+" + r"(?:Users|Documents and Settings)[\\/]+[^\\/\s]+", re.I)),
    ("machine-local path (macOS)", re.compile(r"(?<![\w.])/" + r"Users/[^/\s]+/")),
    ("machine-local path (Linux)", re.compile(r"(?<![\w.])/" + r"home/[^/\s]+/")),
]

# Paths that must never be committed (checked against vault-relative paths).
FORBIDDEN_PATHS = [
    ("Obsidian plugin state", re.compile(r"^\.obsidian/plugins/")),
    ("Obsidian cache", re.compile(r"^\.obsidian/cache")),
    ("Obsidian logs", re.compile(r"^\.obsidian/logs/")),
    ("Obsidian window layout", re.compile(r"^\.obsidian/workspace[^/]*\.json$")),
    ("Obsidian trash", re.compile(r"^\.trash/")),
    ("raw binary file (keep it out of git)", re.compile(r"^Raw/Files/(?!\.gitkeep$)")),
    ("draft", re.compile(r"^Drafts/")),
    ("environment file with secrets", re.compile(r"(^|/)\.env(\.(?!example$)[^/]+)?$")),
    ("key or certificate file", re.compile(r"\.(key|pem|p12|pfx)$", re.I)),
]


def candidate_files():
    """Files git would commit: tracked plus untracked-but-not-ignored."""
    try:
        output = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, capture_output=True, check=True,
        ).stdout.decode("utf-8", errors="replace")
        return sorted({path for path in output.split("\0") if path and (ROOT / path).is_file()})
    except (OSError, subprocess.CalledProcessError):
        print("WARN  git not available: scanning every file in the vault folder instead")
        skip = re.compile(r"^(\.git/|\.obsidian/(plugins|cache|logs)/|\.trash/|Raw/Files/|Drafts/)")
        return sorted(
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file() and not skip.match(path.relative_to(ROOT).as_posix())
        )


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    problems = []
    files = candidate_files()
    for path in files:
        for label, pattern in FORBIDDEN_PATHS:
            if pattern.search(path):
                problems.append("{}: {} should not be committed".format(path, label))
        full = ROOT / path
        if full.stat().st_size > MAX_BYTES:
            continue
        data = full.read_bytes()
        if b"\0" in data:
            continue
        for number, line in enumerate(data.decode("utf-8", errors="replace").splitlines(), start=1):
            if IGNORE_MARKER in line:
                continue
            for label, pattern in CONTENT_RULES:
                if pattern.search(line):
                    problems.append("{}:{}: looks like a {}".format(path, number, label))
    for problem in problems:
        print("ERROR " + problem)
    if problems:
        print("FAILED: audit_public found {} problem(s). Remove them before committing.".format(len(problems)))
        return 1
    print("OK    audit_public: {} file(s) checked, nothing private found".format(len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
