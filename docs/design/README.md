# Design System Index

**Overall status:** Draft / pre-production

| Area | Status | Document |
|---|---|---|
| Psychological traits | Candidate model | [Traits](traits.md) |
| Animal archetypes | Schema ready; profiles incomplete | [Animals](animals/README.md) |
| Animal portfolio | Accepted for construct audit v0.3 | [Admission Gate](animal-admission-gate.md) · [Roster Audit](animal-roster-audit-v0.3.md) |
| Scoring | Architecture accepted | [Scoring](scoring.md) |
| Narrative quiz flow | Concept accepted | [Quiz Flow](quiz-flow.md) |
| Result experience | Playable deep result v0.2 | [Result Experience Bible](result-experience.md) · [Wireframe](result-wireframe.md) |
| Realm identities | Accepted for construct audit v0.2 | [Realm Identity Matrix](realm-identity-matrix.md) |
| Cross-biome constructs | Review v0.1 | [16-Anchor Audit](cross-biome-construct-audit-v0.1.md) |
| Question evidence | Sandbox contract v0.2 | [Evidence Schema](question-evidence-schema-v0.2.md) |
| Desert–Taiga boundaries | Design review v0.1 | [Boundary Question Bank](desert-taiga-boundary-bank-v0.1.md) |
| Visual theme | Prototype v0.1 | [Boreal Ceremonial](theme-system.md) |
| Animal visuals | Concept review v0.1 | [Boreal Tapestry](animal-visual-system.md) |
| Court symbols | Prototype accepted v0.1 | [Court Sigils](court-sigils.md) |

## Result examples

- [Grey Wolf full result](results/grey-wolf-example.md)
- [Reindeer full result](results/reindeer-example.md)
- [Bear full result](results/bear-example.md)
- [Moose full result](results/moose-example.md)
- [Lynx full result](results/lynx-example.md)
- [Wolverine full result](results/wolverine-example.md)

## Narrative prototype

- [Central Narrative Spine v0.1 — The First Winter](narrative-spine.md)
- [Taiga Playable Script v0.1](taiga-playable-script-v0.1.md)
- [Taiga Session Runner v0.1](session-runner.md)

## Validation reports

- [Vector Validation v0.3](../reports/vector-validation-v0.3.md) — Taiga animal separation, simulated recovery และ kingdom collision
- [Question Simulation v0.1](../reports/question-simulation-v0.1.md) — 16 narrative questions, trait coverage และ answer-to-animal recovery
- [Adaptive Simulation v0.1](../reports/adaptive-simulation-v0.1.md) — pair-specific Judgment questions, accuracy lift และ question cost
- [Cross-Biome Numeric Sandbox v0.1](../reports/cross-biome-numeric-sandbox-v0.1.md) — 16 anchors, core-only vs core+facet ablation และ residual collisions
- [Taiga–Desert Weighted Softmax v0.4](../reports/taiga-desert-weighted-softmax-v0.4.md) — weighted evidence, normalized priors, animal softmax และ realm aggregation

## Dependency order

```text
World Bible
    ↓
Trait definitions
    ↓
Kingdom + animal vectors
    ↓
Scoring prototype
    ↓
Question bank + story flow
    ↓
Adaptive selection
    ↓
Results + calibration
```

อย่าเขียน question bank จำนวนมากก่อน trait definitions และ animal vectors ผ่าน review เพราะทุกคำถามต้องอธิบายได้ว่ากำลังวัดอะไร
