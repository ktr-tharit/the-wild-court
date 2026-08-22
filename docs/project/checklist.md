# Current Checklist

**Status:** Active  
**Last updated:** 2026-08-23

เอกสารนี้คือหน้าหลักสำหรับเริ่มและจบทุก design session

## Current — Portfolio-first biome expansion

- [x] เลื่อน per-biome vector tuning และ synthetic accuracy optimization ไปหลัง core portfolio ครบ
- [x] ใช้ desirability, recognition, distinction และ share intent เป็น content gate หลัก
- [x] ล็อก Rainforest roster: Jaguar, Scarlet Macaw, Orchid Mantis, Okapi, Golden Lion Tamarin, Blue Morpho
- [x] เปลี่ยน Poison Dart Frog เป็น Orchid Mantis
- [x] เขียน Rainforest Animal Bible v0.1 ครบ 6 ตัว
- [x] owner approve Rainforest identity direction for provisional playable integration
- [x] ล็อก Rainforest visual direction `The Living Veil`
- [x] สร้าง Rainforest realm background v1 และ canonical web export
- [x] Rainforest realm background v1 ผ่าน technical crop QA แต่ไม่ผ่าน owner visual review
- [x] ระบุ failure: building mass ทำให้ settlement dominate ecosystem
- [x] สร้าง ecosystem-first realm background v2 ที่ crafted structures เป็นเพียง visual accent
- [x] Rainforest realm background v2 ผ่าน technical crop QA ที่ desktop/mobile
- [x] owner re-review Rainforest realm v2: rejected เพราะ settlement หายและ rendering cinematic เกิน Taiga/Desert
- [x] เขียน Rainforest canonical portrait grammar และ visual sheets ครบ 6 ตัว
- [x] สร้าง Jaguar/Orchid Mantis calibration pair และแก้ Mantis gender-coding รอบแรก
- [x] สร้าง Rainforest animal concept portraits v1 ครบ 6 ตัว
- [x] normalize Rainforest master/web portraits เป็น `1122×1402` / `1120×1400`
- [x] สร้าง Rainforest animal visual-review route
- [x] owner review Rainforest animal concept set v1: rejected เพราะ style drift และ personal court setting ไม่ชัด
- [x] สร้าง Rainforest realm v3 แบบ ecological settlement + painterly match
- [x] Rainforest realm v3 ผ่าน technical crop QA ที่ desktop/mobile
- [x] owner review Rainforest realm v3: rejected เพราะ roots/foliage dominate และ civilization ดู temporary/โทรม
- [x] redesign realm v4 เป็น ancient inhabited waterfall court พร้อม foliage simplification contract
- [x] owner approve Rainforest realm v4 components ก่อน generation
- [x] สร้าง realm v4 และ reject เพราะ civilization ครอง frame มากเกินไป
- [x] สร้าง pulled-back Rainforest realm v5 พร้อม simplified forest masses
- [x] Rainforest realm v5 ผ่าน technical crop QA ที่ desktop/mobile
- [x] owner approve Rainforest realm v5
- [x] ล็อก Rainforest animal territory briefs v2 ครบหกเขต
- [x] regenerate Rainforest animal territory v2 ครบหกตัวโดยใช้ Lynx/Grey Wolf เป็น style references
- [x] normalize Rainforest animal v2 master/web เป็น `1122×1402` / `1120×1400`
- [x] update Rainforest animal visual-review route ให้ใช้ v2
- [x] owner approve Rainforest animal territory concept set v2 (for now)
- [x] เขียน provisional Rainforest result manifest ครบ schema ทั้งหกตัว
- [x] assign provisional vectors เพื่อ runtime integration โดยไม่ tune distribution
- [x] ต่อ Rainforest realm/animal asset paths เข้าหน้า reveal และ deep result
- [x] deterministic playable test: Jaguar → Rainforest / Jaguar ใน 18 คำถาม
- [ ] ทำ global calibration หลัง core realms และ animal portfolio พร้อม

## Now — Project organization

- [x] สร้าง project navigation
- [x] สร้าง roadmap และ review process
- [x] สร้าง decision log
- [x] ย้าย kingdom vibe และ politics ทั้ง 8 แห่งเข้า repository
- [x] สร้าง templates สำหรับ kingdom, animal และ question
- [ ] review เนื้อหาที่ migrate แล้ว และเปลี่ยน status จาก `Draft` เป็น `Review`

## Next — Lock the trait model

- [x] นิยาม candidate traits ทั้ง 8 แกน
- [x] เขียน `measures / does not measure` ทุกแกน
- [x] เขียน behavioral anchors ที่ `-1`, `0`, `+1`
- [x] แยก Affiliation ออกจาก Allegiance
- [x] แยก Agency ออกจาก Structure
- [x] ตัดสินใจคง 8 traits สำหรับ prototype
- [x] ย้าย Social Strategy เป็น secondary facet
- [x] บันทึก Trait Model v0.3 ใน Decision Log
- [ ] ทดสอบ vectors กับ Taiga animals ทั้ง 6 ตัว
- [ ] ทดสอบ kingdom fingerprint collision
- [ ] เขียนคำถามทดลองอย่างน้อย 2 ข้อต่อ dimension
- [ ] review wording กับ target users ก่อนเปลี่ยน status เป็น `Locked`

## Then — Taiga vertical slice

- [x] review roster: Wolf, Reindeer, Lynx, Bear, Moose, Wolverine
- [x] เขียน Animal Bible v0.1 ครบทั้ง 6 ตัว
- [x] กำหนด trait vectors รุ่นทดลอง v0.3
- [x] ตรวจ pairwise distinction ครบ 15 คู่
- [x] เขียนสถานการณ์ต้นแบบ 16 ข้อ
- [x] จำลอง prototype recovery และตรวจ geometry distribution
- [x] จำลอง scoring จาก noisy question responses
- [ ] human review ด้าน wording และ social desirability
- [x] เขียน adaptive tie-breakers 6 ข้อสำหรับ Wolf/Bear/Moose
- [x] จำลอง adaptive question cost และ accuracy lift
- [ ] target-user review Animal Bible และ result copy

## Realm and roster architecture

- [x] แยก player-facing realm identity ออกจาก politics และ governance
- [x] สร้าง Realm Identity Matrix v0.2 ครบ 8 realms
- [x] เขียน belonging currency, gift, shadow และ public share line ครบทุก realm
- [x] เขียน anti-overlap statements สำหรับ realm ที่ใกล้กัน
- [x] สร้าง Animal Admission Gate v0.1
- [x] audit draft roster ทุกตัวเป็น `Approve / Revise / Reserve / Cut`
- [x] เขียน qualitative `embody / resist realm` สำหรับ proposed core roster 48 slots
- [x] incorporate desirability feedback และปรับ roster เป็น v0.3
- [x] ทำ qualitative construct audit ด้วย 16 anchors จากทั้ง 8 realms
- [x] ระบุ candidate motive facets และ critical cross-realm collisions
- [x] สร้าง Question Evidence Schema v0.2 ที่แยก construct, value และ weight
- [x] ทำ numeric sandbox 16 anchors แบบ core-only เทียบ core+facet
- [x] ตรวจ per-animal regression และ critical collision clusters
- [ ] ตรวจ construct coverage กับ remaining animals หลัง anchor sandbox ผ่าน
- [ ] ทำ Taiga + Desert full cross-biome slice
- [x] ออกแบบ Desert Animal Bible architecture และ pairwise distinctions
- [x] approve Desert identity fantasy, titles และ ambiguity clusters
- [x] เขียน Desert–Taiga boundary bank ครบ 6 Desert anchors
- [x] กระจาย Desert motive probes อย่างน้อย 3 domains
- [x] แตก Desert architecture เป็น Animal Bibles รายตัว 6 ไฟล์
- [x] กำหนด provisional Desert vectors และทดสอบร่วมกับ Taiga
- [x] implement weighted evidence + confidence-aware distance + animal softmax
- [x] normalize realm likelihood ด้วย mean pooling และเลือก animal แบบ conditional ภายใน winning realm
- [x] เพิ่ม boundary item คู่ที่สองให้ Taiga–Desert collision clusters
- [x] implement expected-information-gain selector พร้อม domain diversity
- [x] ผ่าน paired regression gate และ adaptive budget ไม่เกิน 2 ข้อ
- [ ] เขียน motive probes อย่างน้อย 3 domains และ residual boundary questions
- [x] รวม weighted evidence เข้า Scoring Model v0.4 sandbox
- [x] promote Scoring Model v0.4 เข้า TypeScript scoring engine พร้อม Python parity test
- [x] promote hierarchical Scoring Model v0.5 พร้อม cross-realm coherence regression
- [x] เชื่อม information-gain selector เข้า playable session flow

## Later

- [ ] ทำ kingdom vectors ครบ 8 แห่ง
- [ ] ขยาย animal profiles ไป biome อื่น
- [x] ล็อก central story premise สำหรับ Taiga prototype
- [x] สร้าง adaptive question selection
- [x] ออกแบบ result experience architecture v0.1
- [ ] วาง telemetry และ calibration plan

## Narrative experience

- [x] ล็อก player role, central crisis และ four-act spine v0.1
- [x] map core questions 16 ข้อเข้ากับลำดับ scene
- [x] กำหนด recurring cast และ prototype ending
- [x] เลือก remembered continuity ก่อน branching plot
- [x] rewrite player-facing scenarios ให้มี continuity เดียวกันระดับ thin prototype
- [x] เขียน opening, act transitions และ result transition ระดับ prototype
- [x] เพิ่ม consequence tags ผ่าน narrative overlay โดยไม่แก้ measurement baseline
- [ ] เขียน callback variants จาก consequence tags
- [x] สร้าง end-to-end Taiga session runner
- [x] แยก public result ออกจาก internal audit output
- [x] เพิ่ม deterministic journeys สำหรับสัตว์ Taiga ทั้ง 6 ตัว
- [ ] human-test pacing และ emotional comprehension

## Frontend prototype

- [x] สร้าง web application surface
- [x] ล็อก Boreal Ceremonial theme tokens v0.1
- [x] ทำ responsive Opening, Arrival Question และ Act Interlude
- [x] ทำ palette reference drawer ใน prototype
- [x] แทน interlude/realm letter placeholders ด้วย Court Sigils 4 แบบ
- [x] เชื่อม core questions ครบ 16 ข้อกับ TypeScript scoring runtime
- [x] เชื่อม Judgment และ animal result ทั้ง 6 ตัว
- [x] สร้าง canonical web bundle จาก Python source of truth
- [x] export two-biome scoring contract: 12 animals + boundary bank 16 ข้อ
- [x] port weighted softmax, realm aggregation และ information gain เข้า TypeScript
- [x] เปลี่ยน playable flow จาก Taiga-only evaluation เป็น Taiga–Desert evaluation
- [x] เชื่อม Desert result manifest และ visual assets
- [x] ออกแบบและเชื่อม Desert Court sigil เข้ากับ realm reveal
- [x] ผ่าน automated mobile end-to-end QA สำหรับ Taiga และ Desert ที่ `390×844`
- [x] เพิ่ม back, restart และ local save/resume
- [ ] accessibility และ mobile playtest

## Result experience

- [x] ล็อก result emotional arc และ content hierarchy v0.1
- [x] กำหนด probability, rarity และ secondary-realm policies
- [x] ออกแบบ share-card content policy
- [x] เขียน full result example: Grey Wolf
- [x] เขียน full result example: Reindeer
- [x] เขียน result copy สำหรับ Bear, Moose, Lynx และ Wolverine
- [x] ทำ visual wireframe ของ realm reveal, animal hero และ result scroll
- [x] เชื่อม deep-result content เฉพาะสัตว์ครบทั้ง 6 ตัวเข้า frontend
- [ ] human-test recognition, desirability และ share intent

## Character visuals

- [x] ล็อก visual direction `Boreal Tapestry` สำหรับ prototype
- [x] สร้าง concept portrait สัตว์ Taiga ครบ 6 ตัว
- [x] เขียน shared visual grammar, palette และ stereotype guardrails
- [x] สร้างภาพ Taiga realm สำหรับ result reveal
- [x] เชื่อม realm และ animal portraits เข้ากับ result experience
- [x] ทดลอง crop ภาพใน desktop และ mobile result reveal
- [ ] target-user review ด้าน recognition, desirability และ tone
- [ ] ล็อก production art direction หลังทดสอบ biome ที่สอง
- [x] ออกแบบ Desert visual direction `The Measured Sun` ระดับ v0.1
- [x] ใช้ Desert visual direction สร้าง concept set v1 ครบ realm + animals
- [x] สร้าง Desert realm image v1 และ web asset ขนาดเดียวกับ Taiga
- [x] approve Desert realm image หลัง desktop/mobile result-layout review
- [x] สร้าง Caracal/Oryx calibration pair
- [x] สร้าง Desert animal portraits ที่เหลือครบ 6 ตัว
- [x] normalize Desert master/web portraits เป็น `1122×1402` / `1120×1400`
- [x] approve Desert animal portraits หลัง result-layout crop QA

## Parking lot

- Global political map และประวัติศาสตร์สงคราม
- Royal marriages และ resource economy ระหว่าง kingdoms
- Compatibility reports
- Shadow animal
- Expansion biomes: Mangrove, Temperate Forest, Steppe, Coral Reef, Cave
