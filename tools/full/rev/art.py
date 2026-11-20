"""Drawings for Revelation 1–3 (chapter 1 of the volume), and the shared figures the later chapters build on.

Figures (never blobs: drawn on the kit's MAN silhouette through epistle.robed; each panel needs defs(p)):
    angel(p, x, b, s, up=, flip=)        a figure of white light, a gold rim, no face, a glow about it
    john_fig(p, x, b, s, pose=, up=)     John, very old: ntcast's rust robe, a grey mantle, white hair, a long white beard
    john_fallen(x, b, s, flip=)          John fallen at his feet as one dead (1:17), face to the ground, arms forward
    christ(p, x, b, s, up=, girdle=, stars=)   Jesus as ntcast draws him, risen, in white light (co1.art5.risen_fig's look);
                                         girdle= the golden girdle at the breasts; stars= the seven stars at his raised hand
    candlestick(x, b, s)                 a golden lampstand with its lamp burning
    star(x, y, r, color)                 a five-pointed star
Scenes (w × h, p a prefix unique to the panel):
    churches_map(w, h, lit=)             Patmos and the seven churches of Asia on Acts' projection (act.geo), the letters' circuit
    patmos(p, w, h, seed, stage=)        the isle that is called Patmos: the rocky shore, the sea, John ("stand", "write",
                                         "turn" toward the great voice behind him, "dawn" an angel of light over the sea)
    clouds_coming(p, w, h, seed)         he cometh with the clouds: clouds lit from within, the tribes of the earth looking up
    alpha_omega(w, h, seed)              the light and the letters Alpha and Omega (no figure: the Lord God speaks)
    son_of_man(p, w, h, seed, stage=)    the seven golden candlesticks and one like unto a son of man in their midst, in
                                         blinding light ("stand", "near" — closer, the seven stars in his hand —, "fallen")
    mystery(w, h)                        the mystery of the seven stars and the seven golden candlesticks, a technical plate
    church(p, w, h, seed, city)          a church's city with its emblem (ephesus, smyrna, pergamum, thyatira, sardis,
                                         philadelphia, laodicea), a medallion at the top right
    door(p, w, h, seed)                  behold, I stand at the door and knock: Jesus at the shut door of a house at evening"""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from num.art import ALL
from epistle import robed, radiance
from oba.minor import halo, rays, starfield, sea, walls, crowd, scroll, fig_tree, olive
from genesis.art2 import ground, hills, birds, fit
from genesis.art3 import label, node, route
from sa2.art import sky
from kg1.art import ship, temple_front
from ntcast import JESUS_SKIN, _HAIR_FIG, _BEARD_FIG
from exo.art8 import tag
from act import geo

INK = "#0D0D0F"
GOLD, GOLD_L, WHITE = "#E8B830", "#FFD23F", "#FFFFFF"
def f(v): return f"{v:.1f}"
def defs(p): return mk.defs(p, *ALL, "ManUp", "WomanUp")

# ---- figures ----------------------------------------------------------------------------------------------------------------
def angel(p, x, b, s, up=None, flip=False, glow=True, extra="", line="#E8B830"):
    """An angel: a figure of white light with a gold rim, no face (epistle.robed in white, the skin and the hands light too)."""
    return ((halo(x, b - 110 * s, 125 * s, "#FFF4C2", 0.5) if glow else "")
            + robed(p, x, b, s, WHITE, skin="#FFF6DA", line=line, up=up, flip=flip, extra=extra))

JOHN_ROBE, JOHN_MANTLE, JOHN_HAIR = "#B85A3A", "#8A847A", "#EEECE6"
_LONG = '<path d="M-6 -168 C -8 -150 -4 -132 4 -122 C 10 -132 14 -150 12 -168 Z" fill="#EEECE6" stroke="#0D0D0F" stroke-width="1.3"></path>'

def john_fig(p, x, b, s, pose="stand", up=None, flip=False, seat=None, extra=""):
    """John, very old (ntcast's JOHN grown old): the rust robe, a grey mantle, white hair and a long white beard."""
    return robed(p, x, b, s, JOHN_ROBE, hair=JOHN_HAIR, beard=JOHN_HAIR, mantle=JOHN_MANTLE, belt="#5A2A1A", up=up, flip=flip, pose=pose,
                 seat=seat, extra=_LONG + extra)

def john_fallen(x, b, s, flip=False):
    """John fallen at his feet as one dead (1:17): lying face to the ground, the arms stretched out before him, the white
    hair and beard, the rust robe and the grey mantle (drawn lying, not a standing figure turned over)."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(b)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-66 -2 C -66 -22 -40 -30 -8 -28 C 30 -26 70 -22 92 -12 C 98 -8 98 -2 94 0 L -66 0 Z" fill="{JOHN_ROBE}" stroke="{INK}" stroke-width="2.6"></path>'
            f'<path d="M-58 -22 C -30 -34 14 -32 44 -24 C 40 -16 30 -12 18 -12 C -8 -18 -34 -16 -54 -10 Z" fill="{JOHN_MANTLE}" stroke="{INK}" stroke-width="2"></path>'
            f'<path d="M-20 -12 C 10 -10 50 -10 80 -6" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.45"></path>'
            f'<path d="M-56 -20 C -74 -18 -94 -12 -110 -8" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"></path>'
            f'<path d="M-56 -20 C -74 -18 -94 -12 -110 -8" fill="none" stroke="{JOHN_ROBE}" stroke-width="8.5" stroke-linecap="round"></path>'
            f'<path d="M-52 -10 C -72 -8 -92 -4 -108 -2" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"></path>'
            f'<path d="M-52 -10 C -72 -8 -92 -4 -108 -2" fill="none" stroke="{JOHN_ROBE}" stroke-width="8.5" stroke-linecap="round"></path>'
            f'<ellipse cx="-116" cy="-8" rx="6.5" ry="4.5" fill="#CF9A76" stroke="{INK}" stroke-width="1.4"></ellipse>'
            f'<ellipse cx="-114" cy="-1.5" rx="6.5" ry="4.2" fill="#CF9A76" stroke="{INK}" stroke-width="1.4"></ellipse>'
            f'<circle cx="-78" cy="-13" r="12" fill="#CF9A76" stroke="{INK}" stroke-width="2"></circle>'
            f'<path d="M-66 -16 C -68 -26 -82 -30 -90 -22 C -94 -16 -92 -8 -86 -3 C -80 -6 -72 -6 -66 -8 Z" fill="{JOHN_HAIR}" stroke="{INK}" stroke-width="1.6"></path>'
            f'<path d="M-90 -6 C -98 -4 -104 -1 -106 1 L -84 1 Z" fill="{JOHN_HAIR}" stroke="{INK}" stroke-width="1.3"></path>'
            f'<path d="M92 -10 C 100 -10 106 -6 104 -2 L 92 -2 Z" fill="#CF9A76" stroke="{INK}" stroke-width="1.4"></path>'
            '</g>')

GIRDLE = ('<path d="M-21 -141 C -8 -136 8 -136 21 -141" fill="none" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path>'
          '<path d="M-21 -141 C -8 -136 8 -136 21 -141" fill="none" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"></path>')

def star(x, y, r, color=GOLD_L, sw=1.2, stroke=INK):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{f(x + rr * math.cos(a))} {f(y + rr * math.sin(a))}")
    return f'<path d="M{" L ".join(pts)} Z" fill="{color}" stroke="{stroke}" stroke-width="{sw}"></path>'

def star_ring(cx, cy, r, k=7, sr=7, color="#FFF4C2"):
    """The seven stars in a ring (in a figure's own units when used as robed's extra)."""
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 1.5)}" fill="#FFF4C2" opacity="0.35"></circle>'
            + "".join(star(cx + r * math.cos(-math.pi / 2 + i * 2 * math.pi / k), cy + r * math.sin(-math.pi / 2 + i * 2 * math.pi / k), sr, color, 0.9)
                      for i in range(k)))

UP_STARS = [(-22, -158), (-46, -150), (-66, -158)]            # the right hand held out, the seven stars about it (flip=True: toward +x)
UP_HAND = [(-22, -158), (-44, -128), (-58, -100)]             # the right hand laid upon one fallen before him

def christ(p, x, b, s, up=None, flip=False, girdle=False, stars=False, glow=True, rays_=True):
    """Jesus risen (ntcast's look, as co1.art5.risen_fig draws him): skin, hair and short beard as ntcast, the robe white
    and the mantle pale blue-grey, a white glow and soft rays behind him; girdle= the golden girdle at the breasts (1:13);
    stars= the seven stars about the raised hand (1:16, 1:20, 2:1)."""
    ex = _HAIR_FIG + _BEARD_FIG + (GIRDLE if girdle else "")
    if stars and up: ex += star_ring(up[-1][0], up[-1][1], 15, sr=5.5)
    o = ""
    if glow: o += halo(x, b - 110 * s, 190 * s, WHITE, 0.85)
    if rays_: o += rays(x, b - 110 * s, 26, 70 * s, 260 * s, color="#FFFDF0", op=0.4, sw=max(2, 4 * s))
    return o + robed(p, x, b, s, WHITE, skin=JESUS_SKIN, mantle="#C8D2E6", up=up, flip=flip, extra=ex)

def candlestick(x, b, s=1.0, lit=True, color=GOLD):
    """A golden lampstand: a spreading foot, a shaft with two knops, the bowl of the lamp and its flame."""
    o = [f'<path d="M{f(x - 20 * s)} {f(b)} C {f(x - 16 * s)} {f(b - 8 * s)} {f(x - 6 * s)} {f(b - 12 * s)} {f(x - 4 * s)} {f(b - 16 * s)} L {f(x + 4 * s)} {f(b - 16 * s)} '
         f'C {f(x + 6 * s)} {f(b - 12 * s)} {f(x + 16 * s)} {f(b - 8 * s)} {f(x + 20 * s)} {f(b)} Z" fill="{color}" stroke="{INK}" stroke-width="{f(max(1.2, 2 * s))}"></path>',
         f'<rect x="{f(x - 3 * s)}" y="{f(b - 98 * s)}" width="{f(6 * s)}" height="{f(84 * s)}" fill="{color}" stroke="{INK}" stroke-width="{f(max(1, 1.6 * s))}"></rect>']
    for k in (36, 66):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(b - k * s)}" rx="{f(7 * s)}" ry="{f(4 * s)}" fill="{color}" stroke="{INK}" stroke-width="{f(max(1, 1.5 * s))}"></ellipse>')
    o.append(f'<path d="M{f(x - 14 * s)} {f(b - 104 * s)} C {f(x - 12 * s)} {f(b - 94 * s)} {f(x + 12 * s)} {f(b - 94 * s)} {f(x + 14 * s)} {f(b - 104 * s)} Z" '
             f'fill="{color}" stroke="{INK}" stroke-width="{f(max(1.2, 1.8 * s))}"></path>')
    if lit:
        o.append(halo(x, b - 114 * s, 26 * s, "#FFE680", 0.5)
                 + f'<path d="M{f(x)} {f(b - 128 * s)} C {f(x + 7 * s)} {f(b - 118 * s)} {f(x + 6 * s)} {f(b - 106 * s)} {f(x)} {f(b - 104 * s)} '
                 f'C {f(x - 6 * s)} {f(b - 106 * s)} {f(x - 7 * s)} {f(b - 118 * s)} {f(x)} {f(b - 128 * s)} Z" fill="#FFB02E" stroke="#C8401A" stroke-width="{f(max(0.8, 1.2 * s))}"></path>'
                 f'<path d="M{f(x)} {f(b - 121 * s)} C {f(x + 3 * s)} {f(b - 114 * s)} {f(x + 3 * s)} {f(b - 109 * s)} {f(x)} {f(b - 107 * s)} C {f(x - 3 * s)} {f(b - 109 * s)} {f(x - 3 * s)} {f(b - 114 * s)} {f(x)} {f(b - 121 * s)} Z" fill="#FFF4C2"></path>')
    return "".join(o)

def rocks(x0, x1, base, hh, seed, color="#6A5A5A", dark="#4A3E44", n=None):
    """A rocky shore: jagged boulders and ledges."""
    r = random.Random(seed); o = []; n = n or max(3, int((x1 - x0) / (hh * 0.9 + 1)))
    for i in range(n):
        cx = x0 + (x1 - x0) * (i + r.uniform(0.1, 0.9)) / n; rw = hh * r.uniform(0.5, 1.0); rh = hh * r.uniform(0.4, 1.0)
        d = (f"M{f(cx - rw)} {f(base)} L {f(cx - rw * 0.8)} {f(base - rh * 0.6)} L {f(cx - rw * 0.3)} {f(base - rh)} L {f(cx + rw * 0.2)} {f(base - rh * 0.9)} "
             f"L {f(cx + rw * 0.7)} {f(base - rh * 0.5)} L {f(cx + rw)} {f(base)} Z")
        o.append(f'<path d="{d}" fill="{r.choice([color, dark])}" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(cx - rw * 0.3)} {f(base - rh)} L {f(cx - rw * 0.1)} {f(base - rh * 0.4)}" stroke="#2A2228" stroke-width="1.4" opacity="0.6"></path>')
    return "".join(o)

def foam(w, y, seed, n=10, color="#E8F4F8"):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(x)} {f(y + r.uniform(-4, 4))} q 10 -6 20 0 q 10 6 20 0" fill="none" stroke="{color}" stroke-width="2" opacity="0.8"></path>'
                   for x in (r.uniform(-10, w) for _ in range(n)))

# ---- Patmos and the seven churches -----------------------------------------------------------------------------------------
CITIES = {"PATMOS": (26.57, 37.32), "EPHESUS": (27.34, 37.94), "SMYRNA": (27.14, 38.42), "PERGAMUM": (27.18, 39.12), "THYATIRA": (27.84, 38.92),
          "SARDIS": (28.04, 38.49), "PHILADELPHIA": (28.52, 38.35), "LAODICEA": (29.11, 37.84)}
_AT = {"PATMOS": (12, 4, "start"), "EPHESUS": (-9, 14, "end"), "SMYRNA": (-9, 4, "end"), "PERGAMUM": (0, -12, "middle"), "THYATIRA": (9, -6, "start"),
       "SARDIS": (-9, 14, "end"), "PHILADELPHIA": (9, -6, "start"), "LAODICEA": (0, 18, "middle")}
PATMOS_ISLE = [(26.52, 37.37), (26.6, 37.35), (26.62, 37.31), (26.58, 37.27), (26.55, 37.29), (26.54, 37.33)]
ORDER = ["EPHESUS", "SMYRNA", "PERGAMUM", "THYATIRA", "SARDIS", "PHILADELPHIA", "LAODICEA"]

def churches_map(w, h, lit=None, title="THE SEVEN CHURCHES THAT ARE IN ASIA", circuit=True):
    """Patmos and the seven churches of Asia on the map of Acts (act.geo's projection): the letters' circuit from Ephesus
    round to Laodicea in gold, lit= one city lit red."""
    box = (25.6, 30.0, 36.75, 39.6)
    base = geo.med_map(w, h, box=box, regions=(("ASIA", 29.2, 39.25), ("ÆGEAN SEA", 25.95, 38.1), ("LYDIA", 28.6, 38.75), ("CARIA", 28.4, 37.35)),
                       title=title, dots=False)
    P = geo.Proj(w, h, box)
    o = [base, f'<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in (P(*q) for q in PATMOS_ISLE)) + ' Z" fill="#3A4A3A" stroke="#8FD0E2" stroke-width="1.6"></path>']
    if circuit:
        o.append(route([P(*CITIES["PATMOS"])] + [P(*CITIES[c]) for c in ORDER], color="#FFD23F", sw=2.2))
    for nm, (lon, lat) in CITIES.items():
        x, y = P(lon, lat); c = "#FF6A4A" if nm == lit or (nm == "PATMOS" and lit is None) else "#FFD23F"
        dx, dy, an = _AT[nm]
        o.append(node(x, y, "", c, r=4.2 if c == "#FFD23F" else 5.5, size=9) + geo.label(x + dx, y + dy, nm, c, 10, an))
    return "".join(o)

def patmos(p, w, h, seed, stage="stand"):
    """The isle that is called Patmos: a rocky headland over the sea at evening (dawn for "dawn"), John on the rock.
    stage "stand" (John looking out to sea), "write" (sitting on the rock, the book on his knee), "turn" (turned toward
    the great voice behind him, a burst of light at the right), "dawn" (an angel of light over the sea, John far off)."""
    r = random.Random(seed)
    top, bot = {"dawn": ("#3A3A7A", "#FFC890"), "turn": ("#2A2A5A", "#E8B880")}.get(stage, ("#3A2A5A", "#E8906A"))
    hz = h * 0.56
    o = [defs(p), sky(w, h, top, bot), starfield(w, h, seed, 30, 0.35)]
    o.append(halo(w * 0.22, hz - h * 0.04, h * 0.3, "#FFE6A0", 0.55) + f'<circle cx="{f(w * 0.22)}" cy="{f(hz - h * 0.02)}" r="{f(h * 0.06)}" fill="#FFE6A0"></circle>')
    o.append(f'<path d="M{f(w * 0.02)} {f(hz)} L {f(w * 0.1)} {f(hz - h * 0.05)} L {f(w * 0.17)} {f(hz - h * 0.02)} L {f(w * 0.24)} {f(hz)} Z" fill="#5A4A6A" stroke="{INK}" stroke-width="1.6"></path>')   # a far isle
    o.append(sea(w, h, hz, seed, color="#2A5A7A", deep="#0F2E4A"))
    o.append(foam(w, hz + (h - hz) * 0.3, seed, 6))
    # the headland at the right: cliffs rising from the sea, the rock John stands on
    cx = w * 0.62
    d = (f"M{f(cx - w * 0.2)} {f(h + 10)} L {f(cx - w * 0.16)} {f(h * 0.8)} L {f(cx - w * 0.08)} {f(h * 0.74)} L {f(cx)} {f(h * 0.7)} L {f(cx + w * 0.08)} {f(h * 0.52)} "
         f"L {f(cx + w * 0.18)} {f(h * 0.42)} L {f(cx + w * 0.3)} {f(h * 0.36)} L {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h + 10)} Z")
    o.append(f'<path d="{d}" fill="#7A5A4A" stroke="{INK}" stroke-width="2.6"></path>')
    for k in range(5):
        y = h * (0.48 + k * 0.1)
        o.append(f'<path d="M{f(cx + w * 0.02 + k * 8)} {f(y)} L {f(w + 10)} {f(y - 10)}" stroke="#5A3E34" stroke-width="2" opacity="0.6"></path>')
    o.append(f'<path d="M{f(cx + w * 0.22)} {f(h * 0.62)} C {f(cx + w * 0.24)} {f(h * 0.5)} {f(cx + w * 0.32)} {f(h * 0.5)} {f(cx + w * 0.33)} {f(h * 0.64)} Z" fill="#1E140F" stroke="{INK}" stroke-width="2"></path>')   # a cave in the rock
    o.append(rocks(cx - w * 0.26, cx + w * 0.02, h + 4, h * 0.12, seed + 3))
    o.append(foam(cx - w * 0.2, h * 0.94, seed + 1, 4))
    b = h * 0.7 + 2
    s = min(1.0, (h * 0.42) / 205)
    if stage == "write":
        o.append(f'<path d="M{f(cx - 36 * s)} {f(b)} L {f(cx - 30 * s)} {f(b - 50 * s)} L {f(cx + 34 * s)} {f(b - 52 * s)} L {f(cx + 40 * s)} {f(b)} Z" fill="#6A4A3E" stroke="{INK}" stroke-width="2"></path>')
        o.append(john_fig(p, cx, b, s, pose="sit", seat=None, flip=False,
                          extra='<rect x="-58" y="-70" width="26" height="18" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="1.6" transform="rotate(-14 -45 -61)"></rect>'))
    elif stage == "turn":
        o.append(halo(w * 0.96, h * 0.3, h * 0.7, WHITE, 0.8) + rays(w * 0.96, h * 0.3, 28, h * 0.1, w * 0.7, "#FFFDF0", 0.35, 4))
        o.append(john_fig(p, cx + w * 0.04, b - h * 0.03, s, flip=True, up=[(-22, -158), (-40, -172), (-34, -192)]))
    elif stage == "dawn":
        o.append(angel(p, w * 0.3, hz + h * 0.02, (hz * 0.8) / 205, up=[(-22, -158), (-44, -176), (-62, -196)]))
        o.append(john_fig(p, cx + w * 0.02, b, s * 0.8, flip=False))
    else:
        o.append(john_fig(p, cx + w * 0.02, b, s, flip=False))
    o.append(birds(3, w * 0.3, w * 0.5, h * 0.1, h * 0.3, seed, 0.5, 0.9))
    return "".join(o)

def clouds_coming(p, w, h, seed):
    """Behold, he cometh with the clouds (1:7): great clouds lit from within, rays falling through them, and the tribes of
    the earth on the plain below, small, looking up."""
    r = random.Random(seed)
    hz = h * 0.74
    o = [defs(p), sky(w, h, "#2A2A5A", "#C8A8B8"), halo(w * 0.5, h * 0.28, w * 0.6, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.28, 30, h * 0.15, w, "#FFFDF0", 0.3, 5)]
    for k in range(9):
        cx = w * (0.08 + 0.84 * k / 8) + r.uniform(-20, 20); cy = h * (0.3 + 0.12 * math.sin(k * 1.3)); rw = w * r.uniform(0.1, 0.16)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rw)}" ry="{f(rw * 0.32)}" fill="#F3EEF4" stroke="#B8A8C8" stroke-width="2" opacity="0.92"></ellipse>')
    o.append(halo(w * 0.5, h * 0.3, h * 0.2, WHITE, 0.95))
    o.append(hills(w, h, hz - h * 0.04, seed, color="#4A3A5A", amp=10, step=80) + ground(w, h, hz, "#5A4A4A", dy=0))
    o.append(crowd(p, w * 0.04, w * 0.96, h * 0.97, h * 0.8, 22, seed, up=[(-22, -158), (-40, -176), (-52, -198)]))
    return "".join(o)

def alpha_omega(w, h, seed):
    """I am the Alpha and the Omega, saith the Lord God (1:8): no figure — the light, and the first and last letters."""
    o = [radiance(w, h, seed, cy=0.5)]
    for x, ch in ((w * 0.34, "Α"), (w * 0.66, "Ω")):
        o.append(f'<text x="{f(x)}" y="{f(h * 0.5 + h * 0.16)}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{f(h * 0.5)}" fill="#FFF8DC" '
                 f'stroke="#C8962E" stroke-width="3" opacity="0.92">{ch}</text>')
    return "".join(o)

def son_of_man(p, w, h, seed, stage="stand"):
    """The seven golden candlesticks and one like unto a son of man in the midst of them (1:12–20): Jesus in blinding white
    light, the golden girdle at the breasts, the seven stars about his right hand. "stand": the whole scene, the
    candlesticks in an arc; "near": closer, he fills the height; "fallen": John fallen at his feet as one dead, the right
    hand laid upon him."""
    o = [defs(p), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1A4A"></rect>',
         halo(w * 0.5, h * 0.5, max(w, h) * 0.8, "#FFF4C2", 0.8), rays(w * 0.5, h * 0.45, 40, h * 0.1, max(w, h), "#FFFDF0", 0.35, 6)]
    b = h * 0.96
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(b)}" rx="{f(w * 0.48)}" ry="{f(h * 0.06)}" fill="#FFF4C2" opacity="0.5"></ellipse>')
    if stage == "stand":
        s_c = min(1.3, h * 0.45 / 128)
        xs = [w * (0.08 + 0.84 * i / 6) for i in range(7)]
        back = [1, 2, 4, 5]                                   # an arc: the outer ones nearer, the middle ones behind him
        for i in back: o.append(candlestick(xs[i], b - h * 0.1, s_c * 0.82))
        o.append(christ(p, w * 0.5, b - h * 0.03, (h * 0.86) / 205, up=UP_STARS, flip=True, girdle=True, stars=True))
        for i in (0, 3, 6):
            if i == 3: continue
            o.append(candlestick(xs[i], b, s_c))
    elif stage == "near":
        s = (h * 1.05) / 205
        o.append(candlestick(w * 0.12, b, min(1.6, h * 0.7 / 128)) + candlestick(w * 0.88, b, min(1.6, h * 0.7 / 128)))
        o.append(candlestick(w * 0.26, b - h * 0.08, min(1.2, h * 0.55 / 128)) + candlestick(w * 0.74, b - h * 0.08, min(1.2, h * 0.55 / 128)))
        o.append(christ(p, w * 0.5, h * 1.08, s, up=UP_STARS, flip=True, girdle=True, stars=True))
    else:
        s = (h * 0.84) / 205
        for i, x in enumerate((0.07, 0.17, 0.83, 0.93)): o.append(candlestick(w * x, b - (h * 0.06 if i in (1, 2) else 0), min(1.2, h * 0.5 / 128)))
        o.append(christ(p, w * 0.58, b, s, up=UP_HAND, girdle=True))
        o.append(john_fallen(w * 0.38, b, s * 0.95))
    return "".join(o)

def mystery(w, h):
    """The mystery of the seven stars and the seven golden candlesticks (1:20; 2:1): a technical plate, the seven stars
    above, the seven candlesticks below, each pair named for its church — the stars the angels of the churches, the
    candlesticks the churches."""
    import exo.art8 as B
    B._W[0] = w
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE MYSTERY OF THE SEVEN STARS AND THE SEVEN GOLDEN CANDLESTICKS")]
    s = min(1.0, (h - 120) * 0.5 / 128)
    for i, nm in enumerate(ORDER):
        x = w * (0.09 + 0.82 * i / 6)
        o.append(halo(x, h * 0.22, 22, "#FFF4C2", 0.5) + star(x, h * 0.22, 11, "#FFF4C2"))
        o.append(f'<path d="M{f(x)} {f(h * 0.22 + 16)} L {f(x)} {f(h * 0.86 - 128 * s - 8)}" stroke="#8FD0E2" stroke-width="1" stroke-dasharray="3 4"></path>')
        o.append(candlestick(x, h * 0.86, s))
        o.append(label(x, h * 0.86 + 16, nm, "#FFD23F", 9))
    o.append(label(w * 0.5, h * 0.22 - 22, "THE SEVEN STARS · THE ANGELS OF THE SEVEN CHURCHES", "#8FD0E2", 9))
    o.append(label(w * 0.5, h - 10, "THE SEVEN CANDLESTICKS · SEVEN CHURCHES", "#8FD0E2", 9))
    return "".join(o)

# ---- the seven churches ------------------------------------------------------------------------------------------------------
def medallion(cx, cy, r, inner, ring="#E8B830", bg="#1A1A3A", name=None):
    """A gold-ringed roundel holding an emblem (inner: svg drawn about (0, 0) at radius 1), the city's name under it."""
    o = [f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r + 6)}" fill="{ring}" stroke="{INK}" stroke-width="2.4"></circle>',
         f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{bg}" stroke="{INK}" stroke-width="2"></circle>',
         f'<g transform="translate({f(cx)} {f(cy)}) scale({f(r)})">{inner}</g>']
    if name:
        wd = len(name) * 8.4 + 18
        o.append(f'<rect x="{f(cx - wd / 2)}" y="{f(cy + r + 2)}" width="{f(wd)}" height="18" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 + label(cx, cy + r + 15, name, INK, 10))
    return "".join(o)

def _em(kind):
    """The emblems, drawn in a unit circle (stroke widths in those units)."""
    if kind == "lampstand":
        return ""                                             # drawn in the panel's own units (church())
    if kind == "crown":                                       # a wreath crown of life
        o = '<path d="M-0.62 0.1 C -0.66 -0.3 -0.4 -0.58 0 -0.62 C 0.4 -0.58 0.66 -0.3 0.62 0.1" fill="none" stroke="#3F7A34" stroke-width="0.09"></path>'
        for i in range(9):
            a = math.pi * (1.05 + 0.9 * i / 8); x, y = 0.62 * math.cos(a), 0.62 * math.sin(a) + 0.06
            o += f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="0.13" ry="0.06" transform="rotate({f(math.degrees(a) + 90)} {f(x)} {f(y)})" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="0.02"></ellipse>'
        return o + '<path d="M-0.5 0.2 L 0.5 0.2 L 0.42 0.42 L -0.42 0.42 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.03"></path>'
    if kind == "stone":                                       # the white stone, a new name written on it, and the hidden manna
        return ('<ellipse cx="0" cy="0.08" rx="0.56" ry="0.44" fill="#F8F6EE" stroke="#0D0D0F" stroke-width="0.04"></ellipse>'
                '<path d="M-0.32 0 L 0.3 0 M-0.26 0.16 L 0.2 0.16" stroke="#8A7A5A" stroke-width="0.05" stroke-dasharray="0.1 0.05"></path>'
                '<path d="M-0.18 -0.62 L 0.18 -0.62 L 0.24 -0.34 L -0.24 -0.34 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.03"></path>')
    if kind == "morning":
        return halo(0, 0, 0.8, "#FFF4C2", 0.6) + star(0, 0, 0.62, "#FFF4C2", 0.03) + star(0, 0, 0.3, "#FFFFFF", 0.0, "#FFFFFF")
    if kind == "garments":                                    # white garments, and the book of life
        return ('<path d="M-0.18 -0.6 L 0.18 -0.6 L 0.5 -0.4 L 0.4 -0.24 L 0.26 -0.3 L 0.3 0.5 L -0.3 0.5 L -0.26 -0.3 L -0.4 -0.24 L -0.5 -0.4 Z" '
                'fill="#FFFFFF" stroke="#0D0D0F" stroke-width="0.04"></path><path d="M-0.06 -0.56 L 0 -0.44 L 0.06 -0.56" fill="none" stroke="#0D0D0F" stroke-width="0.03"></path>')
    if kind == "door":                                        # a door opened, which none can shut; the key of David
        return ('<rect x="-0.34" y="-0.56" width="0.5" height="1.06" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="0.04"></rect>'
                '<path d="M-0.34 -0.56 L -0.62 -0.46 L -0.62 0.6 L -0.34 0.5 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="0.04"></path>'
                '<circle cx="0.36" cy="0.0" r="0.1" fill="none" stroke="#E8B830" stroke-width="0.06"></circle><path d="M0.36 0.1 L 0.36 0.5 M0.36 0.36 L 0.46 0.36 M0.36 0.46 L 0.46 0.46" stroke="#E8B830" stroke-width="0.06"></path>')
    if kind == "gold":                                        # gold refined by fire, white garments, eyesalve
        return ('<path d="M-0.56 0.2 L -0.44 -0.04 L -0.04 -0.04 L 0.08 0.2 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.03"></path>'
                '<path d="M-0.42 -0.06 L -0.32 -0.28 L 0.0 -0.28 L 0.06 -0.06 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="0.03"></path>'
                '<path d="M0.2 -0.5 L 0.4 -0.5 L 0.38 -0.4 C 0.5 -0.34 0.52 0.1 0.46 0.2 L 0.14 0.2 C 0.08 0.1 0.1 -0.34 0.22 -0.4 Z" fill="#8FD0E2" stroke="#0D0D0F" stroke-width="0.03"></path>'
                '<path d="M-0.5 0.3 L 0.5 0.3 L 0.44 0.5 L -0.44 0.5 Z" fill="#FFFFFF" stroke="#0D0D0F" stroke-width="0.03"></path>')
    return ""

EMBLEM = {"ephesus": "lampstand", "smyrna": "crown", "pergamum": "stone", "thyatira": "morning", "sardis": "garments", "philadelphia": "door", "laodicea": "gold"}

def colonnade(x0, x1, base, hh, color="#E8DCC0", n=None):
    n = n or max(4, int((x1 - x0) / (hh * 0.28)))
    o = [f'<rect x="{f(x0)}" y="{f(base - hh)}" width="{f(x1 - x0)}" height="{f(hh * 0.12)}" fill="{color}" stroke="{INK}" stroke-width="1.8"></rect>']
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        o.append(f'<rect x="{f(x - hh * 0.04)}" y="{f(base - hh * 0.88)}" width="{f(hh * 0.08)}" height="{f(hh * 0.88)}" fill="{color}" stroke="{INK}" stroke-width="1.4"></rect>')
    return "".join(o)

def temple(cx, base, wd, hh, color="#E8DCC0"):
    """A temple front of the Greek cities: steps, columns, a pediment."""
    o = [f'<rect x="{f(cx - wd / 2)}" y="{f(base - hh * 0.1)}" width="{f(wd)}" height="{f(hh * 0.1)}" fill="{color}" stroke="{INK}" stroke-width="1.8"></rect>']
    o.append(colonnade(cx - wd * 0.44, cx + wd * 0.44, base - hh * 0.1, hh * 0.68, color, n=max(3, int(wd / (hh * 0.22)))))
    o.append(f'<path d="M{f(cx - wd * 0.5)} {f(base - hh * 0.78)} L {f(cx)} {f(base - hh)} L {f(cx + wd * 0.5)} {f(base - hh * 0.78)} Z" fill="{color}" stroke="{INK}" stroke-width="1.8"></path>')
    return "".join(o)

def theatre(cx, base, r, color="#D8C8A0"):
    """A Greek theatre cut into the hillside: tiers in a half-ring, the stage building in front."""
    o = [f'<path d="M{f(cx - r)} {f(base)} A {f(r)} {f(r * 0.55)} 0 0 1 {f(cx + r)} {f(base)} Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>']
    for k in range(1, 6):
        rr = r * (1 - k * 0.15)
        o.append(f'<path d="M{f(cx - rr)} {f(base)} A {f(rr)} {f(rr * 0.55)} 0 0 1 {f(cx + rr)} {f(base)}" fill="none" stroke="#8A7A5A" stroke-width="1.4"></path>')
    o.append(f'<rect x="{f(cx - r * 0.6)}" y="{f(base - r * 0.12)}" width="{f(r * 1.2)}" height="{f(r * 0.14)}" fill="#C8B888" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def houses(x0, x1, base, hh, seed, colors=("#E8D8B8", "#D8C8A0", "#E0CCA8", "#C8B890"), lit=False):
    """Flat-roofed white houses climbing a slope (base may be a function of x)."""
    r = random.Random(seed); o = []; x = x0
    while x < x1:
        bw = hh * r.uniform(0.5, 0.9); bh = hh * r.uniform(0.45, 0.8); b = base(x) if callable(base) else base
        o.append(f'<rect x="{f(x)}" y="{f(b - bh)}" width="{f(bw)}" height="{f(bh + 2)}" fill="{r.choice(colors)}" stroke="{INK}" stroke-width="1.4"></rect>'
                 f'<rect x="{f(x + bw * 0.4)}" y="{f(b - bh * 0.6)}" width="{f(bw * 0.18)}" height="{f(bh * 0.24)}" fill="{"#FFC14D" if lit else "#3A2A1E"}"></rect>')
        x += bw * r.uniform(0.75, 1.0)
    return "".join(o)

def church(p, w, h, seed, city, tone="day"):
    """A church's city, its emblem in a gold-ringed medallion at the top right, a golden lampstand in the foreground
    (the candlestick that is the church, 1:20)."""
    r = random.Random(seed)
    tops = {"day": ("#6AB0D8", "#F3E8C8"), "dusk": ("#3A2A5A", "#E8906A"), "night": ("#0B0B2A", "#2A2A5A")}
    top, bot = tops[tone]
    hz = h * 0.6
    o = [defs(p), sky(w, h, top, bot)]
    if tone != "day": o.append(starfield(w, h, seed, 30, 0.4))
    if city == "ephesus":                                     # the harbour, the colonnaded street, the theatre on the hillside
        o.append(hills(w, h, hz - h * 0.18, seed, color="#8A9A6A", amp=26, step=110))
        o.append(theatre(w * 0.66, hz - h * 0.04, h * 0.28))
        o.append(houses(w * 0.3, w * 0.98, lambda x: hz - h * 0.02 - (x - w * 0.3) * 0.05, h * 0.12, seed))
        o.append(sea(w, h, hz + h * 0.04, seed, color="#3A8AB0", deep="#1F5A7A"))
        o.append(f'<path d="M{f(w * 0.28)} {f(hz + h * 0.04)} L {f(w + 10)} {f(hz - h * 0.02)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#C8B888" stroke="{INK}" stroke-width="2"></path>')
        o.append(colonnade(w * 0.36, w * 0.98, hz + h * 0.2, h * 0.14))
        o.append(ship(w * 0.14, hz + h * 0.2, min(0.7, h / 500)))
    elif city == "smyrna":                                    # the bay, and mount Pagus with its crown of buildings
        o.append(f'<path d="M{f(w * 0.3)} {f(hz)} C {f(w * 0.42)} {f(hz - h * 0.36)} {f(w * 0.78)} {f(hz - h * 0.38)} {f(w * 0.94)} {f(hz)} Z" fill="#9A8A6A" stroke="{INK}" stroke-width="2.2"></path>')
        o.append(walls(w * 0.46, w * 0.78, hz - h * 0.26, h * 0.1, seed, towers=4, gate=False, houses=False))
        o.append(houses(w * 0.36, w * 0.94, lambda x: hz + h * 0.02 - max(0, h * 0.12 - abs(x - w * 0.62) * 0.3), h * 0.1, seed))
        o.append(sea(w, h, hz + h * 0.04, seed, color="#3A8AB0", deep="#1F5A7A"))
        o.append(ship(w * 0.18, hz + h * 0.22, min(0.6, h / 520)) + ship(w * 0.86, hz + h * 0.3, min(0.5, h / 600), flip=True))
    elif city == "pergamum":                                  # the steep acropolis, temples and the great altar on its terraces
        o.append(f'<path d="M{f(w * 0.2)} {f(hz + h * 0.05)} L {f(w * 0.36)} {f(h * 0.3)} L {f(w * 0.5)} {f(h * 0.2)} L {f(w * 0.66)} {f(h * 0.26)} L {f(w * 0.86)} {f(hz + h * 0.05)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>')
        o.append(temple(w * 0.5, h * 0.21, w * 0.14, h * 0.13) + temple(w * 0.4, h * 0.32, w * 0.1, h * 0.1))
        o.append(f'<rect x="{f(w * 0.56)}" y="{f(h * 0.34)}" width="{f(w * 0.14)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.8"></rect>'
                 + colonnade(w * 0.56, w * 0.7, h * 0.34, h * 0.06))
        o.append(hills(w, h, hz + h * 0.04, seed, color="#7A8A5A", amp=8, step=90) + houses(w * 0.2, w * 0.86, hz + h * 0.08, h * 0.08, seed))
        o.append(ground(w, h, hz + h * 0.1, "#9A9A6A", dy=0))
    elif city == "thyatira":                                  # a trading town on the plain, the dyers' purple cloth drying, a river
        o.append(hills(w, h, hz - h * 0.08, seed, color="#8A8AA0", amp=14, step=100))
        o.append(walls(w * 0.4, w * 0.92, hz + h * 0.04, h * 0.18, seed, towers=3))
        o.append(ground(w, h, hz + h * 0.04, "#A8A86A", dy=0))
        for k in range(5):
            x = w * (0.08 + 0.06 * k)
            o.append(f'<path d="M{f(x)} {f(hz + h * 0.06)} L {f(x)} {f(hz + h * 0.28)}" stroke="#5A3A22" stroke-width="3"></path>')
        o.append(f'<path d="M{f(w * 0.08)} {f(hz + h * 0.08)} L {f(w * 0.32)} {f(hz + h * 0.08)}" stroke="#5A3A22" stroke-width="2"></path>')
        for k, c in enumerate(("#6A1A6A", "#8A2A7A", "#5A1A5A", "#A8325A")):
            x = w * (0.1 + 0.055 * k)
            o.append(f'<path d="M{f(x)} {f(hz + h * 0.08)} L {f(x + w * 0.045)} {f(hz + h * 0.08)} L {f(x + w * 0.042)} {f(hz + h * 0.24)} L {f(x + 3)} {f(hz + h * 0.25)} Z" fill="{c}" stroke="{INK}" stroke-width="1.4"></path>')
        o.append(f'<path d="M-10 {f(h * 0.92)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.98)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A8AB0" stroke="{INK}" stroke-width="2"></path>')
    elif city == "sardis":                                    # the citadel on its sheer crag above the town, the river below
        o.append(f'<path d="M{f(w * 0.28)} {f(hz + h * 0.06)} L {f(w * 0.36)} {f(h * 0.3)} L {f(w * 0.42)} {f(h * 0.26)} L {f(w * 0.46)} {f(h * 0.14)} L {f(w * 0.6)} {f(h * 0.12)} '
                 f'L {f(w * 0.64)} {f(h * 0.3)} L {f(w * 0.74)} {f(h * 0.36)} L {f(w * 0.8)} {f(hz + h * 0.06)} Z" fill="#B88A6A" stroke="{INK}" stroke-width="2.4"></path>')
        for k in range(4):
            o.append(f'<path d="M{f(w * (0.4 + 0.06 * k))} {f(h * 0.2)} L {f(w * (0.38 + 0.07 * k))} {f(hz)}" stroke="#7A5A4A" stroke-width="2" opacity="0.7"></path>')
        o.append(walls(w * 0.45, w * 0.61, h * 0.14, h * 0.08, seed, towers=2, gate=False, houses=False))
        o.append(houses(w * 0.04, w * 0.96, hz + h * 0.12, h * 0.1, seed) + ground(w, h, hz + h * 0.12, "#A89A6A", dy=0))
        o.append(f'<path d="M-10 {f(h * 0.94)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.98)} {f(w + 10)} {f(h * 0.92)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A040" stroke="{INK}" stroke-width="2"></path>')
    elif city == "philadelphia":                              # a small town at the edge of the plain, vineyards, dark hills behind
        o.append(hills(w, h, hz - h * 0.14, seed, color="#4A3A3A", amp=24, step=90))
        o.append(walls(w * 0.5, w * 0.88, hz + h * 0.02, h * 0.18, seed, towers=2))
        o.append(ground(w, h, hz + h * 0.02, "#9AA86A", dy=0))
        for k in range(3):
            y = hz + h * (0.12 + k * 0.1)
            o.append("".join(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 14)}" stroke="#5A3A22" stroke-width="2"></path><ellipse cx="{f(x)}" cy="{f(y - 16)}" rx="9" ry="6" fill="#3F7A34" stroke="{INK}" stroke-width="1.2"></ellipse>'
                         for x in range(int(w * 0.04), int(w * 0.46), 26)))
    elif city == "laodicea":                                  # the rich city, its aqueduct of stone pipes on arches, the white terraces far off
        o.append(hills(w, h, hz - h * 0.12, seed, color="#8A8A9A", amp=18, step=100))
        o.append(f'<path d="M{f(w * 0.04)} {f(hz - h * 0.08)} L {f(w * 0.08)} {f(hz - h * 0.14)} L {f(w * 0.2)} {f(hz - h * 0.12)} L {f(w * 0.24)} {f(hz - h * 0.06)} Z" fill="#F3F3F0" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(walls(w * 0.46, w * 0.96, hz + h * 0.02, h * 0.2, seed, towers=3, color="#D8C8A0"))
        o.append(temple(w * 0.7, hz - h * 0.14, w * 0.12, h * 0.1))
        o.append(ground(w, h, hz + h * 0.02, "#A8A070", dy=0))
        y0 = hz + h * 0.1
        o.append(f'<rect x="-10" y="{f(y0 - h * 0.1)}" width="{f(w * 0.5)}" height="{f(h * 0.24)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="-10" y="{f(y0 - h * 0.1)}" width="{f(w * 0.5)}" height="{f(h * 0.035)}" fill="#A8987A" stroke="{INK}" stroke-width="1.6"></rect>')
        for k in range(6):                                    # the arches, the ground seen through them
            x = w * (0.0 + 0.08 * k) + w * 0.012; aw = w * 0.056
            o.append(f'<path d="M{f(x)} {f(y0 + h * 0.14)} L {f(x)} {f(y0 - h * 0.02)} A {f(aw / 2)} {f(aw / 2)} 0 0 1 {f(x + aw)} {f(y0 - h * 0.02)} L {f(x + aw)} {f(y0 + h * 0.14)} Z" fill="#A8A070" stroke="{INK}" stroke-width="1.6"></path>')
    if city in EMBLEM:
        rr = min(h * 0.17, 54)
        o.append(medallion(w - rr - 22, rr + 18, rr, _em(EMBLEM[city]), name=city.upper()))
        if EMBLEM[city] == "lampstand": o.append(candlestick(w - rr - 22, rr + 18 + rr * 0.8, rr * 1.45 / 128))
    o.append(candlestick(w * 0.06 if city != "ephesus" else w * 0.04, h * 0.98, min(1.0, h * 0.4 / 128)))
    return "".join(o)

def door(p, w, h, seed):
    """Behold, I stand at the door and knock (3:20): evening, a house with its door shut and a lamp in the window, Jesus
    (ntcast's look, risen, in light) standing at the door, his hand raised to knock."""
    hz = h * 0.82
    o = [defs(p), sky(w, h, "#1E1A4A", "#C87A5A"), starfield(w, h, seed, 30, 0.5)]
    o.append(hills(w, h, hz - h * 0.1, seed, color="#3A2A4A", amp=12, step=90))
    hx0, hx1, ht = w * 0.5, w * 0.94, h * 0.66
    o.append(f'<rect x="{f(hx0)}" y="{f(hz - ht)}" width="{f(hx1 - hx0)}" height="{f(ht)}" fill="#C8B08A" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(hx0 - 8)}" y="{f(hz - ht - 10)}" width="{f(hx1 - hx0 + 16)}" height="12" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    dx0, dw, dh = hx0 + (hx1 - hx0) * 0.14, (hx1 - hx0) * 0.24, ht * 0.62
    o.append(f'<rect x="{f(dx0)}" y="{f(hz - dh)}" width="{f(dw)}" height="{f(dh)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(dx0 + dw * k / 4)} {f(hz - dh)} L {f(dx0 + dw * k / 4)} {f(hz)}" stroke="#4A2412" stroke-width="1.6"></path>' for k in (1, 2, 3))
             + f'<circle cx="{f(dx0 + dw * 0.82)}" cy="{f(hz - dh * 0.5)}" r="3.5" fill="#C8963E" stroke="{INK}" stroke-width="1"></circle>')
    wx = hx0 + (hx1 - hx0) * 0.62
    o.append(f'<rect x="{f(wx)}" y="{f(hz - ht * 0.7)}" width="{f((hx1 - hx0) * 0.2)}" height="{f(ht * 0.24)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>'
             + halo(wx + (hx1 - hx0) * 0.1, hz - ht * 0.58, ht * 0.3, "#FFC14D", 0.35))
    o.append(ground(w, h, hz, "#4A3A3A", dy=0))
    s = (h * 0.7) / 205
    o.append(christ(p, dx0 + dw * 0.3 - 50 * s, hz + 2, s, up=[(-22, -158), (-38, -150), (-50, -150)], flip=True, rays_=False))
    return "".join(o)

def morning_star(w, h, seed, hz=0.74):
    """The morning star (2:28; 22:16): the sky before dawn over the hills, one star bright and low in the east."""
    o = [sky(w, h, "#0B0B2A", "#E8906A"), starfield(w, h, seed, 50, hz * 0.8)]
    x, y = w * 0.62, h * (hz - 0.2)
    o.append(halo(x, y, h * 0.28, "#FFF4C2", 0.7) + rays(x, y, 16, 12, h * 0.36, "#FFFDF0", 0.5, 2) + star(x, y, h * 0.06, "#FFFFFF", 1.2, "#C8962E"))
    o.append(hills(w, h, h * hz, seed, color="#2A1E3A", amp=16, step=90) + hills(w, h, h * (hz + 0.1), seed + 1, color="#1A1428", amp=10, step=70))
    return "".join(o)

def pillar(w, h, seed):
    """A pillar in the temple of my God (3:12): a white column in light, lines of writing cut on it (no words), the
    colonnade going back on either side."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8DCC0"></rect>', halo(w * 0.5, h * 0.4, max(w, h) * 0.6, WHITE, 0.9),
         rays(w * 0.5, h * 0.35, 30, h * 0.1, max(w, h), "#FFFDF0", 0.5, 5)]
    for k, x in enumerate((0.08, 0.2, 0.8, 0.92)):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.12)}" width="28" height="{f(h * 0.82)}" fill="#F3EEE0" stroke="{INK}" stroke-width="2" opacity="0.7"></rect>')
    cw = min(w * 0.14, 90)
    o.append(f'<rect x="{f(w * 0.5 - cw / 2)}" y="{f(h * 0.06)}" width="{f(cw)}" height="{f(h * 0.88)}" fill="#FFFFFF" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(w * 0.5 - cw * 0.7)}" y="{f(h * 0.02)}" width="{f(cw * 1.4)}" height="{f(h * 0.06)}" fill="#F3EEE0" stroke="{INK}" stroke-width="2.2"></rect>'
             f'<rect x="{f(w * 0.5 - cw * 0.7)}" y="{f(h * 0.92)}" width="{f(cw * 1.4)}" height="{f(h * 0.06)}" fill="#F3EEE0" stroke="{INK}" stroke-width="2.2"></rect>')
    for k in range(3):
        y = h * (0.26 + 0.2 * k)
        o.append(f'<path d="M{f(w * 0.5 - cw * 0.34)} {f(y)} L {f(w * 0.5 + cw * 0.34)} {f(y)} M{f(w * 0.5 - cw * 0.26)} {f(y + 10)} L {f(w * 0.5 + cw * 0.26)} {f(y + 10)}" '
                 f'stroke="#C8962E" stroke-width="3" stroke-dasharray="7 3 12 3"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.96)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

FRUITS = ["#D7261E", "#E8B830", "#FF8A3D", "#8A2A7A", "#9CCB5E", "#F3EFE6", "#C8401A", "#5A1A5A", "#FFD23F", "#E86A8A", "#3A8AB0", "#B5652E"]

def tree_life(cx, b, s, seed=1, fruit=True):
    """The tree of life: a broad trunk, a great round crown of leaves, and twelve manner of fruits in it (2:7; 22:2)."""
    r = random.Random(seed); o = []
    o.append(f'<path d="M{f(cx - 16 * s)} {f(b)} C {f(cx - 10 * s)} {f(b - 50 * s)} {f(cx - 14 * s)} {f(b - 90 * s)} {f(cx - 30 * s)} {f(b - 120 * s)} L {f(cx - 18 * s)} {f(b - 124 * s)} '
             f'C {f(cx - 4 * s)} {f(b - 104 * s)} {f(cx + 4 * s)} {f(b - 104 * s)} {f(cx + 18 * s)} {f(b - 124 * s)} L {f(cx + 30 * s)} {f(b - 120 * s)} '
             f'C {f(cx + 14 * s)} {f(b - 90 * s)} {f(cx + 10 * s)} {f(b - 50 * s)} {f(cx + 16 * s)} {f(b)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="{f(max(1.6, 2.4 * s))}"></path>')
    blobs = [(0, -170, 70), (-60, -150, 52), (60, -150, 52), (-36, -200, 50), (36, -200, 50), (0, -225, 44), (-84, -128, 36), (84, -128, 36)]
    for dx, dy, rr in blobs:
        o.append(f'<circle cx="{f(cx + dx * s)}" cy="{f(b + dy * s)}" r="{f(rr * s)}" fill="#2E7A3A" stroke="{INK}" stroke-width="{f(max(1.4, 2 * s))}"></circle>')
    for dx, dy, rr in blobs:
        o.append(f'<circle cx="{f(cx + (dx - rr * 0.2) * s)}" cy="{f(b + (dy - rr * 0.25) * s)}" r="{f(rr * 0.6 * s)}" fill="#4A9A4A"></circle>')
    if fruit:
        for i in range(24):
            dx, dy, rr = blobs[i % len(blobs)]
            a = r.uniform(0, 2 * math.pi); d = r.uniform(0.2, 0.8) * rr
            o.append(f'<circle cx="{f(cx + (dx + d * math.cos(a)) * s)}" cy="{f(b + (dy + d * math.sin(a)) * s)}" r="{f(6 * s)}" fill="{FRUITS[i % 12]}" stroke="{INK}" stroke-width="{f(max(0.8, 1.2 * s))}"></circle>')
    return "".join(o)

def paradise(w, h, seed):
    """The tree of life, which is in the Paradise of God (2:7): the tree in a garden full of light."""
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), halo(w * 0.5, h * 0.3, w * 0.6, WHITE, 0.8), rays(w * 0.5, h * 0.3, 24, h * 0.1, w, "#FFFDF0", 0.4, 4)]
    o.append(hills(w, h, h * 0.78, seed, color="#7AB86A", amp=10, step=90) + ground(w, h, h * 0.86, "#9CCB5E", dy=0))
    for x in (0.12, 0.24, 0.78, 0.9): o.append(olive(w * x, h * 0.9, min(0.8, h / 400), seed=int(x * 100)))
    o.append(tree_life(w * 0.5, h * 0.96, h * 0.9 / 270, seed))
    return "".join(o)

def emblem_plate(w, h, seed, inner, r=None, bg=("#1A1440", "#3A2A6A")):
    """An emblem in a great gold-ringed medallion over a burst of light (the promises to him that overcometh)."""
    rr = r or min(h * 0.36, w * 0.2)
    o = [sky(w, h, *bg), radiance(w, h, seed, cy=0.5)]
    o.append(medallion(w * 0.5, h * 0.5, rr, inner, bg="#12113A"))
    return "".join(o)

def white_stone(w, h, seed):
    """The hidden manna and a white stone with a new name written on it (2:17)."""
    return emblem_plate(w, h, seed, _em("stone"))

def crown_life(w, h, seed):
    """Be thou faithful unto death, and I will give thee the crown of life (2:10)."""
    return emblem_plate(w, h, seed, _em("crown"))

def book_life(w, h, seed):
    """Arrayed in white garments; the book of life, open (3:5): the white garment and the open book in light."""
    book = ('<path d="M-0.62 0.2 L -0.02 0.3 L -0.02 0.62 L -0.62 0.5 Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="0.03"></path>'
            '<path d="M0.62 0.2 L 0.02 0.3 L 0.02 0.62 L 0.62 0.5 Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="0.03"></path>'
            + "".join(f'<path d="M-0.54 {f(0.3 + k * 0.07)} L -0.1 {f(0.38 + k * 0.07)} M0.54 {f(0.3 + k * 0.07)} L 0.1 {f(0.38 + k * 0.07)}" stroke="#8A7A5A" stroke-width="0.02"></path>' for k in range(3)))
    robe = ('<path d="M-0.14 -0.66 L 0.14 -0.66 L 0.4 -0.5 L 0.32 -0.36 L 0.2 -0.42 L 0.24 0.12 L -0.24 0.12 L -0.2 -0.42 L -0.32 -0.36 L -0.4 -0.5 Z" '
            'fill="#FFFFFF" stroke="#0D0D0F" stroke-width="0.03"></path>')
    return emblem_plate(w, h, seed, robe + book)

def throne_light(w, h, seed, rainbow=False):
    """A throne in white light, empty — no one drawn upon it (3:21; God is never drawn): steps of light, rays."""
    o = [sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.5, h * 0.5, max(w, h) * 0.7, "#FFF4C2", 0.85), rays(w * 0.5, h * 0.45, 36, h * 0.1, max(w, h), "#FFFDF0", 0.35, 5)]
    if rainbow:
        for k, c in enumerate(("#2E9A5A", "#5AC88A", "#9CE8B8")):
            rr = h * (0.5 - k * 0.04)
            o.append(f'<path d="M{f(w * 0.5 - rr)} {f(h * 0.7)} A {f(rr)} {f(rr)} 0 0 1 {f(w * 0.5 + rr)} {f(h * 0.7)}" fill="none" stroke="{c}" stroke-width="{f(h * 0.035)}" opacity="0.85"></path>')
    cx, b = w * 0.5, h * 0.92; s = h / 330
    for k in range(3):
        o.append(f'<rect x="{f(cx - (90 - k * 18) * s)}" y="{f(b - (k + 1) * 14 * s)}" width="{f((180 - k * 36) * s)}" height="{f(14 * s)}" fill="#FFF4C2" stroke="#C8962E" stroke-width="2"></rect>')
    y0 = b - 42 * s
    o.append(f'<path d="M{f(cx - 44 * s)} {f(y0)} L {f(cx - 44 * s)} {f(y0 - 150 * s)} C {f(cx - 40 * s)} {f(y0 - 176 * s)} {f(cx + 40 * s)} {f(y0 - 176 * s)} {f(cx + 44 * s)} {f(y0 - 150 * s)} L {f(cx + 44 * s)} {f(y0)} Z" '
             f'fill="#FFF8DC" stroke="#C8962E" stroke-width="3"></path>'
             f'<rect x="{f(cx - 56 * s)}" y="{f(y0 - 60 * s)}" width="{f(112 * s)}" height="{f(16 * s)}" fill="#FFE680" stroke="#C8962E" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(cx + d * 52 * s - 7 * s)}" y="{f(y0 - 96 * s)}" width="{f(14 * s)}" height="{f(96 * s)}" fill="#FFE680" stroke="#C8962E" stroke-width="2.4"></rect>' for d in (-1, 1)))
    o.append(halo(cx, y0 - 90 * s, 120 * s, WHITE, 0.9))
    return "".join(o)

def holy_city(cx, base, wd, hh, seed, glow_=True):
    """The holy city, new Jerusalem, seen from without: the wall great and high of jasper (pale green-gold light), three of
    its twelve gates of pearl in the face toward us, towers, and the light of the city within (21:11–21)."""
    o = []
    if glow_: o.append(halo(cx, base - hh * 0.5, wd * 0.9, "#FFF4C2", 0.75))
    x0, x1, top = cx - wd / 2, cx + wd / 2, base - hh
    o.append(f'<path d="M{f(x0 + wd * 0.1)} {f(top - hh * 0.18)} L {f(x1 - wd * 0.1)} {f(top - hh * 0.18)} L {f(x1)} {f(top)} L {f(x0)} {f(top)} Z" fill="#F3F0D8" stroke="#C8A040" stroke-width="2"></path>')
    for k in range(9):                                        # the light of the city rising within the wall
        bx = x0 + wd * (0.1 + 0.8 * k / 8); bh = hh * (0.2 + 0.25 * math.sin(k * 1.7) ** 2)
        o.append(f'<rect x="{f(bx - wd * 0.03)}" y="{f(top - bh)}" width="{f(wd * 0.06)}" height="{f(bh)}" fill="#FFF8DC" stroke="#E8C060" stroke-width="1.4"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(wd)}" height="{f(hh)}" fill="#CFE8C8" stroke="#8A9A5A" stroke-width="2.4"></rect>')
    for k in range(1, 6):                                     # courses of the jasper wall
        o.append(f'<path d="M{f(x0)} {f(top + hh * k / 6)} L {f(x1)} {f(top + hh * k / 6)}" stroke="#A8C8A0" stroke-width="1.2"></path>')
    for k in range(4):
        tx = x0 + wd * k / 3
        o.append(f'<rect x="{f(tx - wd * 0.035)}" y="{f(top - hh * 0.12)}" width="{f(wd * 0.07)}" height="{f(hh * 1.12)}" fill="#DCEFD4" stroke="#8A9A5A" stroke-width="2"></rect>')
    for k in range(3):
        gx = x0 + wd * (k + 0.5) / 3; gw = wd * 0.07
        o.append(f'<path d="M{f(gx - gw)} {f(base)} L {f(gx - gw)} {f(base - hh * 0.5)} A {f(gw)} {f(gw)} 0 0 1 {f(gx + gw)} {f(base - hh * 0.5)} L {f(gx + gw)} {f(base)} Z" fill="#FFFFFF" stroke="#C8B8C8" stroke-width="2.4"></path>'
                 f'<path d="M{f(gx - gw * 0.6)} {f(base)} L {f(gx - gw * 0.6)} {f(base - hh * 0.46)} A {f(gw * 0.6)} {f(gw * 0.6)} 0 0 1 {f(gx + gw * 0.6)} {f(base - hh * 0.46)} L {f(gx + gw * 0.6)} {f(base)} Z" fill="#FFF4C2" stroke="#E8D8E8" stroke-width="1.6"></path>')
    return "".join(o)

def cover_city(w, h, seed):
    """The cover: the holy city coming down out of heaven in light over the new earth (21:2, 21:10)."""
    o = [sky(w, h, "#1A1440", "#FFE6A0"), starfield(w, h, seed, 50, 0.4), halo(w * 0.5, h * 0.42, w * 0.8, "#FFF4C2", 0.8),
         rays(w * 0.5, h * 0.42, 36, h * 0.1, w * 1.2, "#FFFDF0", 0.35, 5)]
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.66)}" rx="{f(w * 0.55)}" ry="{f(h * 0.06)}" fill="#FFFFFF" opacity="0.6"></ellipse>')
    o.append(holy_city(w * 0.5, h * 0.64, w * 0.66, h * 0.24, seed))
    o.append(hills(w, h, h * 0.84, seed, color="#5A8A5A", amp=12, step=90) + ground(w, h, h * 0.9, "#7AA86A", dy=0))
    return "".join(o)
