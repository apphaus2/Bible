"""Drawings for the Job volume (chapter by chapter, added below), on top of everything in chr2.art (which carries chr1.art,
kg2.art, kg1.art, and 2 Samuel's drawings as K2).

The cast at a distance: Job in white with a white headcloth and a gold band (job_fig), afflicted in sackcloth (ash=True);
his wife in dark teal; Eliphaz teal, Bildad slate-purple, Zophar deep blue, Elihu green (friend_fig). seated() is a figure
sitting on the ground, knees drawn up (Job on the ash heap with his potsherd, the friends seven days silent). God is never
drawn; Satan is never drawn (heavens(..., shadow=True) at most lets a dark streak fall from the court toward the earth)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
import kg1.art as K1
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import man, woman, sun, flock
from exo import art as A
import joshua1 as J, judges1 as J1, numbers1 as N, samuel1 as S1, samuel4 as S4, exodus as E, exodus2 as E2, exodus3 as E3, exodus5 as V

INK = "#0D0D0F"
JOB_C, SACK, WIFE_C = "#ECE6D8", "#5A5248", "#2A4A4A"
FRIEND_C = {"eli": "#1F5A5A", "bil": "#4A3A6A", "zop": "#1F3F7A", "elihu": "#2A5A3A"}
GREY_BEARD = A.WHITE_BEARD.replace("#E8E2D6", "#B8B2A8")
BEARD = {"eli": A.WHITE_BEARD, "bil": A.WHITE_BEARD.replace("#E8E2D6", "#8A847A"), "zop": A.BLACK_BEARD, "elihu": ""}
BAND = '<path d="M-14 -194 C -6 -198 6 -198 14 -194" fill="none" stroke="#E8B830" stroke-width="3.4"></path>'

def P(d, fill, sw=2.4, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"{extra}></path>'

def rect(w, h, c):
    return f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{c}"></rect>'

# ---- the cast at a distance ---------------------------------------------------------------------------------------------
def job_fig(p, x, y, s, flip=False, up=None, ash=False):
    """Job at a distance: a white robe and headcloth with a gold band, grey beard; ash=True: sackcloth, a sackcloth hood."""
    if ash:
        return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SACK, sw=3, flip=flip, up=up, extra=A.headcloth(SACK, cord=None) + GREY_BEARD)
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JOB_C, sw=3, flip=flip, up=up, extra=A.headcloth("#F3EFE6", cord=None) + BAND + GREY_BEARD)

def friend_fig(p, x, y, s, who, flip=False, up=None):
    c = FRIEND_C[who]
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=c, kind="Tunic" if who == "elihu" else "Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(c, cord="#E8B830" if who in ("eli", "elihu") else "#2A1A10") + BEARD[who])

def wife_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=WIFE_C, woman=True, hair="#3A2A1E", sw=3, flip=flip, up=up)

def seated(x, y, s, cloth, head=None, beard="#B8B2A8", flip=False, shard=False, ash=False, band=False, bowed=False):
    """A man sitting on the ground, knees drawn up, facing right; (x, y) = the ground under him (about 135 units tall)."""
    sx = -s if flip else s
    hx, hy = (-4, -112) if not bowed else (6, -104)
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">',
         P("M-48 0 C -52 -34 -44 -72 -30 -94 C -22 -104 -2 -104 6 -96 C 14 -84 16 -72 22 -62 L 44 -60 C 54 -56 56 -42 56 -26 L 60 0 Z", cloth, 2.6),
         f'<path d="M-30 -60 C -24 -40 -20 -20 -22 0 M10 -60 C 24 -46 34 -30 40 -8" fill="none" stroke="#0D0D0F" stroke-width="1.4" opacity="0.5"></path>',
         P("M54 0 L 72 0 C 72 -6 66 -9 58 -9 Z", SKIN, 1.8),
         f'<circle cx="{hx}" cy="{hy}" r="16" fill="{SKIN}" stroke="{INK}" stroke-width="2.2"></circle>']
    if head:
        o.append(P(f"M{hx - 18} {hy - 2} C {hx - 20} {hy - 26} {hx + 14} {hy - 30} {hx + 16} {hy - 8} L {hx + 10} {hy - 6} L {hx - 4} {hy - 12} L {hx - 16} {hy - 4} L {hx - 26} {hy + 22} Z", head, 2))
        if band: o.append(f'<path d="M{hx - 16} {hy - 14} C {hx - 8} {hy - 20} {hx + 6} {hy - 20} {hx + 14} {hy - 14}" fill="none" stroke="#E8B830" stroke-width="3"></path>')
    if beard:
        o.append(P(f"M{hx + 8} {hy + 6} C {hx + 16} {hy + 14} {hx + 14} {hy + 26} {hx + 4} {hy + 30} C {hx - 2} {hy + 22} {hx} {hy + 12} {hx + 2} {hy + 8} Z", beard, 1.6))
    if shard:
        o.append('<path d="M-8 -90 L 14 -78 L 16 -100" fill="none" stroke="#0D0D0F" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"></path>'
                 f'<path d="M-8 -90 L 14 -78 L 16 -100" fill="none" stroke="{cloth}" stroke-width="9.5" stroke-linecap="round" stroke-linejoin="round"></path>'
                 '<path d="M12 -104 L 26 -112 L 22 -96 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    else:
        o.append('<path d="M-8 -90 L 10 -66 L 38 -62" fill="none" stroke="#0D0D0F" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"></path>'
                 f'<path d="M-8 -90 L 10 -66 L 38 -62" fill="none" stroke="{cloth}" stroke-width="9.5" stroke-linecap="round" stroke-linejoin="round"></path>')
    if ash:
        r = random.Random(int(x))
        o.append('<g fill="#B8B4AE" opacity="0.85">' + "".join(f'<circle cx="{f(hx + r.uniform(-16, 12))}" cy="{f(hy + r.uniform(-22, -6))}" r="{f(r.uniform(1.2, 2.6))}"></circle>' for _ in range(12))
                 + "".join(f'<circle cx="{f(r.uniform(-40, 50))}" cy="{f(r.uniform(-90, -10))}" r="{f(r.uniform(1, 2.2))}"></circle>' for _ in range(14)) + '</g>')
    return "".join(o) + "</g>"

def seated_job(x, y, s, flip=False, shard=True):
    return seated(x, y, s, SACK, head=SACK, flip=flip, shard=shard, ash=True)

def seated_friend(x, y, s, who, flip=False, bowed=True):
    b = {"eli": "#E8E2D6", "bil": "#8A847A", "zop": "#2A1A10", "elihu": None}[who]
    return seated(x, y, s, FRIEND_C[who], head=FRIEND_C[who], beard=b, flip=flip, band=who == "eli", bowed=bowed, ash=True)

# ---- shared scenery -----------------------------------------------------------------------------------------------------
def clouds(w, y, seed, n=6, color="#E8E2D6", op=0.9, ry=0.06, h=None):
    r = random.Random(seed); h = h or w
    return "".join(f'<ellipse cx="{f(r.uniform(-0.1, 1.1) * w)}" cy="{f(y + r.uniform(-12, 12))}" rx="{f(w * r.uniform(0.12, 0.26))}" ry="{f(h * ry * r.uniform(0.7, 1.2))}" fill="{color}" opacity="{op}"></ellipse>' for _ in range(n))

def tents(x, base, s, n=3, color="#3A2A22", seed=1):
    """A few goat-hair tents of the household."""
    return "".join(A.black_tent(x + i * 120 * s, base - (i % 2) * 6 * s, 150 * s * (1 - 0.1 * (i % 2)), 70 * s, color=color) for i in range(n))

def house(x, base, w, h, lit=False, color="#C8A878"):
    """A flat-roofed stone house with a door and two windows."""
    win = "#FFC14D" if lit else "#2A1A14"
    return (P(f"M{f(x)} {f(base)} L {f(x)} {f(base - h)} L {f(x + w)} {f(base - h)} L {f(x + w)} {f(base)} Z", color)
            + P(f"M{f(x - 6)} {f(base - h)} L {f(x + w + 6)} {f(base - h)} L {f(x + w + 6)} {f(base - h - 8)} L {f(x - 6)} {f(base - h - 8)} Z", "#8A6A4A", 2)
            + P(f"M{f(x + w * 0.42)} {f(base)} L {f(x + w * 0.42)} {f(base - h * 0.5)} L {f(x + w * 0.58)} {f(base - h * 0.5)} L {f(x + w * 0.58)} {f(base)} Z", "#3A2214", 2)
            + "".join(P(f"M{f(x + w * k)} {f(base - h * 0.78)} l {f(w * 0.1)} 0 l 0 {f(h * 0.16)} l {f(-w * 0.1)} 0 Z", win, 1.8) for k in (0.14, 0.76)))

def ash_mound(cx, base, w, h, seed):
    """The heap of ashes outside the city: a grey mound, charred sticks and potsherds, a thin smoke."""
    r = random.Random(seed)
    o = [P(f"M{f(cx - w / 2)} {f(base)} C {f(cx - w * 0.3)} {f(base - h)} {f(cx + w * 0.3)} {f(base - h)} {f(cx + w / 2)} {f(base)} Z", "#8A8680", 2.4)]
    o.append('<g fill="#5A5650">' + "".join(f'<circle cx="{f(cx + r.uniform(-0.4, 0.4) * w)}" cy="{f(base - r.uniform(0.05, 0.6) * h)}" r="{f(r.uniform(1.5, 3.5))}"></circle>' for _ in range(40)) + '</g>')
    for i in range(6):
        x = cx + r.uniform(-0.38, 0.38) * w; y = base - r.uniform(0.05, 0.3) * h
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-18, 18))} {f(r.uniform(-6, 6))}" stroke="#2A2220" stroke-width="4" stroke-linecap="round"></path>')
    for i in range(5):
        x = cx + r.uniform(-0.4, 0.4) * w; y = base - r.uniform(0.02, 0.25) * h
        o.append(P(f"M{f(x)} {f(y)} l 10 -6 l 6 8 Z", "#B5652E", 1.4))
    return "".join(o)

def smoke(x, y, n, seed, color="#A8A29A", op=0.5, k=1.0):
    r = random.Random(seed)
    return "".join(f'<circle cx="{f(x + i * 6 * k + r.uniform(-8, 8) * k)}" cy="{f(y - i * 22 * k)}" r="{f((10 + i * 4) * k)}" fill="{color}" opacity="{max(0.05, op - i * 0.04):.2f}"></circle>' for i in range(n))

# ---- Job 1–3 ------------------------------------------------------------------------------------------------------------
def uz_estate(p, w, h, seed):
    """A man in the land of Uz: his tents and house on the plain at morning, Job in white with his staff, flocks of sheep,
    camels, yoked oxen and she-asses spread to the hills."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.84, h * 0.2, min(22, h * 0.06), op=0.3),
         hills(w, h, h * 0.5, seed, "#B89A6A", amp=12, step=80), ground(w, h, h * 0.58, "#D8C08A", dy=0),
         tents(w * 0.06, h * 0.64, min(1.0, h / 400), 2), house(w * 0.36, h * 0.64, w * 0.12, h * 0.12)]
    o.append(flock(w * 0.5, w * 0.98, h * 0.6, h * 0.74, 18, seed, cows=0.0, smin=0.12, smax=0.22))
    for i in range(4): o.append(J1.camel(w * (0.56 + i * 0.1), h * 0.86 - (i % 2) * 6, min(0.36, h / 900), color=["#B5844A", "#C99A5A"][i % 2]))
    for i in range(3): o.append(S1.cow(w * (0.08 + i * 0.1), h * 0.8, min(0.3, h / 1000), color=["#8A5A30", "#C9A27A", "#5A3A22"][i]))
    for i in range(2): o.append(N.ass(w * (0.3 + i * 0.08), h * 0.9, min(0.26, h / 1100), color="#8A8478"))
    s = fit(b, max(h * 0.5, b - 200))
    o.append(mk.person(p, round(w * 0.46), round(b), s, body=SKIN, cloth=JOB_C, sw=3,
                       extra=A.headcloth("#F3EFE6", cord=None) + BAND + GREY_BEARD + '<path d="M-50 -170 L -46 6" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'))
    return "".join(o)

def feast_house(p, w, h, seed, fallen=False):
    """His sons held a feast in the house of each one upon his day: the house open at evening, a lamp, a long table, seven
    sons and three daughters behind it with their cups."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A4A", "#E89A5A"), ground(w, h, h * 0.9, "#6A4A3A", dy=0),
         P(f"M{f(w * 0.04)} {f(b)} L {f(w * 0.04)} {f(h * 0.16)} L {f(w * 0.96)} {f(h * 0.16)} L {f(w * 0.96)} {f(b)} Z", "#E8C890", 2.6),
         P(f"M{f(w * 0.0)} {f(h * 0.16)} L {f(w * 1.0)} {f(h * 0.16)} L {f(w * 1.0)} {f(h * 0.08)} L {f(w * 0.0)} {f(h * 0.08)} Z", "#8A5A30", 2.4),
         f'<rect x="{f(w * 0.08)}" y="{f(h * 0.2)}" width="{f(w * 0.84)}" height="{f(b - h * 0.2)}" fill="#5A3A2A"></rect>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.3)}" r="{f(h * 0.2)}" fill="#FFC14D" opacity="0.25"></circle>']
    o.append(P(f"M{f(w * 0.5 - 14)} {f(h * 0.3)} C {f(w * 0.5 - 14)} {f(h * 0.34)} {f(w * 0.5 + 14)} {f(h * 0.34)} {f(w * 0.5 + 14)} {f(h * 0.3)} Z", "#B5652E", 1.8)
             + E.flame(w * 0.5 + 12, h * 0.3, 8, 18, 0.1))
    s = fit(b, max(h * 0.36, b - 200)) * 0.9
    cl = ["#7A2A3A", "#2C4A7A", "#5A6A2A", "#7A5A2A", "#3A5A6A", "#6A3A5A", "#4A3A2A"]
    xs = [0.14 + i * 0.072 for i in range(10)]
    for i, x in enumerate(xs):
        if i in (2, 5, 8): o.append(woman(p, w * x, b, s * 0.92, ["#C8506A", "#D8A040", "#8A5AB8"][(i - 2) // 3]))
        else: o.append(man(p, w * x, b, s, cl[len([j for j in range(i) if j not in (2, 5, 8)]) % 7]))
    ty = b - 200 * s * 0.42
    o.append(P(f"M{f(w * 0.1)} {f(ty)} L {f(w * 0.9)} {f(ty)} L {f(w * 0.9)} {f(ty + 14)} L {f(w * 0.1)} {f(ty + 14)} Z", "#8A5A30", 2.2)
             + P(f"M{f(w * 0.14)} {f(ty + 14)} L {f(w * 0.14)} {f(b)} M{f(w * 0.86)} {f(ty + 14)} L {f(w * 0.86)} {f(b)}", "none", 6))
    for i in range(9):
        x = w * (0.16 + i * 0.085)
        o.append(P(f"M{f(x - 6)} {f(ty)} L {f(x - 4)} {f(ty - 12)} L {f(x + 4)} {f(ty - 12)} L {f(x + 6)} {f(ty)} Z", "#E8B830", 1.4) if i % 2 else
                 f'<ellipse cx="{f(x)}" cy="{f(ty - 4)}" rx="12" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def dawn_offering(p, w, h, seed):
    """Job rose up early in the morning and offered burnt-offerings according to the number of them all: the altar's
    smoke going up in the dawn, Job with his hands raised, ten lambs' fleeces laid by."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A6A", "#FFB07A"), sun(w * 0.8, h * 0.66, min(26, h * 0.07), color="#FFD23F", op=0.35),
         hills(w, h, h * 0.66, seed, "#4A3A4A", amp=10, step=90), ground(w, h, h * 0.74, "#8A6A4A", dy=0),
         smoke(w * 0.42, h * 0.66, 9, seed, color="#E8E2D6", op=0.55, k=min(1.4, h / 300)), S4.altar(w * 0.42, b - 4, min(1.2, h / 330), fire=True, seed=seed)]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(mk.person(p, round(w * 0.66), round(b), s, body=SKIN, cloth=JOB_C, sw=3, flip=True, up=[(22, -158), (40, -190), (52, -224)],
                       extra=A.headcloth("#F3EFE6", cord=None) + BAND + GREY_BEARD))
    for i in range(10): o.append(E.sheep(w * (0.06 + (i % 5) * 0.05), b - (i // 5) * 16 * s, s * 0.32))
    return "".join(o)

def heavens(w, h, seed, shadow=False, earth=True):
    """The day the sons of God came to present themselves before Jehovah: a radiant light above the clouds (no one drawn in
    it), the host as tall shapes of light in a ring, the earth far below; shadow=True: a dark streak among them falling away
    toward the earth (Satan is never drawn)."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0B0B2A", "#5B2470"), mk.stars(50, w, h * 0.5, seed, color="#C8C0E8"),
         V.rays(w * 0.5, -h * 0.05, 36, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.22),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(-h * 0.02)}" rx="{f(w * 0.3)}" ry="{f(h * 0.22)}" fill="#FFF4C2" opacity="0.55"></ellipse>',
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(-h * 0.04)}" rx="{f(w * 0.14)}" ry="{f(h * 0.12)}" fill="#FFFFFF" opacity="0.8"></ellipse>']
    for i in range(18):
        a = math.pi * (0.08 + 0.84 * i / 17)
        x = w * 0.5 - math.cos(a) * w * 0.46; y = h * 0.16 + math.sin(a) * h * 0.34
        hh = h * 0.16 * (0.7 + 0.3 * math.sin(a))
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - hh * 0.14)} {f(y + hh * 0.4)} {f(x - hh * 0.14)} {f(y + hh * 0.8)} {f(x - hh * 0.1)} {f(y + hh)} L {f(x + hh * 0.1)} {f(y + hh)} C {f(x + hh * 0.14)} {f(y + hh * 0.8)} {f(x + hh * 0.14)} {f(y + hh * 0.4)} {f(x)} {f(y)} Z" fill="#FFF4C2" opacity="0.7"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y - hh * 0.06)}" r="{f(hh * 0.09)}" fill="#FFFFFF" opacity="0.8"></circle>')
    o.append(clouds(w, h * 0.66, seed, 8, color="#C8B8E8", op=0.55, ry=0.05, h=h))
    if earth:
        o.append(f'<path d="M-10 {f(h * 0.92)} Q {f(w * 0.5)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.92)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A2A3A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M-10 {f(h * 0.92)} Q {f(w * 0.5)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.92)}" fill="none" stroke="#5A8AB8" stroke-width="3" opacity="0.7"></path>')
    if shadow:
        x0, y0 = w * 0.78, h * 0.42
        o.append(f'<path d="M{f(x0)} {f(y0)} C {f(x0 + w * 0.04)} {f(y0 + h * 0.2)} {f(x0 - w * 0.02)} {f(y0 + h * 0.36)} {f(x0 + w * 0.06)} {f(h * 0.9)} '
                 f'L {f(x0 + w * 0.1)} {f(h * 0.9)} C {f(x0 + w * 0.06)} {f(y0 + h * 0.36)} {f(x0 + w * 0.08)} {f(y0 + h * 0.2)} {f(x0 + w * 0.02)} {f(y0)} Z" fill="#05050F" opacity="0.75"></path>')
    return "".join(o)

def hedge(p, w, h, seed):
    """Hast not thou made a hedge about him: Job's house, tents and flocks at evening ringed about by a hedge, a line of
    gold light upon it."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A5A", "#E8A06A"), hills(w, h, h * 0.52, seed, "#5A4A4A", amp=10, step=90), ground(w, h, h * 0.6, "#8A7A4A", dy=0)]
    cx, cy, rx, ry = w * 0.5, h * 0.78, w * 0.44, h * 0.16
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#A8984A" stroke="none"></ellipse>')
    o.append(tents(cx - rx * 0.6, cy - ry * 0.2, min(0.7, h / 500), 2) + house(cx + rx * 0.1, cy - ry * 0.1, w * 0.1, h * 0.1, lit=True))
    o.append(flock(cx - rx * 0.6, cx + rx * 0.7, cy, cy + ry * 0.7, 12, seed, cows=0.3, smin=0.1, smax=0.18))
    r = random.Random(seed)
    for i in range(70):
        a = 2 * math.pi * i / 70
        x = cx + math.cos(a) * rx; y = cy + math.sin(a) * ry
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(7, 12))}" fill="#2E4A2A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy - 8)}" rx="{f(rx + 4)}" ry="{f(ry + 4)}" fill="none" stroke="#FFD23F" stroke-width="3" opacity="0.8"></ellipse>')
    return "".join(o)

def runner_scene(p, w, h, seed, kind="plow"):
    """A messenger running to Job, and behind him what he left: kind 'plow' (the plow and the yoke in the field, the
    Sabeans' dust far off), 'fire' (the pasture burnt, fire falling from a dark sky, smoke), 'bands' (three trails of dust
    going away, camels in them), 'wind' (the house fallen, the whirling dust of the wilderness). No one slain is drawn."""
    r = random.Random(seed); b = h * 0.94
    if kind == "plow":
        o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, "#B89A6A", amp=10, step=90), ground(w, h, h * 0.56, "#C8A06A", dy=0)]
        for i in range(8): o.append(f'<path d="M{f(-10)} {f(h * (0.6 + i * 0.05))} L {f(w + 10)} {f(h * (0.58 + i * 0.05))}" stroke="#8A6A3A" stroke-width="2.4"></path>')
        o.append(P(f"M{f(w * 0.36)} {f(h * 0.82)} l 70 -6 l 30 -30 l 6 4 l -26 34 l 10 16 l -8 4 l -14 -14 l -70 6 Z", "#8A5A30", 2))
        o.append(P(f"M{f(w * 0.2)} {f(h * 0.78)} l 80 -4 l 0 8 l -80 4 Z", "#5A3A1E", 2))
        for i in range(5): o.append(f'<ellipse cx="{f(w * (0.62 + i * 0.05))}" cy="{f(h * 0.5 - i * 4)}" rx="{f(w * 0.06)}" ry="{f(h * 0.05)}" fill="#C8A87A" opacity="0.7"></ellipse>')
    elif kind == "fire":
        o = [K2.sky(w, h, "#1A0A0A", "#8A2A1A"), hills(w, h, h * 0.52, seed, "#2A1A1A", amp=14, step=80), ground(w, h, h * 0.6, "#3A2A22", dy=0)]
        for i in range(4): o.append(E2.bolt(w * (0.2 + i * 0.2), 0, h * 0.5, seed + i, w=1.2))
        for i in range(6): o.append(E.blaze(w * (0.06 + i * 0.17), h * 0.62, w * 0.12, h * 0.12, seed + i, n=5))
        o.append(smoke(w * 0.5, h * 0.5, 8, seed, color="#3A3030", op=0.6, k=min(1.6, h / 250)))
    elif kind == "bands":
        o = [K2.sky(w, h, "#C8A87A", "#F3D8A0"), ground(w, h, h * 0.52, "#D8B87A", dy=0)]
        for i, x in enumerate((0.2, 0.5, 0.8)):
            o.append(f'<path d="M{f(w * x - 10)} {f(h * 0.52)} C {f(w * x - 30)} {f(h * 0.4)} {f(w * x + 20)} {f(h * 0.3)} {f(w * x)} {f(h * 0.14)} L {f(w * x + 40)} {f(h * 0.14)} C {f(w * x + 50)} {f(h * 0.3)} {f(w * x + 30)} {f(h * 0.42)} {f(w * x + 30)} {f(h * 0.52)} Z" fill="#B89A6A" opacity="0.7"></path>')
            for k in range(3): o.append(J1.camel(w * x + k * 16, h * 0.53, min(0.1, h / 3000), color="#5A3A22"))
        for i in range(7):                                 # the camels' pen, empty
            x = w * (0.06 + i * 0.06)
            o.append(f'<path d="M{f(x)} {f(h * 0.94)} L {f(x)} {f(h * 0.8)}" stroke="#5A3A1E" stroke-width="5" stroke-linecap="round"></path>')
        o.append(f'<path d="M{f(w * 0.05)} {f(h * 0.84)} L {f(w * 0.43)} {f(h * 0.84)} M{f(w * 0.05)} {f(h * 0.9)} L {f(w * 0.43)} {f(h * 0.9)}" stroke="#5A3A1E" stroke-width="4"></path>')
    else:
        o = [K2.sky(w, h, "#5A5A4A", "#C8B890"), ground(w, h, h * 0.64, "#8A7A5A", dy=0)]
        x0, y0 = w * 0.3, h * 0.64
        o.append(P(f"M{f(x0)} {f(y0)} L {f(x0 + 10)} {f(y0 - h * 0.14)} L {f(x0 + 30)} {f(y0 - h * 0.08)} L {f(x0 + w * 0.12)} {f(y0 - h * 0.12)} L {f(x0 + w * 0.18)} {f(y0 - h * 0.04)} L {f(x0 + w * 0.3)} {f(y0 - h * 0.1)} L {f(x0 + w * 0.32)} {f(y0)} Z", "#A8906A", 2.4))
        o.append(S4.stone_heap(x0 + w * 0.16, y0 + 6, w * 0.4, h * 0.08, seed))
        for i in range(5): o.append(P(f"M{f(x0 + w * (0.02 + i * 0.07))} {f(y0 - 4)} l {f(r.uniform(20, 50))} {f(r.uniform(-30, -10))}", "none", 5))
        for i in range(10):
            yy = h * (0.08 + i * 0.05)
            o.append(f'<path d="M{f(w * 0.98 - i * 6)} {f(yy)} C {f(w * 0.7)} {f(yy - 20)} {f(w * 0.5)} {f(yy + 20)} {f(w * 0.2 - i * 10)} {f(yy + 6)}" fill="none" stroke="#E8DCC0" stroke-width="{3 + i % 3}" opacity="0.6"></path>')
    s = fit(b, max(h * 0.7, b - 190))
    o.insert(0, mk.defs(p, *ALL))
    o.append(S4.runner(p, w * 0.82, b, s, flip=True, cloth="#C8B8A0"))
    return "".join(o)

def job_mourn(p, w, h, seed):
    """Job arose, and rent his robe, and shaved his head, and fell down upon the ground, and worshipped: his tent door at
    dusk, Job fallen on his face in his rent white robe, the shorn grey hair on the ground."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A5A", "#C88A6A"), ground(w, h, h * 0.66, "#6A5A4A", dy=0),
         A.black_tent(w * 0.22, h * 0.68, w * 0.4, h * 0.3, color="#2A2230")]
    s = min(1.6, h / 220)
    o.append(N.prostrate(w * 0.5, b, s, color=JOB_C, skin="#3A1E14"))
    o.append(f'<path d="M{f(w * 0.5)} {f(b - 22 * s)} l {f(10 * s)} {f(14 * s)} l {f(-6 * s)} {f(4 * s)} l {f(12 * s)} {f(8 * s)}" fill="none" stroke="#0D0D0F" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(8):
        x = w * 0.5 + 80 * s + r.uniform(-14, 30) * s; y = b - r.uniform(0, 6)
        o.append(f'<path d="M{f(x)} {f(y)} c 4 -6 10 -6 14 0" fill="none" stroke="#B8B2A8" stroke-width="2.4"></path>')
    return "".join(o)

def ash_heap(p, w, h, seed, wife=False, friends=0, night=False, shard=True):
    """Job sat among the ashes, scraping himself with a potsherd: the ash heap outside the city, the walls far off; wife=True:
    his wife standing over him; friends=3: the three sitting with him on the ground; night=True: under the stars."""
    b = h * 0.97
    sk = K2.sky(w, h, "#0B0B2A", "#2A2A5A") + mk.stars(70, w, h * 0.5, seed) + J.moon(w * 0.84, h * 0.14, min(18, h * 0.05)) if night else K2.sky(w, h, "#6A6A7A", "#D8C8B0")
    o = [mk.defs(p, *ALL), sk, J.city_hill(w * 0.82, h * 0.6, w * 0.3, h * 0.16, seed), ground(w, h, h * 0.6, "#5A5248" if night else "#9A8A72", dy=0),
         ash_mound(w * 0.42, b, w * 0.6, h * 0.13, seed)]
    s = min(1.2, (h * 0.26) / 140)
    o.append(seated_job(w * 0.4, b - h * 0.1, s, shard=shard))
    if wife:
        o.append(wife_fig(p, w * 0.72, b, fit(b, max(h * 0.66, b - 220)), flip=True))
    if friends:
        k = s * 0.85
        o.append(seated_friend(w * 0.12, b + 2, k, "eli") + seated_friend(w * 0.74, b + 4, k, "bil", flip=True) + seated_friend(w * 0.92, b - 4, k * 0.9, "zop", flip=True))
    if night:
        o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A" opacity="0.25"></rect>')
    return "".join(o)

def friends_road(p, w, h, seed, mourn=False):
    """Eliphaz, Bildad and Zophar coming every one from his own place; mourn=True: lifting up their voice, their robes
    rent, dust sprinkled upon their heads toward heaven."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#A8B8C8", "#F3D8A0"), hills(w, h, h * 0.54, seed, "#A88A6A", amp=12, step=90), ground(w, h, h * 0.62, "#C8A87A", dy=0),
         P(f"M{f(w * 0.4)} {f(h * 0.62)} L {f(w * 0.56)} {f(h * 0.62)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z", "#D8C098", 1.6)]
    s = fit(b, max(h * 0.7, b - 210))
    r = random.Random(seed)
    for i, who in enumerate(("eli", "bil", "zop")):
        x = w * (0.32 + i * 0.18)
        up = [(-22, -158), (-40, -200), (-48, -236)] if mourn else None
        o.append(friend_fig(p, x, b - (i % 2) * 8, s, who, up=up))
        if mourn:
            o.append('<g fill="#8A6A4A">' + "".join(f'<circle cx="{f(x + r.uniform(-50, 30) * s)}" cy="{f(b - r.uniform(200, 280) * s)}" r="{f(r.uniform(1.5, 3.5) * s)}"></circle>' for _ in range(26)) + '</g>')
            o.append(f'<path d="M{f(x - 6 * s)} {f(b - 120 * s)} l {f(8 * s)} {f(16 * s)} l {f(-6 * s)} {f(10 * s)} l {f(8 * s)} {f(14 * s)}" fill="none" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if not mourn:
        o.append(job_fig(p, w * 0.08, h * 0.66, s * 0.3, ash=True))
    return "".join(o)

def dark_day(w, h, seed):
    """Let that day be darkness: a pale sun smothered by black cloud, the land below in shadow."""
    o = [K2.sky(w, h, "#1A1A2A", "#4A4A5A"), sun(w * 0.6, h * 0.3, min(30, h * 0.08), color="#C8C0A0", glow="#5A5A6A", op=0.2),
         clouds(w, h * 0.3, seed, 9, color="#0D0D18", op=0.85, ry=0.08, h=h), clouds(w, h * 0.16, seed + 1, 6, color="#1A1A28", op=0.9, ry=0.07, h=h),
         hills(w, h, h * 0.78, seed, "#0D0D14", amp=14, step=70)]
    return "".join(o)

def barren_night(w, h, seed):
    """Let the stars of the twilight thereof be dark; let it look for light, but have none: a starless night, a thin cold line
    where the morning should open its eyelids."""
    o = [K2.sky(w, h, "#05050A", "#14142A"), f'<path d="M-10 {f(h * 0.8)} Q {f(w * 0.5)} {f(h * 0.77)} {f(w + 10)} {f(h * 0.8)}" fill="none" stroke="#5A6A8A" stroke-width="2" opacity="0.6"></path>',
         hills(w, h, h * 0.8, seed, "#05050A", amp=10, step=90), mk.stars(12, w, h * 0.5, seed, color="#3A3A5A")]
    return "".join(o)

def kings_rest(w, h, seed):
    """With kings and counsellors of the earth, who built up waste places for themselves: tombs of kings among ruins in the
    desert at dusk, a crown half in the sand; there the weary are at rest."""
    o = [K2.sky(w, h, "#2A2A4A", "#E8A06A"), mk.stars(20, w, h * 0.3, seed), ground(w, h, h * 0.7, "#B8905A", dy=0)]
    for i, (x, hh) in enumerate(((0.12, 0.26), (0.3, 0.36), (0.72, 0.3))):
        o.append(P(f"M{f(w * x - w * 0.08)} {f(h * 0.72)} L {f(w * x)} {f(h * (0.72 - hh))} L {f(w * x + w * 0.08)} {f(h * 0.72)} Z", ["#A8805A", "#C89A6A", "#98704A"][i]))
    for i in range(4):
        x = w * (0.46 + i * 0.05); hh = h * (0.16 - (i % 2) * 0.06)
        o.append(P(f"M{f(x)} {f(h * 0.74)} L {f(x)} {f(h * 0.74 - hh)} L {f(x + 18)} {f(h * 0.74 - hh - 4)} L {f(x + 18)} {f(h * 0.74)} Z", "#D8C098", 2))
    o.append(f'<g transform="translate({f(w * 0.86)} {f(h * 0.86)}) scale({f(min(1.4, h / 250))})">' + P("M-14 0 L -14 -14 L -7 -6 L 0 -18 L 7 -6 L 14 -14 L 14 0 Z", "#E8B830", 1.6) + '</g>')
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.4)} {f(h * 0.82)} {f(w * 0.7)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def prison_open(w, h, seed):
    """There the prisoners are at ease together: a prison door standing open on the dawn, the fetters broken on the floor."""
    o = [rect(w, h, "#3A3438")]
    for k in range(9):
        for i in range(7):
            o.append(f'<rect x="{f(i * w / 6 - (k % 2) * w / 12)}" y="{f(k * h / 8)}" width="{f(w / 6)}" height="{f(h / 8)}" fill="#4A4448" stroke="#2A2428" stroke-width="2"></rect>')
    dx, dw, dh = w * 0.38, w * 0.22, h * 0.7
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.94 - dh)}" width="{f(dw)}" height="{f(dh)}" fill="#FFD8A0" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             + V.rays(dx + dw / 2, h * 0.94 - dh * 0.4, 14, 10, dh, color="#FFF4C2", op=0.25)
             + P(f"M{f(dx + dw)} {f(h * 0.94 - dh)} L {f(dx + dw * 1.5)} {f(h * 0.94 - dh * 1.06)} L {f(dx + dw * 1.5)} {f(h * 0.98)} L {f(dx + dw)} {f(h * 0.94)} Z", "#5A3A22", 2.4))
    o.append(f'<rect x="-10" y="{f(h * 0.94)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#2A2428"></rect>')
    for i in range(2):
        x = w * (0.18 + i * 0.6)
        o.append(f'<g fill="none" stroke="#8A8A9A" stroke-width="4">' + "".join(f'<ellipse cx="{f(x + k * 14)}" cy="{f(h * 0.95)}" rx="8" ry="5"></ellipse>' for k in range(4)) + '</g>'
                 + f'<path d="M{f(x + 60)} {f(h * 0.94)} a 14 10 0 1 1 20 0" fill="none" stroke="#8A8A9A" stroke-width="5"></path>')
    return "".join(o)

def dug_pit(w, h, seed):
    """Who dig for it more than for hid treasures, and are glad when they can find the grave: a pit dug in the dry ground at
    dusk, the spade standing in the heap, a broken jar of treasure cast aside."""
    o = [K2.sky(w, h, "#3A2A4A", "#E8906A"), ground(w, h, h * 0.62, "#8A6A4A", dy=0),
         f'<ellipse cx="{f(w * 0.46)}" cy="{f(h * 0.8)}" rx="{f(w * 0.2)}" ry="{f(h * 0.08)}" fill="#1A1210" stroke="#0D0D0F" stroke-width="2.4"></ellipse>',
         P(f"M{f(w * 0.7)} {f(h * 0.84)} C {f(w * 0.74)} {f(h * 0.64)} {f(w * 0.86)} {f(h * 0.64)} {f(w * 0.92)} {f(h * 0.84)} Z", "#A8805A"),
         f'<path d="M{f(w * 0.8)} {f(h * 0.7)} L {f(w * 0.84)} {f(h * 0.36)}" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>',
         P(f"M{f(w * 0.78)} {f(h * 0.7)} L {f(w * 0.82)} {f(h * 0.7)} L {f(w * 0.81)} {f(h * 0.78)} L {f(w * 0.77)} {f(h * 0.76)} Z", "#8A8A9A", 2),
         P(f"M{f(w * 0.14)} {f(h * 0.86)} C {f(w * 0.1)} {f(h * 0.78)} {f(w * 0.14)} {f(h * 0.72)} {f(w * 0.2)} {f(h * 0.74)} L {f(w * 0.24)} {f(h * 0.86)} Z", "#B5652E", 2)]
    o.append('<g fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2">' + "".join(f'<circle cx="{f(w * (0.24 + k * 0.025))}" cy="{f(h * 0.87 - (k % 2) * 4)}" r="4"></circle>' for k in range(5)) + '</g>')
    return "".join(o)

def hedged_way(w, h, seed):
    """A man whose way is hid, and whom God hath hedged in: a narrow path shut in by thorn hedges on either side and across
    the way ahead, under a low dark sky."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#2A2A3A", "#6A6A7A"), ground(w, h, h * 0.5, "#4A4038", dy=0),
         P(f"M{f(w * 0.46)} {f(h * 0.52)} L {f(w * 0.54)} {f(h * 0.52)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z", "#8A7A62", 1.6)]
    def thorn_row(x0, y0, x1, y1, n, sz):
        out = []
        for i in range(n):
            t = i / (n - 1); x = x0 + (x1 - x0) * t; y = y0 + (y1 - y0) * t; s = sz[0] + (sz[1] - sz[0]) * t
            out.append(f'<circle cx="{f(x)}" cy="{f(y - s * 0.6)}" r="{f(s)}" fill="#2A3A22" stroke="#0D0D0F" stroke-width="1.6"></circle>')
            for k in range(4):
                a = r.uniform(0, 2 * math.pi)
                out.append(f'<path d="M{f(x)} {f(y - s * 0.6)} l {f(math.cos(a) * s * 1.4)} {f(math.sin(a) * s * 1.4)}" stroke="#0D0D0F" stroke-width="1.6"></path>')
        return "".join(out)
    o.append(thorn_row(w * 0.42, h * 0.52, -w * 0.05, h * 1.0, 12, (8, 40)) + thorn_row(w * 0.58, h * 0.52, w * 1.05, h * 1.0, 12, (8, 40)) + thorn_row(w * 0.43, h * 0.5, w * 0.57, h * 0.5, 5, (8, 9)))
    return "".join(o)

def poured(w, h, seed):
    """My groanings are poured out like water: a jar tipped over in the dust, its water running away into the cracked ground."""
    o = [K2.sky(w, h, "#4A4A6A", "#C8B8A0"), ground(w, h, h * 0.6, "#B8986A", dy=0)]
    r = random.Random(seed)
    for i in range(14):
        x = r.uniform(0, w); y = r.uniform(h * 0.64, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-30, 30))} {f(r.uniform(-8, 8))} l {f(r.uniform(-20, 20))} {f(r.uniform(-6, 6))}" fill="none" stroke="#6A4A2A" stroke-width="1.6"></path>')
    cx, cy, s = w * 0.3, h * 0.74, min(1.6, h / 220)
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) rotate(-70) scale({f(s)})">' + P("M-18 30 C -34 10 -30 -24 -12 -36 L -10 -46 L 10 -46 L 12 -36 C 30 -24 34 10 18 30 Z", "#B5652E", 2.4) + '</g>')
    o.append(f'<path d="M{f(cx + 40 * s)} {f(cy - 6 * s)} C {f(cx + 90 * s)} {f(cy)} {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.98)} {f(h * 0.84)}" fill="none" stroke="#8FD0E2" stroke-width="{f(10 * s)}" stroke-linecap="round" opacity="0.9"></path>')
    return "".join(o)

def whirl(cx, top, bot, w0, w1, seed, color="#C8C0D8", op=0.5, n=14):
    """A whirlwind: rings of cloud narrowing from the sky down toward the earth, its line bending."""
    o = []
    for i in range(n):
        t = i / (n - 1); y = top + (bot - top) * t; rw = w0 + (w1 - w0) * t
        x = cx + math.sin(t * 3.2 + seed) * w0 * 0.12
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rw)}" ry="{f(rw * 0.18 + 4)}" fill="none" stroke="{color}" stroke-width="{f(3 + 9 * (1 - t))}" opacity="{op}"></ellipse>')
        o.append(f'<path d="M{f(x - rw)} {f(y)} C {f(x - rw * 0.4)} {f(y + rw * 0.24)} {f(x + rw * 0.6)} {f(y + rw * 0.2)} {f(x + rw)} {f(y - 2)}" fill="none" stroke="#F3EFE6" stroke-width="{f(1.5 + 2 * (1 - t))}" opacity="{op * 0.8:.2f}"></path>')
    return "".join(o)

def cover_art(p, w, h, seed):
    """The volume cover: the whirlwind coming down over the ash heap, Job sitting small upon it, lightning about."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#0B0B2A", "#5B2470"), clouds(w, h * 0.38, seed, 10, color="#1E1650", op=0.9, ry=0.06, h=h),
         V.rays(w * 0.62, h * 0.4, 30, 40, h, color="#FFF4C2", op=0.12),
         whirl(w * 0.62, h * 0.36, h * 0.78, w * 0.44, w * 0.06, seed, color="#8A7AB8", op=0.55, n=16)]
    for i in range(3): o.append(E2.bolt(w * (0.2 + i * 0.3), h * 0.34, h * 0.3, seed + i, w=1.4))
    o.append(hills(w, h, h * 0.84, seed, "#1A1430", amp=14, step=70) + ground(w, h, h * 0.9, "#2A2238", dy=0))
    o.append(ash_mound(w * 0.36, h * 0.97, w * 0.5, h * 0.12, seed))
    o.append(seated_job(w * 0.34, h * 0.89, 1.0, shard=False))
    return "".join(o)
