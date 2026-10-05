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

This is the first step: `tutorial-00-empty-vault`. The vault is empty on purpose.

## What is here

- `Welcome.md`: this note.
- `.gitignore`: tells git which files to leave out of the history: your window layout and plugin state (they change every time you open Obsidian), large raw files, drafts, and anything secret such as passwords or keys.
- `.obsidian/`: Obsidian's own settings for this vault.

## What comes next

Step `tutorial-01-core-structure` adds the folders for raw sources, wiki notes and the rules the agent follows.
