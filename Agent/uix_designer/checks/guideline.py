"""Guideline checks — web-design-guidelines audit wrapper."""

from __future__ import annotations

from pathlib import Path


def run_web_guidelines_check(target: Path | str) -> dict[str, str]:
    """Fetch Vercel guidelines and audit target (stub — host fetches URL)."""
    # Real impl fetches
    # https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
    return {
        "status": "not_valid",
        "detail": "web guideline check requires host fetch of Vercel URL",
        "target": str(target),
    }


__all__ = ["run_web_guidelines_check"]
