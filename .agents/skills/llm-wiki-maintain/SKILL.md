---
name: llm-wiki-maintain
description: Rebuild the catalog and indexes, update the source manifest and run the maintenance gate before a commit. Use before committing wiki changes or when the person asks to tidy or rebuild the wiki.
---

# Maintain the wiki

1. Follow **Maintain the wiki** in `Schema/workflow-examples.md`.
2. After ingesting sources, also run `source-scan --update --accept-covered` and `source-lint`.
3. Do not commit if any check fails. Fix the cause or tell the person what is blocking.
