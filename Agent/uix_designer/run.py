"""UIX Designer entry point.

Run: uv run --no-sync python -m agent.skills.uix_designer.run <repository-root>
"""

from __future__ import annotations

import sys
from pathlib import Path

from agent.contracts.host import HostDispatchEnvelope, HostDispatchResult


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m agent.skills.uix_designer.run <repository-root>")
        sys.exit(1)
    repo = Path(sys.argv[1])
    if not repo.exists():
        print(f"Not found: {repo}")
        sys.exit(1)
    print("UIX Designer — ui-ux-pro-max + canvas-design + web-design-guidelines")
    print(f"Repo: {repo}")
    print("Use tools/search.py or design_system.py for UI queries")


def pre_dispatch(request: HostDispatchEnvelope) -> HostDispatchEnvelope:
    if request.stage not in ("build", "planning", "research"):
        raise ValueError(f"UIX stage must be build/planning/research, got '{request.stage}'")
    if request.requester_role not in ("host", "uix_designer", "builder"):
        raise ValueError(f"Unauthorized role '{request.requester_role}'")
    return request.model_copy(
        update={
            "information_needed": request.information_needed
            + " | uix_scope: tokens_components_canvas_guidelines"
        }
    )


def post_dispatch(result: HostDispatchResult) -> HostDispatchResult:
    if not result.output_ref.artifact_id:
        raise ValueError("UIX result must reference artifact")
    if result.output_ref.contract_id not in ("uix_record", "build_record"):
        raise ValueError(f"UIX contract must be uix_record/build_record, got '{result.output_ref.contract_id}'")
    return result


__all__ = ["main", "post_dispatch", "pre_dispatch"]
