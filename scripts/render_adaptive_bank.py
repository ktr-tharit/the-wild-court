#!/usr/bin/env python3
"""Render adaptive Judgment questions for human review."""

from pathlib import Path

from scripts.simulate_adaptive import DEFAULT_ADAPTIVE_BANK, load_adaptive_bank


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "design" / "adaptive-question-bank-v0.1.md"


def render() -> str:
    bank = load_adaptive_bank(DEFAULT_ADAPTIVE_BANK)
    lines = [
        "# Adaptive Judgment Questions — v0.1",
        "",
        "**Status:** Review  ",
        "**Canonical data:** `data/adaptive-question-bank.v0.1.json`",
        "",
        "> Internal mappings are visible for design review and must be hidden from players.",
        "",
    ]
    for question in bank["questions"]:
        pair = " ↔ ".join(question["discriminates"])
        targets = " + ".join(question["targets"])
        lines.extend(
            [
                f"## {question['id']} — {question['title']}",
                "",
                f"**Discriminates:** {pair}  ",
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

