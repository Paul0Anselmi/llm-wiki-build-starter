# AGENTS.md

Instructions for any AI agent working in this vault. Read this file first, then the files in `Schema/`.

## What this vault is

An LLM wiki. The person who owns it collects sources; you, the agent, turn them into a linked set of wiki pages and keep those pages up to date. The person reads the wiki and tells you what to do next.

## The three layers

| Folder | What it holds | Who writes it |
| --- | --- | --- |
| `Raw/` | Original sources: articles, PDFs, notes, transcripts | The person. **Never edit, rename or delete anything here.** |
| `Wiki/` | Wiki pages built from the sources | You |
| `Schema/` | The rules for how the wiki works | The person, with your suggestions |

Other folders: `_templates/` holds note templates, `.agents/skills/` holds the skills you use here, `scripts/` holds helper scripts, `tutorial/` holds tutorial notes.

## Rules

1. Treat `Raw/` as read-only.
2. Every claim in a wiki page links to the source it came from in `Raw/`.
3. Follow the page structure in `Schema/page-types.md` and the names in `Schema/naming-conventions.md`.
4. Link related pages with Obsidian wikilinks: `[[Page Name]]`.
5. Keep `Wiki/index.md` (the table of contents) and `Wiki/log.md` (the change log) up to date on every change.
6. When sources disagree, say so on the page and cite both. Do not quietly pick one.
7. Ask before deleting a wiki page or changing anything in `Schema/`.
8. Never put passwords, tokens or keys in any file.

## How to work

The three jobs you do are described in `Schema/workflows.md`:

- **Ingest**: read a new source and update the wiki. Skill: `.agents/skills/ingest-source/`.
- **Query**: answer a question from the wiki. Skill: `.agents/skills/query-wiki/`.
- **Lint**: check the wiki for problems. Skill: `.agents/skills/lint-wiki/`, using `Schema/lint-checklist.md`.
