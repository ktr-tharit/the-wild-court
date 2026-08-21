#!/usr/bin/env python3
"""Validate the Question Evidence Schema v0.2 example contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXAMPLE = ROOT / "data" / "question-evidence-example.v0.2.json"
CORE_CONSTRUCTS = {"AFF", "AGY", "SEN", "STR", "EXP", "RSK", "DCL", "ALG"}
MOTIVE_CONSTRUCTS = {"REC", "MAS", "RCP", "CON", "RST"}


def load_example(path: Path = DEFAULT_EXAMPLE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if payload.get("schema_version") != "0.2":
        errors.append("schema_version must be 0.2")
    question = payload.get("question", {})
    declared = set(question.get("constructs", []))
    options = question.get("options", [])
    if [option.get("id") for option in options] != ["A", "B", "C", "D"]:
        errors.append("question must contain options A, B, C and D")
    signatures = set()
    for option in options:
        option_id = option.get("id", "<unknown>")
        evidence = option.get("evidence", [])
        if not 1 <= len(evidence) <= 3:
            errors.append(f"{option_id} must contain 1–3 evidence items")
        constructs = [item.get("construct") for item in evidence]
        if len(constructs) != len(set(constructs)):
            errors.append(f"{option_id} repeats a construct")
        if set(constructs) != declared:
            errors.append(f"{option_id} evidence must match declared constructs")
        strong_count = 0
        signature = []
        for item in evidence:
            construct = item.get("construct")
            value = item.get("value")
            weight = item.get("weight")
            role = item.get("role")
            if construct not in CORE_CONSTRUCTS | MOTIVE_CONSTRUCTS:
                errors.append(f"{option_id} uses unknown construct {construct!r}")
            if weight not in {0.5, 1.0}:
                errors.append(f"{option_id}/{construct} uses invalid weight")
            strong_count += weight == 1.0
            if role not in {"primary", "secondary", "motive_probe"}:
                errors.append(f"{option_id}/{construct} uses invalid role")
            if construct in CORE_CONSTRUCTS and (
                not isinstance(value, (int, float)) or not -1 <= value <= 1
            ):
                errors.append(f"{option_id}/{construct} core value must be in [-1, 1]")
            if construct in MOTIVE_CONSTRUCTS and value not in {0.0, 0.5, 1.0}:
                errors.append(f"{option_id}/{construct} motive value must be ordinal")
            if role == "motive_probe" and (
                construct not in MOTIVE_CONSTRUCTS or weight != 0.5
            ):
                errors.append(f"{option_id}/{construct} motive probes must be weak facets")
            signature.append((construct, value, weight))
        if strong_count > 2:
            errors.append(f"{option_id} has more than two strong loadings")
        signatures.add(tuple(sorted(signature)))
    if len(signatures) != len(options):
        errors.append("answer evidence signatures must be distinct")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--example", type=Path, default=DEFAULT_EXAMPLE)
    arguments = parser.parse_args()
    errors = evidence_errors(load_example(arguments.example))
    if errors:
        for error in errors:
            print(f"FAIL  {error}")
        return 1
    print("PASS  Question Evidence Schema v0.2 example")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
