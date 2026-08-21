# Branching Strategy

**Status:** Accepted  
**Last reviewed:** 2026-08-22

## Branch hierarchy

```text
main
└── dev
    ├── biome/desert
    ├── biome/arctic
    ├── biome/savanna
    └── biome/<realm>
```

| Branch | Purpose | Merge target |
|---|---|---|
| `main` | playable, tested release state | — |
| `dev` | integration state for completed biome slices | `main` เมื่อพร้อม release |
| `biome/<realm>` | lore, animals, vectors, questions, results และ visuals ของ realm หนึ่ง | `dev` |
| `feature/<name>` | งานข้าม realm หรือ product feature ที่มี scope ชัด | `dev` |
| `hotfix/<name>` | แก้ release defect เร่งด่วนจาก `main` | `main` แล้ว sync กลับ `dev` |

## Working rules

- แตก `biome/*` และ `feature/*` จาก `dev` ล่าสุด
- branch ต้องสั้นพอให้ review เป็น slice ได้ ไม่เก็บหลาย biome ใน branch เดียว
- merge เข้า `dev` เมื่อ docs/data/runtime ที่เกี่ยวข้องผ่าน tests และ checklist ของ slice
- merge `dev` เข้า `main` เมื่อ integration test ผ่านและผลลัพธ์ที่ user เห็นเล่นได้ต่อเนื่อง
- ห้ามทดลอง vectors หรือ artwork ที่ยังไม่ผ่าน review บน `main`
- หาก biome branch ใช้ construct ใหม่ ให้ validate กับ existing realms ก่อน merge เข้า `dev`

## Current branches

- `main` — Taiga playable baseline
- `dev` — cross-biome construct audit และ numeric sandbox
- `biome/desert` — Desert Animal Bible และ Taiga/Desert vertical slice

`design/cross-biome-sandbox` เก็บเป็น historical feature branch ได้จน `dev` ถูก merge เข้า `main`; หลังจากนั้นจึงลบได้แบบ recoverable ผ่าน GitHub history
