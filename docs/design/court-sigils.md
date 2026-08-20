# Court Sigils v0.1

**Status:** Prototype accepted  
**Scope:** Narrative transitions and realm reveal

Court Sigils replace temporary letter marks with a visual language that belongs to The Wild Court. They are not alphabetic abbreviations and should remain readable without knowing English.

## Shared visual grammar

- Pale lichen lines (`#A8B5A7`) describe the court, paths, boundaries and living structure.
- Ember copper (`#C78E62`) marks the player, the decisive moment or the living heart of a symbol.
- Open geometry and transparent backgrounds let the marks sit on dark ceremonial surfaces without becoming badges or app icons.
- Rounded strokes keep the system organic and non-militaristic.
- Every mark must remain recognizable at the small interlude size and may not rely on text.

## Current set

| Sigil | Meaning | Visual construction | Asset |
|---|---|---|---|
| Bonds | Lives and routes becoming connected | Two branching routes cross around a shared ember | `/sigils/bonds.svg` |
| Fracture | A whole put under pressure by a consequential split | A broken ring with an ember-colored fault line | `/sigils/fracture.svg` |
| Judgment | Many possible actions resolving into one revealed nature | Three paths converge at a central ember and rise toward one point | `/sigils/judgment.svg` |
| Taiga | Endurance, stored warmth and deep-rooted order | A northern pine above roots/tree rings with an ember in its trunk | `/sigils/taiga.svg` |

## Placement rules

- Act sigils appear once at the start of an interlude, before the remembered choices.
- Realm sigils appear during the realm reveal and should never compete with the realm artwork or animal portrait.
- Do not use sigils as answer labels, scoring indicators or decorative repeat patterns.
- Keep the visible act/realm name in nearby text; the symbol supports recognition rather than replacing accessible language.

## Motion and accessibility

- Entry motion is a short fade, scale and upward settle.
- A single faint ring may expand once to suggest the Court responding.
- Motion must stop under `prefers-reduced-motion: reduce`.
- Images are decorative (`aria-hidden` with empty alt text) because the adjacent heading carries the meaning.

## Expansion rule

Future biome sigils should use the same stroke weight, palette and ember logic, but derive their silhouette from the biome's ecology rather than a political crest. Review the full set in monochrome and at small size before locking it.
