# Literary creatures — bonus extension

Five text-only fan designs made from the D2 prompts, kept at the **end** of the project as an entertainment extension. They are **not** part of the 152-SVG benchmark, the model comparison, or the D1/D2/D3 card set.

Open the gallery: [index.html](index.html)  
Post draft: [post.md](post.md)  
Prompts: [three creatures](prompts/three-creatures-d2.md) · [Black Tai Sui / Water Monkey](prompts/black-taisui-water-monkey-d2.md)

> These are fan interpretations, not official canon. Each note keeps `[CANON]` and `[INFERRED]` tags. Short source clues are paraphrased; no film, game, animation, or fan-art reference was used.

## What is here

| Creature | Work | Levels | Portrait | Verdict |
|---|---|---|---|---|
| Watcher in the Water | *The Lord of the Rings* | L0–L3 | yes | 21 tentacles read; six views are weak |
| Runespoor | *Harry Potter* | L0–L3 | yes | best concept; pelt is explicitly headless |
| Feathered Serpent | *Lord of the Mysteries* | L0–L4 | yes | best portrait / best visual; pelt is a headless cape |
| Black Tai Sui | *Dao of the Bizarre Immortal* | L0–L3 | no | best body horror; least information |
| Water Monkey | *Dao of the Bizarre Immortal* | L0–L3 | no | best actual design: head/neck/4 limbs survive the pelt |

## The important finding

The Runespoor and Feathered Serpent outputs were generated **before** the head/neck pelt fix. Their own notes say it plainly:

- Runespoor L3: “in the headless pelt this directionality is hidden with the heads.”
- Feathered Serpent L3: “The pelt has no eye holes; the eyes are removed with the head.”

That is not a model hallucination: the old L3 prompt never required the head and neck to be part of the sheet. A torso-only sheet satisfied “one continuous piece”.

The Water Monkey output was generated **after** the fix, and its pelt explicitly records:

- `HEAD/NECK: 1 head attached; NECK: continuous bridge to torso`
- 4 limb sleeves, 2 eye sockets, 1 mouth, 2 ear holes

So the comparison is also a prompt experiment:

| Prompt version | Creature | Pelt head/neck |
|---|---|---|
| old L3 prompt | Runespoor | omitted; “headless pelt” |
| old L3 prompt | Feathered Serpent | omitted; “eyes removed with the head” |
| new L3 prompt | Water Monkey | attached head + neck |
| new L3 prompt | Black Tai Sui | `HEAD: none in this design` (correct for this creature) |
| old L3 prompt | Watcher | no head by canon (correct) |

## Subjective scorecard (5 = best)

| Creature | Visual | Six views | Pelt | Concept | Postability |
|---|---:|---:|---:|---:|---:|
| Feathered Serpent | 5 | 4 | 2 | 5 | 5 |
| Water Monkey | 4 | 4 | 5 | 3 | 3 |
| Runespoor | 4 | 3 | 1 | 5 | 4 |
| Watcher in the Water | 3 | 2 | 4 | 4 | 3 |
| Black Tai Sui | 3 | 2 | 3 | 5 | 2 |

“Pelt” scores whether the head/neck rule is met, not whether the sheet is pretty. This is why Feathered Serpent and Runespoor fail even though they look good.

## What passed / what failed

### Water Monkey — best design

- The pelt is the only one that reads as a **whole animal skin**: head lobe, neck bridge, four limb sleeves, eye sockets, mouth, ear holes.
- The section and skeleton share the same four-limbed plan.
- Weakness: at L0 it reads more like a frog/humanoid than a “water monkey”; the black hair and water-weed limbs are there, but the silhouette is friendly rather than eerie.

### Feathered Serpent — best portrait, failed pelt

- The oil portrait is the strongest image in the set: close-up head, green-black scales, white feathers, gold symbols, painterly texture.
- L0/L1/L4 read as one creature: 2 wings, 1 head, 2 pale-flame eyes, 1 tail, 0 legs.
- But the pelt has a **head opening with no attached head**: a green cape with a white central strip and two wing sleeves. Under the new rule it is a fail.
- The portrait cannot prove the L1/L3 design; it is a beautiful crop, not a full-body test.

### Runespoor — best concept, most explicit failure

- Three heads with planner/dreamer/critic roles is the strongest “literary” hook.
- The portrait is a clean framed poster, but it reads more like a vector graphic than an oil study; the three heads are similar, so the three roles are not visible.
- The pelt is a pear-shaped tiger-striped sheet with three holes and one tail hole. The heads are gone. The note itself calls it a “headless pelt”.
- L1 also drifts: the three heads change orientation and spacing across views; the roles are not preserved.

### Watcher in the Water — best constraint, weakest six views

- 21 tentacles, no head, no eyes: the count constraint is clear and the no-head rule is correct.
- The pelt is a radial sheet with 21 sleeves and one central opening; it is a good topological exercise.
- L1 front/back/left/right are almost identical: radial symmetry makes the six-view test less informative. The 21 count is asserted in the note, but hard to verify at a glance.
- The portrait is too dark: mood over evidence; the tentacles merge into the frame.

### Black Tai Sui — best atmosphere, least evidence

- The soft blob, stink pores, tentacles, and wet mottling read as body horror.
- No head is correct for this design, and the pelt says `HEAD: none in this design`.
- L1 front/back/left/right are very similar; the “cut limbs still move” and “possession” traits cannot be shown in a static L0.
- No portrait; it is the least “postable” of the five.

## What to say in a post

1. **The pelt is the story.** The prettiest portrait (Feathered Serpent) fails the pelt; the least pretty creature (Water Monkey) passes it.
2. **A portrait is not a design test.** A close-up can hide the missing head, the extra limb, or the wrong count.
3. **The old prompt caused the headless pelts.** This is a prompt bug, not a model conspiracy; the new prompt fixed it, and Water Monkey proves the fix.
4. **Radial symmetry is a weak six-view subject.** Watcher and Black Tai Sui look consistent because they are radially symmetric, not because they have a strong 3D ledger.
5. **Canon vs inference.** The notes mark `[CANON]` and `[INFERRED]`; don’t present inferred anatomy as original canon.

## License / credits

Fan designs for commentary and testing. Original works belong to their authors and rights holders. No official art is included. The prompts and generated SVGs are released under the same CC BY 4.0 content license as the rest of the project; see [../LICENSE-CONTENT](../LICENSE-CONTENT).
