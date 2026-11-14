import math, sys
sys.path.insert(0, '.')
import model as M, creature as C, present as P

OUT = P.ROOT + '/L0/creature.svg'
m = C.build()
cam = P.hero_cam(m.faces, margin=30)
bg = P.backdrop(True, 260, 470)
M.render(m.faces, cam, OUT, bg_html=bg, defs_extra=P.DEFS, outline=9.0,
         under_html=P.ground_shadow(cam, y=-198, z=28, rx=160, rz=44))
print("cam", round(cam.s, 3), round(cam.cx, 1), round(cam.cy, 1))
import os
print("size", os.path.getsize(OUT))
