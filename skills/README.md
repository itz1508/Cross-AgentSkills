# Knowledge and tracing skills

**Summary:** Four independent source-grounded skills for finding session origins, comparing memory provenance, proposing knowledge links, and safely rebuilding an existing wiki. No OneShot Runtime ownership.

| Skill | Responsibility | Default behavior |
|---|---|---|
| [wiki-build](wiki-build/SKILL.md) | Archive, rebuild, restore an existing knowledge projection | Read-only inspection; destructive modes require explicit scoped authorization and verified recovery |
| [session-search](session-search/SKILL.md) | Retrieve specific original sessions and bounded excerpts | Read-only |
| [memory-bridge](memory-bridge/SKILL.md) | Compare knowledge provenance across tools/agents | Read-only |
| [cross-linker](cross-linker/SKILL.md) | Classify and propose exact or inferred links | Read-only; edits require explicit path authorization |

Each skill is a conventional `skills/<name>/SKILL.md` with YAML metadata and self-contained usage instructions. These are **agent-instruction skills**, not the repository's Python V2/R01 executable packages. No `run.py` adapter or Host connection has been created or tested.

Follow actual target repository instructions and verified source availability. Skills cannot confer agent history access, permissions, approval receipts, or execution evidence.

[Upstream attribution](SOURCES.md) · [Questions for later evaluation](QUESTIONS-FOR-LATER.md).
