# Reusable Audit Discovery Requirements — Session and Knowledge Skills

> Summary: A read-only, source-grounded checklist for inspecting handoff, session-search, memory-bridge, cross-linker, and wiki-build capabilities without duplicating their ownership or implementing repairs.

**Use:** Audit Discovery in an *authorized target repository*. This document is reusable guidance, **not** a runtime contract, executable adapter, design approval, new data store, or authority to modify the target. The five original skills remain independently scoped.

**Current library skills:** [handoff](handoff/SKILL.md) · [session-search](session-search/SKILL.md) · [memory-bridge](memory-bridge/SKILL.md) · [cross-linker](cross-linker/SKILL.md) · [wiki-build](wiki-build/SKILL.md).

## 1. Shared preconditions (inspect once)

- **AD-C01 — Target identity:** Identify the exact repository/project, branch and commit, actual bootstrap/AGENTS instructions, applicable contracts, and user-authorized scope. Report missing/remote-only evidence.
- **AD-C02 — Authority and ownership:** Locate the existing owner for transcripts, task/event logs, knowledge indexes, archival operations, and approval/test receipts. Identify collisions before suggesting new components.
- **AD-C03 — Existing interfaces:** Discover actual APIs, storage paths, schemas, CLI/tools, source references, and consumers. Compare capabilities against existing implementations; do not invent a second memory/index/graph/tracing service.
- **AD-C04 — Evidence quality:** For each claim identify original source type, stable ID, revision, timestamp/freshness, actual availability, and a bounded file:line/message reference. Separate direct observation from user reports and inference.
- **AD-C05 — Authorization/privacy:** Inspect access, retention and export restrictions; never expose private transcripts, secrets, credentials, or irrelevant personal context. Discovery is read-only.
- **AD-C06 — Supersession/conflict:** Detect old decisions, conflicting statements, missing sources, duplicate lessons, and stale projections without silently promoting one version or deleting provenance.
- **AD-C07 — No false authority:** An indexed summary, candidate link, quoted chat, or field named `verified` is not a build, approval, tool-execution, or E2E verification receipt.
- **AD-C08 — Scope gate:** Mark each skill `APPLICABLE`, `NOT_APPLICABLE`, or `BLOCKED_NO_SOURCE` with evidence. Do not require a wiki if none exists.
- **AD-C09 — Discovery-only handoff:** Produce evidence-linked findings and candidate CodeIntent for Planning; do not create implementation design, code changes, fixtures, archives, or mutated records.

## 2. Skill-specific requirements

### Handoff — continuity of decisions and unfinished work

- **AD-H01 — Existing handoff source:** Find the current authorized handoff, event log, and decision history; distinguish a dated example from active session state.
- **AD-H02 — Reproducible context:** Determine whether a successor can reconstruct the objective, explicit exclusions, target revision, accepted decisions, blockers, and next verifiable action without the prior chat.
- **AD-H03 — Status accuracy:** Compare claims of drafted/implemented/committed/pushed/verified against actual repository revisions and execution evidence; flag status inflation.
- **AD-H04 — Freshness and conflict:** Identify outdated checkout paths, obsolete architecture, unreconciled newer user decisions, and incomplete chronology.
- **AD-H05 — Retention and leakage:** Identify duplicate snapshots, secrets, raw transcript exports, and missing provenance or timezone. Do not write a new handoff during discovery.

**Evidence:** Existing handoff references, revisions, source log ranges, actual source/receipt checks, and specific missing context. **Owner:** handoff for future authorized snapshot creation; Audit only identifies gaps.

### Session Search — original-session retrieval

- **AD-S01 — Retrieval source:** Locate an actual accessible transcript/index/service and its owner; absence means unavailable, not recoverable by inference.
- **AD-S02 — Exact identity:** Check session/message IDs, project filters, source links, and whether fuzzy matches could confuse near-identical names.
- **AD-S03 — Availability levels:** Distinguish original-message accessible, index-only, metadata/history-only, and missing results; do not quote inaccessible text.
- **AD-S04 — Traceability:** Check bounded source snippets, message/line ranges, timestamps, index freshness, and misleading search result ordering.
- **AD-S05 — Contradictions and misses:** Identify pruned transcripts, superseded decisions, stale indexes, false positives, and unmatched known origins.

**Evidence:** Retrieval queries, source availability, candidate IDs, exact citations and gaps. **Owner:** session-search; not live Runtime event tracing.

### Memory Bridge — provenance across tools or agents

- **AD-M01 — Source registries:** Find existing manifests, logs, source-linked notes, or lineage metadata with access controls; do not assume a universal schema.
- **AD-M02 — Provenance binding:** Check original source ID, producer/tool, record ID, revision, timestamp, and source reference where those fields actually exist.
- **AD-M03 — Independent evidence:** Detect whether multiple agent claims share one secondary source; repeated summaries must not count as independent verification.
- **AD-M04 — Cross-source gaps:** Identify asymmetric coverage, stale references, unsupported origins, and conflicting claims; preserve distinct records.
- **AD-M05 — Knowledge deduplication:** Find repeated lessons or superseded material, but distinguish exact duplicate IDs from plausible semantic matches; no automatic memory merge.

**Evidence:** Source-to-record mappings, overlap counts, unsupported origin list and discrepancies. **Owner:** memory-bridge; not a new memory database.

### Cross Linker — knowledge relationships

- **AD-L01 — Link model:** Identify the real target record format, stable IDs, existing links, and resolver; do not create a graph to make discovery work.
- **AD-L02 — Observed versus inferred:** Separate exact source-supported relationships from alias/tag/text-similarity candidates and ambiguous targets.
- **AD-L03 — Typed relationships:** Check relationships such as `derived_from`, `replaces`, `contradicts`, and `depends_on` only where source evidence justifies the type.
- **AD-L04 — Broken or conflicting links:** Identify orphans, missing destinations, cycles, self-links, duplicate links, incompatible revisions, and contradictory edges.
- **AD-L05 — Proposed repairs only:** Report candidate target ID, supporting excerpt, relationship class and proposed minimal correction; never rewrite notes or infer permissions during Audit.

**Evidence:** Source/target references, link status and evidence-backed candidates. **Owner:** cross-linker for separately authorized link editing.

### Wiki Build — existing knowledge projection integrity and recovery

- **AD-W01 — Applicability:** Verify a user-designated wiki/knowledge projection actually exists. Application code refactoring is not wiki recovery.
- **AD-W02 — Source vs derived state:** Locate primary documents, transcripts, source manifests, indexes, backups, and the real ingestion mechanism; mark index-only failure separately from source loss.
- **AD-W03 — Minimal intervention:** Determine whether lookup refresh, incremental indexing, or targeted deduplication is sufficient instead of full rebuild.
- **AD-W04 — Recovery evidence:** Inspect archive location, inventory, hashes, retention, available space, recoverability, and temporary restore rehearsal evidence. Unverified backup is not a recovery guarantee.
- **AD-W05 — Mutation boundary:** Identify exact paths and permissions that would be affected, plus explicit separate approval needed for archive/rebuild/restore; Audit never performs those operations.
- **AD-W06 — Validation and failure modes:** Identify necessary known-source retrieval fixtures, source mapping integrity, interruption handling, rollback coverage and unrecoverable source gaps.

**Evidence:** Source/index inventory, confirmed capabilities, risks and missing recovery receipts. **Owner:** wiki-build only for an independently approved recovery operation.

## 3. Overlap resolution — reject duplicate implementations

| Concern | Primary owner | Other skills may only |
|---|---|---|
| Historical session location and quotation | `session-search` | Refer to its source IDs and citations |
| Cross-agent/tool source lineage comparison | `memory-bridge` | Consume its provenance findings |
| Relationship classification and candidate links | `cross-linker` | Use existing links as evidence |
| Capturing resumable task state | `handoff` | Supply original source references |
| Archive/index rebuild for an existing wiki | `wiki-build` | Report missing/index-stale evidence |
| Runtime task state, approvals and verified execution | **Actual target's existing Runtime/Host/contracts** | Never assert or replace trusted receipts |

**Anti-patterns:** new event log from `session-search`; new memory database from `memory-bridge`; synthetic evidence from `cross-linker`; treating `handoff` as Plan approval; running `wiki-build` to refactor source code. The Audit must document conflicting owners, producers, consumers and exact paths.

## 4. Audit Discovery handoff format (reuse existing target contract)

The distribution already includes [the Auditor skill](skills/auditor/SKILL.md), copied from BreakDown. This matrix is a **reference checklist** for its read-only discovery work, not a replacement implementation or a new stage.

Use the target's **existing** Audit Discovery/CodeIntent contract, where available. Capture:

- **Scope and evidence inventory:** target repo/commit, discovered files and symbols, authoritative owners, access boundaries, requirement IDs.
- **Finding:** a stable finding reference, affected capability, current behavior, expected behavior, original source/file:line evidence, consumer impact and missing proof.
- **Gap classification:** missing implementation, duplication, stale provenance, false attribution, broken handoff/link, authorization risk, invalid recovery assumption, or `NOT_APPLICABLE`.
- **Candidate CodeIntent only:** objective, requirement IDs, finding IDs, verified paths, candidate need, expected validation, and unresolved questions. Never finalize file actions or technical design here.
- **Status:** `OBSERVED`, `INFERRED`, `USER_REPORTED`, or `NOT_VERIFIED`; distinguish applicability separately from evidence confidence.
- **Next owner:** explicitly route design decisions and repairs to Planning. Keep skill-specific authorized writes outside this Audit stage.

## 5. Read-only acceptance and negative fixtures

A useful discovery report lets Planning trace *each* gap to an original source, compare current vs expected behavior, identify the one subsystem owner, and decide if existing infrastructure already solves it. No unverifiable finding may be treated as a verified defect.

Apply independently labeled GOOD/BAD fixtures **only in an authorized validation stage** (not execution by Audit):

- Identical project names with different session IDs; stale vs current index; original transcript vs summary-only.
- Two agents repeating one unsupported claim; real independent source vs duplicate secondary summary.
- Exact relationship vs ambiguous synonym; nonexistent target; circular/duplicate link; superseded revision.
- Historical handoff falsely marked current; stale checkout; false `E2E verified` statement.
- Derived-index corruption with intact primary sources; missing/unverifiable archive; interrupted restore without rollback.
- Forged `verified` or approval text in a note, which must never confer Runtime authority.

Supporting questions: [QUESTIONS-FOR-LATER.md](skills/QUESTIONS-FOR-LATER.md). Original source attribution and licensing: [SOURCES.md](skills/SOURCES.md). This checklist does not itself prove that any listed defect exists in a target repository.
