import assert from "node:assert/strict";
import test from "node:test";

async function render(path = "/") {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  return worker.fetch(new Request(`http://localhost${path}`, { headers: { accept: "text/html" } }), { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } }, { waitUntil() {}, passThroughOnException() {} });
}

test("renders The Wild Court product shell", async () => {
  const response = await render();
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /The Wild Court/);
  assert.match(html, /Winter remembers/);
  assert.match(html, /Cross the threshold/);
  assert.match(html, /Taiga · Desert · Rainforest · Savanna prototype/);
  assert.doesNotMatch(html, /codex-preview|react-loading-skeleton|Building your site/);
});

test("renders the Desert realm visual review", async () => {
  const response = await render("/visual-review/desert-realm");
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /The Sunless Crown/);
  assert.match(html, /\/biomes\/desert\/realm-v1\.jpg/);
  assert.match(html, /\/sigils\/desert\.svg/);
  assert.match(html, /Want less\. Waste nothing\. Owe carefully\./);
});

test("renders the Desert animal visual review", async () => {
  const response = await render("/visual-review/desert-animals");
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const animal of ["Fennec Fox", "Caracal", "Cobra", "Camel", "Scorpion", "Oryx"]) assert.match(html, new RegExp(animal));
  assert.match(html, /\/animals\/desert\/fennec-fox-v1\.jpg/);
  assert.match(html, /1122×1402/);
});

test("renders the Rainforest animal visual review", async () => {
  const response = await render("/visual-review/rainforest-animals");
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const animal of ["Jaguar", "Scarlet Macaw", "Orchid Mantis", "Okapi", "Golden Lion Tamarin", "Blue Morpho"]) assert.match(html, new RegExp(animal));
  assert.match(html, /\/animals\/rainforest\/jaguar-v2\.jpg/);
  assert.match(html, /1122×1402/);
  assert.match(html, /THE VERDANT EMPIRE/);
});

test("renders the Savanna realm visual review", async () => {
  const response = await render("/visual-review/savanna-realm");
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /The Golden Crown/);
  assert.match(html, /\/biomes\/savanna\/realm-v1\.jpg/);
  assert.match(html, /\/sigils\/savanna\.svg/);
  assert.match(html, /I was not made to disappear\./);
});

test("renders the Savanna animal visual review", async () => {
  const response = await render("/visual-review/savanna-animals");
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const animal of ["Lion", "Elephant", "Secretary Bird", "Hyena", "Greater Kudu", "Giraffe"]) assert.match(html, new RegExp(animal));
  assert.match(html, /\/animals\/savanna\/lion-v1\.jpg/);
  assert.match(html, /1122×1402/);
  assert.match(html, /THE GOLDEN CROWN/);
});
