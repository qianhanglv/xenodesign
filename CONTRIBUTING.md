# Contributing to XenoDesign

This is a pilot. The most useful contribution right now is **another model run**,
not another rule.

## Add a model run

1. Create `submissions/<model-slug>/<card>/<level>/`.
   Example: `submissions/acme-model/D2/L0/creature.svg`.
2. Put the SVG(s) in that folder using the standard names:
   - L0: `creature.svg`
   - L1: `front.svg`, `back.svg`, `left.svg`, `right.svg`, `top.svg`, `bottom.svg`
   - L2: `section.svg`
   - L3: `skeleton.svg`, `pelt.svg`
   - L4: `motion.svg` (or `frame01.svg` … `frame12.svg`)
3. Put the design note next to the card or level:
   - card-level: `submissions/<model>/<card>/note.md`
   - level-level: `submissions/<model>/<card>/<level>/note.md`
4. Run `python3 build_gallery.py` and check `index.html`.
5. Open a pull request with: model name, version, card, levels, date, and any
   deviation from the prompt.

## Rules

- One model per folder; do not edit other people's outputs.
- No API keys, personal data, or chat logs.
- SVGs must be under 512 KB, with `viewBox="0 0 512 512"`, no `<text>`, no
  `<image>`, no `<script>`, and no external URLs.
- Use the prompts in `cards/experiment-prompts.md` unchanged. If you had to
  deviate, say so in the note and the PR.
- Do not submit a 4-frame storyboard as L4. L4 needs `motion.svg` or 8–12 frames
  with a stated fallback.
- Keep the design note within the difficulty cap: D1 300, D2 600, D3 900 words.

## Add a new vocabulary item

The prompt library in `spec/提示词素材库.md` is a menu, not a closed list.

1. Add the item at the end of the relevant table; **do not renumber** existing
   IDs.
2. Classify it as P (global parameter), F (free goal), Q (exact count /
   prohibition), or N (body-plan rule).
3. Write the English prompt phrase, the visual evidence a reviewer should look
   for, the minimum level where it is visible, and conflicts/mutual-exclusion
   notes.
4. If it is a new Q dimension, give it a new `Q-xx` ID and at least three
   variant examples (`no X`, `exactly N`, `no more than N`, etc.).
5. Test it with the authoring guide: turn it into a card, check that the
   difficulty and note cap are right, and run at least one model.
6. Open a PR with the new item and one example card.

## Add an experimental medium

The reference format is SVG, but the design logic is the point.

1. Put the work under `submissions/experimental/<model>/<card>/<level>/`.
2. Include the output, a browser-openable preview, `note.md`, and a one-line
   `medium.md` saying what changed.
3. Keep each file under 10 MB.
4. Say in the PR that it is experimental; the main gallery currently indexes
   SVG only.

For L5, the bicycle is still the target: `ride.svg`, `ride.png`, or `ride.mp4`
all count if the creature is on the bicycle and the note explains contact and
motion.

## Reporting a problem

Open an issue with the model, card, level, file, and what looks wrong. A broken
SVG or a note that does not match the drawing is a valid bug report.
