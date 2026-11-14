"""Shared presentation helpers for the X-DONUT-001 deliverable set."""
import math
import model as M
import creature as C

ROOT = __file__.rsplit('/build/', 1)[0]

# ------------------------------------------------------------------ backdrop
DEFS = """
<radialGradient id="cave" cx="50%" cy="44%" r="76%">
  <stop offset="0" stop-color="#2a1d16"/>
  <stop offset="0.55" stop-color="#160f0c"/>
  <stop offset="1" stop-color="#080505"/>
</radialGradient>
<radialGradient id="lava" cx="50%" cy="50%" r="50%">
  <stop offset="0" stop-color="#ff6a1c" stop-opacity="0.30"/>
  <stop offset="0.55" stop-color="#c2430f" stop-opacity="0.12"/>
  <stop offset="1" stop-color="#7a2a08" stop-opacity="0"/>
</radialGradient>
<radialGradient id="shadow" cx="50%" cy="50%" r="50%">
  <stop offset="0" stop-color="#000000" stop-opacity="0.66"/>
  <stop offset="0.6" stop-color="#050302" stop-opacity="0.30"/>
  <stop offset="1" stop-color="#050302" stop-opacity="0"/>
</radialGradient>
<radialGradient id="heat" cx="50%" cy="50%" r="50%">
  <stop offset="0" stop-color="#ffb45e" stop-opacity="0.28"/>
  <stop offset="1" stop-color="#ff6a1c" stop-opacity="0"/>
</radialGradient>
<linearGradient id="sheet" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#1a1310"/>
  <stop offset="1" stop-color="#0b0807"/>
</linearGradient>
<pattern id="hatch" width="7" height="7" patternTransform="rotate(45)"
         patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="7" stroke="#000000" stroke-opacity="0.30"
        stroke-width="2.2"/>
</pattern>
<pattern id="hatch2" width="6" height="6" patternTransform="rotate(-45)"
         patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="6" stroke="#2a1c12" stroke-opacity="0.5"
        stroke-width="1.4"/>
</pattern>
"""


def backdrop(bottom_glow=True, radius=250, cy=452):
    out = '<rect width="512" height="512" fill="url(#cave)"/>'
    if bottom_glow:
        out += ('<ellipse cx="256" cy="%d" rx="%d" ry="%d" fill="url(#lava)"/>'
                % (cy, radius, int(radius * 0.42)))
    return out


def ground_shadow(cam, y=-200.0, z=30.0, rx=150.0, rz=42.0):
    x, sy, _ = cam.proj((0.0, y, z))
    return ('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="url(#shadow)"/>'
            % (x, sy + 6, rx * cam.s * 0.55, rz * cam.s * 0.55))


# ------------------------------------------------------------------- framing
def hero_cam(faces, margin=30.0, scale_mul=1.0):
    return M.fit_cam(faces, M.vnorm((0.42, -0.16, -0.89)), (0, 1, 0),
                     margin=margin, scale_mul=scale_mul)


ORTHO = {
    'front':  ((0.0, 0.0, -1.0), (0, 1, 0)),
    'back':   ((0.0, 0.0, 1.0), (0, 1, 0)),
    'left':   ((-1.0, 0.0, 0.0), (0, 1, 0)),
    'right':  ((1.0, 0.0, 0.0), (0, 1, 0)),
    'top':    ((0.0, -1.0, 0.0), (0, 0, -1)),
    'bottom': ((0.0, 1.0, 0.0), (0, 0, 1)),
}


def shared_ortho_cam(faces, margin=34.0):
    """One scale + one centre for all six views (they must register)."""
    xs, ys = [], []
    for name, (d, up) in ORTHO.items():
        cam = M.Cam(d, up, 1.0, 256.0, 256.0)
        for f in faces:
            for p in f['p']:
                xs.append(M.vdot(p, cam.r))
                ys.append(-M.vdot(p, cam.u))
    w = max(xs) - min(xs)
    h = max(ys) - min(ys)
    s = min((512 - 2 * margin) / w, (512 - 2 * margin) / h)
    return s, 256.0 - (min(xs) + max(xs)) / 2 * s, 256.0 - (min(ys) + max(ys)) / 2 * s


# ------------------------------------------------------------------ analysis
def area_ratio(png_path, bg=(10, 7, 6), tol=26):
    """Measure hole area / (body + hole) in a rendered PNG (256..511 px box)."""
    try:
        from PIL import Image
    except Exception:
        return None
    im = Image.open(png_path).convert('RGB')
    w, h = im.size
    px = im.load()

    def is_bg(c):
        return all(abs(c[i] - bg[i]) < tol for i in range(3))
    # flood fill from the border over background-ish pixels
    from collections import deque
    outside = [[False] * w for _ in range(h)]
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_bg(px[x, y]) and not outside[y][x]:
                outside[y][x] = True
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg(px[x, y]) and not outside[y][x]:
                outside[y][x] = True
                q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not outside[ny][nx] and is_bg(px[nx, ny]):
                outside[ny][nx] = True
                q.append((nx, ny))
    body = 0
    hole = 0
    for y in range(h):
        for x in range(w):
            if not is_bg(px[x, y]):
                body += 1
            elif not outside[y][x]:
                hole += 1
    return body, hole, (hole / float(body + hole) if body + hole else 0.0)


def projected_area(faces, cam, size=512):
    """Rasterise projected faces (union) and return the covered pixel count."""
    from PIL import Image, ImageDraw
    im = Image.new('L', (size, size), 0)
    dr = ImageDraw.Draw(im)
    for f in faces:
        pts = [cam.proj(p) for p in f['p']]
        dr.polygon([(p[0], p[1]) for p in pts], fill=255)
    return sum(im.getdata()) / 255.0


def bore_ratio(cam, phi_steps=200):
    """(mouth area, silhouette area, ratio) for the Q1 cavity in one view."""
    from PIL import Image, ImageDraw
    rim = []
    for i in range(phi_steps):
        phi = 2 * math.pi * i / phi_steps
        p = M.vadd(M.vmul(C.evec(phi), C.rF(phi)), M.vmul(C.N, C.tF(phi)))
        rim.append(cam.proj(p))
    a = 0.0
    for i in range(len(rim)):
        x1, y1, _ = rim[i]
        x2, y2, _ = rim[(i + 1) % len(rim)]
        a += x1 * y2 - x2 * y1
    a_mouth = abs(a) / 2.0

    m = M.Model()
    C.add_shell(m, albedo=M.C_STONE, bore_ember=False)
    im = Image.new('L', (512, 512), 0)
    dr = ImageDraw.Draw(im)
    for f in m.faces:
        dr.polygon([(cam.proj(p)[0], cam.proj(p)[1]) for p in f['p']], fill=255)
    dr.polygon([(p[0], p[1]) for p in rim], fill=255)
    a_sil = sum(im.getdata()) / 255.0
    return a_mouth, a_sil, a_mouth / max(a_sil, 1e-6)
