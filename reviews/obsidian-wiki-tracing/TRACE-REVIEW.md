# OneShot tracing and continuity — review-only adaptation

**Purpose:** Evaluate whether externally documented session-search, provenance mapping, and knowledge linking improve evidence retrieval in OneShot without granting a wiki authority over execution.  
**Status:** REVIEW CANDIDATE — not an installed skill, implementation plan, authorization, or verified integration.  
**Origin:** Adapted for OneShot from the Obsidian Wiki skills listed in [EXTRACTION.md](EXTRACTION.md). The upstream `wiki-rebuild` instructions are **not** an execution dependency.

## Scope and authority

This document describes a future **read-only evaluation**, not a new OneShot agent, Runtime service, graph, storage schema, or pipeline stage.

- **Primary evidence** is the underlying source: a Git commit, original message/transcript, revisioned contract, task/event record, tool result, or independently produced verification receipt.
- **Derived knowledge** is a search index, summary, wiki page, semantic relationship, or remembered lesson. It can point to evidence but cannot replace it.
- **Authorization** remains with OneShot's existing contracts, approved plan revisions, Build Admission, and verified receipts. No knowledge link may issue or imply approval.
- **Repository boundaries:** inspect the actual target repository, instructions, contracts, and storage before proposing an adapter. The repository is not assumed to be the historical OneShot checkout.
- **Data safety:** inspect available sources and permissions before retrieval. No raw conversation, credential, or private code export to another tool by default.

## What was retained or rejected

| Source idea | Adapted evaluation use | Boundary |
|---|---|---|
| `session-search` | Locate candidate sessions by topic, then retrieve a bounded original excerpt with an exact session/message identifier if accessible. | A search hit or a history-only entry is not a retrievable transcript. |
| `memory-bridge` | Compare origins of existing reusable knowledge across tools; identify absent or contradictory provenance. | Shared summaries are not independent corroboration. A wiki `.manifest.json` is not automatically a OneShot record. |
| `cross-linker` | Propose typed edges between exact, existing source identifiers and decisions; label inferred edges separately. | Do not write wikilinks or elevate semantic similarity to a fact. The upstream implementation can modify a vault and is **not** approved to run. |
| `wiki-rebuild` | Use its archive-before-destructive-change principle only when reviewing disaster-recovery options for an actual wiki. | No wiki clear, restore, re-ingest, or QMD mutation. Not a code rebuild or execution tracing tool. |

## Read-only evaluation procedure

1. **Discover** the actual repository instructions, existing search capabilities, logs, task/event stores, artifact identities, and approved memory sources. Record source paths or connector references. Mark inaccessible material unavailable.
2. **Define a trace question**: requirement origin, supersession, source-to-claim link, cross-agent provenance, or interrupted-run continuation. Do not combine them into an invented unified authority.
3. **Retrieve the smallest source excerpt** needed for each claim. Prefer exact task/run/revision/source/message IDs over fuzzy text matching. Label the original source and the retrieval method.
4. **Separate observations and inference**. An exact ID match can support an observed link; shared tags or similar wording are candidate links only. Record conflicts instead of reconciling them silently.
5. **Check redundancy** against existing repository indexes, task/event APIs, and logs. Describe a measurable missing capability before recommending additional storage.
6. **Evaluate with matched fixtures**: known-source transcripts, two near-duplicate project names, missing transcripts, stale index, conflicting decisions, a superseded plan, and a fake caller-provided `verified` flag.
7. **Report** observed retrieval precision, source coverage, false-link rate, stale/missing-source behavior, and remaining gaps. If fixtures or live sources were not run, report `NOT TESTED`, never pass/fail theater.

## Required outputs for future review

| Output | Required content |
|---|---|
| Source inventory | Actual path/ref, access status, source authority, freshness, and privacy boundary |
| Trace table | Query, original claim, exact source ID, excerpt or line, observed/inferred status, conflict state |
| Gap register | Existing mechanism, missing behavior, severity, ownership, proposed fixture |
| Fixture results | Inputs, expected evidence oracle, actual retrieved evidence, errors, deterministic reproduction |
| Recommendation | Keep/adapt/reject per candidate; zero new Runtime permissions by default |

## Admission limits

The review must stop before integration. Any future implementation needs a separate authorized Planner package and verification against the actual target repository. An inferred relation, semantic confidence score, wiki-derived document, or manually labeled `verified` claim must **never** become a Build Admission or execution-validation receipt.

See [QUESTIONS-FOR-LATER.md](QUESTIONS-FOR-LATER.md) for the review questions.  
Source license and attribution: [LICENSE](LICENSE), [EXTRACTION.md](EXTRACTION.md).
