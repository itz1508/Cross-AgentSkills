---
name: cross-linker
description: Inspect and propose typed links between existing knowledge, decisions, files, and evidence references. Use for provenance gaps, orphaned notes, superseded decisions, and deduplication; do not treat inferred links as verified evidence.
---

# Cross Linker

**Ownership:** Knowledge relationship analysis and optional authorized link editing. Does not own OneShot Runtime tracing, source contracts, stage approvals, or verification receipts.

## Discovery

Identify the target's existing note/index format (Obsidian wikilinks, Markdown, structured references, or another source registry). Read applicable repository rules. Do not assume a vault or create a second graph.

Collect only the relevant titles, stable IDs, aliases, tags, source links, and revision metadata. Read full page bodies only for plausible candidates, respecting privacy and access controls.

## Read-only link assessment (default)

1. Find exact references to an existing source ID, plan revision, transcript message, file, or other canonical identity.
2. Inspect candidate links from aliases, shared tags, or language similarity **separately** from exact identity links.
3. Assign relationship types only when directly justified by the source, for example `derived_from`, `replaces`, `contradicts`, `depends_on`, or `related_to`.
4. Use these evidence classes:
   - **Observed:** exact target exists and the original source explicitly supports the relation.
   - **Inferred:** plausible semantic or structural association that needs review.
   - **Ambiguous:** multiple targets or insufficient information; do not apply.
   - **Broken:** an existing link targets an inaccessible or missing record.
5. Detect duplicate, circular, contradictory, superseded, and orphan references without rewriting the original record.
6. Recommend only the smallest justified changes and include before/after examples. Do not infer a source's runtime permissions from relationships.

## Optional link edits

Only when the user explicitly authorizes edits to specific knowledge paths:

- Verify target existence, path ownership, and the current revision before editing.
- Preserve source text, frontmatter fields, archives, and already-curated links.
- Never link inside code blocks as a textual mutation. Avoid duplicate/self-links and unqualified generic terms.
- Keep inferred links visibly identified as suggestions unless separately confirmed.
- Validate link resolution and changed-file scope afterward. On conflict, stop rather than overwriting concurrent changes.

## Output

A bounded table of source ID, candidate target ID, relationship, observed/inferred/broken class, exact supporting excerpt, recommended action, and unresolved questions. For authorized edits, include actual changed paths and validation results.

## Boundaries

A relationship is not an independent test result, Build Admission, authorization, or trusted approval. The original record and its owning stage remain authoritative. No automatic memory writes or graph persistence without an accepted plan.

Related: [session-search](../session-search/SKILL.md) for locating original statements; [memory-bridge](../memory-bridge/SKILL.md) for cross-tool provenance; [provenance](../SOURCES.md).
