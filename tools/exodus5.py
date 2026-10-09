"""Generators and faces for Exodus Book Five (the glory): the two tables of stone, the golden calf, gold rings and
the melting pot, broken tables, the tabernacle, rays of glory, and new faces (Aaron afraid, Moses shining)."""
import math, random
import mk, exodus as E, exodus2 as X, exodus4 as Z, egypt
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = Z.tokens()
    t["__FACE_AARON_FEAR__"] = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#9A968E", hl="#6A665E", beard=True, scarf="#4A6A9A", cord=True, brow="sorrow", sweat=True)
    t["__FACE_MOSES_SHINE__"] = F("adam", skin="#F0C29E", shadow="#C98E66", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#F3EFE6", cord=True, light="#FFFFFF")
    return t

def rays(cx, cy, n, r0, r1, color="#FFF4C2", op=0.8, w=10):
    o = []
    for i in range(n):
        a = 2 * math.pi * i / n; b = a + math.pi / n * 0.5
        o.append(f'<path d="M{f(cx + r0*math.cos(a))} {f(cy + r0*math.sin(a))} L {f(cx + r1*math.cos(a - 0.04))} {f(cy + r1*math.sin(a - 0.04))} L {f(cx + r1*math.cos(b))} {f(cy + r1*math.sin(b))} Z" fill="{color}" opacity="{op}"></path>')
    return "".join(o)

def tables(x, y, s=1.0, uid="tb", glow=True, rot=0):
    """The two tables of the testimony: rounded-top stone slabs with carved lines, side by side."""
    r = random.Random(5)
    def slab(dx):
        lines = []
        for row in range(8):
            yy = -150 + row * 17; xx = dx - 40
            while xx < dx + 34:
                ln = r.uniform(6, 16)
                lines.append(f'<path d="M{f(xx)} {f(yy)} L {f(xx + ln)} {f(yy)}" stroke="#4A4A5A" stroke-width="3" stroke-linecap="round"></path>')
                xx += ln + r.uniform(3, 7)
        return (f'<path d="M{dx-48} 0 L {dx-48} -150 C {dx-48} -186 {dx+48} -186 {dx+48} -150 L {dx+48} 0 Z" fill="url(#{uid}S)" stroke="#0D0D0F" stroke-width="3"></path>'
                + "".join(lines))
    g = (f'<defs><linearGradient id="{uid}S" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E8E2D6"></stop><stop offset="1" stop-color="#9A968E"></stop></linearGradient></defs>')
    halo = f'<ellipse cx="0" cy="-90" rx="150" ry="140" fill="#FFE680" opacity="0.35"></ellipse>' if glow else ""
    return f'{g}<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">{halo}{slab(-52)}{slab(52)}</g>'

def shards(x, y, s, seed):
    r = random.Random(seed); o = []
    for _ in range(14):
        cx, cy = r.uniform(-120, 120), r.uniform(-60, 20); k = r.uniform(12, 34); a = r.uniform(0, 6.28)
        pts = [(cx + k * math.cos(a + t) * r.uniform(0.6, 1.1), cy + k * math.sin(a + t) * r.uniform(0.6, 1.1)) for t in (0, 2.0, 3.6, 5.0)]
        o.append('<path d="M' + " L ".join(f"{f(px)} {f(py)}" for px, py in pts) + ' Z" fill="#C8C2B6" stroke="#0D0D0F" stroke-width="2"></path>')
        o.append(f'<path d="M{f(pts[0][0])} {f(pts[0][1])} L {f(pts[2][0])} {f(pts[2][1])}" stroke="#4A4A5A" stroke-width="2"></path>')
    for _ in range(30):
        o.append(f'<circle cx="{f(r.uniform(-150, 150))}" cy="{f(r.uniform(-80, 30))}" r="{f(r.uniform(1.5, 4))}" fill="#E8E2D6"></circle>')
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + "".join(o) + '</g>'

def calf(x, y, s=1.0, uid="cf", pedestal=True, flip=True):
    """The molten calf: a gold young bull on a stepped pedestal; (x, y) is the bottom of the pedestal."""
    sx = -s if flip else s
    base = 122 if pedestal else 68
    ped = ('<path d="M-20 68 L 144 68 L 136 94 L -12 94 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
           '<path d="M-36 94 L 160 94 L 152 122 L -28 122 Z" fill="#6B4A22" stroke="#0D0D0F" stroke-width="2.4"></path>') if pedestal else ""
    ox = 124 if flip else 0
    return (f'<defs><linearGradient id="{uid}G" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.35" stop-color="#FFD23F"></stop>'
            f'<stop offset="0.7" stop-color="#E8A317"></stop><stop offset="1" stop-color="#8A5A10"></stop></linearGradient></defs>'
            f'<g transform="translate({f(x)} {f(y - base*s)}) scale({f(sx)} {f(s)}) translate(-62 0)">{ped}'
            f'<path d="{egypt.FAT}" fill="url(#{uid}G)" stroke="#0D0D0F" stroke-width="2.6"></path>'
            '<path d="M24 2 C 18 -10 10 -14 4 -12 M30 -6 C 34 -18 40 -22 46 -20" fill="none" stroke="#FFF4C2" stroke-width="4" stroke-linecap="round"></path>'
            '<path d="M24 2 C 18 -10 10 -14 4 -12 M30 -6 C 34 -18 40 -22 46 -20" fill="none" stroke="#0D0D0F" stroke-width="1.2" stroke-linecap="round" opacity="0.6"></path>'
            '<path d="M40 8 C 70 0 100 4 112 14" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.8"></path>'
            '<circle cx="14" cy="12" r="2.6" fill="#0D0D0F"></circle></g>')

def rings(x, y, n, seed, spread=60):
    r = random.Random(seed)
    return "".join(f'<ellipse cx="{f(x + r.uniform(-spread, spread))}" cy="{f(y + r.uniform(-spread*0.3, spread*0.3))}" rx="{f(r.uniform(5, 9))}" ry="{f(r.uniform(3, 6))}" fill="none" stroke="#FFD23F" stroke-width="3"></ellipse>' for _ in range(n))

def tabernacle(x, y, w, uid="tn"):
    """The tabernacle in its court: a white linen fence on posts, and the tent covered in red-dyed rams' skins."""
    h = w * 0.36; posts = 12
    o = [f'<rect x="{f(x - w/2)}" y="{f(y - h*0.32)}" width="{f(w)}" height="{f(h*0.32)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></rect>']
    for i in range(posts + 1):
        px = x - w / 2 + w * i / posts
        o.append(f'<path d="M{f(px)} {f(y)} L {f(px)} {f(y - h*0.36)}" stroke="#8A5A30" stroke-width="3"></path>')
    o.append(f'<rect x="{f(x - w*0.08)}" y="{f(y - h*0.32)}" width="{f(w*0.16)}" height="{f(h*0.32)}" fill="url(#{uid}Gate)" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.insert(0, f'<defs><pattern id="{uid}Gate" width="12" height="40" patternUnits="userSpaceOnUse"><rect width="4" height="40" fill="#1F5FAD"></rect><rect x="4" width="4" height="40" fill="#7A3BA8"></rect><rect x="8" width="4" height="40" fill="#D7261E"></rect></pattern></defs>')
    tx, ty, tw, th = x + w * 0.12, y - h * 0.3, w * 0.42, h * 0.62
    o.insert(1, f'<path d="M{f(tx - tw/2)} {f(ty)} L {f(tx - tw/2)} {f(ty - th*0.7)} L {f(tx - tw*0.4)} {f(ty - th)} L {f(tx + tw*0.4)} {f(ty - th)} L {f(tx + tw/2)} {f(ty - th*0.7)} L {f(tx + tw/2)} {f(ty)} Z" fill="#8A1A1A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                f'<path d="M{f(tx - tw*0.4)} {f(ty - th)} L {f(tx + tw*0.4)} {f(ty - th)} L {f(tx + tw/2)} {f(ty - th*0.7)} L {f(tx - tw/2)} {f(ty - th*0.7)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
                f'<rect x="{f(tx - tw*0.12)}" y="{f(ty - th*0.62)}" width="{f(tw*0.24)}" height="{f(th*0.62)}" fill="url(#{uid}Gate)" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.insert(1, f'<path d="M{f(x - w*0.3)} {f(y - h*0.36)} L {f(x - w*0.3)} {f(y - h*0.5)} L {f(x - w*0.2)} {f(y - h*0.5)} L {f(x - w*0.2)} {f(y - h*0.36)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)
