# Cross-AgentSkills

Shared skill library for OneShot agents — video generation and UIX design.

## Skills

| Skill | Path | Purpose |
|---|---|---|
| `video_generator` | `video_generator/` | 40+ AI video models via `belt` CLI (Veo 3.1, Seedance 2.0, HappyHorse, Wan, Grok, OmniHuman, Fabric). text-to-video, image-to-video, avatar, edit, upscale, foley |
| `uix_designer` | `uix_designer/` | Unified UI/UX: `ui-ux-pro-max` (80 styles, 192 palettes, 74 font pairings, 120 UX guidelines) + `canvas-design` (philosophy→.pdf/.png) + `web-design-guidelines` (Vercel audit) — single owner per capability, no overlap |

## Knowledge and tracing skills

Four individually scoped instruction skills are available under [`skills/`](skills/README.md): [`wiki-build`](skills/wiki-build/SKILL.md), [`session-search`](skills/session-search/SKILL.md), [`memory-bridge`](skills/memory-bridge/SKILL.md), and [`cross-linker`](skills/cross-linker/SKILL.md).

These are agent-instruction skills and **not** Python V2/R01 runtime packages. They do not create Runtime events, approval receipts, or additional storage. See [the evaluation questions](skills/QUESTIONS-FOR-LATER.md) before any integration.

## Structure (same as `breakdown/agent/skills/`)

Executable Python packages (`uix_designer` and `video_generator`) follow the V2/R01 rule:
```
<skill>/
 ├─ __init__.py, run.py (from __future__ top, pre/post_dispatch), SKILL.md
 ├─ tools/     # permitted ops (belt calls, search, canvas, web fetch)
 ├─ checks/    # validation (prompt, duration, guideline)
 └─ references/# docs, data, fonts (e.g., ui-ux-data/, canvas-fonts/)
```

See `uix_designer/references/overlap-map.md` for overlap resolution.

## Usage

```bash
# Video generation
belt login
belt app run google/veo-3-1-fast --input '{"prompt":"drone over forest"}'
uv run python -m agent.skills.video_generator.run D:/breakdown

# UIX design
uv run python agent/skills/uix_designer/tools/search.py "keyboard focus modal" --domain ux --design-system -p "MyApp"
```

## Verification

- `ruff check`, `mypy` pass (tools excluded for strict)
- `gap_analysis --repo .` → `valid` in source `breakdown` (source_id `b643176`)

## Source

Built from `D:/breakdown` R01 + gap fixes, extracted 2026-11-08.
