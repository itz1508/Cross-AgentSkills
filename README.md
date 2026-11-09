# Cross-AgentSkills

Reusable agent instruction skills, BreakDown role distribution snapshots, and separate UIX/video resources.

The five knowledge/continuity skills live **directly under [Agent/](Agent/README.md)**:

| Skill | Path | Responsibility |
|---|---|---|
| Handoff | [Agent/handoff/](Agent/handoff/SKILL.md) | Session continuity |
| Session search | [Agent/session-search/](Agent/session-search/SKILL.md) | Historical source retrieval |
| Memory bridge | [Agent/memory-bridge/](Agent/memory-bridge/SKILL.md) | Knowledge provenance |
| Cross linker | [Agent/cross-linker/](Agent/cross-linker/SKILL.md) | Relationship analysis |
| Wiki build | [Agent/wiki-build/](Agent/wiki-build/SKILL.md) | Existing wiki/index recovery |

**Reusable read-only requirement list:** [Audit Discovery matrix](Agent/AUDIT_DISCOVERY_REQUIREMENTS.md). This documents the skills' independent ownership, shared evidence rules, source probes, missing/duplicate capabilities, and candidate CodeIntent. It does not create a duplicate Auditor or execute fixes.

Additional resources remain in their existing scopes:

- [BreakDown role skill snapshots](Agent/skills/README.md): Auditor, Researcher, Planner, Builder, CodeDesign and draft Executor. These are pinned source copies, **not** a completed Runtime integration.
- [UIX designer](Agent/uix_designer/SKILL.md): Python tools, checks, datasets, fonts and references.
- [Video generator](Agent/video_generator/SKILL.md): Python tools, checks and production references.
- [Upstream sources and licenses](Agent/skills/SOURCES.md) and [earlier evaluation questions](Agent/skills/QUESTIONS-FOR-LATER.md).

## Use in another repository

The shared distribution tree is not necessarily a Python import root. Consumers must inspect their own bootstrap, `AGENTS.md`, contracts and access restrictions before copying or installing resources.

In BreakDown, package examples reference `agent.skills.*`; these require the actual target repository and authorized Host-dispatch/Runtime contracts. Moving folders here does not authorize execution, build admission, or test receipts.

No connected OneShot/BreakDown E2E verification is claimed by this reference repository.
