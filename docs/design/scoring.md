# Scoring Architecture

**Status:** Hierarchical weighted-softmax sandbox v0.5 implemented
**Last reviewed:** 2026-08-23

## Principle

> Narrative can branch. Mathematics should stay soft.

ระบบประเมิน animal candidates ทุกตัวพร้อมกันตลอด quiz และไม่ปิด biome ใดก่อนมีหลักฐานเพียงพอ

## Shared evidence model

ให้ player vector เป็น `θ` และ animal `j` มี prototype vector `μⱼ`

```text
D²ⱼ = Σₖ wₖ(θₖ - μⱼₖ)²
```

แปลง distance เป็น unnormalized animal likelihood:

```text
Lⱼ = exp(-D²ⱼ / T)
```

- `wₖ` — น้ำหนักของ trait
- `T` — temperature; ต่ำทำให้ winner ชัด สูงทำให้ probability กระจาย
- realm และ animal ใช้ evidence ชุดเดียวกันใน v0.5; ยังไม่มีคำถามหรือ vector ใหม่

## Weighted evidence implementation

Question Evidence Schema v0.2 แยก `value` และ `weight`:

```text
θₖ = Σ(valueᵢₖ × evidence_weightᵢₖ) / Σ(evidence_weightᵢₖ)
cₖ = min(1, Σ evidence_weightᵢₖ / confidence_targetₖ)
```

จากนั้นใช้ confidence กับ model weight ใน distance:

```text
D²ⱼ = Σ(ωₖcₖ(θₖ − μⱼₖ)²) / Σ(ωₖcₖ)
```

## v0.5 hierarchical classification

ห้ามเลือก global top animal แล้วนำ realm มาต่อภายหลัง เพราะ animal เดี่ยวสามารถขัดกับ evidence รวมของ realm ได้ ระบบแบ่งการตัดสินเป็นสองระดับโดยไม่ hard-lock biome ระหว่าง session

Realm score ใช้ค่าเฉลี่ย likelihood ของสัตว์ใน realm เพื่อ normalize roster size:

```text
S_B = (1 / |A_B|) Σⱼ∈B Lⱼ
P(B | θ) = S_B / Σ_C S_C
```

ภายในแต่ละ realm normalize สัตว์แบบ conditional:

```text
P(j | B, θ) = Lⱼ / Σₗ∈B Lₗ
```

Final decode เป็น hierarchical:

```text
B* = argmax_B P(B | θ)
j* = argmax_{j∈B*} P(j | B*, θ)
```

ดังนั้น global closest animal อาจอยู่คนละ realm กับผลสุดท้ายได้ เช่น Lynx เป็น global closest แต่ Desert มี evidence รวมสูงกว่า ระบบต้องคืนสัตว์ Desert ที่ใกล้ที่สุด เช่น Caracal ไม่ใช่ Lynx แห่ง Desert

`P(j | θ) = P(B | θ)P(j | B, θ)` ยังเก็บไว้สำหรับ information gain และ diagnostics แต่ไม่ override hierarchical final decode

Frontend parity implementation อยู่ที่ `web/app/game-engine.ts` และรับ canonical model จาก generated bundle v0.4 โดยมี regression case สำหรับ global Lynx / Desert / conditional Caracal ทั้ง Python และ TypeScript

ระบบยังประเมินทุก realm และสัตว์พร้อมกันตลอด session การเลือก realm ก่อน animal เกิดเฉพาะ final decoding ไม่ใช่การปิด candidate กลาง quiz

## Response updates — candidate accepted

- ใช้ weighted evidence estimate
- track confidence แยกต่อ construct
- ใช้ mean animal likelihood เพื่อสร้าง soft realm posterior โดยไม่ให้ roster ใหญ่กว่าได้เปรียบ
- เลือก animal แบบ conditional ภายใน winning realm
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

### v0.5 information-gain candidate

Boundary Bank v0.2 ใช้ current animal softmax posterior เป็น prior สำหรับแต่ละ item:

```text
P(option o | q) = Σⱼ P(j)P(o | j, q)
P(j | o, q) ∝ P(j)P(o | j, q)
IG(q) = H(P(j)) − Σₒ P(o | q)H(P(j | o, q))
```

Selector เลือก item ที่ `IG` สูงสุดแบบ sequential หลังเห็นคำตอบจริง โดย:

- ไม่เกิน 2 adaptive questions
- ไม่ถาม domain ซ้ำใน adaptive phase เดียวกัน
- หยุดเมื่อ information gain ต่ำกว่า `0.01`
- motive evidence เก็บเป็น telemetry แต่ไม่เข้า final score

นี่เป็น information criterion สำหรับ measurement; narrative runtime ยังต้องตรวจ story position และ repetition กับฉากก่อนแสดงคำถามจริง

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
