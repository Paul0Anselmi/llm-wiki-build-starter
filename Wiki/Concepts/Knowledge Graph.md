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

# Knowledge Graph

## Summary

A knowledge graph is a map of things and the named relationships between them. It is the structure behind an [[LLM Wiki]].

## Details

The source breaks it into three elements:

- **Node**: a thing, such as a person, idea, place or event.
- **Edge**: a named relationship between two nodes, such as "caused", "depends on" or "references".
- **Triple**: subject, relationship, object. Two nodes and one edge. This is the smallest unit of the graph.

A graph grows by adding triples that connect to existing ones, so its value compounds over time.

Familiar examples from the source:

- Google's knowledge panel, which answers a search from a map of related facts without the person clicking a link.
- Wikipedia, where each linked word is a node.
- A book, which the source calls a physical knowledge graph: the author decides the concepts and how they connect.

In [[Obsidian]], each note is a node and each link between notes is an edge. The source's point is that you do not set out to build the graph. It appears when you write specifically about how ideas relate.

After three years of note-taking, the source's author reports two benefits: finding connections between ideas that seemed unrelated, and discovering an older note on a "new" idea and continuing from it instead of starting over.

## Related

- [[Graph Retrieval-Augmented Generation]]
- [[Compiled Knowledge]]
