"""Drawings for the Acts volume. Acts starts from all of Mark's and Matthew's drawings (`from mrk.art9 import *`, which carries
mrk.art … mrk.art8 and mat.art … mat.art11: Jerusalem and the temple, the houses and rooms, the roads, the lake, the tomb,
the cloud of light) and adds its own people and places.

The people at a distance (each the same in every chapter): Jesus only ever ntcast.jesus_fig (risen: mat.art11.jesus_risen,
white light); the apostles in ntcast.ROBES — Peter bareheaded, his short hair and beard dark grey, a brown robe; John young
and beardless in rust; James in tan with a headcloth; Paul (and Saul before he was called, the same man) a dark-brown robe
and headcloth with a cord and a black beard. Acts' own people are listed in act/__init__.py. Angels are figures of white
light with a gold rim and no face (mat.art.angel); God, Satan and demons are never drawn — the Spirit at Pentecost is the
rushing wind and small tongues of flame-light resting over each head.

scene(p, w, h, seed, place, people) composes most panels: a place (PLACES below) and the people standing in it, each
(x, who[, options]) with who a name in WHO, "crowd" (n figures), or "man"/"woman"/"seated"/"kneel" with a colour. Every
function takes (p, w, h, seed, ...) — p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from mrk.art9 import *
from mrk.art9 import f, INK, HEB, TWELVE, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, light_seated
from mat.art import UP_BLESS, UP_HIGH, UP_TOUCH, UP_CALL, angel, woman_fig, scribe_fig, bgr, room, houses, temple, pavement, jerusalem_far, lake, shore, boat
from mat.art3 import centurion_fig
from mat.art2 import soldier_fig
from genesis.art2 import WHITE_BEARD, fit, ground, hills, SKIN
from genesis.art3 import label, sun
from genesis.art4 import clay_lamp
from jer.art import glow, shaft
from sa2.art import sky
from oba.minor import walls, crowd, halo, rays, starfield, scroll, olive, fig_tree, sea as sea_, vista, cup
from job.art import seated, clouds, smoke
from kg1.art import ship
import mk, exodus as E
from exo import art as A
from num.art import ALL
from ntcast import jesus_fig, ROBES, JESUS_TUNIC, JESUS_MANTLE, JESUS_SKIN, JESUS_HAIR
from act import geo

# ---- heads, beards and figures --------------------------------------------------------------------------------------------
def beard(color): return WHITE_BEARD.replace("#E8E2D6", color)
def hair(color): return f'<path d="M-13.5 -186 C -16 -206 16 -206 13.5 -186 C 9 -195 -9 -195 -13.5 -186 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.3"></path>'
def band(color="#E8B830"): return f'<path d="M-14 -194 C -6 -198 6 -198 14 -194" fill="none" stroke="{color}" stroke-width="3.4"></path>'
def diadem(color="#E8B830"):
    return (f'<path d="M-14 -194 L -14 -204 L -9 -198 L -4 -207 L 0 -199 L 4 -207 L 9 -198 L 14 -204 L 14 -194 C 6 -197 -6 -197 -14 -194 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.2"></path>')
TOGA_HAIR = '<path d="M-13 -192 C -12 -204 12 -204 13 -192 C 8 -196 -8 -196 -13 -192 Z" fill="%s"></path>'
HELM = ('<path d="M-14 -190 C -14 -206 14 -206 14 -190 L 14 -180 L -14 -180 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.6"></path>'
        '<path d="M-20 -204 L 20 -204" stroke="#B5121B" stroke-width="7" stroke-linecap="round"></path>')

def man_fig(p, x, y, s, cloth, head=None, cord="#3A2214", bd=None, hr=None, kind="Robe", flip=False, up=None, body=SKIN, extra=""):
    """A man at a distance: robe or tunic in `cloth`; head= a headcloth colour (cord= its cord, None for none), else hr= his
    hair colour; bd= his beard colour."""
    ex = (A.headcloth(head, cord=cord) if head else hair(hr) if hr else "") + (beard(bd) if bd else "") + extra
    return mk.person(p, round(x), round(y), round(s, 3), body=body, cloth=cloth, kind=kind, sw=3, flip=flip, up=up, extra=ex)

def toga_fig(p, x, y, s, hr="#4A3A2A", border="#6A1A5A", cloth="#F3EFE6", flip=False, up=None, extra=""):
    """A Roman of rank (a proconsul, a governor, a magistrate): a white toga with a coloured border, bareheaded, clean-shaven."""
    b = f'<path d="M-24 -160 C -10 -150 6 -120 14 -40 L 22 -40 C 14 -120 0 -156 -14 -164 Z" fill="{border}" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#E3B08A", cloth=cloth, kind="Robe", sw=3, flip=flip, up=up, extra=b + TOGA_HAIR % hr + extra)

def king_fig(p, x, y, s, cloth="#5A1A6A", hr="#2A1A10", bd="#2A1A10", flip=False, up=None):
    """A king of the Herods at a distance: a royal robe, a gold diadem."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Robe", sw=3, flip=flip, up=up,
                     extra=hair(hr) + diadem() + (beard(bd) if bd else ""))

# the recurring people of Acts at a distance (see act/__init__.py)
def peter(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, ROBES["peter"], hr="#2A2420", bd="#4A4440", flip=flip, up=up)
def john_ap(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, ROBES["john"], hr="#2A1A10", flip=flip, up=up)
def james_ap(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, ROBES["james"], head="#8A5A3A", bd="#1A1210", flip=flip, up=up)
def paul(p, x, y, s, flip=False, up=None, kind="Robe"): return man_fig(p, x, y, s, ROBES["paul"], head="#5A4A3A", cord="#2A1A10", bd="#3A2A1A", flip=flip, up=up, kind=kind)
saul = paul
def barnabas(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#3A6A3A", head="#3A6A3A", cord="#2A1A10", bd="#4A2A1A", flip=flip, up=up)
def silas(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#2A4A6A", head="#2A4A6A", cord="#1A1210", bd="#2A1A10", flip=flip, up=up)
def timothy(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#7A8A9A", hr="#3A2214", flip=flip, up=up, kind="Tunic")
def stephen(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#2A6A5A", hr="#2A1A10", bd="#2A1A10", flip=flip, up=up)
def philip_ev(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#2A6A6A", head="#2A6A6A", cord="#1A1210", bd="#2A1A10", flip=flip, up=up)
def matthias(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#8A6A3A", head="#8A6A3A", bd="#3A2A1A", flip=flip, up=up)
def barsabbas(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#5A6A7A", head="#E8E2D6", bd="#5A4A3A", flip=flip, up=up)
def priest(p, x, y, s, flip=False, up=None): return scribe_fig(p, x, y, s, white=True, flip=flip, up=up)
def scribe(p, x, y, s, flip=False, up=None): return scribe_fig(p, x, y, s, white=False, flip=flip, up=up)
def elder(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#3A2A4A", head="#3A2A4A", cord="#E8B830", bd="#7A746A", flip=flip, up=up)
def soldier(p, x, y, s, flip=False, up=None): return soldier_fig(p, x, y, s, flip=flip, up=up)
def centurion(p, x, y, s, flip=False, up=None): return centurion_fig(p, x, y, s, flip=flip, up=up)
def officer(p, x, y, s, flip=False, up=None):
    """An officer of the temple (the captain's men): a grey-blue tunic, a dark headcloth, a staff."""
    return man_fig(p, x, y, s, "#4A5A6A", head="#2A2A3A", cord=None, bd="#1A1210", kind="Tunic", flip=flip, up=up,
                   extra='<path d="M30 -150 L 44 -230" stroke="#5A3A22" stroke-width="5"></path>')

WHO = {"peter": peter, "john": john_ap, "james": james_ap, "paul": paul, "saul": saul, "barnabas": barnabas, "silas": silas, "timothy": timothy,
       "stephen": stephen, "philip": philip_ev, "matthias": matthias, "barsabbas": barsabbas, "priest": priest, "scribe": scribe, "elder": elder,
       "soldier": soldier, "centurion": centurion, "officer": officer,
       "jesus": lambda p, x, y, s, flip=False, up=None: jesus_fig(p, x, y, s, flip=flip, up=up),
       "risen": lambda p, x, y, s, flip=False, up=None: jesus_risen(p, x, y, s, flip=flip, up=up),
       "angel": lambda p, x, y, s, flip=False, up=None: angel(p, x, y, s, flip=flip, up=up)}

def apostle(p, x, y, s, i, flip=False, up=None):
    """One of the eleven (twelve) at a distance, by place: 0 Peter, 1 John, 2 James, then the others in Matthew's colours."""
    if i == 0: return peter(p, x, y, s, flip=flip, up=up)
    if i == 1: return john_ap(p, x, y, s, flip=flip, up=up)
    if i == 2: return james_ap(p, x, y, s, flip=flip, up=up)
    c = [ROBES["andrew"], ROBES["matthew"], ROBES["thomas"], "#4A6A4A", "#7A5A2A", "#5A5A7A", "#6A3A3A", "#3A5A5A", "#8A6A3A"][(i - 3) % 9]
    heads = ["#6A7A5A", "#3A5A6A", "#5A4A6A", None, "#E8E2D6", None, "#6A5A3A", None, "#8A6A3A"]
    hd = heads[(i - 3) % 9]
    return man_fig(p, x, y, s, c, head=hd, hr=None if hd else "#2A1A10", bd=["#3A2A1A", "#1A1210", "#2A1A10"][i % 3], flip=flip, up=up)

def flame_tongue(x, y, s=1.0):
    """A tongue like as of fire resting over a head: a small flame of light with a white heart and a soft glow."""
    return (f'<circle cx="{f(x)}" cy="{f(y - 10 * s)}" r="{f(26 * s)}" fill="#FFE680" opacity="0.25"></circle>'
            + E.flame(x, y, 9 * s, 34 * s, 2 * s, layers=(("#FF8A3D", 1.0), ("#FFD23F", 0.72), ("#FFF4C2", 0.42))))

# ---- places ------------------------------------------------------------------------------------------------------------
def _upper(w, h, seed, night_=False):
    b = h * 0.92
    o = [room(w, h, b, wall="#C8A878" if not night_ else "#3A2E3A", floor="#8A6A4A", window=(w * 0.78, w * 0.08), night_=night_, seed=seed),
         f'<path d="M{f(w * 0.06)} {f(h * 0.1)} L {f(w * 0.06)} {f(b)}" stroke="#6A4A2A" stroke-width="10"></path>',
         A.lamp(w * 0.5, h * 0.18, max(0.6, h / 360)) if night_ else ""]
    return "".join(o), b

def _temple(w, h, seed, tone="day"):
    b = h * 0.94
    top, bot = {"day": ("#8FD0E2", "#FFF4C2"), "dusk": ("#4A2A5A", "#FFB07A"), "dawn": ("#3A3A7A", "#FFC890")}[tone]
    return sky(w, h, top, bot) + temple(w * 0.66, h * 0.54, w * 0.56) + pavement(w, h, h * 0.54), b

def _porch(w, h, seed, tone="day"):
    """Solomon's porch: a long colonnade of white columns under a cedar roof, the court before it."""
    b = h * 0.94
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#8A5A3A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(9):
        x = w * (0.04 + 0.115 * k)
        o.append(f'<rect x="{f(x - 12)}" y="{f(h * 0.16)}" width="24" height="{f(h * 0.4)}" fill="#F8F4EC" stroke="{INK}" stroke-width="1.8"></rect>'
                 f'<rect x="{f(x - 16)}" y="{f(h * 0.16)}" width="32" height="8" fill="#D8C8A0" stroke="{INK}" stroke-width="1.2"></rect>')
    o.append(pavement(w, h, h * 0.56))
    return "".join(o), b

def _street(w, h, seed, tone="day"):
    b = h * 0.94
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#4A2A5A", "#FFB07A"), "night": ("#0B0B2A", "#2A2050"), "dawn": ("#3A3A7A", "#FFC890")}[tone]
    o = [sky(w, h, top, bot)]
    if tone == "night": o.append(mk.stars(30, w, h * 0.3, seed))
    o += [houses(w, h, h * 0.66, seed, hmin=0.3, hmax=0.46, lit=tone == "night"), pavement(w, h, h * 0.66, color="#C8B898" if tone != "night" else "#4A4248")]
    return "".join(o), b

def _gate(w, h, seed, tone="day"):
    b = h * 0.94
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#4A2A5A", "#FFB07A"), "night": ("#0B0B2A", "#2A2050")}[tone]
    return sky(w, h, top, bot) + walls(w * 0.3, w + 10, h * 0.64, h * 0.4, seed, towers=2, lit=tone == "night") + ground(w, h, h * 0.64, "#C8B07A" if tone != "night" else "#3A3440", dy=0), b

def _road(w, h, seed, tone="day"):
    b = h * 0.94
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#4A2A5A", "#FFB07A"), "noon": ("#5AB0D8", "#FFF4C2")}[tone]
    o = [sky(w, h, top, bot), hills(w, h, h * 0.42, seed, color="#9A8A6A" if tone != "dusk" else "#5A4A5A", amp=16, step=90),
         hills(w, h, h * 0.52, seed + 1, color="#B8A06A" if tone != "dusk" else "#6A5A4A", amp=10, step=70), ground(w, h, h * 0.6, "#D8C08A" if tone != "dusk" else "#8A6A4A", dy=0),
         f'<path d="M{f(-10)} {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.78)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.64)}" stroke="#E8D8B0" stroke-width="{f(max(10, h * 0.08))}" fill="none"></path>']
    return "".join(o), b

def _hall(w, h, seed, tone="day"):
    """A hall of judgment or a council chamber: columns, a lamp, the stone floor."""
    b = h * 0.94
    wall = {"day": "#B8A07A", "council": "#4A3A44", "night": "#2A1A2A", "roman": "#C8B8A0"}[tone]
    o = [bgr(w, h, wall)]
    for x in (0.06, 0.3, 0.7, 0.94):
        o.append(f'<rect x="{f(w * x - 16)}" y="-10" width="32" height="{f(b + 10)}" fill="{"#E8DCC0" if tone in ("day", "roman") else "#6A5A54"}" stroke="{INK}" stroke-width="2"></rect>')
    if tone in ("council", "night"): o.append(glow(w * 0.5, h * 0.2, h * 0.3, "#FFC14D", 0.4, f"hall{seed}") + A.lamp(w * 0.5, h * 0.18, max(0.6, h / 360)))
    if tone == "roman":
        o.append(f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#A8281E" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b - h * 0.04)}" width="{f(w + 20)}" height="{f(h)}" fill="{"#8A7A6A" if tone in ("day", "roman") else "#4A3A34"}" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o), b

def _hill(w, h, seed, tone="day"):
    """The mount of Olives: the hilltop with olive trees, Jerusalem across the valley."""
    b = h * 0.94
    top, bot = {"day": ("#8FD0E2", "#FFF4C2"), "dusk": ("#4A2A5A", "#FFB07A")}[tone]
    o = [sky(w, h, top, bot), hills(w, h, h * 0.5, seed, color="#9A9A7A", amp=10, step=90),
         walls(w * 0.52, w * 0.98, h * 0.56, h * 0.16, seed, towers=3), temple(w * 0.72, h * 0.44, w * 0.18),
         f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A8A4A" stroke="{INK}" stroke-width="2"></path>',
         olive(w * 0.06, h * 0.86, h / 420, seed=seed)]
    return "".join(o), b

def _prison(w, h, seed, tone="night"):
    """A prison cell: stone walls, a barred window high up, the iron door, straw on the floor."""
    b = h * 0.92
    o = [bgr(w, h, "#3A3238")]
    for k in range(9):
        y = h * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A2228" stroke-width="2"></path>')
        for j in range(8):
            x = w * (j + (k % 2) * 0.5) / 7
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + h / 8)}" stroke="#2A2228" stroke-width="1.6"></path>')
    wx, wy, ww = w * 0.7, h * 0.12, w * 0.1
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(ww * 0.8)}" fill="#0B0B2A" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(wx + ww * k / 4)} {f(wy)} L {f(wx + ww * k / 4)} {f(wy + ww * 0.8)}" stroke="#6A6A74" stroke-width="3"></path>' for k in (1, 2, 3)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2228" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o), b

def _sea(w, h, seed, tone="day"):
    b = h * 0.86
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#4A2A5A", "#FFB07A"), "storm": ("#14141E", "#4A4A5E"), "night": ("#0B0B2A", "#2A2050")}[tone]
    return sky(w, h, top, bot) + sea_(w, h, h * 0.56, seed, rough=tone == "storm"), b

def _synagogue(w, h, seed, tone="day"):
    b = h * 0.94
    o = [bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.08, 0.3, 0.7, 0.92):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.13)}" width="28" height="{f(b - h * 0.13)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b - h * 0.08)}" width="{f(w + 20)}" height="{f(h)}" fill="#A8906A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.19)} {f(h * 0.13)} L {f(w * 0.19)} {f(h * 0.3)}" stroke="#4A3A2A" stroke-width="2"></path>' + clay_lamp(w * 0.19, h * 0.34, max(0.6, h / 300)))
    return "".join(o), b

def _house(w, h, seed, tone="day"):
    """Within a house: plastered walls, a doorway of daylight, a lamp on a ledge."""
    b = h * 0.92
    o = [room(w, h, b, wall="#D8C098" if tone == "day" else "#4A3A3A", floor="#8A6A4A" if tone == "day" else "#3A2E2A"),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.26)}" width="{f(w * 0.14)}" height="{f(b - h * 0.26)}" fill="{"#FFE6A0" if tone == "day" else "#0B0B2A"}" stroke="{INK}" stroke-width="2"></rect>',
         A.lamp(w * 0.86, h * 0.3, max(0.6, h / 360))]
    return "".join(o), b

def _wilderness(w, h, seed, tone="day"):
    b = h * 0.94
    return vista(w, h, seed, tone="desert" if tone == "day" else tone, horizon=0.56, hills_n=2), b

PLACES = {"upper": _upper, "upper_night": lambda w, h, s, tone=None: _upper(w, h, s, True), "temple": _temple, "porch": _porch, "street": _street,
          "gate": _gate, "road": _road, "hall": _hall, "hill": _hill, "prison": _prison, "sea": _sea, "synagogue": _synagogue, "house": _house,
          "wilderness": _wilderness}

def scene(p, w, h, seed, place, people=(), tone=None, top=0.26, extra="", lie=False):
    """A place and the people in it. people: (x, who) or (x, who, {opts}): who a name in WHO, ("apostle", i), "crowd" (opts n,
    x1, women), "man"/"woman"/"seated"/"kneel" (opts c= colour, v= veil/head colour, bd= beard). opts: flip, up, k (scale), dy."""
    fn = PLACES[place]
    bg, b = fn(w, h, seed, tone) if tone else fn(w, h, seed)
    o = [mk.defs(p, *ALL, *(LIE if lie else ())), bg, extra]
    s = fit(b, max(h * top, b - 220))
    r = random.Random(seed)
    for spec in people:
        x, who = spec[0], spec[1]; op = spec[2] if len(spec) > 2 else {}
        k = op.get("k", 1.0); yy = b + op.get("dy", 0) * s; fl = op.get("flip", False); up = op.get("up")
        X = w * x; ss = s * k
        if isinstance(who, tuple) and who[0] == "apostle": o.append(apostle(p, X, yy, ss, who[1], flip=fl, up=up))
        elif who == "crowd":
            x1 = op.get("x1", x + 0.3); n = op.get("n", 6)
            o.append(crowd(p, w * x, w * x1, yy, yy - 200 * ss * 0.92, n, seed + int(x * 100), women=op.get("women", 0.35), flip=fl, up=up))
        elif who == "eleven":
            x1 = op.get("x1", x + 0.6); n = op.get("n", 11)
            for i in range(n):
                xi = w * (x + (x1 - x) * i / max(1, n - 1)); yi = yy + (i % 2) * 4
                o.append(apostle(p, xi, yi, ss * (0.96 + 0.04 * (i % 2)), i, flip=op.get("flips", fl) if not callable(op.get("flips")) else op["flips"](i), up=op.get("ups", {}).get(i)))
        elif who == "man": o.append(man_fig(p, X, yy, ss, op.get("c", "#6A5A4A"), head=op.get("v"), hr=op.get("hr", None if op.get("v") else "#2A1A10"), bd=op.get("bd"), flip=fl, up=up, kind=op.get("kind", "Robe")))
        elif who == "woman": o.append(woman_fig(p, X, yy, ss * 0.94, op.get("c", "#6A4A5A"), op.get("v"), flip=fl, up=up))
        elif who == "seated": o.append(seated(X, yy, ss * 0.8, op.get("c", "#6A5A4A"), head=op.get("v"), beard=op.get("bd", "#2A1A10"), flip=fl, bowed=op.get("bowed", False)))
        elif who == "kneel": o.append(E.kneel(X, yy, ss * 0.9, color=op.get("c", "#6A5A4A"), flip=fl, skin=SKIN))
        elif who == "toga": o.append(toga_fig(p, X, yy, ss, hr=op.get("hr", "#4A3A2A"), border=op.get("border", "#6A1A5A"), flip=fl, up=up))
        elif who == "king": o.append(king_fig(p, X, yy, ss, cloth=op.get("c", "#5A1A6A"), bd=op.get("bd", "#2A1A10"), flip=fl, up=up))
        elif who == "glow":
            o.append(glow(X, yy - 110 * ss, 160 * ss, op.get("c", "#FFFFFF"), 0.9, f"{p}gw{int(X)}"))
        else: o.append(WHO[who](p, X, yy, ss, flip=fl, up=up))
        if op.get("fire"): o.append(flame_tongue(X, yy - 222 * ss, ss * 1.1))
    return "".join(o)

# ---- maps ----------------------------------------------------------------------------------------------------------------
def map_panel(box, places=(), routes=(), hi=(), regions=(), title=None, **k):
    """A technical map for D(): lambda w, h: map_panel(...)(w, h)."""
    return lambda w, h: geo.med_map(w, h, box=box, places=places, routes=routes, hi=hi, regions=regions, title=title, **k)

# ---- Acts 1 --------------------------------------------------------------------------------------------------------------
def treatise(p, w, h, seed):
    """The former treatise to Theophilus: a writing-table by a window, the finished scroll of the gospel rolled and tied, a
    new scroll begun beside it, the reed pen and the inkhorn, a lamp."""
    o = [bgr(w, h, "#C8A878"), f'<rect x="{f(w * 0.68)}" y="{f(h * 0.1)}" width="{f(w * 0.2)}" height="{f(h * 0.4)}" fill="#8FD0E2" stroke="{INK}" stroke-width="3"></rect>',
         f'<path d="M{f(w * 0.78)} {f(h * 0.1)} L {f(w * 0.78)} {f(h * 0.5)} M{f(w * 0.68)} {f(h * 0.3)} L {f(w * 0.88)} {f(h * 0.3)}" stroke="{INK}" stroke-width="3"></path>',
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.5, h / 300)
    o.append(scroll(w * 0.44, h * 0.62 - 50 * k, 220 * k, 80 * k, lines=5))
    cx, cy = w * 0.16, h * 0.62 - 14 * k
    o.append(f'<rect x="{f(cx - 70 * k)}" y="{f(cy - 14 * k)}" width="{f(140 * k)}" height="{f(28 * k)}" rx="{f(14 * k)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(cx - 20 * k)} {f(cy - 14 * k)} L {f(cx - 20 * k)} {f(cy + 14 * k)} M{f(cx + 20 * k)} {f(cy - 14 * k)} L {f(cx + 20 * k)} {f(cy + 14 * k)}" stroke="#B5121B" stroke-width="{f(3 * k)}"></path>')
    o.append(f'<path d="M{f(w * 0.64)} {f(h * 0.62 - 4)} L {f(w * 0.72)} {f(h * 0.62 - 60 * k)}" stroke="#3A2A1A" stroke-width="{f(3 * k)}"></path>'
             f'<rect x="{f(w * 0.6)}" y="{f(h * 0.62 - 22 * k)}" width="{f(16 * k)}" height="{f(22 * k)}" fill="#2A1A10" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(A.lamp(w * 0.9, h * 0.62 - 10 * k, k))
    return "".join(o)

def forty_days(p, w, h, seed):
    """By the space of forty days: Jesus risen in white light speaking with the apostles under the olive trees, the eleven
    sitting about him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.46, seed, color="#9AA07A", amp=12, step=90), ground(w, h, h * 0.6, "#A8A86A", dy=0),
         olive(w * 0.9, h * 0.9, h / 380, seed=seed), olive(w * 0.08, h * 0.86, h / 440, seed=seed + 1)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus_risen(p, w * 0.22, b, s, up=UP_BLESS))
    for i, x in enumerate((0.4, 0.5, 0.6, 0.7, 0.8)):
        o.append(seated(w * x, b, s * 0.78, TWELVE[i], head=TWELVE[i] if i % 2 else None, beard="#4A4440" if i == 0 else "#2A1A10", flip=True))
    return "".join(o)

def olivet_ask(p, w, h, seed):
    """On the mount of Olives: Jesus risen standing with the eleven, Jerusalem across the valley."""
    return scene(p, w, h, seed, "hill", [(0.18, "risen", {"up": UP_BLESS}), (0.34, "eleven", {"x1": 0.62, "n": 6, "flips": True, "k": 0.92})])

def ascension(p, w, h, seed, gone=False):
    """He was taken up; and a cloud received him out of their sight: above the mount, Jesus risen in white light with his
    hands lifted, a great cloud of light coming about him; the eleven on the hilltop looking up. gone=True: only the cloud
    of light, the sky empty above them."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#2A3A7A", "#FFE6A0"), rays(w * 0.5, h * 0.2, 32, 30, max(w, h), color="#FFFDF0", op=0.22),
         glow(w * 0.5, h * 0.24, h * 0.42, "#FFFFFF", 0.95, f"{p}g"),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A8A4A" stroke="{INK}" stroke-width="2"></path>']
    sj = fit(h * 0.46, h * 0.2)
    if not gone:
        o.append(jesus_risen(p, w * 0.5, h * 0.46, sj, up=UP_HIGH))
        o.append(clouds(w, h * 0.46, seed, n=7, color="#FFFDF0", op=0.92, h=h * 0.7))
    else:
        o.append(clouds(w, h * 0.16, seed, n=8, color="#FFFDF0", op=0.9, h=h))
    for i in range(11):
        x = w * (0.06 + 0.088 * i); y = h * 0.88 + (i % 2) * 6
        s = fit(y, y - h * 0.18)
        o.append(apostle(p, x, y, s, i, flip=i > 5, up=[(-22, -158), (-30, -190), (-34, -222)] if i % 3 == 0 else None))
    return "".join(o)

def two_in_white(p, w, h, seed):
    """Two men stood by them in white apparel: on the hilltop the eleven looking up into the empty sky of light; beside them
    two figures of white light with a gold rim, no faces."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A4A8A", "#FFE6A0"), glow(w * 0.6, 0, h * 0.5, "#FFFFFF", 0.7, f"{p}g"), clouds(w, h * 0.1, seed, n=6, color="#FFFDF0", op=0.8, h=h),
         f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.68)} {f(w * 0.7)} {f(h * 0.68)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A8A4A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    for i in range(7):
        o.append(apostle(p, w * (0.36 + 0.09 * i), b - (i % 2) * 6, s * (0.92 + 0.04 * (i % 2)), i, flip=True, up=[(-22, -158), (-30, -190), (-34, -222)] if i in (1, 4) else None))
    o.append(angel(p, w * 0.1, b, s * 1.02, up=UP_BLESS) + angel(p, w * 0.22, b, s * 1.0))
    return "".join(o)

def olivet_road(p, w, h, seed):
    """They returned unto Jerusalem from the mount called Olivet: the road down the hill and across the valley to the city
    gate, the eleven walking on it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE6A0"), walls(w * 0.48, w + 10, h * 0.5, h * 0.24, seed, towers=3), temple(w * 0.76, h * 0.36, w * 0.24),
         ground(w, h, h * 0.5, "#9AA07A", dy=0),
         f'<path d="M-10 {f(h + 10)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.58)} {f(h * 0.5)}" stroke="#E0D0A8" stroke-width="{f(max(10, h * 0.07))}" fill="none"></path>',
         olive(w * 0.08, h * 0.7, h / 500, seed=seed), olive(w * 0.94, h * 0.98, h / 380, seed=seed + 1)]
    for i in range(6):
        t = i / 5; x = w * (0.1 + 0.36 * t); y = h * (0.96 - 0.3 * t)
        o.append(apostle(p, x, y, fit(y, y - h * (0.3 - 0.16 * t)), i))
    return "".join(o)

def upper_chamber(p, w, h, seed, prayer=True, fire=False, wind=False, peter_up=False):
    """The upper chamber: the eleven sitting along the walls under the beams, the women and Mary the mother of Jesus with
    them; prayer=True some with their hands lifted; fire=True a tongue like as of fire resting over each head and the room
    bright; wind=True the sound as of a rushing mighty wind sweeping through (wind strokes); peter_up=True Peter standing up in
    the midst."""
    bg, b = _upper(w, h, seed, night_=False)
    o = [mk.defs(p, *ALL), bg]
    if fire: o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#FFE680" opacity="0.22"></rect>' + glow(w * 0.5, h * 0.3, w * 0.5, "#FFF4C2", 0.6, f"{p}fg"))
    if wind:
        r = random.Random(seed)
        for _ in range(14):
            y = r.uniform(h * 0.08, h * 0.6); x = r.uniform(-w * 0.1, w * 0.7); L = r.uniform(w * 0.2, w * 0.45)
            o.append(f'<path d="M{f(x)} {f(y)} C {f(x + L * 0.3)} {f(y - 18)} {f(x + L * 0.7)} {f(y + 18)} {f(x + L)} {f(y - 4)}" stroke="#FFFFFF" stroke-width="{f(r.uniform(2, 4))}" fill="none" opacity="0.7"></path>')
    s = fit(b, max(h * 0.24, b - 230))
    seats = [0.16, 0.27, 0.38, 0.49, 0.6, 0.71, 0.82, 0.93]
    # the women behind, standing by the wall between the men (Mary the mother of Jesus in blue)
    ws = s * 0.82
    for i, (x, c, vl) in enumerate(((0.325, ROBES["mary"], "#3A6AA8"), (0.545, ROBES["magdalene"], "#4A3A5A"), (0.765, "#6A5A3A", "#3A3A4A"))):
        o.append(woman_fig(p, w * x, b - 26 * s, ws, c, vl, flip=x > 0.5, up=UP_HIGH if prayer and i == 0 else None))
        if fire: o.append(flame_tongue(w * x, b - 26 * s - 222 * ws, s * 0.72))
    for i, x in enumerate(seats):
        c = TWELVE[i % 12]
        if peter_up and i == 0: continue
        o.append(seated(w * x, b, s * 0.76, c, head=c if i % 2 else None, beard="#4A4440" if i == 0 else "#2A1A10", flip=x > 0.55))
        if fire: o.append(flame_tongue(w * x + (-6 if x > 0.55 else 6) * s * 0.76, b - 150 * s * 0.76, s * 0.8))
    if prayer and not fire:
        o.append(apostle(p, w * 0.06, b, s * 0.96, 3, up=UP_HIGH))
    if peter_up:
        o.append(peter(p, w * 0.1, b, s, up=UP_BLESS))
    return "".join(o)

def lots(p, w, h, seed):
    """They gave lots for them; and the lot fell upon Matthias: two lots shaken out of a vessel onto the floor of the upper
    chamber, one lit gold; Joseph Barsabbas and Matthias standing side by side, the eleven about them."""
    bg, b = _upper(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.26, b - 220))
    o.append(barsabbas(p, w * 0.42, b, s) + matthias(p, w * 0.54, b, s, flip=True))
    o.append(glow(w * 0.54, b - 110 * s, 120 * s, "#FFE680", 0.5, f"{p}m"))
    for i, x in enumerate((0.08, 0.18, 0.28)):
        o.append(apostle(p, w * x, b, s * 0.96, i))
    for i, x in enumerate((0.7, 0.8, 0.9)):
        o.append(apostle(p, w * x, b, s * 0.96, i + 3, flip=True))
    k = s
    o.append(f'<path d="M{f(w * 0.46)} {f(b + 2)} L {f(w * 0.5)} {f(b - 30 * k)} L {f(w * 0.52)} {f(b - 30 * k)} L {f(w * 0.56)} {f(b + 2)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="1.6"></path>')
    for x, c in ((0.44, "#8A847A"), (0.6, "#FFD23F")):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(b + 4)}" rx="{f(10 * k)}" ry="{f(5 * k)}" fill="{c}" stroke="{INK}" stroke-width="1.4"></ellipse>')
    return "".join(o)

# ---- Acts 2 --------------------------------------------------------------------------------------------------------------
def wind_house(p, w, h, seed):
    """A sound from heaven as of the rushing of a mighty wind, filling all the house: the house in Jerusalem seen from the
    street, a shaft of light from the sky upon it and the wind streaming about its roof and windows."""
    o = [sky(w, h, "#5A8AC8", "#FFF4C2"), shaft(w * 0.56, w, h, top_w=0.06, bot_w=0.2, op=0.4), houses(w, h, h * 0.86, seed, hmin=0.3, hmax=0.4, stairs=False),
         f'<rect x="{f(w * 0.42)}" y="{f(h * 0.34)}" width="{f(w * 0.28)}" height="{f(h * 0.52)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.3)}" width="{f(w * 0.32)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.47, 0.6):
        o.append(f'<rect x="{f(w * x)}" y="{f(h * 0.42)}" width="{f(w * 0.06)}" height="{f(h * 0.1)}" fill="#FFE680" stroke="{INK}" stroke-width="1.8"></rect>')
    o.append(pavement(w, h, h * 0.86))
    r = random.Random(seed)
    for _ in range(22):
        y = r.uniform(h * 0.04, h * 0.6); x = r.uniform(-w * 0.1, w * 0.9); L = r.uniform(w * 0.12, w * 0.3)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + L * 0.3)} {f(y - 14)} {f(x + L * 0.7)} {f(y + 14)} {f(x + L)} {f(y - 4)}" stroke="#FFFFFF" stroke-width="{f(r.uniform(2, 4))}" fill="none" opacity="0.75"></path>')
    return "".join(o)

def multitude_door(p, w, h, seed, mock=False):
    """The multitude came together: the street before the house thronged with devout men of every nation, in the dress of
    many lands; mock=True some turning away laughing."""
    bg, b = _street(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.26, b - 220))
    r = random.Random(seed)
    heads = ["#F3EFE6", "#1F5FAD", "#E8B830", "#2A5A3A", "#7A1A2A", None, "#5A2A7A", "#C8B080"]
    robes = ["#8A2A2A", "#1F5A6A", "#5A2A7A", "#C8783A", "#2A4A2A", "#6A5A3A", "#3A3A6A", "#9A6A2A"]
    yb = b - 70 * s
    for i in range(9):
        x = w * (0.08 + 0.1 * i) + r.uniform(-8, 8)
        o.append(man_fig(p, x, yb, s * 0.78, r.choice(robes), head=r.choice(heads), hr="#2A1A10", bd=r.choice(["#2A1A10", "#6A645E", None]), flip=r.random() < 0.5))
    for i in range(7):
        x = w * (0.05 + 0.14 * i) + r.uniform(-8, 8)
        hd = r.choice(heads)
        o.append(man_fig(p, x, b, s, r.choice(robes), head=hd, hr="#2A1A10", bd=r.choice(["#2A1A10", "#4A3A2A", None]), flip=(i < 3) if not mock else (i % 2 == 0),
                         up=UP_HIGH if (mock and i in (1, 5)) else None))
    return "".join(o)

NATIONS = (("PARTHIA", 55, 37.2), ("MEDIA", 48.6, 36.4), ("ELAM", 48.6, 31.6), ("MESOPOTAMIA", 42.2, 35.4), ("JUDÆA", 34.4, 30.9, "end"),
           ("CAPPADOCIA", 35.6, 38.6), ("PONTUS", 36.6, 41.0), ("ASIA", 28.0, 38.1), ("PHRYGIA", 30.8, 39.6), ("PAMPHYLIA", 31.2, 36.9),
           ("EGYPT", 30.4, 28.4), ("LIBYA", 22.4, 30.2), ("CRETE", 24.9, 34.4), ("ARABIA", 40.2, 28.8))

def nations(p, w, h, seed):
    """Parthians and Medes and Elamites …: the map from Rome to Parthia, every land the verse names, the routes of the
    pilgrims from each converging on Jerusalem, lit red."""
    pts = [(55, 36.6), (48.6, 35.8), (48.6, 32.2), (42.2, 35.0), (35.6, 38.2), (36.6, 40.6), (28.4, 38.6), (30.8, 39.2), (31.2, 37.3), (30.6, 29.2),
           (22.4, 31.0), (24.9, 35.2), (39.6, 29.4), (12.5, 41.9)]
    routes = [[q, "JERUSALEM"] for q in pts]
    return geo.med_map(w, h, box=(11, 57, 26, 44), places=("JERUSALEM", "ROME", "CYRENE"), routes=routes, hi=("JERUSALEM",), regions=NATIONS,
                       title="ACTS 2:9–11 · EVERY NATION UNDER HEAVEN", rsize=10, size=10, lit_routes=list(range(len(routes))))

def peter_preach(p, w, h, seed, crowd_n=10, tone="day"):
    """Peter standing up with the eleven, lifting up his voice: on the steps before the house, the eleven behind him, the
    multitude below in the street."""
    bg, b = _street(w, h, seed, tone)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.26, b - 220))
    st = b - 40 * s
    o.append(f'<path d="M-10 {f(st)} L {f(w * 0.42)} {f(st)} L {f(w * 0.42)} {f(st + 20 * s)} L {f(w * 0.48)} {f(st + 20 * s)} L {f(w * 0.48)} {f(b + 10)} L -10 {f(b + 10)} Z" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></path>')
    for i in range(1, 6):
        o.append(apostle(p, w * (0.05 + 0.06 * i), st - 4, s * 0.86, i))
    o.append(peter(p, w * 0.36, st, s * 1.02, up=UP_HIGH))
    o.append(crowd(p, w * 0.52, w * 0.98, b, b - 170 * s, crowd_n, seed, flip=True))
    return "".join(o)

def signs_sky(p, w, h, seed):
    """Wonders in the heaven above: the sun turned into darkness — a black disc rimmed with fire — and the moon into blood,
    over the dark hills and the smoke."""
    o = [sky(w, h, "#05050E", "#3A1418"), starfield(w, h, seed, 40, 0.5), hills(w, h, h * 0.7, seed, color="#1A1018", amp=16, step=80), ground(w, h, h * 0.8, "#120A10", dy=0)]
    o.append(glow(w * 0.3, h * 0.32, h * 0.22, "#FF6A2A", 0.6, f"{p}s") + f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.32)}" r="{f(h * 0.1)}" fill="#05050E" stroke="#FF8A3D" stroke-width="3"></circle>')
    o.append(glow(w * 0.72, h * 0.26, h * 0.16, "#D7261E", 0.6, f"{p}m") + f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.26)}" r="{f(h * 0.07)}" fill="#8A0E16" stroke="#D7261E" stroke-width="2"></circle>')
    o.append(smoke(w * 0.5, h * 0.8, 8, seed, color="#3A2A2E", op=0.6, k=max(0.6, h / 300)))
    return "".join(o)

def davids_tomb(p, w, h, seed):
    """His tomb is with us unto this day: the tomb of David cut in the rock of the city, its doorway sealed, the wall above."""
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), walls(-10, w + 10, h * 0.42, h * 0.3, seed, towers=4, gate=False),
         f'<rect x="-10" y="{f(h * 0.42)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A080" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(5):
        y = h * (0.5 + 0.1 * k)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#9A8460" stroke-width="2"></path>')
    cx = w * 0.5
    o.append(f'<path d="M{f(cx - w * 0.12)} {f(h * 0.96)} L {f(cx - w * 0.12)} {f(h * 0.6)} L {f(cx + w * 0.12)} {f(h * 0.6)} L {f(cx + w * 0.12)} {f(h * 0.96)} Z" fill="#6A5A44" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - w * 0.08)}" y="{f(h * 0.68)}" width="{f(w * 0.16)}" height="{f(h * 0.28)}" fill="#1A1210" stroke="{INK}" stroke-width="2"></rect>'
             f'<circle cx="{f(cx + w * 0.02)}" cy="{f(h * 0.82)}" r="{f(h * 0.13)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.4"></circle>'
             f'<path d="M{f(cx - w * 0.14)} {f(h * 0.58)} L {f(cx + w * 0.14)} {f(h * 0.58)}" stroke="#E8B830" stroke-width="4"></path>')
    return "".join(o)

def baptized(p, w, h, seed):
    """About three thousand souls baptized: a great stepped pool of the city (the pools of Jerusalem), the people going down
    into the water in white, the apostles at the steps."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), houses(w, h, h * 0.42, seed, hmin=0.2, hmax=0.3, stairs=False)]
    o.append(f'<rect x="-10" y="{f(h * 0.42)}" width="{f(w + 20)}" height="{f(h)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(4):
        y = h * (0.5 + 0.06 * k)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#A89878" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.74)}" width="{f(w + 20)}" height="{f(h)}" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></rect>')
    o.append(lake(w, h, h * 0.74, seed, color="#2C7DA8", deep="#1F5F8A", n=10))
    s = fit(h * 0.86, h * 0.86 - min(h * 0.5, 190))
    for i, x in enumerate((0.12, 0.3, 0.5, 0.7, 0.88)):
        o.append(man_fig(p, w * x, h * 0.9, s * 0.92, "#F3EFE6", hr="#2A1A10", bd="#2A1A10" if i % 2 else None, flip=i % 2 == 1, up=UP_HIGH if i == 2 else None))
    o.append(f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h)}" fill="#2C7DA8" opacity="0.85"></rect>')
    s2 = fit(h * 0.6, h * 0.6 - min(h * 0.34, 140))
    for i, x in enumerate((0.2, 0.62)):
        o.append(apostle(p, w * x, h * 0.6, s2, i))
    o.append(crowd(p, w * 0.3, w * 0.56, h * 0.56, h * 0.56 - 130 * s2, 5, seed + 3))
    o.append(crowd(p, w * 0.7, w * 0.98, h * 0.56, h * 0.56 - 130 * s2, 4, seed + 4, flip=True))
    return "".join(o)

def breaking_bread(p, w, h, seed):
    """Breaking bread at home with gladness: a low table under the lamp, loaves and a cup, the believers sitting about it,
    men and women together (all on the left, the doorway and the lamp on the right)."""
    from ecc.art import loaf
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#4A3A3A", floor="#3A2E2A"),
         f'<rect x="{f(w * 0.8)}" y="{f(h * 0.26)}" width="{f(w * 0.14)}" height="{f(b - h * 0.26)}" fill="#0B0B2A" stroke="{INK}" stroke-width="2"></rect>',
         A.lamp(w * 0.4, h * 0.22, max(0.6, h / 360)), glow(w * 0.4, h * 0.5, w * 0.36, "#FFC14D", 0.35, f"{p}l")]
    s = fit(b, max(h * 0.3, b - 210))
    ty = b - 40 * s
    for i, x in enumerate((0.06, 0.66)):
        o.append(woman_fig(p, w * x, b - 10 * s, s * 0.86, ["#5A6A4A", "#6A4A5A"][i], ["#2A4A5A", "#3A3A5A"][i], flip=i == 1))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(ty)}" width="{f(w * 0.4)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    o.append(loaf(w * 0.3, ty - 2, s * 0.7) + cup(w * 0.4, ty, s * 0.36) + loaf(w * 0.5, ty - 2, s * 0.7))
    for i, x in enumerate((0.14, 0.24, 0.56, 0.66)):
        c = TWELVE[(i * 3) % 12]
        o.append(seated(w * x, b, s * 0.78, c, head=c if i % 2 else None, beard="#2A1A10" if i != 0 else "#4A4440", flip=x > 0.4))
    return "".join(o)

def all_common(p, w, h, seed):
    """They sold their possessions and goods, and parted them to all: in the court, goods and money laid down — a jar, rolled
    cloth, a sack of grain, a purse — and the believers sharing them out to the poor, a widow and a lame man among them."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.26, b - 220))
    k = s
    cx = w * 0.5
    o.append(f'<path d="M{f(cx - 60 * k)} {f(b)} C {f(cx - 60 * k)} {f(b - 50 * k)} {f(cx - 20 * k)} {f(b - 60 * k)} {f(cx - 20 * k)} {f(b - 70 * k)} L {f(cx - 10 * k)} {f(b - 70 * k)} C {f(cx - 10 * k)} {f(b - 60 * k)} {f(cx + 20 * k)} {f(b - 50 * k)} {f(cx + 20 * k)} {f(b)} Z" fill="#B5652E" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(cx + 26 * k)}" y="{f(b - 30 * k)}" width="{f(70 * k)}" height="{f(30 * k)}" rx="{f(14 * k)}" fill="#3A6AA8" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(cx - 110 * k)} {f(b)} C {f(cx - 120 * k)} {f(b - 40 * k)} {f(cx - 70 * k)} {f(b - 50 * k)} {f(cx - 70 * k)} {f(b)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>'
             f'<circle cx="{f(cx + 110 * k)}" cy="{f(b - 10 * k)}" r="{f(10 * k)}" fill="#8A5A2A" stroke="{INK}" stroke-width="1.6"></circle>')
    o.append(peter(p, w * 0.2, b, s) + john_ap(p, w * 0.3, b, s * 0.98))
    o.append(woman_fig(p, w * 0.72, b, s * 0.9, "#4A4A5A", "#2A2A3A", flip=True, up=UP_TOUCH))
    o.append(man_fig(p, w * 0.84, b, s * 0.92, "#7A7A80", hr="#6A645E", bd="#6A645E", flip=True, extra='<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(man_fig(p, w * 0.94, b, s * 0.94, "#5A6A3A", head="#6A5A3A", bd="#2A1A10", flip=True))
    return "".join(o)
