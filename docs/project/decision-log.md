# Decision Log

**Status:** Active  
**Last updated:** 2026-08-21

ใช้ไฟล์นี้บันทึกเฉพาะการตัดสินใจที่เปลี่ยนทิศทางหรือ architecture ของโปรเจกต์ ไม่ใช้แทน meeting notes

## D-001 — ใช้ Biome Kingdoms แทน Houses

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** โลกประกอบด้วย biome-based kingdoms และแต่ละ biome มีสัตว์หลาย archetypes
- **Reason:** ช่วยหลุดจากกรอบ 16 MBTI, ทำให้โลกเป็น ecosystem และเพิ่มสัตว์ในอนาคตได้
- **Consequence:** Kingdom เป็น broad worldview ส่วน animal เป็นวิธีที่ worldview นั้นแสดงออก

## D-002 — เริ่มจาก 8 Kingdoms

- **Date:** 2026-08-21
- **Status:** Accepted for prototype
- **Decision:** Taiga, Arctic, Savanna, Rainforest, Desert, Ocean, Alpine และ Wetland
- **Consequence:** แต่ละ kingdom ควรมีสัตว์ประมาณ 5–7 ตัว เป้าหมายรวมระยะยาวราว 40–50 results

## D-003 — ประเมิน Biome และ Animal พร้อมกัน

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** ห้าม hard classify biome กลาง quiz ใน scoring backend
- **Reason:** ผู้เล่นใกล้ boundary อาจเปลี่ยนจาก Taiga ไป Alpine หลังคำตอบช่วงท้าย
- **Consequence:** Biome probability derive จากผลรวม probability ของสัตว์ใน biome นั้น

## D-004 — ใช้ Continuous Traits ไม่ใช้ MBTI letters

- **Date:** 2026-08-21
- **Status:** Accepted; dimensions pending
- **Decision:** ผู้เล่น, kingdom และ animals มี vectors ใน psychological coordinate system เดียวกัน
- **Consequence:** เพิ่มสัตว์ได้โดยไม่สร้าง logic แบบ type-by-type ใหม่ทั้งหมด

## D-005 — MVP ใช้ Prototype Similarity Model

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** เริ่มด้วย weighted distance และ softmax; ยังไม่ใช้ ML/IRT ก่อนมีข้อมูลจริง
- **Consequence:** ต้องกำหนด vectors, weights, temperature และ priors ด้วย design judgment ก่อน แล้ว calibrate ภายหลัง

## D-006 — Story Questions วัด Traits ไม่ map ตรงไป Animal

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** คำตอบทุกตัวเลือกปรับ trait evidence และไม่มีคำตอบประเภท “A = Wolf”
- **Consequence:** ต้องเก็บ trait loadings แยกจาก player-facing copy

## D-007 — Taiga เป็น Vertical Slice แรก

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** ทำ Wolf, Reindeer, Lynx, Bear, Moose และ Wolverine ให้ครบก่อนขยาย biome อื่น
- **Reason:** roster นี้แสดงความแตกต่างภายใน biome เดียวกันได้ชัด

## D-008 — วางตำแหน่งเป็น Identity Adventure

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** เลือก product route แบบ The Wild Court Identity Adventure แทน Court Politics Personality Test
- **Reason:** ต้องการวัด identity, relationships, duty, care, boundaries และ power หลายรูปแบบสำหรับ audience กว้าง โดยเฉพาะวัย 16–30
- **Consequence:** Politics เป็น setting และ pressure source ประมาณ 20–30% ของ question bank ไม่ใช่ construct หลักของทุกคำถาม

## D-009 — ใช้ Trait Model v0.3 จำนวน 8 Dimensions

- **Date:** 2026-08-21
- **Status:** Accepted for review
- **Decision:** ใช้ Affiliation, Agency, Sensemaking, Structure, Expression, Risk Orientation, Decision Lens และ Allegiance เป็น primary vector candidate
- **Reason:** ครอบคลุมตัวตนทั้งด้านเดี่ยว/กลุ่ม, influence, cognition, uncertainty, self-expression, values และ obligation โดยไม่ผูกกับ political behavior มากเกินไป
- **Consequence:** Social Strategy ย้ายเป็น secondary facet จนกว่าจะมี evidence ว่าควรเป็น latent dimension แยก

## D-010 — Freeze Classification Baseline ก่อน Human Feedback

- **Date:** 2026-08-21
- **Status:** Accepted
- **Decision:** หยุด optimize vectors, temperature, priors และ adaptive accuracy หลัง v0.3/v0.1 จนกว่าจะมี human feedback
- **Reason:** ระบบพิสูจน์ feasibility แล้ว แต่ player-facing experience และ interpretation ยังไม่ได้รับการตรวจ
- **Consequence:** งานถัดไปเน้น result, narrative, visual และ playable experience

## D-011 — Result แสดง Identity ก่อน Measurement

- **Date:** 2026-08-21
- **Status:** Accepted for review
- **Decision:** Result reveal แสดง realm, animal, identity promise และ whole-person interpretation ก่อนข้อมูลระบบ
- **Consequence:** ไม่แสดง raw vectors, exact animal probability หรือ unsupported rarity ใน main result

## D-012 — Secondary Realm เป็น Echo ไม่ใช่ Runner-up Score

- **Date:** 2026-08-21
- **Status:** Accepted for review
- **Decision:** แสดง secondary biome เป็น narrative nuance เมื่อมี evidence ที่มั่นคง และซ่อนเมื่อ evidence อ่อน
- **Consequence:** ยังไม่แสดง secondary realm ใน Taiga-only prototype จนมี cross-biome animal rosters

## D-013 — ใช้ The First Winter เป็น Central Spine ของ Taiga Prototype

- **Date:** 2026-08-21
- **Status:** Accepted for prototype review
- **Decision:** ผู้เล่นเป็น the Unmarked Wayfarer ที่มาถึง Hearthhold ระหว่าง early winter crisis และถูกดึงเข้าสู่วิกฤตหลัง Keeper of the Passage หายตัว
- **Reason:** เชื่อมคำถามเดิมทั้ง journey, relationship, care, scarcity, identity และ public pressure โดยไม่ทำให้ politics เป็นเนื้อหาหลัก
- **Consequence:** 16 core questions ใช้ลำดับ Arrival → Bonds → Fracture; Judgment เป็น adaptive identity reflection และ prototype ใช้ remembered continuity ก่อน branching plot จริง
