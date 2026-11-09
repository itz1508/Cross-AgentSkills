---
name: handoff
description: Create, validate, and resume evidence-grounded engineering handoffs across chat or agent sessions without treating summaries as repository authority.
version: 2.0.0
---

# Handoff — engineering session continuity

> Summary: Persist the minimum verified state needed for a new agent to resume the exact task without losing decisions, inventing evidence, or restarting completed planning.

## Trigger and ownership

Use when the user asks to hand off, resume, preserve session history, transfer context, or prepare a new chat/agent. This skill records context; it does **not** approve plans, perform builds, modify application source, or certify test results.

**Distribution path:** `Agent/skills/handoff/` in Multi_Skills. **Installed path:** `agent/skills/handoff/` in the target project. Work inside the *current verified checkout*, not an assumed Windows path. If the checkout is unavailable, produce a staged package and report that it has **not been installed in the target repository**.

## 01. Discover before writing

1. Locate the actual target repository, current branch and HEAD; distinguish a working tree, GitHub read-only view, and older artifacts.
2. Read `OneShot/bootstrap/START_HERE.md` or the repository's actual bootstrap entry point **when it exists and is accessible**. Read applicable `AGENTS.md`, contracts, current README, and existing handoff files.
3. Retrieve prior chat/project decisions only where needed; compare newer explicit decisions against older records. Never infer a missing decision.
4. Identify the immediate user request and approved scope. Do not resurrect rejected stages, reuse obsolete files as authority, or cross repository boundaries.
5. Before adding files, search for matching handoff files and reuse/update instead of duplicating.

## 02. Extract an evidence-backed handoff

Capture only durable information a successor needs:

1. **Authority:** active repo, branch, revision/checkpoint, bootstrap path and relevant contracts; mark unverified fields `NOT_VERIFIED`.
2. **Goal:** latest explicit user intent, acceptance criteria, excluded scope, and must-preserve decisions.
3. **State:** completed changes and exact file references; distinguish proposed, drafted, implemented, committed, pushed, and E2E-verified.
4. **Evidence:** tool commands and outcomes, exact test and build receipts, and links to artifacts. Record unsuccessful checks as failures or blocked.
5. **Open work:** blocker, impact, owning stage, next verifiable action; prioritize blockers of authorization, security, and source integrity.
6. **Resume instructions:** deterministic first actions for the next agent, including the precise task not to re-plan.
7. **Provenance:** timestamp with timezone, handoff author/source, and what was inaccessible.

For each consequential statement distinguish `VERIFIED`, `USER_REPORTED`, `DECIDED`, `PROPOSED`, or `NOT_VERIFIED`. A conversation summary is not a Build authorization receipt.

## 03. Write output

- Default file in the **target project**, not in this shared skill library: `agent/skills/handoff/CURRENT_HANDOFF.md`. Replace the latest current-state snapshot only when expressly updating it. Keep append-only execution/event history in the project's existing event log; do not overwrite it.
- Include a one-line summary first, then a timezone-aware timestamp, target revision, immediate objective, scope, verified state, pending blockers, and restart checklist.
- Do not duplicate substantial source or log content: reference canonical file paths and exact source commits instead.
- Exclude secrets, tokens, credentials, private email, personal data, and unnecessary raw chat transcripts. Use safe summaries or references.
- Keep the handoff concise and task-specific. When history is extensive, include a short chronological decision delta, not a transcript dump.
- Do not install dependencies or run external code just to produce a Markdown handoff.
- Never treat the example snapshot bundled with this shared skill as current evidence for a different repository.

## 04. Validate before claiming completion

1. Re-read the written file and check that paths, timestamps, status labels, and source revisions are internally consistent.
2. Check for conflicts between old and new decisions; mark unresolved conflicts explicitly.
3. Check that every claimed verification has an actual result. Never equate an agent claim, generated diagram, or synthetic test with real E2E evidence.
4. Check that no secrets or unapproved source modifications were introduced.
5. For a portable delivery, archive the directory preserving `agent/skills/handoff/`, open the archive, and confirm expected files exist.
6. Report **stored in checkout**, **staged in workspace**, or **not accessible** accurately. A local archive is not a Git commit or cross-session memory store.

## 05. Resume protocol for the next session

1. Read this skill and the target project's `CURRENT_HANDOFF.md` fully, if present.
2. Verify the actual repository/bootstrap/HEAD and compare them to recorded assumptions.
3. Ask only for an essential inaccessible input; otherwise continue the most recent user-assigned task.
4. Revalidate status and unresolved blockers before edits; honor ownership and approval boundaries.
5. At session end, refresh only the current handoff snapshot, preserving existing project execution logs and confirmed lessons in their established locations.

## Acceptance criteria

A fresh agent can identify (1) the current task, (2) what may be changed, (3) what is already complete, (4) what evidence exists, (5) what remains blocked, and (6) the next action **without access to the prior chat**. If any of these are unknown, label them rather than guessing.

## Origin

Rewritten from the `handoff` concept in https://github.com/mattpocock/skills; adapted for source-grounded OneShot/BreakDown continuity. Not a claim of compatibility testing with upstream CLI.
