# Cross-Biome Construct Audit v0.1

**Status:** Review  
**Last reviewed:** 2026-08-22  
**Scope:** Two qualitative anchors from each of the eight realms

## Decision

ทดสอบ sample จากทั้ง 8 realms ก่อนทำ biome ที่สองแบบ full เพราะความเสี่ยงหลักคือ Trait Model v0.3 อาจอธิบาย Taiga ได้ดีแต่ไม่มี construct สำหรับ identity fantasy ของ realm อื่น การทำ Taiga/Desert แบบละเอียดก่อนเห็นภาพทั้งโลกอาจทำให้ scoring overfit คู่แรกและต้องรื้อเมื่อ Savanna, Alpine หรือ Wetland เข้ามา

Audit นี้ใช้ animal สองตัวต่อ realm:

- **Embody anchor** — แสดง healthy gift ของ realm โดยตรง
- **Resist anchor** — อยู่ใน realm อย่างมีเหตุผลแต่ต่อต้าน shadow หรือ orthodoxy ของ realm

ยังไม่ให้ decimal vectors จุดประสงค์คือดูว่า dimensions ปัจจุบันมองเห็นความแตกต่างหรือมี motive ที่ตกหล่น

## Direction notation

```text
−−  strong negative pole
−   leaning negative
0   contextual / balanced
+   leaning positive
++ strong positive pole
```

เครื่องหมายเป็น qualitative hypothesis ไม่ใช่คะแนน final

## Anchor overview

| Realm | Embody anchor | Resist anchor | Central distinction |
|---|---|---|---|
| Taiga | Grey Wolf | Wolverine | build a reliable system vs break a system that no longer protects life |
| Arctic | Polar Bear | Arctic Fox | bear the covenant openly vs preserve its purpose through adaptation |
| Savanna | Lion | Hyena | concentrate witnessed direction vs distribute power through the chorus |
| Rainforest | Golden Lion Tamarin | Jaguar | grow reciprocity through care vs protect the network by enforcing a boundary |
| Desert | Camel | Fennec Fox | carry a deliberate obligation vs stay responsive enough to avoid unnecessary cost |
| Ocean | Octopus | Orca | reinvent beyond fixed form vs create stable chosen bonds inside changing currents |
| Alpine | Golden Eagle | Red Panda | master the height and direct from it vs practice sustainable skill without worshipping ascent |
| Wetland | Crocodile | Giant River Otter | preserve inherited continuity vs make belonging answerable to living kin now |

## Qualitative trait map

| Animal | AFF | AGY | SEN | STR | EXP | RSK | DCL | ALG |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Grey Wolf | − | ++ | + | ++ | − | 0 | − | + |
| Wolverine | −− | ++ | − | − | 0 | ++ | 0 | −− |
| Polar Bear | − | + | 0 | + | − | −− | + | ++ |
| Arctic Fox | 0 | 0 | + | −− | −− | 0 | 0 | + |
| Lion | + | ++ | 0 | + | ++ | + | 0 | + |
| Hyena | ++ | + | + | − | + | + | + | − |
| Golden Lion Tamarin | ++ | 0 | 0 | − | + | 0 | ++ | + |
| Jaguar | −− | ++ | 0 | − | − | + | − | − |
| Camel | + | 0 | + | ++ | − | −− | 0 | + |
| Fennec Fox | + | 0 | − | −− | 0 | + | + | − |
| Octopus | −− | + | ++ | −− | − | ++ | 0 | −− |
| Orca | ++ | ++ | + | − | + | + | + | ++ |
| Golden Eagle | − | ++ | ++ | + | + | + | − | + |
| Red Panda | − | − | 0 | + | − | −− | 0 | − |
| Crocodile | − | + | − | ++ | −− | −− | − | ++ |
| Giant River Otter | ++ | ++ | + | + | ++ | + | + | + |

## Anchor profiles

### Taiga — Grey Wolf / Wolverine

#### Grey Wolf — embody

- **Core desire:** ทำให้คนและทรัพยากรเคลื่อนไปสู่ outcome ที่ทุกคนพึ่งพาได้
- **Core fear:** ความไร้ทิศทางทำให้คนที่มีค่าถูกเสียไปโดยไม่มีใครรับผิดชอบ
- **Decision pattern:** รวบข้อมูล วาง direction แบ่งบทบาท และรับ burden ของ coordination
- **Relationship strategy:** เลือกวงเล็กที่ไว้ใจและสร้างความสนิทผ่าน competence ร่วมกัน
- **Embodies Taiga:** competence กลายเป็นระบบที่พาคนผ่าน winter
- **Resists Taiga:** loyalty ต่อคนจริงอาจมีน้ำหนักเหนือ efficiency ของ institution
- **Motive not fully visible in core traits:** responsibility-through-coordination ต่างจาก ambition หรือ dominance อย่างไร
- **Nearest within realm:** Moose, Bear
- **Nearest across realms:** Orca, Golden Eagle

#### Wolverine — resist

- **Core desire:** รักษาความเป็นไปได้เมื่อทางที่ถูกอนุญาตทั้งหมดปิดลง
- **Core fear:** system ใช้คำว่า order เพื่อบังคับให้ทุกคนติดอยู่กับ failure
- **Decision pattern:** ลงมือเร็ว เปลี่ยน terrain และยอมขัด authority เพื่อสร้างทางออก
- **Relationship strategy:** ปกป้องผ่าน intervention มากกว่าคำมั่นหรือการอยู่ใกล้
- **Embodies Taiga:** competence ยังคงทำงานภายใต้ frontier pressure
- **Resists Taiga:** ปฏิเสธ structure ทันทีเมื่อมันปกป้องตัวเองมากกว่าชีวิต
- **Motive not fully visible:** principled disruption ต่างจาก novelty seeking อย่างไร
- **Nearest within realm:** Lynx
- **Nearest across realms:** Octopus, Caracal

**Question seed:** เมื่อระบบแจกเสบียงกำลังล้ม—คุณ rebuild chain of command เพื่อให้ทุกคนเดินต่อ หรือทำลายข้อจำกัดและเปิดช่องทางที่ยังไม่มีใครรับรอง?

### Arctic — Polar Bear / Arctic Fox

#### Polar Bear — embody

- **Core desire:** เป็นผู้ที่ยังยืนเฝ้าเมื่อคนอื่นไม่สามารถรับภาระนั้นต่อได้
- **Core fear:** covenant กลายเป็นเพียงคำพูดและมีใครสักคนถูกทิ้งไว้ใน white
- **Decision pattern:** รับ cost ไว้กับตน ยืนขวาง danger และทำหน้าที่ให้มองเห็นได้
- **Relationship strategy:** แสดงความรักผ่าน protection, presence และ promise ที่ไม่ถอนคืนง่าย
- **Embodies Arctic:** sacred duty ทำให้ไม่มีชีวิตที่ถูกฝากไว้ต้องหายไปตามลำพัง
- **Resists Arctic:** guardian conscience มีสิทธิ์ท้ากฎที่รักษารูปพิธีแต่ทรยศความหมายของ covenant
- **Motive not fully visible:** sacred protection ต่างจาก Taiga sanctuary หรือ Desert obligation อย่างไร
- **Nearest within realm:** Snowy Owl, Walrus
- **Nearest across realms:** Taiga Bear, Camel, Crocodile

#### Arctic Fox — resist

- **Core desire:** รักษาสิ่งสำคัญให้รอดด้วยวิธีที่เปลี่ยนได้ตามน้ำแข็งและข้อมูลใหม่
- **Core fear:** ritual rigidity ทำให้ผู้คนตายเพื่อแสดงว่ากฎยังคงบริสุทธิ์
- **Decision pattern:** อ่านช่องว่าง ปรับเส้นทาง และทำงานเงียบพอที่จะไม่สร้าง panic
- **Relationship strategy:** loyalty ผ่าน timely intelligence มากกว่าการประกาศ sacrifice
- **Embodies Arctic:** ไม่ทิ้ง covenant แต่รักษาหน้าที่ผ่าน vigilance
- **Resists Arctic:** fidelity ไม่จำเป็นต้องรักษา form เดิม
- **Motive not fully visible:** adaptation in service of duty ต่างจาก self-authored opportunism อย่างไร
- **Nearest within realm:** Narwhal
- **Nearest across realms:** Fennec Fox, Lynx

**Question seed:** เมื่อ covenant route ใช้ไม่ได้—คุณประกาศรับภาระและพาคนผ่านตามหลักที่ยังเหลือ หรือเปลี่ยนพิธีและเส้นทางเงียบ ๆ เพื่อรักษาจุดประสงค์ของคำมั่น?

### Savanna — Lion / Hyena

#### Lion — embody

- **Core desire:** ใช้ presence ทำให้ความกล้าและ direction กลายเป็นสิ่งที่คนอื่นตอบรับได้
- **Core fear:** ไม่มีใครยืนในที่เปิดเมื่อสังคมต้องการ accountability
- **Decision pattern:** ก้าวสู่ center ประกาศสิ่งที่ตนรับผิดชอบ และยอมให้สาธารณะตัดสิน
- **Relationship strategy:** สร้าง trust ผ่าน visible commitment และความพร้อมแบกรับ scrutiny
- **Embodies Savanna:** strength becomes real through witness
- **Resists Savanna:** visibility ไม่ใช่ entitlement และ crown ต้องตอบต่อคนที่มองอยู่
- **Motive not fully visible:** desire for witnessed impact ไม่เท่ากับ EXP หรือ AGY สูง
- **Nearest within realm:** Elephant, Secretary Bird
- **Nearest across realms:** Golden Eagle, Grey Wolf

#### Hyena — resist

- **Core desire:** ทำให้คนที่ไม่มี throne รวมเสียง ความรู้ และ survival intelligence เป็นอำนาจได้
- **Core fear:** reputation economy ตัดสินว่าใครน่าเชื่อก่อนฟังสิ่งที่เขารู้
- **Decision pattern:** กระจายข้อมูล สร้าง coalition และใช้หลายเสียงกดดัน center
- **Relationship strategy:** belonging ผ่าน chorus, humor, mutual usefulness และการไม่ทิ้ง outsider
- **Embodies Savanna:** power ต้องถูกได้ยินและตอบสนองในพื้นที่สาธารณะ
- **Resists Savanna:** prestige ไม่ควรผูกกับ respectable appearance หรือสายเลือด
- **Motive not fully visible:** network influence ต่างจาก intimacy, care หรือ consensus seeking อย่างไร
- **Nearest within realm:** Greater Kudu, Elephant
- **Nearest across realms:** Golden Lion Tamarin, Giant River Otter, Dolphin

**Question seed:** เมื่อ court ปิดบังความล้มเหลว—คุณยืนกลางลานและผูกชื่อของตนกับคำตอบ หรือทำให้ข้อมูลเดินทางผ่านเครือข่ายจน center ไม่สามารถควบคุมเรื่องเล่าได้?

### Rainforest — Golden Lion Tamarin / Jaguar

#### Golden Lion Tamarin — embody

- **Core desire:** ทำให้ชีวิตเติบโตผ่าน care ที่หมุนเวียนและไม่มีใครต้องสร้าง belonging คนเดียว
- **Core fear:** connection ถูกเปลี่ยนเป็น favor ที่มีเจ้าของและทวงคืนภายหลัง
- **Decision pattern:** เริ่มจากคนที่ได้รับผลกระทบ กระจาย care และซ่อมความไว้วางใจผ่านการลงมือร่วมกัน
- **Relationship strategy:** intimacy, shared attention และ reciprocal caretaking
- **Embodies Rainforest:** nothing flourishes alone
- **Resists Rainforest:** care ต้องชัดและสมัครใจ ไม่ใช่หนี้ใน network ที่ไม่มีใครมองเห็น
- **Motive not fully visible:** reciprocity ต่างจาก AFF+, DCL+ หรือ duty อย่างไร
- **Nearest within realm:** Scarlet Macaw
- **Nearest across realms:** Capybara, Reindeer, Harp Seal

#### Jaguar — resist

- **Core desire:** รักษาพื้นที่ที่มีชีวิตโดยไม่ยอมให้ network ใช้ความสัมพันธ์เป็นข้ออ้างข้าม boundary
- **Core fear:** ทุกคนเชื่อมกันจนไม่มีใครรับผิดชอบการรุกล้ำ
- **Decision pattern:** สังเกตเงียบ เลือก moment และออก action ที่ชัดโดยไม่รอ consensus
- **Relationship strategy:** respect ผ่าน autonomy และ boundary ที่ไม่ต้องเจรจาซ้ำทุกครั้ง
- **Embodies Rainforest:** อ่าน terrain และผลกระทบใน ecosystem อย่างลึก
- **Resists Rainforest:** interdependence ไม่ให้สิทธิ์ใครเข้าถึงทุกชีวิต
- **Motive not fully visible:** protective sovereignty ต่างจาก Desert self-possession หรือ Ocean autonomy อย่างไร
- **Nearest within realm:** Okapi, Orchid Mantis
- **Nearest across realms:** Caracal, Great White, Snow Leopard

**Question seed:** เมื่อพันธมิตรเก่าใช้ความสัมพันธ์ขอข้อยกเว้นที่ทำร้ายชุมชน—คุณเปิดวง care เพื่อซ่อม reciprocal trust หรือปิด boundary และหยุด access ก่อนการเจรจา?

### Desert — Camel / Fennec Fox

#### Camel — embody

- **Core desire:** เลือกภาระที่คู่ควรแล้วพามันผ่านระยะทางโดยไม่ใช้ทรัพยากรเกินจำเป็น
- **Core fear:** promise ถูกให้โดยไม่เข้าใจ cost จนทุกคนต้องจ่ายหนี้ที่ไม่มีใครถือไหว
- **Decision pattern:** วัดระยะ ต้นทุน reserve และ commitment ก่อนออกเดิน จากนั้นไม่ทิ้งภาระง่าย
- **Relationship strategy:** trust ผ่าน exchange ที่ชัดและ capacity ที่พิสูจน์ได้ในระยะยาว
- **Embodies Desert:** restraint, foresight และ deliberate obligation
- **Resists Desert:** capacity มีไว้แบ่งและพาคนอื่นผ่าน ไม่ใช่สร้าง leverage
- **Motive not fully visible:** chosen sufficiency ต่างจาก fear-based preservation หรือ duty อย่างไร
- **Nearest within realm:** Oryx
- **Nearest across realms:** Reindeer, Yak, Polar Bear

#### Fennec Fox — resist

- **Core desire:** รักษาความเบา ความอยากรู้ และทางเลือกไว้ในโลกที่ทุก cost ถูกนับ
- **Core fear:** scarcity discipline กลายเป็น suspicion ที่ปิดทุก possibility ก่อนมันเกิด
- **Decision pattern:** ฟัง signal เล็ก ปรับเร็ว และหาทางที่ใช้ทรัพยากรน้อยกว่าการชนตรง
- **Relationship strategy:** เปิด trust ทีละน้อยผ่าน curiosity, charm และ timely usefulness
- **Embodies Desert:** economy, sensitivity และ respect for limits
- **Resists Desert:** ไม่ยอมให้ self-possession กลายเป็น emotional isolation
- **Motive not fully visible:** lightness under scarcity ต่างจาก Arctic Fox duty adaptation อย่างไร
- **Nearest within realm:** Oryx, Caracal
- **Nearest across realms:** Arctic Fox, Golden Lion Tamarin

**Question seed:** เมื่อ caravan agreement แพงกว่าที่คาด—คุณรักษาภาระที่เลือกไว้และจัด reserve ใหม่ หรือฟังข้อมูลข้างทางแล้วเปลี่ยนข้อตกลงก่อน cost กลายเป็น debt?

### Ocean — Octopus / Orca

#### Octopus — embody

- **Core desire:** รักษา freedom ที่จะเปลี่ยน form, tool และวิธีคิดโดยไม่ถูก identity เดียวกักไว้
- **Core fear:** group หรือ history ตั้งชื่อรูปแบบหนึ่งแล้วห้ามตนกลายเป็นอย่างอื่น
- **Decision pattern:** ทดลองหลายทาง ใช้ terrain เป็นเครื่องมือ และออกจาก frame ของปัญหาเดิม
- **Relationship strategy:** selective contact, negotiated access และ autonomy สูง
- **Embodies Ocean:** adaptation makes reinvention possible
- **Resists Ocean:** ไม่จำเป็นต้องเข้าร่วม federation เพียงเพราะทุกคนเคลื่อนไหวได้
- **Motive not fully visible:** identity fluidity ต่างจาก disruption หรือ low commitment อย่างไร
- **Nearest within realm:** Manta Ray, Great White
- **Nearest across realms:** Wolverine, Lynx

#### Orca — resist

- **Core desire:** ทำให้ chosen bonds แข็งแรงพอจะเดินทางผ่านโลกที่ไม่มีพรมแดนคงที่
- **Core fear:** adaptation ถูกใช้เป็นข้ออ้างจากไปก่อน relationship ต้องการความรับผิดชอบ
- **Decision pattern:** อ่านสถานการณ์ร่วมกัน ประสานบทบาท และเปลี่ยน tactics โดยไม่ทิ้ง clan
- **Relationship strategy:** intense chosen belonging, shared language และ coordinated trust
- **Embodies Ocean:** mobility, intelligence และ adaptive strategy
- **Resists Ocean:** บาง bond ควรมั่นคงแม้ current เปลี่ยน
- **Motive not fully visible:** chosen-clan continuity ต่างจาก Wolf system loyalty หรือ Giant Otter kin defense อย่างไร
- **Nearest within realm:** Dolphin
- **Nearest across realms:** Grey Wolf, Giant River Otter

**Question seed:** เมื่อ coalition แตกและเส้นทางเดิมหายไป—คุณเปลี่ยน form และแก้ปัญหาโดยไม่ผูกกับ group เดิม หรือรวม chosen people ให้เปลี่ยน tactics ไปพร้อมกัน?

### Alpine — Golden Eagle / Red Panda

#### Golden Eagle — embody

- **Core desire:** ฝึก vision และ command ให้สูงพอจะรับผิดชอบ direction ที่คนข้างล่างยังมองไม่เห็น
- **Core fear:** authority ถูกมอบโดยไม่มี proof หรือคนเห็น summit แต่ไม่เห็นเส้นทาง
- **Decision pattern:** สร้าง vantage ตรวจ pattern เลือก direction และลงมืออย่างเด็ดขาด
- **Relationship strategy:** respect ผ่าน competence, clarity และมาตรฐานสูงที่ตนยอมรับก่อน
- **Embodies Alpine:** mastery earns authority
- **Resists Alpine:** insight ต้องยอมลงจากความสูงและสร้างผลต่อชีวิตจริง
- **Motive not fully visible:** aspiration/mastery ต่างจาก Taiga competence หรือ Savanna visibility อย่างไร
- **Nearest within realm:** Snow Leopard
- **Nearest across realms:** Lion, Grey Wolf, Giraffe

#### Red Panda — resist

- **Core desire:** มีชีวิตที่ skill, balance และจังหวะยั่งยืนโดยไม่ต้องเปลี่ยนทุกวันเป็น trial
- **Core fear:** achievement culture เรียก exhaustion ว่า dedication และ rest ว่า failure
- **Decision pattern:** จำกัด expenditure เลือกเส้นทางที่รักษาสมดุล และฝึกสิ่งเล็กอย่างสม่ำเสมอ
- **Relationship strategy:** private warmth, gentle boundaries และ trust ที่ไม่เร่ง performance
- **Embodies Alpine:** quiet skill และ energy discipline ใน terrain ที่ demanding
- **Resists Alpine:** intrinsic worth ไม่ต้องถูก earned ผ่าน suffering หรือ public ascent
- **Motive not fully visible:** sustainable mastery ต่างจาก preserving risk orientation อย่างไร
- **Nearest within realm:** Ibex, Yak
- **Nearest across realms:** Bear, Capybara

**Question seed:** เมื่อ prestigious trial เริ่มทำลายคนที่พยายามผ่าน—คุณรับ oversight และ redesign มาตรฐานให้พิสูจน์ mastery จริง หรือปฏิเสธ pace ของ trial และสร้าง practice ที่ยั่งยืนนอกระบบ?

### Wetland — Crocodile / Giant River Otter

#### Crocodile — embody

- **Core desire:** รักษา continuity และ boundary ที่ผ่านเวลามานานพอจะรู้ว่าการลืมมีราคา
- **Core fear:** present urgency ลบ promise, territory และ consequence ที่ยังไม่จบ
- **Decision pattern:** รอจน pattern ชัด ยึด precedent และลง action เด็ดขาดเมื่อ threshold ถูกข้าม
- **Relationship strategy:** trust ช้า จำได้ยาว และถือการกระทำเก่าเป็นส่วนหนึ่งของ present relationship
- **Embodies Wetland:** nothing is ever truly forgotten
- **Resists Wetland:** ambiguity ต้องจบเมื่อ boundary และ consequence ชัดพอ
- **Motive not fully visible:** inherited continuity ต่างจาก duty, structure หรือ preserving risk อย่างไร
- **Nearest within realm:** Python, Heron
- **Nearest across realms:** Moose, Cobra, Polar Bear

#### Giant River Otter — resist

- **Core desire:** ทำให้ belonging เป็นสิ่งที่คนเป็น ๆ สื่อสาร ปกป้อง และสร้างร่วมกันตอนนี้
- **Core fear:** old families และ hidden patronage อ้าง history เพื่อปิดเสียงคนที่ต้องอยู่กับผลลัพธ์
- **Decision pattern:** เรียกกลุ่มให้ตอบสนองพร้อมกัน ทำ intention ให้ได้ยิน และปกป้อง kin อย่าง active
- **Relationship strategy:** vocal loyalty, collective defense, play และ repair หลัง conflict
- **Embodies Wetland:** community รู้จัก terrain, history และภัยที่ซ่อนใต้ผิวน้ำ
- **Resists Wetland:** living loyalty มีน้ำหนักเหนือ inherited debt
- **Motive not fully visible:** kin defense ต่างจาก Orca clan strategy, Hyena network หรือ Tamarin reciprocity อย่างไร
- **Nearest within realm:** Capybara
- **Nearest across realms:** Orca, Hyena, Dolphin

**Question seed:** เมื่อ treaty เก่าปกป้อง ruling house แต่ทำร้ายครอบครัวที่อยู่ริมแม่น้ำตอนนี้—คุณถือ continuity ไว้จนมีกลไกแก้ที่ชอบธรรม หรือรวม kin ให้หยุดผลกระทบและบังคับเปิดการเจรจาใหม่?

## Dimension coverage result

### What the eight core dimensions cover well

- วิธีเข้าสังคมและระดับ autonomy (`AFF`)
- การรับหรือสร้าง direction (`AGY`)
- วิธีสร้าง confidence จากข้อมูล (`SEN`)
- การตอบสนองต่อ uncertainty ด้วย adaptation หรือ structure (`STR`)
- visibility ของ inner state (`EXP`)
- preservation กับ exploration (`RSK`)
- consistent standard กับ relational context (`DCL`)
- self-authored conscience กับ role/promise (`ALG`)

แกนทั้งแปดยังมีประโยชน์และไม่ควรถูกแทนด้วย realm axes

### Motive gaps exposed by the 16 anchors

| Candidate facet | Core question | Collision it explains | Why current traits are insufficient |
|---|---|---|---|
| Recognition | Does impact become meaningful through being witnessed? | Lion / Golden Eagle / Grey Wolf | `EXP` วัด visibility แต่ไม่วัดว่าผู้เล่นต้องการ public witness หรือเพียงสื่อสารชัด |
| Mastery | Is growth through disciplined capability a central source of meaning? | Golden Eagle / Grey Wolf / Camel | `STR` และ `AGY` วัด strategy แต่ไม่วัด aspiration หรือการพัฒนาความสามารถเป็นเป้าหมาย |
| Reciprocity | Does mutual flourishing create obligation and belonging? | Tamarin / Hyena / Giant Otter | `AFF` และ `DCL` แยก collaboration/context แต่ไม่แยก care exchange, network power และ kin defense |
| Continuity | Should identity and obligation carry something forward across time? | Crocodile / Polar Bear / Camel / Orca | `ALG` วัด source of duty แต่ไม่แยก covenant, inherited memory, chosen obligation และ return |
| Restraint | Does choosing less protect freedom and meaning? | Camel / Polar Bear / Taiga Bear | `RSK−` รวม deliberate sufficiency, fear of loss และ protective preservation ไว้ด้วยกัน |

Facets เหล่านี้เป็น **candidate measurement metadata** ยังไม่ใช่ primary dimensions การเพิ่มทั้งห้าเป็น numeric axes ทันทีจะทำให้ model บวมและ evidence ต่อแกนบางเกินไป

## Critical collision findings

### Core traits alone are likely insufficient

1. **Grey Wolf / Golden Eagle** — directive, analytical, structured และ duty-aware เหมือนกัน แต่ competence-for-reliability ต่างจาก mastery-for-ascent
2. **Polar Bear / Camel / Crocodile** — preserving, structured และ duty-bound เหมือนกัน แต่ covenant protection, deliberate obligation และ inherited continuity เป็นคนละ motive
3. **Hyena / Golden Lion Tamarin / Giant River Otter** — collaborative, expressive และ relational เหมือนกัน แต่ network influence, reciprocal care และ kin defense ต่างกัน
4. **Arctic Fox / Fennec Fox** — adaptive, subtle fox archetypes เหมือนกัน แต่หนึ่งปรับเพื่อรักษา duty อีกหนึ่งปรับเพื่อรักษาทางเลือก

### Core traits distinguish these anchors well

- Grey Wolf / Wolverine
- Lion / Hyena
- Tamarin / Jaguar
- Camel / Fennec
- Octopus / Orca
- Golden Eagle / Red Panda
- Crocodile / Giant River Otter

Polar Bear / Arctic Fox แยกพฤติกรรมได้ แต่ realm membership ต้องพึ่ง duty motive ที่ชัดในคำถาม

## Construct decision

1. **Keep the eight core behavioral dimensions for v0.4.** ไม่มีหลักฐานพอให้ตัดหรือรวมแกนใด
2. **Add motive tags to Question Evidence Schema v0.2** สำหรับ Recognition, Mastery, Reciprocity, Continuity และ Restraint
3. **Do not score all motive tags as dimensions yet.** ใช้ construct coverage และ simulated candidate discrimination ตัดสินทีละ facet
4. **Build a 16-anchor numeric sandbox next.** ให้ provisional values กับ core traits และทดลอง motive features แยกเป็น ablation: core-only เทียบ core+facet
5. **Only then build one second biome fully.** หาก sandbox ผ่าน ให้ใช้ Taiga + Desert เป็น full cross-biome slice เพราะเป็น boundary ที่ชนกันที่สุด

## Exit gate before full Taiga + Desert

- anchor ทุกตัวมี nearest-neighbor distinction ที่คำถามสังเกตได้อย่างน้อยสองสถานการณ์
- core-only baseline และ core+facet variants เปรียบเทียบได้ด้วย simulation เดียวกัน
- adding a facet ต้องลด collision ที่ตั้งใจโดยไม่ทำให้ unrelated animals แย่ลงอย่างมาก
- animal and realm priors ถูก normalize ไม่ให้ roster size สร้างความได้เปรียบ
- question evidence รองรับ value และ weight แยกกัน
- ไม่มีการ tune decimals เพื่อบังคับผลลัพธ์ที่ construct wording ยังอธิบายไม่ได้

## Recommended next artifact

`Question Evidence Schema v0.2 + 16-Anchor Numeric Sandbox` ก่อนเขียน Desert Animal Bible, result copy หรือ artwork
