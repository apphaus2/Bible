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

# ---- 2 Kings 3–4 --------------------------------------------------------------------------------------------------------
def three_kings(p, w, h, seed):
    """The kings of Israel, Judah and Edom with their host in the wilderness of Edom, no water."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#E8B880"), hills(w, h, h * 0.5, seed, color="#B8704A", amp=20), ground(w, h, h * 0.58, "#D8A870", dy=0)]
    s = fit(b, h * 0.4)
    for i, c in enumerate((AHAB_C, "#1F3A7A", "#8A5A2A")):
        o.append(king_fig(p, w * (0.2 + i * 0.12), b, s * 0.9, cloth=c))
    o.append(crowd_at(p, w, h, seed, w * 0.56, w * 0.98, h * 0.66, b, 9, s * 0.4, s * 0.7, flip=True))
    return "".join(o)

def trenches(p, w, h, seed, red=False):
    """The valley full of trenches, filled with water by the way of Edom; red=True: the sun shining on the water as red as
    blood, the Moabites on the border."""
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A" if red else "#8FD0E2", "#F3D8A0"), sun(w * 0.8, h * 0.2, 28, color="#FF6A2A" if red else "#FFE680", op=0.6),
         hills(w, h, h * 0.36, seed, color="#9A6A4A", amp=18), ground(w, h, h * 0.46, "#C8A06A", dy=0)]
    for k in range(5):
        y = h * (0.54 + k * 0.09)
        o.append(f'<path d="M{f(w * (0.04 + k * 0.02))} {f(y)} L {f(w * (0.96 - k * 0.02))} {f(y)}" stroke="#0D0D0F" stroke-width="{f(10 + k * 3)}"></path>'
                 f'<path d="M{f(w * (0.04 + k * 0.02))} {f(y)} L {f(w * (0.96 - k * 0.02))} {f(y)}" stroke="{"#B5121B" if red else "#2C9DB8"}" stroke-width="{f(7 + k * 3)}"></path>')
    if red:
        for i in range(9):
            o.append(mk.person(p, round(w * (0.06 + i * 0.1)), round(h * 0.46), round(fit(h * 0.46, h * 0.36), 3), body="#1A0E10", cloth="#3A2A3A", kind="Tunic", sw=2, extra=E4.SPEAR))
    return "".join(o)

def kir_wall(w, h, seed):
    """Kir-hareseth: the wall of the city with smoke going up from it (3:27 told in words only)."""
    o = [sky(w, h, "#3A1A1A", "#C8603A"), J.jericho(-10, w + 10, h * 0.3, h * 0.84, seed, towers=4, houses=True), ground(w, h, h * 0.84, "#2A1A14", dy=0)]
    for i in range(6):
        o.append(f'<circle cx="{f(w * 0.5 + (i % 2) * 20 - 10)}" cy="{f(h * (0.24 - i * 0.04))}" r="{f(w * (0.06 + i * 0.015))}" fill="#3A2A2E" opacity="0.75"></circle>')
    return "".join(o)

def oil_vessels(p, w, h, seed, flowing=True):
    """The shut door: the widow pouring from her pot of oil into the borrowed vessels, her two sons bringing more."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A878"></rect>', ground(w, h, b, "#8A6A4A", dy=0)]
    for i in range(12):
        x = w * (0.06 + (i % 6) * 0.15); y = b - (i // 6) * h * 0.18; k = min(w, h) / 600 * r.uniform(0.8, 1.1)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M-22 0 C -30 -24 -28 -50 -12 -60 L -10 -72 L 10 -72 L 12 -60 C 28 -50 30 -24 22 0 Z" fill="{r.choice(["#B5652E", "#8A5A30", "#C8A060", "#9A6A4A"])}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<ellipse cx="0" cy="-72" rx="10" ry="3" fill="#E8C840"></ellipse></g>')
    s = fit(b, h * 0.4)
    o.append(mk.person(p, round(w * 0.5), round(b), round(s, 3), body="#3A1E14", cloth="#3A3A3E", woman=True, hair="#3A3430", sw=3, up=[(-22, -158), (-40, -150), (-56, -140)]))
    if flowing:
        o.append(f'<path d="M{f(w * 0.5 - 56 * s)} {f(b - 140 * s)} C {f(w * 0.5 - 60 * s)} {f(b - 110 * s)} {f(w * 0.5 - 64 * s)} {f(b - 90 * s)} {f(w * 0.5 - 66 * s)} {f(b - 60 * s)}" stroke="#E8C840" stroke-width="5" fill="none"></path>')
    return "".join(o)

def shunem_house(p, w, h, seed, chamber=True):
    """The great woman's house at Shunem, with a little chamber on the wall: a bed, a table, a seat and a candlestick."""
    from genesis.art4 import clay_lamp
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.86, "#B89A6A", dy=0),
         f'<rect x="{f(w * 0.08)}" y="{f(h * 0.46)}" width="{f(w * 0.84)}" height="{f(h * 0.4)}" fill="#D8B88A" stroke="#0D0D0F" stroke-width="2.6"></rect>',
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.12)}" width="{f(w * 0.5)}" height="{f(h * 0.34)}" fill="#E8C898" stroke="#0D0D0F" stroke-width="2.6"></rect>',
         f'<rect x="{f(w * 0.32)}" y="{f(h * 0.15)}" width="{f(w * 0.46)}" height="{f(h * 0.28)}" fill="#5A3A2A" stroke="#0D0D0F" stroke-width="2"></rect>']
    if chamber:
        o.append(f'<rect x="{f(w * 0.34)}" y="{f(h * 0.33)}" width="{f(w * 0.2)}" height="{f(h * 0.06)}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(w * 0.58)}" y="{f(h * 0.34)}" width="{f(w * 0.1)}" height="{f(h * 0.04)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(w * 0.7)}" y="{f(h * 0.36)}" width="{f(w * 0.05)}" height="{f(h * 0.05)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 + clay_lamp(w * 0.62, h * 0.33, min(0.6, h / 600)))
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.86)} L {f(w * 0.3)} {f(h * 0.46)}" stroke="#8A6A4A" stroke-width="6"></path>')
    return "".join(o)

def reapers(p, w, h, seed):
    """A boy going out to his father among the reapers in the field at harvest."""
    import ruth1 as R1
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#F3D8A0"), sun(w * 0.8, h * 0.16, 26, color="#FFF4C2", op=0.7), R1.field(-10, w + 10, h * 0.62, h * 0.2, seed), ground(w, h, h * 0.86, "#C8A06A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(R1.reaper(p, w * 0.7, b, s))
    o.append(man(p, w * 0.4, b, s * 0.5, "#E8E2D6", up=[(-22, -158), (-16, -196), (0, -206)]))
    return "".join(o)

def ride_carmel(p, w, h, seed):
    """The Shunammite riding upon her ass toward mount Carmel, her servant driving."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), f'<path d="M{f(w * 0.5)} {f(h * 0.6)} C {f(w * 0.7)} {f(h * 0.2)} {f(w * 0.9)} {f(h * 0.2)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.6)} Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    o.append(N.mount(w * 0.4, b, min(1.0, h / 320), rider_cloth="#2A5A5A", p=p))
    o.append(S4.runner(p, w * 0.2, b, fit(b, h * 0.4) * 0.9, cloth="#8A7A5A"))
    return "".join(o)

def pottage(p, w, h, seed):
    """The great pot of pottage at Gilgal, the sons of the prophets sitting about it; a lap full of wild gourds."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), ground(w, h, h * 0.66, "#A89070", dy=0), E.blaze(w * 0.5, b, w * 0.24, h * 0.16, seed, n=6),
         f'<path d="M{f(w * 0.36)} {f(h * 0.7)} C {f(w * 0.36)} {f(h * 0.86)} {f(w * 0.64)} {f(h * 0.86)} {f(w * 0.64)} {f(h * 0.7)} Z" fill="#4A4A52" stroke="#0D0D0F" stroke-width="2.6"></path>'
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.7)}" rx="{f(w * 0.14)}" ry="{f(h * 0.03)}" fill="#7A6A3A" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    s = fit(b, h * 0.3) * 0.5
    for i, x in enumerate((0.12, 0.24, 0.76, 0.88)):
        o.append(E.kneel(w * x, b, s, color=["#6A645E", "#5A5A3A", "#3A4A5A", "#6A4A3A"][i], skin="#B98A6E", flip=x > 0.5))
    for i in range(4):
        o.append(f'<ellipse cx="{f(w * (0.42 + i * 0.05))}" cy="{f(h * 0.68)}" rx="9" ry="7" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def loaves(w, h, seed):
    """Twenty loaves of barley and fresh ears of grain in a sack."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A22"></rect>', V.rays(w * 0.5, h * 0.7, 30, 20, max(w, h), color="#FFE680", op=0.15), ground(w, h, h * 0.8, "#3A2214", dy=0)]
    for i in range(20):
        x = w * (0.14 + (i % 7) * 0.1) + (i // 7) * 14; y = h * (0.78 - (i // 7) * 0.08)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.045)}" ry="{f(h * 0.03)}" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(f'<path d="M{f(w * 0.84)} {f(h * 0.8)} C {f(w * 0.78)} {f(h * 0.6)} {f(w * 0.8)} {f(h * 0.5)} {f(w * 0.88)} {f(h * 0.48)} C {f(w * 0.96)} {f(h * 0.5)} {f(w * 0.98)} {f(h * 0.6)} {f(w * 0.94)} {f(h * 0.8)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

# ---- 2 Kings 5–6 --------------------------------------------------------------------------------------------------------
NAAMAN_C = "#5A3A6A"
def naaman_fig(p, x, y, s, flip=False, up=None, cloth=NAAMAN_C):
    """Naaman at a distance: a purple Syrian captain's tunic with a gold band."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, up=up, extra=A.headcloth(cloth, cord="#E8B830") + A.BLACK_BEARD)

def naaman_house(p, w, h, seed):
    """Naaman's house in Damascus: the little maiden of Israel waiting on Naaman's wife."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84)]
    s = fit(b, h * 0.42)
    o.append(mk.person(p, round(w * 0.32), round(b), round(s, 3), body="#3A1E14", cloth="#6A2A5A", woman=True, hair="#1A1210", sw=3, extra=CROWN.replace("#E8B830", "#C8C2D6")))
    o.append(mk.person(p, round(w * 0.62), round(b), round(s * 0.66, 3), body="#5A2A16", cloth="#C8B89A", woman=True, hair="#2A1A10", sw=3, flip=True))
    return "".join(o)

def chariots_door(p, w, h, seed):
    """Naaman with his horses and his chariots standing at the door of the house of Elisha."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.7, "#B89A6A", dy=0),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.3)}" width="{f(w * 0.3)}" height="{f(h * 0.4)}" fill="#D8B88A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         f'<rect x="{f(w * 0.16)}" y="{f(h * 0.46)}" width="{f(w * 0.1)}" height="{f(h * 0.24)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    k = min(1.0, h / 340)
    o.append(E3.chariot(w * 0.66, b, k, flip=True, color="#3A2214", driver=NAAMAN_C) + E3.chariot(w * 0.92, b - h * 0.06, k * 0.8, flip=True, color="#3A2214", driver="#3A3A5A"))
    return "".join(o)

def jordan_wash(p, w, h, seed, clean=False):
    """Naaman dipping himself in the Jordan seven times; clean=True: risen up clean, his flesh as a little child's."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.36, seed, color="#6A8A5A", amp=12), ground(w, h, h * 0.46, "#B89A6A", dy=0),
         f'<path d="M-10 {f(h * 0.56)} C {f(w * 0.3)} {f(h * 0.52)} {f(w * 0.6)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(b, h * 0.5)
    if clean:
        o.append(V.rays(w * 0.5, h * 0.6, 24, 12, w * 0.4, color="#FFF4C2", op=0.4))
        o.append(mk.person(p, round(w * 0.5), round(h * 0.86), round(s, 3), body="#E8B08A", cloth="#F3EFE6", kind="Tunic", sw=3, up=[(-22, -158), (-40, -196), (-46, -228)]))
    else:
        o.append(mk.person(p, round(w * 0.5), round(h * 0.98), round(s, 3), body=SKIN, cloth="#F3EFE6", kind="Tunic", sw=3))
        o.append(f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.78)} {f(w * 0.6)} {f(h * 0.82)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" opacity="0.85"></path>')
        for i in range(7):
            o.append(f'<circle cx="{f(w * (0.12 + i * 0.03))}" cy="{f(h * 0.2)}" r="7" fill="{"#FFD23F" if i < 7 else "none"}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    o.append(E3.chariot(w * 0.86, h * 0.5, min(0.6, h / 560), flip=True, color="#3A2214", driver=NAAMAN_C))
    return "".join(o)

def mules_earth(p, w, h, seed):
    """Two mules' burden of earth, Naaman's company turning home."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#8A7A5A", amp=12), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    k = min(0.9, h / 360)
    for i, x in enumerate((0.36, 0.6)):
        o.append(N.ass(w * x, b - i * 6, k, color="#6A5A4A", flip=True)
                 + f'<path d="M{f(w * x - 30 * k)} {f(b - 104 * k)} C {f(w * x - 34 * k)} {f(b - 140 * k)} {f(w * x + 34 * k)} {f(b - 140 * k)} {f(w * x + 30 * k)} {f(b - 104 * k)} Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(naaman_fig(p, w * 0.14, b, fit(b, h * 0.4), flip=True))
    return "".join(o)

def silver_bags(p, w, h, seed):
    """Two talents of silver bound in two bags, with two changes of raiment, borne before Gehazi."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), hills(w, h, h * 0.5, seed, color="#8A7A5A", amp=12), ground(w, h, h * 0.6, "#A89A6A", dy=0)]
    s = fit(b, h * 0.4)
    for i in range(2):
        x = w * (0.44 + i * 0.16)
        o.append(man(p, x, b, s * 0.9, "#5A4A3A", up=[(-22, -158), (-20, -196), (0, -210)]) + f'<ellipse cx="{f(x - 4)}" cy="{f(b - 216 * s * 0.9)}" rx="{f(20 * s)}" ry="{f(14 * s)}" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(man(p, w * 0.2, b, s, "#7A6A4A"))
    return "".join(o)

def axe_head(p, w, h, seed):
    """At the Jordan: the sons of the prophets felling beams; the iron axe-head swimming on the water where the stick was cast."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), ground(w, h, h * 0.52, "#9A8A5A", dy=0),
         f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(4):
        x = w * (0.1 + i * 0.12)
        o.append(f'<path d="M{f(x)} {f(h * 0.56)} L {f(x)} {f(h * 0.2)}" stroke="#5A3A22" stroke-width="8"></path><circle cx="{f(x)}" cy="{f(h * 0.2)}" r="{f(w * 0.05)}" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.8)} L {f(w * 0.68)} {f(h * 0.78)} L {f(w * 0.69)} {f(h * 0.82)} L {f(w * 0.61)} {f(h * 0.84)} Z" fill="#7A7A82" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.56)} {f(h * 0.86)} L {f(w * 0.72)} {f(h * 0.8)}" stroke="#8A6A3A" stroke-width="5"></path>'
             f'<ellipse cx="{f(w * 0.64)}" cy="{f(h * 0.84)}" rx="{f(w * 0.08)}" ry="{f(h * 0.015)}" fill="none" stroke="#E8F6FA" stroke-width="2"></ellipse>')
    o.append(elisha_fig(p, w * 0.84, h * 0.66, fit(h * 0.66, h * 0.36), flip=True, up=[(22, -158), (40, -150), (60, -146)]))
    return "".join(o)

def dothan(p, w, h, seed, fire=False):
    """Dothan compassed about by night with horses and chariots; fire=True: the mountain full of horses and chariots of fire
    round about Elisha."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#8A6A7A"), J.city_hill(w * 0.5, h * 0.62, w * 0.4, h * 0.3, seed), ground(w, h, h * 0.62, "#3A3438", dy=0)]
    if fire:
        o.append(f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.36)} {f(h * 0.3)} {f(w * 0.3)} {f(h * 0.62)} Z M{f(w + 10)} {f(h * 0.6)} C {f(w * 0.8)} {f(h * 0.3)} {f(w * 0.64)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.62)} Z" fill="#3A2A3A" stroke="#0D0D0F" stroke-width="2"></path>')
        for i, (x, y) in enumerate(((0.12, 0.46), (0.24, 0.4), (0.78, 0.4), (0.9, 0.46))):
            o.append(fire_chariot(w * x, h * y, min(0.32, h / 1100), seed + i))
    for i in range(6):
        o.append(E3.chariot(w * (0.06 + i * 0.18), b - (i % 2) * h * 0.06, min(0.45, h / 800), color="#2A1A14", driver="#3A2A3A"))
    o.append(elisha_fig(p, w * 0.5, h * 0.48, fit(h * 0.48, h * 0.4) * 0.6))
    return "".join(o)

def blind_host(p, w, h, seed):
    """The host smitten with blindness led by Elisha into the midst of Samaria."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), J.jericho(w * 0.5, w + 10, h * 0.22, h * 0.62, seed, towers=3, houses=True), ground(w, h, h * 0.62, "#A89A6A", dy=0)]
    s = fit(b, h * 0.36)
    o.append(elisha_fig(p, w * 0.56, b, s, flip=True))
    for i in range(6):
        o.append(warrior(p, w * (0.06 + i * 0.07), b - (i % 2) * 8, s * 0.86, "#5A3A6A", flip=True))
    return "".join(o)

def siege_wall(p, w, h, seed, king=True):
    """Samaria besieged: the king passing by upon the wall, a woman crying up to him (6:28–29 told in words only)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A4A", "#A88A6A"), J.jericho(-10, w + 10, h * 0.36, h * 0.82, seed, towers=3, houses=False), ground(w, h, h * 0.82, "#4A3A30", dy=0)]
    if king:
        o.append(king_fig(p, w * 0.6, h * 0.36, fit(h * 0.36, h * 0.12), cloth="#5A5040"))
        o.append(mk.person(p, round(w * 0.3), round(b), round(fit(b, h * 0.7) * 0.6, 3), body="#3A1E14", cloth="#3A3A3E", woman=True, hair="#3A3430", sw=3, up=[(22, -158), (40, -200), (50, -230)]))
    return "".join(o)

# ---- 2 Kings 7–8 --------------------------------------------------------------------------------------------------------
def lepers_gate(p, w, h, seed):
    """Four leprous men sitting at the entrance of the gate of Samaria in the twilight."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#C8906A"), S4.gatehouse(w * 0.3, b, w * 0.5, h * 0.76), ground(w, h, b, "#5A4A40", dy=0)]
    s = fit(b, h * 0.4)
    for i in range(4):
        o.append(E.kneel(w * (0.56 + i * 0.1), b, s * 0.7, color=["#C8C0B0", "#A8A098", "#B8B0A0", "#988E86"][i], skin="#C8B8A8", flip=True))
    return "".join(o)

def empty_camp(p, w, h, seed, lepers=False):
    """The camp of the Syrians in the twilight with no man there: tents, horses tied, asses tied (lepers=True: four men
    carrying silver and raiment from a tent)."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#A87A7A"), ground(w, h, h * 0.5, "#5A4A40", dy=0), N.camp(14, -10, w + 10, h * 0.56, h * 0.86, seed, color=("#5A3A6A", "#4A3A3A", "#6A5A4A"))]
    for i in range(3):
        o.append(E3.horse(w * (0.12 + i * 0.12), b, min(0.5, h / 600), color="#3A2214") + N.ass(w * (0.7 + i * 0.1), b, min(0.5, h / 600)))
    if lepers:
        s = fit(b, h * 0.36)
        for i in range(2):
            o.append(man(p, w * (0.44 + i * 0.08), b, s * 0.8, "#C8C0B0", up=[(-22, -158), (-20, -196), (0, -210)]) + f'<ellipse cx="{f(w * (0.44 + i * 0.08) - 4)}" cy="{f(b - 214 * s * 0.8)}" rx="12" ry="8" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def strewn_way(w, h, seed):
    """All the way to the Jordan full of garments and vessels which the Syrians had cast away."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#7A8A5A", amp=12), ground(w, h, h * 0.5, "#B89A6A", dy=0),
         f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.86)} {f(h * 0.5)}" stroke="#C8B890" stroke-width="{f(w * 0.12)}" fill="none"></path>']
    for i in range(16):
        t = r.uniform(0, 1); x = w * (0.14 + 0.7 * t) + r.uniform(-30, 30); y = h * (1.0 - 0.5 * t) + r.uniform(-10, 10)
        if r.random() < 0.5: o.append(f'<path d="M{f(x - 14)} {f(y)} L {f(x + 14)} {f(y - 6)} L {f(x + 10)} {f(y + 8)} Z" fill="{r.choice(["#5A3A6A", "#8A2A2A", "#3A4A6A"])}" stroke="#0D0D0F" stroke-width="1.4"></path>')
        else: o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="9" ry="6" fill="{r.choice(["#C8C8D0", "#E8B830", "#B5652E"])}" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def gate_press(p, w, h, seed):
    """The gate of Samaria thronged with the people going out to the spoil; measures of flour and barley sold (7:17 told in
    words only)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#E8C890"), S4.gatehouse(w * 0.5, h * 0.8, w * 0.7, h * 0.66), ground(w, h, h * 0.8, "#A89A6A", dy=0)]
    s = fit(b, h * 0.3) * 0.45
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.98, h * 0.84, b, 16, s * 0.7, s))
    return "".join(o)

def hazael(p, w, h, seed):
    """Hazael coming to meet the man of God with forty camels' burden of every good thing of Damascus."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#F3D8A0"), hills(w, h, h * 0.44, seed, color="#8A8A9A", amp=24), ground(w, h, h * 0.56, "#C8B080", dy=0)]
    k = min(0.7, h / 460)
    for i in range(4):
        o.append(J1.camel(w * (0.5 + i * 0.12), b - (3 - i) * h * 0.03, k * (0.8 + 0.05 * i), color="#B5844A"))
    o.append(captain(p, w * 0.32, b, fit(b, h * 0.42), cloth="#5A3A6A", spear=False, flip=True))
    o.append(elisha_fig(p, w * 0.12, b, fit(b, h * 0.42)))
    return "".join(o)

def coverlet(w, h, seed):
    """The king's bedchamber in Damascus on the morrow: a coverlet dipped in water by the bed (8:15 told in words only)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2A"></rect>', S3.cedar(w, h, h * 0.84).replace("#8A4A26", "#5A3A26").replace("#9A5A30", "#6A4A30"),
         f'<rect x="{f(w * 0.14)}" y="{f(h * 0.7)}" width="{f(w * 0.56)}" height="{f(h * 0.08)}" fill="#6A3A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.86)} C {f(w * 0.72)} {f(h * 0.8)} {f(w * 0.86)} {f(h * 0.78)} {f(w * 0.9)} {f(h * 0.86)} Z" fill="#5A3A6A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<ellipse cx="{f(w * 0.82)}" cy="{f(h * 0.88)}" rx="{f(w * 0.08)}" ry="{f(h * 0.02)}" fill="#2C9DB8" opacity="0.6"></ellipse>']
    return "".join(o)

# ---- 2 Kings 9–10 -------------------------------------------------------------------------------------------------------
JEHU_C = "#3A5A2A"
def inner_chamber(p, w, h, seed):
    """The young prophet pouring the vial of oil on Jehu's head in an inner chamber, the door open behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3A30"></rect>',
         f'<rect x="{f(w * 0.74)}" y="{f(h * 0.2)}" width="{f(w * 0.18)}" height="{f(b - h * 0.2)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.4"></rect>', ground(w, h, b, "#2A1E18", dy=0)]
    s = fit(b, h * 0.44)
    o.append(captain(p, w * 0.32, b, s, cloth=JEHU_C, spear=False))
    o.append(man(p, w * 0.52, b, s * 0.95, "#6A645E", flip=True, up=[(22, -158), (0, -200), (-24, -230)]) + S1.vial(w * 0.52 - 30 * s, b - 236 * s, s * 0.7, rot=150, pour=20 * s)
             + S1.drops(w * 0.32, b - 210 * s, 4, seed, spread=8))
    return "".join(o)

def stairs_garments(p, w, h, seed):
    """The captains putting their garments under Jehu on the top of the stairs, and the trumpet blown: Jehu is king."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, b, "#B89A6A", dy=0)]
    for i in range(6):
        o.append(f'<rect x="{f(w * (0.24 + i * 0.04))}" y="{f(b - (i + 1) * h * 0.08)}" width="{f(w * (0.52 - i * 0.08))}" height="{f(h * 0.08)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    top = b - 6 * h * 0.08
    o.append("".join(f'<path d="M{f(w * (0.42 + i * 0.03))} {f(top)} l 20 0 l -6 {f(h * 0.06)} l -18 0 Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></path>' for i, c in enumerate(("#8A2A2A", "#3A4A6A", "#6A5A3A", "#5A3A6A"))))
    o.append(captain(p, w * 0.5, top, fit(top, top - h * 0.36), cloth=JEHU_C, spear=False))
    s = fit(b, h * 0.36)
    o.append(J.trumpeter(p, w * 0.12, b, s) + J.blasts(w * 0.12 + 70 * s, b - 170 * s, s))
    o.append(crowd_at(p, w, h, seed, w * 0.78, w * 0.98, h * 0.8, b, 5, s * 0.7, s, flip=True))
    return "".join(o)

def watchtower(p, w, h, seed, furious=True):
    """The watchman on the tower in Jezreel; far off the company of Jehu, his chariot driving furiously in a cloud of dust."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#E8B880"), hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.58, "#C8A06A", dy=0),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.2)}" width="{f(w * 0.2)}" height="{f(b - h * 0.2)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         + "".join(f'<rect x="{f(w * 0.06 + i * w * 0.05)}" y="{f(h * 0.17)}" width="{f(w * 0.025)}" height="{f(h * 0.03)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(4)),
         ground(w, h, b, "#A88A5A", dy=0)]
    o.append(mk.person(p, round(w * 0.16), round(h * 0.17), round(fit(h * 0.17, h * 0.04) * 0.5, 3), body="#2A140C", cloth="#5A6A8A", kind="Tunic", sw=2, up=[(22, -158), (40, -170), (60, -176)]))
    k = min(0.7, h / 500)
    o.append(f'<ellipse cx="{f(w * 0.82)}" cy="{f(h * 0.6)}" rx="{f(w * 0.16)}" ry="{f(h * 0.06)}" fill="#E8D0A0" opacity="0.8"></ellipse>')
    o.append(E3.chariot(w * 0.7, h * 0.66, k, flip=True, color="#3A2214", driver=JEHU_C) + mk.speed(w * 0.84, h * 0.6, 12, 10, w * 0.2, seed, color="#8A6A3A", op=0.6))
    return "".join(o)

def naboth_plat(p, w, h, seed):
    """The portion of Naboth the Jezreelite: two chariots met in the field, one turned to flee (9:24 told in words only)."""
    o = [vineyard(p, w, h, seed, empty=True)]
    k = min(0.6, h / 560)
    o.append(E3.chariot(w * 0.3, h * 0.92, k, color="#3A2214", driver=AHAB_C) + E3.chariot(w * 0.72, h * 0.96, k, flip=True, color="#3A2214", driver=JEHU_C))
    return "".join(o)

def jezebel_window(p, w, h, seed, empty=False):
    """Jezebel with painted eyes and attired head looking out at the window over the gate; empty=True: the window empty, the
    gate below (9:33–37 told in words only)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), f'<rect x="{f(w * 0.2)}" y="-10" width="{f(w * 0.7)}" height="{f(b + 10)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2.6"></rect>',
         f'<path d="M{f(w * 0.36)} {f(b)} L {f(w * 0.36)} {f(h * 0.66)} C {f(w * 0.36)} {f(h * 0.56)} {f(w * 0.6)} {f(h * 0.56)} {f(w * 0.6)} {f(h * 0.66)} L {f(w * 0.6)} {f(b)} Z" fill="#2A1A14" stroke="#0D0D0F" stroke-width="2.4"></path>',
         S3.window(w * 0.62, h * 0.12, w * 0.2, h * 0.24), ground(w, h, b, "#8A7A5A", dy=0)]
    if not empty:
        o.append(f'<g transform="translate({f(w * 0.72)} {f(h * 0.36)})"><path d="M-20 0 C -24 -40 -16 -70 0 -76 C 16 -70 24 -40 20 0 Z" fill="#1A1214" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<circle cx="0" cy="-60" r="14" fill="#D9A27A" stroke="#0D0D0F" stroke-width="2"></circle><path d="M-14 -66 C -10 -82 10 -82 14 -66" fill="#0D0D0F"></path>'
                 f'<path d="M-12 -76 L -8 -86 L -2 -78 L 4 -88 L 10 -76 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
        o.append(E3.chariot(w * 0.14, b, min(0.7, h / 480), color="#3A2214", driver=JEHU_C))
    return "".join(o)

def gate_dawn(w, h, seed):
    """The entrance of the gate of Jezreel in the morning (10:7–9 told in words only)."""
    return "".join([sky(w, h, "#5A5A7A", "#FFC89A"), sun(w * 0.8, h * 0.4, 24, color="#FFE680", op=0.4), S4.gatehouse(w * 0.5, h * 0.9, w * 0.6, h * 0.66), ground(w, h, h * 0.9, "#6A5A4A", dy=0)])

def baal_house(p, w, h, seed, broken=False):
    """The house of Baal in Samaria filled from one end to another; broken=True: its pillar burned and the house broken down."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A2A3A" if broken else "#C8B8A0", "#E8803A" if broken else "#E8C8A0"), ground(w, h, h * 0.8, "#6A5A4A", dy=0)]
    if broken:
        o.append(S4.stone_heap(w * 0.5, b, w * 0.7, h * 0.3, seed) + E.blaze(w * 0.5, h * 0.66, w * 0.16, h * 0.3, seed, n=5))
        o.append("".join(f'<circle cx="{f(w * 0.5 + (i % 2) * 20)}" cy="{f(h * (0.3 - i * 0.06))}" r="{f(w * 0.07)}" fill="#3A2A2E" opacity="0.7"></circle>' for i in range(4)))
    else:
        o.append(f'<rect x="{f(w * 0.14)}" y="{f(h * 0.28)}" width="{f(w * 0.72)}" height="{f(h * 0.52)}" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
                 f'<path d="M{f(w * 0.1)} {f(h * 0.28)} L {f(w * 0.5)} {f(h * 0.1)} L {f(w * 0.9)} {f(h * 0.28)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<rect x="{f(w * 0.4)}" y="{f(h * 0.46)}" width="{f(w * 0.2)}" height="{f(h * 0.34)}" fill="#1A1214" stroke="#0D0D0F" stroke-width="2.4"></rect>')
        s = fit(b, h * 0.3)
        for i in range(6):
            o.append(warrior(p, w * (0.06 + i * 0.05) if i < 3 else w * (0.8 + (i - 3) * 0.06), b, s * 0.8, JEHU_C, flip=i >= 3))
    return "".join(o)

def hazael_map(w, h):
    """Hazael smiting Israel from the Jordan eastward: Gilead and Bashan, from Aroer by the Arnon (a technical map)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.42)} {f(h * 0.06)} C {f(w * 0.44)} {f(h * 0.4)} {f(w * 0.4)} {f(h * 0.7)} {f(w * 0.44)} {f(h * 0.94)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>' + label(w * 0.4, h * 0.5, "JORDAN", "#8FD0E2", 9, "end"))
    o.append(f'<rect x="{f(w * 0.48)}" y="{f(h * 0.08)}" width="{f(w * 0.44)}" height="{f(h * 0.82)}" fill="#D7261E" fill-opacity="0.2" stroke="#D7261E" stroke-width="2" stroke-dasharray="6 4"></rect>')
    for nm, x, y in (("BASHAN", 0.7, 0.18), ("GILEAD", 0.66, 0.46), ("AROER · ARNON", 0.62, 0.84)):
        o.append(node(w * x, h * y, nm, "#D7261E", r=5, dy=-12, size=9))
    o.append(node(w * 0.92, h * 0.06, "DAMASCUS", "#FFD23F", r=5, dy=14, size=9))
    return "".join(o)

# ---- 2 Kings 11–12 ------------------------------------------------------------------------------------------------------
import ruth1 as R1
def hidden_child(p, w, h, seed):
    """Jehosheba and the nurse hiding the child Joash in a bedchamber of the house of Jehovah, a lamp burning."""
    from genesis.art4 import clay_lamp
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>', S3.cedar(w, h, h * 0.84).replace("#8A4A26", "#6A3A20"),
         clay_lamp(w * 0.82, h * 0.5, min(1.2, h / 260)), f'<circle cx="{f(w * 0.82)}" cy="{f(h * 0.46)}" r="{f(h * 0.36)}" fill="#FFC14D" opacity="0.1"></circle>']
    s = fit(b, h * 0.4)
    o.append(mk.person(p, round(w * 0.36), round(b), round(s, 3), body="#3A1E14", cloth="#2A4A6A", woman=True, hair="#1A1210", sw=3, up=R1.HOLD_BABY, extra=R1.baby(10, -130, 0.8)))
    o.append(mk.person(p, round(w * 0.56), round(b), round(s * 0.95, 3), body="#3A1E14", cloth="#6A5A4A", woman=True, hair="#3A3430", sw=3, flip=True))
    return "".join(o)

def child_king(p, w, h, seed, athaliah=False):
    """The young king by the pillar in the house of Jehovah with the crown upon him, the guard round about with David's spears
    and shields, the trumpets; athaliah=True: Athaliah crying Treason at the side."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.62, "#C8B88A", dy=0), temple_front(w * 0.5, h * 0.62, w * 0.56, seed)]
    s = fit(b, h * 0.38)
    o.append(mk.person(p, round(w * 0.5), round(b), round(s * 0.55, 3), body="#5A2A16", cloth="#F3EFE6", kind="Tunic", sw=3, extra=S3.KING))
    for i in range(4):
        for d in (-1, 1):
            x = w * 0.5 + d * w * (0.12 + i * 0.08)
            o.append(warrior(p, x, b - i * 4, s * (0.95 - i * 0.05), "#8A3A1E" if i % 2 else "#3A4A6A", flip=d > 0))
    if athaliah:
        o.append(mk.person(p, round(w * 0.06), round(b), round(s, 3), body="#5A2A16", cloth="#7A1A2A", woman=True, hair="#0D0D0F", sw=3, up=[(22, -158), (40, -196), (50, -228)], extra=CROWN))
    else:
        o.append(J.trumpeter(p, w * 0.06, b, s * 0.9) + J.blasts(w * 0.06 + 60 * s, b - 160 * s, s * 0.9))
    return "".join(o)

def horses_entry(w, h, seed):
    """The way of the horses' entry to the king's house, empty (11:16 told in words only)."""
    return "".join([sky(w, h, "#5A4A5A", "#C8A080"), S4.gatehouse(w * 0.6, h * 0.9, w * 0.56, h * 0.62), ground(w, h, h * 0.9, "#6A5A4A", dy=0),
                    f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.92)} {f(w * 0.5)} {f(h * 0.9)} {f(w * 0.6)} {f(h * 0.9)}" stroke="#8A7A5A" stroke-width="{f(w * 0.08)}" fill="none"></path>'])

def chest(p, w, h, seed):
    """Jehoiada's chest with a hole bored in its lid, beside the altar; the people bringing money."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.6, "#C8B88A", dy=0), horned_altar(w * 0.2, b, min(1.0, h / 360), fire=True, seed=seed),
         f'<rect x="{f(w * 0.4)}" y="{f(b - h * 0.16)}" width="{f(w * 0.18)}" height="{f(h * 0.16)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         f'<rect x="{f(w * 0.39)}" y="{f(b - h * 0.18)}" width="{f(w * 0.2)}" height="{f(h * 0.03)}" fill="#A8703A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<ellipse cx="{f(w * 0.49)}" cy="{f(b - h * 0.165)}" rx="8" ry="3" fill="#0D0D0F"></ellipse>']
    s = fit(b, h * 0.4)
    o.append(K1.priest(p, w * 0.66, b, s, flip=True))
    o.append(crowd_at(p, w, h, seed, w * 0.74, w * 0.98, h * 0.7, b, 5, s * 0.6, s * 0.9, flip=True))
    return "".join(o)

def repairers(p, w, h, seed):
    """Carpenters, builders, masons and hewers of stone repairing the breaches of the house of Jehovah."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.66, "#C8B88A", dy=0), temple_front(w * 0.5, h * 0.66, w * 0.5, seed)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.66)} L {f(w * 0.3)} {f(h * 0.3)} M{f(w * 0.36)} {f(h * 0.66)} L {f(w * 0.36)} {f(h * 0.3)}" stroke="#8A6A3A" stroke-width="4"></path>'
             + "".join(f'<path d="M{f(w * 0.3)} {f(h * (0.36 + i * 0.08))} L {f(w * 0.36)} {f(h * (0.36 + i * 0.08))}" stroke="#8A6A3A" stroke-width="3"></path>' for i in range(4)))
    s = fit(b, h * 0.3)
    for i in range(5):
        o.append(man(p, w * (0.06 + i * 0.07) if i < 3 else w * (0.8 + (i - 3) * 0.1), b, s, WAR[i % 4], flip=i >= 3, up=[(-22, -158), (-30, -190), (-20, -214)]))
    o.append(box(w * 0.14, b, w * 0.08, w * 0.04, h * 0.06, fill="#D8CCB0", top="#E8DCC0", side="#B8AC90"))
    return "".join(o)

def millo(w, h, seed):
    """The house of Millo on the way down to Silla at dusk (12:20–21 told in words only)."""
    return "".join([sky(w, h, "#3A1A2A", "#C8603A"), J.city_hill(w * 0.5, h * 0.7, w * 0.8, h * 0.4, seed), ground(w, h, h * 0.72, "#2A1E1E", dy=0),
                    f'<path d="M{f(w * 0.6)} {f(h * 0.72)} C {f(w * 0.7)} {f(h * 0.82)} {f(w * 0.8)} {f(h * 0.92)} {f(w * 0.96)} {f(h + 10)}" stroke="#5A4A3A" stroke-width="{f(w * 0.05)}" fill="none"></path>'])

# ---- 2 Kings 13–14 ------------------------------------------------------------------------------------------------------
def arrow_window(p, w, h, seed, ground_smite=False):
    """Elisha sick upon his bed, his hands upon the king's hands on the bow, the window opened eastward and the arrow of
    victory flying out; ground_smite=True: the king smiting the ground with the arrows."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.window(w * 0.66, h * 0.1, w * 0.26, h * 0.34, inner="#FFE6A0"),
         bed(w, h, w * 0.04, w * 0.42, b, cover="#8A6A3A", head="#C98E66", hair="#8A847A")]
    s = fit(b, h * 0.42)
    if ground_smite:
        o.append(king_fig(p, w * 0.62, b, s, cloth="#7A1A2A", up=[(-22, -158), (-30, -110), (-40, -40)]))
        o.append("".join(f'<path d="M{f(w * 0.6 - 40 * s + i * 6)} {f(b)} L {f(w * 0.6 - 30 * s + i * 6)} {f(b - 40 * s)}" stroke="#3E2416" stroke-width="3"></path>' for i in range(3)))
    else:
        o.append(king_fig(p, w * 0.56, b, s, cloth="#7A1A2A", up=[(22, -158), (50, -170), (80, -180)]))
        o.append(f'<path d="M{f(w * 0.56 + 80 * s)} {f(b - 210 * s)} C {f(w * 0.56 + 100 * s)} {f(b - 180 * s)} {f(w * 0.56 + 100 * s)} {f(b - 150 * s)} {f(w * 0.56 + 80 * s)} {f(b - 120 * s)}" stroke="#5A3A22" stroke-width="4" fill="none"></path>')
        o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.26)} L {f(w * 0.86)} {f(h * 0.2)}" stroke="#3E2416" stroke-width="3"></path><path d="M{f(w * 0.86)} {f(h * 0.2)} l -10 -2 l 4 8 Z" fill="#C8C2D6"></path>')
    return "".join(o)

def elisha_tomb(p, w, h, seed):
    """The sepulchre of Elisha, a band of Moabites seen on the hills, the burying party hurrying (13:21)."""
    o = [JA_cave(w, h, seed)]
    o.append("".join(mk.person(p, round(w * (0.7 + i * 0.05)), round(h * 0.34), round(fit(h * 0.34, h * 0.26) * 0.4, 3), body="#1A0E10", cloth="#5A3A2A", kind="Tunic", sw=2, flip=True, extra=E4.SPEAR) for i in range(4)))
    return "".join(o)
import jos.art as _JA
def JA_cave(w, h, seed): return _JA.cave(w, h, seed, sealed=False, dusk=True)

def thistle_cedar(w, h, seed):
    """The thistle that was in Lebanon and the cedar that was in Lebanon, and a wild beast passing by that trod down the thistle."""
    o = [sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.5, seed, color="#6A7A5A", amp=24), ground(w, h, h * 0.76, "#8A7A5A", dy=0)]
    x, y, s = w * 0.68, h * 0.8, min(1.2, h / 300)
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 L 0 -140" stroke="#5A3A22" stroke-width="10"></path>'
             + "".join(f'<path d="M{-80 + k * 12} {-40 - k * 26} L {80 - k * 12} {-40 - k * 26} L 0 {-66 - k * 26} Z" fill="#1F4A34" stroke="#0D0D0F" stroke-width="1.6"></path>' for k in range(5)) + '</g>')
    tx = w * 0.24
    o.append("".join(f'<path d="M{f(tx)} {f(y)} L {f(tx + dx)} {f(y - 40)}" stroke="#5A6A3A" stroke-width="3"></path><circle cx="{f(tx + dx)}" cy="{f(y - 44)}" r="6" fill="#8A4A8A" stroke="#0D0D0F" stroke-width="1.4"></circle>' for dx in (-14, 0, 14)))
    o.append(J2.lion(w * 0.36, y + 4, min(0.6, h / 500), flip=True, roar=False))
    return "".join(o)

def wall_breach(w, h, seed):
    """The wall of Jerusalem broken down from the gate of Ephraim unto the corner gate, four hundred cubits."""
    return "".join([sky(w, h, "#5A4A5A", "#C8A080"), J.jericho(-10, w * 0.3, h * 0.36, h * 0.84, seed, towers=1, houses=True),
                    J.collapse(w * 0.3, w * 0.74, h * 0.84, h * 0.3, seed, color="#B5652E"), J.jericho(w * 0.74, w + 10, h * 0.36, h * 0.84, seed + 1, towers=1, houses=True),
                    ground(w, h, h * 0.84, "#4A3A30", dy=0), dim(w * 0.3, h * 0.92, w * 0.74, h * 0.92, "400 CUBITS")])

def border_map(w, h):
    """Jeroboam restoring the border of Israel from the entrance of Hamath unto the sea of the Arabah (a technical map)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.1)} C {f(w * 0.52)} {f(h * 0.4)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.52)} {f(h * 0.8)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<ellipse cx="{f(w * 0.52)}" cy="{f(h * 0.86)}" rx="{f(w * 0.02)}" ry="{f(h * 0.06)}" fill="#2C9DB8"></ellipse>')
    o.append(route([(w * 0.6, h * 0.06), (w * 0.52, h * 0.86)], color="#FFD23F"))
    o.append(node(w * 0.6, h * 0.06, "ENTRANCE OF HAMATH", "#FFD23F", r=5, dy=14, size=9) + node(w * 0.52, h * 0.86, "SEA OF THE ARABAH", "#FFD23F", r=5, dy=-12, size=9)
             + node(w * 0.7, h * 0.24, "DAMASCUS", "#8FD0E2", r=4, dy=-10, size=9) + node(w * 0.4, h * 0.56, "SAMARIA", "#D7261E", r=5, dy=-10, size=9))
    return "".join(o)

# ---- 2 Kings 15–16 ------------------------------------------------------------------------------------------------------
def separate_house(p, w, h, seed):
    """The leper king dwelling in a separate house, its door shut, outside the bustle of the king's house."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8A9AB8", "#E8D8C8"), J.city_hill(w * 0.76, h * 0.6, w * 0.4, h * 0.3, seed), ground(w, h, h * 0.62, "#A89A80", dy=0),
         f'<rect x="{f(w * 0.12)}" y="{f(h * 0.42)}" width="{f(w * 0.3)}" height="{f(h * 0.34)}" fill="#C8B8A0" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<rect x="{f(w * 0.24)}" y="{f(h * 0.56)}" width="{f(w * 0.08)}" height="{f(h * 0.2)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.16)}" y="{f(h * 0.48)}" width="{f(w * 0.05)}" height="{f(h * 0.05)}" fill="#FFC14D" stroke="#0D0D0F" stroke-width="1.6"></rect>']
    return "".join(o)

ASSYRIA = [("SAMARIA", 0.32, 0.56), ("DAMASCUS", 0.52, 0.32), ("IJON", 0.4, 0.2), ("HAZOR", 0.36, 0.34), ("GILEAD", 0.5, 0.56), ("NINEVEH", 0.9, 0.12), ("KIR", 0.92, 0.42)]
def assyria_map(w, h, hi=(), arrows=()):
    """Assyria's march westward as a technical map (hi: places taken; arrows: (from, to) pairs)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.12)} {f(h * 0.3)} {f(w * 0.1)} {f(h * 0.7)} {f(w * 0.06)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.78)} -10 C {f(w * 0.8)} {f(h * 0.3)} {f(w * 0.84)} {f(h * 0.6)} {f(w * 0.86)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>' + label(w * 0.76, h * 0.7, "EUPHRATES", "#8FD0E2", 8, "end"))
    pos = {n: (w * x, h * y) for n, x, y in ASSYRIA}
    for a, b in arrows: o.append(route([pos[a], pos[b]], color="#D7261E"))
    for nm, x, y in ASSYRIA:
        o.append(node(w * x, h * y, nm, "#D7261E" if nm in hi else ("#FFD23F" if nm == "NINEVEH" else "#8FD0E2"), r=5, dy=-11, size=9))
    return "".join(o)

def two_altars(w, h, damascus_new=True):
    """The great altar after the fashion of the altar at Damascus, and the brazen altar moved to the north side of it."""
    o = [bp(w, h), title_bar(w, "THE ALTAR AFTER THE PATTERN OF DAMASCUS")]
    o.append(box(w * 0.18, h * 0.86, w * 0.4, w * 0.16, h * 0.3, fill="#C8BC9C", top="#D8CCB0", side="#A89C80") + tag(w * 0.38, h * 0.64, "THE GREAT ALTAR", w * 0.3, h * 0.3))
    o.append(box(w * 0.7, h * 0.86, w * 0.16, w * 0.08, h * 0.16, fill=BRASS, top="#C8863E", side="#8A5A2A") + tag(w * 0.78, h * 0.74, "THE BRAZEN ALTAR · NORTH SIDE", w * 0.6, h * 0.48))
    return "".join(o)

def sea_pavement(w, h):
    """The sea taken down from off the brazen oxen and set upon a pavement of stone; the bases stripped of their panels."""
    o = [bp(w, h), title_bar(w, "THE SEA UPON A PAVEMENT OF STONE")]
    u = min(w * 0.7 / 12, h * 0.66 / 7); cx = w * 0.42; base = h * 0.86
    o.append(f'<rect x="{f(cx - 6 * u)}" y="{f(base - 0.6 * u)}" width="{f(12 * u)}" height="{f(0.6 * u)}" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="2"></rect>')
    top = base - 5.6 * u
    o.append(f'<path d="M{f(cx - 5 * u)} {f(top)} C {f(cx - 5 * u)} {f(top + 4 * u)} {f(cx - 3 * u)} {f(top + 5 * u)} {f(cx)} {f(top + 5 * u)} C {f(cx + 3 * u)} {f(top + 5 * u)} {f(cx + 5 * u)} {f(top + 4 * u)} {f(cx + 5 * u)} {f(top)} Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(top)}" rx="{f(5.3 * u)}" ry="{f(0.9 * u)}" fill="#C8863E" stroke="#0D0D0F" stroke-width="2.4"></ellipse>')
    o.append(f'<g opacity="0.4">' + S1.cow(w * 0.84, base, u / 80, color=BRASS, patch="#C8863E") + '</g>' + tag(w * 0.84, base - u, "THE BRAZEN OXEN, REMOVED", w * 0.7, base - 4 * u))
    return "".join(o)

# ---- 2 Kings 17 ---------------------------------------------------------------------------------------------------------
def captives(p, w, h, seed, city="samaria"):
    """A long column of captives carried away eastward, soldiers with spears beside them, the city smoking behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A5A", "#E8A06A"), J.city_hill(w * 0.12, h * 0.56, w * 0.3, h * 0.24, seed), ground(w, h, h * 0.58, "#A88A6A", dy=0)]
    o.append("".join(f'<circle cx="{f(w * 0.12 + (i % 2) * 14)}" cy="{f(h * (0.3 - i * 0.06))}" r="{f(w * 0.05)}" fill="#3A2A2E" opacity="0.6"></circle>' for i in range(4)))
    for i in range(14):
        t = i / 13; x = w * (0.22 + 0.74 * t); y = h * (0.66 + 0.26 * t)
        s = fit(y, y - h * (0.14 + 0.16 * t))
        if i % 4 == 3: o.append(warrior(p, x, y, s, "#7A5A2A", flip=True))
        else: o.append(mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth=["#5A5A6A", "#6A5A4A", "#4A4A5A"][i % 3], woman=i % 3 == 1, hair="#1A1210" if i % 3 == 1 else False, sw=2, flip=True))
    return "".join(o)

EXILE = [("SAMARIA", 0.14, 0.6), ("NINEVEH", 0.6, 0.16), ("HALAH", 0.7, 0.3), ("GOZAN · THE HABOR", 0.5, 0.12), ("CITIES OF THE MEDES", 0.9, 0.3),
         ("BABYLON", 0.72, 0.74), ("CUTHAH", 0.76, 0.66), ("HAMATH", 0.28, 0.28), ("SEPHARVAIM", 0.66, 0.6)]
def exile_map(w, h, inward=False):
    """Israel carried away into Assyria (or, inward=True, the nations brought from Babylon, Cuthah, Avva, Hamath and
    Sepharvaim into the cities of Samaria) as a technical map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.08)} -10 C {f(w * 0.06)} {f(h * 0.3)} {f(w * 0.05)} {f(h * 0.7)} {f(w * 0.03)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.46)} -10 C {f(w * 0.5)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.74)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<path d="M{f(w * 0.6)} -10 C {f(w * 0.66)} {f(h * 0.3)} {f(w * 0.76)} {f(h * 0.6)} {f(w * 0.8)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>')
    pos = {n: (w * x, h * y) for n, x, y in EXILE}
    if inward:
        for n in ("BABYLON", "CUTHAH", "HAMATH", "SEPHARVAIM"): o.append(route([pos[n], pos["SAMARIA"]], color="#D7261E"))
        show = ("SAMARIA", "BABYLON", "CUTHAH", "HAMATH", "SEPHARVAIM")
    else:
        for n in ("HALAH", "GOZAN · THE HABOR", "CITIES OF THE MEDES"): o.append(route([pos["SAMARIA"], pos[n]], color="#D7261E"))
        show = ("SAMARIA", "NINEVEH", "HALAH", "GOZAN · THE HABOR", "CITIES OF THE MEDES")
    for n in show:
        x, y = pos[n]; o.append(node(x, y, n, "#FFD23F" if n == "SAMARIA" else "#D7261E", r=5, dy=-11, size=9))
    return "".join(o)

def lions_samaria(p, w, h, seed):
    """Lions among the strangers settled in the cities of Samaria (17:25 told without harm drawn)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), J.city_hill(w * 0.7, h * 0.56, w * 0.5, h * 0.3, seed), ground(w, h, h * 0.58, "#A89A6A", dy=0)]
    k = min(0.8, h / 400)
    o.append(J2.lion(w * 0.24, b, k, roar=True) + J2.lion(w * 0.5, b - h * 0.04, k * 0.8, roar=False))
    return "".join(o)

def strange_gods(w, h, seed):
    """Every nation making gods of its own in the houses of the high places: idols on their pedestals."""
    r = random.Random(seed)
    o = [sky(w, h, "#3A2A3A", "#A86A5A"), ground(w, h, h * 0.8, "#4A3A30", dy=0)]
    for i in range(5):
        x = w * (0.12 + i * 0.19); s = min(w, h) / 360
        o.append(f'<g transform="translate({f(x)} {f(h * 0.82)}) scale({f(s)})"><rect x="-26" y="-20" width="52" height="20" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M-14 -20 L -18 -90 C -16 -110 16 -110 18 -90 L 14 -20 Z" fill="{r.choice(["#B5652E", "#8A8478", "#C8A030", "#5A4A6A"])}" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<circle cx="0" cy="-112" r="14" fill="{r.choice(["#B5652E", "#C8A030"])}" stroke="#0D0D0F" stroke-width="2"></circle></g>')
        o.append(E.blaze(x, h * 0.86, w * 0.03, h * 0.05, seed + i, n=3))
    return "".join(o)

# ---- 2 Kings 18–19 ------------------------------------------------------------------------------------------------------
ASSY_C = "#8A5A1A"
def brazen_serpent(w, h, seed):
    """The brazen serpent that Moses had made, broken in pieces; the Asherah cut down."""
    o = [sky(w, h, "#5A3A3A", "#E8A06A"), ground(w, h, h * 0.8, "#5A4A3A", dy=0), N.brass_serpent(w * 0.4, h * 0.2, h * 0.6, "bz%d" % seed)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.3)} L {f(w * 0.5)} {f(h * 0.5)}" stroke="#D7261E" stroke-width="5"></path>')
    o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.82)} L {f(w * 0.9)} {f(h * 0.76)}" stroke="#5A3A22" stroke-width="16" stroke-linecap="round"></path>')
    return "".join(o)

def upper_pool(p, w, h, seed, wall_people=True):
    """Rabshakeh and the great army by the conduit of the upper pool, the people of Jerusalem on the wall above."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), J.jericho(w * 0.5, w + 10, h * 0.2, h * 0.62, seed, towers=3, houses=True), ground(w, h, h * 0.62, "#A89A6A", dy=0),
         f'<ellipse cx="{f(w * 0.36)}" cy="{f(h * 0.7)}" rx="{f(w * 0.14)}" ry="{f(h * 0.04)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    if wall_people:
        for i in range(8):
            o.append(f'<circle cx="{f(w * (0.54 + i * 0.055))}" cy="{f(h * 0.18)}" r="{f(h * 0.018)}" fill="#3A1E14" stroke="#0D0D0F" stroke-width="1"></circle>')
    s = fit(b, h * 0.36)
    o.append(captain(p, w * 0.24, b, s, cloth=ASSY_C, flip=True, up=[(22, -158), (40, -200), (50, -230)]))
    for i in range(7):
        o.append(warrior(p, w * (0.02 + i * 0.04), b - (i % 2) * h * 0.04, s * 0.7, ASSY_C))
    return "".join(o)

def letter_spread(p, w, h, seed):
    """Hezekiah spreading the letter before Jehovah in the house of Jehovah."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1A"></rect>', V.rays(w * 0.6, h * 0.3, 30, 20, max(w, h), color="#FFD23F", op=0.12),
         ground(w, h, b, "#2A1A10", dy=0), S3.letter(w * 0.62, b - h * 0.04, min(1.2, h / 260), rot=0)]
    o.append(E.kneel(w * 0.34, b, fit(b, h * 0.4) * 0.85, color="#5A5040", skin="#C98E66"))
    return "".join(o)

def silent_camp(p, w, h, seed):
    """The camp of the Assyrians at morning, silent: tents and standards, no one moving (19:35 told in words only)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8A8AA8", "#F3D8C0"), sun(w * 0.8, h * 0.36, 22, color="#FFE680", op=0.4), hills(w, h, h * 0.44, seed, color="#6A6A6A", amp=16),
         ground(w, h, h * 0.54, "#8A7A6A", dy=0), N.camp(22, -10, w + 10, h * 0.58, h * 0.96, seed, color=("#8A5A1A", "#6A4A2A", "#5A4A3A"))]
    return "".join(o)

def nineveh(w, h, seed):
    """Nineveh on the Tigris, the house of Nisroch with its winged bulls (19:37 told in words only)."""
    o = [sky(w, h, "#3A2A2A", "#C8803A"), ground(w, h, h * 0.76, "#8A6A4A", dy=0),
         f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.86)}" stroke="#2C7DA8" stroke-width="12" fill="none"></path>']
    for k in range(4):
        wd = w * (0.7 - k * 0.14); y = h * (0.76 - k * 0.12)
        o.append(f'<rect x="{f(w * 0.5 - wd / 2)}" y="{f(y - h * 0.12)}" width="{f(wd)}" height="{f(h * 0.12)}" fill="{["#B8905A", "#A8804A", "#98703A", "#88602A"][k]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

# ---- 2 Kings 20–21 ------------------------------------------------------------------------------------------------------
def dial(w, h, back=False):
    """The dial of Ahaz: a stair of steps and the shadow upon it; back=True: the shadow gone back ten steps."""
    o = [sky(w, h, "#FFE6A0", "#E8B880"), sun(w * 0.86, h * 0.14, 30, color="#FFF4C2", op=0.8), ground(w, h, h * 0.86, "#B89A6A", dy=0)]
    n = 14
    for i in range(n):
        x = w * (0.12 + i * 0.05); top = h * (0.86 - (i + 1) * 0.04)
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(w * 0.05)}" height="{f(h * 0.86 - top)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    k = 2 if back else 12
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.86)} L {f(w * (0.12 + k * 0.05))} {f(h * 0.86)} L {f(w * (0.12 + k * 0.05))} {f(h * (0.86 - k * 0.04))} L {f(w * 0.12)} {f(h * 0.86)} Z" fill="#2A2A4A" opacity="0.45"></path>')
    o.append(f'<path d="M{f(w * 0.8)} {f(h * 0.86)} L {f(w * 0.8)} {f(h * 0.2)}" stroke="#5A3A22" stroke-width="10"></path>')
    if back: o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.2)} C {f(w * 0.5)} {f(h * 0.12)} {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.24)} {f(h * 0.34)}" stroke="#D7261E" stroke-width="4" fill="none" stroke-dasharray="8 5"></path>'
                      f'<path d="M{f(w * 0.24)} {f(h * 0.34)} l -4 -16 l 14 8 Z" fill="#D7261E"></path>')
    return "".join(o)

def treasures(p, w, h, seed):
    """Hezekiah showing the envoys of Babylon all the house of his precious things."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84)]
    for i in range(5):
        x = w * (0.36 + i * 0.12)
        o.append(f'<rect x="{f(x - 20)}" y="{f(b - 30)}" width="40" height="30" fill="{["#E8B830", "#C8C8D0", "#B5652E", "#E8B830", "#8A5A30"][i]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = fit(b, h * 0.42)
    o.append(king_fig(p, w * 0.14, b, s, cloth="#1F3A7A", up=[(22, -158), (50, -150), (80, -150)]))
    for i in range(3): o.append(captain(p, w * (0.66 + i * 0.1), b - 30, s * 0.8, cloth=["#2A4A6A", "#6A2A5A", "#3A5A6A"][i], flip=True, spear=False))
    return "".join(o)

def plumb_line(w, h):
    """The line of Samaria and the plummet of the house of Ahab stretched over Jerusalem (a blueprint)."""
    o = [bp(w, h), title_bar(w, "THE LINE OF SAMARIA · THE PLUMMET OF AHAB")]
    o.append(J.jericho(w * 0.1, w * 0.9, h * 0.5, h * 0.88, 3, towers=4, houses=True).replace("#B5652E", "#3A4A5A").replace("#C8682E", "#4A5A6A"))
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.2)} L {f(w * 0.94)} {f(h * 0.2)}" stroke="{CY}" stroke-width="2" stroke-dasharray="6 4"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.2)} L {f(w * 0.5)} {f(h * 0.44)}" stroke="#FFD23F" stroke-width="2"></path><path d="M{f(w * 0.5 - 10)} {f(h * 0.44)} L {f(w * 0.5 + 10)} {f(h * 0.44)} L {f(w * 0.5)} {f(h * 0.5)} Z" fill="#FFD23F"></path>')
    return "".join(o)

def garden_uzza(w, h, seed):
    """The garden of Uzza, a sepulchre among its trees at dusk."""
    import jos.art as JA
    return JA.cave(w, h, seed, sealed=True, dusk=True)

# ---- 2 Kings 22–23 ------------------------------------------------------------------------------------------------------
def book_found(p, w, h, seed, reading=False):
    """Hilkiah the high priest holding up the book of the law found in the house of Jehovah (reading=True: Shaphan reading it
    before the king, who rends his clothes)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1A"></rect>', V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFD23F", op=0.15),
         ground(w, h, b, "#2A1A10", dy=0)]
    s = fit(b, h * 0.42)
    if reading:
        o.append(king_fig(p, w * 0.24, b, s, cloth="#1F3A7A", up=[(-22, -158), (-40, -120), (-50, -80)]))
        o.append(man(p, w * 0.66, b, s * 0.95, "#5A4A3A", flip=True, up=[(22, -158), (40, -150), (56, -140)]) + S3.letter(w * 0.66 - 70 * s, b - 150 * s, s * 0.6))
    else:
        o.append(priest(p, w * 0.5, b, s, up=[(-22, -158), (-30, -200), (-20, -236)]) + S3.letter(w * 0.5 - 20 * s, b - 250 * s, s * 0.7))
    return "".join(o)

def huldah(p, w, h, seed):
    """Huldah the prophetess in her house in the second quarter of Jerusalem, the king's servants before her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A878"></rect>', ground(w, h, b, "#8A6A4A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(mk.person(p, round(w * 0.22), round(b), round(s, 3), body="#3A1E14", cloth="#2A4A5A", woman=True, hair="#3A3430", sw=3))
    o.append(priest(p, w * 0.54, b, s * 0.95, flip=True))
    for i in range(3): o.append(man(p, w * (0.66 + i * 0.1), b, s * 0.9, ["#5A4A3A", "#3A4A6A", "#6A5A3A"][i], flip=True))
    return "".join(o)

def covenant_pillar(p, w, h, seed):
    """The king standing by the pillar before the house of Jehovah reading the book of the covenant to all the people."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.62, "#C8B88A", dy=0), temple_front(w * 0.5, h * 0.62, w * 0.56, seed)]
    s = fit(b, h * 0.36) * 0.5
    o.append(king_fig(p, w * 0.5, h * 0.8, fit(h * 0.8, h * 0.46), cloth="#1F3A7A", up=[(22, -158), (40, -150), (56, -150)]))
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.36, h * 0.78, b, 8, s * 0.7, s))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.64, w * 0.98, h * 0.78, b, 8, s * 0.7, s, flip=True))
    return "".join(o)

def kidron_fire(w, h, seed):
    """The vessels of Baal and the Asherah burned without Jerusalem at the brook Kidron, the ashes carried away."""
    o = [sky(w, h, "#3A2A3A", "#C8603A"), J.jericho(w * 0.4, w + 10, h * 0.2, h * 0.5, seed, towers=3, houses=True), ground(w, h, h * 0.5, "#5A4A3A", dy=0),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.8)}" stroke="#2C7DA8" stroke-width="12" fill="none"></path>',
         E.blaze(w * 0.3, h * 0.72, w * 0.2, h * 0.3, seed, n=7), f'<path d="M{f(w * 0.24)} {f(h * 0.7)} L {f(w * 0.38)} {f(h * 0.62)}" stroke="#5A3A22" stroke-width="12"></path>']
    return "".join(o)

def bethel_tombs(p, w, h, seed):
    """The altar at Beth-el broken down and the sepulchres in the mount; the monument of the man of God left standing."""
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#E8A06A"), f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(4):
        x = w * (0.14 + i * 0.2); y = h * (0.5 - (i % 2) * 0.04)
        o.append(f'<path d="M{f(x - 22)} {f(y)} C {f(x - 22)} {f(y - 30)} {f(x + 22)} {f(y - 30)} {f(x + 22)} {f(y)} Z" fill="#1A1214" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<rect x="{f(w * 0.76)}" y="{f(h * 0.32)}" width="{f(w * 0.05)}" height="{f(h * 0.18)}" fill="#B8A890" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(S4.stone_heap(w * 0.4, h * 0.9, w * 0.4, h * 0.18, seed) + E.blaze(w * 0.4, h * 0.76, w * 0.1, h * 0.14, seed, n=4))
    o.append(king_fig(p, w * 0.86, h * 0.9, fit(h * 0.9, h * 0.6) * 0.8, cloth="#1F3A7A", flip=True))
    return "".join(o)

def megiddo(p, w, h, seed):
    """Megiddo: the chariot carrying the king back to Jerusalem (23:29–30 told in words only)."""
    return ramoth(p, w, h, seed, dusk=True)

# ---- 2 Kings 24–25 ------------------------------------------------------------------------------------------------------
BABEL_C = "#2A4A6A"
def siege_forts(p, w, h, seed):
    """Jerusalem besieged by the army of Babylon, forts built against it round about."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A5A", "#C8A080"), J.jericho(w * 0.24, w * 0.86, h * 0.24, h * 0.62, seed, towers=4, houses=True), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    for i, x in enumerate((0.08, 0.92)):
        o.append(f'<path d="M{f(w * x - 40)} {f(h * 0.74)} L {f(w * x - 30)} {f(h * 0.5)} L {f(w * x + 30)} {f(h * 0.5)} L {f(w * x + 40)} {f(h * 0.74)} Z" fill="#7A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(N.camp(10, -10, w + 10, h * 0.7, h * 0.8, seed, color=(BABEL_C, "#3A3A5A", "#5A4A3A")))
    s = min(fit(b, h * 0.3), h / 700)
    for i in range(10): o.append(warrior(p, w * (0.04 + i * 0.1), b - (i % 2) * h * 0.03, s * 0.8, BABEL_C))
    return "".join(o)

def burning_city(w, h, seed):
    """The house of Jehovah and every great house of Jerusalem burned with fire, the walls broken down (no one drawn)."""
    o = [sky(w, h, "#2A0A0A", "#8A2A1A"), J.collapse(-10, w * 0.4, h * 0.8, h * 0.36, seed, color="#8A5A3A"), temple_front(w * 0.66, h * 0.8, w * 0.46, seed),
         J.collapse(w * 0.86, w + 10, h * 0.8, h * 0.3, seed + 1, color="#8A5A3A")]
    o += [E.blaze(w * (0.08 + i * 0.16), h * 0.82, w * 0.14, h * 0.4, seed + i, n=7) for i in range(6)]
    for i in range(8): o.append(f'<circle cx="{f(w * (0.1 + i * 0.12))}" cy="{f(h * (0.24 - (i % 3) * 0.06))}" r="{f(w * 0.08)}" fill="#3A2A2E" opacity="0.7"></circle>')
    o.append(ground(w, h, h * 0.84, "#1A0A0A", dy=0))
    return "".join(o)

def brass_carried(p, w, h, seed):
    """The pillars, the sea and the bases broken in pieces, the brass carried away to Babylon on carts."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A2A", "#C8803A"), ground(w, h, h * 0.62, "#6A5A4A", dy=0)]
    for i in range(5):
        x = w * (0.1 + i * 0.18); y = h * (0.72 + (i % 2) * 0.06)
        o.append(f'<path d="M{f(x)} {f(y)} l 30 -14 l 20 18 l -26 10 Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(S1.cart(w * 0.5, b, min(1.0, h / 360), load=f'<path d="M-60 -80 l 40 -30 l 50 10 l 20 20 Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></path>'))
    s = fit(b, h * 0.36)
    for i in range(3): o.append(warrior(p, w * (0.76 + i * 0.08), b, s * 0.8, BABEL_C, flip=True))
    return "".join(o)

def mizpah(p, w, h, seed):
    """Mizpah: the captains of the forces come to Gedaliah the governor."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.76, h * 0.5, w * 0.36, h * 0.26, seed), ground(w, h, h * 0.52, "#A89A6A", dy=0)]
    s = fit(b, h * 0.38)
    o.append(man(p, w * 0.2, b, s, "#5A4A3A", extra=A.headcloth("#5A4A3A") + A.BLACK_BEARD))
    for i in range(4): o.append(captain(p, w * (0.44 + i * 0.12), b, s * 0.9, cloth=WAR[i % 4], flip=True))
    return "".join(o)

def prison_garments(p, w, h, seed):
    """Jehoiachin's prison garments changed; he eats bread before the king of Babylon continually."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.table(w * 0.5, b, w * 0.56, min(1.2, h / 300))]
    s = fit(b, h * 0.4)
    o.append(king_fig(p, w * 0.16, b, s, cloth=BABEL_C) + king_fig(p, w * 0.84, b, s * 0.95, cloth="#E8E2D6", flip=True))
    return "".join(o)
