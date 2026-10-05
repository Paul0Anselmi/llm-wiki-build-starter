# Workflows

The three jobs the agent does in this vault. Each one ends by updating `Wiki/log.md`.

## Ingest: add a new source

Use when a new file appears in `Raw/`. Skill: `.agents/skills/ingest-source/`.

1. Read the source in full.
2. Tell the person the main points in a few lines and ask if anything should be stressed or skipped.
3. Create its `source` page in `Wiki/`.
4. Update every `topic` and `entity` page the source touches, or create them if missing. Cite the source on each.
5. Mark any contradiction with an existing page on both pages and tag them `#contradiction`.
6. Add new pages to `Wiki/index.md`.
7. Add a line to `Wiki/log.md`.

## Query: answer a question

Skill: `.agents/skills/query-wiki/`.

1. Read `Wiki/index.md` to find relevant pages.
2. Read those pages and follow their links as needed.
3. Answer with links to the wiki pages and sources used.
4. If the wiki cannot answer, say so and suggest what source would help.
5. If the answer is worth keeping, offer to save it as a new `topic` page.

## Lint: check the wiki's health

Run every now and then, or after several ingests. Skill: `.agents/skills/lint-wiki/`.

1. Go through `Schema/lint-checklist.md` item by item.
2. Fix the small, safe problems (a missing index entry, a broken link to a renamed page).
3. List everything else for the person to decide.
4. Add a line to `Wiki/log.md`.
