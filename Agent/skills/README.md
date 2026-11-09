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

## BreakDown stage-skill distribution snapshots

The following are **code and instruction snapshots**, separate from the instruction-only knowledge skills above.

| Resource | Location | Responsibility |
|---|---|---|
| Auditor | [auditor/](auditor/SKILL.md) | Read-only codebase Audit Discovery |
| Researcher | [researcher/](researcher/SKILL.md) | Research adapter |
| Planner | [planner/](planner/SKILL.md) | Planning checks, review and gap analysis |
| Builder | [builder/](builder/SKILL.md) | Delegates authorized Build actions to the Host |
| CodeDesign | [code_design.py](code_design.py) | Planner-owned design-review questions |
| Executor | [executor/](executor/SKILL.md) | **Draft** provider-neutral Sandbox, optional Modal integration |

The first five resources were copied from `itz1508/BreakDown` `main` at `82979152109dff2b4424d222f38a442a307531ea`; Executor was copied from its unmerged `draft` branch at `ffbac6593ae148cf7d5d219b6f558605ed612712`. These modules import `agent.contracts` and `agent.runtime`; placing them here does **not** install, activate, authorize, or independently validate them in a consuming project. Preserve that project's existing Host, stage contracts and permission boundaries. See [SOURCES.md](SOURCES.md) for the complete provenance and exclusions.
