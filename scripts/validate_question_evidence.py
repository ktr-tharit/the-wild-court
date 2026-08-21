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
    questions = payload.get("questions")
    if questions is None:
        questions = [payload.get("question", {})]
    question_ids = [question.get("id") for question in questions]
    if len(question_ids) != len(set(question_ids)):
        errors.append("question IDs must be unique")
    for question in questions:
        question_id = question.get("id", "<unknown>")
        declared_list = question.get("constructs", [])
        declared = set(declared_list)
        if not 1 <= len(declared_list) <= 3 or len(declared) != len(declared_list):
            errors.append(f"{question_id} must declare 1–3 distinct constructs")
        options = question.get("options", [])
        if [option.get("id") for option in options] != ["A", "B", "C", "D"]:
            errors.append(f"{question_id} must contain options A, B, C and D")
        signatures = set()
        for option in options:
            option_id = option.get("id", "<unknown>")
            label = f"{question_id}/{option_id}"
            evidence = option.get("evidence", [])
            if not 1 <= len(evidence) <= 3:
                errors.append(f"{label} must contain 1–3 evidence items")
            constructs = [item.get("construct") for item in evidence]
            if len(constructs) != len(set(constructs)):
                errors.append(f"{label} repeats a construct")
            if set(constructs) != declared:
                errors.append(f"{label} evidence must match declared constructs")
            strong_count = 0
            signature = []
            for item in evidence:
                construct = item.get("construct")
                value = item.get("value")
                weight = item.get("weight")
                role = item.get("role")
                if construct not in CORE_CONSTRUCTS | MOTIVE_CONSTRUCTS:
                    errors.append(f"{label} uses unknown construct {construct!r}")
                if weight not in {0.5, 1.0}:
                    errors.append(f"{label}/{construct} uses invalid weight")
                strong_count += weight == 1.0
                if role not in {"primary", "secondary", "motive_probe"}:
                    errors.append(f"{label}/{construct} uses invalid role")
                if role == "primary" and weight != 1.0:
                    errors.append(f"{label}/{construct} primary evidence must weigh 1.0")
                if role == "secondary" and weight != 0.5:
                    errors.append(f"{label}/{construct} secondary evidence must weigh 0.5")
                if construct in CORE_CONSTRUCTS and (
                    not isinstance(value, (int, float)) or not -1 <= value <= 1
                ):
                    errors.append(f"{label}/{construct} core value must be in [-1, 1]")
                if construct in MOTIVE_CONSTRUCTS and value not in {0.0, 0.5, 1.0}:
                    errors.append(f"{label}/{construct} motive value must be ordinal")
                if role == "motive_probe" and (
                    construct not in MOTIVE_CONSTRUCTS or weight != 0.5
                ):
                    errors.append(f"{label}/{construct} motive probes must be weak facets")
                signature.append((construct, value, weight))
            if strong_count > 2:
                errors.append(f"{label} has more than two strong loadings")
            signatures.add(tuple(sorted(signature)))
        if len(signatures) != len(options):
            errors.append(f"{question_id} answer evidence signatures must be distinct")
    return errors


def motive_domain_coverage(payload: dict[str, Any]) -> dict[str, set[str]]:
    coverage = {construct: set() for construct in MOTIVE_CONSTRUCTS}
    questions = payload.get("questions", [payload.get("question", {})])
    for question in questions:
        domain = question.get("domain")
        for construct in question.get("constructs", []):
            if construct in coverage:
                coverage[construct].add(domain)
    return coverage


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--example", type=Path, default=DEFAULT_EXAMPLE)
    arguments = parser.parse_args()
    errors = evidence_errors(load_example(arguments.example))
    if errors:
        for error in errors:
            print(f"FAIL  {error}")
        return 1
    print("PASS  Question Evidence Schema v0.2 payload")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
