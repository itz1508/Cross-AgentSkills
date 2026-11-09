# UIX Designer Skill

## Purpose
Unified UI/UX design intelligence — merges **ui-ux-pro-max** (80 styles, 192 palettes, 74 font pairings, 120 UX guidelines), **canvas-design** (visual philosophy + canvas rendering), and **web-design-guidelines** (Vercel a11y/perf checks) without overlap.

## Entry Point
```bash
uv run --no-sync python -m agent.skills.uix_designer.run <repository-root>
# UI/UX search:
uv run python agent/skills/uix_designer/tools/search.py "keyboard focus modal" --domain ux
# Canvas:
# -> Generates philosophy .md + art .pdf/.png via canvas-design
# Web guidelines:
curl https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

## Tools
- `search` — Query ui-ux-pro-max local DB (styles, palettes, typography, charts) via `tools/search.py`
- `design_system` — Generate design system via `tools/design_system.py --design-system -p "<project>"`
- `canvas_philosophy` — Create visual philosophy (art movement) → render via canvas-design
- `canvas_render` — Express philosophy to .pdf/.png (from canvas-design)
- `web_guidelines` — Fetch Vercel guidelines and audit `file:line` findings
- `validate_data` — Validate ui-ux CSV data integrity

## Output
- Design system dict/markdown/json + philosophy .md + canvas .pdf/.png
- `ArtifactRef` with `uix_record` contract
- Disposition: `completed` / `blocked` (missing data) / `not_valid` (a11y fail)

## Ownership (No Overlap)
| Capability | Owner in uix_designer | Upstream Source | Not Owned |
|---|---|---|---|
| Tokens, palettes, styles, typography, charts | `tools/search.py` + `tools/design_system.py` | ui-ux-pro-max | Guideline validation |
| Canvas philosophy + rendering | `tools/canvas_*` | canvas-design | Web UI code |
| Web a11y/perf/responsive audit | `checks/guideline.py` + `tools/web_guidelines.py` | web-design-guidelines | Token generation |
| Data validation | `tools/validate_data.py` | ui-ux-pro-max | Canvas fonts |

All three sources documented in `references/`; single tool owns each capability.

## Responsibilities
- Search local UI/UX DB before designing (priority 1-10 table in SKILL.md)
- Generate design system with project intent + stack detection
- Create canvas philosophy (4-6 paragraphs, craftsmanship emphasis) then render
- Audit web UI via fetched guidelines, output `file:line` terse findings

## Runtime Integration
- Reports via `HostDispatchResult` (`uix_record`)
- Never issues receipts; host validates digests
- Default deny for outbound fetches (web guidelines, canvas fonts)

## Constraints
- No fabricated 0-result searches — fallback to priority table with explicit note
- Canvas fonts from `references/canvas-fonts/` only; no emoji as icons
- Web guidelines always fetched fresh from Vercel URL, never cached stale
- Max 5 terms per search query; auto-detect domain, pass `--domain` if misrouted
