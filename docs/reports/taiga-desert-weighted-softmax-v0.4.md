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
- Boundary Bank v0.2: 16 Desert–Taiga questions across independent domains
- 3,000 stochastic playthroughs ต่อ animal ต่อ mode
- 36,000 playthroughs ต่อ mode
- paired seed `20260825`: core responses ของ animal/playthrough เดียวกันเหมือนกันข้ามทุก mode
- response choice ใช้ weighted option-distance softmax ที่ temperature `0.7`
- animal ranking ใช้ softmax temperature `0.2`
- information-gain selector เลือกไม่เกิน 2 items และไม่ซ้ำ domain

## Ablation results

| Mode | Question policy | Facets scored | Animal accuracy | Realm accuracy | Mean true-animal probability | Avg extra questions |
|---|---|---:|---:|---:|---:|---:|
| `core_softmax` | core 16 | no | 76.83% | 80.02% | 0.295 | 0.00 |
| `weighted_boundaries_core` | ask all 32 | no | 82.47% | 80.72% | 0.254 | 0.00 |
| `weighted_full` | ask all 32 | yes | 78.86% | 80.45% | 0.232 | 0.00 |
| `adaptive_weighted_core` | exact pair matching | no | 77.64% | 80.53% | 0.293 | 1.18 |
| `adaptive_weighted_full` | exact pair matching | yes | 77.59% | 80.79% | 0.290 | 1.18 |
| `information_gain_core` | entropy reduction + domain diversity | no | 78.85% | 81.01% | 0.292 | 2.00 |
| `information_gain_full` | entropy reduction + domain diversity | yes | 78.73% | 80.58% | 0.289 | 2.00 |

## Findings

### Weighted questions work, but asking every boundary is not the product policy

การถามทั้ง 16 boundary questions เพิ่ม animal accuracy `+5.64 pp` แต่ใช้ 32 questions กับผู้เล่นทุกคน, mean true-animal probability ลด และไม่ตอบโจทย์ pacing ของ identity adventure

ดังนั้นใช้ mode นี้เป็น upper-bound diagnostic ไม่ใช่ production policy แม้ aggregate top-1 สูงสุด

### Information gain is the current candidate

`information_gain_core` คำนวณ expected entropy reduction จาก current animal softmax posterior และ predicted answer likelihood ของแต่ละ item:

- เพิ่ม animal accuracy `+2.02 pp`
- เพิ่ม realm accuracy `+0.99 pp`
- ใช้ adaptive budget 2 ข้อ
- สัตว์ 11 ตัวดีขึ้น; Reindeer ลดเพียง `0.50 pp` ซึ่งผ่าน tolerance `1 pp`
- domain-diversity constraint ป้องกัน adaptive questions สองข้อถามสถานการณ์ประเภทเดียวกัน

Mean true-animal probability ลด `0.003` แม้ top-1 ดีขึ้น แปลว่า softmax temperature ยังไม่ควรถูกอ้างเป็น calibrated confidence จนมี response data จริง

### Motive facets are not ready for final scoring

เมื่อถามทุกข้อ การเปิด motive facets ลด animal accuracy จาก `82.47%` เป็น `78.86%`; ใน information-gain mode ลดจาก `78.85%` เป็น `78.73%` และ realm accuracy ลดด้วย สาเหตุหลักคือ:

- `RST` มีหลาย domains แต่ facet อื่นแทบไม่มี evidence
- `CON` มีเพียงหนึ่ง scenario
- animal motive values ยังเป็น design hypotheses ไม่ใช่ calibrated estimates

จึงเก็บ motive responses เป็น telemetry/construct probes แต่ไม่ใส่ final score ใน candidate mode

## Boundary coverage achieved

1. Lynx / Caracal
2. Reindeer / Oryx
3. Scorpion / Moose
4. Scorpion / Caracal
5. Cobra / Moose
6. Camel / Reindeer / Bear

แต่ละ cluster มีอย่างน้อยสอง independent scenarios และสอง domains แล้ว แต่ frequency จาก information gain ไม่เท่ากัน บางข้อไม่ถูกเลือกใน synthetic posterior ปัจจุบัน จึงยังเก็บไว้สำหรับ story-fit/manual review แทนการลบทิ้งจาก simulation เดียว

## Decision

1. รับ weighted evidence contract และ softmax animal/realm scoring เป็น Scoring Model v0.4 candidate
2. ใช้ `information_gain_core` พร้อม domain diversity เป็น default experiment
3. เก็บ motive probes แต่ไม่ score จน coverage และ ablation ผ่าน
4. ไม่ tune animal decimals เพื่อชดเชย item wording ที่ยังบาง
5. Boundary regression gate ผ่าน ขั้นถัดไปคือ integrate v0.4 engine/selector เข้า session runtime โดยยังไม่แสดง softmax probability เป็น calibrated certainty

## Reproduce

```bash
python3 scripts/simulate_taiga_desert.py
python3 -m unittest -v tests/test_taiga_desert.py
```
