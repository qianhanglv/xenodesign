import math, sys, os
sys.path.insert(0, '.')
import model as M, creature as C, present as P

# ---------------------------------------------------------------- skeleton.svg
m = C.build()
cam = P.hero_cam(m.faces, margin=30)

frame = M.Model()
# shell work: hoops around the bore + radial spokes (no vertebral column)
for rho_f in (-0.62, 0.0, 0.62):
    loop = []
    for i in range(0, 72):
        phi = M.TAU * i / 72
        r = C.rF(phi) + (C.RF(phi) - C.rF(phi)) * (0.5 + rho_f * 0.5)
        loop.append(M.vmul(C.evec(phi), r))
    for i in range(len(loop)):
        M.tube(frame, [loop[i], loop[(i + 1) % len(loop)]], [3.2, 3.2], sides=5,
               albedo=M.C_STONE_L, cap_start=False, cap_end=False, tag='bone')
for i in range(14):
    phi = M.TAU * i / 14 + 0.1
    a = M.vmul(C.evec(phi), C.rF(phi) + 2.0)
    b = M.vmul(C.evec(phi), C.RF(phi) - 2.0)
    M.tube(frame, [a, b], [3.6, 3.6], sides=5, albedo=M.C_STONE_M, tag='bone')
# joint collars at the limb roots and crest sockets
hips, shs = C.limb_roots()
for k, p in list(hips.items()) + list(shs.items()):
    M.ellipsoid(frame, p, (10.0, 10.0, 10.0), 8, 5, albedo=M.C_STONE_L, tag='bone')
# limb bones
pose = C.rest_pose()
for key, foot in pose['feet'].items():
    hip = hips[key]
    joint, end = C.ik2(hip, foot, C.LEG_L[0], C.LEG_L[1], C.M.vnorm((0.10, 0.0, 1.0)))
    M.tube(frame, [hip, joint, end], [9.0, 7.4, 5.6], sides=7,
           albedo=M.C_STONE_L, tag='bone')
    M.ellipsoid(frame, joint, (9.5, 9.5, 9.5), 8, 5, albedo=M.C_STONE_L, tag='bone')
    M.ellipsoid(frame, end, (11.0, 4.5, 16.0), 10, 5, albedo=M.C_STONE_M, tag='bone')
for key, hand in pose['hands'].items():
    sh = shs[key]
    joint, end = C.ik2(sh, hand, C.ARM_L[0], C.ARM_L[1], C.M.vnorm((math.copysign(1.0, sh[0]), -0.15, 0.10)))
    M.tube(frame, [sh, joint, end], [6.4, 5.2, 4.0], sides=7,
           albedo=M.C_STONE_L, tag='bone')
    M.ellipsoid(frame, joint, (6.8, 6.8, 6.8), 8, 5, albedo=M.C_STONE_L, tag='bone')

bg = P.backdrop(True, 250, 466)
parts = [bg]
parts.append(M.flat_polys(m.faces, cam, M.rgb('#d8cbb2'), alpha=0.14))
# draw the frame
order = []
for f in frame.faces:
    n = M._normal(f['p'])
    if M.vdot(n, cam.d) > 0.02:
        continue
    order.append((M.vdot(M._centroid(f['p']), cam.d), n, f))
order.sort(key=lambda t: -t[0])
out = []
for depth, n, f in order:
    nn = n if M.vdot(n, cam.d) > 0 else M.vmul(n, -1)
    c = M.shade(f['c'], nn, cam.d)
    col = M.chex(c)
    d = ' '.join('%.1f,%.1f' % (cam.proj(p)[0], cam.proj(p)[1]) for p in f['p'])
    out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="0.8"/>'
               % (d, col, col))
parts.append(''.join(out))
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
       'width="512" height="512"><defs>%s</defs>%s</svg>' % (P.DEFS, ''.join(parts)))
open(P.ROOT + '/L3/skeleton.svg', 'w').write(svg)
print("skeleton", os.path.getsize(P.ROOT + '/L3/skeleton.svg'))
