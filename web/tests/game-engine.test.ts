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

test("all twelve deterministic journeys reach a matching two-realm result", () => {
  for (const animal of Object.keys(gameBundle.animals)) {
    const session = runAnimalFixture(animal);
    assert.equal(session.result?.primary_animal, animal);
    assert.ok((session.result?.questions_answered ?? 0) >= 16);
    assert.ok((session.result?.questions_answered ?? 0) <= 18);
  }
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

test("all twelve animals have complete deep-result content", () => {
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
  assert.equal(afterCore.current?.id, "DTB09");
  assert.equal(afterCore.phase, "Judgment");

  const afterFirstJudgment = evaluateAnswers(Array(17).fill("A"));
  assert.equal(afterFirstJudgment.current?.id, "DTB04");

  const complete = evaluateAnswers(Array(18).fill("A"));
  assert.equal(complete.result?.primary_animal, "Scorpion");
  assert.equal(complete.result?.realm.name, "Desert");
  assert.equal(complete.result?.realm.title, "The Sunless Crown");
});

test("two-biome weighted softmax probabilities are normalized", () => {
  const responses = gameBundle.core_scenes.map((question) => ({
    evidence: question.options[0].evidence,
  }));
  const result = scoreResponses(responses);
  const animalTotal = Object.values(result.animal_probabilities).reduce((sum, value) => sum + value, 0);
  const realmTotal = Object.values(result.realm_probabilities).reduce((sum, value) => sum + value, 0);
  assert.equal(Object.keys(result.animal_probabilities).length, 12);
  assert.ok(Math.abs(animalTotal - 1) < 1e-12);
  assert.ok(Math.abs(realmTotal - 1) < 1e-12);
  assert.equal(result.top_animal, "Scorpion");
  assert.equal(result.top_realm, "Desert");
  assert.ok(Math.abs(result.realm_probabilities.Desert - 0.5599716888982768) < 1e-12);
});

test("information gain selection matches the Python reference and respects its budget", () => {
  const responses = gameBundle.core_scenes.map((question) => ({
    evidence: question.options[0].evidence,
  }));
  const first = selectNextBoundaryQuestion(responses);
  assert.equal(first?.question.id, "DTB09");
  assert.ok(Math.abs((first?.information_gain ?? 0) - 0.14255324114236045) < 1e-12);

  responses.push({ evidence: first!.question.options[0].evidence });
  const second = selectNextBoundaryQuestion(
    responses,
    [first!.question.id],
    [first!.question.domain],
  );
  assert.equal(second?.question.id, "DTB04");
  assert.notEqual(second?.question.domain, first?.question.domain);

  const exhausted = selectNextBoundaryQuestion(
    responses,
    [first!.question.id, second!.question.id],
    [first!.question.domain, second!.question.domain],
  );
  assert.equal(exhausted, null);
});
