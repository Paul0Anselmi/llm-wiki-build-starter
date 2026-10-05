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
  - "RAG"
---

# Retrieval-Augmented Generation

## Summary

Retrieval-augmented generation (RAG) is how an AI tool usually searches your documents: it finds the pieces of text most similar to your question and answers from them.

## Details

As the source describes it, RAG:

1. converts your notes into numbers,
2. finds the ones most similar to the question,
3. retrieves those chunks of text.

It works well for simple questions of the "what is X" kind, where the answer sits in one or a few documents.

It struggles when the answer lives between documents, in how they relate to each other. The source compares the need to a reference librarian: someone who knows which books led to which and which ideas depend on one another.

## Related

- [[Graph Retrieval-Augmented Generation]]: the approach the source recommends for complex, connected information.
- [[Compiled Knowledge]]: the alternative to retrieving from raw documents on every question.
