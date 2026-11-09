"""Canvas design — philosophy + render (from anthropics/canvas-design)."""

from __future__ import annotations

from pathlib import Path


def create_philosophy(name: str, output: Path) -> Path:
    """Create visual philosophy .md (stub)."""
    output.write_text(f"# {name}\nPhilosophy: visual expression via space, color, form.\n")
    return output


def render_canvas(philosophy: Path, output: Path) -> Path:
    """Render philosophy to .pdf/.png (stub — requires host canvas renderer)."""
    # Real impl would use canvas-fonts and generate PDF/PNG
    output.write_text(f"Canvas rendered from {philosophy.name}")
    return output
