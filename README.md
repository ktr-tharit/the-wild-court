# The Wild Court

Interactive personality adventure ที่จับคู่ผู้เล่นกับ **Kingdom / Biome** และ **Animal Archetype** ผ่านสถานการณ์ในโลกแฟนตาซีการเมือง

> Narrative can branch. Mathematics should stay soft.

## เริ่มอ่านจากตรงไหน

1. [Project Vision](docs/project/vision.md) — เกมนี้คืออะไร และไม่ควรกลายเป็นอะไร
2. [Current Checklist](docs/project/checklist.md) — ตอนนี้ทำถึงไหน และงานถัดไปคืออะไร
3. [World Bible](docs/world/world-bible.md) — กฎกลางของโลกและภาพรวม 8 kingdoms
4. [Kingdom Index](docs/world/kingdoms/README.md) — เอกสาร vibe, politics และ culture รายอาณาจักร
5. [Design Overview](docs/design/README.md) — ระบบ trait, scoring, story flow และ animal profiles
6. [Decision Log](docs/project/decision-log.md) — เหตุผลของการตัดสินใจสำคัญ

## สถานะปัจจุบัน

- Project stage: **Playable Taiga vertical slice**
- World structure: **8 kingdoms selected**
- Kingdom vibe and politics: **Draft v0.1 migrated**
- Psychological traits: **8-dimensional prototype model v0.3**
- Taiga animal roster: **6 complete profiles and result experiences**
- Scoring and adaptive flow: **Implemented and covered by automated tests**

## รันตัวเกม

ต้องใช้ Node.js `>=22.13.0` และ `pnpm`

```bash
cd web
pnpm install
pnpm run dev
```

จากนั้นเปิด `http://localhost:3000`

ตรวจ build และ scoring runtime ด้วย:

```bash
cd web
pnpm test
```

## กติกาการดูแลเอกสาร

- เนื้อหาที่ตกลงแล้วต้องถูกย้ายจากบทสนทนามาอยู่ใน repository นี้
- ทุกเอกสารใช้สถานะ `Seed`, `Draft`, `Review`, `Locked` หรือ `Deprecated`
- การเปลี่ยนหลักการสำคัญต้องบันทึกใน [Decision Log](docs/project/decision-log.md)
- หลังจบแต่ละ design session ให้อัปเดต checklist และเพิ่มบันทึกใน [Review Log](docs/project/review-log.md)
- ห้ามใช้ chat history เป็น source of truth ระยะยาว
