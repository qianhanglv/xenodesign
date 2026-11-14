import math, sys, os
sys.path.insert(0, '.')
import model as M, present as P

TAU = M.TAU
CX, CY = 256.0, 262.0


def wob(a, k, amp, ph=0.0):
    return amp * math.sin(a * k + ph)


def blob_path(cx, cy, rx, ry, n, bumps, rot=0.0, samp=160):
    pts = []
    for i in range(samp):
        a = TAU * i / samp
        r = 1.0 + sum(amp * math.sin(a * k + ph) for (k, amp, ph) in bumps)
        x = cx + rx * r * math.cos(a + rot)
        y = cy + ry * r * math.sin(a + rot)
        pts.append((x, y))
    return pts


def poly_d(pts, close=True):
    return 'M ' + ' L '.join('%.1f %.1f' % p for p in pts) + (' Z' if close else '')


# ---- sheet outline: one continuous piece, dorsal up, ventral down
sheet = blob_path(CX, CY, 205.0, 190.0, 160,
                  [(2, 0.045, 0.7), (3, 0.035, 2.1), (5, 0.022, 0.3),
                   (7, 0.014, 1.7), (11, 0.009, 0.4)])

# ---- holes
bore = blob_path(CX, CY - 6, 84.0, 66.0, 80,
                 [(2, 0.05, 0.2), (3, 0.04, 1.3), (5, 0.03, 2.4)])
collar_o = blob_path(CX, CY - 6, 104.0, 84.0, 80,
                     [(2, 0.045, 0.2), (3, 0.035, 1.3), (5, 0.028, 2.4)])
feed = [blob_path(CX - 62, 372, 21, 17, 40, [(3, 0.06, 0.4)]),
        blob_path(CX, 388, 24, 19, 40, [(3, 0.06, 1.1)]),
        blob_path(CX + 62, 372, 21, 17, 40, [(3, 0.06, 2.0)])]
legs = [blob_path(150, 400, 30, 26, 48, [(4, 0.08, 0.5)]),
        blob_path(362, 400, 30, 26, 48, [(4, 0.08, 1.4)])]
arms = [blob_path(78, 232, 24, 21, 44, [(4, 0.08, 0.9)]),
        blob_path(434, 232, 24, 21, 44, [(4, 0.08, 2.2)])]
crest = []
for i in range(6):
    x = CX - 105 + i * 42
    y = 118 + 9 * math.sin(i * 1.7)
    crest.append(blob_path(x, y, 7.0, 15.0, 26, [(2, 0.12, i)]))

parts = ['<rect width="512" height="512" fill="url(#cave)"/>',
         '<ellipse cx="256" cy="300" rx="240" ry="180" fill="url(#lava)" opacity="0.35"/>']

# the sheet: one path, holes as subpaths (evenodd)
d = poly_d(sheet)
for h in [bore] + feed + legs + arms + crest:
    d += ' ' + poly_d(h)
parts.append('<clipPath id="sheetclip"><path d="%s" fill-rule="evenodd"/></clipPath>' % d)
parts.append('<path d="%s" fill="url(#hide)" fill-rule="evenodd" stroke="#120c08" '
             'stroke-width="3.4" stroke-linejoin="round"/>' % d)
# hide texture: stretch marks, ventral shading
tex = []
for i in range(10):
    a = TAU * i / 10 + 0.2
    r0 = 112 + 6 * math.sin(i * 2.3)
    r1 = r0 + 46 + 18 * math.sin(i * 1.1)
    p1 = (CX + r0 * math.cos(a), CY - 6 + r0 * 0.86 * math.sin(a))
    p2 = (CX + r1 * math.cos(a), CY - 6 + r1 * 0.86 * math.sin(a))
    tex.append('<path d="M %.1f %.1f Q %.1f %.1f %.1f %.1f" fill="none" '
               'stroke="#4a3826" stroke-opacity="0.30" stroke-width="2.0"/>'
               % (p1[0], p1[1],
                  (p1[0] + p2[0]) / 2 + 16 * math.cos(a + 1.2),
                  (p1[1] + p2[1]) / 2 + 16 * math.sin(a + 1.2),
                  p2[0], p2[1]))
parts.append('<g clip-path="url(#sheetclip)">%s'
             '<ellipse cx="256" cy="440" rx="230" ry="110" fill="#3a2a1c" '
             'opacity="0.45"/><ellipse cx="256" cy="96" rx="220" ry="80" '
             'fill="#f0e2c6" opacity="0.18"/></g>' % ''.join(tex))

# collar: tunnel lining folded flat around the bore hole
parts.append('<path d="%s" fill="none" stroke="#8a755a" stroke-width="3.0" '
             'stroke-opacity="0.85" stroke-dasharray="9 6"/>' % poly_d(collar_o))

# seams: radial lines from the collar to the sheet edge
seams = []
for i in range(7):
    a = TAU * i / 7 + 0.35
    p1 = (CX + 108 * math.cos(a), CY - 6 + 88 * math.sin(a))
    p2 = (CX + 198 * math.cos(a), CY - 6 + 184 * math.sin(a))
    seams.append((p1, p2, a))
for p1, p2, a in seams:
    parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#2a1c12" '
                 'stroke-width="2.2" stroke-dasharray="7 5"/>' % (p1 + p2))
    # stitch ticks
    for t in (0.35, 0.55, 0.75):
        mx = p1[0] + (p2[0] - p1[0]) * t
        my = p1[1] + (p2[1] - p1[1]) * t
        dx, dy = math.cos(a + 1.57) * 7, math.sin(a + 1.57) * 7
        parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#3a281a" '
                     'stroke-width="2.4"/>' % (mx - dx, my - dy, mx + dx, my + dy))

# cut seam: the single opening that lets the tube lie flat
cut = []
for i in range(30):
    t = i / 29.0
    a = -0.55 + 1.10 * t
    r = 1.02 - 0.030 * abs(math.sin(t * 12))
    cut.append((CX + 196 * r * math.cos(a + 2.55), CY - 4 + 180 * r * math.sin(a + 2.55)))
parts.append('<path d="%s" fill="none" stroke="#ffb066" stroke-width="3.0" '
             'stroke-opacity="0.75" stroke-dasharray="3 7"/>' % poly_d(cut, False))

# crest socket scorch marks and ventral plating hint
for h in crest:
    cx = sum(p[0] for p in h) / len(h)
    cy = sum(p[1] for p in h) / len(h)
    parts.append('<ellipse cx="%.1f" cy="%.1f" rx="15" ry="24" fill="url(#heat)" '
                 'opacity="0.5"/>' % (cx, cy))

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
       'width="512" height="512"><defs>%s<radialGradient id="hide" cx="46%%" cy="40%%" r="72%%">'
       '<stop offset="0" stop-color="#cbbc9f"/>'
       '<stop offset="0.55" stop-color="#a2937a"/>'
       '<stop offset="1" stop-color="#6d6050"/></radialGradient></defs>%s</svg>'
       % (P.DEFS, ''.join(parts)))
open(P.ROOT + '/L3/pelt.svg', 'w').write(svg)
print("pelt", os.path.getsize(P.ROOT + '/L3/pelt.svg'))
