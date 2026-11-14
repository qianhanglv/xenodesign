import sys
sys.path.insert(0, '.')
import model as M, creature as C, present as P

m = C.build()
s, cx, cy = P.shared_ortho_cam(m.faces, margin=36)
print("shared scale %.3f centre %.1f %.1f" % (s, cx, cy))
for name, (d, up) in P.ORTHO.items():
    cam = M.Cam(d, up, s, cx, cy)
    bg = '<rect width="512" height="512" fill="url(#sheet)"/>' \
         '<rect x="8" y="8" width="496" height="496" fill="none" ' \
         'stroke="#2a1d16" stroke-width="1.2"/>'
    M.render(m.faces, cam, P.ROOT + '/L1/%s.svg' % name, bg_html=bg,
             defs_extra=P.DEFS, outline=7.0)
import os
for n in P.ORTHO:
    print(n, os.path.getsize(P.ROOT + '/L1/%s.svg' % n))
