# Lint checklist

What a healthy wiki looks like. From tutorial step 04, `scripts/wiki_tool.py lint` and `source-lint` check most of this automatically. Until then, the agent checks it by hand.

## Compiled Wiki notes

- [ ] Frontmatter follows `frontmatter-schema.md`.
- [ ] Exactly one allowed tag: `topic`, `concept`, `entity`, `project` or `log`.
- [ ] The note is in the folder that matches its tag.
- [ ] `sources` has at least one link, and every link points to a file that exists in `Raw/Sources/`.
- [ ] `source_count` equals the number of `sources`.
- [ ] Every claim is supported by a listed source. No invented citations.
- [ ] File name follows `naming-conventions.md`.

## Raw sources

- [ ] Every file in `Raw/Sources/` has `Title`, `Reference`, `Created`, `Processed` and `tags`.
- [ ] A source marked `Processed: true` is listed in the `sources` of at least one Wiki note.
- [ ] The agent did not change a source's content.

## Links and indexes

- [ ] No broken wikilinks.
- [ ] No orphan notes: every Wiki note is linked from another note or an index.
- [ ] `Wiki/index.md`, the per-folder indexes and `Wiki/catalog.jsonl` are up to date (rebuilt by `build`).

## Safety

- [ ] No passwords, tokens, private keys or machine-local paths.
- [ ] No plugin state, caches or files from `Raw/Files/` committed.
