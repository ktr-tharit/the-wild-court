# Review Log

บันทึกสั้น ๆ ว่าแต่ละรอบตรวจอะไร เปลี่ยนอะไร และรอบหน้าควรเริ่มตรงไหน รายละเอียดการตัดสินใจสำคัญให้ไปอยู่ใน Decision Log

## 2026-08-21 — Repository foundation

- สร้าง project documentation structure
- migrate world premise, 8 kingdoms, architecture และ agreed decisions จากบทสนทนาเดิม
- เนื้อหา kingdom ทั้งหมดยังเป็น `Draft v0.1`
- รอบถัดไป: review kingdom schema แล้วเริ่มล็อก psychological traits

## 2026-08-21 — Product scope and Trait Model v0.3

- เลือก Identity Adventure route; politics เป็น setting ไม่ใช่เนื้อหาส่วนใหญ่
- redesign primary vector เป็น 8 dimensions ที่ครอบคลุม relationship, values และ duty
- ย้าย Candid ↔ Calculated ออกจาก primary vectorไปเป็น secondary facet
- เปลี่ยน story acts เป็น Arrival → Bonds → Fracture → Judgment
- รอบถัดไป: vectorize Taiga animals 6 ตัวเพื่อ stress-test model

## 2026-08-21 — Taiga vector validation

- สร้าง repeatable dataset, validation script และ automated tests
- Taiga animal separation ผ่าน; closest pair Grey Wolf/Moose = 0.449
- prototype recovery ที่ simulated noise σ 0.25 = 99.45%
- พบ expected failure: Taiga/Desert kingdom fingerprints distance 0.200
- ยืนยันว่า kingdom probability ต้อง derive จาก animal probabilities
- รอบถัดไป: question-level testing และ cross-biome animal prototypes

## 2026-08-21 — Question Bank v0.1 simulation

- เขียน fixed diagnostic bank 16 ข้อ ครบ 4 exposures ต่อ dimension
- politics/public power เหลือ 18.75% ของ content
- จำลอง 30,000 playthroughs; overall recovery = 87.92%
- ambiguity cluster หลักคือ Grey Wolf / Bear / Moose
- รอบถัดไป: human wording review และ adaptive tie-breaker questions

## 2026-08-21 — Taiga Animal Bible v0.1

- เขียน Animal Bible ครบ Grey Wolf, Bear, Moose, Lynx, Wolverine และ Reindeer
- แก้ ambiguity cluster: Wolf = direction, Bear = sanctuary, Moose = boundary
- แยก Lynx = freedom through distance ออกจาก Wolverine = freedom through intervention
- วาง Reindeer เป็น shared-continuity anchor โดยไม่เขียนเป็น passive support
- ทำ distinction matrix ครบ 15 คู่และ adaptive-question seeds รายตัว
- รอบถัดไป: เขียน Wolf/Bear/Moose tie-breakers และ human review result copy

## 2026-08-21 — Adaptive Judgment Bank v0.1

- เขียน tie-breakers 6 ข้อสำหรับ Wolf/Bear, Wolf/Moose และ Bear/Moose
- trigger rate 40.36%; average extra questions 0.81
- accuracy เพิ่ม 87.92% → 89.51%
- cluster lifts: Wolf +2.84, Bear +2.86, Moose +3.38 percentage points
- Wolf/Moose ยังเป็นคู่ยากที่สุด
- รอบถัดไป: human comprehension/social-desirability test ก่อนเพิ่ม item bank

## 2026-08-21 — Result Experience Bible v0.1

- freeze classification baseline จนกว่าจะมี human feedback
- ออกแบบ reveal: Realm → Animal → Recognition → Patterns → Shadow → Realm fit → Share
- main result ไม่แสดง exact probability หรือ unsupported rarity
- secondary realm ใช้เป็น narrative echo และยังซ่อนใน Taiga-only prototype
- เขียน full result examples สำหรับ Grey Wolf และ Reindeer
- รอบถัดไป: result visual wireframe หรือ central narrative spine

## 2026-08-21 — Result Wireframe v0.1

- แปลง Result Experience Bible เป็น mobile flow 3 ช่วง: Realm Reveal → Animal Hero → Deep Result
- ทดสอบ content hierarchy กับ Grey Wolf และ Reindeer ในโครงเดียวกัน
- แยก dark ceremonial reveal ออกจาก warm long-form reading
- ยังไม่แสดง raw vector, probability, rarity หรือ secondary realm
- รอบถัดไป: review visual hierarchy แล้วออกแบบ central narrative spine ของ quiz

## 2026-08-21 — Central Narrative Spine v0.1

- เลือก The First Winter เป็น premise ของ Taiga prototype
- ให้ผู้เล่นเป็น the Unmarked Wayfarer ซึ่งสำคัญจากการเป็นพยาน ไม่ใช่ chosen one
- map คำถาม 16 ข้อเข้า Arrival → Bonds → Fracture และใช้ adaptive questions เป็น Judgment
- กำหนด recurring cast, emotional arc, consequence tags และ ending ที่ไม่มี single villain
- เลือก remembered continuity เพื่อให้เรื่องจำการเลือกได้โดยยังรักษา scoring/testability
- รอบถัดไป: continuity rewrite ของคำถาม 16 ข้อและเขียน opening/act transitions

## 2026-08-21 — Taiga Story Overlay v0.1

- rewrite scenario ทั้ง 16 ข้อให้ต่อกันใน The First Winter โดยยังคง option evidence เดิมทุกค่า
- แยก narrative overlay ออกจาก measurement bank เพื่อลดงานรื้อเมื่อเพิ่ม biome
- เพิ่ม opening, act framing, scene transitions, Judgment transition และ consequence tags
- เพิ่ม validation ว่า story ครบทุกข้อ ลำดับถูก และไม่เปลี่ยน measurement evidence
- รอบถัดไป: สร้าง end-to-end session runner และประกอบผลลัพธ์ทั้ง 6 animals

## 2026-08-21 — Taiga Session Runner v0.1

- เชื่อม opening, 16 core scenes, scoring, adaptive Judgment และ animal reveal เป็น session เดียว
- รองรับ interactive play และ deterministic archetype journey ทั้ง 6 ตัว
- เก็บ consequence tags และสร้าง remembered callbacks ในผลลัพธ์
- แยก public reveal ออกจาก internal vector/ranking/response audit
- เพิ่ม result identity manifest ครบสัตว์ Taiga ทั้ง 6 ตัว
- รอบถัดไป: run end-to-end fixtures, ตรวจ outcome และเขียน long-form result อีก 4 ตัว

## 2026-08-21 — Boreal Ceremonial Frontend v0.1

- สร้าง frontend surface แยกใน `web/`
- ล็อก palette: Pine Night, Frosted Bone, Lichen Silver, Ember Copper และ Covenant Red
- ทำ product UI สำหรับ Opening → Arrival questions → remembered interlude
- เพิ่ม responsive mobile layout, keyboard-accessible choices และ reduced-motion behavior
- รอบถัดไป: port session runner เป็น TypeScript และเชื่อมคำถามครบ 16 ข้อ

## 2026-08-21 — Playable Taiga Web Runtime v0.1

- export canonical questions, story, vectors, adaptive bank และ result manifest เข้า frontend bundle
- port vector estimation, animal ranking และ pair-specific Judgment เป็น TypeScript
- เชื่อม flow เต็ม Opening → 16 scenes → Judgment → Realm → Animal → Result
- deterministic frontend fixtures ให้สัตว์ทั้ง 6 กลับไปยัง archetype ต้นทางได้
- เพิ่ม back, restart, local save/resume และเก็บ internal audit ออกจากหน้าผู้เล่น
- รอบถัดไป: human mobile playtest และเขียน long-form result ให้ Bear, Moose, Lynx, Wolverine

## 2026-08-21 — Taiga Deep Results v0.2

- เขียน full result profiles ครบทั้ง 6 animals โดยเพิ่ม five personal patterns, misunderstanding, shadow, restoring balance, realm fit และ closing permission
- เชื่อม structured result content เข้า canonical manifest และ frontend bundle โดยไม่เปลี่ยน scoring baseline
- ปรับหน้าอ่านผลให้ pattern cards, remembered callbacks และ animal-specific interpretation มีลำดับทางอารมณ์ชัดเจน
- visual QA ผ่าน desktop และ mobile 390px โดยไม่มี horizontal overflow หรือ browser console error
- รอบถัดไป: เพิ่ม post-result feedback และทำ target-user playtest 5–8 คน

## 2026-08-21 — Manual Blind Playthrough v0.1

- เล่นจริงผ่าน browser UI ตั้งแต่ Opening ถึง Deep Result ด้วย persona ที่กำหนดก่อนเห็นคะแนน
- เลือกครบ 16 ข้อและได้ Lynx ตรงกับ expected range โดยมี margin เหนือ Wolverine ประมาณ 0.28
- remembered callbacks สอดคล้องกับพฤติกรรมหลัก: adaptive, evidence-seeking และ emotionally private
- ไม่พบ technical blocker หรือ browser console error
- พบ observation ที่ไม่เร่งด่วน: Bonds ยาวที่สุด, Q14 มี social-desirability pressure และ mixed Thai/English ลด emotional flow
- รอบถัดไป: เลือก polish copy เฉพาะจุดหรือเดินหน้า biome ที่สองได้โดยไม่ต้องรอ human playtest

## 2026-08-21 — Court Sigils v0.1

- แทน B / F / J / T placeholders ด้วย Bonds, Fracture, Judgment และ Taiga sigils
- ล็อก visual grammar แบบเส้น Lichen Silver กับจุดตัดสินใจ Ember Copper โดยไม่พึ่งตัวอักษร
- ใช้ SVG พื้นโปร่งใสเพื่อให้คมในทุกขนาดและขยายระบบไป biome อื่นได้
- เพิ่ม restrained entry motion, one-shot response ring และรองรับ reduced motion
- visual asset review และ production build ผ่าน
- รอบถัดไป: ออกแบบ sigil ของ biome ที่สองพร้อมกับ vertical slice นั้น ไม่ต้องสร้างครบทุก biome ล่วงหน้า
