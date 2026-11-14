from math import cos, sin, radians
from pathlib import Path
from xml.etree import ElementTree as ET

OUT = Path(__file__).parent
TAU = 360
BODY = "M256 64 C236 65 221 86 218 111 C213 125 211 136 210 143 C194 159 190 204 192 248 C193 273 200 298 211 307 C214 339 222 369 230 403 C236 429 246 444 256 448 C266 444 276 429 282 403 C290 369 298 339 301 307 C312 298 319 273 320 248 C322 204 318 159 302 143 C301 136 299 125 294 111 C291 86 276 65 256 64 Z"
DEFS = '''<defs><linearGradient id="skin" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#254b72"/><stop offset=".43" stop-color="#359c9b"/><stop offset=".75" stop-color="#6d6aa8"/><stop offset="1" stop-color="#172d5e"/></linearGradient><linearGradient id="limb" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#66c4ae"/><stop offset="1" stop-color="#3b5d9b"/></linearGradient><radialGradient id="glow"><stop stop-color="#f5fff1"/><stop offset=".42" stop-color="#b0f7dd"/><stop offset="1" stop-color="#3a9fd0"/></radialGradient><clipPath id="bodyClip"><path d="'''+BODY+'''"/></clipPath></defs>'''

def f(v): return f"{v:.1f}"

def point(r, a, cx=256, cy=256):
    a=radians(a)
    return cx+r*cos(a),cy+r*sin(a)

def circle(x,y,r,fill,stroke='none',sw=0,other=''):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {other}/>'

def side_projection(r,a,az):
    d=radians(a-az)
    # All appendages curve clockwise in their own radial plane.
    return 256+r*cos(d)-0.14*max(0,r-58)*sin(d)

def limb_side(a,az,near):
    xs=[side_projection(r,a,az) for r in (55,95,150,210)]
    path=f'M{f(xs[0])} 234 C{f(xs[1])} 231 {f(xs[2])} 248 {f(xs[3])} 259'
    color='#91e8c4' if near else '#3b668d'
    opacity='.95' if near else '.55'
    return f'<path data-part="limb" d="{path}" fill="none" stroke="{color}" stroke-width="7" stroke-linecap="round" opacity="{opacity}"/>'+circle(xs[3],259,5.5,'#a8e5c5','#1a537c',1.8)

def side_organs(az):
    s=[]
    # Surface organs on rings. Back-facing marks exist but are occluded by body.
    for a in (0,90,180,270):
        d=radians(a-az)
        if sin(d)>=-.03:
            x=side_projection(28,a,az)
            s.append(f'<ellipse data-part="eye" cx="{f(x)}" cy="104" rx="6.2" ry="8.3" fill="#0a2144" stroke="#b4e5dc" stroke-width="2"/>')
    for a in (45,135,225,315):
        d=radians(a-az)
        if sin(d)>=.05:
            x=side_projection(35,a,az)
            s.append(circle(x,132,3.7,'#081d3c','#a8d0ca',1.3,'data-part="sensory-pit"'))
    for a in range(0,360,60):
        d=radians(a-az)
        if sin(d)>=-.03:
            x=side_projection(54,a,az)
            s.append(f'<ellipse data-part="light-organ" cx="{f(x)}" cy="274" rx="7" ry="10" fill="url(#glow)" stroke="#216c94" stroke-width="1.4"/>')
    for a in (0,90,180,270):
        d=radians(a-az)
        if sin(d)>=-.03:
            x=side_projection(37,a,az)
            s.append(f'<path data-part="gill-opening" d="M{f(x-6)} 350 q6 8 12 0" fill="none" stroke="#102750" stroke-width="4" stroke-linecap="round"/>')
    return ''.join(s)

def occluded_side_organs(az):
    # Draw far-side features before the opaque body, so the complete anatomy is
    # retained in each SVG without showing through the cuticle.
    s=[]
    for a in (0,90,180,270):
        d=radians(a-az)
        if sin(d)<-.03:
            x=side_projection(28,a,az)
            s.append(f'<ellipse data-part="eye" cx="{f(x)}" cy="104" rx="6.2" ry="8.3" fill="#0a2144"/>')
            x=side_projection(37,a,az)
            s.append(f'<path data-part="gill-opening" d="M{f(x-6)} 350 q6 8 12 0" fill="none" stroke="#102750" stroke-width="4"/>')
    for a in (45,135,225,315):
        if sin(radians(a-az))<.05:
            x=side_projection(35,a,az)
            s.append(circle(x,132,3.7,'#081d3c',other='data-part="sensory-pit"'))
    for a in range(0,360,60):
        if sin(radians(a-az))<-.03:
            x=side_projection(54,a,az)
            s.append(circle(x,274,7,'url(#glow)',other='data-part="light-organ"'))
    for x in (246,256,266):
        s.append(f'<ellipse data-part="feeding-opening" cx="{x}" cy="75" rx="3" ry="5" fill="#0a1f43"/>')
    return ''.join(s)

def side(az):
    far=[]; near=[]
    for a in range(0,360,60):
        (near if sin(radians(a-az))>=0 else far).append(limb_side(a,az,sin(radians(a-az))>=0))
    p=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">',DEFS]
    p+=far
    p.append(occluded_side_organs(az))
    p.append(f'<path d="{BODY}" fill="url(#skin)" stroke="#142b55" stroke-width="4"/>')
    p.append('<g clip-path="url(#bodyClip)"><path d="M184 142 H328 V306 H184Z" fill="#54b69f" opacity=".19"/><path d="M200 306 H312 V454 H200Z" fill="#44558e" opacity=".24"/>')
    # Eight transverse units: two crown, three thorax, three abdomen.
    for y,rx in ((106,38),(142,46),(194,61),(250,64),(306,46),(354,36),(400,27)):
        thick=3.8 if y in (142,306) else 1.9
        p.append(f'<path d="M{256-rx} {y} Q256 {y+13} {256+rx} {y}" fill="none" stroke="#b5e6d2" stroke-width="{thick}" opacity=".63"/>')
    # Open fluid lacunae are broad translucent spaces, not vessels.
    p.append('<path d="M237 175 C230 205 232 266 244 294 M275 175 C282 205 280 266 268 294" fill="none" stroke="#d2f3cf" stroke-width="13" stroke-linecap="round" opacity=".24"/>')
    p.append('<path d="M231 326 Q256 309 281 326 L276 418 Q256 440 236 418Z" fill="#79acc4" fill-opacity=".18" stroke="#b5d9d4" stroke-width="2" opacity=".8"/>')
    p.append('</g>')
    p+=near
    p.append(side_organs(az))
    # Small visible section of the filament trap between limb tips.
    p.append('<path d="M52 259 Q256 282 460 259" fill="none" stroke="#c7f5df" stroke-width="1.4" opacity=".65"/>')
    p.append('</svg>')
    return ''.join(p)

def radial_limb(a):
    x0,y0=point(57,a);x1,y1=point(105,a+4);x2,y2=point(161,a+8);x3,y3=point(210,a+8)
    return f'<path data-part="limb" d="M{f(x0)} {f(y0)} Q{f(x1)} {f(y1)} {f(x2)} {f(y2)} T{f(x3)} {f(y3)}" fill="none" stroke="url(#limb)" stroke-width="8" stroke-linecap="round"/>'+circle(x3,y3,5.5,'#a8e5c5','#1a537c',1.8)

def axial(which):
    top=which=='top'; p=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">',DEFS]
    # Radial silk trap is a filament ring supported by the six limb cups.
    coords=[point(210,a+8) for a in range(0,360,60)]
    pts=' '.join(f'{f(x)},{f(y)}' for x,y in coords)
    p.append(f'<polygon points="{pts}" fill="none" stroke="#a5dcca" stroke-width="1.4" opacity=".7"/>')
    for a in range(0,360,60): p.append(radial_limb(a))
    if top:
        for a in (0,90,180,270):
            x,y=point(36,a)
            p.append(circle(x,y,3,'#102750',other='data-part="gill-opening"'))
    else:
        for a in (0,90,180,270):
            x,y=point(36,a)
            p.append(circle(x,y,6.5,'#091e40',other='data-part="eye"'))
        for a in (45,135,225,315):
            x,y=point(40,a)
            p.append(circle(x,y,3.4,'#081d3c',other='data-part="sensory-pit"'))
        for a in (30,150,270):
            x,y=point(16,a)
            p.append(circle(x,y,5,'#0a1f43',other='data-part="feeding-opening"'))
    p.append(circle(256,256,64,'url(#skin)','#142b55',3))
    # Six light organs in a ring at the limb angles.
    for a in range(0,360,60):
        x,y=point(55,a)
        p.append(circle(x,y,7,'url(#glow)','#287b9e',1.3,'data-part="light-organ"'))
    if top:
        p.append(circle(256,256,43,'#368c9c','#b3e2d0',3))
        p.append(circle(256,256,30,'#286a91','#9fd5d5',1.5))
        for a in (0,90,180,270):
            x,y=point(36,a)
            p.append(circle(x,y,6.5,'#091e40','#c0e9e2',2,'data-part="eye"'))
        for a in (45,135,225,315):
            x,y=point(40,a)
            p.append(circle(x,y,3.4,'#081d3c','#9fcdca',1,'data-part="sensory-pit"'))
        for a in (30,150,270):
            x,y=point(16,a)
            p.append(f'<ellipse data-part="feeding-opening" cx="{f(x)}" cy="{f(y)}" rx="5" ry="8" transform="rotate({a+90} {f(x)} {f(y)})" fill="#0a1f43" stroke="#a8d9d8" stroke-width="1.5"/>')
        p.append(circle(256,256,5,'#c5e6ce'))
    else:
        p.append(circle(256,256,44,'#5d709b','#b4d8d0',2))
        p.append(circle(256,256,31,'#4c739a','#a3d6cf',2))
        p.append(circle(256,256,20,'#7ca6b2','#d0e8d9',2))
        for a in (0,90,180,270):
            x,y=point(36,a)
            p.append(f'<path data-part="gill-opening" d="M{f(x-5)} {f(y-4)} q5 8 10 0" fill="none" stroke="#102750" stroke-width="4" stroke-linecap="round" transform="rotate({a+90} {f(x)} {f(y)})"/>')
    p.append('</svg>')
    return ''.join(p)

def main():
    views={'creature':side(25).replace('viewBox="0 0 512 512"', 'viewBox="0 0 512 512" id="cyst-weaver-24m"', 1),'front':side(0),'back':side(180),'left':side(90),'right':side(270),'top':axial('top'),'bottom':axial('bottom')}
    for name,svg in views.items():
        ET.fromstring(svg)
        assert len(svg.encode())<512_000
        (OUT/f'{name}.svg').write_text(svg+'\n')
        print(f'{name}.svg {len(svg.encode())} bytes')

if __name__=='__main__': main()
