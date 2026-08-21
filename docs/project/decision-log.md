# Decision Log

**Status:** Active  
**Last updated:** 2026-08-22

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

## D-014 — Realm Identity มาก่อน Political Identity

- **Date:** 2026-08-22
- **Status:** Accepted for roster review
- **Decision:** Realm ทุกแห่งต้องมี player-facing emotional worldview, belonging currency, desirable gift และ shadow ที่เกิดจากรากเดียวกัน ส่วน governance และ policy เป็นผลที่ worldview นั้นสร้างเมื่อขยายเป็นสังคม
- **Reason:** ผู้เล่นต้องสามารถภูมิใจกับ realm result โดยไม่จำเป็นต้องเห็นด้วยกับระบอบการเมือง และทั้ง 8 realms ต้องต่างกันในระดับ identity fantasy ไม่ใช่เพียง worldbuilding
- **Consequence:** Animal roster, result copy, visuals และ scoring construct audit ต้องอ้างอิง Realm Identity Matrix v0.2 ก่อนสร้าง biome vertical slice ถัดไป

## D-015 — Sample ทั้ง 8 Realms ก่อนทำ Biome ที่สองแบบ Full

- **Date:** 2026-08-22
- **Status:** Accepted
- **Decision:** ใช้ embody/resist anchors realm ละสองตัวเพื่อตรวจ construct coverage ก่อนเขียน Desert Animal Bible หรือ numeric vectors ครบ 48 ตัว
- **Reason:** การทดสอบ Taiga/Desert อย่างเดียวอาจทำให้ Trait Model และ scoring overfit boundary คู่แรกโดยไม่เห็น motive ที่ Savanna, Rainforest, Alpine และ Wetland ต้องใช้
- **Consequence:** ขั้นถัดไปคือ 16-anchor numeric sandbox และ motive-facet ablation; Taiga + Desert เป็น full cross-biome slice หลัง sandbox ผ่าน

## D-016 — คง 8 Core Dimensions และทดลอง Motive เป็น Supporting Facets

- **Date:** 2026-08-22
- **Status:** Accepted for sandbox
- **Decision:** คง primary behavioral vector 8 แกน และใช้ Recognition, Mastery, Reciprocity, Continuity และ Restraint เป็น motive probes น้ำหนักกลุ่ม `0.5` แทนการเพิ่มเป็น primary axes ทันที
- **Reason:** 16-anchor simulation เพิ่ม recovery จาก 73.90% เป็น 81.85%, ทำให้ critical clusters ทั้งสี่ดีขึ้น และไม่มี per-animal regression แต่ยังเป็น synthetic evidence ไม่ใช่ player-response validation
- **Consequence:** รับ Question Evidence Schema v0.2 เป็น authoring contract และเดินหน้า Taiga + Desert full slice; facets ยังไม่เข้า production score จนมีคำถามอย่างน้อย 3 domains และ question-level simulation

## D-017 — ใช้ Main / Dev / Biome Branch Hierarchy

- **Date:** 2026-08-22
- **Status:** Accepted
- **Decision:** รักษา `main` เป็น playable release, ใช้ `dev` รวม slice ที่ผ่าน tests และแตก `biome/<realm>` จาก `dev` สำหรับงานของแต่ละ realm
- **Reason:** biome slice เปลี่ยน lore, vectors, questions, results และ visuals พร้อมกัน การมี integration branch ช่วยรักษา Taiga baseline และให้ validate cross-realm behavior ก่อน release
- **Consequence:** Desert ทำบน `biome/desert` และ merge เข้า `dev`; เมื่อ integration พร้อมจึง merge `dev` เข้า `main`
