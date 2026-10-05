# Lint checklist

What a healthy wiki looks like. The agent checks each item during a lint.

## Structure

- [ ] Every page in `Wiki/` has frontmatter with `type`, `created`, `updated` and `sources`.
- [ ] Every page follows its section layout in `page-types.md`.
- [ ] File names follow `naming-conventions.md`.

## Links

- [ ] No broken wikilinks (links to pages that do not exist).
- [ ] No orphan pages: every page is linked from at least one other page or from `Wiki/index.md`.
- [ ] Every file in `Raw/` has a `source` page.
- [ ] Every link in a `sources` field points to a file that exists in `Raw/`.

## Content

- [ ] Every claim cites a source.
- [ ] Contradictions are marked on both pages and tagged `#contradiction`.
- [ ] No two pages cover the same subject under different names.
- [ ] Subjects mentioned on several pages without a page of their own are listed as candidates.

## Housekeeping

- [ ] `Wiki/index.md` lists every page.
- [ ] `Wiki/log.md` has a line for every recent change.
- [ ] Nothing in `Raw/` was changed by the agent.
- [ ] No passwords, tokens or keys in any file.
