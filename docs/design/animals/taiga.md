# Taiga Animal Vertical Slice

**Status:** Review v0.1  
**Last reviewed:** 2026-08-21

Taiga เชื่อว่า **competence makes us survive** แต่สัตว์ทั้งหกตอบต่างกันว่า competence มีไว้เพื่ออะไร: นำทาง ปกป้องเขตแดน สร้างที่พัก มองเห็นความจริง เปิดทางใหม่ หรือพาทุกคนเดินต่อ

## Animal Bibles

| Animal | Working title | Identity core | Bible |
|---|---|---|---|
| Grey Wolf | The Winter Strategist | Selective belonging through strategic coordination | [Read](taiga/grey-wolf.md) |
| Bear | The Keeper of the Hearth | Safety through protective responsibility | [Read](taiga/bear.md) |
| Moose | The Warden of the Threshold | Peace through visible boundaries | [Read](taiga/moose.md) |
| Lynx | The Quiet Witness | Clarity through autonomous observation | [Read](taiga/lynx.md) |
| Wolverine | The Breaker of Closed Roads | Freedom and effectiveness when systems fail | [Read](taiga/wolverine.md) |
| Reindeer | The Bearer of the Northern Road | Shared endurance and continuity | [Read](taiga/reindeer.md) |

## Trait Model v0.3 vectors

Canonical values อยู่ใน `data/vector-model.v0.3.json`

| Animal | AFF | AGY | SEN | STR | EXP | RSK | DCL | ALG |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Grey Wolf | -0.2 | +0.7 | +0.6 | +0.8 | -0.6 | -0.1 | -0.2 | +0.5 |
| Reindeer | +0.8 | -0.3 | +0.1 | +0.3 | +0.1 | -0.3 | +0.7 | +0.8 |
| Lynx | -0.9 | 0.0 | +0.5 | +0.1 | -0.9 | -0.1 | -0.1 | -0.7 |
| Bear | -0.3 | +0.3 | 0.0 | +0.6 | -0.5 | -0.8 | +0.6 | +0.6 |
| Moose | 0.0 | +0.4 | -0.2 | +0.7 | -0.3 | -0.8 | -0.5 | +0.1 |
| Wolverine | -0.7 | +0.8 | -0.4 | -0.3 | -0.1 | +0.7 | +0.1 | -0.6 |

## Pairwise distinction matrix

| Pair | Shared ground | Deciding difference |
|---|---|---|
| Wolf ↔ Bear | loyalty, preparation, quiet strength | Wolf moves the group toward an outcome; Bear makes a place where the group can survive |
| Wolf ↔ Moose | structure, authority, guarded presence | Wolf coordinates people and tradeoffs; Moose protects boundaries that should not be crossed |
| Wolf ↔ Lynx | observation, restraint, autonomy | Wolf accepts leadership and selective pack duty; Lynx protects clarity by remaining outside control |
| Wolf ↔ Wolverine | initiative, independence, competence under pressure | Wolf builds a functioning system; Wolverine acts when the system is no longer useful |
| Wolf ↔ Reindeer | group loyalty and long-range thinking | Wolf chooses a capable inner circle; Reindeer keeps the whole migration connected |
| Bear ↔ Moose | preservation, stability, grounded force | Bear bends rules for particular lives; Moose applies boundaries consistently |
| Bear ↔ Lynx | privacy, patience, low expression | Bear withdraws to protect and restore; Lynx withdraws to see and remain unclaimed |
| Bear ↔ Wolverine | tenacity and protective courage | Bear holds ground and absorbs impact; Wolverine abandons the ground to break through elsewhere |
| Bear ↔ Reindeer | duty, care, continuity | Bear creates sanctuary; Reindeer sustains movement and shared morale |
| Moose ↔ Lynx | independence and dislike of intrusion | Moose declares the line publicly; Lynx avoids the line becoming visible at all |
| Moose ↔ Wolverine | resistance to external control | Moose defends a stable territory; Wolverine refuses stability when it becomes confinement |
| Moose ↔ Reindeer | endurance and responsibility | Moose protects integrity through limits; Reindeer protects continuity through accommodation |
| Lynx ↔ Wolverine | self-authorship and frontier competence | Lynx gains freedom through distance; Wolverine gains freedom through intervention |
| Lynx ↔ Reindeer | quiet endurance | Lynx preserves self through separation; Reindeer preserves the group through connection |
| Wolverine ↔ Reindeer | survival through movement | Wolverine breaks away to create possibility; Reindeer carries obligations forward together |

## Main ambiguity cluster

```text
Grey Wolf → “Where are we going, and how do we move as one?”
Bear      → “Who needs shelter, and what must I preserve?”
Moose     → “What line keeps this place intact?”
```

หากผู้เล่นตอบเป็น Wolf/Bear/Moose ใกล้กัน Act IV ควรถามเรื่อง:

- coordinated progress vs sanctuary vs boundary
- outcome strategy vs particular care vs consistent rule
- sharing command vs carrying burden vs refusing intrusion

## Validation

- [Current scoring architecture](../scoring.md)
- [Hierarchical scoring report v0.5](../../reports/hierarchical-scoring-v0.5.md)
- Canonical core questions: `data/question-bank.v0.1.json`
- Canonical adaptive questions: `data/adaptive-question-bank.v0.1.json`

## Acceptance status

- [x] มี desire, fear, strength, shadow และ secret need ครบทั้ง 6 ตัว
- [x] ทุกคู่มี distinction statement
- [x] ไม่มีสัตว์ใดเป็น weaker version ของอีกตัว
- [x] vectors มี behavioral rationale
- [x] ทุกตัวมี ordinary และ pressure scenario
- [x] ทุกตัวมี adaptive tie-breaker seeds
- [ ] ผ่าน target-user review
- [ ] result copy ผ่าน tone and inclusivity review
