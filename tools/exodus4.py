"""Generators and faces for Exodus Book Four (the wilderness and Sinai): quails, manna, tents, the smitten rock,
both-arms-raised figures, warriors, Mount Sinai on fire, and new faces (Joshua, an Israelite woman)."""
import math, random
import mk, exodus as E, exodus2 as X, exodus3 as Y
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = Y.tokens()
    t["__FACE_JOSHUA__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#2A1A10", hl="#5A4A3E", brow="scowl", stubble="#2A1A10", light="#FF8A3D")
    t["__FACE_WOMAN__"] = F("eve", skin="#D9A27A", shadow="#9A6A4A", hair="#2A1A10", scarf="#7A3BA8")
    t["__FACE_WOMAN_FEAR__"] = F("eve", skin="#C9967A", shadow="#6A4A5A", hair="#2A1A10", scarf="#7A3BA8", brow="sorrow", sweat=True)
    return t

# both arms free (Moses holding up his hands)
MAN_BOTH = mk.MAN_UP.replace("L 22 -142 L 24 -122 L 25 -98 C 24 -90 25 -84 28 -84 C 31 -84 33 -90 32 -98 L 31 -122 L 29 -146 C 29 -152 28 -159 24 -162", "C 20 -150 22 -158 24 -162")
assert MAN_BOTH != mk.MAN_UP

def figure_both(x, y, s, body, cloth, left, right, uid, stroke="#0D0D0F"):
    """A robed man with both arms raised: left/right are point lists from each shoulder (local units)."""
    return (f'<defs><path id="{uid}B" d="{MAN_BOTH}"></path><path id="{uid}R" d="{mk.ROBE}"></path></defs>'
            f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" fill="{body}"><use href="#{uid}B"></use>'
            f'<use href="#{uid}R" fill="{cloth}" stroke="{stroke}" stroke-width="3"></use>'
            + mk.arm(left, body, 10) + mk.arm(right, body, 10) + '</g>')

def quail(x, y, s=1.0, flip=False, flying=True):
    sx = -s if flip else s
    wing = ('<path d="M-4 -10 C -10 -30 -26 -36 -34 -30 C -24 -24 -14 -16 -8 -6 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.4"></path>' if flying
            else '<path d="M-14 -10 C -4 -14 8 -12 12 -4 C 2 -2 -8 -4 -14 -10 Z" fill="#6B4A2A"></path>')
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-18 -6 C -16 -16 0 -18 10 -14 C 16 -18 22 -16 22 -10 L 28 -8 L 22 -6 C 20 0 8 4 -6 2 C -14 0 -18 -2 -18 -6 Z" fill="#A8845A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<g fill="#F3EFE6"><circle cx="-8" cy="-6" r="1.2"></circle><circle cx="-2" cy="-4" r="1.2"></circle><circle cx="4" cy="-6" r="1.2"></circle></g>'
            '<circle cx="18" cy="-11" r="1.6" fill="#0D0D0F"></circle><path d="M14 -16 C 16 -22 20 -22 20 -18" fill="none" stroke="#3A2214" stroke-width="1.4"></path>'
            + wing + '</g>')

def quails(n, x0, x1, y0, y1, seed, smin=0.4, smax=1.0, flying=True):
    r = random.Random(seed)
    return "".join(quail(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(smin, smax), r.random() < 0.3, flying) for _ in range(n))

def manna(n, x0, x1, y0, y1, seed):
    r = random.Random(seed); o = []
    for _ in range(n):
        y = r.uniform(y0, y1); k = (y - y0) / max(1, (y1 - y0)); rr = 1.2 + 3.2 * k
        x = r.uniform(x0, x1)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr)}" ry="{f(rr*0.7)}" fill="#F8F6F0" stroke="#B8B2A6" stroke-width="0.6"></ellipse>')
    return "".join(o)

def tent(x, y, w, h, color="#5A3A22", stripe="#2A1A10"):
    return (f'<path d="M{f(x-w/2)} {f(y)} L {f(x)} {f(y-h)} L {f(x+w/2)} {f(y)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M{f(x-w*0.25)} {f(y-h*0.5)} L {f(x+w*0.25)} {f(y-h*0.5)}" stroke="{stripe}" stroke-width="3"></path>'
            f'<path d="M{f(x)} {f(y-h)} L {f(x-w*0.1)} {f(y)} L {f(x+w*0.1)} {f(y)} Z" fill="#12090A"></path>')

def basket(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-16 -14 L 16 -14 L 12 0 L -12 0 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-14 -9 L 14 -9 M-13 -4 L 13 -4" stroke="#8A6A3A" stroke-width="1.2"></path><g fill="#F8F6F0"><circle cx="-6" cy="-15" r="2.4"></circle><circle cx="0" cy="-16" r="2.4"></circle><circle cx="6" cy="-15" r="2.4"></circle></g></g>')

def rock(x, y, w, h, color="#8A6A5A", dark="#4A3A3A"):
    return (f'<path d="M{f(x)} {f(y)} C {f(x+w*0.05)} {f(y-h*0.6)} {f(x+w*0.25)} {f(y-h)} {f(x+w*0.55)} {f(y-h*0.95)} C {f(x+w*0.85)} {f(y-h*0.9)} {f(x+w)} {f(y-h*0.5)} {f(x+w)} {f(y)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<path d="M{f(x+w*0.55)} {f(y-h*0.95)} C {f(x+w*0.85)} {f(y-h*0.9)} {f(x+w)} {f(y-h*0.5)} {f(x+w)} {f(y)} L {f(x+w*0.7)} {f(y)} C {f(x+w*0.75)} {f(y-h*0.5)} {f(x+w*0.7)} {f(y-h*0.8)} {f(x+w*0.55)} {f(y-h*0.95)} Z" fill="{dark}" opacity="0.6"></path>'
            f'<g fill="none" stroke="#3A2A2A" stroke-width="1.6"><path d="M{f(x+w*0.2)} {f(y-h*0.6)} L {f(x+w*0.35)} {f(y-h*0.45)} L {f(x+w*0.3)} {f(y-h*0.2)}"></path><path d="M{f(x+w*0.5)} {f(y-h*0.8)} L {f(x+w*0.6)} {f(y-h*0.6)}"></path></g>')

def gush(x, y, seed, scale=1.0):
    """Water bursting out of a rock at (x, y) and falling in arcs to the right and left."""
    r = random.Random(seed); o = []
    for k in range(7):
        dx = (k - 3) * 40 * scale; top = y - r.uniform(40, 110) * scale; end_y = y + 140 * scale
        d = f"M{f(x)} {f(y)} C {f(x + dx*0.4)} {f(top)} {f(x + dx*0.9)} {f(top)} {f(x + dx*1.3)} {f(end_y)}"
        o.append(f'<path d="{d}" fill="none" stroke="#0F4C68" stroke-width="{f(13*scale)}" stroke-linecap="round"></path>')
        o.append(f'<path d="{d}" fill="none" stroke="#8FD0E2" stroke-width="{f(9*scale)}" stroke-linecap="round"></path>')
        o.append(f'<path d="{d}" fill="none" stroke="#F3F7FA" stroke-width="{f(3*scale)}" stroke-linecap="round" opacity="0.8"></path>')
    for _ in range(30):
        o.append(f'<circle cx="{f(x + r.uniform(-150, 150)*scale)}" cy="{f(y + r.uniform(-110, 60)*scale)}" r="{f(r.uniform(2, 5)*scale)}" fill="#E8F6FA" stroke="#2C9DB8" stroke-width="0.8"></circle>')
    return "".join(o)

SPEAR = '<path d="M-28 -150 L -56 -300" stroke="#3E2416" stroke-width="5"></path><path d="M-56 -300 L -64 -320 L -50 -306 Z" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="2"></path>'
SHIELD = '<ellipse cx="22" cy="-120" rx="22" ry="34" fill="#8A3A1E" stroke="#0D0D0F" stroke-width="3"></ellipse><circle cx="22" cy="-120" r="6" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>'
def warriors(p, n, x0, x1, y0, y1, seed, smin, smax, flip=False, body="#2A140C", cloth=("#8A3A1E", "#5A2A16", "#3A2214")):
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)); out = []
    for y, x in items:
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        out.append(mk.person(p, round(x), round(y), round(s, 2), body=body, cloth=r.choice(cloth), kind="Tunic", sw=4, flip=flip,
                             up=[(-22, -158), (-40, -200), (-28, -150)], extra=SPEAR + SHIELD))
    return "".join(out)

def sinai(cx, base, w, h, seed, fire=True):
    """Mount Sinai: a jagged granite massif, fire on the summit, and a column of smoke rising like a furnace's."""
    r = random.Random(seed); top = base - h
    # jagged ridge: left foot -> summit -> right foot
    pts = [(cx - w / 2, base)]
    for i in range(1, 7):
        t = i / 7; pts.append((cx - w / 2 + w / 2 * t + r.uniform(-w * 0.02, w * 0.02), base - h * (t ** 1.25) * r.uniform(0.86, 1.0) + (r.uniform(0, h * 0.06) if i % 2 else 0)))
    pts.append((cx, top))
    for i in range(1, 7):
        t = 1 - i / 7; pts.append((cx + w / 2 * (1 - t) + r.uniform(-w * 0.02, w * 0.02), base - h * (t ** 1.4) * r.uniform(0.86, 1.0) + (r.uniform(0, h * 0.06) if i % 2 else 0)))
    pts.append((cx + w / 2, base))
    ridge = " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
    o = [f'<path d="M{ridge} Z" fill="#3A2A3E" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>']
    # shadow side and lit ridge
    right = " L ".join(f"{f(x)} {f(y)}" for x, y in pts[7:])
    o.append(f'<path d="M{f(cx)} {f(top)} L {right} L {f(cx + w*0.04)} {f(base)} C {f(cx + w*0.06)} {f(base - h*0.4)} {f(cx + w*0.02)} {f(top + h*0.3)} {f(cx)} {f(top)} Z" fill="#1A1220" opacity="0.75"></path>')
    left = " L ".join(f"{f(x)} {f(y)}" for x, y in pts[3:8])
    o.append(f'<path d="M{left}" fill="none" stroke="#FF8A3D" stroke-width="3" opacity="0.8"></path>')
    for _ in range(7):
        x0 = cx + r.uniform(-w * 0.35, w * 0.3); y0 = base - r.uniform(h * 0.1, h * 0.6)
        o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x0 + r.uniform(10, 30))} {f(y0 - r.uniform(20, 50))} L {f(x0 + r.uniform(20, 50))} {f(y0 - r.uniform(10, 30))}" fill="none" stroke="#5A4A6E" stroke-width="1.6"></path>')
    def puffs(n, x0, x1, y0, y1, rmin, rmax):
        return [(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(rmin, rmax)) for _ in range(n)]
    def cloud(P, fill="#2A2232", hl="#5A4A6E"):
        c = "".join(f'<circle cx="{f(a)}" cy="{f(b)}" r="{f(rr)}"></circle>' for a, b, rr in P)
        return (f'<g fill="{fill}" stroke="#0D0D0F" stroke-width="2.4">{c}</g><g fill="{fill}">{c}</g>'
                f'<g fill="{hl}" opacity="0.55">' + "".join(f'<circle cx="{f(a - rr*0.3)}" cy="{f(b - rr*0.35)}" r="{f(rr*0.5)}"></circle>' for a, b, rr in P[::2]) + '</g>')
    # smoke column behind the fire: widens as it rises
    col = []
    for k in range(9):
        t = k / 8; yy = top - h * 0.1 - t * h * 0.9; ww = w * (0.12 + 0.3 * t)
        col += puffs(4, cx - ww, cx + ww, yy - 20, yy + 20, w * (0.05 + 0.05 * t), w * (0.08 + 0.07 * t))
    o.append(cloud(col))
    if fire:
        o.append(E.blaze(cx, top + h * 0.12, w * 0.24, h * 0.34, seed + 3, n=9))
        # smoke wrapping the summit in front of the fire's base
        o.append(cloud(puffs(7, cx - w * 0.16, cx + w * 0.16, top + h * 0.08, top + h * 0.16, w * 0.03, w * 0.06)))
    # smoke clinging to the slopes
    o.append(cloud(puffs(5, cx - w * 0.42, cx - w * 0.2, base - h * 0.45, base - h * 0.2, w * 0.03, w * 0.06)))
    o.append(cloud(puffs(5, cx + w * 0.2, cx + w * 0.42, base - h * 0.5, base - h * 0.25, w * 0.03, w * 0.06)))
    return "".join(o)

def numeral(k, pos, color="#FFD23F", size=96):
    """A big kanji commandment number (一 … 十) for the Ten Words pages."""
    return (f'    <div style="position: absolute; {pos}; font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: {size}px; line-height: 1; '
            f'color: {color}; -webkit-text-stroke: 3px #0D0D0F; paint-order: stroke fill">{mk.kanji_num(k)}</div>\n')
