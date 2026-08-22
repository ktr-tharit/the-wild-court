# Design System Index

**Overall status:** Taiga + Desert playable prototype

อ่านเฉพาะเอกสารในตารางนี้ก่อน เอกสารที่เป็น JSON คือ canonical runtime data; review sheets ที่ render จาก JSON ไม่เก็บซ้ำใน repository และสร้างใหม่จาก `scripts/render_*.py` ได้เมื่อจำเป็น

| Area | Current source of truth |
|---|---|
| Realm identities | [Realm Identity Matrix](realm-identity-matrix.md) |
| Psychological model | [Traits](traits.md) |
| Scoring | [Scoring Architecture](scoring.md) |
| Story and pacing | [Central Narrative Spine](narrative-spine.md) |
| Question evidence | [Evidence Schema](question-evidence-schema-v0.2.md) |
| Result structure | [Result Experience Bible](result-experience.md) |
| Animal admission | [Admission Gate](animal-admission-gate.md) · [Roster Audit](animal-roster-audit-v0.3.md) |
| Animal bibles | [Animal Index](animals/README.md) |
| Cross-biome coverage | [16-Anchor Construct Audit](cross-biome-construct-audit-v0.1.md) |
| Visual system | [Theme](theme-system.md) · [Animal Visuals](animal-visual-system.md) · [Court Sigils](court-sigils.md) |
| Desert visuals | [The Measured Sun](desert-visual-direction.md) |
| Rainforest visuals | [The Living Veil](rainforest-visual-direction.md) |
| Savanna visuals | [The Witnessed Sun](savanna-visual-direction.md) |

## Canonical runtime data

- Core questions: `data/question-bank.v0.1.json`
- Adaptive Taiga questions: `data/adaptive-question-bank.v0.1.json`
- Taiga–Desert boundary questions: `data/desert-taiga-boundary-bank.v0.1.json` + `v0.2.json`
- Current vectors and classifier settings: `data/vector-model.v0.5.json`
- Result content: the Taiga, Desert, Rainforest and Savanna manifests under `data/`
- Playable bundle: `web/app/game-data.generated.json`

## Current validation

- [Cross-Biome Numeric Sandbox v0.1](../reports/cross-biome-numeric-sandbox-v0.1.md) — why the 8 core dimensions and 5 motive probes were retained
- [Hierarchical Scoring v0.5](../reports/hierarchical-scoring-v0.5.md) — current soft realm → conditional animal behavior and regression metrics

Older simulations and rendered review sheets are recoverable from Git history. Their accepted conclusions live in the [Decision Log](../project/decision-log.md), so they are not part of the active reading path.

## Dependency order

```text
Realm identity → traits → animal profiles → scoring
              → story/evidence → results → calibration
```

อย่าเขียน question bank จำนวนมากก่อน realm identity, trait evidence และ animal distinctions ที่เกี่ยวข้องผ่าน review
