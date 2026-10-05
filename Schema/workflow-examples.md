# Workflow examples

Short worked examples of the four jobs the agent does here. Every command is explained in `command-reference.md`; on Windows, use `python` (or `py`) instead of `python3`.

## Ingest a new source

The person adds `Raw/Sources/why-llm-wiki.md` and says: "Ingest the new source."

1. Read the source and note its main claims.
2. Search the wiki for related notes: `python3 scripts/wiki_tool.py search-catalog --query "llm wiki"`.
3. Open only the most relevant Wiki notes.
4. Create or update focused notes, for example:
   - `Wiki/Topics/LLM Wiki.md` (`topic`)
   - `Wiki/Concepts/Compiled Knowledge.md` (`concept`)
5. Add `"[[Raw/Sources/why-llm-wiki]]"` to each note's `sources` and update `source_count`.
6. Set `Processed: true` on the source.
7. Run the maintenance gate from `AGENTS.md`, including `source-scan --update --accept-covered`.
8. Add a log entry if the wiki changed in a meaningful way: `python3 scripts/wiki_tool.py log --title "Ingest why-llm-wiki" --details "Added 2 notes"`.

## Answer a question

The person asks: "What is the difference between Raw and Wiki?"

1. Start with `Wiki/index.md`.
2. Search the catalog: `python3 scripts/wiki_tool.py search-catalog --query "raw wiki"`.
3. Open the matching notes and answer from them.
4. Open the Raw source only if the notes are not enough or the person asks for source-level proof.
5. Cite the Wiki note and its Raw source in the answer.

## Lint the wiki

The person says: "Check the wiki."

1. Run `python3 scripts/wiki_tool.py lint` and `python3 scripts/wiki_tool.py source-lint`.
2. Go through anything in `lint-checklist.md` the scripts do not cover.
3. Fix small, safe problems, such as a wrong `source_count`.
4. List anything that needs a decision, such as two notes on the same idea.

## Maintain the wiki

Before a commit, or after several changes:

1. `python3 scripts/wiki_tool.py doctor`
2. `python3 scripts/wiki_tool.py build` to rebuild the catalog and indexes.
3. `python3 scripts/wiki_tool.py lint` and `source-lint`.
4. `python3 scripts/audit_public.py` to check for secrets and private paths.
5. Commit only when all of them pass.
