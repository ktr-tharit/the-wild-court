#!/usr/bin/env python3
"""Simulate weighted evidence and softmax scoring across Taiga and Desert."""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "data" / "vector-model.v0.4.json"
CORE_BANK = ROOT / "data" / "question-bank.v0.1.json"
BOUNDARY_BANK = ROOT / "data" / "desert-taiga-boundary-bank.v0.1.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def model_errors(model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    core = model.get("core_dimensions", [])
    facets = model.get("motive_facets", [])
    constructs = core + facets
    animals = model.get("animals", {})
    realms: dict[str, int] = {}
    if len(animals) != 12:
        errors.append(f"expected 12 animals, found {len(animals)}")
    if set(model.get("construct_weights", {})) != set(constructs):
        errors.append("construct weights must cover every construct exactly")
    if set(model.get("confidence_targets", {})) != set(constructs):
        errors.append("confidence targets must cover every construct exactly")
    if model.get("prior_policy") != "equal_realm_then_equal_animal":
        errors.append("sandbox requires normalized realm/animal priors")
    for name, animal in animals.items():
        realms[animal.get("realm", "")] = realms.get(animal.get("realm", ""), 0) + 1
        if len(animal.get("core", [])) != len(core):
            errors.append(f"{name} has wrong core vector length")
        if len(animal.get("facets", [])) != len(facets):
            errors.append(f"{name} has wrong facet vector length")
        if any(not -1 <= value <= 1 for value in animal.get("core", [])):
            errors.append(f"{name} core value outside [-1, 1]")
        if any(value not in {0.0, 0.5, 1.0} for value in animal.get("facets", [])):
            errors.append(f"{name} facet values must use the ordinal scale")
    if realms != {"Taiga": 6, "Desert": 6}:
        errors.append(f"expected six animals in each realm, found {realms}")
    return errors


def animal_profiles(model: dict[str, Any]) -> dict[str, dict[str, float]]:
    core = model["core_dimensions"]
    facets = model["motive_facets"]
    return {
        name: dict(zip(core + facets, animal["core"] + animal["facets"]))
        for name, animal in model["animals"].items()
    }


def normalized_questions(bank: dict[str, Any]) -> list[dict[str, Any]]:
    questions = []
    for question in bank["questions"]:
        normalized = {**question, "options": []}
        for option in question["options"]:
            raw = option["evidence"]
            if isinstance(raw, dict):
                evidence = [
                    {
                        "construct": construct,
                        "value": value,
                        "weight": 1.0,
                        "role": "primary",
                    }
                    for construct, value in raw.items()
                ]
            else:
                evidence = raw
            normalized["options"].append({**option, "evidence": evidence})
        questions.append(normalized)
    return questions


def option_probabilities(
    profile: dict[str, float],
    question: dict[str, Any],
    temperature: float,
    *,
    include_facets: bool,
) -> list[float]:
    utilities = []
    for option in question["options"]:
        evidence = [
            item
            for item in option["evidence"]
            if include_facets or item["construct"] not in {"REC", "MAS", "RCP", "CON", "RST"}
        ]
        total_weight = sum(item["weight"] for item in evidence)
        squared_error = sum(
            item["weight"] * (profile[item["construct"]] - item["value"]) ** 2
            for item in evidence
        ) / total_weight
        utilities.append(-squared_error / temperature)
    peak = max(utilities)
    exponentials = [math.exp(value - peak) for value in utilities]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def sample_option(probabilities: list[float], generator: random.Random) -> int:
    marker = generator.random()
    cumulative = 0.0
    for index, probability in enumerate(probabilities):
        cumulative += probability
        if marker <= cumulative:
            return index
    return len(probabilities) - 1


def estimate_constructs(
    responses: list[dict[str, Any]],
    model: dict[str, Any],
    *,
    include_facets: bool,
) -> tuple[dict[str, float], dict[str, float]]:
    constructs = list(model["core_dimensions"])
    if include_facets:
        constructs += model["motive_facets"]
    sums = {construct: 0.0 for construct in constructs}
    evidence_weights = {construct: 0.0 for construct in constructs}
    for option in responses:
        for item in option["evidence"]:
            construct = item["construct"]
            if construct not in sums:
                continue
            sums[construct] += item["value"] * item["weight"]
            evidence_weights[construct] += item["weight"]
    estimates = {
        construct: sums[construct] / evidence_weights[construct]
        for construct in constructs
        if evidence_weights[construct] > 0
    }
    confidence = {
        construct: min(
            1.0,
            evidence_weights[construct] / model["confidence_targets"][construct],
        )
        for construct in estimates
    }
    return estimates, confidence


def normalized_priors(model: dict[str, Any]) -> dict[str, float]:
    realm_animals: dict[str, list[str]] = {}
    for name, animal in model["animals"].items():
        realm_animals.setdefault(animal["realm"], []).append(name)
    realm_prior = 1.0 / len(realm_animals)
    return {
        name: realm_prior / len(realm_animals[animal["realm"]])
        for name, animal in model["animals"].items()
    }


def softmax_scores(
    estimates: dict[str, float],
    confidence: dict[str, float],
    model: dict[str, Any],
) -> dict[str, Any]:
    profiles = animal_profiles(model)
    priors = normalized_priors(model)
    logits: dict[str, float] = {}
    distances: dict[str, float] = {}
    for name, profile in profiles.items():
        weighted_terms = {
            construct: model["construct_weights"][construct] * confidence[construct]
            for construct in estimates
        }
        denominator = sum(weighted_terms.values())
        distance = (
            sum(
                weight * (estimates[construct] - profile[construct]) ** 2
                for construct, weight in weighted_terms.items()
            ) / denominator
            if denominator
            else 0.0
        )
        distances[name] = distance
        logits[name] = (
            -distance / model["animal_softmax_temperature"] + math.log(priors[name])
        )
    peak = max(logits.values())
    exponentials = {name: math.exp(value - peak) for name, value in logits.items()}
    total = sum(exponentials.values())
    animal_probabilities = {
        name: value / total for name, value in exponentials.items()
    }
    realm_probabilities: dict[str, float] = {}
    for name, probability in animal_probabilities.items():
        realm = model["animals"][name]["realm"]
        realm_probabilities[realm] = realm_probabilities.get(realm, 0.0) + probability
    ranked = sorted(animal_probabilities, key=animal_probabilities.get, reverse=True)
    return {
        "animal_probabilities": animal_probabilities,
        "realm_probabilities": realm_probabilities,
        "distances": distances,
        "top_animal": ranked[0],
        "top_margin": animal_probabilities[ranked[0]] - animal_probabilities[ranked[1]],
    }


def simulate_mode(
    model: dict[str, Any],
    questions: list[dict[str, Any]],
    *,
    include_facets: bool,
    seed: int,
    adaptive_pool: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    generator = random.Random(seed)
    profiles = animal_profiles(model)
    settings = model["simulation"]
    samples = settings["playthroughs_per_animal"]
    response_temperature = settings["response_softmax_temperature"]
    animal_correct = 0
    realm_correct = 0
    total = len(profiles) * samples
    per_animal_correct = {name: 0 for name in profiles}
    probability_sum = 0.0
    margin_sum = 0.0
    extra_questions = 0
    confusion = {name: {candidate: 0 for candidate in profiles} for name in profiles}
    for source, profile in profiles.items():
        for _ in range(samples):
            responses = []
            for question in questions:
                probabilities = option_probabilities(
                    profile,
                    question,
                    response_temperature,
                    include_facets=include_facets,
                )
                responses.append(
                    question["options"][sample_option(probabilities, generator)]
                )
            if adaptive_pool:
                initial_estimates, initial_confidence = estimate_constructs(
                    responses, model, include_facets=include_facets
                )
                initial_result = softmax_scores(
                    initial_estimates, initial_confidence, model
                )
                ranked = sorted(
                    initial_result["animal_probabilities"],
                    key=initial_result["animal_probabilities"].get,
                    reverse=True,
                )
                top_pair = set(ranked[:2])
                selected = [
                    question
                    for question in adaptive_pool
                    if top_pair.issubset(set(question.get("discriminates", [])))
                ][:2]
                for question in selected:
                    probabilities = option_probabilities(
                        profile,
                        question,
                        response_temperature,
                        include_facets=include_facets,
                    )
                    responses.append(
                        question["options"][sample_option(probabilities, generator)]
                    )
                    extra_questions += 1
            estimates, confidence = estimate_constructs(
                responses, model, include_facets=include_facets
            )
            result = softmax_scores(estimates, confidence, model)
            predicted = result["top_animal"]
            source_realm = model["animals"][source]["realm"]
            predicted_realm = max(
                result["realm_probabilities"],
                key=result["realm_probabilities"].get,
            )
            animal_correct += predicted == source
            realm_correct += predicted_realm == source_realm
            per_animal_correct[source] += predicted == source
            confusion[source][predicted] += 1
            probability_sum += result["animal_probabilities"][source]
            margin_sum += result["top_margin"]
    return {
        "base_questions": len(questions),
        "average_extra_questions": extra_questions / total,
        "include_facets": include_facets,
        "animal_accuracy": animal_correct / total,
        "realm_accuracy": realm_correct / total,
        "mean_true_animal_probability": probability_sum / total,
        "mean_top_margin": margin_sum / total,
        "per_animal_accuracy": {
            name: count / samples for name, count in per_animal_correct.items()
        },
        "confusion": {
            source: {
                target: count / samples
                for target, count in row.items()
                if count
            }
            for source, row in confusion.items()
        },
    }


def build_report(model: dict[str, Any]) -> dict[str, Any]:
    errors = model_errors(model)
    if errors:
        return {"model_version": model.get("model_version"), "errors": errors}
    core_questions = normalized_questions(load_json(CORE_BANK))
    boundary_questions = normalized_questions(load_json(BOUNDARY_BANK))
    seed = model["simulation"]["seed"]
    modes = {
        "core_softmax": simulate_mode(
            model, core_questions, include_facets=False, seed=seed
        ),
        "weighted_boundaries_core": simulate_mode(
            model, core_questions + boundary_questions, include_facets=False, seed=seed
        ),
        "weighted_full": simulate_mode(
            model, core_questions + boundary_questions, include_facets=True, seed=seed
        ),
        "adaptive_weighted_core": simulate_mode(
            model,
            core_questions,
            include_facets=False,
            seed=seed,
            adaptive_pool=boundary_questions,
        ),
        "adaptive_weighted_full": simulate_mode(
            model,
            core_questions,
            include_facets=True,
            seed=seed,
            adaptive_pool=boundary_questions,
        ),
    }
    baseline = modes["core_softmax"]
    candidate = modes["adaptive_weighted_core"]
    return {
        "model_version": model["model_version"],
        "errors": [],
        "selected_mode": "adaptive_weighted_core",
        "modes": modes,
        "lift": {
            "animal_accuracy": candidate["animal_accuracy"] - baseline["animal_accuracy"],
            "realm_accuracy": candidate["realm_accuracy"] - baseline["realm_accuracy"],
            "true_probability": candidate["mean_true_animal_probability"] - baseline["mean_true_animal_probability"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args()
    report = build_report(load_json(arguments.model))
    if arguments.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    elif report["errors"]:
        for error in report["errors"]:
            print(f"FAIL  {error}")
    else:
        print(f"Taiga–Desert weighted softmax sandbox {report['model_version']}")
        for name, result in report["modes"].items():
            print(
                f"{name}: animal={result['animal_accuracy']:.2%} "
                f"realm={result['realm_accuracy']:.2%} "
                f"true_p={result['mean_true_animal_probability']:.3f} "
                f"extra_q={result['average_extra_questions']:.2f}"
            )
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
