#!/usr/bin/env python3
"""Validate and render the Taiga narrative overlay without changing measurement data."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts.simulate_questions import DEFAULT_BANK, load_bank


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STORY = ROOT / "data" / "taiga-story-overlay.v0.1.json"
DEFAULT_OUTPUT = ROOT / "docs" / "design" / "taiga-playable-script-v0.1.md"

ALLOWED_TAGS = {
    "observed_first", "stepped_forward", "acted_alone", "gathered_people",
    "trusted_instinct", "checked_evidence", "kept_structure",
    "adapted_in_motion", "challenged_rule", "honored_duty",
    "protected_bond", "protected_principle", "showed_feeling",
    "held_feeling", "kept_known", "took_risk", "followed_expertise",
    "supported_others", "self_authored",
}


def load_story(path: Path = DEFAULT_STORY) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def story_errors(story: dict[str, Any], bank: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    scenes = story.get("scenes", [])
    bank_by_id = {question["id"]: question for question in bank["questions"]}
    scene_ids = [scene.get("question_id") for scene in scenes]
    orders = [scene.get("order") for scene in scenes]

    if set(scene_ids) != set(bank_by_id) or len(scene_ids) != len(bank_by_id):
        errors.append("story must contain every core question exactly once")
    if orders != list(range(1, len(scenes) + 1)):
        errors.append("scene order must be sequential and match list order")

    seen_acts: list[str] = []
    for scene in scenes:
        qid = scene.get("question_id", "<unknown>")
        question = bank_by_id.get(qid)
        if not question:
            continue
        act = question["act"]
        if not seen_acts or seen_acts[-1] != act:
            seen_acts.append(act)
        for field in ("location", "intensity", "setup", "scenario", "transition_after"):
            if not scene.get(field):
                errors.append(f"{qid} missing story field {field}")
        option_ids = {option["id"] for option in question["options"]}
        option_tags = scene.get("option_tags", {})
        if set(option_tags) != option_ids:
            errors.append(f"{qid} must tag every option exactly once")
        for option_id, tags in option_tags.items():
            if not isinstance(tags, list) or not 1 <= len(tags) <= 2:
                errors.append(f"{qid}/{option_id} must add one or two story tags")
            unknown = set(tags) - ALLOWED_TAGS
            if unknown:
                errors.append(f"{qid}/{option_id} has unknown tags {sorted(unknown)}")

    if seen_acts != ["Arrival", "Bonds", "Fracture"]:
        errors.append(f"story act order is invalid: {seen_acts}")
    if set(story.get("acts", {})) != {"Arrival", "Bonds", "Fracture"}:
        errors.append("story must define Arrival, Bonds and Fracture framing")
    return errors


def merge_story(story: dict[str, Any], bank: dict[str, Any]) -> list[dict[str, Any]]:
    """Return playable scenes while preserving base option evidence verbatim."""
    bank_by_id = {question["id"]: question for question in bank["questions"]}
    merged = []
    for overlay in story["scenes"]:
        question = deepcopy(bank_by_id[overlay["question_id"]])
        question.update({
            "scene_order": overlay["order"],
            "location": overlay["location"],
            "intensity": overlay["intensity"],
            "setup": overlay["setup"],
            "scenario": overlay["scenario"],
            "transition_after": overlay["transition_after"],
        })
        for option in question["options"]:
            option["consequence_tags"] = overlay["option_tags"][option["id"]]
        merged.append(question)
    return merged


def render(story: dict[str, Any], bank: dict[str, Any]) -> str:
    scenes = merge_story(story, bank)
    lines = [
        f"# {story['title']} — Taiga Playable Script v{story['story_version']}",
        "",
        "**Status:** Thin vertical slice / prototype prose  ",
        "**Measurement source:** `data/question-bank.v0.1.json`  ",
        "**Narrative source:** `data/taiga-story-overlay.v0.1.json`",
        "",
        "> Internal evidence and consequence tags are visible for review only.",
        "",
        "## Opening",
        "",
    ]
    lines.extend(f"> {paragraph}" for paragraph in story["opening"])
    lines.append("")
    current_act = None
    for scene in scenes:
        if scene["act"] != current_act:
            current_act = scene["act"]
            framing = story["acts"][current_act]
            lines.extend([
                f"## {framing['title']}", "", framing["intro"], "",
            ])
        lines.extend([
            f"### Scene {scene['scene_order']:02d} · {scene['title']}", "",
            f"**Location:** {scene['location']}  ",
            f"**Intensity:** {scene['intensity']}  ",
            f"**Question:** `{scene['id']}` · **Measures:** `{' + '.join(scene['targets'])}`",
            "", scene["setup"], "", f"**Choice:** {scene['scenario']}", "",
        ])
        for option in scene["options"]:
            evidence = ", ".join(
                f"{trait} {value:+.1f}" for trait, value in option["evidence"].items()
            )
            tags = ", ".join(option["consequence_tags"])
            lines.extend([
                f"- **{option['id']}.** {option['copy']}  ",
                f"  `{evidence}` · adds `{tags}`",
            ])
        lines.extend(["", f"*Transition:* {scene['transition_after']}", ""])
        next_scene_index = scene["scene_order"]
        is_last_of_act = (
            next_scene_index == len(scenes)
            or scenes[next_scene_index]["act"] != current_act
        )
        if is_last_of_act:
            lines.extend([f"> {story['acts'][current_act]['outro']}", ""])
    lines.extend([
        "## Judgment", "", story["judgment"]["intro"], "",
        "Adaptive question 0–2 ข้อจะถูกเลือกจาก candidate pair โดยไม่เปิดเผยคะแนน", "",
        f"> {story['judgment']['transition_to_result']}", "",
    ])
    return "\n".join(lines)


def main() -> int:
    bank = load_bank(DEFAULT_BANK)
    story = load_story(DEFAULT_STORY)
    errors = story_errors(story, bank)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    DEFAULT_OUTPUT.write_text(render(story, bank), encoding="utf-8")
    print(DEFAULT_OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
