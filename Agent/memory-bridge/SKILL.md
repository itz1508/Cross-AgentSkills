---
name: memory-bridge
description: Compare provenance of existing knowledge records across agents and tools, identify missing sources or contradictory claims, and report cross-agent knowledge gaps without copying or inventing memory.
---

# Memory Bridge

**Ownership:** Read-only provenance comparison of knowledge already indexed or recorded. Does not transfer ChatGPT memory, scrape agent internals, create a shared memory database, or certify execution.

## Preconditions

1. Locate the exact existing source registry, wiki manifest, page frontmatter, or source-linked records **in the authorized project**.
2. Identify each registry's source identity, tool/agent origin, original evidence reference, timestamps, and page/lesson update relation.
3. If a registry is missing or incomplete, record that limitation. Never manufacture a generic manifest to make this skill run.
4. Confirm access and retention rules before reading any personal conversation or private code record.

## Supported operations

- **Browse:** Which knowledge records have attributed origins from one named agent/tool?
- **Search:** Which source-backed records from that tool address a specified topic?
- **Diff:** Which records appear only in one tool's source projection, only in another, or are shared?
- **Map:** For each record, show which exact source references associate it with each tool.

Operate on stable IDs. When only labels or summaries exist, report a candidate match rather than falsely merging records. Do not assume two agents independently verified something just because the same text appears twice.

## Procedure

1. Read the smallest required source registry slice and check freshness.
2. Extract explicit `source_id`, `producer`/`tool`, `record_id`, `revision`, and `source_ref` **only when those fields actually exist**; document source-specific mappings rather than inventing a universal schema.
3. Build an ephemeral set/index in the evaluation context; do not persist another copy without a separate accepted design.
4. Resolve each displayed record to its source when available. Mark unsupported origin as `unknown`.
5. Report overlap, asymmetry, stale references, duplicates, and contradictions. Preserve different observations even when they disagree.
6. Where an existing authoritative log or contract answers the question, report it as the primary source; do not elevate derived wiki knowledge over it.

## Output

A count-based provenance table with source references, distinct/shared record counts, unverifiable links, timestamps/freshness, and evidence gaps. Label all derived judgments as observations or inferences.

## Validation

Use matched, independently labeled fixtures: shared secondary summary, genuinely independent source, missing origin, invalid source ID, superseded decision, duplicate lesson, and a forged `verified` attribute. The forged value must not become an execution receipt.

## Boundaries

Only existing knowledge sources are compared. No cross-agent broadcast, session ingestion, user-data export, or Runtime mutation is authorized. Use [session-search](../session-search/SKILL.md) to locate original messages and [cross-linker](../cross-linker/SKILL.md) to analyze relationships.

[Provenance](../skills/SOURCES.md).

## Reusable Audit Discovery

For read-only evidence inventory, ownership/overlap checks and candidate CodeIntent, use the [Audit Discovery requirements matrix](../AUDIT_DISCOVERY_REQUIREMENTS.md). Do not execute this skill's write operations from Audit Discovery.
