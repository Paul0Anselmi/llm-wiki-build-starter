---
tags:
  - "concept"
topics:
  - "[[LLM Wiki]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/why-llm-wiki]]"
source_count: 1
aliases: []
---

# Compiled Knowledge

## Summary

Compiled knowledge is knowledge an AI agent has already read, extracted and written into wiki pages, so it does not have to be worked out again from the raw documents each time a question is asked.

## Details

The source presents this as the core of [[Andrej Karpathy]]'s framing of the [[LLM Wiki]]:

- When a new source is added, the agent does not just index it for later search. It reads it, extracts the key information and integrates it into the existing wiki.
- Integrating means updating entity pages, revising summaries and noting where new information contradicts older claims.
- The knowledge is compiled once and then kept current, instead of being re-derived on every query as in [[Retrieval-Augmented Generation]].

## Related

- [[Knowledge Graph]]
- [[Agentic Vault]]
