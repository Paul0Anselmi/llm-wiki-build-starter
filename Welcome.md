# Welcome to llm-wiki-starter

This vault is the starting point for an **LLM wiki**: a knowledge base that an AI agent writes and maintains, and that you read and direct.

## The idea in one minute

You collect **sources**: articles, video transcripts, your own notes. The agent reads them and **compiles** them into short, linked notes, one idea per note, each pointing back to where it came from. When you have a question, the agent searches those compiled notes first, so answers stay fast and traceable.

The vault will have three layers:

- `Raw/`: your sources, kept as they are.
- `Wiki/`: the notes the agent compiles from them.
- `Schema/`: the rules the agent follows.

## How this tutorial works

The vault is built one step at a time. Each step adds one small piece and is saved as its own git commit, named after the step. You can always see what a step changed, and go back to it.

This is step `tutorial-04-tooling`. The agent has its rules, skills and templates, and `scripts/` now has the tools that build the indexes and check the wiki. The Raw and Wiki folders are still empty.

## What is here

- `Welcome.md`: this note.
- `README.md`: how to set up and use the vault.
- `AGENTS.md`: the instructions the AI agent reads first, before doing anything in this vault.
- `.gitignore`: tells git which files to leave out of the history: your window layout and plugin state (they change every time you open Obsidian), large raw files, drafts, and anything secret such as passwords or keys.
- `.obsidian/`: Obsidian's own settings for this vault.

### Folders

| Folder | What goes in it |
| --- | --- |
| `Raw/Sources/` | Your sources as Markdown notes: articles, video transcripts, your own notes. |
| `Raw/Files/` | Original files such as PDFs, images and audio. They stay on your device and are not saved in git. |
| `Wiki/Topics/` | Broad subjects that group other notes. |
| `Wiki/Concepts/` | One idea per note, explained briefly. |
| `Wiki/Entities/` | People, organisations, tools and places. |
| `Wiki/Projects/` | Things being built or worked on. |
| `Wiki/Logs/` | Dated records of what happened or was decided. |
| `Schema/` | The rules the agent follows: note properties, names, a lint checklist and worked examples. |
| `_templates/` | Templates for new notes: `source-note`, `concept-note`, `topic-note`, `entity-note`, `project-note` and `log-note`. |
| `.agents/skills/` | Skills the agent uses inside this vault: ingest, query, lint and maintain. Obsidian hides folders that start with a dot, so you will not see it there. |
| `scripts/` | `wiki_tool.py` (builds the indexes and checks the wiki), `audit_public.py` (checks nothing private gets committed) and `install_hooks.sh` (optional). |
| `tutorial/` | Notes about the tutorial steps. |

Each folder that is still empty holds a hidden `.gitkeep` file. Git does not save empty folders, so this tiny file keeps them in the history.

## Using a template

In Obsidian, create a new note, open the command palette (`Ctrl+P`, or `Cmd+P` on a Mac) and run **Templates: Insert template**. Pick a template and Obsidian fills in the title and today's date.

## Checking the wiki

Open a terminal in the vault folder and run:

```
python3 scripts/wiki_tool.py doctor
```

On Windows, type `python` (or `py`) instead of `python3`. All commands are listed in `Schema/command-reference.md`.

## What comes next

Step `tutorial-05-first-ingest` adds the first source to `Raw/Sources/` and compiles it into Wiki notes.
