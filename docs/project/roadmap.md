# Design Roadmap

**Status:** Draft  
**Last reviewed:** 2026-08-21

## Workflow หลัก

> World → Traits → Animal vectors → Probability model → Story situations → Adaptive questions → Results → Calibration

## Phase 0 — Project foundation

- สร้าง repository structure และ navigation
- แยก source of truth ออกจาก discussion history
- สร้าง checklist, decision log, review process และ templates

**Exit condition:** คนที่ไม่เคยอ่าน chat เดิมสามารถเปิด README แล้วตามสถานะโปรเจกต์ได้

## Phase 1 — World Bible

- ล็อก 8 kingdoms และชื่อชั่วคราว
- นิยาม governing philosophy, political structure, virtue, vice, taboo, rule, relations และ aesthetic
- ตรวจความต่างและความขัดแย้งระหว่าง kingdoms
- กำหนดเหตุการณ์กลางของโลกภายหลัง โดยยังไม่เขียนประวัติศาสตร์ยาวเกินจำเป็น

**Exit condition:** kingdom ทุกแห่งตอบ schema เดียวกันครบและไม่มีสองแห่งที่ทำหน้าที่ซ้ำกัน

## Phase 2 — Psychological coordinate system

- นิยาม 6–8 continuous traits
- ระบุสิ่งที่แต่ละ trait วัดและไม่วัด
- ตรวจ overlap เช่น Affiliation vs Allegiance และ Agency vs Structure
- สร้าง behavioral anchors ที่ `-1`, `0`, `+1`

**Exit condition:** ทีมสามารถให้คะแนนพฤติกรรมตัวอย่างได้ใกล้เคียงกันโดยไม่ต้องเดา

## Phase 3 — Kingdom and animal vectors

- ให้ kingdom ทุกแห่งมี prototype vector
- ทำ Taiga animals 6 ตัวเป็น vertical slice
- เขียน desire, fear, strength, shadow, court role และ stress behavior
- ตรวจระยะห่างระหว่างสัตว์และขอบเขตระหว่าง biome

**Exit condition:** Taiga roster แยกกันชัดและเป็น template ให้ biome อื่นได้

## Phase 4 — Scoring prototype

- คำนวณ player trait vector จาก responses
- ใช้ weighted distance + softmax similarity
- derive biome probability จากผลรวมของ animal probabilities
- ทดลอง temperature, weights และ priors

**Exit condition:** simulation ให้ผลสมเหตุผลและไม่กระจุกที่สัตว์ไม่กี่ตัว

## Phase 5 — Story and question bank

- ล็อก central premise และ 4-act flow
- เขียน core question bank 60–100 items ในระยะยาว
- ทำ prototype 16–20 ข้อก่อน
- กำหนด trait loading, story tags และ candidate discrimination ของทุก option

**Exit condition:** prototype เล่นจบได้โดยคำถามไม่ซ้ำอารมณ์และเรื่องราวต่อกันได้

## Phase 6 — Adaptive engine and result experience

- เลือกคำถามตาม information gain + diversity + story fit - repetition
- กำหนด stopping rule และ confidence language
- สร้าง primary, secondary และ shadow result
- ออกแบบ result card และ share loop

## Phase 7 — Calibration

- ตรวจ result distribution และ item discrimination
- ตรวจ trait correlation และ redundant dimensions
- เก็บ self-identification feedback โดยไม่ถือเป็น ground truth เพียงอย่างเดียว
- พิจารณา EFA/CFA และ IRT/MIRT เมื่อข้อมูลมากพอ
