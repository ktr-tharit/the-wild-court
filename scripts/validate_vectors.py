#!/usr/bin/env python3
"""Validate prototype vectors without external dependencies.

Distances are normalized root-mean-square distances, so their scale remains
comparable if the number of dimensions changes.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "data" / "vector-model.v0.3.json"


def load_model(path: Path = DEFAULT_MODEL) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalized_distance(left: Iterable[float], right: Iterable[float]) -> float:
    pairs = list(zip(left, right))
    if not pairs:
        raise ValueError("Vectors must contain at least one dimension")
    return math.sqrt(sum((a - b) ** 2 for a, b in pairs) / len(pairs))


def schema_errors(model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    dimensions = model.get("dimensions", [])
    dimension_count = len(dimensions)
    ids = [item.get("id") for item in dimensions]
    if dimension_count != 8:
        errors.append(f"expected 8 dimensions, found {dimension_count}")
    if len(set(ids)) != len(ids):
        errors.append("dimension IDs must be unique")

    collections = {
        "kingdom": model.get("kingdom_fingerprints", {}),
        "animal": {
            name: value.get("vector", [])
            for name, value in model.get("animals", {}).items()
        },
    }
    for kind, values in collections.items():
        for name, vector in values.items():
            if len(vector) != dimension_count:
                errors.append(
                    f"{kind} {name!r} has {len(vector)} values; expected {dimension_count}"
                )
            for value in vector:
                if not isinstance(value, (int, float)) or not -1 <= value <= 1:
                    errors.append(f"{kind} {name!r} contains out-of-range value {value!r}")
    return errors


def pairwise_distances(vectors: dict[str, list[float]]) -> list[tuple[float, str, str]]:
    names = sorted(vectors)
    results = []
    for index, left_name in enumerate(names):
        for right_name in names[index + 1 :]:
            distance = normalized_distance(vectors[left_name], vectors[right_name])
            results.append((distance, left_name, right_name))
    return sorted(results)


def dimension_spans(model: dict[str, Any]) -> dict[str, float]:
    ids = [item["id"] for item in model["dimensions"]]
    animal_vectors = [item["vector"] for item in model["animals"].values()]
    return {
        trait_id: max(vector[index] for vector in animal_vectors)
        - min(vector[index] for vector in animal_vectors)
        for index, trait_id in enumerate(ids)
    }


def recovery_simulation(
    model: dict[str, Any], *, seed: int = 20260821
) -> dict[str, Any]:
    settings = model["validation_thresholds"]
    sigma = settings["recovery_noise_sigma"]
    samples = settings["recovery_samples_per_animal"]
    animals = {name: item["vector"] for name, item in model["animals"].items()}
    generator = random.Random(seed)
    confusion = {name: {candidate: 0 for candidate in animals} for name in animals}
    correct = 0
    total = 0

    for source_name, source_vector in animals.items():
        for _ in range(samples):
            player = [
                max(-1.0, min(1.0, value + generator.gauss(0.0, sigma)))
                for value in source_vector
            ]
            predicted = min(
                animals,
                key=lambda candidate: normalized_distance(player, animals[candidate]),
            )
            confusion[source_name][predicted] += 1
            correct += predicted == source_name
            total += 1

    return {
        "seed": seed,
        "sigma": sigma,
        "samples_per_animal": samples,
        "accuracy": correct / total,
        "confusion": {
            source: {target: count / samples for target, count in row.items()}
            for source, row in confusion.items()
        },
    }


def uniform_voronoi_share(
    model: dict[str, Any], *, samples: int = 100_000, seed: int = 20260822
) -> dict[str, float]:
    """Diagnostic only: uniform trait space is not a population model."""
    generator = random.Random(seed)
    animals = {name: item["vector"] for name, item in model["animals"].items()}
    dimension_count = len(model["dimensions"])
    counts = {name: 0 for name in animals}
    for _ in range(samples):
        player = [generator.uniform(-1.0, 1.0) for _ in range(dimension_count)]
        predicted = min(
            animals,
            key=lambda candidate: normalized_distance(player, animals[candidate]),
        )
        counts[predicted] += 1
    return {name: count / samples for name, count in counts.items()}


def nearest_kingdoms(model: dict[str, Any]) -> dict[str, list[tuple[str, float]]]:
    kingdoms = model["kingdom_fingerprints"]
    return {
        animal_name: [
            (kingdom_name, distance)
            for distance, kingdom_name in sorted(
                (
                    normalized_distance(animal["vector"], kingdom_vector),
                    kingdom_name,
                )
                for kingdom_name, kingdom_vector in kingdoms.items()
            )[:3]
        ]
        for animal_name, animal in model["animals"].items()
    }


def build_report(model: dict[str, Any]) -> dict[str, Any]:
    animal_vectors = {name: item["vector"] for name, item in model["animals"].items()}
    animal_pairs = pairwise_distances(animal_vectors)
    kingdom_pairs = pairwise_distances(model["kingdom_fingerprints"])
    recovery = recovery_simulation(model)
    thresholds = model["validation_thresholds"]
    spans = dimension_spans(model)
    errors = schema_errors(model)
    checks = {
        "schema": not errors,
        "animal_separation": animal_pairs[0][0] >= thresholds["minimum_animal_distance"],
        "dimension_coverage": min(spans.values()) >= thresholds["minimum_dimension_span"],
        "kingdom_separation": kingdom_pairs[0][0] >= thresholds["minimum_kingdom_distance"],
        "prototype_recovery": recovery["accuracy"] >= thresholds["minimum_recovery_accuracy"],
    }
    return {
        "model_version": model["model_version"],
        "checks": checks,
        "schema_errors": errors,
        "closest_animal_pairs": animal_pairs[:6],
        "closest_kingdom_pairs": kingdom_pairs[:6],
        "dimension_spans": spans,
        "recovery": recovery,
        "uniform_voronoi_share": uniform_voronoi_share(model),
        "nearest_kingdoms": nearest_kingdoms(model),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    arguments = parser.parse_args()
    report = build_report(load_model(arguments.model))
    if arguments.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Vector model v{report['model_version']}")
        for name, passed in report["checks"].items():
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        closest_animal = report["closest_animal_pairs"][0]
        closest_kingdom = report["closest_kingdom_pairs"][0]
        print(
            f"Closest animals: {closest_animal[1]} / {closest_animal[2]} "
            f"({closest_animal[0]:.3f})"
        )
        print(
            f"Closest kingdoms: {closest_kingdom[1]} / {closest_kingdom[2]} "
            f"({closest_kingdom[0]:.3f})"
        )
        print(f"Recovery accuracy: {report['recovery']['accuracy']:.2%}")
    return 0 if all(report["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

