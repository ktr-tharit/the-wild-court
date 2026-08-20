#!/usr/bin/env python3
"""Validate and simulate the v0.1 narrative question bank."""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Any

from scripts.validate_vectors import DEFAULT_MODEL, load_model, normalized_distance


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BANK = ROOT / "data" / "question-bank.v0.1.json"
DEFAULT_PLAYTHROUGHS = 5_000
DEFAULT_SEED = 20260823


def load_bank(path: Path = DEFAULT_BANK) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def bank_errors(bank: dict[str, Any], model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    dimensions = {item["id"] for item in model["dimensions"]}
    questions = bank.get("questions", [])
    ids = [question.get("id") for question in questions]
    if len(questions) != 16:
        errors.append(f"expected 16 questions, found {len(questions)}")
    if len(set(ids)) != len(ids):
        errors.append("question IDs must be unique")

    for question in questions:
        qid = question.get("id", "<unknown>")
        targets = question.get("targets", [])
        if len(targets) != 2 or len(set(targets)) != 2:
            errors.append(f"{qid} must target exactly two distinct dimensions")
        if not set(targets).issubset(dimensions):
            errors.append(f"{qid} targets an unknown dimension")
        options = question.get("options", [])
        if [option.get("id") for option in options] != ["A", "B", "C", "D"]:
            errors.append(f"{qid} must contain options A, B, C and D")
        seen_patterns = set()
        for option in options:
            evidence = option.get("evidence", {})
            if set(evidence) != set(targets):
                errors.append(f"{qid}/{option.get('id')} evidence must match targets")
            pattern = tuple(evidence.get(trait) for trait in targets)
            seen_patterns.add(pattern)
            for value in evidence.values():
                if not isinstance(value, (int, float)) or not -1 <= value <= 1:
                    errors.append(f"{qid}/{option.get('id')} has invalid evidence {value!r}")
        if len(seen_patterns) != 4:
            errors.append(f"{qid} must offer four distinct ideal-point patterns")
    return errors


def coverage(bank: dict[str, Any], model: dict[str, Any]) -> dict[str, int]:
    counts = {item["id"]: 0 for item in model["dimensions"]}
    for question in bank["questions"]:
        for trait in question["targets"]:
            counts[trait] += 1
    return counts


def domain_distribution(bank: dict[str, Any]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for question in bank["questions"]:
        domain = question["domain"]
        counts[domain] = counts.get(domain, 0) + 1
    return counts


def option_probabilities(
    theta: list[float],
    question: dict[str, Any],
    trait_index: dict[str, int],
    temperature: float,
) -> list[float]:
    utilities = []
    for option in question["options"]:
        squared_error = sum(
            (theta[trait_index[trait]] - target) ** 2
            for trait, target in option["evidence"].items()
        ) / len(option["evidence"])
        utilities.append(math.exp(-squared_error / temperature))
    total = sum(utilities)
    return [value / total for value in utilities]


def sample_option(probabilities: list[float], generator: random.Random) -> int:
    marker = generator.random()
    cumulative = 0.0
    for index, probability in enumerate(probabilities):
        cumulative += probability
        if marker <= cumulative:
            return index
    return len(probabilities) - 1


def estimate_vector(
    responses: list[tuple[dict[str, Any], dict[str, Any]]],
    model: dict[str, Any],
) -> list[float]:
    ids = [item["id"] for item in model["dimensions"]]
    sums = {trait: 0.0 for trait in ids}
    counts = {trait: 0 for trait in ids}
    for _, option in responses:
        for trait, value in option["evidence"].items():
            sums[trait] += value
            counts[trait] += 1
    return [sums[trait] / counts[trait] if counts[trait] else 0.0 for trait in ids]


def simulate(
    bank: dict[str, Any],
    model: dict[str, Any],
    *,
    playthroughs_per_animal: int = DEFAULT_PLAYTHROUGHS,
    seed: int = DEFAULT_SEED,
) -> dict[str, Any]:
    generator = random.Random(seed)
    trait_index = {item["id"]: index for index, item in enumerate(model["dimensions"])}
    animals = {name: item["vector"] for name, item in model["animals"].items()}
    temperature = bank["response_temperature"]
    confusion = {name: {candidate: 0 for candidate in animals} for name in animals}
    absolute_errors = [0.0] * len(trait_index)
    source_absolute_errors = {
        name: [0.0] * len(trait_index) for name in animals
    }
    correct = 0
    total = 0

    for source_name, theta in animals.items():
        for _ in range(playthroughs_per_animal):
            responses = []
            for question in bank["questions"]:
                probabilities = option_probabilities(
                    theta, question, trait_index, temperature
                )
                option_index = sample_option(probabilities, generator)
                responses.append((question, question["options"][option_index]))
            estimate = estimate_vector(responses, model)
            predicted = min(
                animals,
                key=lambda candidate: normalized_distance(estimate, animals[candidate]),
            )
            confusion[source_name][predicted] += 1
            correct += predicted == source_name
            total += 1
            for index, (estimated, actual) in enumerate(zip(estimate, theta)):
                error = abs(estimated - actual)
                absolute_errors[index] += error
                source_absolute_errors[source_name][index] += error

    ids = [item["id"] for item in model["dimensions"]]
    per_animal_accuracy = {
        name: confusion[name][name] / playthroughs_per_animal for name in animals
    }
    return {
        "seed": seed,
        "response_temperature": temperature,
        "playthroughs_per_animal": playthroughs_per_animal,
        "accuracy": correct / total,
        "per_animal_accuracy": per_animal_accuracy,
        "mean_absolute_error": sum(absolute_errors) / (total * len(ids)),
        "dimension_mae": {
            trait: absolute_errors[index] / total
            for index, trait in enumerate(ids)
        },
        "per_animal_dimension_mae": {
            name: {
                trait: source_absolute_errors[name][index] / playthroughs_per_animal
                for index, trait in enumerate(ids)
            }
            for name in animals
        },
        "confusion": {
            source: {
                target: count / playthroughs_per_animal
                for target, count in row.items()
            }
            for source, row in confusion.items()
        },
    }


def build_report(bank: dict[str, Any], model: dict[str, Any]) -> dict[str, Any]:
    errors = bank_errors(bank, model)
    question_coverage = coverage(bank, model)
    domains = domain_distribution(bank)
    simulation = simulate(bank, model)
    public_power_share = domains.get("public_power", 0) / len(bank["questions"])
    checks = {
        "schema": not errors,
        "balanced_trait_coverage": set(question_coverage.values()) == {4},
        "public_power_scope": public_power_share <= 0.30,
        "classification_accuracy": simulation["accuracy"] >= 0.80,
        "per_animal_floor": min(simulation["per_animal_accuracy"].values()) >= 0.75,
        "vector_mae": simulation["mean_absolute_error"] <= 0.35,
    }
    return {
        "bank_version": bank["bank_version"],
        "checks": checks,
        "schema_errors": errors,
        "coverage": question_coverage,
        "domains": domains,
        "public_power_share": public_power_share,
        "simulation": simulation,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args()
    report = build_report(load_bank(arguments.bank), load_model(arguments.model))
    if arguments.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Question bank v{report['bank_version']}")
        for name, passed in report["checks"].items():
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        simulation = report["simulation"]
        print(f"Classification accuracy: {simulation['accuracy']:.2%}")
        print(f"Mean absolute vector error: {simulation['mean_absolute_error']:.3f}")
    return 0 if all(report["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

