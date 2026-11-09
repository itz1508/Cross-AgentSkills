# Upstream sources and adaptation record

**Summary:** These four instruction-only skills were rewritten for evidence-first knowledge management and tracing; they are not the upstream Obsidian Wiki implementation.

## Original source and license

Upstream project: https://github.com/Ar9av/obsidian-wiki  
Pinned reference commit: `acc0ac1769349c7550696724f564b0ca719e146c`  
License: MIT, Copyright (c) 2026 Ar9av. See [LICENSE-AR9AV.txt](LICENSE-AR9AV.txt).

| Adapted skill | Upstream source | Upstream Git blob |
|---|---|---|
| [wiki-build](wiki-build/SKILL.md) | `skills/wiki-rebuild/SKILL.md` | `a83e15574aa176256464fd0f85ce0c421d108577` |
| [session-search](session-search/SKILL.md) | `skills/session-search/SKILL.md` | `6621cbed9f29b5c4a2a55bfad84a92688ecf7d0f` |
| [memory-bridge](memory-bridge/SKILL.md) | `skills/memory-bridge/SKILL.md` | `f1fb5f829a50974890030b2cddd643a1e81da2b2` |
| [cross-linker](cross-linker/SKILL.md) | `skills/cross-linker/SKILL.md` | `a5ed6a7448e40f852ea1132ac4945d0fb3f57c5d` |

Also consulted: `skills/llm-wiki/SKILL.md` for original vault configuration and source-vs-index responsibilities.

## What changed

- Renamed the recovery-focused upstream `wiki-rebuild` adaptation to `wiki-build`, per Cross-AgentSkills organization. It retains archive/rebuild/restore semantics only when an actual knowledge store is configured and scoped.
- Replaced hard dependencies on the Obsidian CLI, vault paths, and QMD with **discovery of the target's existing interfaces**; an unavailable source is a blocker, not evidence of success.
- Converted the history search and provenance/mapping procedures into bounded source-grounded tasks; they do not manufacture memory or Runtime events.
- Made cross-link discovery read-only by default. Writes and destructive operations require explicit authorization and target-specific checks.
- No `run.py`, Host adapter, contract, database, index, service, or OneShot Runtime integration is asserted or generated. Existing `uix_designer` and `video_generator` packages remain separate.

## Attribution and verification limitations

The skills preserve their core concepts but are **adaptations**, not verbatim upstream copies. The pinned originals remain available under the corresponding source URLs. The text is reviewed for structural consistency; correct operation against a live OneShot repository, session store, or Obsidian vault is **not tested**.

These instructions do not authorize a new storage schema or change acceptance gates. Any executable adapter would require repository discovery, a Planner-owned implementation proposal, admission, and actual validation.
