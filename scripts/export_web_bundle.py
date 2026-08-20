#!/usr/bin/env python3
"""Export canonical Taiga design data into a frontend-safe runtime bundle."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts.session_runner import load_result_manifest
from scripts.simulate_adaptive import load_adaptive_bank
from scripts.simulate_questions import load_bank
from scripts.taiga_story import load_story, merge_story, story_errors
from scripts.validate_vectors import load_model


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "web" / "app" / "game-data.generated.json"


def build_bundle() -> dict[str, Any]:
    bank = load_bank()
    story = load_story()
    model = load_model()
    adaptive = load_adaptive_bank()
    manifest = load_result_manifest()
    errors = story_errors(story, bank)
    if errors:
        raise ValueError("Invalid story overlay: " + "; ".join(errors))
    return {
        "bundle_version": "0.1",
        "source_versions": {
            "questions": bank["bank_version"],
            "story": story["story_version"],
            "vectors": model["model_version"],
            "adaptive": adaptive["bank_version"],
            "results": manifest["manifest_version"],
        },
        "title": story["title"],
        "player_role": story["player_role"],
        "opening": story["opening"],
        "acts": story["acts"],
        "judgment": story["judgment"],
        "core_scenes": merge_story(story, bank),
        "adaptive_questions": adaptive["questions"],
        "dimensions": model["dimensions"],
        "animals": model["animals"],
        "realm": {
            "name": manifest["realm"],
            "title": manifest["realm_title"],
        },
        "results": manifest["animals"],
    }


def render_bundle() -> str:
    return json.dumps(build_bundle(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    DEFAULT_OUTPUT.write_text(render_bundle(), encoding="utf-8")
    print(DEFAULT_OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
