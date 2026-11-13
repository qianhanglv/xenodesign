# Experimental submissions

The reference protocol is SVG: it renders in a browser, diffs cleanly, and is
easy to check. But the point of XenoDesign is the design logic — P/F/Q/N
constraints, L0–L5 views, the topological pelt — not the file extension.

If you want to try a different medium, this folder is for you.

## What to submit

Put your experiment under:

```text
submissions/experimental/<model-slug>/<card>/<level>/
```

Include:

1. the output — PNG, JPEG, WebP, GIF, MP4, ASCII text, 3D file, etc.;
2. a preview that can be opened in a browser (PNG/JPEG/WebP/GIF/MP4);
3. `note.md` with the same constraint-to-feature mapping as the SVG protocol;
4. a one-line `medium.md` saying what you changed (e.g. "raster", "pixel art",
   "3D render", "video").

Keep each file under 10 MB. No secrets, no chat logs, no personal data.

## What is different

- The main gallery currently indexes SVG only. Experimental work is linked from
  the PR and can be added to the gallery later.
- The P/F/Q/N checks still apply; only the output format changes.
- For L5, the bicycle is still the goal: `ride.svg`, `ride.png`, or `ride.mp4`
  all count, as long as the creature is on the bicycle and the note explains
  the contact and motion.

## What is not different

- One creature per drawing (or per shot).
- Keep the counts and patterns consistent across views.
- Save the prompt and the note; without them, the experiment is not reviewable.
- Do not edit another contributor's folder.
