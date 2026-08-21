#!/usr/bin/env python3
"""Compare core-only and core-plus-motive recovery for 16 realm anchors."""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = ROOT / "data" / "cross-biome-anchor-model.v0.1.json"


def load_model(path: Path = DEFAULT_MODEL) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def model_errors(model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    core_count = len(model.get("core_dimensions", []))
    facet_count = len(model.get("motive_facets", []))
    animals = model.get("animals", {})
    if len(animals) != 16:
        errors.append(f"expected 16 anchors, found {len(animals)}")
    realms: dict[str, list[str]] = {}
    for name, animal in animals.items():
        realms.setdefault(animal.get("realm", ""), []).append(animal.get("role", ""))
        core = animal.get("core", [])
        facets = animal.get("facets", [])
        if len(core) != core_count:
            errors.append(f"{name} has {len(core)} core values; expected {core_count}")
        if len(facets) != facet_count:
            errors.append(f"{name} has {len(facets)} facets; expected {facet_count}")
        if any(value not in {-0.8, -0.4, 0.0, 0.4, 0.8} for value in core):
            errors.append(f"{name} uses a non-ordinal core value")
        if any(value not in {0.0, 0.5, 1.0} for value in facets):
            errors.append(f"{name} uses a non-ordinal facet value")
    if len(realms) != 8:
        errors.append(f"expected 8 realms, found {len(realms)}")
    for realm, roles in realms.items():
        if sorted(roles) != ["embody", "resist"]:
            errors.append(f"{realm} must contain one embody and one resist anchor")
    names = set(animals)
    for cluster in model.get("critical_clusters", []):
        if len(cluster) < 2 or not set(cluster).issubset(names):
            errors.append(f"invalid critical cluster: {cluster}")
    return errors


def mean_squared_distance(left: list[float], right: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(left, right)) / len(left)


def candidate_distance(
    observed_core: list[float],
    observed_facets: list[float],
    candidate: dict[str, Any],
    *,
    include_facets: bool,
    facet_group_weight: float,
) -> float:
    core_distance = mean_squared_distance(observed_core, candidate["core"])
    if not include_facets:
        return core_distance
    facet_distance = mean_squared_distance(observed_facets, candidate["facets"])
    return core_distance + facet_group_weight * facet_distance


def classify(
    observed_core: list[float],
    observed_facets: list[float],
    animals: dict[str, dict[str, Any]],
    *,
    include_facets: bool,
    facet_group_weight: float,
    candidates: list[str] | None = None,
) -> str:
    pool = candidates or sorted(animals)
    return min(
        pool,
        key=lambda name: (
            candidate_distance(
                observed_core,
                observed_facets,
                animals[name],
                include_facets=include_facets,
                facet_group_weight=facet_group_weight,
            ),
            name,
        ),
    )


def noisy(
    values: list[float],
    sigma: float,
    generator: random.Random,
    *,
    lower: float,
    upper: float,
) -> list[float]:
    return [
        max(lower, min(upper, value + generator.gauss(0.0, sigma)))
        for value in values
    ]


def pairwise_distances(model: dict[str, Any], include_facets: bool) -> list[dict[str, Any]]:
    animals = model["animals"]
    weight = model["facet_group_weight"]
    names = sorted(animals)
    rows = []
    for index, left in enumerate(names):
        for right in names[index + 1:]:
            distance = candidate_distance(
                animals[left]["core"],
                animals[left]["facets"],
                animals[right],
                include_facets=include_facets,
                facet_group_weight=weight,
            )
            rows.append({"left": left, "right": right, "distance": math.sqrt(distance)})
    return sorted(rows, key=lambda row: (row["distance"], row["left"], row["right"]))


def simulate(model: dict[str, Any]) -> dict[str, Any]:
    settings = model["simulation"]
    generator = random.Random(settings["seed"])
    animals = model["animals"]
    weight = model["facet_group_weight"]
    samples = settings["samples_per_animal"]
    sigma = settings["observation_noise_sigma"]
    modes = ("core_only", "core_plus_facets")
    correct = {mode: 0 for mode in modes}
    confusion = {
        mode: {source: {target: 0 for target in animals} for source in animals}
        for mode in modes
    }
    cluster_correct = {
        mode: {" / ".join(cluster): 0 for cluster in model["critical_clusters"]}
        for mode in modes
    }
    cluster_totals = {
        " / ".join(cluster): len(cluster) * samples
        for cluster in model["critical_clusters"]
    }

    for source, profile in animals.items():
        for _ in range(samples):
            observed_core = noisy(
                profile["core"], sigma, generator, lower=-1.0, upper=1.0
            )
            observed_facets = noisy(
                profile["facets"], sigma, generator, lower=0.0, upper=1.0
            )
            for mode in modes:
                predicted = classify(
                    observed_core,
                    observed_facets,
                    animals,
                    include_facets=mode == "core_plus_facets",
                    facet_group_weight=weight,
                )
                confusion[mode][source][predicted] += 1
                correct[mode] += predicted == source
            for cluster in model["critical_clusters"]:
                if source not in cluster:
                    continue
                cluster_name = " / ".join(cluster)
                for mode in modes:
                    predicted = classify(
                        observed_core,
                        observed_facets,
                        animals,
                        include_facets=mode == "core_plus_facets",
                        facet_group_weight=weight,
                        candidates=sorted(cluster),
                    )
                    cluster_correct[mode][cluster_name] += predicted == source

    total = len(animals) * samples
    accuracy = {mode: correct[mode] / total for mode in modes}
    per_cluster_accuracy = {
        mode: {
            name: count / cluster_totals[name]
            for name, count in cluster_correct[mode].items()
        }
        for mode in modes
    }
    critical_accuracy = {
        mode: sum(cluster_correct[mode].values()) / sum(cluster_totals.values())
        for mode in modes
    }
    per_animal = {
        mode: {
            source: confusion[mode][source][source] / samples for source in animals
        }
        for mode in modes
    }
    return {
        "seed": settings["seed"],
        "samples_per_animal": samples,
        "observation_noise_sigma": sigma,
        "accuracy": accuracy,
        "overall_lift": accuracy["core_plus_facets"] - accuracy["core_only"],
        "critical_cluster_accuracy": critical_accuracy,
        "critical_cluster_lift": critical_accuracy["core_plus_facets"] - critical_accuracy["core_only"],
        "per_cluster_accuracy": per_cluster_accuracy,
        "per_animal_accuracy": per_animal,
        "nearest_pairs": {
            "core_only": pairwise_distances(model, False)[:10],
            "core_plus_facets": pairwise_distances(model, True)[:10],
        },
        "confusion": {
            mode: {
                source: {
                    target: count / samples
                    for target, count in row.items()
                    if count
                }
                for source, row in table.items()
            }
            for mode, table in confusion.items()
        },
    }


def build_report(model: dict[str, Any]) -> dict[str, Any]:
    errors = model_errors(model)
    result = simulate(model) if not errors else None
    checks = {
        "schema": not errors,
        "overall_non_regression": bool(result and result["overall_lift"] >= 0.0),
        "critical_collision_lift": bool(result and result["critical_cluster_lift"] > 0.0),
    }
    return {
        "model_version": model.get("model_version"),
        "checks": checks,
        "schema_errors": errors,
        "simulation": result,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args()
    report = build_report(load_model(arguments.model))
    if arguments.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Cross-biome anchor sandbox v{report['model_version']}")
        for name, passed in report["checks"].items():
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        if report["simulation"]:
            result = report["simulation"]
            print(f"Core-only accuracy: {result['accuracy']['core_only']:.2%}")
            print(f"Core+facet accuracy: {result['accuracy']['core_plus_facets']:.2%}")
            print(f"Overall lift: {result['overall_lift']:+.2%}")
            print(f"Critical-cluster lift: {result['critical_cluster_lift']:+.2%}")
    return 0 if all(report["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
