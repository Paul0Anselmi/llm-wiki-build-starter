# Page types

Every wiki page lives in `Wiki/` and starts with frontmatter (the block between `---` lines) that says what kind of page it is.

## Common frontmatter

```yaml
---
type: source | topic | entity
created: 2026-01-31
updated: 2026-01-31
sources:
  - "[[Raw/example-article.md]]"
tags: []
---
```

- `type`: one of the page types below.
- `created` and `updated`: dates in `YYYY-MM-DD` format.
- `sources`: links to the files in `Raw/` this page draws on.
- `tags`: optional, see `naming-conventions.md`.

## `source`: one page per raw source

A summary of a single file in `Raw/`.

- **Summary**: what the source says, in a few sentences.
- **Key points**: a bullet list.
- **Related**: links to the topic and entity pages this source feeds.

## `topic`: one page per idea or subject

What the wiki knows about a subject, drawn from all sources.

- **Overview**: a short explanation.
- **Details**: the main points, each citing a source.
- **Open questions**: things the sources do not answer or disagree on.
- **Related**: links to other pages.

## `entity`: one page per person, organisation, tool or place

- **Who or what it is**: one or two sentences.
- **Appears in**: links to the source and topic pages that mention it.

## Special pages

- `Wiki/index.md`: the table of contents. Lists every page with a one-line description, grouped by type.
- `Wiki/log.md`: the change log. One line per change, newest at the bottom: `YYYY-MM-DD: what changed (source or question)`.

The agent creates both the first time it ingests a source.
