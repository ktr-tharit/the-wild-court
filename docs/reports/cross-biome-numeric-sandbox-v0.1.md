# Cross-Biome Numeric Sandbox v0.1

**Status:** Construct gate passed; facets remain provisional  
**Date:** 2026-08-22  
**Model:** `data/cross-biome-anchor-model.v0.1.json`  
**Simulation:** `scripts/simulate_cross_biome.py`  
**Test:** `python3 -m unittest -v tests/test_cross_biome.py`

## Question

8 core behavioral dimensions แยก animal anchors ทั้ง 16 ตัวได้พอหรือไม่ และ motive facets ที่พบจาก qualitative audit ลด collision ที่ตั้งใจโดยไม่ทำให้ recovery โดยรวมแย่ลงหรือไม่

## Model discipline

ค่าทั้งหมดมาจาก ordinal mapping ที่ประกาศก่อน simulation:

```text
core:  −− = −0.8, − = −0.4, 0 = 0, + = 0.4, ++ = 0.8
motive: absent = 0, supporting = 0.5, defining = 1
```

ไม่มีการปรับ decimal รายสัตว์เพื่อไล่ accuracy และใช้ observation noise เดียวกัน `σ = 0.45` กับทุก construct

Distance ถูก normalize แยกสองกลุ่ม:

```text
core-only = mean squared core distance
core+facet = mean squared core distance + 0.5 × mean squared facet distance
```

น้ำหนัก `0.5` ตรงกับ supporting-evidence tier ใน Question Evidence Schema v0.2

## Setup

- 16 anchors จาก 8 realms
- 5 motive facets: Recognition, Mastery, Reciprocity, Continuity, Restraint
- 5,000 noisy observations ต่อ animal รวม 80,000 observations
- deterministic seed `20260824`
- เปรียบเทียบ prototype เดียวกันด้วย core-only และ core+facet

## Results

| Metric | Core only | Core + facets | Lift |
|---|---:|---:|---:|
| Overall recovery | 73.90% | 81.85% | +7.95 pp |
| Critical-cluster recovery | 87.41% | 90.72% | +3.31 pp |
| Lowest animal recovery | 57.12% (Giant River Otter) | 74.36% (Orca) | +17.24 pp floor |

สัตว์ทั้ง 16 ตัวมี recovery ดีขึ้น ไม่มี per-animal regression ใน deterministic run นี้

### Intended collision clusters

| Cluster | Core only | Core + facets | Lift |
|---|---:|---:|---:|
| Grey Wolf / Golden Eagle | 87.30% | 92.15% | +4.85 pp |
| Polar Bear / Camel / Crocodile | 84.14% | 87.59% | +3.45 pp |
| Hyena / Golden Lion Tamarin / Giant River Otter | 85.35% | 88.99% | +3.65 pp |
| Arctic Fox / Fennec Fox | 95.52% | 96.55% | +1.03 pp |

Fox pair แยกได้ดีจาก core behavior อยู่แล้ว จึงได้ประโยชน์จาก motive น้อยที่สุด ส่วน Wolf/Eagle ยืนยันว่า Mastery และ Recognition ช่วยอธิบายความต่างที่ core vector มองเห็นไม่เต็ม

## Residual collisions

คู่ใกล้ที่สุดหลังเพิ่ม facets ได้แก่:

1. Giant River Otter / Orca
2. Jaguar / Wolverine
3. Crocodile / Polar Bear
4. Golden Lion Tamarin / Orca
5. Fennec Fox / Hyena

สองคู่แรกชี้ว่า motive taxonomy ปัจจุบันยังไม่มีภาษาสำหรับ:

- **chosen-bond stewardship vs immediate kin defense** — Orca และ Giant River Otter
- **boundary enforcement vs radical autonomy** — Jaguar และ Wolverine

ยังไม่เพิ่ม facet ใหม่จาก sandbox เดียว ให้เขียนสถานการณ์แยกคู่ก่อนแล้วดูว่า distinction เกิดจาก configuration ของ core traits หรือ residual motive จริง

## Interpretation

ผลผ่าน construct gate เพราะ:

- overall recovery ไม่ลดลง
- collision ทั้งสี่กลุ่มดีขึ้น
- ไม่มี animal ใด regression
- improvement เกิดจาก fixed ordinal scheme ไม่ใช่ decimal tuning

แต่ผลนี้ **ไม่ใช่ validation ของคำถามจริง** เพราะ observation ถูก sample รอบ prototype โดยตรง ยังไม่ได้พิสูจน์ว่าผู้เล่นตีความ motive wording ตามที่ออกแบบ หรือแต่ละ facet แยกจาก core dimensions ใน response data ได้จริง

ดังนั้น facets ทั้งห้ายังคงเป็น `motive_probe` ไม่ใช่ primary dimensions

## Decision

1. รับ Question Evidence Schema v0.2 เป็น sandbox authoring contract
2. คง primary vector 8 dimensions
3. เก็บ motive facets ทั้งห้าใน scoring experiment ด้วย group weight เดียว
4. เดินหน้าทำ **Taiga + Desert full cross-biome slice**
5. ใน slice ดังกล่าวต้องเขียน motive probes อย่างน้อย 3 domains และ boundary questions สำหรับ residual pairs ก่อน promote facet ใด

## Reproduce

```bash
python3 scripts/validate_question_evidence.py
python3 scripts/simulate_cross_biome.py
python3 -m unittest -v tests/test_cross_biome.py
```
