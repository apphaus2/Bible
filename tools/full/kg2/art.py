"""Drawings for the 2 Kings volume (chapter by chapter, added below), on top of everything in kg1.art (re-exported here).

Elisha at a distance: a tan tunic, bareheaded (elisha_fig); Elijah as in 1 Kings (elijah_fig, the hairy mantle)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from kg1.art import *
from kg1.art import f, SOL_C, AHAB_C, BRASS, CEDAR_C, JERO_C, REHO_C, MANTLE
import kg1.art as K1
import sa2.art as K2

ELISHA_C = "#8A6A3A"
def elisha_fig(p, x, y, s, flip=False, up=None, mantle=False):
    """Elisha at a distance: tan tunic, bareheaded, short beard (mantle=True: wearing Elijah's mantle)."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ELISHA_C, kind="Tunic", sw=3, flip=flip, up=up, extra=(MANTLE if mantle else "") + A.BLACK_BEARD)

def fire_chariot(x, y, s=1.0, seed=1):
    """A chariot of fire with horses of fire."""
    o = [f'<g opacity="0.75">' + E.blaze(x + 40 * s, y + 10 * s, 300 * s, 200 * s, seed, n=9) + '</g>',
         E3.chariot(x, y, s, color="#FF6A2A", driver="#FFE680"),
         f'<g opacity="0.5">' + E.blaze(x + 60 * s, y - 10 * s, 160 * s, 110 * s, seed + 1, n=6) + '</g>']
    return "".join(o)

# ---- 2 Kings 1–2 --------------------------------------------------------------------------------------------------------
def lattice_fall(w, h, seed):
    """The lattice in the upper chamber in Samaria, broken."""
    o = [sky(w, h, "#5A4A6A", "#C8A080"), f'<rect x="{f(w * 0.2)}" y="{f(h * 0.1)}" width="{f(w * 0.6)}" height="{f(h * 0.9)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.6"></rect>']
    x0, y0, lw, lh = w * 0.36, h * 0.24, w * 0.28, h * 0.4
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(lw)}" height="{f(lh)}" fill="#1A1214" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for i in range(1, 6):
        o.append(f'<path d="M{f(x0 + i * lw / 6)} {f(y0)} L {f(x0 + i * lw / 6)} {f(y0 + lh * (0.5 if i in (3, 4) else 1))}" stroke="#8A5A30" stroke-width="4"></path>'
                 f'<path d="M{f(x0)} {f(y0 + i * lh / 6)} L {f(x0 + lw * (0.4 if i > 3 else 1))} {f(y0 + i * lh / 6)}" stroke="#8A5A30" stroke-width="4"></path>')
    o.append(f'<path d="M{f(x0 + lw * 0.5)} {f(y0 + lh)} l -20 60 l 30 40 l -10 50" stroke="#8A5A30" stroke-width="4" fill="none"></path>')
    return "".join(o)

def sickbed(p, w, h, seed):
    """Ahaziah sick upon his bed, his messengers standing."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), bed(w, h, w * 0.06, w * 0.5, b, cover=AHAB_C, head="#C98E66", hair="#1A1210")]
    s = fit(b, h * 0.4)
    for i in range(3): o.append(man(p, w * (0.64 + i * 0.12), b, s * 0.86, ["#6A5A3A", "#3A4A6A", "#5A3A2A"][i], flip=True))
    return "".join(o)

def hilltop(p, w, h, seed, fire=False, kneel=False):
    """Elijah sitting on the top of the hill; a captain of fifty with his fifty below; fire=True: fire come down from heaven
    upon the slope (the fifty told in words only: nothing but the flames and smoke); kneel=True: the third captain on his knees."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A2A" if fire else "#8FD0E2", "#C8603A" if fire else "#F3E8C8"),
         f'<path d="M{f(w * 0.4)} {f(h + 10)} C {f(w * 0.56)} {f(h * 0.4)} {f(w * 0.8)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.32)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.8, "#9A8A5A", dy=0)]
    s = fit(h * 0.36, h * 0.16)
    o.append(E.kneel(w * 0.82, h * 0.36, s * 0.9, color="#5A3A1E", skin="#B98A6E", flip=True))
    if fire:
        o.append(V.rays(w * 0.3, -h * 0.1, 20, 10, h, color="#FFB04A", op=0.35))
        o += [E.blaze(w * (0.08 + i * 0.12), b, w * 0.12, h * 0.4, seed + i, n=6) for i in range(4)]
        o.append("".join(f'<circle cx="{f(w * (0.1 + i * 0.1))}" cy="{f(h * 0.3)}" r="{f(w * 0.08)}" fill="#3A2A2E" opacity="0.7"></circle>' for i in range(5)))
    else:
        for k in range(3):
            for i in range(6):
                x = w * (0.04 + i * 0.06 + (k % 2) * 0.03); y = h * (0.78 + k * 0.07)
                o.append(warrior(p, x, y, fit(y, y - h * (0.14 + 0.04 * k)), WAR[(i + k) % 4]))
        if kneel: o.append(E.kneel(w * 0.5, h * 0.74, fit(h * 0.74, h * 0.4) * 0.8, color="#8A3A1E", skin="#B98A6E", flip=True))
        else: o.append(captain(p, w * 0.46, h * 0.82, fit(h * 0.82, h * 0.5), flip=True, up=[(22, -158), (40, -190), (50, -220)]))
    return "".join(o)

def jordan_part(p, w, h, seed, two=True):
    """The waters of the Jordan divided hither and thither by the mantle, the two going over on dry ground (two=False: Elisha
    alone with the mantle)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#7A8A5A", amp=14), ground(w, h, h * 0.5, "#B89A6A", dy=0),
         f'<path d="M-10 {f(h * 0.56)} L {f(w * 0.36)} {f(h * 0.56)} L {f(w * 0.4)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w + 10)} {f(h * 0.56)} L {f(w * 0.64)} {f(h * 0.56)} L {f(w * 0.6)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.56)} C {f(w * 0.32)} {f(h * 0.4)} {f(w * 0.4)} {f(h * 0.36)} {f(w * 0.38)} {f(h * 0.56)} M{f(w * 0.64)} {f(h * 0.56)} C {f(w * 0.68)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.36)} {f(w * 0.62)} {f(h * 0.56)}" fill="#E8F6FA" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M{f(w * 0.4)} {f(h * 0.56)} L {f(w * 0.6)} {f(h * 0.56)} L {f(w * 0.62)} {f(h + 10)} L {f(w * 0.38)} {f(h + 10)} Z" fill="#C8A878"></path>']
    s = fit(b, h * 0.34)
    if two: o.append(elijah_fig(p, w * 0.46, b, s, up=[(-22, -158), (-40, -150), (-60, -146)]) + elisha_fig(p, w * 0.56, b - 6, s * 0.95))
    else: o.append(elisha_fig(p, w * 0.5, b, s, mantle=True, up=[(-22, -158), (-40, -150), (-60, -146)]))
    return "".join(o)

def whirlwind(p, w, h, seed):
    """The chariot of fire and horses of fire parting them asunder, and Elijah going up by a whirlwind; Elisha below."""
    r = random.Random(seed)
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A"), V.rays(w * 0.56, h * 0.2, 36, 20, max(w, h), color="#FFE680", op=0.25)]
    for i in range(10):
        y = h * (0.1 + i * 0.07); rx = w * (0.08 + i * 0.012)
        o.append(f'<ellipse cx="{f(w * 0.56 + math.sin(i) * 12)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(h * 0.02)}" fill="none" stroke="#E8D8C8" stroke-width="3" opacity="0.6"></ellipse>')
    o.append(fire_chariot(w * 0.56, h * 0.42, min(1.0, h / 400), seed))
    o.append(ground(w, h, h * 0.84, "#3A2A2A", dy=0))
    o.append(elisha_fig(p, w * 0.2, b, fit(b, h * 0.7), up=[(-22, -158), (-40, -196), (-50, -230)]))
    o.append(f'<path d="M{f(w * 0.4)} {f(h * 0.82)} C {f(w * 0.36)} {f(h * 0.86)} {f(w * 0.44)} {f(h * 0.9)} {f(w * 0.48)} {f(h * 0.88)} L {f(w * 0.46)} {f(h * 0.82)} Z" fill="#5A3A1E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def salt_spring(p, w, h, seed):
    """The spring of the waters at Jericho: Elisha casting salt into it from a new cruse."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.8, h * 0.5, w * 0.36, h * 0.28, seed), ground(w, h, h * 0.52, "#B89A6A", dy=0),
         J1.palm(w * 0.6, h * 0.7, min(1.0, h / 360)),
         f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.82)}" rx="{f(w * 0.18)}" ry="{f(h * 0.07)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2.4"></ellipse>']
    s = fit(b, h * 0.4)
    o.append(elisha_fig(p, w * 0.5, b, s, mantle=True, flip=True, up=[(22, -158), (0, -150), (-20, -146)]))
    o.append("".join(f'<circle cx="{f(w * 0.4 + i * 5)}" cy="{f(b - 150 * s + i * 14)}" r="2.5" fill="#F3EFE6"></circle>' for i in range(6)))
    return "".join(o)

def bethel_way(p, w, h, seed):
    """The way up to Beth-el, the wood beside it (2:24 told in words only)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), hills(w, h, h * 0.4, seed, color="#5A6A4A", amp=16),
         ground(w, h, h * 0.56, "#9A8A5A", dy=0), f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.66)} {f(w * 0.56)} {f(h * 0.56)}" stroke="#C8B890" stroke-width="{f(w * 0.08)}" fill="none"></path>']
    r = random.Random(seed)
    for i in range(10):
        x = w * (0.62 + r.uniform(0, 0.36)); y = h * r.uniform(0.5, 0.7)
        o.append(f'<path d="M{f(x)} {f(y + 30)} L {f(x)} {f(y)}" stroke="#3A2A1A" stroke-width="5"></path><circle cx="{f(x)}" cy="{f(y - 10)}" r="{f(w * 0.04)}" fill="#1F4A34" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    return "".join(o)
