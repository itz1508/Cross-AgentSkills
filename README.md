# Cross-AgentSkills

Reusable agent skills, UIX design, and video generation resources.

All shared agent resources live under [`Agent/`](Agent/):

| Resource | Location | Scope |
|---|---|---|
| Knowledge and tracing skills | [`Agent/skills/`](Agent/skills/README.md) | Session search, provenance, cross-linking, wiki recovery, and session handoff |
| UIX designer | [`Agent/uix_designer/`](Agent/uix_designer/SKILL.md) | UI/UX design references, validation, data, and tools |
| Video generator | [`Agent/video_generator/`](Agent/video_generator/SKILL.md) | Video generation, editing, avatar, foley, and related tools |

## Skill entry points

- [Handoff](Agent/skills/handoff/SKILL.md) — durable session continuity. Its [dated BreakDown example](Agent/skills/handoff/CURRENT_HANDOFF.md) is historical, not the current state of this repository.
- [Wiki build](Agent/skills/wiki-build/SKILL.md) — safe existing-wiki recovery.
- [Session search](Agent/skills/session-search/SKILL.md) — source-bounded session retrieval.
- [Memory bridge](Agent/skills/memory-bridge/SKILL.md) — provenance comparison.
- [Cross-linker](Agent/skills/cross-linker/SKILL.md) — evidence-backed knowledge links.

## Distribution versus installed paths

This repository organizes resources under `Agent/`. A consuming OneShot/BreakDown project may install a package under its own `agent/skills/`, if that project's bootstrap and contracts authorize it. **Renaming repository paths does not install an adapter or verify Runtime compatibility.**

The UIX and video Python packages are moved without changing their contents; their existing docs show target-project commands such as:

```bash
uv run --no-sync python -m agent.skills.uix_designer.run <repository-root>
uv run --no-sync python -m agent.skills.video_generator.run <repository-root>
```

Those commands require the consumer project's `agent.skills` Python package and contracts; they are **not** standalone launch commands from this repository root. Data, fonts, and references remain inside their respective packages.

## Ownership and validation

Knowledge/tracing/handoff documents do not grant Runtime authorization, source access, approval receipts, or E2E evidence. See [knowledge evaluation questions](Agent/skills/QUESTIONS-FOR-LATER.md) and [source attributions](Agent/skills/SOURCES.md).

This reorganization retains existing UIX/video byte content and moves resource paths. No connected OneShot/BreakDown build or hosted inference E2E is asserted.

## BreakDown stage skills

Current BreakDown stage skills are distributed under [`Agent/skills/`](Agent/skills/README.md): Audit Discovery, Research, Planning, Builder, and CodeDesign review. An additional [Executor/Sandbox](Agent/skills/executor/SKILL.md) snapshot comes from an **unmerged draft branch**. See [pinned source revisions](Agent/skills/SOURCES.md).

These are source copies, not installed or independently validated Runtime roles. The existing handoff, wiki/tracing, UIX, and video resources remain in place.
