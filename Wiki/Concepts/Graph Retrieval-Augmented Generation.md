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
aliases:
  - "Graph RAG"
  - "GraphRAG"
---

# Graph Retrieval-Augmented Generation

## Summary

Graph RAG is retrieval that follows the relationships in a [[Knowledge Graph]] instead of only fetching similar chunks of text.

## Details

- The source says that on larger, complex data sets graph RAG significantly outperforms standard [[Retrieval-Augmented Generation]].
- Instead of retrieving thousands of chunks and spending tokens on them, the AI follows the links between sources.
- Standard RAG is still fine for simple questions. Graph RAG pays off for complex or high-volume information spread across many sources.
- The source says a simple version can be built by hand with [[Obsidian]], a knowledge graph and the AI tools a person already uses. An [[LLM Wiki]] is that simple version.

## Related

- [[Compiled Knowledge]]
