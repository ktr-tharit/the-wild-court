# Theme System v0.1 — Boreal Ceremonial

## Intent

The Wild Court ควรรู้สึกเหมือนพิธีกรรมที่เชื้อเชิญให้ผู้เล่นมองตัวเอง ไม่ใช่ dashboard, fantasy combat UI หรือแบบทดสอบออนไลน์ทั่วไป

หลักของ theme:

- **Spectacle is dark; reflection is light.** Opening, Judgment และ Reveal ใช้พื้นมืด ส่วนคำถามยาวใช้พื้นสว่าง
- **Prestige without gold.** ใช้ copper และ silver-lichen แทนทอง เพื่อไม่ให้โลกดูเป็นราชสำนัก fantasy ทั่วไป
- **One accent, one meaning.** Copper = identity/recognition, Covenant Red = consequence/progress
- รูปทรงเน้นเส้น กรอบ และพื้นที่ว่าง ไม่ใช้ rounded cards จำนวนมาก

## Color tokens

| Token | Hex | Role |
|---|---|---|
| Pine Night | `#08110E` | ceremonial background, opening, reveal |
| Deep Fir | `#10221B` | elevated dark surface |
| Forest Glass | `#183029` | atmospheric depth |
| Frosted Bone | `#E7E3D7` | long-form reading surface |
| Snow Mist | `#F5F3EC` | high-emphasis light text/surface |
| Lichen Silver | `#A8B5A7` | guidance, metadata, secondary text |
| Ember Copper | `#C78E62` | identity, warmth, selected recognition |
| Covenant Red | `#743B3D` | consequence, progress, warning |
| Ink | `#17221C` | primary text on light surfaces |
| Muted Ink | `#59645D` | secondary text on light surfaces |

## Typography

- Display: classical serif with organic contrast; prototype uses Georgia for zero-dependency reliability
- Interface/body: neutral sans serif
- English display copy can be large and compressed in line-height
- Thai body copy uses generous line-height and avoids ultra-light weights
- Uppercase tracking is reserved for navigation, realm labels and ritual metadata

## Surface rhythm

```text
Opening / Threshold   Pine Night
Story Question        Frosted Bone
Act Transition        Pine Night
Judgment              Pine Night
Result Long Read      Frosted Bone
Share Card            Pine Night
```

## Accessibility guardrails

- Body copy never uses Copper or Covenant Red as its only text color
- Selected choices use shape, fill and symbol together—not color alone
- Minimum touch target approximately 44px
- Respect reduced-motion preference
- Thai body copy target line-height 1.7–1.9
