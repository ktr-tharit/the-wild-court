# Animal Visual System v0.1 — Boreal Tapestry

**Status:** Review v0.1  
**Last reviewed:** 2026-08-21  
**Prototype scope:** Taiga animals 6 ตัว

## Intent

ภาพสัตว์ของ The Wild Court ต้องให้ความรู้สึกเป็น **ตัวละครเชิงสัญลักษณ์ที่มีชีวิตอยู่ในโลกเดียวกัน** ไม่ใช่ภาพสัตว์ป่าจริง ไม่ใช่มนุษย์สวมหัว mascot และไม่ใช่คลาสตัวละครเกมต่อสู้

ทิศทางหลักใช้ชื่อว่า **Boreal Tapestry**: ภาพนิทาน editorial แบบ 2D ผสม gouache, cut-paper shapes, ขอบคล้ายภาพพิมพ์ linocut และ grain แบบผ้าทอ เส้น anatomy ยังทำให้จำ species ได้ทันที แต่ลดรายละเอียดขนและกล้ามเนื้อให้เป็นรูปทรงกราฟิก

## Shared visual grammar

- ภาพแนวตั้งประมาณ `4:5`; ตัวละครเต็มตัวหรือเกือบเต็มตัว อยู่กึ่งกลางและมีพื้นที่หายใจเหนือศีรษะ
- ท่ายืนสงบแบบ three-quarter ไม่โพสฮีโร่ ไม่แสดงอำนาจด้วยการคำรามหรือโชว์อาวุธ
- เสื้อผ้าต้องเหมือนสิ่งที่สัตว์ชนิดนั้นสวมและใช้งานได้จริง ไม่เปลี่ยนร่างกายให้เป็นมนุษย์
- ใช้ silhouette, posture, tools และพื้นที่รอบตัวเป็นภาษาหลักในการเล่าบุคลิก
- ฉากหลังเป็น Taiga แบบ layered flat shapes; รายละเอียดมีไว้บอกหน้าที่ ไม่ใช่สร้าง spectacle
- ไม่ใส่ตัวหนังสือ กรอบภาพ watermark มงกุฎ อาวุธ หรือเครื่องหมายเพศที่ชัดเกินไป

## Shared palette

| Color | Hex | Use |
|---|---|---|
| Pine Night | `#08110E` | ฉากพิธีกรรม เงาลึก |
| Deep Fir | `#10221B` | เสื้อคลุมและโครงสร้างไม้ |
| Frosted Bone | `#E7E3D7` | หิมะ ผ้า แสงสะท้อน |
| Lichen Silver | `#A8B5A7` | โลหะ เครื่องมือ และรายละเอียดรอง |
| Ember Copper | `#C78E62` | จุดรับรู้ตัวตน เส้นทาง ความอบอุ่น |

Covenant Red ใช้ได้ในปริมาณน้อยมากเมื่อหมายถึงพันธะ ผลของการตัดสินใจ หรือสิ่งที่ต้องรับผิดชอบ ไม่ใช้เป็นสีประจำตัวละคร

## Realm image — Taiga

ภาพ biome หลักใช้ valley view ของ The Boreal Dominion ในช่วง blue hour: แม่น้ำแข็งพาเข้าสู่ Hearthhold, แสง ember ขนาดเล็กเชื่อมชุมชน และท้องฟ้ามืดเปิดพื้นที่สำหรับ result typography

- Web asset: `/biomes/taiga/realm-v1.jpg`
- ใช้เป็น full-bleed background ใน Realm Reveal และ Result masthead
- Desktop crop เน้น valley และ settlement; mobile crop รักษาแม่น้ำกับแนวเขาตรงกลาง
- ต้องมี dark overlay เสมอเพื่อให้ text contrast ไม่ขึ้นกับรายละเอียดของภาพ
- environment only: ไม่มีสัตว์ ตัวละคร พระราชวัง หรือสัญลักษณ์ที่แย่งความหมายจากผลลัพธ์

## Taiga cast

| Animal | Visual thesis | Shape / posture | Signature objects | Environment | Avoid |
|---|---|---|---|---|---|
| Grey Wolf | ผู้ออกแบบการเคลื่อนที่ร่วมกัน | เส้นเฉียงที่พุ่งไปข้างหน้า แต่ร่างกายสงบและเปิดพื้นที่ให้ผู้อื่น | แผนที่ซ้อนกัน หมุดเงิน ด้าย copper | ห้องวางแผน มีเก้าอี้ว่างและทางออกสู่หิมะ | alpha pose, howl, military uniform, scars |
| Reindeer | ผู้ทำให้ทุกคนเดินต่อไปด้วยกัน | รูปทรงยาวต่อเนื่อง จังหวะการก้าวมั่นคง | route tokens และกระดิ่งประสานงานบนเขา ผ้าทอเป็นแผนที่ | ถนนอพยพยามรุ่ง มีไฟนำทางหลายจุด | Christmas, sleigh, passive saint, royal ornament |
| Lynx | ผู้เห็นสิ่งที่คนอื่นยังไม่เห็น | รูปทรงโปร่ง เงียบ น้ำหนักถอยจากศูนย์กลางเล็กน้อย | สมุดซ่อนในเสื้อ เอกสารและตัวอย่างที่จัดไว้อย่างแม่นยำ | ห้อง archive ข้างหน้าต่างเบิร์ช | oracle, magic eyes, thief coding, sexualization |
| Bear | ผู้สร้างเงื่อนไขให้ชีวิตฟื้นตัว | มวลโค้งกว้างและมั่นคง มืออยู่ใกล้ลำตัว ไม่ข่มผู้ชม | กุญแจคลัง เครื่องมือซ่อม กระเป๋าสมุนไพร | storehouse เชื่อมครัวและห้องพักฟื้น | dumb muscle, gluttony, maternal stereotype, roaring |
| Moose | ผู้ทำให้ขอบเขตมองเห็นและคงอยู่ | แนวตั้งสูง เขาเป็นรูป doorway ไม่ใช่มงกุฎ | boundary markers ตราประตู ผ้าคลุมเชิงสถาปัตยกรรม | ประตูชุมชนระหว่างป่าและแม่น้ำ | slow brute, dominance display, monarch, armor |
| Wolverine | ผู้เปิดทางเมื่อระบบเดิมใช้ไม่ได้ | มวลเล็กแน่น เอียงไปข้างหน้าเหมือนกำลังลงมือ | เชือกฉุกเฉิน อุปกรณ์ซ่อมแล้วซ่อมอีก broken insignia clasp | สะพานหรือประตูที่พังและกำลังถูกข้าม | berserker, snarl, weapons, edgelord, superhero pose |

## Asset map

| Animal | Canonical prototype asset |
|---|---|
| Grey Wolf | `/animals/taiga/grey-wolf-v1.jpg` |
| Reindeer | `/animals/taiga/reindeer-v1.jpg` |
| Lynx | `/animals/taiga/lynx-v1.jpg` |
| Bear | `/animals/taiga/bear-v1.jpg` |
| Moose | `/animals/taiga/moose-v1.jpg` |
| Wolverine | `/animals/taiga/wolverine-v1.jpg` |

ไฟล์สำหรับเว็บอยู่ใน `web/public/` ส่วน PNG ความละเอียดสูงเก็บที่ `assets/concept-art/taiga/` ภาพชุดนี้ยังถือเป็น concept art สำหรับ review ไม่ใช่ final production asset

## Prompt construction rule

ทุกภาพใช้ prompt backbone เดียวกัน แล้วเปลี่ยนเฉพาะ 5 ส่วน:

1. species และ identity core
2. silhouette / posture
3. clothing construction
4. signature objects
5. environmental story

Negative direction ต้องย้ำร่วมกันว่า: no photoreal fur, no 3D render, no Disney mascot, no anime, no chibi, no crown, no weapon, no text และเพิ่ม stereotype เฉพาะ species จากตารางด้านบน

## Review checklist

- [x] มอง silhouette แล้วแยก species ได้
- [x] มอง scene และ props แล้วเดาหน้าที่ของ archetype ได้โดยไม่อ่านข้อความ
- [x] ทั้งหกตัวใช้ภาษาแสง สี texture และระดับ abstraction เดียวกัน
- [x] ไม่มีตัวใดถูกทำให้เป็นผู้ชายหรือผู้หญิงโดย default
- [x] ไม่มีตัวใดพึ่ง trope นักรบ ราชา หรือสัตว์น่ารักเพื่อสร้าง desirability
- [x] ทดลอง crop บน desktop และ mobile result reveal
- [ ] target-user review: recognition, desirability และ emotional tone
- [ ] ตรวจความสม่ำเสมออีกครั้งเมื่อเพิ่ม biome ที่สอง

## Expansion rule

เมื่อเพิ่ม biome ใหม่ ให้คงระดับ abstraction, composition และ narrative density เดิม แต่เปลี่ยน material language ตามระบบนิเวศ เช่น Ocean อาจใช้ translucent wash และ shell inlay ส่วน Desert อาจใช้ dry brush และ sun-bleached textile โดยห้ามเปลี่ยนจนดูเหมือนคนละเกม
