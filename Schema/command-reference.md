# Command reference

The vault's helper scripts live in `scripts/`. They use only Python's standard library, so there is nothing to install besides Python 3.8 or newer.

## How to run them

Open a terminal **in the vault folder** (the folder that has `AGENTS.md` in it), then:

| System | Command to start Python | Example |
| --- | --- | --- |
| macOS / Linux | `python3` | `python3 scripts/wiki_tool.py doctor` |
| Windows (PowerShell or Command Prompt) | `python` or `py` | `python scripts/wiki_tool.py doctor` |

On Windows, if `python` opens the Microsoft Store or says it is not recognised, try `py` instead. If neither works, install Python from [python.org](https://www.python.org/downloads/) and tick **Add python.exe to PATH** during setup.

The examples below use `python3`. On Windows, write `python` (or `py`) in its place.

Every command prints `OK` when all is well. Problems start with `ERROR` (the command fails) or `WARN` (worth fixing, but not a failure).

## `scripts/wiki_tool.py`

| Command | What it does | Changes files? |
| --- | --- | --- |
| `doctor` | Health check: Python version, required folders, note and source counts, and whether the catalog and manifest are up to date. | No |
| `build` | Writes `Wiki/catalog.jsonl`, `Wiki/index.md` and an `index.md` in each Wiki folder. | Yes, only those generated files |
| `lint` | Checks every compiled Wiki note: frontmatter, exactly one allowed tag that matches its folder, `status`, dates, `sources` pointing to real files in `Raw/Sources/`, and `source_count`. | No |
| `source-scan` | Lists the Raw sources and how many Wiki notes cite each one. | No |
| `source-scan --update` | Same, and writes `Schema/source-manifest.jsonl`. | Yes, the manifest |
| `source-scan --update --accept-covered` | Same, and counts a source as processed in the manifest once a Wiki note cites it. Use it after an ingest. | Yes, the manifest |
| `source-lint` | Checks every Raw source's frontmatter (`Title`, `Reference`, `Created`, `Processed`, `tags`) and fails if a source is marked processed but no Wiki note covers it. | No |
| `source-delta` | Shows Raw sources that are new since the last manifest update, or have been removed. | No |
| `source-coverage` | Shows which Wiki notes cite each Raw source. | No |
| `search-catalog --query "text"` | Searches the compiled notes through the catalog, best matches first. Add `--limit 5` to show fewer. Run `build` first. | No |
| `log --title "title" --details "details"` | Adds a dated line to `Wiki/log.md`. | Yes, the log |

### Generated files

`build` and `source-scan --update` write these files. Do not edit them by hand; run the command again instead.

- `Wiki/catalog.jsonl`: one line per compiled note, with `path`, `title`, `tag`, `topics`, `sources`, `updated` and a short `summary`.
- `Wiki/index.md` and `Wiki/<Folder>/index.md`: lists of notes you can click through in Obsidian.
- `Schema/source-manifest.jsonl`: one line per Raw source, with `path`, `title`, `processed`, `covered_by` and `updated`.

## `scripts/audit_public.py`

```bash
python3 scripts/audit_public.py
```

Checks every file git would commit and fails if it finds:

- something that looks like a password, API key, token or private key;
- a path from your own computer, such as your user folder;
- Obsidian plugin state, caches or window layout, raw files from `Raw/Files/`, drafts, `.env` files or key files.

If a line is a false alarm, add the text `audit-public: ignore` to that line.

## Maintenance gate

Run these before every meaningful commit:

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-lint
python3 scripts/audit_public.py
```

After ingesting sources, also run:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
```

## Optional: run the checks automatically before each commit

The vault includes a git hook, `.githooks/pre-commit`, that runs `build`, `lint`, `source-lint` and `audit_public.py` every time you commit, and stops the commit if one fails. It is **off** until you turn it on:

| System | Turn it on |
| --- | --- |
| macOS / Linux / Git Bash | `sh scripts/install_hooks.sh` |
| Windows PowerShell | `git config core.hooksPath .githooks` |

- Turn it off again: `git config --unset core.hooksPath`
- Skip it for one commit: `git commit --no-verify`

If `build` changed the catalog or indexes, the hook stops and asks you to `git add` them, so the commit always carries up-to-date indexes.
