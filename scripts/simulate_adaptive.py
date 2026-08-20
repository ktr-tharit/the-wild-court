#!/usr/bin/env python3
"""Simulate pair-specific Judgment questions after the 16-item core bank."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

from scripts.simulate_questions import (
    DEFAULT_BANK,
    estimate_vector,
    load_bank,
    option_probabilities,
    sample_option,
)
from scripts.validate_vectors import DEFAULT_MODEL, load_model, normalized_distance


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ADAPTIVE_BANK = ROOT / "data" / "adaptive-question-bank.v0.1.json"
DEFAULT_PLAYTHROUGHS = 5_000
DEFAULT_SEED = 20260824


def load_adaptive_bank(path: Path = DEFAULT_ADAPTIVE_BANK) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def adaptive_bank_errors(bank: dict[str, Any], model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    dimensions = {item["id"] for item in model["dimensions"]}
    animals = set(model["animals"])
    questions = bank.get("questions", [])
    ids = [question.get("id") for question in questions]
    if len(questions) != 6:
        errors.append(f"expected 6 adaptive questions, found {len(questions)}")
    if len(set(ids)) != len(ids):
        errors.append("adaptive question IDs must be unique")

    pair_counts: dict[frozenset[str], int] = {}
    for question in questions:
        qid = question.get("id", "<unknown>")
        pair = question.get("discriminates", [])
        if len(pair) != 2 or len(set(pair)) != 2 or not set(pair).issubset(animals):
            errors.append(f"{qid} must discriminate exactly two known animals")
        pair_key = frozenset(pair)
        pair_counts[pair_key] = pair_counts.get(pair_key, 0) + 1
        targets = question.get("targets", [])
        if len(targets) != 2 or len(set(targets)) != 2:
            errors.append(f"{qid} must target exactly two distinct dimensions")
        if not set(targets).issubset(dimensions):
            errors.append(f"{qid} contains an unknown dimension")
        options = question.get("options", [])
        if [option.get("id") for option in options] != ["A", "B", "C", "D"]:
            errors.append(f"{qid} must contain options A, B, C and D")
        patterns = set()
        for option in options:
            evidence = option.get("evidence", {})
            if set(evidence) != set(targets):
                errors.append(f"{qid}/{option.get('id')} evidence must match targets")
            patterns.add(tuple(evidence.get(trait) for trait in targets))
        if len(patterns) != 4:
            errors.append(f"{qid} must offer four distinct ideal points")

    expected_pairs = {
        frozenset(("Grey Wolf", "Bear")),
        frozenset(("Grey Wolf", "Moose")),
        frozenset(("Bear", "Moose")),
    }
    if set(pair_counts) != expected_pairs or set(pair_counts.values()) != {2}:
        errors.append("bank must contain exactly two questions for each ambiguity pair")
    return errors


def ranked_animals(
    estimate: list[float], animals: dict[str, list[float]]
) -> list[str]:
    return sorted(
        animals,
        key=lambda candidate: normalized_distance(estimate, animals[candidate]),
    )


def simulate_adaptive(
    core_bank: dict[str, Any],
    adaptive_bank: dict[str, Any],
    model: dict[str, Any],
    *,
    playthroughs_per_animal: int = DEFAULT_PLAYTHROUGHS,
    seed: int = DEFAULT_SEED,
) -> dict[str, Any]:
    generator = random.Random(seed)
    trait_index = {item["id"]: index for index, item in enumerate(model["dimensions"])}
    animals = {name: item["vector"] for name, item in model["animals"].items()}
    core_temperature = core_bank["response_temperature"]
    adaptive_temperature = adaptive_bank["response_temperature"]
    adaptive_by_pair: dict[frozenset[str], list[dict[str, Any]]] = {}
    for question in adaptive_bank["questions"]:
        adaptive_by_pair.setdefault(frozenset(question["discriminates"]), []).append(question)

    baseline_confusion = {
        name: {candidate: 0 for candidate in animals} for name in animals
    }
    adaptive_confusion = {
        name: {candidate: 0 for candidate in animals} for name in animals
    }
    extra_question_counts = {name: 0 for name in animals}
    triggered_playthroughs = {name: 0 for name in animals}
    total = 0

    for source_name, theta in animals.items():
        for _ in range(playthroughs_per_animal):
            responses = []
            for question in core_bank["questions"]:
                probabilities = option_probabilities(
                    theta, question, trait_index, core_temperature
                )
                option = question["options"][sample_option(probabilities, generator)]
                responses.append((question, option))

            baseline_estimate = estimate_vector(responses, model)
            baseline_ranking = ranked_animals(baseline_estimate, animals)
            baseline_confusion[source_name][baseline_ranking[0]] += 1

            pair = frozenset(baseline_ranking[:2])
            selected_questions = adaptive_by_pair.get(pair, [])
            if selected_questions:
                triggered_playthroughs[source_name] += 1
            for question in selected_questions:
                probabilities = option_probabilities(
                    theta, question, trait_index, adaptive_temperature
                )
                option = question["options"][sample_option(probabilities, generator)]
                responses.append((question, option))
                extra_question_counts[source_name] += 1

            final_estimate = estimate_vector(responses, model)
            final_ranking = ranked_animals(final_estimate, animals)
            adaptive_confusion[source_name][final_ranking[0]] += 1
            total += 1

    baseline_accuracy = sum(
        baseline_confusion[name][name] for name in animals
    ) / total
    adaptive_accuracy = sum(
        adaptive_confusion[name][name] for name in animals
    ) / total
    per_animal_baseline = {
        name: baseline_confusion[name][name] / playthroughs_per_animal
        for name in animals
    }
    per_animal_adaptive = {
        name: adaptive_confusion[name][name] / playthroughs_per_animal
        for name in animals
    }
    return {
        "seed": seed,
        "playthroughs_per_animal": playthroughs_per_animal,
        "baseline_accuracy": baseline_accuracy,
        "adaptive_accuracy": adaptive_accuracy,
        "accuracy_lift": adaptive_accuracy - baseline_accuracy,
        "average_extra_questions": sum(extra_question_counts.values()) / total,
        "trigger_rate": sum(triggered_playthroughs.values()) / total,
        "per_animal_baseline": per_animal_baseline,
        "per_animal_adaptive": per_animal_adaptive,
        "per_animal_lift": {
            name: per_animal_adaptive[name] - per_animal_baseline[name]
            for name in animals
        },
        "per_animal_average_extra_questions": {
            name: extra_question_counts[name] / playthroughs_per_animal
            for name in animals
        },
        "baseline_confusion": {
            source: {
                target: count / playthroughs_per_animal
                for target, count in row.items()
            }
            for source, row in baseline_confusion.items()
        },
        "adaptive_confusion": {
            source: {
                target: count / playthroughs_per_animal
                for target, count in row.items()
            }
            for source, row in adaptive_confusion.items()
        },
    }


def build_report(
    core_bank: dict[str, Any], adaptive_bank: dict[str, Any], model: dict[str, Any]
) -> dict[str, Any]:
    errors = adaptive_bank_errors(adaptive_bank, model)
    simulation = simulate_adaptive(core_bank, adaptive_bank, model)
    cluster = ("Grey Wolf", "Bear", "Moose")
    checks = {
        "schema": not errors,
        "overall_accuracy_lift": simulation["accuracy_lift"] >= 0.01,
        "cluster_animals_improve": all(
            simulation["per_animal_lift"][animal] > 0 for animal in cluster
        ),
        "question_budget": simulation["average_extra_questions"] <= 1.0,
        "final_accuracy": simulation["adaptive_accuracy"] >= 0.88,
    }
    return {
        "adaptive_bank_version": adaptive_bank["bank_version"],
        "checks": checks,
        "schema_errors": errors,
        "simulation": simulation,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--adaptive-bank", type=Path, default=DEFAULT_ADAPTIVE_BANK)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args()
    report = build_report(
        load_bank(arguments.core_bank),
        load_adaptive_bank(arguments.adaptive_bank),
        load_model(arguments.model),
    )
    if arguments.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for name, passed in report["checks"].items():
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        result = report["simulation"]
        print(f"Baseline accuracy: {result['baseline_accuracy']:.2%}")
        print(f"Adaptive accuracy: {result['adaptive_accuracy']:.2%}")
        print(f"Average extra questions: {result['average_extra_questions']:.2f}")
    return 0 if all(report["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

