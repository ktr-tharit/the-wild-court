# Scoring Architecture

**Status:** Weighted-softmax sandbox v0.4 implemented  
**Last reviewed:** 2026-08-22

## Principle

> Narrative can branch. Mathematics should stay soft.

ระบบประเมิน animal candidates ทุกตัวพร้อมกันตลอด quiz และไม่ปิด biome ใดก่อนมีหลักฐานเพียงพอ

## Prototype model

ให้ player vector เป็น `θ` และ animal `j` มี prototype vector `μⱼ`

```text
D²ⱼ = Σₖ wₖ(θₖ - μⱼₖ)²
```

แปลง similarity เป็น probability ด้วย softmax:

```text
P(j | θ) = exp(-D²ⱼ / T + bⱼ) / Σₗ exp(-D²ₗ / T + bₗ)
```

- `wₖ` — น้ำหนักของ trait
- `T` — temperature; ต่ำทำให้ winner ชัด สูงทำให้ probability กระจาย
- `bⱼ` — prior/bias สำหรับ calibration distribution โดยไม่แก้นิยามสัตว์

## v0.4 weighted evidence implementation

Question Evidence Schema v0.2 แยก `value` และ `weight`:

```text
θₖ = Σ(valueᵢₖ × evidence_weightᵢₖ) / Σ(evidence_weightᵢₖ)
cₖ = min(1, Σ evidence_weightᵢₖ / confidence_targetₖ)
```

จากนั้นใช้ confidence กับ model weight ใน distance:

```text
D²ⱼ = Σ(ωₖcₖ(θₖ − μⱼₖ)²) / Σ(ωₖcₖ)
```

Final classification ไม่เลือกจาก average score แต่ใช้:

```text
logitⱼ = −D²ⱼ / T + log(priorⱼ)
P(j | θ) = softmax(logitⱼ)
```

Prior normalize แบบ equal realm แล้ว equal animal ภายใน realm เพื่อป้องกัน roster-size bias ดู implementation ที่ `scripts/simulate_taiga_desert.py` และผลที่ `docs/reports/taiga-desert-weighted-softmax-v0.4.md`

## Biome probability

```text
P(biome B) = Σ P(j) for every animal j in B
```

ผลลัพธ์จึงสามารถแสดง primary realm, secondary realm และ top animal โดยยังรักษาความไม่แน่นอน

## Response updates — candidate accepted

- ใช้ weighted evidence estimate
- track confidence แยกต่อ construct
- ใช้ softmax probability เหนือสัตว์ทุกตัวพร้อมกัน
- motive probes ยังไม่เข้า final score จนกว่า coverage จะผ่าน

MVP ควรเริ่มจากวิธีที่อธิบายและ simulate ง่าย ก่อนเพิ่ม complexity

## Adaptive item selection — later phase

Candidate objective:

```text
QuestionScore(q)
  = InformationGain(q)
  + λ · Diversity(q)
  + γ · StoryFit(q)
  - δ · Repetition(q)
```

การเลือก purely maximum information อาจถามหัวข้อเดิมซ้ำจน pacing แย่ จึงต้องรวม game-design constraints

## Calibration checks

- animal and biome distribution
- top-1 / top-2 margin
- item discrimination
- trait coverage ต่อ playthrough
- correlation ระหว่าง traits
- response option popularity
- question drop-off
- stability เมื่อเปลี่ยนคำตอบหนึ่งข้อ

## Deferred methods

ยังไม่ใช้ neural networks, IRT หรือ MIRT ก่อนมี labelled/response data มากพอ หากมีข้อมูลแล้วจึงพิจารณา factor analysis, item parameters และ posterior-based adaptive testing
