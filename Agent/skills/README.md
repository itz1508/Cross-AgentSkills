# Knowledge, tracing, and continuity skills

**Summary:** Five individually scoped agent-instruction skills. These do not create Runtime events, approval receipts, or shared storage.

| Skill | Responsibility | Default behavior |
|---|---|---|
| [wiki-build](wiki-build/SKILL.md) | Archive, rebuild, restore an existing knowledge projection | Read-only inspection; destructive modes require scoped authorization and recovery checks |
| [session-search](session-search/SKILL.md) | Retrieve original sessions and bounded excerpts | Read-only |
| [memory-bridge](memory-bridge/SKILL.md) | Compare knowledge provenance across agents and tools | Read-only |
| [cross-linker](cross-linker/SKILL.md) | Classify and propose exact or inferred links | Read-only; edits require explicit path authorization |
| [handoff](handoff/SKILL.md) | Record and resume a source-grounded engineering session | Writes an authorized handoff file in the *target project*; does not modify application source |

Each skill uses `skills/<name>/SKILL.md` with self-contained instructions. These are not the target project's Python V2/R01 executable packages. No Host connection or executable adapter for these Markdown skills has been tested.

[Upstream attribution for the four wiki/tracing adaptations](SOURCES.md). The handoff skill's source is documented in its own `SKILL.md`. [Questions for later evaluation](QUESTIONS-FOR-LATER.md).
