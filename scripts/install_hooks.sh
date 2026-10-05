#!/bin/sh
# Turn on the optional pre-commit hook in .githooks/.
# It runs build, lint, source-lint and audit_public.py before every commit.
#
# macOS / Linux / Git Bash:  sh scripts/install_hooks.sh
# Windows PowerShell:        git config core.hooksPath .githooks
# Turn it off again:         git config --unset core.hooksPath

cd "$(git rev-parse --show-toplevel)" || exit 1
chmod +x .githooks/pre-commit 2>/dev/null
git config core.hooksPath .githooks
echo "Pre-commit hook installed: git now runs .githooks/pre-commit before each commit."
echo "Skip it once with: git commit --no-verify"
echo "Turn it off with:  git config --unset core.hooksPath"
