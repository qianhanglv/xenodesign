# Manifest — 三头蛇 / Triune Forest Serpent

**L0 ID:** `TTS-L0-01`  
**Requested levels:** L0, L1, L2, L3 only. No L4/L5.  
**Deliverables:** 10 SVG assets, 4 notes, this manifest, plus one additional oil-style portrait image.  
**Note limit:** 600 words; largest note is 463 words.

## File tree

```text
三头蛇/
├── L0/
│   ├── creature.svg
│   └── design.md
├── L1/
│   ├── front.svg
│   ├── back.svg
│   ├── left.svg
│   ├── right.svg
│   ├── top.svg
│   ├── bottom.svg
│   └── note.md
├── L2/
│   ├── section.svg
│   └── note.md
├── L3/
│   ├── skeleton.svg
│   ├── pelt.svg
│   └── note.md
├── portrait/
│   └── oil.png
└── manifest.md
```

## File manifest

`Note word count` is the whitespace-token count of the level note, including headings and tags. L1's single note covers all six views, so the six SVG rows share its count.

| File path | Level | Note word count | Source | [CANON]/[INFERRED] counts |
|---|---:|---:|---|---:|
| `三头蛇/L0/creature.svg` | L0 | 370 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L0/design.md` | L0 | 370 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/front.svg` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/back.svg` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/left.svg` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/right.svg` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/top.svg` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/bottom.svg` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L1/note.md` | L1 | 444 | Source: L0 TTS-L0-01 | 9/4 |
| `三头蛇/L2/section.svg` | L2 | 415 | Source: L0 TTS-L0-01 | 9/5 |
| `三头蛇/L2/note.md` | L2 | 415 | Source: L0 TTS-L0-01 | 9/5 |
| `三头蛇/L3/skeleton.svg` | L3 | 463 | Source: L0 TTS-L0-01 | 9/5 |
| `三头蛇/L3/pelt.svg` | L3 | 463 | Source: L0 TTS-L0-01 | 9/5 |
| `三头蛇/L3/note.md` | L3 | 463 | Source: L0 TTS-L0-01 | 9/5 |
| `三头蛇/manifest.md` | — | — | — | — |

**Totals:** notes 1,692 words; constraint tags 36 `[CANON]` and 18 `[INFERRED]`. The base 13-constraint set is 9 `[CANON]` / 4 `[INFERRED]`; L2 adds one level-specific `[INFERRED]` neck-junction tag and L3 adds one `[INFERRED]` connective-anatomy tag.

## Asset specification

| Asset | Contents |
|---|---|
| `L0/creature.svg` | One 3/4 full-body presentation plate; three role-bearing heads, one shared trunk, one curled tail; dark forest field. |
| `L1/front.svg` | Front projection; three heads fanned, two eyes each, one tail. |
| `L1/back.svg` | Dorsal/rear projection; heads turned back, paired lateral eye slivers, dorsal spine stripe, one tail. |
| `L1/left.svg` | Left orthographic side; three heads at different heights and directions, one coiled tail. |
| `L1/right.svg` | Exact mirrored projection of the left plate; same three heads and one tail. |
| `L1/top.svg` | Dorsal top view; three heads with paired dorsal eyes, one tail. |
| `L1/bottom.svg` | Ventral view; left/right reversed on the page, three heads with paired lateral eye turrets, one tail. |
| `L2/section.svg` | Longitudinal section; three necks join one body, one shared gut lumen, one tail; three teal marks identify inferred necks. |
| `L3/skeleton.svg` | One serpentine frame, three skulls on three cervical arches, two orbital fenestrae per skull, one tail, no limb or wing bones. |
| `L3/pelt.svg` | One continuous unfolded sheet; three head/neck holes, one tail opening, no limb or wing holes; continuous orange/black field across the seam. |

## Validation

- All 10 SVGs use `viewBox="0 0 512 512"`.
- No SVG contains `<text>`, `<image>`, `<script>`, `foreignObject`, or external `href=`.
- Largest SVG is 90,576 bytes, below 512 KB.
- Four notes are 370, 444, 415 and 463 words; all are below 600.
- Constraint coverage: every note contains one line for each of P1–N1, for 13 lines per note.
- Count coverage: 3 heads / 1 tail / 0 limbs / 0 wings / 6 eyes / 1 body across all head-bearing plates.
- Pelt topology: one compound path, one outer boundary, exactly 3 head/neck holes and exactly 1 tail opening; the seam is a line on one sheet, not a second piece.
- No lore or narrative prose is used.

## Self-check (8)

| # | Check | Result |
|---:|---|---|
| 1 | One creature; one body | Pass — every plate has one shared trunk; the pelt is one sheet; the skeleton is one frame. |
| 2 | viewBox 512; no text/image/script/external refs | Pass — 10/10 SVGs validated. |
| 3 | Exactly 3 heads, 1 tail, 0 limbs, 0 wings | Pass — 3 heads in L0/L1/L2/skeleton; 3 head holes in pelt; one tail or tail opening; no limb or wing forms. |
| 4 | 2 eyes per head in every view; 6 total | Pass — 6 rendered eyes in L0, each L1 view, L2; 6 amber orbital loci in the skeleton; pelt is headless. |
| 5 | Every constraint has one note line | Pass — 13 P1–N1 lines in each of the four notes. |
| 6 | Pelt is one sheet with 3 head holes and 1 tail opening | Pass — one compound outline with 4 fenestrations; no limb or wing holes. |
| 7 | No note exceeds 600 words | Pass — maximum 463. |
| 8 | No lore | Pass — notes are method, count and anatomy statements only. |

## Additional deliverable — oil-style portrait

| File | Format | Dimensions | Role |
|---|---|---:|---|
| `三头蛇/portrait/oil.png` | PNG, RGB | 1800 × 2400 px | Framed oil-style character portrait of the L0 design; painterly canvas texture, gilt frame, brass title plaque. |

This image is a presentation piece derived from `L0/creature.svg`. It does not replace any L0–L3 asset and is outside the 13-constraint note scheme.

## Reconciliations / conflicts

- **RECONCILE — P1 within one frame:** the 6 ft 6 in animal is coiled or projected, never cropped.
- **RECONCILE — F4 with L1 traceability:** the heads are independently posed per plate so three heads and six eyes remain countable; the trunk stays one body.
- **RECONCILE — L2 section plane with three lateral necks:** a single parasagittal plane cannot contain all three necks, so the flanking necks are cut projections; the teal marks state this explicitly.
- **RECONCILE — pelt openings with one continuous sheet:** the four openings are fenestrations in one surface, not cut pieces or an exploded view.
- **CONFLICT:** none. No same-group conflict required a priority decision.

**Bonus status:** non-humanoid — yes; non-cliché body plan — three independently role-specialized heads on one serpentine trunk; non-earth — not claimed, because P2 fixes the animal to Burkina Faso, Earth.
