# Psychological Trait System

**Status:** Review v0.3  
**Last reviewed:** 2026-08-21

ผู้เล่นไม่ใช่ type แต่เป็น vector ต่อเนื่อง:

```text
θ = [AFF, AGY, SEN, STR, EXP, RSK, DCL, ALG]
θₖ ∈ [-1, +1]
```

โมเดลนี้ออกแบบสำหรับ **The Wild Court Identity Adventure**: วัด identity, relationships, agency, duty และการตอบสนองต่อความไม่แน่นอน โดยใช้ politics เป็นหนึ่งในฉากกดดัน ไม่ใช่ construct หลักเพียงอย่างเดียว

## Trait model v0.3

| ID | Dimension | -1 pole | +1 pole | วัดคำถามหลักว่า… |
|---|---|---|---|---|
| AFF | Affiliation | Independent | Collaborative | เราเข้าใจและรับมือโลกผ่านพื้นที่ส่วนตัวหรือการมีส่วนร่วมกับคนอื่น? |
| AGY | Agency | Accommodating | Directive | เมื่อ direction ไม่ชัด เรารับและประสานแรงรอบตัวหรือสร้างทิศทางขึ้นมา? |
| SEN | Sensemaking | Intuitive | Analytical | เมื่อข้อมูลไม่ครบ เราเชื่อ pattern/timing หรือการแยกเหตุผลและหลักฐาน? |
| STR | Structure | Responsive | Structuring | เราเปลี่ยนตัวเองตามสถานการณ์หรือจัดสถานการณ์ให้คาดการณ์ได้? |
| EXP | Expression | Guarded | Expressive | เราทำให้ inner state มองเห็นจากภายนอกมากเพียงใด? |
| RSK | Risk Orientation | Preserving | Exploring | เรารักษาสิ่งที่มีหรือเปิดทางให้ความเป็นไปได้ใหม่เมื่อผลไม่แน่นอน? |
| DCL | Decision Lens | Impartial | Relational | เมื่อคุณค่าขัดกัน เราให้น้ำหนักกับมาตรฐานสม่ำเสมอหรือบริบทของความสัมพันธ์? |
| ALG | Allegiance | Self-authored | Duty-bound | ความชอบธรรมเริ่มจาก conscience ส่วนตัวหรือพันธะ บทบาท และคำสัญญา? |

`-1` และ `+1` ไม่ใช่คะแนนลบ/บวก และ `0` ไม่ได้แปลว่าไม่มี personality แต่หมายถึงใช้ทั้งสอง strategy ตามบริบท

---

## AFF — Affiliation

**Independent ↔ Collaborative**

- **Measures:** preferred mode of processing, coordination และ recovery
- **Does not measure:** social skill, empathy, popularity หรือความสามารถในการรักผู้อื่น
- **-1 healthy:** self-contained, focused, comfortable acting alone
- **-1 shadow:** isolated, inaccessible, refuses useful support
- **0 anchor:** ทำงานเดี่ยวหรือร่วมมือได้ตามประเภทของปัญหา
- **+1 healthy:** connective, cooperative, generates insight through participation
- **+1 shadow:** consensus-dependent, boundaryless, unable to separate from group emotion
- **Under pressure:** Independent ถอนตัวไปหาคำตอบ; Collaborative สร้างวงคนเพื่อรับมือร่วมกัน

## AGY — Agency

**Accommodating ↔ Directive**

- **Measures:** tendency to receive, coordinate or create direction when wills collide
- **Does not measure:** competence, confidence, social status หรือ aggression
- **-1 healthy:** receptive, diplomatic, makes room for others
- **-1 shadow:** passive, conflict-avoidant, lets others define the situation
- **0 anchor:** นำเมื่อมี mandate ชัด และถอยเมื่อคนอื่นเหมาะกว่า
- **+1 healthy:** decisive, mobilizing, willing to own a direction
- **+1 shadow:** overbearing, takes control before understanding others
- **Under pressure:** Accommodating ลดแรงปะทะ; Directive ตัดสินใจและรวบอำนาจเพื่อให้เกิด movement

## SEN — Sensemaking

**Intuitive ↔ Analytical**

- **Measures:** preferred way of forming confidence when information is incomplete
- **Does not measure:** intelligence, education, creativity หรือ emotionality
- **-1 healthy:** perceptive, fast pattern recognition, sensitive to timing and atmosphere
- **-1 shadow:** impulsive, projection-prone, trusts a feeling without checking it
- **0 anchor:** ใช้ instinct ตั้งสมมติฐานแล้วตรวจด้วยหลักฐาน
- **+1 healthy:** precise, consistent, evidence-aware
- **+1 shadow:** overthinks, delays commitment, ignores tacit knowledge
- **Under pressure:** Intuitive เลือกจาก pattern ที่รู้สึกได้; Analytical แยกข้อมูลและตรวจ contradiction

## STR — Structure

**Responsive ↔ Structuring**

- **Measures:** strategy toward environment, uncertainty, plans and rules
- **Does not measure:** leadership over people; ใช้ AGY สำหรับเรื่องนั้น
- **-1 healthy:** flexible, resilient, changes form without losing purpose
- **-1 shadow:** inconsistent, easily carried by circumstances
- **0 anchor:** วางกรอบเบา ๆ และพร้อมเปลี่ยนเมื่อ context เปลี่ยน
- **+1 healthy:** organized, stabilizing, creates boundaries and predictability
- **+1 shadow:** rigid, compulsively controlling, mistakes plan for reality
- **Under pressure:** Responsive เปลี่ยนแผน; Structuring เพิ่มกฎ ขอบเขต และการเตรียมพร้อม

## EXP — Expression

**Guarded ↔ Expressive**

- **Measures:** visibility of feelings, intentions and identity
- **Does not measure:** Affiliation, honesty หรือ emotional depth
- **-1 healthy:** composed, discerning, protects inner life
- **-1 shadow:** unreadable, emotionally unavailable, withholds until trust collapses
- **0 anchor:** เปิดเผยกับคนและเวลาที่เลือก แต่ไม่รู้สึกว่าต้องซ่อนหรือแสดงเสมอ
- **+1 healthy:** vivid, emotionally legible, gives energy to a room
- **+1 shadow:** performative, overshares, cannot contain emotion when containment is needed
- **Under pressure:** Guarded ปิดสัญญาณ; Expressive ทำให้ทุกคนรู้ว่ากำลังรู้สึกและต้องการอะไร

## RSK — Risk Orientation

**Preserving ↔ Exploring**

- **Measures:** preference when security and possibility compete
- **Does not measure:** bravery, morality หรือ physical thrill-seeking เท่านั้น
- **-1 healthy:** prudent, protective, preserves resources and relationships
- **-1 shadow:** stagnant, fear-governed, treats every loss as unacceptable
- **0 anchor:** ยอมเสี่ยงเมื่อ downside จำกัดหรือมีข้อมูลเพียงพอ
- **+1 healthy:** curious, opportunity-seeking, tolerant of uncertainty
- **+1 shadow:** reckless, novelty-dependent, abandons value before it matures
- **Under pressure:** Preserving ปกป้องฐานที่เหลือ; Exploring เปิดเส้นทางใหม่แม้ผลยังไม่ชัด

## DCL — Decision Lens

**Impartial ↔ Relational**

- **Measures:** what receives priority when consistent standards conflict with specific relationships and contexts
- **Does not measure:** coldness vs kindness, Thinking vs Feeling หรือความสามารถในการเห็นอกเห็นใจ
- **-1 healthy:** fair, consistent, applies principles beyond personal preference
- **-1 shadow:** rule-bound, emotionally distant, erases meaningful context
- **0 anchor:** เริ่มจากมาตรฐานร่วม แล้วอนุญาต exception เมื่อบริบทมีน้ำหนักจริง
- **+1 healthy:** compassionate, context-sensitive, honors particular bonds
- **+1 shadow:** biased, unable to set boundaries, excuses harm for someone close
- **Under pressure:** Impartial ถามว่า “ถ้าเป็นทุกคนควรใช้กฎอะไร?”; Relational ถามว่า “เราติดค้างอะไรต่อคนเหล่านี้โดยเฉพาะ?”

## ALG — Allegiance

**Self-authored ↔ Duty-bound**

- **Measures:** source of legitimate obligation when personal conviction conflicts with role, promise or institution
- **Does not measure:** Affiliation, selfishness, loyalty in every context หรือ obedience to authority อย่างเดียว
- **-1 healthy:** autonomous, conscience-led, chooses commitments deliberately
- **-1 shadow:** unaccountable, commitment-resistant, treats freedom as exemption
- **0 anchor:** ยอมรับพันธะที่สอดคล้องกับ conscience และพร้อมทบทวนเมื่อมันสร้างอันตราย
- **+1 healthy:** loyal, dependable, accepts cost for promises and shared continuity
- **+1 shadow:** self-erasing, obedient to harmful systems, cannot release inherited duty
- **Under pressure:** Self-authored ทำตามสิ่งที่ตนยอมรับว่าถูก; Duty-bound ยืนกับคำสัญญาแม้ความรู้สึกส่วนตัวเปลี่ยน

---

## Independence checks

คู่ต่อไปนี้ต้องเกิดขึ้นได้จริงใน animal roster เพื่อยืนยันว่า dimensions ไม่ซ้ำกัน:

| Combination | Example meaning |
|---|---|
| Independent + Duty-bound | ทำงานลำพังแต่ผูกชีวิตกับภารกิจหรือคำสัญญา |
| Collaborative + Self-authored | ชอบอยู่กับคนแต่ไม่ยอมให้ institution นิยาม conscience |
| Accommodating + Structuring | รักษาระบบและแผนโดยไม่ต้องการเป็นคนสั่งทุกคน |
| Directive + Responsive | นำคนได้เด็ดขาดแต่เปลี่ยนยุทธวิธีตามสถานการณ์ |
| Guarded + Collaborative | ต้องการกลุ่มแต่เปิดเผย inner state อย่างเลือกสรร |
| Expressive + Independent | แสดงตัวตนชัดแต่ไม่ต้องการการตัดสินใจแบบกลุ่ม |
| Impartial + Duty-bound | ยึด covenant หรือกฎที่ควรใช้กับทุกคน |
| Relational + Self-authored | เลือกปกป้องความสัมพันธ์เฉพาะ แม้ institution ไม่รับรอง |

## What moved out of the primary vector

`Social Strategy: Candid ↔ Calculated` ไม่อยู่ใน primary 8 dimensions ของ v0.3 เพราะทำให้ model เอนเข้าหา court politics มากเกินไป และสามารถเกิดจาก configuration ของ Sensemaking, Expression, Agency และ context ได้

เก็บไว้เป็น **question/result facet** เพื่อ:

- tag คำถามที่เกี่ยวกับ disclosure, timing และ information control
- ช่วยเขียน distinction ระหว่างสัตว์
- ตรวจภายหลังว่ามันอธิบาย residual variance มากพอจะกลับมาเป็น dimension หรือไม่

Facets อื่นที่เก็บเป็น metadata ก่อน ได้แก่ care, creativity, status, intimacy, competition และ aesthetic expression

## Provisional kingdom fingerprints

ตารางนี้ใช้ตรวจว่า vector space สามารถวาง 8 kingdoms ให้ต่างกันได้หรือไม่ ยังไม่ใช่ scoring source และค่าจริงควร derive จาก animal roster ภายหลัง

| Kingdom | AFF | AGY | SEN | STR | EXP | RSK | DCL | ALG |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Taiga | -0.5 | +0.3 | +0.6 | +0.7 | -0.7 | -0.5 | -0.2 | +0.3 |
| Arctic | +0.4 | -0.1 | +0.4 | +0.8 | -0.7 | -0.7 | -0.1 | +0.9 |
| Savanna | +0.5 | +0.8 | -0.1 | +0.4 | +0.8 | +0.3 | -0.1 | +0.2 |
| Rainforest | +0.8 | -0.1 | -0.3 | -0.7 | +0.4 | +0.5 | +0.8 | +0.3 |
| Desert | -0.3 | +0.2 | +0.7 | +0.8 | -0.5 | -0.7 | -0.6 | +0.2 |
| Ocean | +0.2 | -0.2 | -0.4 | -0.9 | +0.1 | +0.8 | +0.2 | -0.7 |
| Alpine | -0.4 | +0.6 | +0.7 | +0.6 | -0.4 | +0.4 | -0.7 | -0.1 |
| Wetland | +0.4 | 0.0 | +0.5 | +0.2 | -0.6 | -0.2 | +0.6 | +0.7 |

## Question-loading rules

- แต่ละ option ควรมี strong loading ไม่เกิน 2 dimensions และ weak loading ได้อีกไม่เกิน 1
- ห้ามใช้ kingdom หรือ animal เป็น scoring target ของ option โดยตรง
- ทุก playthrough ควรมี evidence อย่างน้อย 4 ครั้งต่อ dimension ก่อนรายงาน confidence สูง
- ทั้งสอง poles ต้องมีคำตอบที่ดู competent, caring หรือ courageous ได้เท่าเทียมกัน
- Question bank ต้องกระจาย domain: relationships, public power, care/community, identity/expression และ uncertainty/exploration
- Political questions เป็นประมาณหนึ่งในสี่ของ core bank ไม่ใช่ majority

## Gate ก่อนเปลี่ยนเป็น Locked

- [ ] ทำ Taiga animals ทั้ง 6 ตัวด้วย vectors ชุดนี้
- [ ] ทุก animal pair มี distinction ที่ไม่พึ่ง species stereotype อย่างเดียว
- [ ] provisional kingdom fingerprints ไม่เกิด collision ที่อธิบายไม่ได้
- [ ] เขียนคำถามทดลองอย่างน้อย 2 ข้อต่อ dimension
- [ ] ให้ target users ตรวจว่า wording ทั้งสอง poles ไม่ชี้นำหรือดูมีค่าต่างกัน
- [ ] simulation แสดงว่า 16–20 ข้อเก็บ evidence ครบพอ

