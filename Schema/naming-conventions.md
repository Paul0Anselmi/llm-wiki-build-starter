# Naming conventions

Consistent names keep links working and make notes easy to find.

## Files

- Raw source files use lowercase words joined by hyphens: `Raw/Sources/why-llm-wiki.md`.
- Wiki note files use the note's title with normal capitals and spaces: `Wiki/Concepts/Compiled Knowledge.md`.
- Log notes start with the date: `Wiki/Logs/2026-01-31 First Ingest.md`.
- No characters that break links: `# ^ [ ] | \ / : ? * " < >`.

## Titles

- One idea per note, named by the plainest common name: `Large Language Model`, not `LLMs and their uses`.
- Singular, not plural: `Vector Database`, not `Vector Databases`.
- People by full name: `Ada Lovelace`.
- Spell out an abbreviation in the title and put the short form in `aliases`.

## Links

- Link with Obsidian wikilinks: `[[Large Language Model]]`.
- To show different text: `[[Large Language Model|LLMs]]`.
- Link the first mention of a note on another note, not every mention.
- In `sources`, link the Raw file by path: `"[[Raw/Sources/why-llm-wiki]]"`.

## Tags

- Each compiled note has exactly one of: `topic`, `concept`, `entity`, `project`, `log`.
- Raw sources have the tag `source`.
- Use links and `topics` for subjects, not extra tags.
