# Design System Index

**Overall status:** Draft / pre-production

| Area | Status | Document |
|---|---|---|
| Psychological traits | Candidate model | [Traits](traits.md) |
| Animal archetypes | Schema ready; profiles incomplete | [Animals](animals/README.md) |
| Scoring | Architecture accepted | [Scoring](scoring.md) |
| Narrative quiz flow | Concept accepted | [Quiz Flow](quiz-flow.md) |
| Result experience | Playable deep result v0.2 | [Result Experience Bible](result-experience.md) · [Wireframe](result-wireframe.md) |
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
