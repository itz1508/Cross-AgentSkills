# Standalone agent skills

> Summary: Independent reusable skill packages. No workflow stages, project orchestration, host adapters, or Build/Audit/Planning runtime integrations are distributed here.

## Skills

| Standalone skill | Entry point | Purpose |
|---|---|---|
| Handoff | [handoff/SKILL.md](handoff/SKILL.md) | Prepare and resume a bounded session handoff |
| Cross Linker | [cross-linker/SKILL.md](cross-linker/SKILL.md) | Identify evidence-backed links and duplicate references |
| Memory Bridge | [memory-bridge/SKILL.md](memory-bridge/SKILL.md) | Compare provenance of existing records |
| Session Search | [session-search/SKILL.md](session-search/SKILL.md) | Retrieve original sessions and bounded source excerpts |
| Wiki Build | [wiki-build/SKILL.md](wiki-build/SKILL.md) | Inspect or explicitly authorized recovery of an existing knowledge store |
| UIX Designer | [uix_designer/SKILL.md](uix_designer/SKILL.md) | Independent UI/UX design reference data and tools |
| Video Generator | [video_generator/SKILL.md](video_generator/SKILL.md) | Video generation and editing resources |

## Boundaries

- Every skill has its own purpose and supporting files. None establishes a new workflow stage or grants approval, source-write, or Runtime privileges.
- Existing UIX and video Python source files are preserved as distributed. They reference dependencies from their consuming project; this repository does not independently install or verify those dependencies.
- The dated [handoff example](handoff/CURRENT_HANDOFF.md) is historical context, not the current state of any target repository.
- Before invoking a skill, inspect the actual target project's instructions, source, access permissions, and dependencies.
- The four wiki/tracing skills adapt upstream materials; see [source attribution](SOURCES.md) and [license](LICENSE-AR9AV.txt). Handoff records its source in its own SKILL.md.

Project workflow roles and Audit Discovery/Planner/Builder/Executor implementations belong in the *owning project*, not this standalone skill library.
