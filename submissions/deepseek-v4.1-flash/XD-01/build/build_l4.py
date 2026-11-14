"""L4: motion.svg - a looping idle -> run -> jump -> land -> idle cycle."""
import math
import sys
sys.path.insert(0, '.')
import model as M
import creature as C
import present as P

TAU = M.TAU
OUT = P.ROOT + '/L4/motion.svg'
DUR = 3.2

m = C.build()
cam = P.hero_cam(m.faces, margin=44)

BODY_TAGS = ('shell', 'crest', 'crest-base', 'maw', 'maw-glow', 'rib')
LIMB_TAGS = {'leg-L': 'L', 'leg-R': 'R', 'arm-L': 'L', 'arm-R': 'R'}

body_faces = [f for f in m.faces if f['t'] in BODY_TAGS]
leg_faces = {k: [f for f in m.faces if f['t'] == 'leg-' + k] for k in ('L', 'R')}
arm_faces = {k: [f for f in m.faces if f['t'] == 'arm-' + k] for k in ('L', 'R')}

pose = C.rest_pose()
hips, shs = C.limb_roots()

# rest joint chains (world) -> screen
leg_rest = {}
for k, foot in pose['feet'].items():
    hip = hips[k]
    j, e = C.ik2(hip, foot, C.LEG_L[0], C.LEG_L[1], M.vnorm((0.10, 0.0, 1.0)))
    leg_rest[k] = (hip, j, e)
arm_rest = {}
for k, hand in pose['hands'].items():
    sh = shs[k]
    j, e = C.ik2(sh, hand, C.ARM_L[0], C.ARM_L[1],
                M.vnorm((math.copysign(1.0, sh[0]), -0.15, 0.10)))
    arm_rest[k] = (sh, j, e)


def scr(p):
    x, y, _ = cam.proj(p)
    return (x, y)


def ang(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def ik2d(H, T, L1, L2, side):
    dx, dy = T[0] - H[0], T[1] - H[1]
    dist = math.hypot(dx, dy)
    dist = max(1e-3, min(dist, (L1 + L2) * 0.999))
    ca = (L1 * L1 + dist * dist - L2 * L2) / (2 * L1 * dist)
    a = math.acos(max(-1.0, min(1.0, ca)))
    ux, uy = dx / (math.hypot(dx, dy) + 1e-9), dy / (math.hypot(dx, dy) + 1e-9)
    px, py = -uy * side, ux * side
    return (H[0] + (ux * math.cos(a) + px * math.sin(a)) * L1,
            H[1] + (uy * math.cos(a) + py * math.sin(a)) * L1)


# screen kinematics of the rest pose
LEG = {}
for k, (hip, j, e) in leg_rest.items():
    H, J, E = scr(hip), scr(j), scr(e)
    L1 = math.hypot(J[0] - H[0], J[1] - H[1])
    L2 = math.hypot(E[0] - J[0], E[1] - J[1])
    ux, uy = (E[0] - H[0]) / max(math.dist(H, E), 1e-6), (E[1] - H[1]) / max(math.dist(H, E), 1e-6)
    side = 1.0 if (ux * (J[1] - H[1]) - uy * (J[0] - H[0])) > 0 else -1.0
    LEG[k] = dict(H=H, J=J, E=E, L1=L1, L2=L2, side=side,
                  t1=ang(H, J), t2=ang(J, E), hip3=hip)
ARM = {}
for k, (sh, j, e) in arm_rest.items():
    H, J, E = scr(sh), scr(j), scr(e)
    L1 = math.hypot(J[0] - H[0], J[1] - H[1])
    L2 = math.hypot(E[0] - J[0], E[1] - J[1])
    ux, uy = (E[0] - H[0]) / max(math.dist(H, E), 1e-6), (E[1] - H[1]) / max(math.dist(H, E), 1e-6)
    side = 1.0 if (ux * (J[1] - H[1]) - uy * (J[0] - H[0])) > 0 else -1.0
    ARM[k] = dict(H=H, J=J, E=E, L1=L1, L2=L2, side=side,
                  t1=ang(H, J), t2=ang(J, E), sh3=sh)

# ------------------------------------------------------------------ keyframes
# (t, body dx, body dy, footL, footR, handL, handR)   -- a two-legged hop cycle
G = C.GROUND + 2.0
RL = (-80.0, G, 118.0)
RR = (86.0, G, -8.0)
HL = (-98.0, -76.0, 116.0)
HR = (100.0, -72.0, 122.0)


def ride(keys):
    out = []
    for (t, dx, dy, fl, fr, hl, hr) in keys:
        out.append((t, dx, dy,
                    (fl[0], fl[1] + dy, fl[2]), (fr[0], fr[1] + dy, fr[2]),
                    (hl[0], hl[1] + dy * 0.9, hl[2]), (hr[0], hr[1] + dy * 0.9, hr[2])))
    return out


def F(x, z, lift=0.0):
    return (x, G + lift, z)


def Hh(x, y, z):
    return (x, y, z)


KEYS = [
    (0.00, 0.0, 0.0, RL, RR, HL, HR),
    (0.06, 0.0, 3.0, RL, RR, Hh(-100, -72, 120), Hh(102, -68, 126)),
    (0.12, 0.0, 0.0, RL, RR, HL, HR),
    # hop 1 - anticipation, push, air, land
    (0.18, 0.0, -26.0, F(-80, 118), F(86, -8), Hh(-106, -86, 106), Hh(108, -82, 112)),
    (0.23, 0.0, 16.0, F(-80, 112), F(86, -12), Hh(-96, -58, 124), Hh(98, -54, 130)),
    (0.29, 0.0, 58.0, F(-78, 92, 44), F(88, -22, 44), Hh(-90, -40, 128), Hh(92, -36, 134)),
    (0.35, 0.0, 14.0, F(-80, 106, 14), F(86, -14, 14), Hh(-100, -66, 118), Hh(102, -62, 124)),
    (0.41, 0.0, -24.0, F(-80, 120), F(86, -10), Hh(-108, -88, 104), Hh(110, -84, 110)),
    # hop 2 - faster, lower
    (0.46, 0.0, 10.0, F(-80, 114), F(86, -12), Hh(-96, -60, 122), Hh(98, -56, 128)),
    (0.51, 0.0, 48.0, F(-78, 96, 36), F(88, -18, 36), Hh(-90, -44, 126), Hh(92, -40, 132)),
    (0.57, 0.0, 10.0, F(-80, 108, 10), F(86, -12, 10), Hh(-102, -68, 116), Hh(104, -64, 122)),
    (0.62, 0.0, -20.0, F(-80, 120), F(86, -8), Hh(-108, -86, 106), Hh(110, -82, 112)),
    (0.68, 0.0, 4.0, F(-80, 118), F(86, -8), Hh(-100, -72, 118), Hh(102, -68, 124)),
    # the jump
    (0.74, 0.0, -30.0, F(-80, 116), F(86, -10), Hh(-112, -92, 100), Hh(114, -88, 106)),
    (0.79, 0.0, 24.0, F(-80, 110), F(86, -14), Hh(-92, -50, 128), Hh(94, -46, 134)),
    (0.84, 0.0, 72.0, F(-76, 86, 52), F(90, -30, 52), Hh(-84, -30, 132), Hh(86, -26, 138)),
    (0.89, 0.0, 24.0, F(-80, 104, 22), F(86, -16, 22), Hh(-98, -60, 122), Hh(100, -56, 128)),
    (0.93, 0.0, -26.0, F(-80, 120), F(86, -8), Hh(-110, -90, 102), Hh(112, -86, 108)),
    (0.97, 0.0, 4.0, F(-80, 118), F(86, -8), Hh(-100, -74, 118), Hh(102, -70, 124)),
    (1.00, 0.0, 0.0, RL, RR, HL, HR),
]
KEYS = ride(KEYS)

# ------------------------------------------------------------------ animation
SPLINES = ';'.join(['0.42 0 0.58 1'] * (len(KEYS) - 1))
KTIMES = ';'.join('%.3f' % k[0] for k in KEYS)

# screen-space body offset for each key (world dy up -> screen dy down)
BODY = [((k[1]) * cam.s, -(k[2]) * cam.s) for k in KEYS]
body_vals = ';'.join('%.2f,%.2f' % b for b in BODY)


def deltas_for(chains, kind):
    out = []
    for (t, dx, dy, fl, fr, hl, hr) in KEYS:
        tgt = (fl, fr) if kind == 'leg' else (hl, hr)
        per = {}
        for k in ('L', 'R'):
            ch = chains[k]
            T = scr(tgt[0] if k == 'L' else tgt[1])
            bx, by = BODY[KEYS.index((t, dx, dy, fl, fr, hl, hr))]
            T = (T[0] - bx, T[1] - by)
            K = ik2d(ch['H'], T, ch['L1'], ch['L2'], ch['side'])
            d1 = math.degrees(ang(ch['H'], K) - ch['t1'])
            d2 = math.degrees(ang(K, T) - ch['t2']) - d1
            per[k] = (d1, d2)
        out.append(per)
    return out


leg_vals = deltas_for(LEG, 'leg')
arm_vals = deltas_for(ARM, 'arm')


def rot_group(markup, deltas, root, joint):
    d1 = ';'.join('%.2f %.1f %.1f' % (dd[0], root[0], root[1]) for dd in deltas)
    d2 = ';'.join('%.2f %.1f %.1f' % (dd[1], joint[0], joint[1]) for dd in deltas)
    return ('<g><animateTransform attributeName="transform" type="rotate" '
            'values="%s" keyTimes="%s" dur="%.2fs" repeatCount="indefinite" '
            'calcMode="spline" keySplines="%s"/>'
            '<g><animateTransform attributeName="transform" type="rotate" '
            'values="%s" keyTimes="%s" dur="%.2fs" repeatCount="indefinite" '
            'calcMode="spline" keySplines="%s"/>%s</g></g>'
            % (d1, KTIMES, DUR, SPLINES, d2, KTIMES, DUR, SPLINES, markup))


def polys(faces):
    order = []
    for f in faces:
        n = M._normal(f['p'])
        if M.vdot(n, cam.d) > 0.02:
            continue
        order.append((M.vdot(M._centroid(f['p']), cam.d), n, f))
    order.sort(key=lambda t: -t[0])
    out = []
    for depth, n, f in order:
        nn = n if M.vdot(n, cam.d) > 0 else M.vmul(n, -1)
        c = M.shade(f['c'], nn, cam.d)
        if f.get('e'):
            c = M.vadd(c, f['e'])
        col = M.chex(c)
        d = ' '.join('%.1f,%.1f' % (cam.proj(p)[0], cam.proj(p)[1]) for p in f['p'])
        out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="0.8"/>'
                   % (d, col, col))
    return ''.join(out)


parts = ['<rect width="512" height="512" fill="url(#cave)"/>',
         '<ellipse cx="256" cy="446" rx="196" ry="52" fill="url(#shadow)"/>',
         '<g><animateTransform attributeName="transform" type="translate" '
         'values="%s" keyTimes="%s" dur="%.2fs" repeatCount="indefinite" '
         'calcMode="spline" keySplines="%s"/>'
         % (body_vals, KTIMES, DUR, SPLINES)]
parts.append(rot_group(polys(leg_faces['R']), [v['R'] for v in leg_vals],
                       LEG['R']['H'], LEG['R']['J']))
parts.append(rot_group(polys(arm_faces['R']), [v['R'] for v in arm_vals],
                       ARM['R']['H'], ARM['R']['J']))
parts.append(polys(body_faces))
parts.append(rot_group(polys(arm_faces['L']), [v['L'] for v in arm_vals],
                       ARM['L']['H'], ARM['L']['J']))
parts.append(rot_group(polys(leg_faces['L']), [v['L'] for v in leg_vals],
                       LEG['L']['H'], LEG['L']['J']))
parts.append('</g>')

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
       'width="512" height="512"><defs>%s</defs>%s</svg>'
       % (P.DEFS, ''.join(parts)))
open(OUT, 'w').write(svg)
import os
print("motion", os.path.getsize(OUT), "keys", len(KEYS), "scale", round(cam.s, 2))

# --------------------------------------------------------------- verification
if os.environ.get('VERIFY'):
    def static_svg(i):
        bx, by = BODY[i]
        out = ['<rect width="512" height="512" fill="url(#cave)"/>',
               '<g transform="translate(%.2f,%.2f)">' % (bx, by)]
        for k, faces, vals in (('R', leg_faces['R'], leg_vals),
                               ('R', arm_faces['R'], arm_vals)):
            pass
        def grp(markup, dd, root, joint):
            return ('<g transform="rotate(%.2f %.1f %.1f)">'
                    '<g transform="rotate(%.2f %.1f %.1f)">%s</g></g>'
                    % (dd[0], root[0], root[1], dd[1], joint[0], joint[1], markup))
        out.append(grp(polys(leg_faces['R']), leg_vals[i]['R'], LEG['R']['H'], LEG['R']['J']))
        out.append(grp(polys(arm_faces['R']), arm_vals[i]['R'], ARM['R']['H'], ARM['R']['J']))
        out.append(polys(body_faces))
        out.append(grp(polys(arm_faces['L']), arm_vals[i]['L'], ARM['L']['H'], ARM['L']['J']))
        out.append(grp(polys(leg_faces['L']), leg_vals[i]['L'], LEG['L']['H'], LEG['L']['J']))
        out.append('</g>')
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
                'width="512" height="512"><defs>%s</defs>%s</svg>'
                % (P.DEFS, ''.join(out)))
    for i in range(len(KEYS)):
        open('/tmp/svgtest/frame_%02d.svg' % i, 'w').write(static_svg(i))
    print("wrote", len(KEYS), "verification frames")
