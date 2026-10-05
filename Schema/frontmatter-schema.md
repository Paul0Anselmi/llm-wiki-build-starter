# Frontmatter schema

Every note starts with frontmatter: the block of properties between two `---` lines. Obsidian shows it as **Properties**. The agent and the lint checks rely on these fields.

## Raw source notes (`Raw/Sources/`)

```yaml
---
Title: ""
Author: ""
Reference: ""
ContentType:
  - "markdown"
Created: YYYY-MM-DD
Processed: false
tags:
  - "source"
---
```

| Field | Required | Meaning |
| --- | --- | --- |
| `Title` | yes | The source's title. |
| `Author` | no | Who made it. |
| `Reference` | yes | Where it came from: a URL, a book, or `owned` for your own notes. |
| `ContentType` | no | The original format, such as `markdown`, `video` or `pdf`. |
| `Created` | yes | Date added, `YYYY-MM-DD`. |
| `Processed` | yes | `false` until Wiki notes cover this source, then `true`. |
| `tags` | yes | Always includes `source`. |

## Compiled Wiki notes (`Wiki/`)

```yaml
---
tags:
  - "concept"
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
aliases: []
---
```

| Field | Required | Meaning |
| --- | --- | --- |
| `tags` | yes | Exactly one allowed tag: `topic`, `concept`, `entity`, `project` or `log`. |
| `topics` | no | Links to the topic notes this note belongs to, such as `"[[LLM Wiki]]"`. |
| `status` | yes | `seed` (new and thin), `growing` (several sources) or `evergreen` (stable). |
| `created` / `updated` | yes | Dates in `YYYY-MM-DD` format. |
| `sources` | yes | Links to files in `Raw/Sources/`, such as `"[[Raw/Sources/why-llm-wiki]]"`. At least one. |
| `source_count` | yes | The number of entries in `sources`. |
| `aliases` | no | Other names for the note, such as abbreviations. |

## Which tag goes in which folder

| Tag | Folder | Use for |
| --- | --- | --- |
| `topic` | `Wiki/Topics/` | A broad subject that groups other notes. |
| `concept` | `Wiki/Concepts/` | One idea, explained briefly. |
| `entity` | `Wiki/Entities/` | A person, organisation, tool or place. |
| `project` | `Wiki/Projects/` | Something being built or worked on. |
| `log` | `Wiki/Logs/` | A dated record of what happened or was decided. |
