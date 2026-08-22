# Hierarchical Scoring v0.5 Report

**Date:** 2026-08-23
**Status:** Algorithm implemented; question bank unchanged

## Decision

ใช้ soft realm posterior แล้วเลือก animal แบบ conditional ภายใน winning realm แทนการผสม global top animal กับ aggregated top realm

```text
animal distance → likelihood
likelihood mean by realm → realm posterior
winning realm → conditional animal winner
```

Mean pooling normalize ด้วยจำนวนสัตว์ในแต่ละ realm จึงไม่ให้ realm ที่มี roster ใหญ่กว่าได้เปรียบอัตโนมัติ ทุก candidate ยังเปิดอยู่จน final decode

## Regression case

Synthetic case ตั้งให้ Lynx เป็น global closest animal แต่สัตว์ Desert หลายตัวมี likelihood รวมสูงกว่า:

```text
global closest: Lynx
winning realm: Desert
conditional Desert winner: Caracal
final result: Desert / Caracal
```

Python และ frontend runtime ใช้ contract เดียวกันและตรวจ invariant:

```text
realm(primary_animal) = primary_realm
```

## Seeded simulation

ใช้ seed `20260825`, 3,000 playthroughs ต่อ animal และ question/evidence bank เดิมทุกข้อ

| Mode | Animal accuracy | Realm accuracy | Mean true animal probability | Extra questions |
|---|---:|---:|---:|---:|
| Core softmax | 71.53% | 80.02% | 0.295 | 0.00 |
| Weighted boundaries, core | 74.64% | 80.72% | 0.254 | 0.00 |
| Adaptive weighted, core | 72.21% | 80.53% | 0.293 | 1.18 |
| Information gain, core | **73.21%** | **81.01%** | 0.292 | 2.00 |

Realm accuracy ของ selected mode เท่ากับ v0.4 (`81.01%`) แต่ animal accuracy ลดจาก `78.85%` เป็น `73.21%` เพราะ v0.4 ให้ global animal ชนะได้แม้ aggregated realm จะเป็นอีก biome ส่วน v0.5 บังคับ result coherence ตาม product contract ใหม่

## Scope boundary

- ไม่เพิ่ม ไม่ลบ และไม่ rewrite คำถาม
- ไม่เปลี่ยน question evidence
- ไม่ tune animal vectors หรือ temperature
- ไม่เพิ่ม within-realm adaptive questions

Animal discrimination จะกลับมาทำหลัง realm content และ session pacing ผ่าน review แล้ว
