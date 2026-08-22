#!/usr/bin/env python3
"""Export canonical playable-realm data into a frontend-safe runtime bundle."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts.session_runner import load_result_manifest
from scripts.simulate_taiga_desert import (
    DEFAULT_MODEL as SCORING_MODEL,
    load_boundary_bank,
    load_json,
    normalized_questions,
)
from scripts.simulate_adaptive import load_adaptive_bank
from scripts.simulate_questions import load_bank
from scripts.taiga_story import load_story, merge_story, story_errors
from scripts.validate_vectors import load_model


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "web" / "app" / "game-data.generated.json"
DESERT_RESULTS = ROOT / "data" / "desert-result-manifest.v0.1.json"
RAINFOREST_RESULTS = ROOT / "data" / "rainforest-result-manifest.v0.1.json"


def build_bundle() -> dict[str, Any]:
    bank = load_bank()
    story = load_story()
    model = load_model()
    adaptive = load_adaptive_bank()
    taiga_manifest = load_result_manifest()
    desert_manifest = load_result_manifest(DESERT_RESULTS)
    rainforest_manifest = load_result_manifest(RAINFOREST_RESULTS)
    scoring_model = load_json(SCORING_MODEL)
    boundary = load_boundary_bank()
    errors = story_errors(story, bank)
    if errors:
        raise ValueError("Invalid story overlay: " + "; ".join(errors))
    return {
        "bundle_version": "0.5",
        "source_versions": {
            "questions": bank["bank_version"],
            "story": story["story_version"],
            "vectors": model["model_version"],
            "adaptive": adaptive["bank_version"],
            "results": {
                "Taiga": taiga_manifest["manifest_version"],
                "Desert": desert_manifest["manifest_version"],
                "Rainforest": rainforest_manifest["manifest_version"],
            },
            "scoring": scoring_model["model_version"],
            "boundary": boundary["bank_version"],
        },
        "title": story["title"],
        "player_role": story["player_role"],
        "opening": story["opening"],
        "acts": story["acts"],
        "judgment": story["judgment"],
        "core_scenes": merge_story(story, bank),
        "adaptive_questions": adaptive["questions"],
        "boundary_questions": normalized_questions(boundary),
        "dimensions": model["dimensions"],
        "animals": {
            name: {
                "kingdom": animal["realm"],
                "vector": animal["core"],
                "design_note": "Canonical Scoring Model v0.5 profile",
            }
            for name, animal in scoring_model["animals"].items()
        },
        "realms": {
            manifest["realm"]: {
                "name": manifest["realm"],
                "title": manifest["realm_title"],
                "belief": manifest["realm_belief"],
            }
            for manifest in (taiga_manifest, desert_manifest, rainforest_manifest)
        },
        "results": {
            **taiga_manifest["animals"],
            **desert_manifest["animals"],
            **rainforest_manifest["animals"],
        },
        "scoring": {
            "model_version": scoring_model["model_version"],
            "classification_policy": scoring_model["classification_policy"],
            "core_dimensions": scoring_model["core_dimensions"],
            "motive_facets": scoring_model["motive_facets"],
            "construct_weights": scoring_model["construct_weights"],
            "confidence_targets": scoring_model["confidence_targets"],
            "animal_softmax_temperature": scoring_model["animal_softmax_temperature"],
            "realm_pooling": scoring_model["realm_pooling"],
            "prior_policy": scoring_model["prior_policy"],
            "animals": scoring_model["animals"],
            "response_softmax_temperature": scoring_model["simulation"]["response_softmax_temperature"],
            "max_adaptive_questions": scoring_model["simulation"]["max_adaptive_questions"],
            "minimum_information_gain": scoring_model["simulation"]["minimum_information_gain"],
            "require_adaptive_domain_diversity": scoring_model["simulation"]["require_adaptive_domain_diversity"],
        },
    }


def render_bundle() -> str:
    return json.dumps(build_bundle(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    DEFAULT_OUTPUT.write_text(render_bundle(), encoding="utf-8")
    print(DEFAULT_OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
