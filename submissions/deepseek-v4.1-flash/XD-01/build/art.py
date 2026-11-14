"""Two illustration-grade PNGs of the L0 creature.

  * creature-illuminated.png  - polychrome bestiary miniature (parchment, gilt)
  * creature-woodcut.png      - woodcut / engraving plate (hatched ink on paper)

Rasterised with Pillow straight from the same 3D geometry as the SVG set, so the
anatomy is identical to L0.
"""
import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops

import model as M
import creature as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'L0', 'art')
W = 1400
SS = 2
CW = CH = W * SS


# ------------------------------------------------------------------ helpers
def prepare(faces, cam):
    rows = []
    for f in faces:
        n = M._normal(f['p'])
        if M.vdot(n, cam.d) > 0.02:
            continue
        rows.append((M.vdot(M._centroid(f['p']), cam.d), n, f))
    rows.sort(key=lambda t: -t[0])
    return rows


def scr(cam, p):
    x, y, _ = cam.proj(p)
    return (x, y)


KEY = M.vnorm((-0.56, 0.56, 0.61))     # upper-left, on the camera side
FILL = M.vnorm((0.78, 0.14, 0.28))     # warm bounce from the right


def bore_bounce(p, n):
    """light rising through the throat: 1 on surfaces that face the bore axis"""
    r = M.vlen(p)
    if r < 1e-6:
        return 0.0
    d = M.vmul(p, -1.0 / r)
    return max(0.0, M.vdot(n, d)) * max(0.0, 1.0 - (r - 78.0) / 60.0)


def lam(n, p=None):
    """lighting term, 0..1.5, independent of albedo (for engraving tone)."""
    k = max(0.0, M.vdot(n, KEY))
    f = max(0.0, M.vdot(n, FILL))
    up = max(0.0, n[1])
    und = max(0.0, -n[1])
    t = 0.20 + 1.00 * k ** 1.15 + 0.22 * f + 0.09 * up + 0.24 * und ** 1.5
    if p is not None:
        t += 0.55 * bore_bounce(p, n)
    return t


COOL = (0.13, 0.27, 0.31)      # shadow colour (verdigris/slate)
WARM = (1.00, 0.86, 0.62)


def shade_paint(albedo, n, d, p=None):
    L = min(1.6, lam(n, p))
    lit = [albedo[i] * L for i in range(3)]
    # push the deep shadows toward a cold verdigris instead of dead brown
    k = max(0.0, 0.52 - L) / 0.52
    for i in range(3):
        lit[i] = lit[i] * (1 - 0.62 * k) + COOL[i] * 0.62 * k
    # fresnel gold rim
    fr = (1.0 - abs(M.vdot(n, d))) ** 2.8 * 0.55
    out = []
    for i in range(3):
        v = lit[i] + WARM[i] * fr
        out.append(min(1.0, max(0.0, v)))
    return out


def tone(n, p=None):
    """engraving tone: diffuse only, no fresnel rim (rim would punch paper
    holes just inside the silhouette)."""
    k = max(0.0, M.vdot(n, KEY))
    f = max(0.0, M.vdot(n, FILL))
    up = max(0.0, n[1])
    und = max(0.0, -n[1])
    t = 0.10 + 1.02 * k ** 1.18 + 0.22 * f + 0.10 * up + 0.20 * und ** 1.4
    if p is not None:
        t += 0.60 * bore_bounce(p, n)
    return min(1.0, max(0.0, t))


def tag_colour(tag):
    if tag.startswith('crest'):
        return (0.97, 0.74, 0.22)
    if tag.startswith('maw'):
        return (0.26, 0.09, 0.06)
    if tag in ('leg-L', 'leg-R', 'arm-L', 'arm-R'):
        return (0.62, 0.38, 0.21)
    if tag.startswith('rib'):
        return (0.90, 0.74, 0.46)
    return (0.88, 0.61, 0.31)


def mask_of(faces, cam, blur=0.0):
    mk = Image.new('L', (CW, CH), 0)
    d = ImageDraw.Draw(mk)
    for f in faces:
        d.polygon([scr(cam, p) for p in f['p']], fill=255)
    return mk.filter(ImageFilter.GaussianBlur(blur)) if blur else mk


def outline(img, mask, colour, w, alpha=255):
    grown = mask.filter(ImageFilter.GaussianBlur(w * 0.62))
    band = grown.point(lambda v: 255 if v > 30 else 0)
    band = ImageChops.subtract(band, mask.point(lambda v: 255 if v > 40 else 0))
    layer = Image.new('RGBA', img.size, colour + (alpha,))
    layer.putalpha(band)
    return Image.alpha_composite(img, layer)


def group_faces(rows):
    """split the visible faces into anatomical parts for outlining"""
    g = {'shell': [], 'crest': [], 'leg-L': [], 'leg-R': [], 'arm-L': [], 'arm-R': [],
         'maw': []}
    for depth, n, f in rows:
        t = f['t']
        if t.startswith('leg-'):
            g['leg-L' if 'L' in t else 'leg-R'].append(f)
        elif t.startswith('arm-'):
            g['arm-L' if 'L' in t else 'arm-R'].append(f)
        elif t.startswith('crest'):
            g['crest'].append(f)
        elif t.startswith('maw'):
            g['maw'].append(f)
        else:
            g['shell'].append(f)
    return g


# ------------------------------------------------------------- backgrounds
def parchment(size, warm=(0.94, 0.87, 0.72), edge=(0.70, 0.57, 0.41), seed=7):
    yy, xx = np.mgrid[0:size, 0:size] / float(size)
    r = np.sqrt((xx - 0.5) ** 2 + (yy - 0.47) ** 2) / 0.74
    base = np.array(warm, np.float32)
    ed = np.array(edge, np.float32)
    t = np.clip(r, 0, 1)[..., None] ** 1.6
    arr = base * (1 - t) + ed * t
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, (size, size)).astype(np.float32)
    n = np.array(Image.fromarray(((n * 0.5 + 0.5) * 255).astype(np.uint8))
                 .filter(ImageFilter.GaussianBlur(size / 900.0)), np.float32) / 255.0
    arr *= (0.95 + 0.10 * n[..., None])
    stains = np.zeros((size, size), np.float32)
    rng2 = np.random.default_rng(seed + 14)
    ax = np.arange(size)
    for _ in range(30):
        cx, cy = rng2.uniform(0, size, 2)
        rad = rng2.uniform(size * 0.02, size * 0.13)
        d = np.sqrt((ax[None, :] - cx) ** 2 + (ax[:, None] - cy) ** 2)
        stains += np.exp(-(d / rad) ** 2) * rng2.uniform(0.015, 0.06)
    arr *= (1 - np.clip(stains, 0, 0.20)[..., None])
    return Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), 'RGB').convert('RGBA')


def glow(img, cx, cy, r, colour, power=1.5, alpha=1.0):
    g = Image.radial_gradient('L').resize((int(r * 2), int(r * 2)), Image.BICUBIC)
    a = np.array(g, np.float32) / 255.0
    a = (1.0 - a) ** power
    lay = np.zeros((int(r * 2), int(r * 2), 4), np.uint8)
    for i in range(3):
        lay[..., i] = int(colour[i] * 255)
    lay[..., 3] = (np.clip(a, 0, 1) * 255 * alpha).astype(np.uint8)
    img.alpha_composite(Image.fromarray(lay, 'RGBA'), (int(cx - r), int(cy - r)))


def grain(img, amount=0.06, size=7):
    arr = np.array(img.convert('RGB'), np.float32) / 255.0
    rng = np.random.default_rng(size)
    n = rng.normal(0, 1, arr.shape[:2]).astype(np.float32)
    n = np.array(Image.fromarray(((n * 0.5 + 0.5) * 255).astype(np.uint8))
                 .filter(ImageFilter.GaussianBlur(1.4)), np.float32) / 255.0
    arr = arr * (1 - amount + amount * 2 * n[..., None])
    return Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), 'RGB').convert('RGBA')


# ------------------------------------------------------------------ painter
def draw_painted(img, rows, cam):
    dr = ImageDraw.Draw(img)
    for depth, n, f in rows:
        nn = n if M.vdot(n, cam.d) > 0 else M.vmul(n, -1)
        col = tag_colour(f['t'])
        if f['t'].startswith('maw'):
            base = f['c']
            col = (0.86, 0.78, 0.64) if (base[0] + base[1] + base[2]) > 0.9 else (0.16, 0.07, 0.05)
        c = shade_paint(col, nn, cam.d, M._centroid(f['p']))
        rgb = (int(c[0] * 255), int(c[1] * 255), int(c[2] * 255))
        pts = [scr(cam, p) for p in f['p']]
        dr.polygon(pts, fill=rgb)
        dr.line(pts + [pts[0]], fill=rgb, width=SS + 1, joint='curve')
    return img


def render_illuminated(path):
    m = C.build()
    cam = M.fit_cam(m.faces, M.vnorm((0.44, -0.15, -0.88)), (0, 1, 0),
                    margin=120 * SS / 2.0, canvas=CW)
    rows = prepare(m.faces, cam)
    g = group_faces(rows)

    bg = parchment(CW)
    # roundel behind the creature
    rr = CW * 0.40
    cx, cy = CW * 0.50, CW * 0.47
    glow(bg, cx, cy, rr * 1.5, (1.0, 0.80, 0.38), 2.0, 0.55)
    glow(bg, cx, CW * 0.86, CW * 0.42, (1.0, 0.44, 0.10), 1.7, 0.40)

    # a faint sunburst behind the arch (illuminated-manuscript device)
    rays = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    dr_ = ImageDraw.Draw(rays)
    import random
    random.seed(4)
    for i in range(34):
        a0 = 2 * math.pi * i / 34 + random.uniform(-0.02, 0.02)
        wdt = 0.030 + random.uniform(0.0, 0.012)
        r0, r1 = CW * 0.30, CW * 0.56
        p1 = (cx + math.cos(a0) * r0, cy + math.sin(a0) * r0)
        p2 = (cx + math.cos(a0 - wdt) * r1, cy + math.sin(a0 - wdt) * r1)
        p3 = (cx + math.cos(a0 + wdt) * r1, cy + math.sin(a0 + wdt) * r1)
        dr_.polygon([p1, p2, p3], fill=(214, 158, 52, 44))
    bg = Image.alpha_composite(bg, rays.filter(ImageFilter.GaussianBlur(SS * 1.2)))
    # ember inside the bore
    glow(bg, CW * 0.505, CW * 0.455, CW * 0.20, (1.0, 0.52, 0.14), 1.5, 0.75)
    # ground shadow
    glow(bg, CW * 0.50, CW * 0.80, CW * 0.42, (0.10, 0.06, 0.04), 1.6, 0.85)

    draw_painted(bg, rows, cam)
    # soften the facets a touch so it reads as paint, not polygons
    soft = bg.filter(ImageFilter.GaussianBlur(SS * 1.6))
    body0 = Image.new('L', (CW, CH), 0)
    db0 = ImageDraw.Draw(body0)
    for depth, n, f in rows:
        db0.polygon([scr(cam, p) for p in f['p']], fill=255)
    bg = Image.composite(Image.blend(bg, soft, 0.55), bg, body0)

    # atmosphere: cool above, ember below (very light hand)
    atm = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    da = ImageDraw.Draw(atm)
    steps = 120
    for i in range(steps):
        t = i / float(steps - 1)
        y0 = int(CW * (0.10 + 0.90 * t))
        y1 = int(CW * (0.10 + 0.90 * (i + 1) / float(steps - 1))) + 1
        col = (int(255 * (0.30 + 0.45 * t)), int(80 * (0.25 + 0.55 * t)),
               int(30 * (0.25 + 0.30 * t)), 7)
        da.rectangle([0, y0, CW, y1], fill=col)
    body = Image.new('L', (CW, CH), 0)
    db = ImageDraw.Draw(body)
    for depth, n, f in rows:
        db.polygon([scr(cam, p) for p in f['p']], fill=255)
    atm.putalpha(ImageChops.multiply(atm.split()[3], body))
    bg = Image.alpha_composite(bg, atm)

    # ink: one clean outline per part
    for key, col in (('shell', (56, 32, 18)), ('maw', (40, 18, 12)),
                     ('leg-L', (56, 32, 18)), ('leg-R', (56, 32, 18)),
                     ('arm-L', (56, 32, 18)), ('arm-R', (56, 32, 18)),
                     ('crest', (74, 42, 12))):
        if not g[key]:
            continue
        mk = mask_of(g[key], cam)
        bg = outline(bg, mk, col, int(2.6 * SS), 235)

    # gilt on the crystal crest
    mk = mask_of(g['crest'], cam)
    lay = Image.new('RGBA', bg.size, (255, 196, 84, 255))
    a = mk.filter(ImageFilter.GaussianBlur(SS * 2)).point(lambda v: int(v * 0.55))
    lay.putalpha(a)
    bg = Image.alpha_composite(bg, lay)
    mk2 = mk.filter(ImageFilter.GaussianBlur(SS * 9))
    lay2 = Image.new('RGBA', bg.size, (255, 170, 60, 255))
    lay2.putalpha(mk2.point(lambda v: int(v * 0.30)))
    bg = Image.alpha_composite(bg, lay2)

    bg = grain(bg, 0.045, 11)
    # soft bloom so the gold and the ember read as light, not paint
    arr = np.array(bg.convert('RGB'), np.float32) / 255.0
    mbody = np.array(body0.filter(ImageFilter.GaussianBlur(SS * 3)), np.float32) / 255.0
    hi = np.clip((arr - 0.72) * 3.0, 0, 1) * mbody[..., None]
    blur = np.array(Image.fromarray((hi * 255).astype(np.uint8))
                    .filter(ImageFilter.GaussianBlur(SS * 6)), np.float32) / 255.0
    arr = 1 - (1 - arr) * (1 - blur * 0.55)
    bg = Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), 'RGB').convert('RGBA')

    # embers
    rng = np.random.default_rng(5)
    em = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    de = ImageDraw.Draw(em)
    for _ in range(70):
        x, y = rng.uniform(CW * 0.06, CW * 0.94), rng.uniform(CW * 0.18, CW * 0.94)
        r = rng.uniform(CW * 0.0018, CW * 0.005)
        de.ellipse([x - r, y - r, x + r, y + r],
                   fill=(255, int(rng.uniform(150, 225)), int(rng.uniform(70, 150)),
                         int(rng.uniform(50, 170))))
    bg = Image.alpha_composite(bg, em.filter(ImageFilter.GaussianBlur(SS * 0.8)))

    bg = frame_illuminated(bg, int(CW * 0.034), int(10 * SS))

    out = bg.convert('RGB').resize((W, W), Image.LANCZOS)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.1, percent=45, threshold=2))
    out.save(path, 'PNG')
    return out


def frame_illuminated(img, inset, thickness):
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    dr = ImageDraw.Draw(lay)
    w, h = img.size
    gold = (198, 150, 58)
    dark = (58, 36, 18)
    gold_d = (120, 84, 26)
    for k in range(thickness):
        t = k / float(max(thickness - 1, 1))
        shade = 0.74 + 0.30 * math.sin(t * math.pi)
        col = (int(gold[0] * shade), int(gold[1] * shade), int(gold[2] * shade), 255)
        dr.rectangle([inset + k, inset + k, w - inset - k, h - inset - k], outline=col)
    for off in (-7, thickness + 3):
        dr.rectangle([inset + off, inset + off, w - inset - off, h - inset - off],
                     outline=dark, width=int(2.6 * SS))
    dr.rectangle([inset + thickness + 9, inset + thickness + 9,
                  w - inset - thickness - 9, h - inset - thickness - 9],
                 outline=gold_d, width=int(1.2 * SS))
    for cx, cy, sx, sy in ((inset, inset, 1, 1), (w - inset, inset, -1, 1),
                           (inset, h - inset, 1, -1), (w - inset, h - inset, -1, -1)):
        r = 30 * SS
        for k in range(3):
            rr = r * (1 - k * 0.28)
            dr.arc([cx + sx * 5 - rr, cy + sy * 5 - rr, cx + sx * 5 + rr, cy + sy * 5 + rr],
                   0, 360, fill=dark, width=int(2.6 * SS))
        dr.ellipse([cx - 8 * SS, cy - 8 * SS, cx + 8 * SS, cy + 8 * SS],
                   fill=gold, outline=dark, width=int(2.2 * SS))
    return Image.alpha_composite(img, lay)


# ------------------------------------------------------------------ woodcut
def hatch_lines(size, angle_deg, spacing, jitter=0.0, seed=0):
    ang = math.radians(angle_deg)
    ca, sa = math.cos(ang), math.sin(ang)
    diag = int(size * 1.6)
    rng = np.random.default_rng(seed)
    out = []
    c = -diag
    while c < diag:
        jc = c + (rng.uniform(-jitter, jitter) if jitter else 0.0)
        px, py = ca * jc, sa * jc
        out.append(((px - sa * diag, py + ca * diag), (px + sa * diag, py - ca * diag)))
        c += spacing
    return out


def render_woodcut(path):
    m = C.build()
    cam = M.fit_cam(m.faces, M.vnorm((0.44, -0.15, -0.88)), (0, 1, 0),
                    margin=120 * SS / 2.0, canvas=CW)
    rows = prepare(m.faces, cam)
    g = group_faces(rows)

    paper = parchment(CW, warm=(0.955, 0.925, 0.845), edge=(0.80, 0.74, 0.62), seed=31)

    # tone -> hatch level 0..5, normalised over the visible faces
    ts = []
    for depth, n, f in rows:
        nn = n if M.vdot(n, cam.d) > 0 else M.vmul(n, -1)
        ts.append(tone(nn, M._centroid(f['p'])))
    ts_arr = np.array(ts, np.float32)
    lo, hi = np.percentile(ts_arr, 4), np.percentile(ts_arr, 98)
    lev = []
    for t in ts:
        u = min(1.0, max(0.0, (t - lo) / max(hi - lo, 1e-6)))
        lv = int((1.0 - u) * 5.0 + 0.4)
        if u > 0.90:
            lv = 0
        lev.append(min(5, max(0, lv)))

    NB = 5
    masks = {}
    for lv in range(NB + 1):
        mk = Image.new('L', (CW, CH), 0)
        d = ImageDraw.Draw(mk)
        for i, (depth, n, f) in enumerate(rows):
            if lev[i] == lv:
                d.polygon([scr(cam, p) for p in f['p']], fill=255)
        masks[lv] = mk.filter(ImageFilter.GaussianBlur(0.7))

    ink = Image.new('L', (CW, CH), 0)
    ladder = {
        1: [(41, 17, 1.7)],
        2: [(41, 11, 2.6)],
        3: [(41, 8, 3.2), (131, 26, 1.5)],
        4: [(41, 7, 3.6), (131, 11, 3.0)],
    }
    for lv, pats in ladder.items():
        m2 = Image.new('L', (CW, CH), 0)
        d2 = ImageDraw.Draw(m2)
        for (ang, sp, lw) in pats:
            for a, b in hatch_lines(CW, ang, sp * SS, jitter=sp * SS * 0.22, seed=lv * 7 + ang):
                d2.line([a, b], fill=255, width=int(lw * SS * 1.05))
        ink = ImageChops.lighter(ink, ImageChops.multiply(m2, masks[lv]))
    ink = ImageChops.lighter(ink, masks[NB])

    paper.paste((44, 34, 26), (0, 0), ink)

    # contours: one clean line around each part
    for key in ('shell', 'maw', 'leg-L', 'leg-R', 'arm-L', 'arm-R', 'crest'):
        if not g[key]:
            continue
        mk = mask_of(g[key], cam)
        paper = outline(paper, mk, (34, 26, 19), int(3.0 * SS), 255)

    # hatched ground
    gm = Image.new('L', (CW, CH), 0)
    dg = ImageDraw.Draw(gm)
    dg.ellipse([CW * 0.13, CW * 0.755, CW * 0.87, CW * 0.845], fill=255)
    gm = gm.filter(ImageFilter.GaussianBlur(SS * 16)).point(lambda v: int(v * 0.85))
    gi = Image.new('L', (CW, CH), 0)
    d2 = ImageDraw.Draw(gi)
    for a, b in hatch_lines(CW, 5, 7 * SS, jitter=2 * SS, seed=99):
        d2.line([a, b], fill=255, width=int(1.5 * SS))
    paper.paste((36, 28, 20), (0, 0), ImageChops.multiply(gi, gm))

    paper = grain(paper, 0.05, 41)
    paper = frame_woodcut(paper, int(CW * 0.030))

    out = paper.convert('RGB').resize((W, W), Image.LANCZOS)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.0, percent=65, threshold=2))
    out.save(path, 'PNG')
    return out


def frame_woodcut(img, inset):
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    dr = ImageDraw.Draw(lay)
    w, h = img.size
    ink = (28, 22, 16, 255)
    dr.rectangle([inset, inset, w - inset, h - inset], outline=ink, width=int(3.4 * SS))
    dr.rectangle([inset + int(7 * SS), inset + int(7 * SS), w - inset - int(7 * SS),
                  h - inset - int(7 * SS)], outline=ink, width=int(1.5 * SS))
    # corner ticks
    L = int(26 * SS)
    for cx, cy, sx, sy in ((inset, inset, 1, 1), (w - inset, inset, -1, 1),
                           (inset, h - inset, 1, -1), (w - inset, h - inset, -1, -1)):
        dr.line([(cx + sx * 4, cy + sy * L), (cx + sx * 4, cy + sy * 4)],
                fill=ink, width=int(2.4 * SS))
        dr.line([(cx + sx * L, cy + sy * 4), (cx + sx * 4, cy + sy * 4)],
                fill=ink, width=int(2.4 * SS))
    return Image.alpha_composite(img, lay)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    a = render_illuminated(os.path.join(OUT, 'creature-illuminated.png'))
    print('illuminated', a.size)
    b = render_woodcut(os.path.join(OUT, 'creature-woodcut.png'))
    print('woodcut', b.size)
