---
tags:
  - "topic"
topics: []
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/why-llm-wiki]]"
source_count: 1
aliases:
  - "Shared brain"
---

# LLM Wiki

## Overview

An LLM wiki is a structured, interlinked set of Markdown notes that an AI agent builds and keeps up to date from raw sources. It sits between the person and the sources, so every AI tool the person uses can read the same knowledge instead of each tool keeping its own separate memory.

The source describes three layers:

1. **Raw sources**: articles and research clipped into the vault, for example with the [[Obsidian]] Web Clipper. They stay untouched.
2. **The wiki**: an agent reads the sources and compiles them into clean, linked pages. It is a [[Knowledge Graph]] written in plain language.
3. **Maintenance**: the agent periodically checks the wiki for contradictions, outdated information and orphan pages.

The idea became popular through a post by [[Andrej Karpathy]], but the source says it builds on years of knowledge graph research.

## Key notes

- [[Knowledge Graph]]: the structure behind the wiki.
- [[Compiled Knowledge]]: why the wiki is written once and kept current.
- [[Retrieval-Augmented Generation]]: how AI tools usually search documents.
- [[Graph Retrieval-Augmented Generation]]: retrieval that follows relationships.
- [[Agentic Vault]]: keeping the AI's wiki apart from your own notes.
- [[Obsidian]], [[Andrej Karpathy]], [[Wanderloots]]: the tool and people mentioned.

## Open questions

- How to set up an LLM wiki from scratch, firewall it from other vaults and share it between several agents. The source leaves these for a follow-up video.
