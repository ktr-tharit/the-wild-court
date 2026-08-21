# Question Evidence Schema v0.2

**Status:** Sandbox contract  
**Last reviewed:** 2026-08-22  
**Example data:** `data/question-evidence-example.v0.2.json`

## Purpose

แยกสามสิ่งที่ v0.1 รวมอยู่ใน object เดียว:

1. **Construct** — คำตอบกำลังให้ข้อมูลเรื่องอะไร
2. **Value** — ideal point ที่คำตอบนั้นเป็นหลักฐานให้
3. **Weight** — คำตอบนี้บอก construct นั้นชัดเพียงใด

การแยกนี้ทำให้คำตอบหนึ่งสามารถวัด core behavior อย่างจริงจังและติด motive probe เบา ๆ โดยไม่บวกสอง metric เท่ากันโดยอัตโนมัติ

## Evidence item

```json
{
  "construct": "REC",
  "value": 1.0,
  "weight": 0.5,
  "role": "motive_probe"
}
```

| Field | Allowed values | Meaning |
|---|---|---|
| `construct` | core ID หรือ approved facet ID | construct ที่ได้รับ evidence |
| `value` | core `[-1, 1]`; motive `{0, 0.5, 1}` | ideal point ไม่ใช่คะแนนบวกสะสม |
| `weight` | `1.0` หรือ `0.5` | strong หรือ supporting evidence |
| `role` | `primary`, `secondary`, `motive_probe` | หน้าที่ของ evidence ใน item design |

Role และ weight ใช้ contract คงที่:

| Role | Weight | Use |
|---|---:|---|
| `primary` | `1.0` | construct หลักที่ trade-off ของ option แสดงโดยตรง |
| `secondary` | `0.5` | behavioral signal รองที่ช่วยแยกคำตอบแต่ไม่ควรมีอำนาจเท่าแกนหลัก |
| `motive_probe` | `0.5` | hypothesis เรื่องเหตุผลเบื้องหลัง; ยังไม่ใช่ production axis |

Approved motive IDs ใน sandbox:

| ID | Facet | `0` | `0.5` | `1` |
|---|---|---|---|---|
| REC | Recognition | witness ไม่สำคัญต่อความหมาย | witness ช่วยยืนยัน impact | public witness เป็นส่วนหลักของ meaning |
| MAS | Mastery | capability เป็นเครื่องมือ | growth through skill สำคัญ | disciplined capability เป็นแหล่ง identity หลัก |
| RCP | Reciprocity | mutual exchange ไม่ใช่ฐาน belonging | exchange สร้างความผูกพันบางส่วน | mutual flourishing สร้างหน้าที่โดยตรง |
| CON | Continuity | ไม่ต้อง carry สิ่งใดข้ามเวลา | เลือกส่งต่อบาง commitment | identity มีความหมายผ่านสิ่งที่รักษาและส่งต่อ |
| RST | Restraint | choosing less ไม่ใช่คุณค่าหลัก | restraint ใช้คุ้มครองบางสิ่ง | sufficiency และการไม่ใช้เกินจำเป็นเป็นหลักชีวิต |

`0` หมายถึง motive นี้ไม่ใช่ตัวอธิบายหลัก ไม่ได้หมายถึงขั้วตรงข้ามหรือข้อเสีย

## Loading rules

- option หนึ่งมี evidence สูงสุด 3 constructs
- strong evidence (`1.0`) สูงสุด 2 constructs
- motive probe เริ่มที่ weight `0.5`; ห้ามแอบทำให้เป็น primary dimension ด้วย weight รายข้อ
- คำตอบสี่ตัวเลือกต้องไม่ซ้ำ evidence signature
- missing evidence หมายถึง **unobserved** ไม่ใช่ `0`
- คำนวณ estimate ต่อ construct ด้วย weighted mean:

```text
estimate(k) = Σ(valueᵢ × weightᵢ) / Σ(weightᵢ)
confidence(k) = Σ(weightᵢ)
```

- ranking ต้อง normalize distance แยก core group กับ facet group ก่อน blend เพื่อไม่ให้จำนวนแกนมากกว่าชนะเอง
- sandbox ใช้ `core_distance + 0.5 × facet_distance`; ค่า `0.5` มาจาก supporting-evidence tier ไม่ใช่ tuning รายสัตว์

## Authoring checklist

- scenario มี trade-off จริงและทุก option ดู competent ได้
- wording ของ option อธิบายเหตุผล ไม่ใช่แค่ action ที่ animal หลายตัวทำเหมือนกัน
- core value และ motive value สามารถแตกต่างกันได้ เช่น expressive แต่ไม่ได้ต้องการ recognition
- weight สะท้อนความชัดของหลักฐาน ไม่สะท้อนว่า designer อยากให้ animal ใดชนะ
- ห้ามใช้ realm, species หรือ result title เป็น scoring target
- motive หนึ่งต้องมีอย่างน้อย 3 scenarios คนละ domain ก่อนพิจารณาเปิดใช้ใน production score

## Migration from v0.1

v0.1:

```json
"evidence": {"AFF": 0.8, "EXP": -0.8}
```

v0.2 equivalent:

```json
"evidence": [
  {"construct": "AFF", "value": 0.8, "weight": 1.0, "role": "primary"},
  {"construct": "EXP", "value": -0.8, "weight": 1.0, "role": "primary"}
]
```

ยังไม่ migrate question bank เดิมจนกว่า 16-anchor sandbox จะผ่าน gate เพราะ runtime และ frontend ปัจจุบันยังอ่าน v0.1 object form

## Promotion gate

facet จะเข้า production scoring ได้ต่อเมื่อ:

- ลด confusion ของ collision ที่ตั้งใจอย่างสม่ำเสมอ
- ไม่ทำให้ overall recovery ลดลง
- มี question evidence อย่างน้อย 3 domains
- distinction สามารถอธิบายด้วย motive wording โดยไม่อ้าง species stereotype
- pilot data ไม่แสดงว่า facet เป็นเพียง proxy ของ core dimension เดิม
