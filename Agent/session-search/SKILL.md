---
name: session-search
description: Retrieve and cite earlier agent sessions or decisions from accessible transcripts or existing session indexes. Use for questions about when, where, or why work happened; do not treat indexed summaries as original evidence.
---

# Session Search

**Ownership:** Read-only historical session retrieval. Not a session collector, event logger, wiki builder, or Runtime execution tracer.

## Prerequisites

Discover the **existing** authorized history source: a repository session index, transcript directory, connected history service, or other user-authorized store. Read source instructions and permissions first. No accessible source means **unavailable**, not reconstructed history.

Do not create a new database, crawl unrelated devices, or infer that connected agents have access to one another's private transcripts.

## Procedure

1. Restate the retrieval target precisely: project, requirement, decision, file, stage, timeframe, or session ID.
2. Prefer exact IDs and filters. Use the existing search interface for candidate sessions; semantic similarity is a ranking signal only.
3. For each result, inspect source type, last indexed timestamp, transcript path or URI, and whether full content is still loadable.
4. Distinguish:
   - `source-verified`: the original transcript/message was opened and the relevant excerpt is present.
   - `index-only`: a candidate matching index entry exists but the source was not opened.
   - `history-only`: index metadata remains but the transcript is known to be pruned or inaccessible.
   - `missing`: no supported matching source.
5. Load only bounded sections needed to answer the question; do not print whole logs or expose secrets.
6. Compare contradictory or superseded statements by timestamp and source revision. Do not silently choose the latest search hit as canonical.
7. Cite the exact accessible source ID and message/line range. If only an index entry remains, explicitly state that full original evidence is unavailable.

## Output

Return the matched session IDs, query scope, source type and availability, relevant excerpt with reference, freshness uncertainty, contradictions, and confidence *basis* (not a made-up probability).

## Test cases before automation

Use labeled fixtures with near-identical project names, renamed files, repeated requirements, pruned transcripts, stale indexes, and contradictory revisions. Compare known origins to actual returned IDs and report false positives and omissions.

## Boundaries

- No new event tracing schema, memory store, auto-ingestion, or Build Admission.
- Session text is historical evidence of a statement, **not** evidence that a command ran or a test passed unless independent execution evidence supports it.
- If the session index needs reconstruction, refer to [wiki-build](../wiki-build/SKILL.md) only when that index is part of an actual managed wiki; do not invoke a destructive operation automatically.

Related: [memory-bridge](../memory-bridge/SKILL.md) for origin comparisons, [provenance](../skills/SOURCES.md).

## Reusable Audit Discovery

For read-only evidence inventory, ownership/overlap checks and candidate CodeIntent, use the [Audit Discovery requirements matrix](../AUDIT_DISCOVERY_REQUIREMENTS.md). Do not execute this skill's write operations from Audit Discovery.
