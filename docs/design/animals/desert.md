# Desert Animal Bible Architecture v0.1

**Status:** Animal Bibles + provisional vectors v0.4  
**Last reviewed:** 2026-08-22  
**Realm:** The Sunless Crown / Desert

## Realm thesis

Desert เชื่อว่า **restraint protects freedom** แต่ restraint ของที่นี่ไม่ใช่การอดทนเฉย ๆ หรือความกลัวว่าจะไม่มีพอ มันคือความสามารถในการรู้ว่าอะไรคู่ควรแก่เวลา ความสนใจ ความไว้ใจ ความต้องการ และภาระที่มีอยู่อย่างจำกัด

สัตว์ทั้งหกตอบคำถามเดียวกัน:

> **What will you refuse to spend without meaning?**

| Animal | Working title | Refuses to waste | Identity fantasy |
|---|---|---|---|
| Fennec Fox | The Listener in the Dunes | Attention | ฉันมองเห็น possibility เล็ก ๆ ก่อนคนอื่นใช้กำลังและทรัพยากรเกินจำเป็น |
| Caracal | The Silent Standard | Dignity | ฉันไม่ต้องอธิบายคุณค่าของตัวเองเพื่อให้มันเป็นจริง |
| Cobra | The Keeper of the Final Line | Consequence | ฉันทำให้ขอบเขตชัดพอที่ความรุนแรงไม่จำเป็นต้องเกิดโดยไม่เตือน |
| Camel | The Bearer of the Long Measure | Capacity | ฉันเลือกภาระด้วยความเข้าใจต้นทุน แล้วพามันไปถึงปลายทาง |
| Scorpion | The Unbowed Sovereign | Access | ไม่มีใครได้สิทธิ์เข้าถึงฉันเพียงเพราะตัวใหญ่กว่า มีตำแหน่งกว่า หรือเรียกร้องดังกว่า |
| Oryx | The Keeper of the Inner Spring | Desire | ฉันเลือกความพอโดยไม่ทำให้ชีวิต ความงาม หรือความหวังของตัวเองเล็กลง |

## Animal Bibles

| Animal | Working title | Bible |
|---|---|---|
| Fennec Fox | The Listener in the Dunes | [Read](desert/fennec-fox.md) |
| Caracal | The Silent Standard | [Read](desert/caracal.md) |
| Cobra | The Keeper of the Final Line | [Read](desert/cobra.md) |
| Camel | The Bearer of the Long Measure | [Read](desert/camel.md) |
| Scorpion | The Unbowed Sovereign | [Read](desert/scorpion.md) |
| Oryx | The Keeper of the Inner Spring | [Read](desert/oryx.md) |

## Provisional Trait Model v0.5 vectors

Canonical values อยู่ใน `data/vector-model.v0.5.json` และต้องเปลี่ยนผ่าน joint Taiga–Desert simulation ไม่ tune แยกรายตัว

| Animal | AFF | AGY | SEN | STR | EXP | RSK | DCL | ALG |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fennec Fox | +0.4 | -0.2 | -0.6 | -0.6 | -0.4 | +0.5 | +0.5 | -0.4 |
| Caracal | -0.6 | +0.5 | +0.6 | +0.3 | -0.7 | -0.4 | -0.5 | -0.7 |
| Cobra | -0.4 | +0.6 | +0.2 | +0.7 | +0.7 | -0.6 | -0.7 | 0.0 |
| Camel | +0.5 | 0.0 | +0.6 | +0.8 | -0.4 | -0.8 | +0.2 | +0.6 |
| Scorpion | -0.8 | +0.6 | -0.5 | +0.6 | -0.8 | -0.7 | -0.7 | -0.8 |
| Oryx | +0.6 | -0.2 | 0.0 | +0.6 | +0.5 | -0.7 | +0.5 | 0.0 |

## Portfolio shape

```text
              reads possibility
                 Fennec
                    │
inner standard ─ Caracal ─ Cobra ─ declared consequence
                    │          │
              Scorpion      Camel
             guards access  carries commitment
                    ╲          ╱
                       Oryx
                embodies enoughness
```

แผนภาพนี้เป็น conceptual relationship ไม่ใช่ scoring axes

## Archetype briefs

### Fennec Fox — The Listener in the Dunes

- **Identity promise:** Sensitivity is not fragility; it lets you hear the path that force would bury.
- **Core desire:** รักษาความเบา ความอยากรู้ และทางเลือกไว้ในโลกที่ทุก action มีต้นทุน
- **Core fear:** discipline กลายเป็น suspicion จน possibility ถูกปิดก่อนมีใครได้ฟังมัน
- **Strength:** signal detection, timing, low-cost adaptation และ social warmth ที่ไม่รุกล้ำ
- **Shadow:** เปลี่ยน direction บ่อย หลีกเลี่ยง commitment ด้วยคำว่า flexibility และใช้ charm แทนความชัด
- **Secret need:** มีคนเห็นว่าความเบาและความสนุกของตนไม่ใช่การไม่จริงจัง
- **Relationship strategy:** เปิด trust ทีละน้อยผ่าน curiosity, shared observation และ timely usefulness
- **Embodies Desert:** ใช้ attention ก่อนใช้ resource
- **Resists Desert:** ไม่ยอมให้ caution ทำลาย warmth และ wonder
- **Ordinary anchor:** สังเกต tension เล็ก ๆ ในวงสนทนาแล้วเปลี่ยนจังหวะก่อนความขัดแย้งต้องใช้ authority แก้
- **Pressure anchor:** เมื่อทุกคนต้องการคำตอบถาวร Fennec อาจรักษาทางเลือกมากเกินไปจนไม่มีใครรู้ว่าพึ่งพาได้หรือไม่
- **Share line seed:** *My nature belongs to the Fennec—the one who hears a path beneath the wind.*

### Caracal — The Silent Standard

- **Identity promise:** Your dignity does not begin when the room recognizes it.
- **Core desire:** ดำรงมาตรฐานภายในโดยไม่แลก self-respect กับ approval, access หรือความสะดวก
- **Core fear:** ถูกบังคับให้ perform, explain หรือ bargain away ตัวตนเพื่อได้รับการยอมรับ
- **Strength:** precision, composure, self-command และ action ที่ไม่ต้องมี spectacle
- **Shadow:** pride กลายเป็น inaccessibility; มองการขอความช่วยเหลือหรือการอธิบายเป็นการลดตัว
- **Secret need:** ได้รับความรักในเวลาที่ไม่ polished, precise หรือควบคุมตัวเองได้ทั้งหมด
- **Relationship strategy:** ให้เกียรติผ่าน space, consistency และการไม่ทำให้ vulnerability ของอีกฝ่ายเป็น spectacle
- **Embodies Desert:** self-possession ทำให้ไม่ต้องใช้ excess เพื่อพิสูจน์คุณค่า
- **Resists Desert:** inner sovereignty อยู่เหนือราคาและ contract ที่ Court ตั้งให้
- **Ordinary anchor:** เลือกงานน้อยชิ้นแต่ทำให้คมชัด โดยไม่แข่งเรียก attention กับคนอื่น
- **Pressure anchor:** เมื่อถูกเข้าใจผิด Caracal อาจปฏิเสธการอธิบายแม้ silence กำลังทำร้ายความสัมพันธ์จริง
- **Share line seed:** *My nature belongs to the Caracal—the standard that does not bend for an audience.*

### Cobra — The Keeper of the Final Line

- **Identity promise:** A boundary spoken clearly is an act of mercy before consequence becomes necessary.
- **Core desire:** ทำให้ limit, consent และ consequence ชัดก่อน hidden cost จะถูกผลักให้คนที่อ่อนแอกว่า
- **Core fear:** คำเตือนถูกละเลยจนต้องเลือกระหว่างยอมถูกละเมิดกับใช้ force โดยไม่มีใครเตรียมรับผล
- **Strength:** explicit boundaries, moral clarity, proportionate consequence และ presence ที่หยุด escalation
- **Shadow:** ทุก disagreement กลายเป็น final warning; certainty แข็งจนไม่มีทาง repair
- **Secret need:** อยู่ในความสัมพันธ์ที่ไม่ต้องแสดง danger ก่อนคนอื่นจะฟังคำว่า “พอ”
- **Relationship strategy:** บอก terms และ deal-breakers ตรง ให้โอกาสเลือกอย่างรู้ผล และไม่ใช้ ambiguity สร้าง leverage
- **Embodies Desert:** clarity prevents waste, coercion และ debt ที่ไม่มีใครยอมรับจริง
- **Resists Desert:** ปฏิเสธ covert threat และข้อตกลงที่อีกฝ่ายไม่เคยได้รับ warning ชัด
- **Ordinary anchor:** ระบุขอบเขตตั้งแต่ต้นโดยไม่ทำให้เป็น drama แล้วรักษามาตรฐานเดียวกันเมื่อถึงเวลาตนเสียประโยชน์
- **Pressure anchor:** เมื่อถูกท้าทายซ้ำ Cobra อาจปิด negotiation เร็วเกินไปเพราะกลัวว่าการยืดหยุ่นจะทำให้คำเตือนไร้ความหมาย
- **Share line seed:** *My nature belongs to the Cobra—the one who makes the final line visible.*

### Camel — The Bearer of the Long Measure

- **Identity promise:** You know the weight of a promise before you lift it—and that is why yours arrives.
- **Core desire:** เลือกภาระที่คู่ควรและพาคน ทรัพยากร หรือคำสัญญาผ่านระยะทางโดยไม่ใช้เกินจำเป็น
- **Core fear:** commitment ถูกให้โดยไม่เข้าใจ cost จนทุกคนต้องรับหนี้ที่ไม่มีใครถือไหว
- **Strength:** capacity planning, endurance, deliberate generosity และ reliability ระยะยาว
- **Shadow:** วัดทุก need เป็น logistics, แบกเกิน capacity เพราะเคยบอกว่าไหว และจดจำ cost จน generosity กลายเป็นบัญชี
- **Secret need:** ได้รับการดูแลโดยไม่ต้องพิสูจน์ก่อนว่าตนใช้ทรัพยากรนั้นคุ้ม
- **Relationship strategy:** สร้าง trust ด้วยข้อตกลงชัด การมาตามนัด และ generosity ที่รู้ต้นทุนแต่ยังเลือกให้
- **Embodies Desert:** foresight, restraint และ deliberate obligation
- **Resists Desert:** capacity มีไว้พาคนอื่นผ่าน ไม่ใช่สะสม leverage เหนือคนที่ต้องพึ่งตน
- **Ordinary anchor:** ก่อนรับงานจะถามระยะ เวลา reserve และคนที่ได้รับผล แต่เมื่อรับแล้วจะจัดการจนถึงปลายทาง
- **Pressure anchor:** เมื่อ reserve ต่ำ Camel อาจเงียบและแบกต่อเพราะการยอมรับว่าไม่ไหวรู้สึกเหมือนผิดสัญญา
- **Share line seed:** *My nature belongs to the Camel—the one whose promises survive the distance.*

### Scorpion — The Unbowed Sovereign

- **Identity promise:** Your right to a boundary is not measured by your size, status or usefulness.
- **Core desire:** ควบคุม access ต่อ body, time, secrets และ inner territory ของตนโดยไม่ต้องมีอำนาจเหนือใคร
- **Core fear:** ถูกมองว่าเล็ก เก็บตัว หรือไม่มี leverage จึงไม่มีสิทธิ์ปฏิเสธ
- **Strength:** compact courage, economy of force, privacy และ refusal ที่ไม่ต้องพึ่ง rank
- **Shadow:** anticipatory retaliation, isolation และตีความ approach ทุกอย่างเป็น intrusion
- **Secret need:** ความใกล้ชิดที่รอ consent ได้โดยไม่ทดสอบว่าจะถูกต่อยหรือไม่
- **Relationship strategy:** วงเล็ก access ชัด; loyalty สูงเมื่ออีกฝ่ายเคารพคำว่าไม่และไม่ใช้ intimacy เป็นสิทธิ์ครอบครอง
- **Embodies Desert:** ใช้พื้นที่และ force เท่าที่จำเป็น พร้อมรักษาสิ่งที่ไม่ควรถูกซื้อขาย
- **Resists Desert:** ปฏิเสธว่า wealth, contract หรือ hierarchy สามารถซื้อ access ส่วนตัวได้
- **Ordinary anchor:** ปฏิเสธ request สั้นและชัดโดยไม่แต่งเหตุผลยาวเพื่อให้คนอื่นอนุมัติ boundary
- **Pressure anchor:** เมื่อรู้สึก cornered Scorpion อาจลง consequence ก่อนตรวจว่าอีกฝ่ายไม่รู้ขอบเขตหรือจงใจละเมิด
- **Share line seed:** *My nature belongs to the Scorpion—the sovereign no throne can make smaller.*

### Oryx — The Keeper of the Inner Spring

- **Identity promise:** Enoughness can be radiant; survival does not require you to become barren inside.
- **Core desire:** รักษาความสง่างาม ความหวัง และ capacity for joy โดยไม่ปล่อยให้ desire กลายเป็น consumption
- **Core fear:** scarcity กลายเป็น identity จนชีวิตมีแต่การพิสูจน์ว่าไม่ต้องการอะไร
- **Strength:** self-regulation, graceful endurance, sustainable abundance และ calm collective movement
- **Shadow:** composure ปิดบัง need, aesthetic control ทำให้ความยุ่งเหยิงของชีวิตรู้สึกน่าอาย และความพอกลายเป็นการไม่ขอ
- **Secret need:** เชื่อว่าความต้องการของตนไม่ทำให้เป็น burden หรือคนที่มีวินัยน้อยลง
- **Relationship strategy:** generosity ที่ไม่เร่ง intimacy; สร้างบรรยากาศให้คนรับและให้ได้โดยไม่เสีย dignity
- **Embodies Desert:** restraint เป็นความพอที่เลือก ไม่ใช่ deprivation
- **Resists Desert:** ไม่ยอมให้ culture of scarcity ทำให้ beauty, celebration และ open-handedness ถูกมองเป็นความโง่
- **Ordinary anchor:** เลือกสิ่งของและ commitment น้อย แต่ดูแลให้เกิดความงามและ nourishment ต่อคนรอบข้าง
- **Pressure anchor:** เมื่อคนอื่น panic Oryx จะรักษาจังหวะและความสงบ แต่อาจซ่อนว่าตนเองก็ต้องการความช่วยเหลือ
- **Share line seed:** *My nature belongs to the Oryx—the one who keeps an inner spring beneath the sun.*

## Pairwise distinction matrix

| Pair | Shared ground | Deciding difference |
|---|---|---|
| Fennec ↔ Caracal | subtlety, low display, self-direction | Fennec listens for the cheapest opening; Caracal acts from a standard that does not require an opening |
| Fennec ↔ Cobra | sensitivity to risk and timing | Fennec works through small signals and adaptation; Cobra makes the signal explicit and attaches consequence |
| Fennec ↔ Camel | economy, foresight, warm usefulness | Fennec preserves options until the terrain speaks; Camel chooses a burden and preserves capacity to finish it |
| Fennec ↔ Scorpion | privacy, alertness, small-footprint action | Fennec cautiously opens toward possibility; Scorpion controls access until consent is unmistakable |
| Fennec ↔ Oryx | warmth, restraint, non-dominant presence | Fennec stays light by changing quickly; Oryx stays whole by needing neither excess nor constant escape |
| Caracal ↔ Cobra | composure, precision, strong limits | Caracal protects an inner standard; Cobra declares an external line and its consequence |
| Caracal ↔ Camel | discipline, self-command, reliability | Caracal refuses to bargain away dignity; Camel deliberately spends capacity on a chosen obligation |
| Caracal ↔ Scorpion | sovereignty, guardedness, refusal of hierarchy | Caracal remains dignified under judgment; Scorpion determines who receives access at all |
| Caracal ↔ Oryx | elegance, restraint, visible composure | Caracal finds freedom through exact standards; Oryx finds freedom through enoughness without austerity |
| Cobra ↔ Camel | clarity, foresight, seriousness about cost | Cobra prevents unacceptable cost by drawing a line; Camel accepts understood cost to carry a promise |
| Cobra ↔ Scorpion | defended boundaries and proportionate force | Cobra warns publicly so others can choose; Scorpion protects private access without owing public explanation |
| Cobra ↔ Oryx | restraint with visible presence | Cobra creates safety through prohibition; Oryx creates it through composure and sustainable abundance |
| Camel ↔ Scorpion | deliberate commitment and respect for limits | Camel accepts chosen weight; Scorpion refuses weight that was never consensually given |
| Camel ↔ Oryx | endurance, generosity, resource discipline | Camel proves capacity by carrying what matters; Oryx refuses to make burden the proof of worth |
| Scorpion ↔ Oryx | self-possession, quiet resilience | Scorpion preserves sovereignty through defended access; Oryx preserves it through open but self-regulated enoughness |

## Main ambiguity clusters

### Boundary cluster

```text
Caracal  → “What standard lets me remain myself?”
Cobra    → “What line must others see before consequence?”
Scorpion → “Who has the right to access me at all?”
```

Questions ต้องแยก `inner standard`, `public limit` และ `personal access` ไม่ใช่ถามเพียงว่าใคร “เด็ดขาด” หรือ “เก็บตัว”

### Restraint cluster

```text
Fennec → preserves possibility through lightness
Camel  → preserves capacity for chosen commitment
Oryx   → preserves inner abundance through enoughness
```

Questions ต้องแยก `keep options open`, `carry the selected weight` และ `choose enough without deprivation`

## Cross-realm boundary priorities

| Desert animal | High-risk Taiga neighbor | Required distinction |
|---|---|---|
| Fennec | Lynx / Wolverine | sensitivity that stays relational vs autonomous observation or disruptive action |
| Caracal | Lynx / Moose | dignity and inner standard vs freedom through distance or territorial order |
| Cobra | Moose | consent-based visible consequence vs impersonal boundary that preserves territory |
| Camel | Reindeer / Bear / Grey Wolf | chosen capacity vs communal continuity, sanctuary or coordinated outcome |
| Scorpion | Lynx / Wolverine | control of access vs detachment or escape from control |
| Oryx | Reindeer / Bear | enoughness and unashamed desire vs shared duty or protective preservation |

## Motive hypotheses

ยังไม่ใช่ production values:

| Animal | Likely supporting facets | Do not force into |
|---|---|---|
| Fennec | none yet; test curiosity/lightness as configuration first | Restraint เพียงเพราะใช้ resource น้อย |
| Caracal | Restraint supporting | Mastery หากไม่มี growth motive |
| Cobra | Restraint supporting; boundary remains metadata | Continuity หรือ duty เพียงเพราะรักษากฎ |
| Camel | Restraint defining, Continuity supporting, Mastery supporting | Duty-bound โดยอัตโนมัติ |
| Scorpion | boundary/access metadata | Restraint เพียงเพราะใช้ force น้อย |
| Oryx | Restraint defining | Recognition เพียงเพราะ visual presence สูง |

## Design decisions requiring review

1. **Scorpion title:** `The Unbowed Sovereign` แทน `The Small Sovereign` เพื่อรักษา compact-power fantasy โดยไม่ทำให้ผลลัพธ์รู้สึกด้อยกว่า
2. **Oryx role:** เป็น emotional counterweight ของ realm ทำให้ Desert ไม่เท่ากับ deprivation, mistrust และ severity ทั้งหมด
3. **Cobra tone:** sacred danger ต้องแปลเป็น explicit consent/consequence ไม่ใช่ manipulative mysticism
4. **Caracal tone:** prestige มาจาก dignity และ precision ไม่ใช่ aloof beauty อย่างเดียว
5. **Camel tone:** generosity ต้องมองเห็นชัดเพื่อแยกจาก Taiga-style duty และ logistics

## Gate before individual Bibles

- [x] approve identity fantasy และ working title ทั้ง 6 ตัว
- [x] approve Boundary cluster และ Restraint cluster
- [x] ทุกตัวมีอย่างน้อยหนึ่ง ordinary-life scenario ที่ไม่เกี่ยวกับ politics
- [x] เขียน cross-realm boundary questions สำหรับ Taiga neighbors ตัวละอย่างน้อยหนึ่งข้อ
- [x] สร้างไฟล์ `desert/*.md` ครบ 6 ตัว
- [x] กำหนด provisional vectors พร้อมกันใน joint Taiga–Desert model
- [x] เพิ่ม boundary item คู่ที่สองให้ remaining collision clusters
- [x] ผ่าน paired information-gain simulation โดยไม่มี regression เกิน 1 pp
