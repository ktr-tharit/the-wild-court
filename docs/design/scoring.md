# Scoring Architecture

**Status:** Draft architecture; not implemented  
**Last reviewed:** 2026-08-21

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

## Biome probability

```text
P(biome B) = Σ P(j) for every animal j in B
```

ผลลัพธ์จึงสามารถแสดง primary realm, secondary realm และ top animal โดยยังรักษาความไม่แน่นอน

## Response updates — ยังต้องตัดสินใจ

- simple additive trait evidence
- normalized running average
- Bayesian posterior over trait vector
- confidence per dimension เมื่อจำนวน items ไม่เท่ากัน

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

