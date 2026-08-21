# Taiga–Desert Weighted Softmax Sandbox v0.4

**Status:** Engine accepted; item bank requires expansion  
**Date:** 2026-08-22  
**Model:** `data/vector-model.v0.4.json`  
**Simulation:** `scripts/simulate_taiga_desert.py`

## Decision question

เมื่อเพิ่ม Desert ครบ 6 ตัว ระบบควรใช้ weighted evidence และ softmax probabilities อย่างไรโดยไม่กลับไปใช้การบวกคะแนนเท่ากันหรือเลือกจาก average score เพียงค่าเดียว

## Accepted scoring pipeline

```text
answer evidence
→ weighted construct estimate + confidence
→ confidence-aware weighted distance to every animal
→ animal softmax probabilities with normalized priors
→ realm probability = sum of its animal probabilities
```

### 1. Weighted evidence

```text
θₖ = Σ(valueᵢₖ × evidence_weightᵢₖ) / Σ(evidence_weightᵢₖ)
cₖ = min(1, Σ evidence_weightᵢₖ / confidence_targetₖ)
```

- primary evidence: `1.0`
- secondary evidence: `0.5`
- motive probe: `0.5`
- missing construct: unobserved ไม่ใช่ zero

Weighted mean ใช้ estimate construct เท่านั้น ไม่ได้ใช้เป็น final animal score

### 2. Weighted distance

```text
D²ⱼ = Σ(ωₖ × cₖ × (θₖ − μⱼₖ)²) / Σ(ωₖ × cₖ)
```

- core construct weight `ω = 1.0`
- provisional motive weight `ω = 0.5`
- confidence ต่ำลดอำนาจของ construct ที่ evidence ยังบาง

### 3. Normalized priors and softmax

```text
prior(animal j) = 1 / realm_count × 1 / animals_in_j_realm
logitⱼ = −D²ⱼ / T + log(priorⱼ)
P(j | θ) = softmax(logitⱼ)
P(realm R) = Σ P(j | θ), j ∈ R
```

จึงไม่มี biome ใดได้เปรียบเพียงเพราะมี animal slots มากกว่า และ realm ไม่ได้ถูก hard-classify ก่อนสัตว์

## Simulation setup

- 12 animals: Taiga 6 + Desert 6
- 16 core questions
- 6 Desert–Taiga boundary questions
- 3,000 stochastic playthroughs ต่อ animal ต่อ mode
- 36,000 playthroughs ต่อ mode
- fixed seed `20260825`
- response choice ใช้ weighted option-distance softmax ที่ temperature `0.7`
- animal ranking ใช้ softmax temperature `0.2`

## Ablation results

| Mode | Question policy | Facets scored | Animal accuracy | Realm accuracy | Mean true-animal probability | Avg extra questions |
|---|---|---:|---:|---:|---:|---:|
| `core_softmax` | core 16 | no | 76.41% | 79.56% | 0.296 | 0.00 |
| `weighted_boundaries_core` | ask all 22 | no | 79.99% | 80.26% | 0.279 | 0.00 |
| `weighted_full` | ask all 22 | yes | 78.36% | 79.61% | 0.260 | 0.00 |
| `adaptive_weighted_core` | core + matching boundary | no | 76.99% | 80.11% | 0.295 | 0.44 |
| `adaptive_weighted_full` | core + matching boundary | yes | 76.95% | 80.13% | 0.294 | 0.44 |

## Findings

### Weighted questions work, but asking every boundary is not safe

การถามทั้ง 6 boundary questions เพิ่ม overall animal accuracy `+3.58 pp` แต่ Scorpion ลดจาก `71.80%` เป็น `65.07%` เพราะผู้เล่นทุกตัวถูกบังคับตอบ items ที่ไม่ได้ออกแบบสำหรับ candidate pair ของตน

ดังนั้นไม่ใช้ `weighted_boundaries_core` เป็น production policy แม้ aggregate score สูงสุด

### Adaptive weighted softmax is the current candidate

`adaptive_weighted_core`:

- เพิ่ม animal accuracy `+0.58 pp`
- เพิ่ม realm accuracy `+0.55 pp`
- ใช้คำถามเพิ่มเฉลี่ยเพียง `0.44` ข้อ
- ลด Lynx → Caracal confusion จาก `22.13%` เป็น `20.07%`
- ไม่บังคับผู้เล่นตอบ boundary questions ที่ไม่ตรงกับ top candidate pair

Camel และ Oryx ยังมี regression เล็กน้อย (`−1.37 pp`, `−0.67 pp`) แสดงว่าหนึ่ง item ต่อ boundary ยังเปราะเกินกว่าจะ lock bank

### Motive facets are not ready for final scoring

เมื่อถามทุกข้อ การเปิด motive facets ลด animal accuracy จาก `79.99%` เป็น `78.36%` และลด mean true-animal probability ด้วย สาเหตุหลักคือ:

- `RST` มีหลาย domains แต่ facet อื่นแทบไม่มี evidence
- `CON` มีเพียงหนึ่ง scenario
- animal motive values ยังเป็น design hypotheses ไม่ใช่ calibrated estimates

จึงเก็บ motive responses เป็น telemetry/construct probes แต่ไม่ใส่ final score ใน candidate mode

## Remaining collision priorities

1. Lynx / Caracal
2. Reindeer / Oryx
3. Scorpion / Moose
4. Scorpion / Caracal
5. Cobra / Moose
6. Camel / Reindeer / Bear

แต่ละ cluster ต้องมีอย่างน้อยสอง independent scenarios คนละ domain ก่อน adaptive bank lock

## Decision

1. รับ weighted evidence contract และ softmax animal/realm scoring เป็น Scoring Model v0.4 candidate
2. ใช้ `adaptive_weighted_core` เป็น default experiment
3. เก็บ motive probes แต่ไม่ score จน coverage และ ablation ผ่าน
4. ไม่ tune animal decimals เพื่อชดเชย item wording ที่ยังบาง
5. ขั้นถัดไปคือเพิ่ม boundary item คู่ที่สองให้ collision priorities แล้ว rerun แบบ paired simulation

## Reproduce

```bash
python3 scripts/simulate_taiga_desert.py
python3 -m unittest -v tests/test_taiga_desert.py
```
