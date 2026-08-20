# Adaptive Judgment Simulation Report — v0.1

**Status:** Review  
**Run date:** 2026-08-21  
**Core bank:** `data/question-bank.v0.1.json`  
**Adaptive bank:** `data/adaptive-question-bank.v0.1.json`  
**Vector model:** `data/vector-model.v0.3.json`

## Executive summary

Adaptive Judgment Bank v0.1 ผ่าน automated checks ทั้ง 5 รายการ

- เพิ่มคำถาม 6 ข้อ: 2 ข้อต่อ ambiguity pair
- ถามเฉพาะเมื่อ top two เป็น Wolf/Bear, Wolf/Moose หรือ Bear/Moose
- trigger rate = **40.36%** ของ playthroughs
- ผู้เล่นทุกคนเฉลี่ยได้รับคำถามเพิ่มเพียง **0.81 ข้อ**
- accuracy รวมเพิ่มจาก **87.92% → 89.51%**
- Grey Wolf, Bear และ Moose ดีขึ้นทุกตัว

## Adaptive bank structure

| Pair | Questions | Main dimensions |
|---|---:|---|
| Grey Wolf ↔ Bear | 2 | DCL, RSK, SEN |
| Grey Wolf ↔ Moose | 2 | SEN, ALG, AGY |
| Bear ↔ Moose | 2 | DCL, ALG, SEN |

ผู้เล่นที่ trigger จะได้รับคำถามของ top-two pair จำนวน 2 ข้อ หลัง core bank 16 ข้อ

## Accuracy lift

| Animal | Core only | With adaptive | Lift |
|---|---:|---:|---:|
| Grey Wolf | 80.56% | 83.40% | +2.84 pp |
| Reindeer | 93.80% | 93.88% | +0.08 pp |
| Lynx | 90.22% | 90.58% | +0.36 pp |
| Bear | 81.64% | 84.50% | +2.86 pp |
| Moose | 85.50% | 88.88% | +3.38 pp |
| Wolverine | 95.82% | 95.84% | +0.02 pp |
| **Overall** | **87.92%** | **89.51%** | **+1.59 pp** |

Lift รวมดูไม่ใหญ่มากเพราะ Reindeer, Lynx และ Wolverine ไม่ได้เป็นเป้าหมายของ bank และแทบไม่ถูกถามเพิ่ม ผลที่ต้องดูคือ cluster animals ดีขึ้นพร้อมกันโดยไม่ทำร้ายผลอื่น

## Question cost

| Animal source | Average extra questions |
|---|---:|
| Grey Wolf | 1.65 |
| Bear | 1.45 |
| Moose | 1.66 |
| Reindeer | 0.03 |
| Lynx | 0.04 |
| Wolverine | 0.01 |
| **Overall** | **0.81** |

ระบบจึงรักษา playthrough ส่วนใหญ่ไว้ที่ 16 ข้อ และเพิ่มเป็น 18 ข้อเมื่อพบ ambiguity cluster

## Confusion changes

| Route | Core only | Adaptive | Change |
|---|---:|---:|---:|
| Wolf → Bear | 6.82% | 4.48% | -2.34 pp |
| Wolf → Moose | 8.92% | 8.30% | -0.62 pp |
| Bear → Wolf | 5.80% | 4.48% | -1.32 pp |
| Bear → Moose | 6.42% | 4.84% | -1.58 pp |
| Moose → Wolf | 5.78% | 4.46% | -1.32 pp |
| Moose → Bear | 5.38% | 3.20% | -2.18 pp |

Bear/Moose tie-breakers มีผลชัดที่สุด ส่วน Wolf/Moose ยังแยกได้ยาก แสดงว่าคู่ดังกล่าวอาจต้องวัด construct ที่ vector ปัจจุบันจับไม่เต็ม เช่น:

- strategic tradeoff vs non-negotiable integrity
- willingness to redesign a boundary for group outcome
- responsibility for coordinating people vs responsibility for holding a line

หาก human test ยืนยัน pattern นี้ อาจเพิ่ม secondary facet ด้าน `Outcome Optimization ↔ Boundary Integrity` หรือเขียน item ที่แยกสองแนวคิดนี้โดยไม่เพิ่ม latent dimension ทันที

## Simulation rule

```text
Answer 16 core questions
        ↓
Rank animal prototypes
        ↓
If top-two pair ∈ {Wolf/Bear, Wolf/Moose, Bear/Moose}
        ↓ yes
Ask its 2 Judgment questions
        ↓
Re-estimate vector and rank again
```

Simulation ใช้ response temperature `0.7`, 5,000 playthroughs ต่อสัตว์ รวม 30,000 และ seed `20260824`

## Limitations

- Question response model รู้ ideal-point mapping ที่ designer กำหนด จึงยังไม่ทดสอบว่ามนุษย์ตีความ option ตรงกัน
- ระบบเลือกจาก top-two nearest prototypes ไม่ใช่ expected information gain เต็มรูปแบบ
- ยังไม่มี stopping rule จาก probability margin หรือ posterior uncertainty
- มีเพียง Taiga animals; cross-biome candidates อาจเปลี่ยนว่า tie-breaker ใด informative ที่สุด
- Accuracy lift อาจเปลี่ยนมากหลังปรับ response temperature จากข้อมูลจริง

## Decision

Adaptive Judgment Bank v0.1 ผ่าน prototype gate แต่ยังอยู่สถานะ `Review`

ขั้นต่อไปที่ให้ข้อมูลมากที่สุดไม่ใช่เพิ่มคำถามอีกทันที แต่คือ **human comprehension and social-desirability test** ของ core 16 + adaptive 6 เพื่อดูว่า options วัด construct ตามที่ตั้งใจหรือเพียงวัดว่าคำตอบใดดูดี

