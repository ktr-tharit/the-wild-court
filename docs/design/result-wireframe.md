# Result Experience Wireframe v0.1

**Status:** Structure ready for prototype review  
**Companion:** [Result Experience Bible](result-experience.md)

## Purpose

แปลง Result Experience Bible ให้เป็น mobile-first screen hierarchy ก่อนทำ final visual art หรือ implementation และตรวจว่าโครงเดียวกันรองรับสัตว์ที่มีบุคลิกต่างกันได้จริง

## Prototype flow

### 1. Realm Reveal

เป้าหมายคือสร้าง recognition และ belonging ก่อนบอกชื่อสัตว์

- Progress cue: Judgment → Realm → Nature
- ชื่อ kingdom และ formal title
- Kingdom belief หนึ่งประโยคที่ทำหน้าที่เป็น identity mirror
- อธิบายสั้น ๆ ว่า realm คือ survival worldview ไม่ใช่ label
- Primary action เดียว: `Meet your nature`

### 2. Animal Hero

เป้าหมายคือ identity moment ที่ผู้เล่นจดจำและอยากแชร์

- Animal crest หรือ portrait
- Animal name และ archetype title
- Identity promise หนึ่งประโยค
- Signature phrases สามคำ
- Primary action เดียว: `Enter your result`

ไม่แสดง score, vector, confidence percentage หรือ rarity ในช่วง reveal

### 3. Deep Result Scroll

เป้าหมายคือเปลี่ยน reveal ให้เป็น nuance, emotional permission และ growth direction

1. Condensed identity hero
2. At your core
3. Pattern modules
   - What moves you
   - How you connect
   - How you protect
   - When winter closes in
   - What you rarely ask for
4. What others may misunderstand
5. When the gift hardens
6. Restoring balance
7. Why this realm knows you
8. Share และ save actions

## Interaction decisions

- Reveal screen มี primary action เดียวเพื่อรักษาจังหวะพิธีกรรม
- Deep result เป็น scroll แทนการบังคับกดทีละหน้า เพื่อให้ผู้เล่นอ่านตามจังหวะตัวเอง
- ทดสอบ hierarchy เดียวกันกับ Grey Wolf และ Reindeer เพื่อไม่ให้ layout overfit กับ archetype เดียว
- Secondary realm ยังซ่อนใน Taiga-only prototype
- Share output เป็น identity crest แบบย่อ ไม่ใช่ภาพเต็มของรายงาน

## Visual direction

- Mobile-first, ceremonial, restrained และอ่านง่าย
- Realm กับ Animal reveal ใช้บรรยากาศ Taiga โทนมืด
- Deep reading เปลี่ยนเป็นพื้น warm bone เพื่อลดความล้า และแยกช่วง spectacle ออกจาก reflection
- ใช้ typography สร้าง hierarchy จนกว่าจะมี final illustration
- Placeholder crest เปลี่ยนเป็น animal portrait ภายหลังได้โดยไม่กระทบ content structure

## Questions for playtest

- Realm reveal มีความหมายหรือรู้สึกว่าเป็นช่วงหน่วง?
- ผู้เล่นจำ identity promise และพูดซ้ำได้ไหม?
- Pattern module ไหนสร้าง recognition มากที่สุด?
- Misunderstanding รู้สึกว่าได้รับการเข้าใจ หรือเป็นคำชมกว้าง ๆ?
- Shadow เฉพาะเจาะจงพอให้มีประโยชน์โดยไม่ลงโทษผู้เล่นไหม?
- ผู้เล่นหยุด scroll ที่ช่วงไหน?
- สิ่งที่อยากแชร์คือ animal, realm, promise หรือหลายอย่างรวมกัน?

## Exit criteria

- ทั้งสอง animal examples อยู่ในโครงเดียวกันได้โดยไม่ต้องทำข้อยกเว้น
- ผู้เล่นเข้าใจลำดับข้อมูลโดยไม่ต้องมีคนอธิบาย
- Reveal ให้ emotional completion ได้ก่อนเห็นข้อมูลเชิงตัวเลข
- Full result scan ง่ายบนหน้าจอเล็ก
- ผู้เล่นระบุ strength ที่ resonate และ tension ที่นำไปใช้ได้อย่างน้อยอย่างละหนึ่งข้อ
