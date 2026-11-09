---
name: wiki-build
description: Archive, rebuild, or restore an existing evidence-linked knowledge wiki with explicit scope, verified backups, and source provenance. Use only for a wiki or derived knowledge index, never for rebuilding application code.
---

# Wiki Build

**Ownership:** Recovery and reconstruction of an existing knowledge projection. Does not own OneShot source code, Runtime, task/event stores, planning, Build Admission, or validation receipts.

## Inputs and prerequisites

- A user-designated wiki/knowledge-store root and requested mode: `inspect`, `archive`, `rebuild`, or `restore`.
- Actual repository/vault instructions and configuration discovered from that target. Never assume an Obsidian vault, `OBSIDIAN_VAULT_PATH`, QMD, or another CLI is installed.
- A source inventory showing original documents, transcripts, manifests/indexes, archive locations, accessible revisions, and permissions.
- A recoverable archive destination outside the paths that would be cleared, with sufficient space and a documented retention rule.

If the target is a software repository or the goal is to clean/refactor application code, this skill is **out of scope**. Refer to the repository's existing audit/planning workflow; do not rename a code build as a wiki rebuild.

## Modes

### Inspect (default; read-only)

1. Read the actual store instructions, manifest/index if available, and source list. Record missing prerequisites as gaps.
2. Determine whether a rebuild is necessary; prefer search refresh, incremental ingestion, or deduplication where sufficient.
3. Inventory pages, source IDs, timestamps, index freshness, and known unrecoverable sources.
4. Present the intended actions and a recovery plan. **Do not mutate files.**

### Archive

Requires an explicit user request to archive the named store.

1. Bound the source and destination paths; exclude nested archives from recursive copies.
2. Create a timestamped snapshot containing the existing knowledge files, manifest, index metadata, and archive inventory.
3. Verify file counts, byte counts, and content hashes against the copied inventory; report exclusions and unverifiable entries.
4. Do not delete originals. Record the archive identifier and results in the store's established log, if authorized.

### Rebuild

Requires **separate explicit authorization for clearing/replacing the exact live target**, after a valid archive has been verified.

1. Confirm the selected archive, source inventory, target root, affected paths, and recovery procedure.
2. Perform a restore rehearsal to a **temporary** destination; compare the recovered inventory to the archive before modifying live content.
3. Stop if the archive, privileges, prerequisites, or confirmation are incomplete.
4. Preserve user configuration, original sources, archives, and unrelated project data. Never delete outside the explicitly scoped knowledge projection.
5. Rebuild only the authorized derived index/wiki content using the project's existing ingestion mechanism. Do not invent missing transcripts or regenerate source observations from a summary.
6. Reconcile records by stable source ID and revision; mark inaccessible/deleted inputs `unavailable`, not restored.
7. Verify new page/index integrity, links, source mappings, and known-source retrieval fixtures before reporting completion.

### Restore

Requires an explicit choice of archive and overwrite authorization.

1. Inspect archive metadata and verify the selected archive.
2. Archive the *current* live state and verify that pre-restore snapshot.
3. Rehearse restoration to a temporary location; verify hashes and source mappings.
4. Replace only approved live knowledge paths, respecting the target's own configuration/locking rules.
5. Verify the restored state with known pages and source queries; disclose any index refresh errors separately.

## Reporting

Report mode, exact target, archival identifiers, source inventory, mutation scope, observed verification results, unresolved gaps, and rollback procedure. Distinguish `archived`, `rebuilt`, `restored`, `blocked`, and `not tested` accurately.

## Safety and boundaries

- Never run a destructive operation from a vague "rebuild" request.
- Never assume a wiki summary or link authorizes OneShot Runtime operations.
- Never expose private transcripts or credentials into a public repository.
- QMD or another search index is *derived* data. An index refresh failure must not be represented as source loss.
- Prefer bounded, idempotent, approved changes; keep append-only correction history where the underlying store supports it.

Related capabilities: [session-search](../session-search/SKILL.md) retrieves history; [memory-bridge](../memory-bridge/SKILL.md) compares origins; [cross-linker](../cross-linker/SKILL.md) proposes relationships. [Provenance](../skills/SOURCES.md).

## Reusable Audit Discovery

For read-only evidence inventory, ownership/overlap checks and candidate CodeIntent, use the [Audit Discovery requirements matrix](../AUDIT_DISCOVERY_REQUIREMENTS.md). Do not execute this skill's write operations from Audit Discovery.
