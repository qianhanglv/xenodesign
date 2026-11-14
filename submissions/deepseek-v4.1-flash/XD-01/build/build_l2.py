"""L2: section.svg - plane through the Q1 bore axis: void, gut, mineral frame."""
import math
import sys
sys.path.insert(0, '.')
import model as M
import creature as C
import present as P

TAU = M.TAU
OUT = P.ROOT + '/L2/section.svg'

m = C.build()
# paper plane = (V, N): look along -U, bore axis up -> section runs left/right
pts = [M.vadd(M.vmul(C.V, v), M.vmul(C.N, nn))
       for v in (-125.0, 125.0) for nn in (-40.0, 40.0)]
cam = M.fit_cam([{'p': pts}], (-1.0, 0.0, 0.0), C.N, margin=40)
cam.cy = 272.0


def sp(v, n):
    p = M.vadd(M.vmul(C.V, v), M.vmul(C.N, n))
    x, y, _ = cam.proj(p)
    return (x, y)


def dpath(pts, close=True):
    d = 'M ' + ' L '.join('%.1f %.1f' % sp(v, n) for (v, n) in pts)
    return d + (' Z' if close else '')


def local(phi, rho, alpha):
    e = C.evec(phi)
    p = M.vadd(M.vmul(e, rho), M.vmul(C.N, alpha))
    return (M.vdot(p, C.V), M.vdot(p, C.N))


def band(phi, steps=64):
    out = []
    for i in range(steps):
        p = C.ring_pt(phi, TAU * i / steps)
        out.append((M.vdot(p, C.V), M.vdot(p, C.N)))
    return out


phi_b, phi_t = -0.5 * math.pi, 0.5 * math.pi
bot, top = band(phi_b), band(phi_t)
R_b, r_b = C.RF(phi_b), C.rF(phi_b)
R_t, r_t = C.RF(phi_t), C.rF(phi_t)
m_b, h_b = 0.5 * (R_b + r_b), 0.5 * (R_b - r_b)
m_t, h_t = 0.5 * (R_t + r_t), 0.5 * (R_t - r_t)

# tunnel seen edge-on: the bore's inner surface projected along U
N_SEG = 42
edge_top, edge_bot = [], []
for i in range(N_SEG + 1):
    phi = -0.5 * math.pi + math.pi * i / N_SEG
    r = C.rF(phi)
    t = C.tF(phi)
    v = r * math.sin(phi)
    edge_top.append((v, t))
    edge_bot.append((v, -t))
tunnel = edge_top + list(reversed(edge_bot))

KEEP = ('shell',)
edges = {}
for f in m.faces:
    if f['t'] not in KEEP:
        continue
    if M.vdot(M._normal(f['p']), cam.d) > 0.02:
        continue
    pts_f = f['p']
    for i in range(len(pts_f)):
        a, b = pts_f[i], pts_f[(i + 1) % len(pts_f)]
        k = tuple(sorted(((round(a[0], 1), round(a[1], 1), round(a[2], 1)),
                          (round(b[0], 1), round(b[1], 1), round(b[2], 1)))))
        edges[k] = edges.get(k, 0) + 1
ghost = []
for (a, b), cnt in edges.items():
    if cnt > 1:
        continue
    p1, p2 = cam.proj(a), cam.proj(b)
    ghost.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (p1[0], p1[1], p2[0], p2[1]))

parts = ['<rect width="512" height="512" fill="url(#cave)"/>',
         '<ellipse cx="256" cy="282" rx="250" ry="92" fill="url(#lava)" '
         'opacity="0.55"/>']
# the body seen behind the cutting plane: one dark mass
parts.append(M.flat_polys(m.faces, cam, M.rgb('#2b1e15')))

# --- the void: continuous bore from mouth to mouth
parts.append('<path d="%s" fill="#100a07"/>' % dpath(tunnel))
parts.append('<path d="%s" fill="url(#heat)" opacity="0.85"/>' % dpath(tunnel))
parts.append('<path d="%s" fill="none" stroke="#f0bd80" stroke-width="2.2" '
             'stroke-opacity="0.55"/>' % dpath(tunnel))

# --- cut faces of the shell (hatched)
parts.append('<path d="%s" fill="#b9a98d" stroke="#1c120c" stroke-width="3.2" '
             'stroke-linejoin="round"/>' % dpath(bot))
parts.append('<path d="%s" fill="#c6b698" stroke="#1c120c" stroke-width="3.2" '
             'stroke-linejoin="round"/>' % dpath(top))
parts.append('<path d="%s" fill="url(#hatch)" opacity="0.9"/>' % dpath(bot))
parts.append('<path d="%s" fill="url(#hatch)" opacity="0.9"/>' % dpath(top))

# --- mineral frame: a truss, not a vertebral column
def truss(phi, mid, hh, ns):
    segs = []
    for i in range(ns):
        a1 = -0.78 + 1.56 * i / (ns - 1.0)
        for sgn in (-1, 1):
            A = local(phi, mid - hh * 0.60, a1 * hh * 0.78)
            B = local(phi, mid + hh * 0.60, a1 * hh * 0.78 + sgn * 0.30 * hh)
            segs.append((A, B))
        A2 = local(phi, mid - hh * 0.60, a1 * hh * 0.78)
        B2 = local(phi, mid + hh * 0.60, a1 * hh * 0.78)
        segs.append((A2, B2))
    return segs


struts = truss(phi_b, m_b, h_b, 8) + truss(phi_t, m_t, h_t, 7)
for col, wid, op in (('#5f4f3c', 5.0, 1.0), ('#e8d6b4', 1.5, 0.55)):
    parts.append('<g stroke="%s" stroke-width="%.1f" stroke-opacity="%.2f" '
                 'stroke-linecap="round">' % (col, wid, op))
    for A, B in struts:
        x1, y1 = sp(*A)
        x2, y2 = sp(*B)
        parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                     % (x1, y1, x2, y2))
    parts.append('</g>')

# --- digestive cavity + three ducts
gut_local = [(-17.0, 0.0), (-20.0, 11.0), (-13.0, 21.0), (0.0, 25.0),
             (13.0, 21.0), (20.0, 11.0), (17.0, 0.0), (0.0, -4.0)]
gut = [local(phi_b, m_b + a, b) for (a, b) in gut_local]

for k, rho0 in enumerate((-13.0, 0.0, 13.0)):
    c0 = local(phi_b, m_b + rho0, C.tF(phi_b) - 2.0)
    c1 = local(phi_b, m_b + rho0 * 0.6, 23.0)
    c2 = local(phi_b, m_b + rho0 * 0.3, 15.0)
    if k == 1:
        parts.append('<path d="%s" fill="none" stroke="#140b07" stroke-width="15.0" '
                     'stroke-linecap="round"/>' % dpath([c0, c1, c2], False))
        parts.append('<path d="%s" fill="none" stroke="#f0c48c" stroke-width="1.6" '
                     'stroke-opacity="0.6" stroke-linecap="round"/>'
                     % dpath([c0, c1, c2], False))
    else:
        parts.append('<path d="%s" fill="none" stroke="#c9b18f" stroke-width="10.0" '
                     'stroke-opacity="0.26" stroke-linecap="round"/>'
                     % dpath([c0, c1, c2], False))

parts.append('<path d="%s" fill="#140b07" stroke="#e8b478" stroke-width="2.6" '
             'stroke-opacity="0.9"/>' % dpath(gut))
parts.append('<path d="%s" fill="url(#heat)"/>' % dpath(gut))

# --- mouth lips cut open on the front face of the lower band
for rho0 in (-13.0, 0.0, 13.0):
    a = C.tF(phi_b)
    parts.append('<path d="%s" fill="#241711" stroke="#d9b184" stroke-width="2.0"/>'
                 % dpath([local(phi_b, m_b + rho0 - 9.0, a - 3.0),
                          local(phi_b, m_b + rho0 - 6.0, a + 4.0),
                          local(phi_b, m_b + rho0 + 6.0, a + 4.0),
                          local(phi_b, m_b + rho0 + 9.0, a - 3.0)]))

# --- crest sockets cut on the arch
for i in range(3):
    rho0 = m_t + (i - 1) * h_t * 0.46
    parts.append('<path d="%s" fill="#2a1a10" stroke="#e8b276" stroke-width="2.2" '
                 'stroke-opacity="0.9"/>'
                 % dpath([local(phi_t, rho0 - 7.0, 0.0),
                          local(phi_t, rho0 + 7.0, 0.0),
                          local(phi_t, rho0 + 2.0, h_t * 0.5 + 34.0)]))

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
       'width="512" height="512"><defs>%s</defs>%s</svg>' % (P.DEFS, ''.join(parts)))
open(OUT, 'w').write(svg)
import os
print("section", os.path.getsize(OUT), "scale", round(cam.s, 2), cam.cx, cam.cy)
