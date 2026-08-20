# Vector Validation Report — v0.3

**Status:** Review  
**Run date:** 2026-08-21  
**Model:** `data/vector-model.v0.3.json`  
**Test command:** `python3 -m unittest -v tests/test_vectors.py`

## Executive summary

Trait Model v0.3 **ผ่านการทดสอบ geometry ระดับ Taiga vertical slice** แต่ **ยังไม่พร้อม Locked**

- 5 checks ผ่าน
- 1 known design check เป็น expected failure
- Taiga animals ทั้ง 6 ตัวแยกกันเหนือ minimum distance
- prototype recovery ภายใต้ simulated noise = **99.45%**
- provisional kingdom fingerprints มี collision ระหว่าง **Taiga และ Desert**
- independent kingdom centroids ไม่ควรถูกใช้เป็น scoring layer แยกจาก animal prototypes

## Test setup

ใช้ 8 dimensions:

```text
[AFF, AGY, SEN, STR, EXP, RSK, DCL, ALG]
```

ระยะทางเป็น normalized root-mean-square distance:

```text
distance(a, b) = sqrt(Σ(aₖ-bₖ)² / K)
```

Thresholds:

| Check | Threshold |
|---|---:|
| Minimum animal distance | 0.35 |
| Minimum dimension span | 0.80 |
| Minimum kingdom distance | 0.30 |
| Prototype recovery accuracy | 90% |
| Simulation noise | Gaussian σ = 0.25 |
| Samples | 5,000 per animal |

## Results

| Check | Result | Status |
|---|---:|---|
| Schema and range validation | 0 errors | Pass |
| Closest animal distance | 0.449 | Pass |
| Smallest dimension span | 1.00 | Pass |
| Prototype recovery | 99.45% | Pass |
| Closest kingdom distance | 0.200 | **Expected failure** |

## Taiga animal vectors tested

| Animal | AFF | AGY | SEN | STR | EXP | RSK | DCL | ALG |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Grey Wolf | -0.2 | +0.7 | +0.6 | +0.8 | -0.6 | -0.1 | -0.2 | +0.5 |
| Reindeer | +0.8 | -0.3 | +0.1 | +0.3 | +0.1 | -0.3 | +0.7 | +0.8 |
| Lynx | -0.9 | 0.0 | +0.5 | +0.1 | -0.9 | -0.1 | -0.1 | -0.7 |
| Bear | -0.3 | +0.3 | 0.0 | +0.6 | -0.5 | -0.8 | +0.6 | +0.6 |
| Moose | 0.0 | +0.4 | -0.2 | +0.7 | -0.3 | -0.8 | -0.5 | +0.1 |
| Wolverine | -0.7 | +0.8 | -0.4 | -0.3 | -0.1 | +0.7 | +0.1 | -0.6 |

## Closest animal pairs

| Pair | Distance | Interpretation |
|---|---:|---|
| Grey Wolf ↔ Moose | 0.449 | ใกล้สุด แต่ยังผ่าน threshold |
| Bear ↔ Moose | 0.454 | ทั้งคู่ preserving/structuring; แยกด้วย DCL และ ALG |
| Bear ↔ Grey Wolf | 0.464 | แยกด้วย preservation และ relational protection |
| Bear ↔ Reindeer | 0.540 | shared duty แต่ต่าง Affiliation/Agency |
| Lynx ↔ Wolverine | 0.610 | shared independence แต่ต่าง Agency/Risk/Structure |
| Grey Wolf ↔ Lynx | 0.614 | shared guarded analysis แต่ต่าง pack duty/control |

ใน iteration แรก Grey Wolf ↔ Moose มี distance เพียง `0.285` เพราะ Moose ถูกเขียนเหมือน Wolf ที่ preservation สูงกว่า หลังแยก Moose ให้เป็น territorial, intuitive และ impartial มากขึ้น distance เพิ่มเป็น `0.449`

## Dimension coverage

| Dimension | Span across Taiga animals | Status |
|---|---:|---|
| AFF | 1.70 | Pass |
| AGY | 1.10 | Pass |
| SEN | 1.00 | Pass |
| STR | 1.10 | Pass |
| EXP | 1.00 | Pass |
| RSK | 1.50 | Pass |
| DCL | 1.20 | Pass |
| ALG | 1.50 | Pass |

ไม่มี dimension ใดถูกใช้แคบจนไม่มีพลังแยกสัตว์ใน vertical slice นี้

## Recovery simulation

สร้าง simulated players รอบ animal prototype แต่ละตัวด้วย independent Gaussian noise `σ = 0.25` แล้ว classify ด้วย nearest prototype

| Source animal | Recovered correctly |
|---|---:|
| Grey Wolf | 98.96% |
| Reindeer | 99.86% |
| Lynx | 99.96% |
| Bear | 99.00% |
| Moose | 98.90% |
| Wolverine | 100.00% |
| **Overall** | **99.45%** |

ตัวเลขนี้พิสูจน์เพียงว่า prototypes แยกกันใน geometry ที่เรากำหนด **ไม่ได้พิสูจน์ว่า quiz จะมี accuracy 99%** เพราะ response noise จริงอาจ correlated, biased และ trait estimation จากคำถามยังไม่ได้ทดสอบ

## Known failure — Kingdom fingerprint collision

Taiga ↔ Desert มี normalized distance เพียง `0.200` ต่ำกว่า threshold `0.300` เพราะทั้งคู่ถูกนิยามเป็น guarded, analytical, structuring, preserving และ resource-disciplined

เมื่อเปรียบเทียบ animal vectors กับ provisional kingdom fingerprints ยังพบว่า:

- Reindeer ใกล้ Wetland มากกว่า Taiga
- Moose ใกล้ Desert มากกว่า Taiga
- Wolverine ใกล้ Ocean มากกว่า Taiga

นี่ไม่จำเป็นต้องแปลว่าสัตว์ถูกออกแบบผิด เพราะ animal ที่อยู่ชายขอบสามารถคล้าย archetype ต่าง biome ได้ แต่แปลว่า **ห้ามใช้ kingdom fingerprint เป็น classifier อีกชั้นหนึ่ง** ไม่เช่นนั้นระบบ animal และ biome จะให้ผลขัดกัน

### Recommended architecture

```text
Player vector
    ↓
Probability over every animal
    ↓
Biome probability = sum of its animal probabilities
    ↓
Kingdom centroid = descriptive average of the final roster only
```

Kingdom fingerprints ใน v0.3 ควรใช้เป็น world-design diagnostic เท่านั้น และค่อย replace ด้วย centroids ที่ derive จาก animal rosters ครบทุก biome

## Uniform-space diagnostic

เมื่อสุ่ม trait vectors แบบ uniform 100,000 ตัว พื้นที่ nearest-prototype แบ่งเป็น:

| Animal | Share |
|---|---:|
| Reindeer | 24.67% |
| Wolverine | 22.04% |
| Moose | 20.39% |
| Lynx | 14.24% |
| Grey Wolf | 9.71% |
| Bear | 8.96% |

นี่ไม่ใช่ predicted population เพราะมนุษย์ไม่ได้กระจาย uniform ใน trait space แต่เตือนว่า Voronoi regions มีขนาดไม่เท่ากัน หากข้อมูลจริงกระจุกคล้ายกัน อาจต้องปรับ prototypes หรือ priors หลัง calibration

## Decision

Trait Model v0.3 ยังอยู่สถานะ `Review` และพร้อมไปขั้นถัดไปคือ **question-level testing**

ก่อน lock ต้อง:

1. เขียนอย่างน้อย 2 questions ต่อ dimension
2. จำลองการ estimate player vector จาก answers แทนการ sample รอบ prototype โดยตรง
3. สร้าง animal prototypes ของ biome ที่อยู่ใกล้ Taiga อย่าง Desert, Arctic และ Alpine
4. ทดสอบ cross-biome confusion บน animal level
5. ทดลอง wording กับ target users เพื่อวัด social desirability และความเข้าใจสองขั้ว

