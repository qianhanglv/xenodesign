"""L5: ride.svg - the same creature riding a bicycle."""
import math
import sys
sys.path.insert(0, '.')
import model as M
import creature as C
import present as P

TAU = M.TAU
OUT = P.ROOT + '/L5/ride.svg'

# ------------------------------------------------------------------ bicycle
BIKE = M.Model()
MET = M.rgb('#8e8b84')
MET_D = M.rgb('#4c4a46')
NW = C.N
NU, NV = C.U, C.V


def wheel(hub, R=46.0):
    tmp = M.Model()
    M.build_ring(tmp, lambda p: R + 4.5, lambda p: R - 4.5, lambda p: 4.5,
                 (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), (0.0, 1.0, 0.0), 44, 8,
                 sq=1.0, albedo=MET_D)
    for k in range(10):
        a = TAU * k / 10
        p1 = (0.0, math.sin(a) * 7.0, math.cos(a) * 7.0)
        p2 = (0.0, math.sin(a) * (R - 7), math.cos(a) * (R - 7))
        M.tube(tmp, [p1, p2], [1.6, 1.2], sides=4, albedo=MET, cap_start=False,
               cap_end=False)
    M.ellipsoid(tmp, (0.0, 0.0, 0.0), (6.0, 9.0, 9.0), 8, 4, albedo=MET)
    for f in tmp.faces:
        f = dict(f)
        f['p'] = [M.vadd(p, hub) for p in f['p']]
        BIKE.faces.append(f)


REAR = (0.0, -168.0, -74.0)
FRONT = (0.0, -168.0, 78.0)
BB = (0.0, -172.0, 6.0)          # bottom bracket
SEAT = (0.0, -112.0, -40.0)
HEAD_B = (0.0, -122.0, 62.0)
HEAD_T = (0.0, -88.0, 70.0)

wheel(REAR)
wheel(FRONT)
for a, b, r in ((REAR, BB, 4.2), (BB, SEAT, 5.0), (SEAT, HEAD_B, 4.6),
                (BB, HEAD_B, 5.2), (HEAD_B, FRONT, 4.0), (SEAT, REAR, 3.6)):
    M.tube(BIKE, [a, b], [r, r], sides=6, albedo=MET)
M.tube(BIKE, [HEAD_B, HEAD_T], [5.4, 5.4], sides=6, albedo=MET)
# handlebar
M.tube(BIKE, [(-30.0, -86.0, 68.0), (0.0, -88.0, 70.0), (30.0, -86.0, 68.0)],
       [4.4, 4.6, 4.4], sides=6, albedo=MET)
for s in (-1, 1):
    M.tube(BIKE, [(s * 30.0, -86.0, 68.0), (s * 44.0, -84.0, 62.0)],
           [4.6, 4.0], sides=6, albedo=MET)
# saddle
M.ellipsoid(BIKE, (0.0, -106.0, -44.0), (16.0, 6.0, 26.0), 10, 5,
            albedo=M.rgb('#3a2a20'))
# cranks + pedals
CRANK = 26.0
M.tube(BIKE, [BB, (0.0, -178.0, 30.0)], [3.4, 3.0], sides=5, albedo=MET_D)
M.tube(BIKE, [BB, (0.0, -164.0, -18.0)], [3.4, 3.0], sides=5, albedo=MET_D)
for pos in ((0.0, -178.0, 30.0), (0.0, -164.0, -18.0)):
    M.tube(BIKE, [(pos[0] - 11, pos[1], pos[2]), (pos[0] + 11, pos[1], pos[2])],
           [3.4, 3.4], sides=5, albedo=MET)
M.ellipsoid(BIKE, BB, (7.0, 7.0, 7.0), 8, 4, albedo=MET)

# scale the bicycle up about the tyre contact patch and sit it on the ground
S, CYC = 1.42, -214.0
for f in BIKE.faces:
    f['p'] = [(p[0] * S, CYC + (p[1] - CYC) * S + 8.0, 6.0 + (p[2] - 6.0) * S)
              for p in f['p']]

# ------------------------------------------------------------------- creature
pose = {
    'body_off': (0.0, 52.0, -6.0),
    'body_rot': (M.vnorm((1.0, 0.0, 0.0)), -0.16),
    'feet': {'L': (18.0, -168.0, 44.0), 'R': (-18.0, -150.0, -26.0)},
    'hands': {'L': (-58.0, -44.0, 88.0), 'R': (58.0, -46.0, 88.0)},
}
cm = C.build(pose)
m = M.Model()
m.extend(cm)
m.extend(BIKE)

cam = M.fit_cam(m.faces, M.vnorm((0.56, -0.20, -0.80)), (0, 1, 0), margin=26)

bg = ('<rect width="512" height="512" fill="url(#cave)"/>'
      '<ellipse cx="256" cy="470" rx="240" ry="58" fill="url(#shadow)"/>')
M.render(m.faces, cam, OUT, bg_html=bg, defs_extra=P.DEFS, outline=8.0)
import os
print("ride", os.path.getsize(OUT), "scale", round(cam.s, 2))
