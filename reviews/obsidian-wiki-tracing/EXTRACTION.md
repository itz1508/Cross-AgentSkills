# Tracing skills — source review and adaptation record

**Summary:** This directory is a rewritten, OneShot-scoped **read-only review package**. It does not install the upstream Obsidian Wiki system or expose destructive wiki operations.

## Provenance (observed source facts)

- Upstream repository: https://github.com/Ar9av/obsidian-wiki
- Inspected upstream commit: `acc0ac1769349c7550696724f564b0ca719e146c`.
- License: MIT, copyright (c) 2026 Ar9av; preserve [LICENSE](LICENSE).
- Original `wiki-rebuild` skill: `skills/wiki-rebuild/SKILL.md`, Git blob `a83e15574aa176256464fd0f85ce0c421d108577`.
- Other source files reviewed:
  - `skills/session-search/SKILL.md` — Git blob `6621cbed9f29b5c4a2a55bfad84a92688ecf7d0f`.
  - `skills/memory-bridge/SKILL.md` — Git blob `f1fb5f829a50974890030b2cddd643a1e81da2b2`.
  - `skills/cross-linker/SKILL.md` — Git blob `a5ed6a7448e40f852ea1132ac4945d0fb3f57c5d`.
  - `skills/llm-wiki/SKILL.md` — configuration and knowledge-store conventions.

Pinned originals:
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/wiki-rebuild/SKILL.md
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/session-search/SKILL.md
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/memory-bridge/SKILL.md
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/cross-linker/SKILL.md

## Source behavior versus adaptation

| Upstream capability | Actual prerequisite/behavior | OneShot review-only interpretation |
|---|---|---|
| `wiki-rebuild` | Configured `OBSIDIAN_VAULT_PATH`; archive, clear/rebuild, or restore; requires user confirmation for destructive actions | Not carried forward as a runnable skill. Evaluate its recovery principles only if a wiki exists. |
| `session-search` | Existing session-brain graph; `obsidian-wiki sessions-query`; transcript may be pruned | Evaluate whether existing OneShot sources can answer origin questions with exact identifiers. |
| `memory-bridge` | Wiki `.manifest.json` and pages with source provenance | Evaluate original source attribution; avoid introducing a duplicate manifest without a justified gap. |
| `cross-linker` | Obsidian page registry; may rewrite links and frontmatter | Evaluate **read-only** exact and inferred relationships; do not invoke its writer. |

## Differences from the previous push

The previous review folder contained a verbatim copy named `wiki-rebuild-SKILL.md`. That raw copy was not rewritten to OneShot's scope and was unsuitable for publication as a proposed Cross-Agent skill. This revision **removes it from the active tree** and adds [TRACE-REVIEW.md](TRACE-REVIEW.md), an original read-only evaluation procedure. The pinned upstream original remains accessible via the links above and prior Git history.

The [question bank](QUESTIONS-FOR-LATER.md) is also rewritten to require an observable evidence answer rather than imply that OneShot has missing services or needs new storage.

## Current verification boundary

- GitHub source contents and the Cross-AgentSkills repository layout were inspected.
- The adaptation is an authored review protocol, **not** a verified implementation or approved OneShot contract.
- No local OneShot checkout, bootstrap instructions, Runtime, logs, or live source history were available for integrated testing here.
- No wiki command, session history ingestion, repository refactor, or destructive action is authorized by this directory.
