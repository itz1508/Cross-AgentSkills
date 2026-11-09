# Multi_Skills

A collection of **standalone reusable agent skills**, not a repository of workflow stages or application/runtime integrations.

All seven skill packages are under [`Agent/`](Agent/README.md):

| Skill | Description |
|---|---|
| [handoff](Agent/handoff/SKILL.md) | Transfer session context into an evidence-grounded, portable handoff |
| [cross-linker](Agent/cross-linker/SKILL.md) | Identify and classify relationships across existing records |
| [memory-bridge](Agent/memory-bridge/SKILL.md) | Compare memory and knowledge provenance |
| [session-search](Agent/session-search/SKILL.md) | Retrieve previous decisions from existing authorized sources |
| [wiki-build](Agent/wiki-build/SKILL.md) | Inspect and safely recover an existing wiki or knowledge index |
| [uix_designer](Agent/uix_designer/SKILL.md) | UI/UX design resources, tools, checks, and references |
| [video_generator](Agent/video_generator/SKILL.md) | Video production resources, tools, checks, and references |

**Boundary:** These skills are distributed independently; no Audit Discovery matrix, Research/Planning/Builder workflow role, Executor/Sandbox runtime package, or project-specific stage orchestration is included.

Source attributions and license notices are retained at [`Agent/SOURCES.md`](Agent/SOURCES.md) and [`Agent/LICENSE-AR9AV.txt`](Agent/LICENSE-AR9AV.txt). The handoff's historical example is not live project state.

Using a skill inside another repository requires that repository's own bootstrap and authorization checks. This source library does not claim executable Runtime or E2E integration.
