import assert from "node:assert/strict";
import test from "node:test";
import { evaluateAnswers, gameBundle, runAnimalFixture } from "../app/game-engine";

test("starts with the canonical first scene", () => {
  const session = evaluateAnswers([]);
  assert.equal(session.current?.id, "Q02");
  assert.equal(session.phase, "Arrival");
});

test("all six deterministic journeys reach a matching result", () => {
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

test("all six animals have complete deep-result content", () => {
  for (const [animal, identity] of Object.entries(gameBundle.results)) {
    assert.ok(identity.full_result, `${animal} is missing a full result document`);
    assert.equal(Object.keys(identity.patterns).length, 5);
    assert.ok(identity.misunderstanding.length > 40);
    assert.ok(identity.restoring_balance.length > 40);
    assert.ok(identity.realm_connection.length > 40);
    assert.ok(identity.closing.length > 40);
  }
});
