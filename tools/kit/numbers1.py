"""Generators and faces for Numbers Book One (in the wilderness): the grape cluster, giants, fiery serpents,
the serpent of brass on its standard, Balaam's ass, the angel with the drawn sword, Israel's tents, and new faces
(Caleb, Balaam)."""
import math, random
import mk, exodus as E, exodus3 as Y, exodus4 as Z, exodus5 as V, snake as SN, ladder
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = V.tokens()
    t["__FACE_CALEB__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#5A3A22", hl="#8A6A4A", beard=True, scarf="#3F8A44", cord=True, light="#FFE680")
    t["__FACE_BALAAM__"] = F("adam", skin="#B9785A", shadow="#5A2A3A", hair="#3A3A3A", hl="#7A7A7A", beard=True, scarf="#7A3BA8", cord=True, brow="scowl")
    t["__FACE_BALAAM_AWE__"] = F("adam", skin="#C98E66", shadow="#5A3A5A", hair="#3A3A3A", hl="#7A7A7A", beard=True, scarf="#7A3BA8", cord=True, brow="sorrow", sweat=True, light="#FFF4C2")
    t["__FACE_SPY__"] = F("adam", skin="#B98A6E", shadow="#5E3A4A", hair="#1A1210", hl="#4A3A2E", brow="sorrow", sweat=True, stubble="#2A1A10")
    return t

def grapes(x, y, s=1.0, seed=1):
    """One huge cluster of grapes hanging from a point (x, y)."""
    r = random.Random(seed); o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">',
                                  '<path d="M0 0 L 0 14" stroke="#3E5A22" stroke-width="5"></path>',
                                  '<path d="M2 8 C 26 0 44 10 50 26 C 30 26 14 20 2 8 Z" fill="#3F8A44" stroke="#0D0D0F" stroke-width="2"></path>']
    rows = 9
    for i in range(rows):
        w = 52 * (1 - i / rows) + 10; yy = 20 + i * 15
        for k in range(int(w / 13) + 1):
            xx = -w / 2 + k * 13 + r.uniform(-2, 2)
            o.append(f'<circle cx="{f(xx)}" cy="{f(yy)}" r="9" fill="#5A1A6E" stroke="#0D0D0F" stroke-width="1.6"></circle>'
                     f'<circle cx="{f(xx-3)}" cy="{f(yy-3)}" r="2.6" fill="#C8A0E0"></circle>')
    o.append('</g>')
    return "".join(o)

def fiery(P, wmax, uid, head_scale=1.0):
    s = SN.snake(P, wmax, uid, head_scale)
    for a, b in {"#5E8F26": "#D7261E", "#22401A": "#5A0E16", "#1B3A12": "#3A0408", "#C9E265": "#FFD23F", "#D8F08A": "#FFE680", "#E4DE9A": "#FFC14D"}.items():
        s = s.replace(a, b)
    return s

def brass_serpent(x, top, h, uid):
    """The serpent of brass coiled on the standard."""
    pole = (f'<path d="M{f(x)} {f(top + h)} L {f(x)} {f(top)}" stroke="#0D0D0F" stroke-width="13" stroke-linecap="round"></path>'
            f'<path d="M{f(x)} {f(top + h)} L {f(x)} {f(top)}" stroke="#8A5A30" stroke-width="9" stroke-linecap="round"></path>'
            f'<path d="M{f(x - 60)} {f(top + 20)} L {f(x + 60)} {f(top + 20)}" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path>'
            f'<path d="M{f(x - 60)} {f(top + 20)} L {f(x + 60)} {f(top + 20)}" stroke="#8A5A30" stroke-width="8" stroke-linecap="round"></path>')
    pts = []
    for k in range(9):
        t = k / 8; yy = top + h * 0.75 - t * h * 0.7; xx = x + math.sin(t * math.pi * 3.2) * 30
        pts.append((xx, yy))
    pts.append((x + 28, top - 30)); pts.append((x + 60, top - 40))
    s = SN.snake(pts, 13, uid, 1.3)
    for a, b in {"#5E8F26": "#C8862E", "#22401A": "#7A4A12", "#1B3A12": "#5A3A10", "#C9E265": "#FFD23F", "#D8F08A": "#FFF4C2", "#E4DE9A": "#E8C88A"}.items():
        s = s.replace(a, b)
    return pole + s

ASS_EARS = '<path d="M60 -104 L 50 -146 L 64 -108 Z M68 -104 L 66 -148 L 74 -106 Z" fill="#7A746A" stroke="#0D0D0F" stroke-width="2"></path><path d="M78 -86 C 86 -80 90 -76 84 -72" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
def ass(x, y, s=1.0, flip=False, color="#8A8478"):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="{Y.TAIL}" fill="#3A3A3A" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="{Y.HORSE}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            f'{ASS_EARS}<circle cx="70" cy="-94" r="2.6" fill="#0D0D0F"></circle>'
            '<path d="M-20 -70 L 40 -84" stroke="#3A3A3A" stroke-width="4"></path></g>')

def ass_lying(x, y, s=1.0, flip=False, color="#8A8478"):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-40 0 L -70 4 M30 0 L 60 4" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path>'
            f'<path d="M-40 0 L -70 4 M30 0 L 60 4" stroke="{color}" stroke-width="6" stroke-linecap="round"></path>'
            f'<ellipse cx="0" cy="-26" rx="62" ry="28" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            f'<path d="M40 -40 C 56 -60 70 -76 84 -84 L 98 -62 C 84 -56 70 -40 58 -20 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<path d="M84 -84 C 94 -90 108 -84 112 -70 C 114 -60 104 -56 98 -62 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M86 -84 L 74 -122 L 90 -88 Z M94 -84 L 96 -124 L 100 -86 Z" fill="#7A746A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<circle cx="98" cy="-76" r="2.6" fill="#0D0D0F"></circle><path d="M104 -64 C 110 -62 112 -58 108 -56" fill="none" stroke="#0D0D0F" stroke-width="1.6"></path></g>')

SWORD_ARM = [(-22, -158), (-40, -200), (-42, -238)]
BLADE = ('<path d="M-46 -246 L -38 -248 L -20 -372 L -26 -392 L -36 -374 Z" fill="#F3F7FA" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
         '<path d="M-42 -250 L -26 -380" stroke="#8FB8D0" stroke-width="2"></path>'
         '<path d="M-60 -244 L -24 -250" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path>'
         '<path d="M-60 -244 L -24 -250" stroke="#E8B830" stroke-width="5" stroke-linecap="round"></path>')
def angel(p, x, y, s, sword=True, glow=True, flip=False):
    """The angel of Jehovah: a man in shining white, the sword drawn in his hand."""
    wings = (f'<path d="{ladder.WING}" fill="#FFF4C2" stroke="#E8B830" stroke-width="2.4"></path>'
             f'<path d="{ladder.WING}" transform="scale(-1 1)" fill="#FFF4C2" stroke="#E8B830" stroke-width="2.4"></path>')
    halo = f'<ellipse cx="{f(x)}" cy="{f(y - 120*s)}" rx="{f(120*s)}" ry="{f(160*s)}" fill="#FFF4C2" opacity="0.4"></ellipse>' if glow else ""
    return halo + mk.person(p, round(x), round(y), s, body="#D9A27A", cloth="#FFFFFF", hair="#F3E2A0", stroke="#E8B830", sw=3, flip=flip,
                            up=SWORD_ARM if sword else None, pre=wings, extra=BLADE if sword else "")

def camp(n, x0, x1, y0, y1, seed, color=("#5A3A22", "#6B4A2A", "#3A2214")):
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)); o = []
    for y, x in items:
        k = (y - y0) / max(1, y1 - y0); w = 30 + 60 * k
        o.append(Z.tent(x, y, w, w * 0.7, color=r.choice(color)))
    return "".join(o)

def star(x, y, r, color="#FFF4C2"):
    pts = []
    for i in range(16):
        a = -math.pi / 2 + i * math.pi / 8; rr = r if i % 2 == 0 else r * (0.18 if i % 4 else 0.35)
        pts.append(f"{f(x + rr*math.cos(a))} {f(y + rr*math.sin(a))}")
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r*0.9)}" fill="{color}" opacity="0.18"></circle>'
            f'<path d="M{" L ".join(pts)} Z" fill="{color}" stroke="#E8B830" stroke-width="2"></path>')

PRONE = "M-96 0 L -92 -12 C -74 -16 -56 -20 -40 -30 C -22 -42 2 -40 24 -28 L 44 -18 C 60 -12 76 -8 96 -6 L 96 2 Z"
def prostrate(x, y, s, color="#3A2214", rim="#0D0D0F", flip=False, skin=None):
    """A man fallen on his face, head to the right, arms stretched out before him."""
    sx = -s if flip else s; sk = skin or color
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="{PRONE}" fill="{color}" stroke="{rim}" stroke-width="2.2" stroke-linejoin="round"></path>'
            f'<circle cx="52" cy="-16" r="13" fill="{sk}" stroke="{rim}" stroke-width="2"></circle>'
            '<path d="M-40 -26 C -20 -22 10 -18 30 -16" fill="none" stroke="#12090A" stroke-width="1.4" opacity="0.6"></path></g>')

def mount(x, y, s, flip=False, color="#8A8478", rider_body="#3A1E14", rider_cloth="#7A3BA8", p="r", up=None, extra=""):
    """A man riding upon an ass (the rider is drawn first so the beast covers his far leg)."""
    sx = -1 if flip else 1
    rx = x + sx * (-14) * s
    rider = mk.person(p, round(rx), round(y - 40 * s), round(s * 0.62, 3), body=rider_body, cloth=rider_cloth, flip=flip, up=up, extra=extra)
    return rider + ass(x, y, s, flip, color)
