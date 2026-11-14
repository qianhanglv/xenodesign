# Pilot 02 — `v0.3-pilot`

Date: 2026-11-14  
Repo: https://github.com/qianhanglv/xenodesign  
Gallery: https://qianhanglv.github.io/xenodesign/  
Report: https://github.com/qianhanglv/xenodesign/blob/main/reports/pilot-02.md

## What this release is

`v0.3-pilot` is the **five-model snapshot** of the living Pilot 02 gallery. It adds **GPT 6.0 Sol** and reorders the model columns:

1. DeepSeek v4.1 Flash
2. GPT 6.0 Sol
3. Kimi K3.1 Pro
4. Gemini (web)
5. ChatGPT (web, free) — the original free web run, moved last

The project now has **5 models, 3 standard cards + 1 challenge, 152 active SVGs, 11 pelts**, and **25 Q dimensions**. The first L5 is animated and still structurally distorted; the static first attempt is archived.

## What's new

- **GPT 6.0 Sol** ran D1/D2/D3 (28 SVGs), with `DESIGN_NOTES.md` for all three cards.
- **Gallery order**: DeepSeek first, GPT 6.0 Sol second, then Kimi, Gemini, and the original free ChatGPT web version last.
- **New comparison assets**: 5×3 L0 grid, 11-pelt comparison, 5×6 L1 six-view grid, GPT Sol L0 grid.
- **v0.2 remains the 4-model snapshot**; this release is the clean five-model version.

## What it is not

- **Not a ranking.** n = 1 per model/card; no repeats, no seeds, no human scoring.
- **Not a complete matrix.** Standard D2 has no L4; D3 has only L0/L1; XD-01 has one model; GPT Sol D3 has only L0/L1; Kimi's D1 note is missing.
- **Not a clean XD-01.** The L1 left/right views lose the cavity; the L2 section reads as a capsule rather than a cut torus; the 0.39 area ratio is self-reported.
- **Not a clean L5.** The ride is structurally distorted — the ring body is visibly twisted/skewed. The current `ride.svg` is an animated 3.2 s loop, but the geometry still twists; contact is hard to verify.
- **Not a claim about intelligence.** It is a visual smoke test for composition, spatial consistency, and instruction following.

## How to reproduce

1. Open `cards/experiment-prompts.md` (D1/D2/D3) or `cards/XD-01-donut-cavity-L5.md` (challenge).
2. Paste the card into a model; save the SVGs and the design note.
3. Run `python3 build_gallery.py`; open `index.html`.
4. Or open the hosted gallery: https://qianhanglv.github.io/xenodesign/

## Known issues

- GPT 6.0 Sol D3 has only L0/L1; D1 is extremely simple and uses two walking limbs (allowed by “≤4”, but easy to misread).
- Kimi D1 has no design note.
- XD-01 has only one model (DeepSeek).
- L5 is animated now but still structurally distorted; the static first attempt is archived at `archive/XD-01-L5/ride-static.svg`.
- XD-01 L1 left/right lose the through-hole; L2 section is hard to read as a ring.
- The XD-01 0.39 / 0.36 cavity ratios are self-reported, not independently measured.
- ChatGPT and Gemini web model versions were not captured.

## Assets to attach

- `xenodesign-spec-v0.3-pilot.zip` — four spec documents with Q-25, offline.
- `assets/hero-l0-pilot02.png` — 5×3 L0 grid (15 portraits).
- `assets/pelt-comparison-pilot02.png` — 11 pelts.
- `assets/l1-pilot02.png` — 5×6 L1 six-view grid.
- `assets/gpt-sol-l0-grid.png` — GPT 6.0 Sol L0.
- `assets/xd01-failure.png` — the L0/L1/L2/L3 failure comparison.
- `assets/xd01-art.png` — illuminated / woodcut style studies.
- `assets/xd01-l5.png` + `submissions/deepseek-v4.1-flash/XD-01/L5/ride.svg` — the animated L5.

GitHub automatically attaches the source ZIP. Do not attach every SVG individually.

## Suggested GitHub Release fields

- **Tag:** `v0.3-pilot`
- **Target:** `main`
- **Title:** `Pilot 02 — v0.3: GPT 6.0 Sol joins the five-model comparison`
- **Description:** paste the sections above.
- **Assets:** the files listed above.
- **Set as latest:** yes.
- **Pre-release:** optional; `0.3` is still a pilot.

## One-line release summary

> v0.3: GPT 6.0 Sol joins; five models, 152 SVGs, eleven pelts — and the donut cavity still breaks.
