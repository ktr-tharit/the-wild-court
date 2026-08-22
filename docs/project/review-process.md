# Review Process

**Status:** Active  
**Last reviewed:** 2026-08-21

## Document statuses

- `Seed` — ไอเดียตั้งต้น ยังไม่ควรนำไปพึ่งพา
- `Draft` — มีเนื้อหาใช้งานได้ แต่ยังเปลี่ยนได้มาก
- `Review` — พร้อมให้ตรวจ consistency และตัดสินใจ
- `Locked` — เป็น source of truth สำหรับงาน downstream
- `Deprecated` — เก็บไว้เป็นประวัติ แต่ไม่ควรใช้อ้างอิง

## ก่อนเริ่ม session

1. เปิด [Current Checklist](checklist.md)
2. เลือกงานหนึ่งกลุ่มจาก `Now` หรือ `Next`
3. อ่าน Decision Log เฉพาะรายการที่เกี่ยวข้อง
4. เปิดเอกสาร source of truth ที่จะได้รับผลกระทบ

## ก่อนจบ session

1. ย้ายข้อสรุปจาก chat/notes เข้าเอกสารหลัก
2. อัปเดตสถานะและ `Last reviewed`
3. อัปเดต checklist
4. เพิ่ม decision record หาก architecture หรือ vocabulary เปลี่ยน
5. ตรวจ links และคำศัพท์สำคัญให้ตรงกัน

ไม่เก็บ chronological review log แยกอีกชุด: checklist บอก current state, Decision Log เก็บเหตุผลที่ยังมีผล และ Git history เก็บลำดับกิจกรรม

## Review gates

### World gate

- schema ของ kingdom ครบ
- governing philosophies ไม่ซ้ำกัน
- virtue และ weakness เป็นสองด้านของหลักเดียวกัน
- animal roles ไม่ขัด ecology/lore โดยไม่มีเหตุผล

### Trait gate

- ทุกแกนมี behavioral anchors
- ไม่มีคำอธิบายที่วนกลับไปใช้ MBTI เป็นนิยาม
- dimensions ไม่ซ้ำกันเกินจำเป็น

### Question gate

- ทุก option plausible และไม่มีคำตอบดีอย่างชัดเจน
- trait loadings อธิบายได้
- story consequence เข้ากับ act
- ไม่มี answer-to-animal mapping โดยตรง

### Release gate

- distribution simulation ผ่านเกณฑ์ที่กำหนด
- result copy ไม่อ้างความแม่นยำเกินจริง
- telemetry และ privacy language พร้อม
