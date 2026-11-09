"""UIX Designer skill — unified UI/UX + canvas + web guidelines.

Ownership:
    - ui-ux-pro-max: tokens, styles, palettes, typography via search.py
    - canvas-design: philosophy + canvas rendering via canvas-fonts
    - web-design-guidelines: Vercel audit via fetched command.md

No overlap: each capability has single owner per overlap-map.md.
Tools are host-authorized; results via HostDispatchResult (uix_record).
"""

from agent.skills.uix_designer.run import post_dispatch, pre_dispatch

__all__ = ["post_dispatch", "pre_dispatch"]
