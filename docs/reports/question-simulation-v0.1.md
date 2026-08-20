# Question Bank Simulation Report — v0.1

**Status:** Review  
**Run date:** 2026-08-21  
**Question bank:** `data/question-bank.v0.1.json`  
**Vector model:** `data/vector-model.v0.3.json`

## Executive summary

Question bank ต้นแบบ 16 ข้อ **ผ่าน automated checks ทั้ง 6 รายการ** และพร้อมเข้าสู่ human wording review

- แต่ละ trait ถูกวัด exactly 4 ครั้ง
- ทุกคำถามวัด 2 dimensions ผ่าน 4 ideal-point options
- public-power/politics มีเพียง 3 จาก 16 ข้อ หรือ **18.75%**
- จำลอง 30,000 playthroughs ได้ classification accuracy **87.92%**
- สัตว์ทุกตัวผ่าน accuracy floor 75%
- mean absolute vector error = **0.289** ต่ำกว่าเกณฑ์ 0.35

## Question coverage

| Dimension | Exposures | Status |
|---|---:|---|
| AFF | 4 | Pass |
| AGY | 4 | Pass |
| SEN | 4 | Pass |
| STR | 4 | Pass |
| EXP | 4 | Pass |
| RSK | 4 | Pass |
| DCL | 4 | Pass |
| ALG | 4 | Pass |

## Content-domain balance

| Domain | Questions | Share |
|---|---:|---:|
| Relationship / boundaries | 4 | 25.00% |
| Identity / expression | 3 | 18.75% |
| Care / community | 3 | 18.75% |
| Uncertainty / exploration | 3 | 18.75% |
| Public power / politics | 3 | 18.75% |

Bank จึงสอดคล้องกับ Identity Adventure route: politics เป็นหนึ่งใน pressure domains แต่ไม่ใช่ majority

## Simulation method

สัตว์แต่ละ prototype ตอบคำถามผ่าน ideal-point response model:

```text
P(option | θ) ∝ exp(-distance(θ, option)² / temperature)
```

- response temperature = `0.7`
- 5,000 playthroughs ต่อสัตว์
- รวม 30,000 playthroughs
- seed = `20260823`
- estimate vector จากค่าเฉลี่ยของ evidence ใน options ที่เลือก
- classify ด้วย nearest animal prototype

Temperature 0.7 ตั้งใจให้เกิด inconsistent responses พอสมควร ไม่ได้จำลองผู้เล่นที่เลือก option ใกล้ prototype แบบสมบูรณ์ทุกครั้ง

## Classification result

| Animal | Correct classification |
|---|---:|
| Grey Wolf | 80.94% |
| Reindeer | 93.78% |
| Lynx | 90.08% |
| Bear | 82.10% |
| Moose | 85.24% |
| Wolverine | 95.38% |
| **Overall** | **87.92%** |

## Main confusion routes

| Source | Misclassified as | Rate |
|---|---|---:|
| Grey Wolf | Moose | 8.66% |
| Grey Wolf | Bear | 6.58% |
| Bear | Grey Wolf | 6.34% |
| Bear | Moose | 5.88% |
| Moose | Grey Wolf | 5.92% |
| Moose | Bear | 5.80% |
| Lynx | Wolverine | 3.60% |

ผลยืนยันว่า **Wolf–Bear–Moose เป็น ambiguity cluster หลัก**:

- ทั้งสามตัวมีแนวโน้ม structuring และ guarded
- Wolf แยกด้วย directive strategy และ analytical coordination
- Bear แยกด้วย relational protection, duty และ preservation
- Moose แยกด้วย impartial boundaries, embodied judgment และ territorial preservation

Act IV ควรมี adaptive questions ที่แยกสามคู่นี้โดยตรง แทนการเพิ่ม broad questions อีกหลายข้อ

## Vector-estimation error

| Dimension | MAE |
|---|---:|
| ALG | 0.278 |
| RSK | 0.279 |
| AGY | 0.279 |
| AFF | 0.284 |
| STR | 0.287 |
| SEN | 0.296 |
| DCL | 0.302 |
| EXP | 0.303 |

Expression และ Decision Lens มี error สูงสุดเล็กน้อย แต่ยังไม่มากพอให้เพิ่มคำถามทันที ควรตรวจ wording กับมนุษย์ก่อน เพราะ response model เชิงคณิตศาสตร์ไม่สามารถบอกได้ว่าผู้เล่นตีความ Guarded/Expressive หรือ Impartial/Relational ตามที่ designer ตั้งใจหรือไม่

## Qualitative review risks

Automated tests ไม่ตรวจปัญหาต่อไปนี้:

1. **Quadrant pattern visibility** — ทุกข้อมีสี่ options ที่แทนสองแกน ผู้เล่นอาจเริ่มเห็นสูตรหาก wording ไม่เป็นธรรมชาติ
2. **Social desirability** — Q09 ตัวเลือกช่วยกลุ่มเปราะบางและ Q15 การตามหาเด็กอาจทำให้บาง options ดู morally heroic กว่า
3. **Cultural loading** — Q08 ความฝันกับหน้าที่ครอบครัวอาจวัด cultural expectation ร่วมกับ Allegiance
4. **Reading load** — บาง options โดยเฉพาะ DCL/ALG มีความยาวและ abstraction สูงสำหรับ mobile
5. **High-stakes distortion** — Q14 และ Q15 อาจทำให้ผู้เล่นเลือกสิ่งที่อยากเชื่อว่าตนจะทำ มากกว่าพฤติกรรมจริง
6. **No adaptive Judgment items yet** — bank นี้เป็น fixed diagnostic set จึงยังไม่มี tie-breakers สำหรับ top candidates

## Decision

Question Bank v0.1 ผ่าน quantitative prototype gate แต่ยังอยู่สถานะ `Review`

ขั้นต่อไป:

1. ทำ plain-language edit ให้ทุก option อ่านจบบน mobile ได้เร็วขึ้น
2. ทำ social-desirability review โดยให้ผู้ทดสอบจัดอันดับว่า option ใดดู “ดีที่สุด”
3. เขียน adaptive tie-breakers สำหรับ Wolf/Bear/Moose อย่างน้อย 3 ข้อ
4. ทดสอบกับผู้เล่นเป้าหมายก่อนเพิ่ม question bank เกิน 16 ข้อ
5. หลังได้ human responses ค่อย estimate response temperature และ item discrimination จากข้อมูลจริง

