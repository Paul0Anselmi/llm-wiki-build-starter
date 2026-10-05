# Welcome to llm-wiki-starter

This vault is the starting point for an **LLM wiki**: a knowledge base that an AI agent writes and maintains, and that you read and direct.

This is tutorial step `tutorial-01-core-structure`. Each step adds one small piece and is saved as its own git commit, so you can always see what changed and go back.

## What is here

- `Welcome.md`: this note.
- `.gitignore`: tells git which files to leave out, such as your window layout, plugin state, large raw files and anything secret.
- `.obsidian/`: Obsidian's own settings for this vault.
- `Raw/Sources/`: your source notes in Markdown (articles, transcripts, notes). The agent reads them but does not rewrite them.
- `Raw/Files/`: original files such as PDFs and images. Kept on your device only, not in git.
- `Wiki/`: the notes the agent compiles from your sources, split into `Topics/`, `Concepts/`, `Entities/`, `Projects/` and `Logs/`.
- `Schema/`: the rules the agent follows.
- `_templates/`: starting shapes for new notes.
- `.agents/skills/`: skills the agent uses inside this vault.
- `scripts/`: helper scripts and checks.
- `tutorial/`: notes about the tutorial steps.

Empty folders hold a hidden `.gitkeep` file, because git does not save empty folders.

## What comes next

The next step adds `AGENTS.md`, the schema files and the starter agent skills.
