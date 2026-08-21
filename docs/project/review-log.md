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

## 2026-08-22 — Realm Identity Matrix v0.2

- แยก emotional worldview ที่ผู้เล่นได้รับออกจาก politics ที่ใช้สร้าง story pressure
- ล็อก core fantasy, belonging currency, gift, hardened shadow และ public share line ครบทั้ง 8 realms
- เพิ่ม anti-overlap ระหว่าง Taiga/Desert/Alpine, Arctic/Wetland, Rainforest/Ocean และคู่ใกล้เคียงอื่น
- ยืนยันว่า realm ไม่ map หนึ่งต่อหนึ่งกับ 8 dimensions และต้อง derive จาก animal evidence
- เพิ่ม shareability gate ระดับ realm ก่อนเริ่มสร้าง roster 40–50 ตัว
- รอบถัดไป: สร้าง Animal Admission Gate แล้ว audit roster เป็น `Keep / Revise / Cut / Candidate`

## 2026-08-22 — Animal Admission Gate and Roster Audit v0.2

- สร้าง admission gate 7 ด้าน: desire, identity, visual, ecology, distinction, realm dialectic และ prestige parity
- audit draft roster ทุกตัวและเสนอ core portfolio สูงสุด 48 slots โดยไม่บังคับเติม quota
- เก็บ Taiga และ Savanna เดิม, sharpen species ใน Arctic/Ocean/Alpine และ rebuild Rainforest/Wetland บางส่วน
- ตัด Panther ซึ่งซ้ำ Jaguar, Alligator ซึ่งซ้ำ Crocodile และ generic Frog result
- เพิ่ม embody/resist relationship และ qualitative trait direction ให้ทุก proposed animal
- ระบุ cross-realm collision risks 10 clusters สำหรับ construct audit รอบถัดไป
- รอบถัดไป: review emotional desirability ของ replacements แล้วทำ construct coverage โดยยังไม่ใส่ numeric vectors

## 2026-08-22 — Roster Desirability Revision v0.3

- เพิ่ม beauty prestige ใน Rainforest ด้วย Golden Lion Tamarin และ Blue Morpho แทน Orangutan/Tapir
- เพิ่มความหลากหลายด้าน scale และ silhouette ใน Ocean ด้วย Green Sea Turtle แทน Whale และ Great White แทน Hammerhead
- ลด bird count ของ Alpine ด้วย Red Panda แทน Himalayan Monal
- เปลี่ยน Axolotl เป็น Giant River Otter เพื่อให้ Wetland มี relational result ที่ active และทรงพลังขึ้น
- ecology spot-check ผ่านสำหรับ candidate ใหม่ทั้งหมด แต่ Red Panda ถูกระบุว่าเป็น high-elevation mountain forest ไม่ใช่ above-tree-line alpine
- รอบถัดไป: review working titles และ nearest-pair desirability ก่อน construct coverage

## 2026-08-22 — Cross-Biome Construct Audit v0.1

- เลือก sample ทั้ง 8 realms ก่อนทำ Taiga/Desert แบบ full เพื่อหลีกเลี่ยง architecture overfit
- audit 16 anchors แบบ embody/resist พร้อม desire, fear, relationship strategy, qualitative traits และ question seeds
- ยืนยันว่า 8 core dimensions อธิบาย behavioral style ได้ดีและยังไม่ควรถูกตัด
- พบ motive gaps 5 กลุ่ม: Recognition, Mastery, Reciprocity, Continuity และ Restraint
- พบ collision สำคัญที่ core traits อย่างเดียวอาจแยกไม่พอ: Wolf/Eagle, Polar Bear/Camel/Crocodile, Hyena/Tamarin/Giant Otter และ Arctic Fox/Fennec
- รอบถัดไป: Question Evidence Schema v0.2 และ numeric sandbox แบบ core-only เทียบ core+facet

## 2026-08-22 — Question Evidence Schema + Numeric Sandbox v0.1

- แยก `construct`, `value`, `weight` และ `role` ใน evidence contract v0.2
- กำหนด motive เป็น ordinal `0 / 0.5 / 1` และ weight tier คงที่ แทน decimal tuning
- simulate 16 anchors × 5,000 observations ด้วย seed คงที่
- overall recovery เพิ่ม 73.90% → 81.85%; critical-cluster recovery เพิ่ม 87.41% → 90.72%
- animal ทั้ง 16 ตัวดีขึ้นโดยไม่มี per-animal regression
- residual collisions หลักคือ Otter/Orca และ Jaguar/Wolverine
- ยืนยัน 8 core dimensions; motive facets ยังเป็น probes ไม่ใช่ production axes
- รอบถัดไป: Taiga + Desert full cross-biome slice พร้อม motive questions และ boundary cases

## 2026-08-22 — Desert Architecture + Branch Workflow

- approve identity fantasy และ working titles ของ Desert ทั้ง 6 ตัว
- แยก portfolio ด้วยสิ่งที่แต่ละ archetype ไม่ยอมใช้โดยไร้ความหมาย: attention, dignity, consequence, capacity, access และ desire
- approve Boundary cluster: Caracal/Cobra/Scorpion
- approve Restraint cluster: Fennec/Camel/Oryx
- ตั้ง `dev` เป็น integration branch และ `biome/desert` เป็น working branch ของ slice นี้
- รอบถัดไป: เขียน cross-realm boundary questions แล้วแตก Animal Bibles รายตัว

## 2026-08-22 — Desert–Taiga Boundary Bank v0.1

- เขียน boundary scenarios 6 ข้อ ครบ Fennec, Caracal, Cobra, Camel, Scorpion และ Oryx
- แยก Fennec/Lynx/Wolverine, Caracal/Lynx/Moose, Cobra/Moose, Camel/Reindeer, Scorpion/Lynx/Wolverine และ Oryx/Bear
- ใช้ Question Evidence Schema v0.2 โดยแยก value และ weight จริง
- motive probes ครอบคลุม identity expression, public power และ care/community
- schema, Desert-anchor coverage, domain coverage และ generated-document tests ผ่าน
- รอบถัดไป: แตก Animal Bibles รายตัวและตั้ง provisional Desert vectors ก่อน question-level simulation

## 2026-08-22 — Desert Animal Bibles v0.1

- แตก Fennec, Caracal, Cobra, Camel, Scorpion และ Oryx เป็น Bible รายตัวครบ
- เพิ่ม court role, kingdom fit, qualitative trait rationale, cross-realm distinctions, adaptive seeds, visual direction และ result-page draft
- รักษา prestige fantasy ของทุกตัวโดยไม่ใช้ predator/prey hierarchy
- Camel ถูกกำหนดเป็น deliberate generosity, Scorpion เป็น compact sovereignty และ Oryx เป็น radiant enoughness
- ยังไม่ใส่ decimal vectors เพื่อป้องกันการ tune ทีละตัวก่อนเห็น Taiga–Desert space ร่วมกัน
- รอบถัดไป: สร้าง provisional 12-animal model และรัน pairwise/recovery simulation

## 2026-08-22 — Taiga–Desert Weighted Softmax v0.4

- สร้าง provisional model 12 animals พร้อม core vectors และ motive metadata
- implement primary `1.0`, secondary `0.5`, motive-probe `0.5` evidence weights
- ใช้ confidence-aware weighted distance, normalized priors และ softmax animal probabilities
- realm probability มาจากผลรวม probability ของสัตว์ ไม่ hard-split biome ก่อน
- core softmax baseline: animal 76.41%, realm 79.56%
- adaptive weighted core: animal 76.99%, realm 80.11%, extra questions เฉลี่ย 0.44
- asking all boundary questions ได้ animal 79.99% แต่ทำให้ Scorpion regression จึงไม่ใช้เป็น default
- motive facets ลด aggregate performance เมื่อเปิดทุกข้อ จึงยังเป็น telemetry เท่านั้น
- รอบถัดไป: เพิ่ม independent boundary item คู่ที่สองให้ collision clusters แล้ว rerun

## 2026-08-22 — Boundary Bank v0.2 + Information Gain

- เพิ่ม boundary questions 10 ข้อ รวม bank เป็น 16 ข้อ
- collision หลักทุก cluster มีอย่างน้อย 2 scenarios และอย่างน้อย 2 domains
- เปลี่ยน simulation เป็น paired random streams เพื่อเทียบ mode โดย core responses เดียวกัน
- implement expected information gain จาก softmax posterior และ predicted option likelihoods
- บังคับ adaptive domain diversity และงบสูงสุด 2 questions
- core softmax baseline: animal 76.83%, realm 80.02%
- information-gain core: animal 78.85%, realm 81.01%, extra questions 2.00
- Reindeer ลด 0.50 pp; animal อื่นดีขึ้นทั้งหมด จึงผ่าน no-regression tolerance 1 pp
- motive facets ยังลดผลรวม จึงคงเป็น telemetry
- รอบถัดไป: integrate Scoring Model v0.4 และ selector เข้า session/runtime

## 2026-08-22 — Two-Biome Frontend Scoring Runtime

- อัปเกรด generated web bundle เป็น v0.2 พร้อม Scoring Model v0.4, สัตว์ Taiga–Desert 12 ตัว และ Boundary Bank 16 ข้อ
- port weighted evidence, confidence-aware distance, normalized priors, animal softmax และ realm aggregation เข้า TypeScript
- port expected-information-gain selector พร้อม minimum gain, adaptive budget 2 ข้อ และ domain diversity
- เพิ่ม golden parity test เทียบ Python: all-A core path ได้ Scorpion/Desert และเลือก DTB09 → DTB04
- frontend build และ engine tests ผ่าน; playable page ยังใช้ Taiga result flow จนกว่า Desert result manifest จะพร้อม
- รอบถัดไป: เชื่อม scoring runtime เข้ากับ session state จากนั้นทำ Desert result manifest และ visual system

## 2026-08-22 — Desert Visual Direction v0.1

- เสนอ `The Measured Sun` ระดับ Review v0.1: mineral gouache, dry-brush pigment, cut-paper shadow geometry, sun-worn textile และ oxidized copper
- ใช้ light/shade เป็นภาษาของ chosen visibility, protected access และ capacity แทน desert spectacle
- กำหนด canonical palette, realm composition, material language และ stereotype guardrails ของสัตว์ทั้ง 6 ตัว
- เพิ่ม shareability gate ที่ไม่ผูก desirability กับ dominance, sexualization, wealth หรือ combat coding
- กำหนด production order: realm image → Caracal/Oryx calibration pair → Scorpion/Cobra → Camel/Fennec
- รอบถัดไป: generate และ review Desert realm image ก่อนสร้าง animal portraits

## 2026-08-22 — Desert Realm Image v1

- สร้างภาพ The Sunless Crown จาก `The Measured Sun` โดยใช้ Taiga realm เป็น reference เฉพาะ framing, abstraction level และ typography negative space
- refinement รอบสองลด architectural realism เป็น mineral-gouache planes และ cut-paper shadow shapes เพื่อให้ coherent กับ Boreal Tapestry
- เก็บ master `1536×1024` ที่ `assets/concept-art/desert/desert-realm-v1.png`
- export web JPEG `1400×933` ที่ `web/public/biomes/desert/realm-v1.jpg` เท่ากับ Taiga web asset
- รอบถัดไป: วางภาพใน result layout เพื่อตรวจ desktop/mobile crop แล้วสร้าง Caracal/Oryx calibration pair

## 2026-08-22 — Desert Realm Result-Layout QA

- เพิ่ม internal review route ที่ `/visual-review/desert-realm` โดยใช้ reveal layout และ overlay จริง
- desktop `1280×720` รักษา typography negative space, city identity และ contrast ได้ครบ
- mobile `390×844` ใช้ Desert-specific `object-position: 52% center`; escarpment, title และ CTA ไม่ชนกัน
- approve Desert realm image v1 สำหรับ result reveal; Desert sigil ใน review route ยังเป็น geometric placeholder
- รอบถัดไป: สร้าง Caracal/Oryx calibration pair เพื่อ approve visual direction ทั้งระบบ

## 2026-08-22 — Desert Animal Portrait Set v1

- ตั้ง Lynx เป็น canonical animal asset size: master `1122×1402`, web `1120×1400`, aspect ratio `4:5`
- สร้าง Fennec Fox, Caracal, Cobra, Camel, Scorpion และ Oryx ด้วย built-in ImageGen แยก prompt รายตัว
- ใช้ Lynx เป็น reference เฉพาะ framing/render density และ Desert realm เป็น reference เฉพาะ palette/material language
- สัตว์ใหญ่แสดง mass ภายใน subject box เดียวกัน; Cobra/Scorpion ใช้ anatomy-specific composition โดยไม่เปลี่ยน canvas
- reject Scorpion draft แรกที่อ่านเป็น giant/horror และ refine ให้ body mass เบาลง ก้ามสงบ และมี negative space มากขึ้น
- export master PNG และ web JPEG ครบทุกตัวโดยไม่มี size exception
- รอบถัดไป: ทำ animal result visual-review route และตรวจ desktop/mobile crops ทั้ง 6 ตัว

## 2026-08-22 — Desert Animal Result-Layout QA

- เพิ่ม internal review route `/visual-review/desert-animals` พร้อม selector สัตว์ 6 ตัว
- desktop `1280×720` ตรวจครบทั้ง 6 ตัว: subject scale, silhouette, title wrapping และ crop ผ่าน
- mobile `390×844` ตรวจ Fennec/Oryx/Cobra/Scorpion เป็นตัวแทน ears, horns, vertical coil และ wide body; ไม่มี critical crop
- approve Desert animal portrait set v1 สำหรับ result use
- รอบถัดไป: สร้าง Desert result manifest แล้วเชื่อม two-biome runtime เข้ากับ playable flow

## 2026-08-22 — Two-Realm Playable Result Flow v0.3

- เพิ่ม Desert result manifest ครบ Fennec Fox, Caracal, Cobra, Camel, Scorpion และ Oryx โดยมี deep-result contract เท่ากับ Taiga
- รวม manifest ทั้งสอง realm และ animal 12 ตัวเข้า generated web bundle v0.3
- เปลี่ยน playable session จาก average-distance Taiga-only เป็น confidence-aware weighted softmax และ normalized realm aggregation
- Judgment เลือกคำถามทีละข้อจาก expected information gain, จำกัด 2 ข้อ และรักษา domain diversity
- realm reveal, animal reveal และ deep result เลือกภาพ copy และ visual treatment ตาม Taiga/Desert จริง
- deterministic journeys ของสัตว์ทั้ง 12 ตัวกลับไปยัง archetype ต้นทาง และ all-A parity ยังได้ Scorpion / Desert ผ่าน DTB09 → DTB04
- browser QA แบบ end-to-end ผ่านทั้ง all-A Desert/Scorpion และ deterministic Taiga/Grey Wolf รวม interlude, Judgment, realm, animal และ deep result
- รอบถัดไป: ออกแบบ Desert Court sigil แทน geometric placeholder แล้วทำ mobile end-to-end pass

## 2026-08-22 — Desert Court Sigil + Mobile QA

- เพิ่ม Desert sigil: measured sun เหนือ layered shade และ copper drop ที่ถูกปกป้องตรงกลาง
- ใช้ shared `160×160` canvas, lichen stroke, copper living center และ transparent background เหมือน Court Sigils เดิม
- แทน geometric placeholder ใน playable realm reveal และ Desert realm review route
- mobile `390×844` ผ่าน end-to-end ทั้ง all-A Desert/Scorpion และ deterministic Taiga/Grey Wolf
- realm glyph, backdrop crop, animal portrait, long animal heading, signature chips และ deep-result hero ไม่มี critical overflow หรือ crop
- รอบถัดไป: review share action และออกแบบ share-card artifact ที่ผู้เล่นบันทึกหรือส่งต่อได้จริง
