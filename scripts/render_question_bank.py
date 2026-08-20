#!/usr/bin/env python3
"""Render the canonical JSON question bank as a human review sheet."""

from pathlib import Path

from scripts.simulate_questions import DEFAULT_BANK, load_bank


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "design" / "question-bank-v0.1.md"


def render() -> str:
    bank = load_bank(DEFAULT_BANK)
    lines = [
        "# Narrative Question Bank — v0.1",
        "",
        "**Status:** Review  ",
        "**Language:** Thai  ",
        "**Canonical data:** `data/question-bank.v0.1.json`",
        "",
        "> Internal trait mappings are shown for design review and must not appear in the player UI.",
        "",
    ]
    current_act = None
    for question in bank["questions"]:
        if question["act"] != current_act:
            current_act = question["act"]
            lines.extend([f"## Act — {current_act}", ""])
        targets = " + ".join(question["targets"])
        lines.extend(
            [
                f"### {question['id']} — {question['title']}",
                "",
                f"**Domain:** `{question['domain']}`  ",
                f"**Measures:** `{targets}`",
                "",
                question["scenario"],
                "",
            ]
        )
        for option in question["options"]:
            mapping = ", ".join(
                f"{trait} {value:+.1f}" for trait, value in option["evidence"].items()
            )
            lines.append(f"- **{option['id']}.** {option['copy']}  ")
            lines.append(f"  `{mapping}`")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    OUTPUT.write_text(render(), encoding="utf-8")
    print(OUTPUT)

