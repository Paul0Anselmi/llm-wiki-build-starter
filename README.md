# llm-wiki-starter

An Obsidian vault for building an **LLM wiki**: a personal knowledge base that an AI agent writes and keeps up to date, while you collect the sources and decide what matters.

## How it works

1. You save a **source** in `Raw/Sources/`: an article, a video transcript, your own notes.
2. You ask your AI agent to **ingest** it. The agent compiles it into short notes in `Wiki/`, one idea per note, each linking back to the source it came from.
3. When you have a question, you ask the agent. It searches the compiled notes first and opens the raw sources only when it needs more detail.
4. Every so often, you ask the agent to **lint** the wiki: check for broken links, missing sources and notes that drifted from the rules.

Over time, `Wiki/` becomes a linked map of everything you have read, and you can open it in Obsidian to browse it yourself.

## What you need

- [Obsidian](https://obsidian.md), to read and browse the vault.
- [Git](https://git-scm.com), to save the history and sync with GitHub.
- An AI coding agent that can read and edit files in this folder, such as Claude Code. Point it at `AGENTS.md` first.

## Getting started

1. **Get the vault on your computer.** In a terminal, go to where you keep your projects and run:

   ```bash
   git clone https://github.com/Paul0Anselmi/llm-wiki-build-starter.git
   ```

2. **Open it in Obsidian.** Choose *Open folder as vault* and pick the `llm-wiki-build-starter` folder.
3. **Read `Welcome.md`.** It shows what the vault has at the current tutorial step.

## Folders

| Folder | What goes in it | Who writes it |
| --- | --- | --- |
| `Raw/Sources/` | Your sources as Markdown notes. | You |
| `Raw/Files/` | Original files such as PDFs, images and audio. Not saved in git. | You |
| `Wiki/Topics/` | Broad subjects that group other notes. | The agent |
| `Wiki/Concepts/` | One idea per note. | The agent |
| `Wiki/Entities/` | People, organisations, tools and places. | The agent |
| `Wiki/Projects/` | Things being built or worked on. | The agent |
| `Wiki/Logs/` | Dated records of what happened or was decided. | The agent |
| `Schema/` | The rules the agent follows. | You, with the agent's suggestions |
| `_templates/` | Starting shapes for new notes. | You |
| `.agents/skills/` | Skills the agent uses inside this vault. Hidden in Obsidian because the name starts with a dot. | You |
| `scripts/` | Helper scripts that check the wiki. | You |
| `tutorial/` | Notes about the tutorial steps. | You |

Empty folders hold a hidden `.gitkeep` file so git keeps them.

## Keeping your vault in sync

The vault on GitHub and the folder on your computer are two copies. Git moves changes between them.

- **Get the latest changes from GitHub:**

  ```bash
  git pull
  ```

- **Save and upload your own changes:**

  ```bash
  git add .
  git commit -m "Short description of what changed"
  git push
  ```

Run these in a terminal opened inside the vault folder. `git status` shows what changed since your last commit.

## The tutorial

The vault is built one step at a time. Each step is a single git commit named after it, so you can see exactly what it added with `git log --oneline`.

| Step | What it adds | Status |
| --- | --- | --- |
| `tutorial-00-empty-vault` | `Welcome.md`, `.gitignore` and Obsidian settings | Done |
| `tutorial-01-core-structure` | The folder structure above | Done |
| `tutorial-02-schema-and-agents` | `AGENTS.md`, the schema rules and the agent skills | Done |
| `tutorial-03-templates` | Note templates for sources and each kind of Wiki note | Next |
| `tutorial-04-tooling` | `scripts/wiki_tool.py` and the automatic checks | Planned |
| `tutorial-05-first-ingest` | A first source compiled into Wiki notes | Planned |
| `tutorial-06-query-and-lint` | The catalog, indexes and a full health check | Planned |

The agent's rules are in `AGENTS.md` and `Schema/`. The commands they mention, such as `python3 scripts/wiki_tool.py build`, arrive in step 04. Until then the agent checks notes by hand against `Schema/lint-checklist.md`.

## Safety

- `.gitignore` keeps your window layout, plugin state, `Raw/Files/`, `Drafts/` and secret files (`.env`, `*.key`, `*.pem`) out of git.
- Never put passwords, tokens or keys in a note.
- If the repository is public, everything you commit can be read by anyone. Keep private sources out of it, or make the repository private.
