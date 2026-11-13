# Pilot 01 — `v0.1-pilot`

Date: 2026-11-13  
Repo: https://github.com/qianhanglv/xenodesign  
Gallery: https://qianhanglv.github.io/xenodesign/

## What this release is

The first visual pilot of XenoDesign: two models, three constraint cards, and a
single creature carried through portrait → six views → section → skeleton +
topological pelt → motion.

- **Models:** ChatGPT (web; version not captured) and DeepSeek v4.1 Flash.
- **Cards:** D1 (6 constraints), D2 (13), D3 (20).
- **Outputs:** 56 SVGs — L0 6, L1 36, L2 4, L3 8, L4 2.
- **Notes:** card-level and level-level design notes, including hidden-feature,
  `RECONCILE`, and `CONFLICT` lines.
- **Standard:** `spec/` contains the main standard, authoring guide, prompt
  library, and L0 template.

## Read the standard

- [Spec index](https://github.com/qianhanglv/xenodesign/blob/main/spec/README.md) — links to the main standard, authoring guide, prompt library, and L0 template.
- **Offline:** attach `xenodesign-spec-v0.1-pilot.zip` to this release. It contains the four documents with ASCII filenames, plus a short `README.txt`.

## What it is not

- **Not a ranking.** n = 1 per model/card; no repeats, no seeds.
- **Not a complete run.** D2 has no L4; D3 has only L0/L1.
- **Not a formal score.** K1–K8 / M1–M7 are not filled yet.
- **Not a claim about intelligence.** It is a visual smoke test for
  composition, spatial consistency, and instruction following.

## How to reproduce

1. Open `cards/experiment-prompts.md` and pick a card.
2. Paste the card into a model; save the SVGs under
   `submissions/<model>/<card>/<level>/`.
3. Save the design note next to the card or level.
4. Run `python3 build_gallery.py` and open `index.html`.
5. Or open the hosted gallery: https://qianhanglv.github.io/xenodesign/

## Known issues

- ChatGPT web model version was not recorded.
- Note file names are inconsistent (`DESIGN_NOTES.md`, `README_设计说明.txt`,
  `design-notes.md`, `L0.md`, `design_note.txt`).
- D2 has no L4; D3 has no L2/L3/L4.
- L4 is a real loop but not verified as a full run/jump; ChatGPT D1 has only
  two animation tracks, while its note claims more.

## Next

- Fill K1–K8 and M1–M7 for the existing artifacts.
- Run 3 seeds per model/card; show all, not best-of.
- Add a blind human check on the L0 images.
- Capture model versions.
- Complete the missing L4 / L2–L4 combinations.
- Invite new model submissions via `CONTRIBUTING.md`.

## Suggested GitHub Release fields

- **Tag:** `v0.1-pilot`
- **Title:** `Pilot 01 — 2 models, 3 cards, 56 SVGs`
- **Description:** paste the sections above, plus the gallery link.
- **Assets:** GitHub automatically attaches the source ZIP. Optionally attach:
  - `xenodesign-spec-v0.1-pilot.zip` — the four spec documents, offline (47 KB)
  - `assets/pelt-comparison.png` (the visual hook)
  - a PDF of `reports/pilot-01.md` (if you export one)
  - a ZIP of `assets/` (optional; not required)
- **Do not attach:** every SVG individually, `.DS_Store`, API keys, or chat logs.

## One-line release summary

> Pilot 01: 2 models × 3 cards, 56 SVGs, from portrait to topological pelt to
> motion. A gallery and a pipeline test — not a leaderboard.
