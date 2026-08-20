#!/usr/bin/env python3
"""Run a complete Taiga prototype session from opening to animal reveal."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from scripts.simulate_adaptive import load_adaptive_bank, ranked_animals
from scripts.simulate_questions import estimate_vector, load_bank
from scripts.taiga_story import load_story, merge_story, story_errors
from scripts.validate_vectors import load_model, normalized_distance


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = ROOT / "data" / "taiga-result-manifest.v0.1.json"

TAG_CALLBACKS = {
    "acted_alone": "เมื่อคนอื่นลังเล คุณมักเริ่มจากพื้นที่ที่ตัวเองรับผิดชอบได้",
    "gathered_people": "เมื่อสถานการณ์แตกออก คุณมักพยายามทำให้ผู้คนกลับมาเคลื่อนไหวร่วมกัน",
    "trusted_instinct": "คุณยอมรับข้อมูลที่ร่างกายและประสบการณ์มองเห็นก่อนจะอธิบายได้ทั้งหมด",
    "checked_evidence": "ก่อนฝากน้ำหนักไว้กับข้อสรุป คุณมักต้องการเห็นว่าหลักฐานเชื่อมกันอย่างไร",
    "kept_structure": "ภายใต้แรงกดดัน คุณสร้างขอบเขต ลำดับ หรือทางสำรองให้สิ่งต่าง ๆ ยังเดินต่อ",
    "adapted_in_motion": "คุณยอมให้คำตอบเปลี่ยนไปพร้อมสถานการณ์ แทนที่จะรักษาแผนเพียงเพราะเคยวางไว้",
    "protected_bond": "เมื่อหลักการชนกับชีวิตจริง คุณมองเห็นน้ำหนักของความสัมพันธ์เฉพาะหน้า",
    "protected_principle": "คุณพยายามรักษาหลักที่สามารถอธิบายและใช้กับทุกคนได้",
    "showed_feeling": "คุณยอมให้สิ่งที่รู้สึกกลายเป็นข้อมูลซึ่งคนอื่นมองเห็น",
    "held_feeling": "คุณมักถือความรู้สึกไว้ภายในจนกว่าจะรู้ว่าการเปิดเผยมันจำเป็น",
    "stepped_forward": "เมื่อ direction ว่างลง คุณพร้อมรับผิดชอบการขยับครั้งถัดไป",
    "supported_others": "คุณมองหาเจ้าของ direction ที่เหมาะสม และช่วยให้เขาทำหน้าที่ได้ดีขึ้น",
    "self_authored": "คุณต้องยอมรับการตัดสินใจนั้นด้วยตัวเอง ก่อนบทบาทหรือธรรมเนียมจะมีอำนาจเหนือคุณ",
    "honored_duty": "เมื่อรับบางสิ่งเป็นหน้าที่แล้ว คุณให้ความต่อเนื่องของคำมั่นมีน้ำหนักจริง",
    "kept_known": "คุณรักษาสิ่งที่พิสูจน์แล้วเมื่อความเสียหายจากการลองผิดอาจสูงเกินไป",
    "took_risk": "คุณยอมเปิดทางใหม่เมื่อเส้นทางเดิมไม่พอจะพาใครไปถึงอนาคต",
}


def load_result_manifest(path: Path = DEFAULT_RESULTS) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


class TaigaSession:
    def __init__(self) -> None:
        self.bank = load_bank()
        self.story = load_story()
        errors = story_errors(self.story, self.bank)
        if errors:
            raise ValueError("Invalid story overlay: " + "; ".join(errors))
        self.model = load_model()
        self.adaptive_bank = load_adaptive_bank()
        self.manifest = load_result_manifest()
        self.core_scenes = merge_story(self.story, self.bank)
        self.responses: list[tuple[dict[str, Any], dict[str, Any]]] = []
        self.response_audit: list[dict[str, Any]] = []
        self.tags: Counter[str] = Counter()
        self.core_index = 0
        self.judgment_questions: list[dict[str, Any]] | None = None
        self.judgment_index = 0
        self._outcome: dict[str, Any] | None = None

    @property
    def phase(self) -> str:
        if self._outcome is not None:
            return "Result"
        if self.core_index < len(self.core_scenes):
            return self.core_scenes[self.core_index]["act"]
        return "Judgment"

    @property
    def is_complete(self) -> bool:
        return self._outcome is not None

    def current_question(self) -> dict[str, Any] | None:
        if self.is_complete:
            return None
        if self.core_index < len(self.core_scenes):
            return self.core_scenes[self.core_index]
        self._prepare_judgment()
        if self.judgment_index < len(self.judgment_questions or []):
            return (self.judgment_questions or [])[self.judgment_index]
        self._finalize()
        return None

    def submit(self, option_id: str, *, question_id: str | None = None) -> None:
        question = self.current_question()
        if question is None:
            raise ValueError("Session is already complete")
        if question_id is not None and question_id != question["id"]:
            raise ValueError(f"Expected {question['id']}, received {question_id}")
        option_id = option_id.upper()
        option = next(
            (candidate for candidate in question["options"] if candidate["id"] == option_id),
            None,
        )
        if option is None:
            raise ValueError(f"{question['id']} requires one of A, B, C or D")

        self.responses.append((question, option))
        consequence_tags = option.get("consequence_tags", [])
        self.tags.update(consequence_tags)
        self.response_audit.append({
            "question_id": question["id"],
            "phase": question["act"],
            "option_id": option["id"],
            "evidence": option["evidence"],
            "consequence_tags": consequence_tags,
        })

        if self.core_index < len(self.core_scenes):
            self.core_index += 1
        else:
            self.judgment_index += 1
        self.current_question()

    def _estimate(self) -> list[float]:
        return estimate_vector(self.responses, self.model)

    def _ranking(self) -> list[str]:
        animals = {
            name: item["vector"] for name, item in self.model["animals"].items()
        }
        return ranked_animals(self._estimate(), animals)

    def _prepare_judgment(self) -> None:
        if self.judgment_questions is not None:
            return
        pair = frozenset(self._ranking()[:2])
        self.judgment_questions = [
            question for question in self.adaptive_bank["questions"]
            if frozenset(question["discriminates"]) == pair
        ]

    def _finalize(self) -> None:
        if self._outcome is not None:
            return
        estimate = self._estimate()
        animals = self.model["animals"]
        ranking = sorted(
            animals,
            key=lambda name: normalized_distance(estimate, animals[name]["vector"]),
        )
        distances = {
            name: normalized_distance(estimate, animals[name]["vector"])
            for name in ranking
        }
        primary = ranking[0]
        identity = self.manifest["animals"][primary]
        strongest_tags = sorted(self.tags.items(), key=lambda item: (-item[1], item[0]))[:3]
        self._outcome = {
            "session_version": "0.1",
            "story": self.story["title"],
            "realm": self.manifest["realm"],
            "primary_animal": primary,
            "identity": identity,
            "callbacks": [TAG_CALLBACKS[tag] for tag, _ in strongest_tags if tag in TAG_CALLBACKS],
            "questions_answered": len(self.responses),
            "adaptive_questions_answered": len(self.responses) - len(self.core_scenes),
            "continuity_tags": dict(self.tags),
            "internal": {
                "player_vector": dict(zip(
                    [dimension["id"] for dimension in self.model["dimensions"]],
                    estimate,
                )),
                "ranking": ranking,
                "distances": distances,
                "responses": self.response_audit,
            },
        }

    def public_result(self) -> dict[str, Any]:
        if not self.is_complete:
            self.current_question()
        if not self.is_complete:
            raise ValueError("Session still has unanswered questions")
        assert self._outcome is not None
        return {key: value for key, value in self._outcome.items() if key != "internal"}

    def audit_result(self) -> dict[str, Any]:
        result = self.public_result()
        assert self._outcome is not None
        return {**result, "internal": self._outcome["internal"]}


def best_option_for_vector(question: dict[str, Any], vector: list[float], model: dict[str, Any]) -> str:
    trait_index = {item["id"]: index for index, item in enumerate(model["dimensions"])}
    return min(
        question["options"],
        key=lambda option: sum(
            (vector[trait_index[trait]] - value) ** 2
            for trait, value in option["evidence"].items()
        ),
    )["id"]


def run_profile(animal_name: str) -> TaigaSession:
    session = TaigaSession()
    if animal_name not in session.model["animals"]:
        raise ValueError(f"Unknown animal {animal_name!r}")
    vector = session.model["animals"][animal_name]["vector"]
    while not session.is_complete:
        question = session.current_question()
        if question is None:
            break
        session.submit(best_option_for_vector(question, vector, session.model))
    return session


def print_question(question: dict[str, Any]) -> None:
    if question.get("setup"):
        print(f"\n{question['setup']}")
    print(f"\n{question['scenario']}\n")
    for option in question["options"]:
        print(f"  {option['id']}. {option['copy']}")


def print_reveal(result: dict[str, Any]) -> None:
    identity = result["identity"]
    print("\n" + "═" * 52)
    print(f"{result['realm'].upper()} · THE BOREAL DOMINION")
    print(f"{result['primary_animal'].upper()} — {identity['title']}")
    print(identity["identity_promise"])
    print(" · ".join(identity["signatures"]))
    if result["callbacks"]:
        print("\nWhat the Court remembers:")
        for callback in result["callbacks"]:
            print(f"- {callback}")
    print(f"\nQuestions answered: {result['questions_answered']} "
          f"({result['adaptive_questions_answered']} Judgment)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run The First Winter Taiga session")
    parser.add_argument("--auto-animal", choices=list(load_model()["animals"]), help="Run a deterministic archetype journey")
    parser.add_argument("--json", action="store_true", help="Print public result as JSON")
    parser.add_argument("--audit", action="store_true", help="Include internal scores and responses with --json")
    arguments = parser.parse_args()

    if arguments.auto_animal:
        session = run_profile(arguments.auto_animal)
    else:
        session = TaigaSession()
        print("\nTHE FIRST WINTER\n")
        for paragraph in session.story["opening"]:
            print(paragraph + "\n")
        previous_phase = None
        while not session.is_complete:
            question = session.current_question()
            if question is None:
                break
            if session.phase != previous_phase:
                previous_phase = session.phase
                if previous_phase in session.story["acts"]:
                    framing = session.story["acts"][previous_phase]
                    print(f"\n--- {framing['title']} ---\n{framing['intro']}")
                else:
                    print(f"\n--- JUDGMENT ---\n{session.story['judgment']['intro']}")
            print_question(question)
            while True:
                answer = input("\nเลือก A, B, C หรือ D: ").strip().upper()
                if answer in {"A", "B", "C", "D"}:
                    break
                print("กรุณาเลือก A, B, C หรือ D")
            session.submit(answer)
            if question.get("transition_after"):
                print(f"\n{question['transition_after']}")

    result = session.audit_result() if arguments.audit else session.public_result()
    if arguments.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_reveal(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
