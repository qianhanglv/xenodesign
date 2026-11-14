"""X-DONUT-001 creature 'Pyroryx': toroidal mineral shell, 4 limbs, 3 maws."""
import math
import model as M

D2R = M.D2R
TAU = M.TAU

# ---------------------------------------------------------------- body frame
TILT = 27.0 * D2R
N = M.vnorm((0.0, math.sin(TILT), math.cos(TILT)))   # bore axis (up-forward)
U = (1.0, 0.0, 0.0)                                   # ring plane +x
V = M.vnorm(M.vcross(N, U))                           # ring plane up (up-back)

# --- shell: heavy lower mass, slender upper arch, off-centre bore ---------
IN_C = (0.0, 13.0)     # bore centre offset in the ring plane (u, v)
IN_R = 74.0            # bore radius
THICK = 31.0
SQ = 0.60

GROUND = -205.0
LEG_L = (92.0, 88.0)
ARM_L = (66.0, 60.0)


def RF(phi):
    """outer contour radius (ring plane)"""
    return (112.0 + 7.0 * math.cos(2 * phi + 0.70)
            + 4.0 * math.cos(5 * phi + 1.90)
            + 1.6 * math.cos(9 * phi + 0.20)
            + 3.0 * math.cos(1 * phi - 0.30))


def rF(phi):
    """inner contour radius: distance to an off-centre circular bore"""
    ex, ey = math.cos(phi), math.sin(phi)
    b = ex * IN_C[0] + ey * IN_C[1]
    cc = IN_C[0] ** 2 + IN_C[1] ** 2 - IN_R ** 2
    return b + math.sqrt(max(b * b - cc, 0.0))


def tF(phi):
    """half thickness along the bore axis: thick low, thin on the arch"""
    return THICK + 5.0 * (-math.sin(phi)) + 1.8 * math.cos(2 * phi + 0.4)


def ring_pt(phi, psi, sq=SQ):
    return M.ring_point(phi, psi, RF, rF, tF, N, U, V, sq)


def evec(phi):
    return M.vadd(M.vmul(U, math.cos(phi)), M.vmul(V, math.sin(phi)))


def face_pt(phi, rho_frac=0.5, ax=None):
    """point on the front (bore-facing) face at ring-angle phi."""
    e = evec(phi)
    rho = rF(phi) + (RF(phi) - rF(phi)) * rho_frac
    return M.vadd(M.vmul(e, rho), M.vmul(N, tF(phi) if ax is None else ax))


PHI_PLATE = TAU / 14.0
PSI_PLATE = TAU / 7.0


def shell_albedo(phi, psi, c):
    """basalt shell: plate patches, crevices between plates, darker bore."""
    inner = max(0.0, -math.cos(psi))
    ao = 1.0 - 0.24 * inner ** 1.2
    axial = max(0.0, -math.sin(psi))
    ao *= 1.0 - 0.14 * axial ** 1.2
    bp = int(phi / PHI_PLATE)
    bq = int(psi / PSI_PLATE)
    h = math.sin(bp * 12.9898 + bq * 78.233) * 43758.5453
    h = h - math.floor(h)
    tone = 1.0 + (h - 0.5) * 0.14
    fp = (phi / PHI_PLATE) % 1.0
    fq = (psi / PSI_PLATE) % 1.0
    seam = 1.0
    if min(fp, 1 - fp) < 0.09 or min(fq, 1 - fq) < 0.09:
        seam = 0.74
    return M.cscale(c, M.clamp(ao * tone * seam, 0.12, 1.2))


# --------------------------------------------------------------------- shell
def add_shell(m, seg_u=60, seg_v=16, albedo=None, alpha=None, bore_ember=True):
    albedo = albedo or M.C_STONE
    pts = [[ring_pt(TAU * i / seg_u, TAU * j / seg_v) for j in range(seg_v)]
           for i in range(seg_u)]
    for i in range(seg_u):
        i2 = (i + 1) % seg_u
        phi = TAU * (i + 0.5) / seg_u
        e = evec(phi)
        ctr = M.vmul(e, 0.5 * (RF(phi) + rF(phi)))
        for j in range(seg_v):
            j2 = (j + 1) % seg_v
            quad = [pts[i][j], pts[i2][j], pts[i2][j2], pts[i][j2]]
            psi = TAU * (j + 0.5) / seg_v
            a = shell_albedo(phi, psi, albedo)
            emi = None
            if bore_ember and math.cos(psi) < -0.2:
                c = M._centroid(quad)
                warm = M.clamp((-c[1] + 10.0) / 110.0) ** 1.5
                deep = M.clamp((-math.cos(psi) - 0.2) / 0.8)
                k = warm * deep * 0.65
                emi = M.cscale(M.C_EMBER, k)
            jit = 0.06 + 0.05 * math.sin(i * 2.7 + j * 1.9)
            m.poly(quad, a, alpha=alpha, jitter=jit, outward=ctr, emissive=emi,
                   tag='shell')


def add_crest(m, glow=1.0):
    """dorsal heat organ: a ridge of crystal shards along the upper arch."""
    shards = [(0.55, 34, 15), (0.80, 46, 19), (1.05, 54, 21), (1.57, 58, 22),
              (2.05, 50, 19), (2.30, 40, 16)]
    for i, (phi, ln, wd) in enumerate(shards):
        e = evec(phi)
        lean = -0.35 + 0.13 * i
        base = M.vmul(e, RF(phi) - 4.0)
        d = M.vnorm(M.vadd(M.vmul(e, 0.55),
                           M.vadd(M.vmul(N, 0.30 + 0.10 * (i - 2)),
                                  (0.0, 0.78, 0.0))))
        d = M.vnorm(M.vadd(d, M.vmul(M.vcross(N, e), lean * 0.5)))
        tip = M.vadd(base, M.vmul(d, ln))
        side = M.vnorm(M.vcross(d, N))
        if M.vlen(side) < 0.3:
            side = M.vnorm(M.vcross(d, (0.0, 0.0, 1.0)))
        n2 = M.vnorm(M.vcross(side, d))
        hot = M.cmix(M.rgb('#ff7a24'), M.rgb('#ffe7ba'), 0.25 + 0.35 * glow)
        base_col = M.rgb('#4c3a28')
        for f in range(6):
            a1 = TAU * f / 6 + 0.3
            a2 = TAU * (f + 1) / 6 + 0.3
            p1 = M.vadd(base, M.vadd(M.vmul(side, math.cos(a1) * wd),
                                     M.vmul(n2, math.sin(a1) * wd * 0.30)))
            p2 = M.vadd(base, M.vadd(M.vmul(side, math.cos(a2) * wd),
                                     M.vmul(n2, math.sin(a2) * wd * 0.30)))
            q1 = M.vlerp(p1, tip, 0.62)
            q2 = M.vlerp(p2, tip, 0.62)
            m2 = M.vlerp(M.vlerp(p1, p2, 0.5), tip, 0.84)
            hotf = 0.25 + 0.75 * M.clamp((f % 3) / 2.0)
            col = M.cmix(base_col, hot, 0.30 + 0.45 * hotf)
            m.poly([p1, p2, q2, q1], col, kind='emit', tag='crest')
            m.poly([q1, q2, m2], M.cmix(col, hot, 0.7), kind='emit', tag='crest')
            m.poly([p1, M.vlerp(p1, p2, 0.5), m2, q1],
                   M.cmix(col, hot, 0.9), kind='emit', tag='crest')
            m.poly([M.vlerp(p1, p2, 0.5), p2, q2, m2],
                   M.cmix(col, M.rgb('#241608'), 0.45), kind='emit', tag='crest')
        M.ellipsoid(m, M.vadd(base, M.vmul(d, -1)), (wd * 1.3, wd * 0.6, wd * 1.1),
                    7, 3, albedo=M.C_STONE_M, tag='crest-base')


def add_maw(m, c, nrm, rad=12.0, glow=1.0, up=(0.0, 0.0, -1.0)):
    """feeding opening: raised mineral lip around a funnel throat."""
    nrm = M.vnorm(nrm)
    t1 = M.vnorm(M.vcross(nrm, up))
    t2 = M.vnorm(M.vcross(t1, nrm))
    seg = 16
    A, B, C, D = rad * 1.80, rad * 1.22, rad * 0.84, rad * 0.36
    hA, hB, hC, hD = 0.4, 4.6, 1.4, -0.6

    def rk(r, h):
        return [M.vadd(c, M.vadd(M.vadd(M.vmul(t1, math.cos(TAU * k / seg) * r),
                                        M.vmul(t2, math.sin(TAU * k / seg) * r)),
                                 M.vmul(nrm, h))) for k in range(seg)]
    rA, rB, rC, rD = rk(A, hA), rk(B, hB), rk(C, hC), rk(D, hD)
    ref = M.vadd(c, M.vmul(nrm, -2.0))
    for k in range(seg):
        k2 = (k + 1) % seg
        m.poly([rA[k], rA[k2], rB[k2], rB[k]], M.C_STONE_M, jitter=0.04,
               outward=ref, tag='maw')
        m.poly([rB[k], rB[k2], rC[k2], rC[k]], M.C_STONE_D, jitter=0.05,
               outward=ref, tag='maw')
        m.poly([rC[k], rC[k2], rD[k2], rD[k]], M.rgb('#2a1c13'), jitter=0.02,
               kind='flat', tag='maw')
    m.poly(rD, M.cmix(M.rgb('#1a1008'), M.C_HOT_ROCK, 0.7), kind='flat', tag='maw')
    m.poly(rD, M.cscale(M.C_EMBER, 0.5 * glow), kind='emit', alpha=0.4,
           tag='maw-glow')


def add_ribs(m, phi0, phi1, count=14, out=8.5):
    """vibration plate: fan of lamellae on the outer rim (left flank)."""
    for k in range(count):
        phi = phi0 + (phi1 - phi0) * k / (count - 1)
        e = evec(phi)
        tan = M.vnorm(M.vcross(N, e))
        base = M.vmul(e, RF(phi) - 1.5)
        w = 1.7
        for s in (-1, 1):
            a = M.vadd(base, M.vadd(M.vmul(N, s * 9.0), M.vmul(tan, -w)))
            b = M.vadd(base, M.vadd(M.vmul(N, s * 9.0), M.vmul(tan, w)))
            c2 = M.vadd(base, M.vadd(M.vmul(N, s * 3.0), M.vmul(tan, w * 0.8)))
            d2 = M.vadd(base, M.vadd(M.vmul(N, s * 3.0), M.vmul(tan, -w * 0.8)))
            top = M.vadd(base, M.vmul(e, out))
            m.poly([a, b, c2, d2], M.C_STONE_L, jitter=0.03, tag='rib')
            m.poly([a, b, top], M.C_STONE_L, jitter=0.03, tag='rib')


MUZZLE_C = (0.0, -104.0, 82.0)


def add_muzzle(m, albedo=None):
    albedo = albedo or M.C_STONE_D
    c = MUZZLE_C
    # main mass: swept blob projecting forward
    M.ellipsoid(m, c, (54.0, 36.0, 40.0), 16, 8, albedo=albedo, tag='muzzle')
    M.ellipsoid(m, (0.0, -88.0, 52.0), (62.0, 30.0, 30.0), 16, 6,
                albedo=albedo, tag='muzzle')
    # lip ridge around the plate
    for k in range(18):
        a1 = TAU * k / 18
        a2 = TAU * (k + 1) / 18
        p1 = M.vadd(c, (math.cos(a1) * 50.0, math.sin(a1) * 30.0, -26.0))
        p2 = M.vadd(c, (math.cos(a2) * 50.0, math.sin(a2) * 30.0, -26.0))
        p3 = M.vadd(c, (math.cos(a2) * 46.0, math.sin(a2) * 26.0, -12.0))
        p4 = M.vadd(c, (math.cos(a1) * 46.0, math.sin(a1) * 26.0, -12.0))
        m.poly([p1, p2, p3, p4], M.C_STONE_M, jitter=0.05, tag='muzzle-lip')
    return c


# --------------------------------------------------------------------- limbs
def ik2(root, target, l1, l2, pole):
    d = M.vsub(target, root)
    dist = M.vlen(d)
    dist = min(max(dist, 1e-3), (l1 + l2) * 0.995)
    u = M.vnorm(d)
    cos_a = (l1 * l1 + dist * dist - l2 * l2) / (2 * l1 * dist)
    a = math.acos(max(-1.0, min(1.0, cos_a)))
    p = M.vsub(pole, M.vmul(u, M.vdot(pole, u)))
    if M.vlen(p) < 1e-4:
        p = M.vcross(u, (0.0, 0.0, 1.0))
    p = M.vnorm(p)
    joint = M.vadd(root, M.vmul(M.vadd(M.vmul(u, math.cos(a)),
                                       M.vmul(p, math.sin(a))), l1))
    end = M.vadd(root, M.vmul(u, dist))
    return joint, end


def limb(m, root, target, l1, l2, r0_, r1_, r2_, pole, albedo=None,
         foot=None, claws=0, claw_len=14.0, tag='limb', knuckle=1.12):
    albedo = albedo or M.C_STONE
    joint, end = ik2(root, target, l1, l2, pole)
    # upper segment
    M.tube(m, [root, M.vlerp(root, joint, 0.5), joint], [r0_, r0_ * 1.06, r0_ * 0.94],
           sides=8, albedo=albedo, cap_start=True, cap_end=False, tag=tag)
    if knuckle > 0:
        M.ellipsoid(m, joint, (r0_ * knuckle, r0_ * knuckle, r0_ * knuckle), 9, 5,
                    albedo=albedo, tag=tag, jitter=0.10)
    # lower segment
    M.tube(m, [joint, M.vlerp(joint, end, 0.55), end],
           [r0_ * 0.94, r1_, r2_], sides=8, albedo=albedo, cap_start=False,
           cap_end=True, tag=tag)
    if foot:
        M.ellipsoid(m, end, foot, 10, 5, albedo=albedo, tag=tag + '-pad')
    if claws:
        side = M.vnorm(M.vcross(M.vsub(end, joint), (0.0, 1.0, 0.0)))
        fwd = M.vnorm(M.vsub(end, joint))
        for k in range(claws):
            ang = (k - (claws - 1) / 2.0) * 0.55
            dirv = M.vnorm(M.vadd(M.vmul(side, math.sin(ang)),
                                  M.vmul(M.vcross(side, fwd), 0.0)))
            out = M.vnorm(M.vadd(fwd, M.vmul(side, math.sin(ang) * 1.4)))
            tip = M.vadd(end, M.vmul(out, claw_len))
            M.tube(m, [end, M.vlerp(end, tip, 0.6), tip],
                   [r2_ * 0.9, r2_ * 0.55, r2_ * 0.12], sides=5, albedo=albedo,
                   cap_start=False, cap_end=True, tag=tag)
    return joint, end


LEG_HIPS = {'L': math.radians(-124.0), 'R': math.radians(-56.0)}
ARM_SH = {'L': math.radians(205.0), 'R': math.radians(-25.0)}


def limb_roots():
    hips = {}
    for k, phi in LEG_HIPS.items():
        e = evec(phi)
        hips[k] = M.vadd(M.vmul(e, RF(phi) - 4.0), M.vmul(N, 5.0))
    shs = {}
    for k, phi in ARM_SH.items():
        e = evec(phi)
        shs[k] = M.vadd(M.vmul(e, RF(phi) - 6.0), M.vmul(N, 6.0))
    return hips, shs


def add_limbs(m, pose):
    hips, shs = limb_roots()
    s = pose.get('scale', 1.0)
    for key, hip in hips.items():
        tgt = pose['feet'][key]
        limb(m, hip, tgt, LEG_L[0] * s, LEG_L[1] * s, 20.0, 14.0, 11.0,
             pose.get('leg_pole', M.vnorm((0.0, 0.0, 1.0))),
             albedo=M.C_STONE, foot=(15.0, 7.0, 25.0), tag='leg-' + key,
             knuckle=1.02)
    for key, sh in shs.items():
        hand = pose['hands'][key]
        limb(m, sh, hand, ARM_L[0] * s, ARM_L[1] * s, 16.5, 11.5, 8.4,
             pose.get('arm_pole', M.vnorm((math.copysign(0.6, sh[0]), -0.2, 0.6))),
             albedo=M.C_STONE, claws=3, claw_len=13.0, tag='arm-' + key,
             knuckle=1.02)


# --------------------------------------------------------------------- build
def make_xf(pose):
    off = pose.get('body_off', (0.0, 0.0, 0.0))
    rot = pose.get('body_rot', ((1.0, 0.0, 0.0), 0.0))
    axis, ang = rot

    def xf(p):
        q = p
        if ang:
            q = M.rot_axis(q, axis, ang)
        return M.vadd(q, off)
    return xf


def rest_pose():
    return {
        'feet': {'L': (-80.0, GROUND + 10.0, 118.0), 'R': (86.0, GROUND + 8.0, -8.0)},
        'hands': {'L': (-98.0, -76.0, 116.0), 'R': (100.0, -72.0, 122.0)},
        'leg_pole': M.vnorm((0.10, 0.0, 1.0)),
        'arm_pole': M.vnorm((0.6, -0.30, 0.6)),
        'body_rot': (M.vnorm((0.0, 0.0, 1.0)), -0.055),
    }


def build(pose=None, shell_kw=None, crest_glow=1.0):
    pose = dict(rest_pose(), **(pose or {}))
    xf = make_xf(pose)
    body = M.Model()
    add_shell(body, **(shell_kw or {}))
    add_crest(body, glow=crest_glow)
    for phi, rad, tilt in ((-58.0, 12.0, -0.30), (-90.0, 14.0, -0.50),
                           (-122.0, 12.0, -0.30)):
        e = evec(math.radians(phi))
        c = face_pt(math.radians(phi), 0.52, ax=tF(math.radians(phi)) + 0.5)
        nrm = M.vnorm(M.vadd(M.vmul(N, 1.0), M.vmul(V, tilt)))
        add_maw(body, c, nrm, rad=rad)
    add_ribs(body, math.radians(-78.0), math.radians(-24.0))
    out = M.Model()
    for f in body.faces:
        f = dict(f)
        f['p'] = [xf(p) for p in f['p']]
        out.faces.append(f)
    # limbs are built in world space at the transformed roots
    hips, shs = limb_roots()
    for k in hips:
        hips[k] = xf(hips[k])
    for k in shs:
        shs[k] = xf(shs[k])
    s = pose.get('scale', 1.0)
    for key, hip in hips.items():
        limb(out, hip, pose['feet'][key], LEG_L[0] * s, LEG_L[1] * s, 20.0, 14.0, 11.0,
             pose.get('leg_pole', M.vnorm((0.0, 0.0, 1.0))),
             albedo=M.C_STONE, foot=(15.0, 7.0, 25.0), tag='leg-' + key,
             knuckle=1.02)
    for key, sh in shs.items():
        limb(out, sh, pose['hands'][key], ARM_L[0] * s, ARM_L[1] * s, 16.5, 11.5, 8.4,
             M.vnorm((math.copysign(1.0, sh[0]), -0.15, 0.10)),
             albedo=M.C_STONE, claws=3, claw_len=13.0, tag='arm-' + key,
             knuckle=1.02)
    return out
