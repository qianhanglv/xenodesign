#!/usr/bin/env python3
"""Build a static gallery for XenoDesign Pilot 01.

No dependencies. Run: python3 build_gallery.py
"""
from pathlib import Path
from urllib.parse import quote
import html

ROOT = Path(__file__).resolve().parent
SUB = ROOT / "submissions"

MODELS = [
    ("chatgpt-web", "ChatGPT (web)"),
    ("deepseek-v4.1-flash", "DeepSeek v4.1 Flash"),
]
CARDS = [
    ("D1", "6 constraints", "L0–L4", "300-word note cap"),
    ("D2", "13 constraints", "L0–L3", "600-word note cap"),
    ("D3", "20 constraints", "L0–L1", "900-word note cap"),
]
LEVELS = [
    ("L0", "portrait"),
    ("L1", "six views"),
    ("L2", "section"),
    ("L3", "skeleton + pelt"),
    ("L4", "motion"),
]
VIEW_ORDER = ["front", "back", "left", "right", "top", "bottom"]
CARD_NOTES = ["DESIGN_NOTES.md", "README_设计说明.txt", "design-notes.md", "xenodesign.md"]
LEVEL_NOTES = ["design_note.txt", "note.md"]


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def url(p: Path) -> str:
    return quote(rel(p), safe="/")


def note_for_card(model_dir: Path, card: str) -> Path | None:
    for name in CARD_NOTES:
        p = model_dir / card / name
        if p.exists():
            return p
    return None


def note_for_level(model_dir: Path, card: str, level: str) -> Path | None:
    for name in LEVEL_NOTES:
        p = model_dir / card / level / name
        if p.exists():
            return p
    p = model_dir / card / f"{level}.md"
    if p.exists():
        return p
    return None


def files_for(model_dir: Path, card: str, level: str) -> list[Path]:
    d = model_dir / card / level
    if not d.exists():
        return []
    files = list(d.glob("*.svg"))
    if level == "L1":
        order = {v: i for i, v in enumerate(VIEW_ORDER)}
        files.sort(key=lambda p: (order.get(p.stem, 99), p.name))
    elif level == "L3":
        order = {"skeleton": 0, "pelt": 1}
        files.sort(key=lambda p: (order.get(p.stem, 99), p.name))
    elif level == "L4":
        order = {"motion": 0}
        files.sort(key=lambda p: (order.get(p.stem, 99), p.name))
    else:
        files.sort(key=lambda p: p.name)
    return files


def figure(src: Path, caption: str) -> str:
    return (
        f'<figure class="fig">'
        f'<a href="{url(src)}"><img loading="lazy" src="{url(src)}" alt="{html.escape(caption)}"></a>'
        f'<figcaption>{html.escape(caption)}</figcaption>'
        f'</figure>'
    )


def build() -> str:
    parts: list[str] = []
    parts.append(
        """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>XenoDesign — Pilot 01</title>
<style>
:root{
  --bg:#0b0e13; --panel:#11161e; --panel2:#0d1218; --line:#26303c;
  --text:#e9eef5; --muted:#9aa7b6; --accent:#7fd6c2; --warn:#e7b36a;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);
  font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1320px;margin:0 auto;padding:0 20px}
header.hero{padding:42px 0 28px;border-bottom:1px solid var(--line)}
.kicker{color:var(--accent);font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 10px}
h1{font-size:clamp(30px,4.6vw,54px);line-height:1.05;margin:0 0 12px;letter-spacing:-.02em}
.sub{color:var(--muted);font-size:18px;max-width:820px;margin:0 0 18px}
.badges{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}
.badge{border:1px solid var(--line);border-radius:999px;padding:5px 10px;font-size:12px;color:var(--muted)}
.hero-grid{width:100%;border-radius:14px;border:1px solid var(--line);background:#05070a}
.caveat{color:var(--warn);font-size:13px;margin:12px 0 0}
nav{display:flex;flex-wrap:wrap;gap:14px;padding:16px 0;border-bottom:1px solid var(--line);font-size:14px}
main{padding:26px 0 50px}
section.card{margin:0 0 44px}
.card-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px;margin:0 0 8px}
.card-head h2{font-size:26px;margin:0}
.card-head .meta{color:var(--muted);font-size:14px}
.note{font-size:13px;border:1px solid var(--line);border-radius:8px;padding:4px 8px}
.models{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.model{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px}
.model h3{margin:0 0 10px;font-size:18px}
.level{border-top:1px solid var(--line);padding:14px 0 4px}
.level:first-of-type{border-top:0}
.level-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 10px}
.level-head h4{margin:0;font-size:14px;letter-spacing:.02em}
.level-head .kind{color:var(--muted);font-size:12px}
.figs{display:grid;grid-template-columns:1fr;gap:10px}
.figs.thumbs{grid-template-columns:repeat(3,1fr)}
.figs.pair{grid-template-columns:1fr 1fr}
.fig{margin:0}
.fig img{width:100%;display:block;background:#05070a;border:1px solid var(--line);border-radius:10px}
.fig figcaption{font-size:12px;color:var(--muted);margin-top:4px}
.missing{color:var(--muted);font-size:13px;font-style:italic;margin:4px 0}
footer{border-top:1px solid var(--line);padding:22px 0 40px;color:var(--muted);font-size:13px}
footer p{max-width:900px}
@media (max-width:860px){
  .models{grid-template-columns:1fr}
  .figs.thumbs{grid-template-columns:repeat(2,1fr)}
  .figs.pair{grid-template-columns:1fr}
}
</style>
</head>
<body>
<header class="hero"><div class="wrap">
  <p class="kicker">XenoDesign · Pilot 01</p>
  <h1>Can an AI design a coherent alien?</h1>
  <p class="sub">Two models. Three constraint cards. Up to five view levels. Same SVG rules, same prompts — a visual pilot, not a leaderboard.</p>
  <div class="badges">
    <span class="badge">n = 1 per model/card</span>
    <span class="badge">no repeats</span>
    <span class="badge">no human scoring yet</span>
    <span class="badge">ChatGPT version not captured</span>
  </div>
  <img class="hero-grid" src="assets/hero-l0-grid.png" alt="Six L0 alien creatures, ChatGPT and DeepSeek, D1/D2/D3">
  <p class="caveat">Pilot only: one run per model per card. The notes are included; the checks are not yet formalized into a scorecard.</p>
</div></header>
<nav><div class="wrap">
  <a href="#D1">D1</a><a href="#D2">D2</a><a href="#D3">D3</a>
  <a href="assets/pelt-comparison.png">Pelt comparison</a>
  <a href="assets/l1-grid.png">L1 six views</a>
  <a href="reports/pilot-01.md">Pilot report</a>
  <a href="cards/experiment-prompts.md">Prompts</a>
  <a href="spec/README.md">Spec</a>
  <a href="CONTRIBUTING.md">Contribute</a>
  <a href="README.md">README</a>
</div></nav>
<main><div class="wrap">"""
    )

    for card, count, levels, cap in CARDS:
        parts.append(f'<section class="card" id="{card}">')
        parts.append('<div class="card-head">')
        parts.append(f'<h2>{card}</h2>')
        parts.append(f'<span class="meta">{html.escape(count)} · {html.escape(levels)} · {html.escape(cap)}</span>')
        # card-level notes, one per model (show both links if present)
        card_notes = []
        for mid, name in MODELS:
            n = note_for_card(SUB / mid, card)
            if n:
                card_notes.append(f'<a class="note" href="{url(n)}">{html.escape(name)} note</a>')
        if card_notes:
            parts.append(" ".join(card_notes))
        parts.append("</div>")

        parts.append('<div class="models">')
        for mid, name in MODELS:
            model_dir = SUB / mid
            parts.append('<article class="model">')
            parts.append(f'<h3>{html.escape(name)}</h3>')
            for level, kind in LEVELS:
                files = files_for(model_dir, card, level)
                level_note = note_for_level(model_dir, card, level)
                parts.append('<div class="level">')
                parts.append('<div class="level-head">')
                parts.append(f'<h4>{level}</h4><span class="kind">{html.escape(kind)}</span>')
                if level_note:
                    parts.append(f'<a class="note" href="{url(level_note)}">note</a>')
                parts.append("</div>")
                if not files:
                    parts.append('<p class="missing">not run</p>')
                else:
                    if level == "L1":
                        parts.append('<div class="figs thumbs">')
                        for f in files:
                            parts.append(figure(f, f.stem))
                        parts.append("</div>")
                    elif level == "L3":
                        parts.append('<div class="figs pair">')
                        for f in files:
                            parts.append(figure(f, f.stem))
                        parts.append("</div>")
                    else:
                        parts.append('<div class="figs">')
                        for f in files:
                            caption = f.stem
                            if level == "L4":
                                caption += " · animated SVG"
                            parts.append(figure(f, caption))
                        parts.append("</div>")
                parts.append("</div>")
            parts.append("</article>")
        parts.append("</div></section>")

    parts.append(
        """</div></main>
<footer><div class="wrap">
  <p><strong>What this is:</strong> a first visual pilot of the XenoDesign prompts — a single alien creature carried through portrait, six views, section, skeleton, topological pelt, and motion. <strong>What this is not:</strong> a ranking. One sample per model per card, different cards for different difficulties, no repeated seeds, and no formal K1–K8 / M1–M7 review yet.</p>
  <p>Pelt comparison: <a href="assets/pelt-comparison.png">assets/pelt-comparison.png</a> · Six views: <a href="assets/l1-grid.png">assets/l1-grid.png</a> · Sections and skeletons: <a href="assets/section-skeleton-grid.png">assets/section-skeleton-grid.png</a> · Motion: <a href="assets/motion-grid.png">assets/motion-grid.png</a></p>
  <p>Generated by <code>build_gallery.py</code>. No external assets, no JavaScript, no tracking.</p>
</div></footer>
</body></html>"""
    )
    return "\n".join(parts)


if __name__ == "__main__":
    html_text = build()
    (ROOT / "index.html").write_text(html_text, encoding="utf-8")
    print(f"wrote {ROOT/'index.html'} ({len(html_text)} chars)")
