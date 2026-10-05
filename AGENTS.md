# AGENTS.md

Instructions for any AI agent working in this vault. Read this file first, then the files in `Schema/`.

## What this vault is

An LLM wiki. The person who owns it collects sources; you, the agent, compile them into short, linked, reusable notes and keep those notes up to date. The person reads the wiki and tells you what to do next.

## The layers

| Folder | What it holds | Who writes it |
| --- | --- | --- |
| `Raw/Sources/` | Source notes in Markdown: articles, transcripts, notes | The person |
| `Raw/Files/` | Original files such as PDFs and images (not in git) | The person |
| `Wiki/` | Compiled notes in `Topics/`, `Concepts/`, `Entities/`, `Projects/`, `Logs/` | You |
| `Schema/` | The rules for how the wiki works | The person, with your suggestions |

Other folders: `_templates/` holds note templates, `.agents/skills/` holds the skills you use here, `scripts/` holds helper scripts, `tutorial/` holds tutorial notes.

## Rules

1. Treat `Raw/Sources/` as source material, not as compiled notes. Do not rewrite a source's content. The only change you make there is setting `Processed: true` once a source is covered.
2. Write reusable knowledge only under `Wiki/`.
3. Keep every compiled note linked to one or more Raw sources in its `sources` field, and keep `source_count` equal to the number of `sources`.
4. Search `Wiki/catalog.jsonl` before opening broad Raw context. Open Raw sources only when the compiled notes are not enough.
5. Run the `build`, `lint` and source checks before every commit (see the maintenance gate below).
6. Do not invent citations or create unsupported claims. If the sources do not say it, do not write it.
7. Follow `Schema/frontmatter-schema.md` for note properties and `Schema/naming-conventions.md` for names.
8. Ask before deleting a Wiki note or changing anything in `Schema/`.
9. Never put passwords, tokens, private keys or machine-local paths in any file.

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

On Windows, use `python` (or `py`) instead of `python3`. If `Wiki/catalog.jsonl` does not exist yet, run `build` first. Every command is explained in `Schema/command-reference.md`.

## Skills

- `llm-wiki-ingest`: compile new Raw sources into Wiki notes.
- `llm-wiki-query`: answer a question from the compiled Wiki.
- `llm-wiki-lint`: check the Wiki against `Schema/lint-checklist.md`.
- `llm-wiki-maintain`: rebuild indexes, update the source manifest and run the maintenance gate.

Worked examples of each are in `Schema/workflow-examples.md`.
