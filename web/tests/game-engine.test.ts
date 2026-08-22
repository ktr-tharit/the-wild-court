import assert from "node:assert/strict";
import test from "node:test";
import {
  evaluateAnswers,
  gameBundle,
  runAnimalFixture,
  scoreResponses,
  selectNextBoundaryQuestion,
} from "../app/game-engine";

test("starts with the canonical first scene", () => {
  const session = evaluateAnswers([]);
  assert.equal(session.current?.id, "Q02");
  assert.equal(session.phase, "Arrival");
});

test("all twenty-four deterministic journeys reach a realm-coherent result", () => {
  for (const animal of Object.keys(gameBundle.animals)) {
    const session = runAnimalFixture(animal);
    const resultAnimal = session.result?.primary_animal ?? "";
    assert.ok(resultAnimal in gameBundle.animals);
    assert.equal(session.result?.realm.name, gameBundle.animals[resultAnimal].kingdom);
    assert.ok((session.result?.questions_answered ?? 0) >= 16);
    assert.ok((session.result?.questions_answered ?? 0) <= 18);
  }
});

test("winning realm selects its closest conditional animal instead of the global animal", () => {
  const bundle = structuredClone(gameBundle);
  for (const [animal, profile] of Object.entries(bundle.scoring.animals)) {
    profile.core[0] = profile.realm === "Taiga" ? 1 : 0.3;
    if (animal === "Lynx") profile.core[0] = 0;
    if (animal === "Caracal") profile.core[0] = 0.2;
  }
  const result = scoreResponses([{ evidence: { AFF: 0 } }], bundle);
  const globalClosest = Object.keys(result.animal_probabilities).sort((left, right) =>
    result.animal_probabilities[right] - result.animal_probabilities[left])[0];

  assert.equal(globalClosest, "Lynx");
  assert.equal(result.top_realm, "Desert");
  assert.equal(result.top_animal, "Caracal");
  assert.equal(bundle.scoring.animals[result.top_animal].realm, result.top_realm);
});

test("public flow requires 16 core answers before result", () => {
  const session = evaluateAnswers(Array(15).fill("A"));
  assert.equal(session.result, null);
  assert.equal(session.core_answered, 15);
});

test("result contains callbacks and an eight-dimensional audit vector", () => {
  const session = runAnimalFixture("Grey Wolf");
  assert.ok(session.callbacks.length > 0);
  assert.equal(Object.keys(session.result?.internal.vector ?? {}).length, 8);
});

test("all twenty-four animals have complete deep-result content", () => {
  for (const [animal, identity] of Object.entries(gameBundle.results)) {
    assert.ok(identity.full_result, `${animal} is missing a full result document`);
    assert.equal(Object.keys(identity.patterns).length, 5);
    assert.ok(identity.misunderstanding.length > 40);
    assert.ok(identity.restoring_balance.length > 40);
    assert.ok(identity.realm_connection.length > 40);
    assert.ok(identity.closing.length > 40);
  }
});

test("playable flow uses information-gain Judgment and returns a dynamic realm", () => {
  const afterCore = evaluateAnswers(Array(16).fill("A"));
  assert.equal(afterCore.current?.id, "DTB11");
  assert.equal(afterCore.phase, "Judgment");

  const afterFirstJudgment = evaluateAnswers(Array(17).fill("A"));
  assert.equal(afterFirstJudgment.current?.id, "DTB06");

  const complete = evaluateAnswers(Array(18).fill("A"));
  assert.equal(complete.result?.primary_animal, "Greater Kudu");
  assert.equal(complete.result?.realm.name, "Savanna");
  assert.equal(complete.result?.realm.title, "The Golden Crown");
});

test("four-realm weighted softmax probabilities are normalized", () => {
  const responses = gameBundle.core_scenes.map((question) => ({
    evidence: question.options[0].evidence,
  }));
  const result = scoreResponses(responses);
  const animalTotal = Object.values(result.animal_probabilities).reduce((sum, value) => sum + value, 0);
  const realmTotal = Object.values(result.realm_probabilities).reduce((sum, value) => sum + value, 0);
  assert.equal(Object.keys(result.animal_probabilities).length, 24);
  assert.ok(Math.abs(animalTotal - 1) < 1e-12);
  assert.ok(Math.abs(realmTotal - 1) < 1e-12);
  for (const probabilities of Object.values(result.conditional_animal_probabilities)) {
    assert.ok(Math.abs(Object.values(probabilities).reduce((sum, value) => sum + value, 0) - 1) < 1e-12);
  }
  assert.equal(Object.keys(result.realm_probabilities).length, 4);
});

test("Lion fixture completes the playable flow with a Savanna result", () => {
  const session = runAnimalFixture("Lion");
  assert.equal(session.result?.realm.name, "Savanna");
  assert.equal(session.result?.realm.title, "The Golden Crown");
  assert.equal(session.result?.primary_animal, "Lion");
  assert.equal(session.result?.identity.title, "The Crown in Full View");
  assert.ok((session.result?.questions_answered ?? 0) >= 16);
  assert.ok((session.result?.questions_answered ?? 0) <= 18);
});

test("every Savanna animal has a locked playable smoke path", () => {
  const paths: Record<string, string> = {
    Lion: "CDDDDDBDBCADDBDCDA",
    Elephant: "BDDDDDDCDDDBDDBDAD",
    "Secretary Bird": "DDDBDDABBDBDDADDDC",
    Hyena: "CCBBBCBCACAACADCBD",
    "Greater Kudu": "AAAAAAAAAAAAAAAACA",
    Giraffe: "BCBDCABCBBBBCBADAA",
  };
  for (const [animal, path] of Object.entries(paths)) {
    const session = evaluateAnswers([...path]);
    assert.equal(session.result?.realm.name, "Savanna", `${animal} path left Savanna`);
    assert.equal(session.result?.primary_animal, animal, `${animal} path resolved to another animal`);
  }
});

test("Jaguar fixture completes the playable flow with a Rainforest result", () => {
  const session = runAnimalFixture("Jaguar");
  assert.equal(session.result?.realm.name, "Rainforest");
  assert.equal(session.result?.realm.title, "The Verdant Empire");
  assert.equal(session.result?.primary_animal, "Jaguar");
  assert.equal(session.result?.identity.title, "The Sovereign Under Leaves");
  assert.equal(session.result?.questions_answered, 18);
});

test("information gain selection matches the Python reference and respects its budget", () => {
  const responses = gameBundle.core_scenes.map((question) => ({
    evidence: question.options[0].evidence,
  }));
  const first = selectNextBoundaryQuestion(responses);
  assert.equal(first?.question.id, "DTB11");
  assert.ok(Math.abs((first?.information_gain ?? 0) - 0.1100482265322611) < 1e-12);

  responses.push({ evidence: first!.question.options[0].evidence });
  const second = selectNextBoundaryQuestion(
    responses,
    [first!.question.id],
    [first!.question.domain],
  );
  assert.equal(second?.question.id, "DTB06");
  assert.notEqual(second?.question.domain, first?.question.domain);

  const exhausted = selectNextBoundaryQuestion(
    responses,
    [first!.question.id, second!.question.id],
    [first!.question.domain, second!.question.domain],
  );
  assert.equal(exhausted, null);
});
