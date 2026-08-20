# Taiga Session Runner v0.1

**Status:** Working thin vertical slice

Runner เชื่อม story overlay, core questions, trait evidence, adaptive Judgment และ result manifest เป็น session เดียว

## Session flow

```text
Opening
→ 16 story scenes
→ estimate player vector
→ inspect top-two candidates
→ 0–2 pair-specific Judgment questions
→ final animal ranking
→ public reveal + private audit data
```

## Run interactively

```bash
python3 -m scripts.session_runner
```

## Run deterministic archetype journey

```bash
python3 -m scripts.session_runner --auto-animal "Grey Wolf"
python3 -m scripts.session_runner --auto-animal "Reindeer" --json
python3 -m scripts.session_runner --auto-animal "Bear" --json --audit
```

`--auto-animal` ไม่ใช่ accuracy simulation แต่เป็น deterministic fixture: แต่ละข้อเลือก option ที่อยู่ใกล้ prototype vector ของสัตว์นั้นที่สุด ใช้ตรวจว่า pipeline เล่นจนจบและ result render ได้

## Public vs audit output

Public result แสดง:

- Realm และ animal
- Archetype title
- Identity promise
- Signature phrases
- Narrative callbacks จาก consequence tags
- จำนวน core/Judgment questions

Audit output เพิ่ม:

- Estimated player vector
- Full animal ranking และ distances
- Response/evidence log ทุกข้อ

ข้อมูล audit เป็น internal design data และต้องไม่ปรากฏใน player-facing result

## Current limitation

- Result manifest ครบ identity reveal ทั้ง 6 ตัว แต่ full long-form result มีเฉพาะ Grey Wolf และ Reindeer
- Adaptive bank รองรับ Grey Wolf/Bear/Moose ambiguity cluster เท่านั้น
- Runner ประเมินเฉพาะสัตว์ Taiga และยังไม่ใช่ global biome classifier
- Narrative callbacks เลือกจาก tag ที่เกิดบ่อยที่สุด ยังไม่มี context-specific wording variants
