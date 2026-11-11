"""Drawings for the Romans volume. Romans starts from all of Acts' drawings (`from act.art16 import *`, which carries act.art …
act.art15, Mark's and Matthew's drawings) and from the epistle kit (epistle.py: the study, the sealed scroll, the still life,
the letter's road, the radiance, the technical plate), and adds its own.

Romans' people at a distance: Paul only ever act.art.paul; Tertius (tertius) a young beardless scribe in a dark-teal
headcloth and a teal-grey tunic; Phoebe (phoebe) a deep-blue veil and a grey travelling cloak. God is never drawn (light,
storm, an empty throne); no one is drawn in the panels of 1:24–32. Every function takes (p, w, h, seed, ...) or (w, h,
...); p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from act.art16 import *
from act.art import f, INK, _synagogue, _street, _hall, _road
from act.art10 import statue, philosopher, judgment_bema
from act.art16 import islander, rome
from act.art8 import jupiter_temple
from act.art4 import throne_footstool
from epistle import (study, still_life, sealed_scroll, open_letter, reed_pen, inkpot, lamp_glow, letter_road, plate_bg, radiance, tag, dim,
                     TERTIUS_LOOK, PHOEBE_LOOK, SEPIA, SEAL)
from oba.minor import vista, eagle, halo, rays, starfield, bolt, rain, sea as sea_
from exo.art8 import mercy_seat
from ecc.art import scales
from ezk.art11 import croc
from genesis.art3 import label, node, route
import exodus5 as V

# ---- Romans' cast at a distance -------------------------------------------------------------------------------------------
def tertius(p, x, y, s, flip=False, up=None):
    return man_fig(p, x, y, s, TERTIUS_LOOK["cloth"], head=TERTIUS_LOOK["head"], cord="#0D2A2A", flip=flip, up=up, kind="Tunic")
def phoebe(p, x, y, s, flip=False, up=None):
    return woman_fig(p, x, y, s * 0.94, PHOEBE_LOOK["cloth"], PHOEBE_LOOK["veil"], flip=flip, up=up)
WHO.update({"tertius": tertius, "phoebe": phoebe})

GOLD, CY = "#FFD23F", "#8FD0E2"

def plate_label(x, y, text, color=GOLD, size=10, anchor="middle"):
    """A label on a plate with a dark halo so it reads over the drawing."""
    return label(x, y, text, color, size, anchor).replace("<text ", '<text stroke="#0B1A2E" stroke-width="3" paint-order="stroke" stroke-linejoin="round" ', 1)

# ---- Romans 1 -----------------------------------------------------------------------------------------------------------
def letter_to_rome(w, h, lit=None):
    """The letter's road: from Cenchreæ, the port of Corinth, across the isthmus and the sea, by the Appian Way to Rome."""
    rt = ["CENCHREÆ", "CORINTH", (21.6, 38.3), (19.6, 38.9), (17.9, 40.6), (16.6, 40.9), (15.0, 41.0), (14.0, 41.15), "MARKET OF APPIUS", "ROME"]
    o = letter_road(w, h, rt, title="ROMANS 16:1 · FROM CENCHREÆ TO ROME", box=(11.2, 24.6, 36.4, 42.6), places=("CENCHREÆ", "CORINTH", "MARKET OF APPIUS", "ROME"),
                    hi=("CENCHREÆ", "ROME"), regions=("ITALY", "ACHAIA", "MACEDONIA", "SICILY"))
    import act.geo as G_
    P = G_.Proj(w, h, (11.2, 24.6, 36.4, 42.6))
    x, y = P(18.0, 40.62)
    o = o[:-4] + plate_label(x + 8, y + 16, "BRUNDISIUM", CY, 8, "start") + o[-4:]
    sx, sy = P(19.4, 38.4)
    o = o[:-4] + sealed_scroll(sx, sy, 0.32, rot=-8) + o[-4:]
    return o

def debtors(p, w, h, seed):
    """Debtor both to Greeks and to Barbarians: on the left the colonnade of a Greek city and two philosophers in their
    himations; on the right the shore of a far island, a hut and a fire, two islanders; Paul between them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#9AA07A", amp=14, step=90)]
    o.append(f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w * 0.44)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M-10 {f(h * 0.2)} L {f(w * 0.2)} {f(h * 0.1)} L {f(w * 0.44)} {f(h * 0.2)} Z" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></path>')
    for k in range(5):
        x = w * (0.02 + k * 0.095)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.26)}" width="{f(w * 0.03)}" height="{f(h * 0.34)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(pavement(w * 0.5, h, h * 0.6, color="#D8D0C0"))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.6)} C {f(w * 0.66)} {f(h * 0.56)} {f(w * 0.86)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#B8A06A" stroke="{INK}" stroke-width="2"></path>')
    hx = w * 0.86
    o.append(f'<path d="M{f(hx - w * 0.07)} {f(h * 0.62)} L {f(hx)} {f(h * 0.44)} L {f(hx + w * 0.07)} {f(h * 0.62)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(hx - w * 0.07 + k * w * 0.02)} {f(h * 0.62)} L {f(hx)} {f(h * 0.44)}" stroke="#5A4020" stroke-width="1.4"></path>' for k in range(8)))
    o.append(E.blaze(w * 0.7, b - 4, w * 0.05, h * 0.14, seed, n=5))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(philosopher(p, w * 0.12, b, s, 0) + philosopher(p, w * 0.24, b, s * 0.98, 1))
    o.append(islander(p, w * 0.78, b, s, 0, flip=True) + islander(p, w * 0.92, b, s * 0.97, 2, flip=True))
    o.append(paul(p, w * 0.48, b, s, up=[(22, -158), (46, -150), (70, -156)]))
    o.append(plate_label(w * 0.18, h * 0.08, "GREEKS", "#12113A", 11) + plate_label(w * 0.85, h * 0.08, "BARBARIANS", "#12113A", 11))
    return "".join(o).replace('stroke="#0B1A2E" stroke-width="3" paint-order', 'stroke="#F3EFE6" stroke-width="3" paint-order')

def jew_first(w, h):
    """To the Jew first, and also to the Greek: the light of the gospel going out from Jerusalem in rings over the nations,
    west to Rome."""
    import act.geo as G_
    return G_.med_map(w, h, box=(11.5, 39.5, 30.4, 42.6), places=("JERUSALEM", "ANTIOCH", "EPHESUS", "CORINTH", "ROME"),
                      routes=[["JERUSALEM", "ANTIOCH", "EPHESUS", "CORINTH", "ROME"]], hi=("JERUSALEM",), rings="JERUSALEM", red=True,
                      regions=("SYRIA", "ASIA", "ITALY", "THE GREAT SEA"), title="ROMANS 1:16 · TO THE JEW FIRST, AND ALSO TO THE GREEK")

def wrath(w, h, seed):
    """The wrath of God revealed from heaven: a storm breaking over the bare hills, lightning and rain — nothing struck, no figure."""
    return vista(w, h, seed, tone="storm", horizon=0.66, hills_n=2, bolts=3, rain_=True, far="mount", cx=0.7, cw=0.4)

def creation(w, h, seed):
    """The invisible things of him clearly seen through the things that are made: the night sky and its stars giving way to
    the dawn over the great sea, a mountain, the birds."""
    o = [sky(w, h, "#0B0B2A", "#FFB07A"), starfield(w, h, seed, 70, 0.4), J.moon(w * 0.14, h * 0.14, max(8, h * 0.03)),
         halo(w * 0.74, h * 0.62, max(w, h) * 0.4, "#FFE680", 0.55), sun(w * 0.74, h * 0.62, max(16, h * 0.07), color="#FFE680", op=0.4),
         f'<path d="M{f(w * 0.02)} {f(h * 0.64)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.28)} {f(h * 0.38)} L {f(w * 0.4)} {f(h * 0.22)} L {f(w * 0.58)} {f(h * 0.64)} Z" fill="#3A3A5A" stroke="{INK}" stroke-width="2.2"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.28)} L {f(w * 0.4)} {f(h * 0.22)} L {f(w * 0.44)} {f(h * 0.3)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></path>',
         sea_(w, h, h * 0.64, seed, color="#1F6F9A", deep="#0F4C68"), birds(5, w * 0.5, w * 0.9, h * 0.2, h * 0.45, seed)]
    return "".join(o)

def _bird_idol(x, base, s, color):
    """An image of a bird on a plinth: an eagle with spread wings, gilded."""
    return (f'<rect x="{f(x - 22 * s)}" y="{f(base - 44 * s)}" width="{f(44 * s)}" height="{f(44 * s)}" fill="#7A6A5A" stroke="{INK}" stroke-width="1.8"></rect>'
            f'<path d="M{f(x)} {f(base - 44 * s)} L {f(x)} {f(base - 70 * s)}" stroke="{INK}" stroke-width="{f(4 * s)}"></path>'
            + eagle(x, base - 96 * s, s * 0.62, color=color).replace('fill="#E8E2D6"', f'fill="{color}"'))

def _creeper_idol(x, base, s, color):
    """An image of a creeping thing on a plinth: a crocodile cast in metal."""
    return (f'<rect x="{f(x - 50 * s)}" y="{f(base - 30 * s)}" width="{f(100 * s)}" height="{f(30 * s)}" fill="#7A6A5A" stroke="{INK}" stroke-width="1.8"></rect>'
            + croc(x, base - 38 * s, s * 0.22).replace('#4A6A3A', color).replace('#5A7A4A', color).replace('#3A5A2A', "#8A6A1E"))

def image_of_man(p, x, base, s, color="#C8C8D0", flip=False):
    """An image of corruptible man: a standing figure of stone (or gilded) on its plinth, a man's true proportions, its
    arm raised; an object, no face drawn."""
    k = s * 0.9
    return (f'<rect x="{f(x - 24 * k)}" y="{f(base - 34 * k)}" width="{f(48 * k)}" height="{f(34 * k)}" fill="#7A6A5A" stroke="{INK}" stroke-width="1.8"></rect>'
            + mk.person(p, round(x), round(base - 34 * k), round(s * 0.62, 3), body=color, cloth=color, kind="Robe", sw=2.6, flip=flip, up=[(22, -158), (40, -176), (52, -200)]))

def idols(w, h, seed, dark=False, tags=True):
    """They changed the glory of the incorruptible God for the likeness of an image of corruptible man, and of birds, and
    four-footed beasts, and creeping things: four images on their plinths in the court of an idol-temple, gilded and grey."""
    b = h * 0.86
    p = f"id{seed}"
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#5A3A4A" if not dark else "#1A1020", "#C8906A" if not dark else "#3A2430")]
    o.append(f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(7):
        x = w * (0.02 + k * 0.16)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.12)}" width="{f(w * 0.04)}" height="{f(b - h * 0.12)}" fill="#D8CCB0" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A5A4A" stroke="{INK}" stroke-width="2"></rect>')
    k = min(1.6, (b - h * 0.16) / 170)
    o.append(image_of_man(p, w * 0.14, b, k, color="#C8C8D0"))
    o.append(_bird_idol(w * 0.38, b, k, "#E8B830"))
    o.append(V.calf(w * 0.62, b, k * 0.62, uid=f"ic{seed}"))
    o.append(_creeper_idol(w * 0.86, b, k * 1.3, "#C8963E"))
    if tags:
        for x, t in ((0.14, "CORRUPTIBLE MAN"), (0.38, "BIRDS"), (0.62, "FOUR-FOOTED BEASTS"), (0.86, "CREEPING THINGS")):
            o.append(f'<rect x="{f(w * x - len(t) * 3.4 - 6)}" y="{f(b + 6)}" width="{f(len(t) * 6.8 + 12)}" height="16" fill="#12113A"></rect>' + label(w * x, b + 18, t, GOLD, 9))
    return "".join(o)

def shut_doors(w, h, seed):
    """The great doors of the idol-temple seen close at night, shut and barred, a torch gone out in its bracket; no one."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1418"></rect>']
    for i in range(int(h / 34) + 2):
        y = i * 34
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A2228" stroke-width="2"></path>')
        for j in range(int(w / 90) + 2):
            x = j * 90 + (45 if i % 2 else 0)
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + 34)}" stroke="#2A2228" stroke-width="1.6"></path>')
    dw, dt = min(w * 0.5, h * 1.0), h * 0.06
    dx = w * 0.5 - dw / 2
    o.append(f'<rect x="{f(dx - 14)}" y="{f(dt - 14)}" width="{f(dw + 28)}" height="{f(h)}" fill="#5A5058" stroke="{INK}" stroke-width="3"></rect>'
             f'<rect x="{f(dx)}" y="{f(dt)}" width="{f(dw)}" height="{f(h)}" fill="#5A3A1E" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(w * 0.5)} {f(dt)} L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="3.4"></path>')
    for side in (0, 1):
        x0 = dx + side * dw / 2
        for r_ in range(3):
            o.append(f'<rect x="{f(x0 + dw * 0.06)}" y="{f(dt + h * (0.06 + r_ * 0.3))}" width="{f(dw * 0.38)}" height="{f(h * 0.24)}" fill="none" stroke="#3A2410" stroke-width="2.4"></rect>')
            for c in range(3):
                o.append(f'<circle cx="{f(x0 + dw * (0.1 + c * 0.15))}" cy="{f(dt + h * (0.04 + r_ * 0.3))}" r="{f(max(2.4, h * 0.012))}" fill="#A8803A" stroke="{INK}" stroke-width="1"></circle>')
    by = h * 0.52
    o.append(f'<rect x="{f(dx - 24)}" y="{f(by)}" width="{f(dw + 48)}" height="{f(h * 0.07)}" fill="#3A2A1A" stroke="{INK}" stroke-width="2.6"></rect>'
             + "".join(f'<rect x="{f(bx - 8)}" y="{f(by - 6)}" width="16" height="{f(h * 0.07 + 12)}" fill="#6A6A70" stroke="{INK}" stroke-width="2"></rect>' for bx in (dx - 4, dx + dw + 4)))
    tx = dx - 40
    o.append(f'<rect x="{f(tx - 4)}" y="{f(h * 0.3)}" width="8" height="{f(h * 0.12)}" fill="#3A3238" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(tx - 10)} {f(h * 0.3)} L {f(tx + 10)} {f(h * 0.3)} L {f(tx + 6)} {f(h * 0.24)} L {f(tx - 6)} {f(h * 0.24)} Z" fill="#2A2020" stroke="{INK}" stroke-width="1.6"></path>'
             + smoke(tx, h * 0.22, 4, seed, color="#4A4048", op=0.4))
    return "".join(o)

def temple_doors(w, h, seed, night=False):
    """An idol-temple's front at dusk, its great bronze doors shut, the steps empty, a dead altar before it; no one there."""
    b = h * 0.94
    top, bot = ("#1A1024", "#4A2A3A") if night else ("#3A2440", "#C8704A")
    o = [sky(w, h, top, bot)]
    if night: o.append(mk.stars(24, w, h * 0.3, seed))
    cx, tw = w * 0.5, w * 0.7
    o.append(f'<path d="M{f(cx - tw / 2)} {f(h * 0.22)} L {f(cx)} {f(h * 0.08)} L {f(cx + tw / 2)} {f(h * 0.22)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - tw / 2)}" y="{f(h * 0.22)}" width="{f(tw)}" height="{f(h * 0.05)}" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(6):
        x = cx - tw / 2 + tw * (k + 0.5) / 6
        if k in (2, 3): continue
        o.append(f'<rect x="{f(x - w * 0.025)}" y="{f(h * 0.27)}" width="{f(w * 0.05)}" height="{f(h * 0.45)}" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></rect>')
    dw, dh = tw * 0.26, h * 0.42
    o.append(f'<rect x="{f(cx - dw / 2)}" y="{f(h * 0.3)}" width="{f(dw)}" height="{f(dh)}" fill="#6A4A22" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(cx)} {f(h * 0.3)} L {f(cx)} {f(h * 0.3 + dh)}" stroke="{INK}" stroke-width="3"></path>')
    for j in range(4):
        for side in (-1, 1):
            o.append(f'<circle cx="{f(cx + side * dw * 0.25)}" cy="{f(h * 0.36 + j * dh * 0.22)}" r="{f(max(2.5, w * 0.006))}" fill="#C8963E" stroke="{INK}" stroke-width="1"></circle>')
    o.append(f'<rect x="{f(cx - dw * 0.08)}" y="{f(h * 0.3 + dh * 0.5)}" width="{f(dw * 0.16)}" height="{f(dh * 0.06)}" fill="#3A2A1A" stroke="{INK}" stroke-width="1.6"></rect>')
    for k in range(3):
        o.append(f'<rect x="{f(cx - tw / 2 - k * w * 0.03)}" y="{f(h * 0.72 + k * h * 0.06)}" width="{f(tw + k * w * 0.06)}" height="{f(h * 0.06)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.8"></rect>')
    ax = w * 0.14
    o.append(f'<rect x="{f(ax - w * 0.04)}" y="{f(b - h * 0.16)}" width="{f(w * 0.08)}" height="{f(h * 0.16)}" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></rect>'
             + smoke(ax, b - h * 0.18, 5, seed, color="#4A3A44", op=0.5))
    o.append(ground(w, h, b, "#4A3A3A", dy=0))
    return "".join(o)

def dark_court(w, h, seed, night=True):
    """The idol-temple's court in the dark: the colonnade round about, the images grey on their plinths, the brazier gone
    out, every door shut — empty."""
    b = h * 0.9
    o = [sky(w, h, "#05050E" if night else "#2A1A2A", "#2A1A30" if night else "#6A3A3A"), mk.stars(18, w, h * 0.12, seed)]
    o.append(f'<rect x="-10" y="{f(h * 0.14)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#4A4048" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(9):
        x = w * (0.01 + k * 0.125)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.19)}" width="{f(w * 0.03)}" height="{f(h * 0.5)}" fill="#5A5058" stroke="{INK}" stroke-width="1.6"></rect>')
        if k % 2 == 1:
            o.append(f'<rect x="{f(x + w * 0.04)}" y="{f(h * 0.34)}" width="{f(w * 0.075)}" height="{f(h * 0.35)}" fill="#2A1A14" stroke="{INK}" stroke-width="2"></rect>'
                     f'<path d="M{f(x + w * 0.0775)} {f(h * 0.34)} L {f(x + w * 0.0775)} {f(h * 0.69)}" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.69)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2228" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(10):
        y = h * 0.69 + (b - h * 0.69) * i / 9
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#3A3238" stroke-width="1.2"></path>')
    k = min(1.2, h / 330)
    o.append(statue(w * 0.24, h * 0.72, k * 0.9, kind=1, color="#5A5A64") + statue(w * 0.76, h * 0.72, k * 0.9, kind=2, color="#6A5A3A"))
    bx = w * 0.5
    o.append(f'<path d="M{f(bx - w * 0.06)} {f(b - h * 0.02)} L {f(bx - w * 0.04)} {f(b - h * 0.14)} L {f(bx + w * 0.04)} {f(b - h * 0.14)} L {f(bx + w * 0.06)} {f(b - h * 0.02)} Z" fill="#3A3234" stroke="{INK}" stroke-width="2"></path>'
             f'<ellipse cx="{f(bx)}" cy="{f(b - h * 0.14)}" rx="{f(w * 0.05)}" ry="{f(h * 0.015)}" fill="#1A1414" stroke="{INK}" stroke-width="1.6"></ellipse>'
             + smoke(bx, b - h * 0.16, 6, seed, color="#5A4A54", op=0.4))
    return "".join(o)

# ---- Romans 2 -----------------------------------------------------------------------------------------------------------
def judgment_seat(p, w, h, seed):
    """Thou that judgest: the judgment-seat in the forum empty, the scales beside it (no judge drawn)."""
    o = judgment_bema(p, w, h, seed, gallio_=False, accusers=False, paul_=False)
    return o + scales(w * 0.24, h * 0.94, min(0.9, h / 330), tilt=-10)

def two_roads(w, h, seed):
    """To every man according to his works: one road climbing to the light — glory and honor and incorruption, eternal life
    — and one going down into the storm — wrath and indignation, tribulation and anguish. No one on either road."""
    o = [f'<defs><linearGradient id="tr{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1A1420"></stop><stop offset="0.45" stop-color="#4A3A4A"></stop>'
         f'<stop offset="0.55" stop-color="#C8B080"></stop><stop offset="1" stop-color="#FFF4C2"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#tr{seed})"></rect>',
         halo(w * 0.84, h * 0.26, max(w, h) * 0.36, "#FFFFFF", 0.7), rays(w * 0.84, h * 0.26, 20, h * 0.06, max(w, h) * 0.5, "#FFF4C2", 0.3, 4),
         bolt(w * 0.12, 0, h * 0.4, seed, color="#C8C8E8", sw=3), rain(w * 0.45, h * 0.7, seed, n=26, color="#8A8AA8", op=0.4)]
    o.append(f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.6)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A5048" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.42)} {f(h + 10)} C {f(w * 0.46)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.74)} {f(w * 0.52)} {f(h * 0.7)}" stroke="#D8C8A0" stroke-width="{f(max(14, h * 0.09))}" fill="none"></path>'
             f'<path d="M{f(w * 0.52)} {f(h * 0.7)} C {f(w * 0.62)} {f(h * 0.62)} {f(w * 0.74)} {f(h * 0.5)} {f(w * 0.82)} {f(h * 0.44)}" stroke="#F3E8C8" stroke-width="{f(max(8, h * 0.05))}" fill="none"></path>'
             f'<path d="M{f(w * 0.52)} {f(h * 0.7)} C {f(w * 0.4)} {f(h * 0.66)} {f(w * 0.24)} {f(h * 0.62)} {f(w * 0.1)} {f(h * 0.64)}" stroke="#6A6070" stroke-width="{f(max(8, h * 0.05))}" fill="none"></path>')
    o.append(plate_label(w * 0.84, h * 0.08, "GLORY · HONOR · INCORRUPTION", "#7A4A2A", 10).replace('stroke="#0B1A2E"', 'stroke="#FFF8E6"')
             + plate_label(w * 0.16, h * 0.08, "WRATH · INDIGNATION", "#C8C8E8", 10))
    return "".join(o)

def _tablets(cx, cy, s, glow_=False):
    """The two tables of stone, round-topped, with rows of writing (no words)."""
    o = []
    for side in (-1, 1):
        x = cx + side * 34 * s
        o.append(f'<path d="M{f(x - 30 * s)} {f(cy + 60 * s)} L {f(x - 30 * s)} {f(cy - 40 * s)} C {f(x - 30 * s)} {f(cy - 74 * s)} {f(x + 30 * s)} {f(cy - 74 * s)} {f(x + 30 * s)} {f(cy - 40 * s)} '
                 f'L {f(x + 30 * s)} {f(cy + 60 * s)} Z" fill="#B8B0A0" stroke="{INK}" stroke-width="2.4"></path>')
        for k in range(5):
            yy = cy - 34 * s + k * 18 * s
            o.append(f'<path d="M{f(x - 20 * s)} {f(yy)} L {f(x + 20 * s)} {f(yy)}" stroke="#4A4038" stroke-width="{f(2.4 * s)}" stroke-dasharray="{f(6 * s)} {f(3 * s)}"></path>')
    return "".join(o)

def _heart(cx, cy, R, fill="#C8202A", writing=True, glow_=True):
    d = (f"M{f(cx)} {f(cy + R)} C {f(cx - R * 1.4)} {f(cy)} {f(cx - R * 1.1)} {f(cy - R * 1.1)} {f(cx)} {f(cy - R * 0.45)} "
         f"C {f(cx + R * 1.1)} {f(cy - R * 1.1)} {f(cx + R * 1.4)} {f(cy)} {f(cx)} {f(cy + R)} Z")
    o = [halo(cx, cy, R * 1.8, "#FF8A6A", 0.45) if glow_ else "", f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="2.6"></path>']
    if writing:
        for k in range(4):
            yy = cy - R * 0.36 + k * R * 0.24; hw = R * (0.62 - abs(k - 1.2) * 0.12)
            o.append(f'<path d="M{f(cx - hw)} {f(yy)} L {f(cx + hw)} {f(yy)}" stroke="#FFE6A0" stroke-width="{f(max(1.6, R * 0.05))}" stroke-dasharray="{f(R * 0.12)} {f(R * 0.05)}"></path>')
    return "".join(o)

def law_in_hearts(w, h):
    """The work of the law written in their hearts: a technical plate — the two tables of stone at the left, an arrow, the
    heart with the same rows of writing at the right; the conscience bearing witness."""
    o = [plate_bg(w, h, "ROMANS 2:14–15 · THE LAW WRITTEN IN THEIR HEARTS")]
    k = min(w / 520, (h - 40) / 230)
    cy = h * 0.54
    o.append(_tablets(w * 0.26, cy, k))
    o.append(route([(w * 0.42, cy), (w * 0.58, cy)], color=GOLD, sw=3, dash="8 5"))
    o.append(_heart(w * 0.74, cy, 64 * k))
    ly = min(cy + 86 * k, h - 12)
    o.append(label(w * 0.26, ly, "THE LAW · TABLES OF STONE", CY, 10) + label(w * 0.74, ly, "WRITTEN IN THEIR HEARTS", GOLD, 10))
    o.append(tag(w * 0.74 - 50 * k, cy - 40 * k, "CONSCIENCE BEARING WITNESS", w * 0.6 - 10 * k, cy - 84 * k, color=CY))
    return "".join(o)

def teacher(p, w, h, seed):
    """A guide of the blind, a light of them that are in darkness: a teacher of the law standing in the synagogue with the
    scroll open in his hands, the lamp burning, the listeners seated on the floor."""
    bg, b = _synagogue(w, h, seed)
    o = [mk.defs(p, *ALL, "ManUp"), bg, lamp_glow(w * 0.19, h * 0.34, max(w, h) * 0.3, f"{p}tl", op=0.5)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(man_fig(p, w * 0.36, b, s, "#E8E2D6", head="#F3EFE6", cord="#1F3A7A", bd="#3A2A1A", up=[(22, -158), (40, -150), (56, -158)]))
    o.append(open_letter(w * 0.36 + 44 * s, b - 186 * s, 40 * s, 34 * s, rows=4, seed=seed))
    for i, x in enumerate((0.56, 0.68, 0.8, 0.92)):
        o.append(seated(w * x, b, s * 0.78, ["#5A6A3A", "#3A4A6A", "#7A5A3A", "#5A4A6A"][i], head=["#5A6A3A", None, "#7A5A3A", None][i],
                        beard=["#2A1A10", "#3A2A1A", None, "#6A645E"][i], flip=True))
    return "".join(o)

def letter_spirit(w, h):
    """He is a Jew who is one inwardly; circumcision is that of the heart, in the spirit not in the letter: a plate —
    'outwardly, in the flesh' at the left, a cut mark on a silhouette; 'inwardly, of the heart' at the right, the heart in light."""
    o = [plate_bg(w, h, "ROMANS 2:28–29 · OUTWARDLY · INWARDLY")]
    k = min(w / 560, (h - 40) / 230); cy = h * 0.56
    o.append(f'<path d="M{f(w * 0.5)} 34 L {f(w * 0.5)} {f(h - 10)}" stroke="#2C5A7A" stroke-width="1.6" stroke-dasharray="6 5"></path>')
    o.append(open_letter(w * 0.12, cy - 60 * k, w * 0.26, 110 * k, rows=7, seed=29, color="#C8B888"))
    o.append(_heart(w * 0.74, cy, 60 * k, writing=False) + halo(w * 0.74, cy, 110 * k, "#FFF4C2", 0.5) + rays(w * 0.74, cy, 16, 70 * k, 130 * k, "#FFF4C2", 0.35, 3))
    ly = min(cy + 84 * k, h - 12)
    o.append(label(w * 0.25, ly, "OUTWARDLY · IN THE FLESH · THE LETTER", CY, 9.5) + label(w * 0.74, ly, "INWARDLY · OF THE HEART · THE SPIRIT", GOLD, 9.5))
    return "".join(o)

# ---- Romans 3 -----------------------------------------------------------------------------------------------------------
def oracles(w, h, seed):
    """Intrusted with the oracles of God: the ark of the scrolls in the synagogue, its doors open, the rolled scrolls of the
    law and the prophets in their places, a lamp before them."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', lamp_glow(w * 0.5, h * 0.4, max(w, h) * 0.5, f"or{seed}", op=0.45)]
    b = h * 0.9
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A1E18" stroke="{INK}" stroke-width="2"></rect>')
    aw, ah = min(w * 0.44, h * 0.96), h * 0.76
    ax, ay = w * 0.5 - aw / 2, b - ah
    o.append(f'<path d="M{f(ax - 10)} {f(ay)} L {f(w * 0.5)} {f(ay - ah * 0.14)} L {f(ax + aw + 10)} {f(ay)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(ax)}" y="{f(ay)}" width="{f(aw)}" height="{f(ah)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<rect x="{f(ax + aw * 0.08)}" y="{f(ay + ah * 0.08)}" width="{f(aw * 0.84)}" height="{f(ah * 0.84)}" fill="#1E120C" stroke="{INK}" stroke-width="2"></rect>')
    for side in (-1, 1):
        dx = ax - aw * 0.3 if side < 0 else ax + aw
        o.append(f'<path d="M{f(ax if side < 0 else ax + aw)} {f(ay + ah * 0.06)} L {f(dx + (aw * 0.3 if side < 0 else 0))} {f(ay + ah * 0.06)} L {f(dx if side < 0 else dx + aw * 0.3)} {f(ay + ah * 0.12)} '
                 f'L {f(dx if side < 0 else dx + aw * 0.3)} {f(ay + ah * 0.88)} L {f(ax if side < 0 else ax + aw)} {f(ay + ah * 0.94)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2"></path>')
    n = 5
    for i in range(n):
        x = ax + aw * (0.16 + 0.68 * i / (n - 1))
        o.append(f'<rect x="{f(x - aw * 0.05)}" y="{f(ay + ah * 0.16)}" width="{f(aw * 0.1)}" height="{f(ah * 0.68)}" rx="{f(aw * 0.03)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.8"></rect>'
                 f'<rect x="{f(x - aw * 0.05)}" y="{f(ay + ah * 0.44)}" width="{f(aw * 0.1)}" height="{f(ah * 0.06)}" fill="{["#1F3A7A", "#7A1A2A", "#E8B830", "#1F5A4A", "#5A2A6A"][i]}" stroke="{INK}" stroke-width="1.2"></rect>'
                 f'<rect x="{f(x - 3)}" y="{f(ay + ah * 0.1)}" width="6" height="{f(ah * 0.06)}" fill="#C8A060" stroke="{INK}" stroke-width="1"></rect>')
    o.append(clay_lamp(w * 0.5, b + h * 0.0 - 4, min(1.4, h / 300)))
    return "".join(o)

def dark_road(w, h, seed, fork=True):
    """They have all turned aside: a road at night among bare rocks, breaking into ways that go nowhere; no one on it."""
    o = [sky(w, h, "#05050E", "#2A2040"), mk.stars(30, w, h * 0.4, seed), hills(w, h, h * 0.5, seed, color="#1A1626", amp=20, step=90),
         ground(w, h, h * 0.56, "#2A2430", dy=0)]
    o.append(f'<path d="M{f(w * 0.44)} {f(h + 10)} C {f(w * 0.46)} {f(h * 0.84)} {f(w * 0.48)} {f(h * 0.76)} {f(w * 0.5)} {f(h * 0.72)}" stroke="#4A4250" stroke-width="{f(max(16, h * 0.1))}" fill="none"></path>')
    if fork:
        for tx, ty in ((0.1, 0.62), (0.3, 0.58), (0.72, 0.6), (0.94, 0.66)):
            o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.72)} C {f(w * (0.5 + tx) / 2)} {f(h * 0.68)} {f(w * tx)} {f(h * (ty + 0.04))} {f(w * tx)} {f(h * ty)}" stroke="#3A3440" stroke-width="{f(max(6, h * 0.03))}" fill="none"></path>')
    r = random.Random(seed)
    for _ in range(9):
        x, y = w * r.uniform(0, 1), h * r.uniform(0.6, 0.96); s = h * r.uniform(0.03, 0.07)
        o.append(f'<path d="M{f(x - s * 1.4)} {f(y)} L {f(x - s * 0.6)} {f(y - s)} L {f(x + s * 0.8)} {f(y - s * 0.8)} L {f(x + s * 1.4)} {f(y)} Z" fill="#3A3240" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def open_tomb(p, w, h, seed):
    """Their throat is an open sepulchre: a tomb cut in the rock at night, its stone rolled back and its door gaping dark — empty."""
    b = h * 0.92
    o = [sky(w, h, "#0B0B2A", "#3A2A4A"), mk.stars(20, w, h * 0.3, seed), hills(w, h, h * 0.5, seed, color="#2A2434", amp=12, step=80),
         f'<path d="M{f(w * 0.16)} {f(b)} C {f(w * 0.2)} {f(h * 0.26)} {f(w * 0.8)} {f(h * 0.22)} {f(w * 0.86)} {f(b)} Z" fill="#5A5060" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.42)} {f(b)} L {f(w * 0.42)} {f(h * 0.56)} Q {f(w * 0.5)} {f(h * 0.44)} {f(w * 0.58)} {f(h * 0.56)} L {f(w * 0.58)} {f(b)} Z" fill="#05050A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<circle cx="{f(w * 0.72)}" cy="{f(b - h * 0.17)}" r="{f(h * 0.17)}" fill="#6A6070" stroke="{INK}" stroke-width="2.4"></circle>',
         f'<circle cx="{f(w * 0.72)}" cy="{f(b - h * 0.17)}" r="{f(h * 0.1)}" fill="none" stroke="#4A4250" stroke-width="2"></circle>',
         ground(w, h, b, "#2A2430", dy=0)]
    return "".join(o)

def throne_light(p, w, h, seed):
    """All the world brought under the judgment of God: the sky full of light over the whole round of the earth (Acts'
    throne and footstool), no figure."""
    return throne_footstool(p, w, h, seed)

def dawn(w, h, seed):
    """But now a righteousness of God hath been manifested: the dawn breaking over the hills, a great light rising."""
    return vista(w, h, seed, tone="dawn", horizon=0.66, hills_n=2, glow_at=(0.5, 0.66, 0.6, "#FFF4C2"), sun_at=(0.5, 0.64), birds_=4)

def fall_short(w, h):
    """All have sinned, and fall short of the glory of God: a technical plate — a measuring rule rising to a gold band of
    light at the top (the glory of God), and a row of men and women standing at its foot, every one far beneath the mark."""
    o = [plate_bg(w, h, "ROMANS 3:23 · ALL HAVE SINNED, AND FALL SHORT")]
    top, base = h * 0.18, h * 0.9
    rx = w * 0.16
    o.append(f'<rect x="{f(rx - 10)}" y="{f(top)}" width="20" height="{f(base - top)}" fill="#12304A" stroke="{CY}" stroke-width="1.6"></rect>')
    for k in range(11):
        y = base - (base - top) * k / 10
        o.append(f'<path d="M{f(rx - 10)} {f(y)} l {f(-10 if k % 5 else -18)} 0" stroke="{CY}" stroke-width="1.4"></path>')
    o.append(f'<rect x="{f(rx - 30)}" y="{f(top - 8)}" width="{f(w * 0.8)}" height="14" fill="{GOLD}" opacity="0.9"></rect>' + halo(w * 0.55, top - 2, h * 0.25, "#FFE680", 0.5)
             + label(w * 0.55, top - 14, "THE GLORY OF GOD", GOLD, 10))
    o.append(f'<path d="M{f(rx + 14)} {f(top + 6)} L {f(w * 0.94)} {f(top + 6)}" stroke="{GOLD}" stroke-width="1.2" stroke-dasharray="4 4"></path>')
    n = 8; r = random.Random(323)
    peak = base
    o.insert(1, mk.defs("fsh323", *ALL))
    for i in range(n):
        x = w * (0.3 + 0.6 * i / (n - 1)); hh = (base - top) * r.uniform(0.3, 0.42)
        peak = min(peak, base - hh)
        woman = i % 3 == 1
        o.append(mk.person("fsh323", round(x), round(base), round(hh / 205, 3), body="#1E4A6A", cloth="#163A56", woman=woman, kind="Robe" if woman else "Tunic", stroke=CY, sw=2.4, flip=i % 2 == 1))
    o.append(dim(w * 0.95, top + 8, w * 0.95, peak - 2, "FALL SHORT", size=9, color="#FF6A4A"))
    return "".join(o)

def propitiation(w, h):
    """Whom God set forth to be a propitiation: the mercy-seat of the ark (Exodus' blueprint), the two cherubim of gold, and
    the light between them (God is never drawn)."""
    o = plate_bg(w, h, "ROMANS 3:25 · A PROPITIATION · THE MERCY-SEAT") + mercy_seat(w, h, grid=False, cx=0.5, scale=0.8)
    return o + halo(w * 0.5, h * 0.42, min(w, h) * 0.28, "#FFFFFF", 0.6)

def under_sin(w, h):
    """We before laid to the charge both of Jews and Greeks, that they are all under sin: a plate — two companies of men
    and women standing, the Jews at the left (headcloths), the Greeks at the right (bareheaded, himations), one dark band
    lying over them all."""
    o = [plate_bg(w, h, "ROMANS 3:9 · BOTH JEWS AND GREEKS"), mk.defs("us39", *ALL)]
    base, top = h * 0.9, h * 0.34
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(top - h * 0.1)}" width="{f(w * 0.92)}" height="{f(h * 0.08)}" fill="#05050E" stroke="#FF6A4A" stroke-width="1.6"></rect>'
             + label(w * 0.5, top - h * 0.045, "ALL UNDER SIN", "#FF6A4A", 11))
    s = (base - top) / 205
    for i in range(6):
        x = w * (0.1 + i * 0.06)
        o.append(mk.person("us39", round(x), round(base), round(s * (0.96 + 0.04 * (i % 2)), 3), body="#1E4A6A", cloth="#163A56", woman=i % 3 == 2, kind="Robe" if i % 3 == 2 else "Tunic", stroke=CY, sw=2.4,
                           extra=A.headcloth("#163A56", cord=None).replace('stroke="#0D0D0F"', f'stroke="{CY}"') if i % 3 != 2 else ""))
    for i in range(6):
        x = w * (0.6 + i * 0.06)
        o.append(mk.person("us39", round(x), round(base), round(s * (0.96 + 0.04 * (i % 2)), 3), body="#1E4A6A", cloth="#24506E", woman=i % 3 == 1, kind="Robe" if i % 3 == 1 else "Tunic", stroke=CY, sw=2.4, flip=True))
    o.append(label(w * 0.25, min(base + 18, h - 6), "JEWS", GOLD, 10) + label(w * 0.75, min(base + 18, h - 6), "GREEKS", GOLD, 10))
    o.append(f'<path d="M{f(w * 0.5)} {f(top)} L {f(w * 0.5)} {f(base)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    return "".join(o)

def ruined_way(w, h, seed):
    """Destruction and misery are in their ways: a broken road at night through the stones of a fallen town, nothing living."""
    return vista(w, h, seed, tone="dark", horizon=0.6, hills_n=2, city="ruin", cx=0.6, cw=0.7, smoke_=2, stars=True)
