# Pilot 02 — `v0.2-pilot`

Date: 2026-11-14  
Repo: https://github.com/qianhanglv/xenodesign  
Gallery: https://qianhanglv.github.io/xenodesign/  
Report: https://github.com/qianhanglv/xenodesign/blob/main/reports/pilot-02.md

## What this release is

Pilot 02 adds Gemini (web), Kimi K3.1 Pro, the XD-01 donut-cavity challenge, the first L5 bicycle, and two style studies. The project now has **4 models, 3 standard cards + 1 challenge, 124 active SVGs** (the archived static L5 is extra), and **25 Q dimensions**.

## What's new

- **Gemini (web)** ran D1/D2/D3 (28 SVGs).
- **Kimi K3.1 Pro** ran D1/D2/D3 (28 SVGs).
- **XD-01**: a D2 card with a hard geometric Q — one real through-hole covering at least 1/3 of the body silhouette. Only DeepSeek has run it so far; its failures are kept and compared.
- **First L5**: now an animated 3.2 s bicycle loop; the first static attempt is archived. Still structurally distorted.
- **Q-25**: a reusable geometric-ratio Q for through-hole cavities, added to the prompt library.
- **Two style studies**: the XD-01 creature as an illuminated miniature and a woodcut.

## What it is not

- **Not a ranking.** n = 1 per model/card; no repeats, no seeds, no human scoring.
- **Not a complete matrix.** Standard D2 has no L4; D3 has only L0/L1; XD-01 has one model; Kimi's D1 note is missing.
- **Not a clean XD-01.** The L1 left/right views lose the cavity; the L2 section reads as a capsule rather than a cut torus; the 0.39 area ratio is self-reported.
- **Not a clean L5.** The ride is **structurally distorted** — the ring body is visibly twisted/skewed. The first attempt was static; the current `ride.svg` is an animated 3.2 s loop, but the geometry still twists. The bicycle is small relative to the body, so saddle/pedal/bar contact is hard to verify.

## How to reproduce

1. Open `cards/experiment-prompts.md` (D1/D2/D3) or `cards/XD-01-donut-cavity-L5.md` (challenge).
2. Paste the card into a model; save the SVGs and the design note.
3. Run `python3 build_gallery.py`; open `index.html`.
4. Or open the hosted gallery: https://qianhanglv.github.io/xenodesign/

## Known issues

- L5 is animated now (`ride.svg`, 3.2 s, 14 transform tracks), but it is still structurally distorted in the riding pose and is not a clean torus; the static first attempt is archived at `archive/XD-01-L5/ride-static.svg`.
- L5 contact points need a close-up / frame-by-frame check.
- XD-01 L1 left/right lose the through-hole; L2 section is hard to read as a ring.
- The XD-01 0.39 / 0.36 cavity ratios are self-reported, not independently measured.
- Kimi D1 has no design note.
- ChatGPT and Gemini web model versions were not captured.

## Assets to attach

- `xenodesign-spec-v0.2-pilot.zip` — four spec documents with Q-25, offline.
- `assets/pelt-comparison-pilot02.png` — nine pelts.
- `assets/xd01-failure.png` — the L0/L1/L2/L3 failure comparison.
- `assets/xd01-art.png` — illuminated / woodcut style studies.
- `assets/xd01-l5.png` — the animated L5, first frame (still distorted).

GitHub automatically attaches the source ZIP. Do not attach every SVG individually.

## Suggested GitHub Release fields

- **Tag:** `v0.2-pilot`
- **Target:** `main`
- **Title:** `Pilot 02 — Gemini, Kimi, the donut cavity, and the first L5`
- **Description:** paste the sections above.
- **Assets:** the five files listed above.
- **Set as latest:** yes.
- **Pre-release:** optional; `0.2` is already a pilot.

## One-line release summary

> Pilot 02: Gemini and Kimi join, the donut cavity breaks, and the first alien rides a bicycle — twisted, finally animated, and still worth it.
