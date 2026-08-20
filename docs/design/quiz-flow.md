# Narrative Quiz Flow

**Status:** Central spine accepted for Taiga prototype  
**Last reviewed:** 2026-08-21

## Central premise

Taiga prototype ใช้ **The First Winter**: ผู้เล่นคือ the Unmarked Wayfarer ซึ่งมาถึง Hearthhold ในปีที่ฤดูหนาวมาเร็วกว่าปกติ เส้นทางและเสบียงเริ่มล้มเหลว ก่อน Keeper of the Passage จะหายตัวไป ผู้เล่นจึงถูกดึงจาก outsider ให้กลายเป็นพยานและผู้มีส่วนร่วมในวิกฤตความไว้ใจ

ดูรายละเอียด cast, scene order, continuity system และ ending ใน [Central Narrative Spine v0.1](narrative-spine.md)

## Four-act structure

### Act I — The Arrival

- 4–5 broad situations
- วัด social orientation, risk, command, expression และ world-shaping
- ลด uncertainty ระดับ biome โดยไม่ประกาศผลกลางทาง
- tone: discovery, first impressions, low-to-medium stakes

### Act II — The Bonds

- relationship and belonging situations ภายใต้แรงกดดันของ Court
- friendship, family expectation, protection requests, boundaries, public identity, divided loyalties
- แยกวิธีสร้าง trust และรักษา autonomy ภายใน biome และข้าม biome
- tone: intimacy, belonging, reputation, mutual obligation

### Act III — The Fracture

- pressure reveals values, relational priorities and shadow behavior
- betrayal, institutional injustice, scarcity, sacrifice, broken promises, irreversible choices
- politics เป็นหนึ่งใน pressure sources ร่วมกับ relationship, identity และ survival
- tone: rupture, urgency and consequence

### Act IV — The Judgment

- ระบบรู้ top candidates แล้ว
- เลือก questions ที่ discriminate candidates เหล่านั้น
- จบเมื่อ confidence/stability ถึงเกณฑ์หรือครบ maximum length
- tone: recognition and identity reveal

Taiga prototype ปัจจุบันมี [Adaptive Judgment Bank v0.1](adaptive-question-bank-v0.1.md) จำนวน 6 ข้อสำหรับ Wolf/Bear/Moose โดยผู้เล่นที่ top-two อยู่ใน cluster จะได้รับคำถามเพิ่ม 2 ข้อ

## Question design rules

- ใช้ situational choices เป็น core format
- ใช้ forced choice, ranking และ moral dilemma เป็น variation
- ทุก option ต้อง plausible และมี tradeoff
- หลีกเลี่ยง wording ที่ทำให้ผู้เล่นเลือกตัวตนในอุดมคติแทนพฤติกรรมจริง
- player-facing copy แยกจาก trait loadings และ scoring metadata
- ไม่มี option ใด map ตรงไป animal

## Story continuity metadata ที่แต่ละ question ควรมี

- Act / eligible acts
- Location
- Characters or factions involved
- Required prior event
- Consequence tags
- Tone and intensity
- Trait coverage
- Candidate pairs it discriminates
- Cooldown/repetition category

## Open decisions

- หลัง playtest จะคงชื่อ The First Winter, Hearthhold และ cast ชุดนี้หรือไม่
- branching หลัง prototype ควรเปลี่ยนเพียง dialogue/scene setup หรือเปลี่ยน event pool จริง
- minimum / maximum question count
- stopping threshold และภาษาที่ใช้อธิบาย confidence
