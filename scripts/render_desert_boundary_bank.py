#!/usr/bin/env python3
"""Render the Desert–Taiga boundary question bank for design review."""

import json
from pathlib import Path

from scripts.validate_question_evidence import motive_domain_coverage


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "data" / "desert-taiga-boundary-bank.v0.1.json"
OUTPUT = ROOT / "docs" / "design" / "desert-taiga-boundary-bank-v0.1.md"


def render() -> str:
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    motive_coverage = motive_domain_coverage(bank)
    covered_domains = sorted(set().union(*motive_coverage.values()))
    lines = [
        "# Desert–Taiga Boundary Questions — v0.1",
        "",
        "**Status:** Design review  ",
        "**Evidence schema:** v0.2  ",
        "**Canonical data:** `data/desert-taiga-boundary-bank.v0.1.json`",
        "",
        "> Internal mappings are visible for design review and must be hidden from players.",
        "",
        "## Coverage",
        "",
        f"- Questions: {len(bank['questions'])}",
        "- Desert anchors: Fennec Fox, Caracal, Cobra, Camel, Scorpion, Oryx",
        f"- Motive-probe domains: {', '.join(covered_domains)}",
        "- Purpose: test observable Taiga/Desert boundaries; not yet a complete playable bank",
        "",
    ]
    for question in bank["questions"]:
        animals = " ↔ ".join(question["discriminates"])
        constructs = " + ".join(question["constructs"])
        lines.extend(
            [
                f"## {question['id']} — {question['title']}",
                "",
                f"**Domain:** `{question['domain']}`  ",
                f"**Discriminates:** {animals}  ",
                f"**Measures:** `{constructs}`",
                "",
                question["scenario"],
                "",
            ]
        )
        for option in question["options"]:
            mappings = []
            for item in option["evidence"]:
                suffix = " probe" if item["role"] == "motive_probe" else ""
                mappings.append(
                    f"{item['construct']} {item['value']:+.1f} ×{item['weight']:.1f}{suffix}"
                )
            lines.append(f"- **{option['id']}.** {option['copy']}  ")
            lines.append(f"  `{', '.join(mappings)}`")
        lines.append("")
    lines.extend(
        [
            "## Review gate",
            "",
            "- [x] มี boundary scenario อย่างน้อยหนึ่งข้อต่อ Desert animal",
            "- [x] motive probes กระจายอย่างน้อย 3 domains",
            "- [x] ทุก option ผ่าน Question Evidence Schema v0.2",
            "- [ ] vectors ของ Desert ทั้ง 6 ตัวพร้อมใช้ simulation",
            "- [ ] question-level recovery test แสดงว่าแต่ละ boundary แยกได้จริง",
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    OUTPUT.write_text(render(), encoding="utf-8")
    print(OUTPUT)
