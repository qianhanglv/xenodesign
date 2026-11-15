# Pilot 02 — `v0.4-pilot`

Date: 2026-11-15  
Repo: https://github.com/qianhanglv/xenodesign  
Gallery: https://qianhanglv.github.io/xenodesign/  
Report: https://github.com/qianhanglv/xenodesign/blob/main/reports/pilot-02.md

## What this release is

`v0.4-pilot` is a **documentation + bonus-extension release**. It does not add a new model run and it does not change the 152-SVG benchmark matrix.

It ships three things:

1. the **D0–Dn / bilingual preflight** authoring guide;
2. the **L3 pelt head/neck fix** and the prompt audit behind it;
3. **five literary-creature fan designs** as an entertainment extension at the end of the project.

The benchmark remains **5 models, 3 standard cards, 1 D2 hard variant, 152 active SVGs, 11 pelts**. The bonus adds **5 fan designs, 51 SVGs, 3 oil portraits** and is **not counted** in the 152.

## What's new

### 1. D0–Dn and preflight

- Points: `5P + 10F + 5Q + 10N`; D0 < 40, D1 40–89, D2 90–139, D3 140–189, D4 190–239, D5 240–289, Dn by the same +50 pattern.
- Two requirements with no declared D default to **D0**, not D1.
- A bilingual preflight now comes **before** the formal prompt: counts/IDs, points, D, levels, conflicts, seed, next-D gap, and “do you want to upgrade?”
- Bonus is B, costs 0, and is valid at every D.
- The target model must output complete SVG/MD files in per-level folders.

### 2. L3 pelt head/neck fix

The old L3 prompt required “one continuous sheet” and holes for eyes/limbs/tail, but never said the head and neck must be part of the sheet. Models could therefore produce a **headless torso sheet** and still satisfy every explicit requirement.

The new rule:

- if the creature has a head, the head/face is a front lobe and the neck is a continuous bridge to the torso;
- do not omit the head, do not draw a separate head/mask, and do not replace the head with a hole;
- if the creature has no head by canon, write `HEAD: none by canon` (or `HEAD: none in this design` for a design decision).

The fix is in the standard, the authoring guide, the D1/D2 card prompts, the XD-01 prompt, the L3 note format, and the K5 check.

### 3. Literary bonus

A separate `literary/` section, not part of the benchmark:

- **Watcher in the Water** — *The Lord of the Rings*; 21 tentacles, body not described.
- **Runespoor** — *Harry Potter*; three heads with planner/dreamer/critic roles.
- **Feathered Serpent** — *Lord of the Mysteries*; dark scales, white feathers, pale flame.
- **Black Tai Sui** — *Dao of the Bizarre Immortal*; soft body, stink pores, no head.
- **Water Monkey** — *Dao of the Bizarre Immortal*; black hair, water-weed limbs, head/neck.

Each has `[CANON]` / `[INFERRED]` tags in its notes. The set is also the evidence for the pelt fix:

- Runespoor and Feathered Serpent were generated with the old L3 prompt; their notes literally say “headless pelt” / “eyes removed with the head”.
- Water Monkey was generated with the new L3 prompt; its pelt records `HEAD/NECK: 1 head attached; NECK: continuous bridge to torso`.
- Watcher has no head by canon; Black Tai Sui has `HEAD: none in this design`.

The literary section is deliberately **not** a ranking and **not** a model comparison. The social-media post and its publishing images are kept outside the repository.

## What it is not

- **Not a new model matrix.** The 152-SVG benchmark is unchanged.
- **Not a ranking.** n = 1 per model/card; no repeats, no human scoring.
- **Not canon.** The literary creatures are fan interpretations; `[INFERRED]` anatomy is not an original-source claim.
- **Not a clean literary set.** Runespoor and Feathered Serpent fail the new head/neck pelt rule; they are kept as evidence, not silently rerun.
- **Not a social-media pack.** `post.md` and the posting images are intentionally outside the repo.

## Counts

### Main benchmark (unchanged)

```text
models: 5
standard cards: 3
D2 hard variants: 1
active SVGs: 152
L0: 16
L1: 96
L2: 11
L3: 22
L4: 6
L5: 1
pelts: 11
```

### Literary bonus (not counted in 152)

```text
designs: 5
SVGs: 51
L0: 5
L1: 30
L2: 5
L3: 10
L4: 1
portraits: 3
```

## Known issues

- The main benchmark still has one run per model/card, no repeated seeds, and no formal K1–K8 / M1–M7 scoring.
- XD-01 is still a single-model stress test; L1 left/right lose the cavity and L2 is hard to read as a torus.
- The first L5 is still structurally distorted; the static attempt remains archived.
- Runespoor L1 drifts in head orientation; the Feathered Serpent pelt is a headless cape; both are old-prompt outputs.
- Watcher and Black Tai Sui have weak six-view differentiation because they are radially symmetric.
- The Feathered Serpent portrait is the strongest image but cannot prove the L1/L3 design.
- ChatGPT and Gemini web versions were not captured.

## How to reproduce

1. For the benchmark: `cards/experiment-prompts.md` or `cards/XD-01-donut-cavity-L5.md`; `python3 build_gallery.py`.
2. For literary bonus: `literary/prompts/three-creatures-d2.md` and `literary/prompts/black-taisui-water-monkey-d2.md`; open `literary/index.html`.
3. Main gallery: https://qianhanglv.github.io/xenodesign/
4. Literary gallery: https://qianhanglv.github.io/xenodesign/literary/

## Assets to attach

- `xenodesign-spec-v0.4-pilot.zip` — four spec documents with D0–Dn, preflight, head/neck pelt rule, offline.
- `xenodesign-v0.4-hero-main.png` — main benchmark 5×3 L0 grid.
- `xenodesign-v0.4-pelt-comparison.png` — main benchmark 11-pelt comparison.
- `xenodesign-v0.4-literary-l0-grid.png` — five literary L0 portraits.
- `xenodesign-v0.4-literary-portraits.png` — three oil portraits.
- `xenodesign-v0.4-literary-pelts.png` — five literary pelts.
- `xenodesign-v0.4-literary-pelt-verdict.png` — the three key pelts: Runespoor FAIL, Feathered Serpent FAIL, Water Monkey PASS.

Do **not** attach the social post, cover, CTA, or posting-only images; they are outside the repo. The six images above are result sheets, not the social cover.

GitHub automatically attaches the source ZIP. Do not attach every SVG individually.

## Suggested GitHub Release fields

- **Tag:** `v0.4-pilot`
- **Target:** `main`
- **Title:** `Pilot 02 — v0.4: D0–Dn guide, pelt head/neck fix, literary bonus`
- **Description:** paste the sections above.
- **Assets:** the spec ZIP.
- **Set as latest:** yes.
- **Pre-release:** optional; `0.4` is still a pilot.

## One-line release summary

> v0.4: the authoring guide gets D0–Dn and a preflight, the pelt gets a head/neck rule, and five literary creatures join at the end — not as a benchmark, but as the evidence for why the rule was needed.
