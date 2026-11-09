# Overlap Map — No Duplication

| Capability | Owner | Upstream | Reason |
|---|---|---|---|
| Tokens/styles/palettes/typography/charts | tools/search.py + design_system.py | ui-ux-pro-max | Single DB, no duplicate |
| Canvas philosophy + .pdf/.png | tools/canvas.py | canvas-design | Visual art only, not web |
| Web a11y/perf/responsive audit | checks/guideline.py + tools/web_guidelines.py | web-design-guidelines | Audit only, no token gen |
| Data validation | tools/validate_data.py | ui-ux-pro-max | Data integrity |

**Rule:** One capability → one owner. No tool appears in 2 places. References hold docs only.

**Supporting-files resolved:**
- ui-ux-pro-max: /tmp/skills-use-kKJRsH/ui-ux-pro-max/{data,references,scripts} → tools/* + references/ui-ux-data
- canvas-design: /tmp/skills-use-aBguNV/canvas-design/{canvas-fonts,SKILL.md} → references/canvas-fonts
- web-design-guidelines: No local files — fetch https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
