"""Generators and faces for Ruth: barley fields and sheaves, reapers with sickles, a gleaner, Beth-lehem on its hill,
graves in Moab, the threshing-floor at night, the city gate with elders, a swaddled child, and new faces (Naomi,
Mara, Ruth, Orpah, Boaz)."""
import math, random
import mk, exodus as E, exodus4 as Z, joshua1 as J, judges1 as G, judges2 as S
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = S.tokens()
    t["__FACE_NAOMI__"] = F("eve", skin="#C98E66", shadow="#7A4A3A", hair="#B8B2A6", scarf="#4A3A6A", brow="sorrow")
    t["__FACE_MARA__"] = F("eve", skin="#B98A6E", shadow="#5A3A4A", hair="#B8B2A6", scarf="#2A2A3E", brow="sorrow", tear=True)
    t["__FACE_NAOMI_JOY__"] = F("eve", skin="#D9A27A", shadow="#8A5A3E", hair="#C8C2B6", scarf="#4A3A6A", laugh=True, light="#FFE680")
    t["__FACE_RUTH__"] = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", scarf="#C2456A", light="#FFE680")
    t["__FACE_RUTH_WEEP__"] = F("eve", skin="#C98E66", shadow="#6A3A4A", hair="#2A1A10", scarf="#C2456A", brow="sorrow", tear=True)
    t["__FACE_ORPAH__"] = F("eve", skin="#D9A27A", shadow="#8A5A3E", hair="#3A1E14", scarf="#E8A317", brow="sorrow", tear=True)
    t["__FACE_BOAZ__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#6A5A4E", hl="#9A8A7E", beard=True, beard_color="#6A5A4E", scarf="#F3EFE6", cord=True, light="#FFE680")
    return t

def sheaf(x, y, s=1.0, color="#E8C88A"):
    """A bound sheaf of barley standing upright."""
    stalks = "".join(f'<path d="M{f(dx*0.4)} 0 L {f(dx)} -60" stroke="#C9A86A" stroke-width="2"></path>' for dx in range(-14, 16, 4))
    heads = "".join(f'<ellipse cx="{f(dx)}" cy="-64" rx="3" ry="8" transform="rotate({f(dx*1.5)} {f(dx)} -64)" fill="{color}" stroke="#8A6A3A" stroke-width="1"></ellipse>' for dx in range(-16, 18, 4))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{stalks}{heads}'
            '<path d="M-8 -30 L 8 -30" stroke="#8A5A30" stroke-width="4"></path></g>')

def field(x0, x1, y, h, seed, rows=3, color="#E8C88A"):
    """A field of ripe barley in a few receding rows."""
    return "".join(S.grain(x0, x1, y + k * h * 0.6, h * (0.7 + 0.15 * k), seed + k) for k in range(rows))

SICKLE = '<path d="M-44 -240 C -70 -250 -86 -232 -78 -214 C -76 -230 -62 -238 -46 -232 Z" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
def reaper(p, x, y, s, flip=False, cloth="#8A6A4A", body="#2A140C", woman=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=body, cloth=cloth, kind="Tunic", sw=4, flip=flip, woman=woman, hair=woman,
                     up=[(-22, -158), (-40, -200), (-44, -240)], extra=SICKLE)

GLEAN = ("M-50 0 L -40 0 L -36 -46 C -20 -58 6 -70 30 -72 C 42 -72 50 -66 52 -58 L 60 -40 L 52 -38 L 44 -52 C 30 -52 10 -44 -4 -30 L -14 0 L -4 0 "
         "L -10 -40 C -20 -36 -28 -30 -34 -20 Z")
def gleaner(x, y, s=1.0, flip=False, color="#C2456A", skin="#3A1E14"):
    """A woman stooping to glean ears from the stubble."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-46 0 L -38 -60 C -30 -82 10 -96 36 -86 C 48 -82 54 -70 50 -60 L 30 -40 L 24 -10 L 30 0 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2" stroke-linejoin="round"></path>'
            f'<circle cx="56" cy="-80" r="12" fill="{skin}" stroke="#0D0D0F" stroke-width="2"></circle>'
            f'<path d="M44 -92 C 54 -100 70 -96 70 -84 L 62 -72 C 58 -82 50 -86 44 -84 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<path d="M36 -70 L 60 -40 L 66 -18" fill="none" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path>'
            f'<path d="M36 -70 L 60 -40 L 66 -18" fill="none" stroke="{skin}" stroke-width="6" stroke-linecap="round"></path>'
            f'<path d="M66 -18 L 70 -40 M66 -18 L 76 -36" stroke="#C9A86A" stroke-width="2"></path></g>')

def graves(x, y, n, s=1.0):
    """Stone-heaped graves on a hillside."""
    o = []
    for i in range(n):
        cx = x + i * 70 * s
        o.append(f'<path d="M{f(cx - 30*s)} {f(y)} C {f(cx - 26*s)} {f(y - 30*s)} {f(cx + 26*s)} {f(y - 30*s)} {f(cx + 30*s)} {f(y)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + "".join(f'<ellipse cx="{f(cx + dx*s)}" cy="{f(y - dy*s)}" rx="{f(8*s)}" ry="{f(5*s)}" fill="#A89A86" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for dx, dy in [(-14, 8), (0, 12), (14, 8), (-6, 20), (8, 20)]))
    return "".join(o)

def baby(x, y, s=1.0):
    """A swaddled infant."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><ellipse cx="0" cy="0" rx="22" ry="12" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            '<path d="M-14 -6 L 12 6 M-8 -10 L 16 2" stroke="#C9A86A" stroke-width="2"></path>'
            '<circle cx="20" cy="-4" r="8" fill="#D9A27A" stroke="#0D0D0F" stroke-width="2"></circle></g>')

HOLD_BABY = [(-22, -158), (-10, -128), (14, -124)]
def naomi_with_child(p, x, y, s, flip=False):
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth="#4A3A6A", woman=True, hair="#B8B2A6", sw=4, flip=flip,
                     up=HOLD_BABY, extra=baby(10, -130, 0.8))

def heap(cx, base, w, h, color="#E8C88A"):
    r = random.Random(3)
    dots = "".join(f'<circle cx="{f(cx + r.uniform(-w*0.4, w*0.4))}" cy="{f(base - r.uniform(2, h*0.8))}" r="1.6" fill="#C9A86A"></circle>' for _ in range(60))
    return f'<path d="M{f(cx - w/2)} {f(base)} C {f(cx - w*0.3)} {f(base - h)} {f(cx + w*0.3)} {f(base - h)} {f(cx + w/2)} {f(base)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></path>' + dots

def sack(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-22 0 C -30 -20 -24 -44 -10 -50 L -14 -58 L 14 -58 L 10 -50 C 24 -44 30 -20 22 0 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-12 -52 L 12 -52" stroke="#5A3A22" stroke-width="3"></path></g>')
