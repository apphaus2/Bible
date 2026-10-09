"""Generators and faces for Judges Book One (Deborah and Gideon): the palm-tree of Deborah, mount Tabor, Jael's tent,
the winepress, the fleece, pitchers and torches, the three hundred, camels of Midian, and new faces (Deborah,
Barak, Jael, Gideon)."""
import math, random
import mk, exodus as E, exodus3 as Y, exodus4 as Z, numbers1 as N, joshua1 as J
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = J.tokens()
    t["__FACE_DEBORAH__"] = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#1A1210", scarf="#E8B830", light="#FFF4C2")
    t["__FACE_BARAK__"] = F("adam", skin="#B9785A", shadow="#5A2A1E", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#5A6E8A", cord=True, brow="sorrow", sweat=True)
    t["__FACE_BARAK_BOLD__"] = F("adam", skin="#C98E66", shadow="#7A3A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#5A6E8A", cord=True, brow="scowl", light="#FF8A3D")
    t["__FACE_JAEL__"] = F("eve", skin="#C98E66", shadow="#5A3A4A", hair="#1A1210", scarf="#2E6A32", brow="scowl")
    t["__FACE_GIDEON__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", scarf="#C9A86A", cord=True, brow="sorrow", sweat=True, light="#FFF4C2")
    t["__FACE_GIDEON_BOLD__"] = F("adam", skin="#D9A27A", shadow="#7A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", scarf="#C9A86A", cord=True, brow="scowl", light="#FF8A3D")
    t["__FACE_GIDEON_CALM__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, scarf="#C9A86A", cord=True, light="#FFE680")
    return t

def palm(x, y, s=1.0):
    """A date palm: a curved ringed trunk and a crown of drooping fronds."""
    trunk = "M-10 0 C -8 -80 4 -160 18 -230 L 30 -228 C 18 -160 8 -80 10 0 Z"
    rings = "".join(f'<path d="M{f(-9 + k*0.14)} {f(-k)} L {f(10 + k*0.1)} {f(-k - 4)}" stroke="#5A3A22" stroke-width="2"></path>' for k in range(16, 220, 16))
    fronds = ""
    for a in (-170, -140, -110, -70, -40, -10, 20):
        r = math.radians(a); ex, ey = 24 + 110 * math.cos(r), -232 + 110 * math.sin(r) + 30
        mx, my = 24 + 60 * math.cos(r), -232 + 60 * math.sin(r) - 20
        fronds += (f'<path d="M24 -232 Q {f(mx)} {f(my)} {f(ex)} {f(ey)} Q {f(mx + 6)} {f(my + 18)} 24 -226 Z" fill="#2E6A32" stroke="#0D0D0F" stroke-width="2"></path>'
                   f'<path d="M24 -232 Q {f(mx)} {f(my)} {f(ex)} {f(ey)}" fill="none" stroke="#9CCB5E" stroke-width="1.6"></path>')
    dates = "".join(f'<circle cx="{f(16 + dx)}" cy="{f(-220 + dy)}" r="4" fill="#B5421E" stroke="#0D0D0F" stroke-width="1"></circle>' for dx, dy in [(0, 0), (8, 4), (14, -2), (4, 8)])
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{trunk}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></path>{rings}{fronds}{dates}</g>'

def tabor(cx, base, w, h, color="#3F6A3A", seed=1):
    """Mount Tabor: a lone rounded dome rising out of the plain."""
    r = random.Random(seed)
    trees = "".join(f'<circle cx="{f(cx + r.uniform(-w*0.35, w*0.35))}" cy="{f(base - r.uniform(h*0.1, h*0.75))}" r="{f(r.uniform(5, 10))}" fill="#2E4A22" opacity="0.8"></circle>' for _ in range(30))
    return (f'<path d="M{f(cx - w/2)} {f(base)} C {f(cx - w*0.35)} {f(base - h*0.9)} {f(cx - w*0.15)} {f(base - h)} {f(cx)} {f(base - h)} C {f(cx + w*0.15)} {f(base - h)} {f(cx + w*0.35)} {f(base - h*0.9)} {f(cx + w/2)} {f(base)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>' + trees)

def tent_big(x, y, w, h, color="#3A2214", stripe="#8A6A4A", open_=True, glow=None):
    """A large goat-hair tent seen from the front with its door open."""
    door = (f'<path d="M{f(x - w*0.12)} {f(y)} L {f(x)} {f(y - h*0.7)} L {f(x + w*0.12)} {f(y)} Z" fill="{glow or "#12090A"}" stroke="#0D0D0F" stroke-width="2"></path>') if open_ else ""
    return (f'<path d="M{f(x - w/2)} {f(y)} L {f(x - w*0.4)} {f(y - h*0.7)} L {f(x)} {f(y - h)} L {f(x + w*0.4)} {f(y - h*0.7)} L {f(x + w/2)} {f(y)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + "".join(f'<path d="M{f(x - w*0.45 + k*w*0.15)} {f(y)} L {f(x - w*0.35 + k*w*0.1)} {f(y - h*0.7)}" stroke="{stripe}" stroke-width="3" opacity="0.6"></path>' for k in range(7))
            + f'<path d="M{f(x - w*0.4)} {f(y - h*0.7)} L {f(x)} {f(y - h)} L {f(x + w*0.4)} {f(y - h*0.7)}" fill="none" stroke="#0D0D0F" stroke-width="2.4"></path>' + door
            + f'<path d="M{f(x - w/2)} {f(y)} L {f(x - w/2 - 30)} {f(y - h*0.2)} M{f(x + w/2)} {f(y)} L {f(x + w/2 + 30)} {f(y - h*0.2)}" stroke="#5A3A22" stroke-width="2"></path>')

PIN = '<path d="M0 0 L 4 -60 L 10 -60 L 8 0 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2"></path>'
HAMMER = '<path d="M0 0 L 0 -70" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path><rect x="-16" y="-84" width="32" height="18" rx="4" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>'

def rug_sleeper(x, y, s, color="#7A3BA8", flip=False):
    """A man asleep under a rug: only the head shows."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<circle cx="78" cy="-18" r="14" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></circle>'
            f'<path d="M-96 0 C -96 -30 -60 -40 0 -40 C 40 -40 66 -34 70 -6 L 70 0 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-80 -10 L 60 -10 M-70 -24 L 50 -26" stroke="#E8B830" stroke-width="3" opacity="0.8"></path>'
            '<path d="M-90 0 L -96 8 M-70 0 L -74 8 M-50 0 L -54 8 M50 0 L 54 8" stroke="#E8B830" stroke-width="2"></path></g>')

def winepress(x, y, w, h):
    """A winepress cut into the rock: a stone-rimmed pit seen at an angle."""
    return (f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w/2)}" ry="{f(h/2)}" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            f'<ellipse cx="{f(x)}" cy="{f(y + h*0.08)}" rx="{f(w/2 - 14)}" ry="{f(h/2 - 10)}" fill="#3A2A2A"></ellipse>'
            + "".join(f'<path d="M{f(x + (w/2)*math.cos(a))} {f(y + (h/2)*math.sin(a))} L {f(x + (w/2 - 14)*math.cos(a))} {f(y + h*0.08 + (h/2 - 10)*math.sin(a))}" stroke="#8A7A6A" stroke-width="2"></path>' for a in [i * math.pi / 6 for i in range(12)]))

def wheat(x, y, s=1.0, n=7, seed=1):
    r = random.Random(seed); o = []
    for i in range(n):
        a = math.radians(-90 + (i - n / 2) * 8 + r.uniform(-3, 3)); ex, ey = 60 * math.cos(a), 60 * math.sin(a)
        o.append(f'<path d="M0 0 L {f(ex)} {f(ey)}" stroke="#C9A86A" stroke-width="2.4"></path>'
                 f'<ellipse cx="{f(ex)}" cy="{f(ey)}" rx="4" ry="11" transform="rotate({f(math.degrees(a) + 90)} {f(ex)} {f(ey)})" fill="#E8C88A" stroke="#8A6A3A" stroke-width="1.4"></ellipse>')
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + "".join(o) + '</g>'

def chaff(n, x0, x1, y0, y1, seed):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-6, 6))} {f(r.uniform(-3, 3))}" stroke="#E8C88A" stroke-width="2"></path>' for x, y in ((r.uniform(x0, x1), r.uniform(y0, y1)) for _ in range(n)))

def fleece(x, y, s=1.0, wet=True, seed=1):
    """A fleece of wool spread on the threshing-floor; wet = beaded with dew."""
    r = random.Random(seed)
    puffs = "".join(f'<circle cx="{f(r.uniform(-60, 60))}" cy="{f(r.uniform(-16, 6))}" r="{f(r.uniform(9, 15))}"></circle>' for _ in range(26))
    dew = "".join(f'<circle cx="{f(r.uniform(-60, 60))}" cy="{f(r.uniform(-22, 4))}" r="{f(r.uniform(1.5, 3))}" fill="#E8F6FA" stroke="#2C9DB8" stroke-width="0.8"></circle>' for _ in range(30)) if wet else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><g fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2">{puffs}</g>'
            f'<g fill="#F3EFE6">{puffs}</g>{dew}</g>')

def dew(n, x0, x1, y0, y1, seed):
    r = random.Random(seed)
    return "".join(f'<circle cx="{f(r.uniform(x0, x1))}" cy="{f(r.uniform(y0, y1))}" r="{f(r.uniform(1.4, 3.2))}" fill="#E8F6FA" stroke="#2C9DB8" stroke-width="0.8"></circle>' for _ in range(n))

def bowl(x, y, w, full=True):
    water = f'<ellipse cx="{f(x)}" cy="{f(y - w*0.3)}" rx="{f(w*0.42)}" ry="{f(w*0.09)}" fill="#8FD0E2" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' if full else ""
    return (f'<path d="M{f(x - w/2)} {f(y - w*0.3)} C {f(x - w/2)} {f(y)} {f(x + w/2)} {f(y)} {f(x + w/2)} {f(y - w*0.3)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<ellipse cx="{f(x)}" cy="{f(y - w*0.3)}" rx="{f(w/2)}" ry="{f(w*0.11)}" fill="#8A4A22" stroke="#0D0D0F" stroke-width="2"></ellipse>' + water)

def pitcher(x, y, s=1.0, broken=False, torch=True, seed=1):
    """An earthen pitcher with a torch inside; broken = shattered, the torch blazing out."""
    r = random.Random(seed)
    flame = E.flame(0, -50, 14, 60 if broken else 16, r.uniform(-6, 6))
    if not broken:
        body = ('<path d="M-12 -60 L -12 -52 C -28 -44 -30 -10 -16 0 L 16 0 C 30 -10 28 -44 12 -52 L 12 -60 Z" fill="#C8682E" stroke="#0D0D0F" stroke-width="2.4"></path>'
                '<path d="M-14 -62 L 14 -62" stroke="#0D0D0F" stroke-width="5"></path><path d="M-20 -34 C -10 -30 10 -30 20 -34" fill="none" stroke="#8A3A1E" stroke-width="2"></path>')
        return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + (flame if torch else "") + body + '</g>'
    shards = "".join(f'<path d="M{f(cx)} {f(cy)} l {f(r.uniform(8, 16))} {f(r.uniform(-6, 6))} l {f(r.uniform(-6, 2))} {f(r.uniform(8, 14))} Z" fill="#C8682E" stroke="#0D0D0F" stroke-width="1.6" transform="rotate({f(r.uniform(0, 360))} {f(cx)} {f(cy)})"></path>'
                     for cx, cy in ((r.uniform(-40, 40), r.uniform(-70, 10)) for _ in range(9)))
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 L 0 -50" stroke="#5A3A22" stroke-width="6"></path>{flame}{shards}</g>'

TORCH_ARM = [(-22, -158), (-40, -200), (-44, -240)]
def torchbearer(p, x, y, s, flip=False, body="#12090A", cloth="#3A2214", seed=1):
    """One of the three hundred: torch held high in one hand, the ram's horn at his mouth."""
    torch = ('<path d="M-44 -236 L -46 -290" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>'
             + E.flame(-46, -286, 12, 46, random.Random(seed).uniform(-8, 8)))
    horn = J.shofar(14, -190, 0.85, rot=-18)
    return mk.person(p, round(x), round(y), round(s, 3), body=body, cloth=cloth, kind="Tunic", sw=4, flip=flip, up=TORCH_ARM, extra=torch + horn)

def drinker_lap(p, x, y, s, flip=False, cloth="#5A2A16"):
    """A man who lapped, putting his hand to his mouth, standing alert."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#2A140C", cloth=cloth, kind="Tunic", sw=4, flip=flip, up=[(-22, -158), (-6, -150), (2, -176)])

CAMEL = ("M-70 -80 C -70 -96 -60 -104 -46 -104 C -36 -128 -14 -130 -4 -110 C 6 -126 26 -126 34 -104 C 44 -98 50 -92 56 -100 "
         "L 66 -136 C 70 -148 84 -150 92 -142 L 100 -132 C 102 -126 96 -124 90 -126 L 84 -128 L 72 -94 C 66 -78 54 -72 40 -72 "
         "L 36 -40 L 40 0 L 30 0 L 26 -44 L 22 -66 L -40 -66 L -46 -40 L -40 0 L -50 0 L -56 -42 L -62 -66 C -70 -70 -72 -76 -70 -80 Z")
def camel(x, y, s=1.0, flip=False, color="#B5844A", rider=None):
    sx = -s if flip else s
    rid = (f'<path d="M-14 -110 L -10 -150 C -10 -160 2 -160 4 -150 L 8 -110 Z" fill="{rider}" stroke="#0D0D0F" stroke-width="2"></path>'
           f'<circle cx="-3" cy="-164" r="8" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></circle>') if rider else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">{rid}<path d="{CAMEL}" fill="{color}" stroke="#0D0D0F" stroke-width="{f(2.2/s)}" stroke-linejoin="round"></path>'
            f'<circle cx="88" cy="-138" r="2.4" fill="#0D0D0F"></circle><path d="M-70 -80 C -78 -70 -80 -60 -76 -50" fill="none" stroke="#0D0D0F" stroke-width="{f(3/s)}"></path>'
            '<path d="M-40 -100 L 30 -100 L 26 -80 L -36 -80 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6" opacity="0.9"></path></g>')
