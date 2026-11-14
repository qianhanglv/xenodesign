"""Geometry + SVG renderer for X-DONUT-001.

World frame (creature body frame):  X = right, Y = up, Z = front.
1 unit = 1 cm.  Body shell outer diameter ~216 (2.16 m).
"""
import math

TAU = 2.0 * math.pi
D2R = math.pi / 180.0


# ----------------------------------------------------------------- vec math
def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vmul(a, s):
    return (a[0] * s, a[1] * s, a[2] * s)


def vmad(a, b, s):
    return (a[0] + b[0] * s, a[1] + b[1] * s, a[2] + b[2] * s)


def vdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vcross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def vlen(a):
    return math.sqrt(vdot(a, a))


def vnorm(a):
    l = vlen(a)
    if l < 1e-9:
        return (0.0, 0.0, 1.0)
    return (a[0] / l, a[1] / l, a[2] / l)


def vlerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t,
            a[1] + (b[1] - a[1]) * t,
            a[2] + (b[2] - a[2]) * t)


def rot_axis(p, axis, ang):
    """Rotate p about axis through origin (Rodrigues)."""
    k = vnorm(axis)
    c, s = math.cos(ang), math.sin(ang)
    return vadd(vadd(vmul(p, c), vmul(vcross(k, p), s)),
                vmul(k, vdot(k, p) * (1 - c)))


def rot_about(p, origin, axis, ang):
    return vadd(origin, rot_axis(vsub(p, origin), axis, ang))


def clamp(x, lo=0.0, hi=1.0):
    return lo if x < lo else (hi if x > hi else x)


def smoothstep(a, b, x):
    t = clamp((x - a) / (b - a) if b != a else 0.0)
    return t * t * (3 - 2 * t)


# --------------------------------------------------------------------- color
def rgb(h):
    h = h.lstrip('#')
    return (int(h[0:2], 16) / 255.0, int(h[2:4], 16) / 255.0, int(h[4:6], 16) / 255.0)


def cmix(a, b, t):
    return (a[0] + (b[0] - a[0]) * t,
            a[1] + (b[1] - a[1]) * t,
            a[2] + (b[2] - a[2]) * t)


def cscale(c, s):
    return (c[0] * s, c[1] * s, c[2] * s)


def chex(c):
    return '#%02x%02x%02x' % (int(clamp(c[0]) * 255 + 0.5),
                              int(clamp(c[1]) * 255 + 0.5),
                              int(clamp(c[2]) * 255 + 0.5))


# ------------------------------------------------------------------ palette
C_STONE = rgb('#a3957f')
C_STONE_D = rgb('#857659')
C_STONE_L = rgb('#c0b097')
C_STONE_M = rgb('#b0a189')
C_BASALT = rgb('#4a443c')
C_WARM = rgb('#8a6a4e')
C_HOT_ROCK = rgb('#3d2a21')
C_VOID = rgb('#0d0908')
C_EMBER = rgb('#ff7f2a')
C_LAVA = rgb('#ff5312')
C_GLOW = rgb('#ffd9a0')
C_COOL = rgb('#6d7f8f')

BG_DARK = rgb('#100b09')
BG_MID = rgb('#2a1f19')

# lights: (direction toward the light, colour, intensity)
KEY = (vnorm((0.46, 0.72, 0.52)), rgb('#fff6e9'), 1.45)
FILL = (vnorm((-0.86, 0.30, 0.28)), rgb('#86a0bd'), 0.42)
SKY = (vnorm((0.02, 1.0, 0.06)), rgb('#c6d4de'), 0.14)
UNDER = (vnorm((0.02, -0.94, 0.34)), rgb('#ff5c10'), 0.55)
AMBIENT = 0.22
RIM_COL = rgb('#ff9a4a')
RIM_POW = 2.2
RIM_AMT = 0.75


SHADE_STEPS = (0.30, 0.46, 0.62, 0.78, 0.92)
SHADE_GAMMA = 1.0


def shade(albedo, n, d=None):
    """Flat-shaded mineral stone: five-step key, cool fill, ember bounce, rim."""
    lam = vdot(n, KEY[0])
    if lam > 0.78:
        k = 1.20
    elif lam > 0.52:
        k = 1.03
    elif lam > 0.26:
        k = 0.85
    elif lam > 0.0:
        k = 0.67
    else:
        k = 0.54
    lit = cscale(albedo, k)
    fl = max(0.0, vdot(n, FILL[0]))
    lit = (lit[0] + albedo[0] * FILL[1][0] * fl * 0.16,
           lit[1] + albedo[1] * FILL[1][1] * fl * 0.16,
           lit[2] + albedo[2] * FILL[1][2] * fl * 0.16)
    ul = max(0.0, vdot(n, UNDER[0]))
    lit = (lit[0] + UNDER[1][0] * ul * 0.20,
           lit[1] + UNDER[1][1] * ul * 0.20,
           lit[2] + UNDER[1][2] * ul * 0.20)
    if d is not None:
        fr = (1.0 - abs(vdot(n, d))) ** 2.4 * 0.44
        lit = (lit[0] + RIM_COL[0] * fr,
               lit[1] + RIM_COL[1] * fr,
               lit[2] + RIM_COL[2] * fr)
    return lit


# -------------------------------------------------------------------- camera
class Cam:
    def __init__(self, d, up, scale=1.0, cx=256.0, cy=256.0):
        self.d = vnorm(d)                       # view direction (into scene)
        self.r = vnorm(vcross(self.d, up))      # screen +x
        self.u = vcross(self.r, self.d)         # screen +y (up)
        self.s = scale
        self.cx = cx
        self.cy = cy

    def proj(self, p):
        return (self.cx + vdot(p, self.r) * self.s,
                self.cy - vdot(p, self.u) * self.s,
                vdot(p, self.d))

    def ray(self):
        return self.d


def fit_cam(faces, d, up, margin=26.0, canvas=512.0, scale_mul=1.0):
    """Return a camera that frames all points in direction d (uniform scale)."""
    cam = Cam(d, up, 1.0, canvas / 2, canvas / 2)
    xs, ys = [], []
    for f in faces:
        for p in f['p']:
            xs.append(vdot(p, cam.r))
            ys.append(-vdot(p, cam.u))
    w = max(xs) - min(xs)
    h = max(ys) - min(ys)
    s = min((canvas - 2 * margin) / max(w, 1e-6),
            (canvas - 2 * margin) / max(h, 1e-6)) * scale_mul
    cam.s = s
    cam.cx = canvas / 2 - (min(xs) + max(xs)) / 2 * s
    cam.cy = canvas / 2 - (min(ys) + max(ys)) / 2 * s
    return cam


# --------------------------------------------------------------------- faces
class Model:
    """Collects polygons. kind: 'solid' (culled+shaded), 'emit', 'flat'."""

    def __init__(self):
        self.faces = []

    def poly(self, pts, albedo, kind='solid', alpha=None, jitter=0.0, tag='',
             outward=None, emissive=None):
        pts = [tuple(x) for x in pts]
        if outward is not None and len(pts) >= 3:
            n = _normal(pts)
            c = _centroid(pts)
            ref = vsub(c, outward)
            if vdot(n, ref) < 0:
                pts = list(reversed(pts))
        self.faces.append({'p': pts, 'c': albedo, 'e': emissive,
                           'k': kind, 'a': alpha, 'j': jitter, 't': tag})

    def extend(self, other):
        self.faces.extend(other.faces)


def _centroid(pts):
    n = float(len(pts))
    return (sum(p[0] for p in pts) / n,
            sum(p[1] for p in pts) / n,
            sum(p[2] for p in pts) / n)


def _normal(pts):
    n = (0.0, 0.0, 0.0)
    for i in range(len(pts)):
        a = pts[i]
        b = pts[(i + 1) % len(pts)]
        n = vadd(n, ((a[1] - b[1]) * (a[2] + b[2]),
                     (a[2] - b[2]) * (a[0] + b[0]),
                     (a[0] - b[0]) * (a[1] + b[1])))
    return vnorm(n)


# ----------------------------------------------------------------- svg emit
def render(faces, cam, path, bg=None, vignette=True, defs_extra='', title=None,
           wobble=None, edge=0.0, outline=0.0, outline_col='#0b0806',
           bg_html=None, under_html='', top_html=''):
    """Sort by depth (far first), cull back faces, shade, write svg."""
    order = []
    for f in faces:
        pts = f['p']
        if len(pts) < 3:
            continue
        n = _normal(pts)
        depth = vdot(_centroid(pts), cam.d)
        if f['k'] == 'solid' and vdot(n, cam.d) > 0.02:
            continue
        order.append((depth, n, f))
    order.sort(key=lambda t: -t[0])

    out = []
    for depth, n, f in order:
        pts = f['p']
        if wobble:
            pts = [wobble(p) for p in pts]
        d = ' '.join('%.1f,%.1f' % (cam.proj(p)[0], cam.proj(p)[1]) for p in pts)
        col = f['c']
        if f['k'] == 'solid':
            nn = n if vdot(n, cam.d) > 0 else vmul(n, -1)
            c = shade(col, nn, cam.d)
            if f['j']:
                c = cscale(c, 1.0 + f['j'])
        elif f['k'] == 'emit':
            c = col
        elif f['k'] == 'flat':
            c = col
        else:
            c = col
        if f.get('e'):
            c = vadd(c, f['e'])
        fill = chex(c)
        a = f['a']
        st = chex(cmix(c, rgb('#0a0705'), edge)) if edge else fill
        attrs = 'fill="%s" stroke="%s" stroke-width="%.2f"' % (fill, st, 0.7 + 1.2 * edge)
        if a is not None:
            attrs += ' fill-opacity="%.3f" stroke-opacity="%.3f"' % (a, a * 0.9)
        out.append('<polygon points="%s" %s/>' % (d, attrs))

    pre = []
    if outline:
        k = 1.0 + outline / 256.0
        # silhouette faces only: an edge used by exactly one visible face
        use = {}
        for depth, n, f in order:
            pts = f['p']
            for i in range(len(pts)):
                a = pts[i]
                b = pts[(i + 1) % len(pts)]
                key = tuple(sorted(((round(a[0], 2), round(a[1], 2), round(a[2], 2)),
                                    (round(b[0], 2), round(b[1], 2), round(b[2], 2)))))
                use[key] = use.get(key, 0) + 1
        sil = []
        for depth, n, f in order:
            pts = f['p']
            edge = False
            for i in range(len(pts)):
                a = pts[i]
                b = pts[(i + 1) % len(pts)]
                key = tuple(sorted(((round(a[0], 2), round(a[1], 2), round(a[2], 2)),
                                    (round(b[0], 2), round(b[1], 2), round(b[2], 2)))))
                if use.get(key, 0) <= 1:
                    edge = True
                    break
            if edge:
                sil.append(f)
        for f in sil:
            pts = f['p']
            d = ' '.join('%.1f,%.1f' % (cam.cx + (cam.proj(p)[0] - cam.cx) * k,
                                        cam.cy + (cam.proj(p)[1] - cam.cy) * k)
                         for p in pts)
            pre.append('<polygon points="%s" fill="%s" stroke="%s" '
                       'stroke-width="1" stroke-linejoin="round"/>'
                       % (d, outline_col, outline_col))
    if bg_html is not None:
        defs = '<defs>%s</defs>' % defs_extra
        bg = bg_html
    elif bg is None:
        bg = '<rect width="512" height="512" fill="#0d0908"/>'
    if bg_html is None and vignette:
        vig = ('<radialGradient id="bgv" cx="50%" cy="42%" r="72%">'
               '<stop offset="0" stop-color="#2b1f18"/>'
               '<stop offset="0.62" stop-color="#17100d"/>'
               '<stop offset="1" stop-color="#0a0706"/></radialGradient>')
        defs = '<defs>%s%s</defs>' % (vig, defs_extra)
        bg = '<rect width="512" height="512" fill="url(#bgv)"/>'
    else:
        defs = '<defs>%s</defs>' % defs_extra
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
           'width="512" height="512">' + defs + bg + under_html + '\n'
           + '\n'.join(pre) + '\n' + '\n'.join(out) + top_html + '</svg>')
    with open(path, 'w') as fh:
        fh.write(svg)
    return len(svg)


# ------------------------------------------------------------------ builders
def ring_point(phi, psi, RF, rF, tF, N, U, V, sq=0.72):
    e = vadd(vmul(U, math.cos(phi)), vmul(V, math.sin(phi)))
    R = RF(phi)
    r = rF(phi)
    rho = 0.5 * (R + r)
    h = 0.5 * (R - r)
    t = tF(phi)
    cs, sn = math.cos(psi), math.sin(psi)
    radial = h * math.copysign(abs(cs) ** sq, cs)
    axial = t * math.copysign(abs(sn) ** sq, sn)
    return vadd(vmul(e, rho + radial), vmul(N, axial))


def build_ring(m, RF, rF, tF, N, U, V, seg_u=48, seg_v=14, sq=0.72,
               albedo=None, alb_fn=None, tag='ring'):
    """Closed torus-ish shell, quads, outward winding."""
    albedo = albedo or C_STONE
    pts = [[ring_point(TAU * i / seg_u, TAU * j / seg_v, RF, rF, tF, N, U, V, sq)
            for j in range(seg_v)] for i in range(seg_u)]
    for i in range(seg_u):
        i2 = (i + 1) % seg_u
        for j in range(seg_v):
            j2 = (j + 1) % seg_v
            quad = [pts[i][j], pts[i2][j], pts[i2][j2], pts[i][j2]]
            a = albedo
            if alb_fn is not None:
                phi = TAU * (i + 0.5) / seg_u
                psi = TAU * (j + 0.5) / seg_v
                a = alb_fn(phi, psi, albedo)
            jit = 0.05 + 0.05 * math.sin(i * 2.7 + j * 1.9)
            phi = TAU * (i + 0.5) / seg_u
            e = vadd(vmul(U, math.cos(phi)), vmul(V, math.sin(phi)))
            ctr = vmul(e, 0.5 * (RF(phi) + rF(phi)))
            m.poly(quad, a, jitter=jit, tag=tag, outward=ctr)


def ring_surface_point(phi, psi, RF, rF, tF, N, U, V, sq=0.72):
    return ring_point(phi, psi, RF, rF, tF, N, U, V, sq)


def tube(m, path, radii, sides=7, albedo=None, cap_start=True, cap_end=True,
         twist=0.0, tag='limb', jitter=0.08):
    """Faceted tube along a polyline with per-node radius."""
    albedo = albedo or C_STONE
    n = len(path)
    rings = []
    up_ref = (0.0, 0.0, 1.0)
    for i, p in enumerate(path):
        if i == 0:
            tan = vnorm(vsub(path[1], path[0]))
        elif i == n - 1:
            tan = vnorm(vsub(path[-1], path[-2]))
        else:
            tan = vnorm(vsub(path[i + 1], path[i - 1]))
        ref = up_ref
        if abs(vdot(ref, tan)) > 0.94:
            ref = (1.0, 0.0, 0.0)
        bx = vnorm(vcross(ref, tan))
        by = vnorm(vcross(tan, bx))
        ring = []
        for k in range(sides):
            a = TAU * k / sides + twist + i * 0.14
            ring.append(vadd(p, vadd(vmul(bx, math.cos(a) * radii[i]),
                                     vmul(by, math.sin(a) * radii[i]))))
        rings.append(ring)
    for i in range(n - 1):
        for k in range(sides):
            k2 = (k + 1) % sides
            quad = [rings[i][k], rings[i][k2], rings[i + 1][k2], rings[i + 1][k]]
            ctr = vmul(vadd(path[i], path[i + 1]), 0.5)
            m.poly(quad, albedo, jitter=jitter, tag=tag, outward=ctr)
    if cap_start:
        m.poly(list(reversed(rings[0])), albedo, jitter=jitter, tag=tag,
               outward=path[0])
    if cap_end:
        m.poly(rings[-1], albedo, jitter=jitter, tag=tag, outward=path[-1])
    return rings


def ellipsoid(m, c, rad, seg_u=10, seg_v=6, albedo=None, tag='blob',
              jitter=0.08, rot=None):
    albedo = albedo or C_STONE
    pts = []
    for i in range(seg_u):
        row = []
        a = TAU * i / seg_u
        for j in range(seg_v):
            b = math.pi * (j + 0.5) / seg_v
            p = (rad[0] * math.cos(a) * math.sin(b),
                 rad[1] * math.cos(b),
                 rad[2] * math.sin(a) * math.sin(b))
            if rot:
                p = rot(p)
            row.append(vadd(c, p))
        pts.append(row)
    for i in range(seg_u):
        i2 = (i + 1) % seg_u
        for j in range(seg_v - 1):
            m.poly([pts[i][j], pts[i2][j], pts[i2][j + 1], pts[i][j + 1]],
                   albedo, jitter=jitter, tag=tag, outward=c)
    # caps
    top = vadd(c, (0.0, rad[1], 0.0) if not rot else rot((0.0, rad[1], 0.0)))
    bot = vadd(c, (0.0, -rad[1], 0.0) if not rot else rot((0.0, -rad[1], 0.0)))
    for i in range(seg_u):
        i2 = (i + 1) % seg_u
        m.poly([pts[i][0], pts[i2][0], top], albedo, jitter=jitter, tag=tag,
               outward=c)
        m.poly([pts[i2][-1], pts[i][-1], bot], albedo, jitter=jitter, tag=tag,
               outward=c)


def disc(m, c, nrm, rad, seg=16, albedo=None, tag='disc', side=None):
    """Flat disc facing nrm (winding chosen to face nrm)."""
    albedo = albedo or C_STONE
    nrm = vnorm(nrm)
    ref = (0.0, 1.0, 0.0) if abs(nrm[1]) < 0.9 else (1.0, 0.0, 0.0)
    ax = vnorm(vcross(ref, nrm))
    ay = vnorm(vcross(nrm, ax))
    pts = []
    for k in range(seg):
        a = TAU * k / seg
        pts.append(vadd(c, vadd(vmul(ax, math.cos(a) * rad),
                                vmul(ay, math.sin(a) * rad))))
    m.poly(pts, albedo, kind=side or 'flat', tag=tag,
           outward=vmad(c, nrm, -10.0))
    return pts
    return pts


def flat_polys(faces, cam, col, alpha=None, tag_filter=None, sort=True):
    """Culled, depth-sorted polygons filled with one flat colour."""
    order = []
    for f in faces:
        if tag_filter and f['t'] not in tag_filter:
            continue
        n = _normal(f['p'])
        if vdot(n, cam.d) > 0.02:
            continue
        order.append((vdot(_centroid(f['p']), cam.d), f))
    if sort:
        order.sort(key=lambda t: -t[0])
    out = []
    fill = chex(col)
    a = '' if alpha is None else ' fill-opacity="%.2f"' % alpha
    for _, f in order:
        d = ' '.join('%.1f,%.1f' % (cam.proj(p)[0], cam.proj(p)[1]) for p in f['p'])
        out.append('<polygon points="%s" fill="%s"%s stroke="%s" stroke-width="0.8"/>'
                   % (d, fill, a, fill))
    return ''.join(out)
