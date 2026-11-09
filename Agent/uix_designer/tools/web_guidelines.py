"""Web guidelines fetcher — vercel-labs/web-interface-guidelines."""

from __future__ import annotations

import urllib.request


GUIDELINES_URL = "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md"


def fetch_guidelines() -> str:
    """Fetch latest guidelines (host-authorized)."""
    try:
        with urllib.request.urlopen(GUIDELINES_URL, timeout=10) as r:
            return r.read().decode("utf-8")
    except Exception as e:
        return f"fetch blocked: {e}"


__all__ = ["fetch_guidelines", "GUIDELINES_URL"]
