"""New drawings for Numbers chapter 14 (Numbers 30–31): pictograms for the law of vows (a man's vow, a daughter in her
father's house, a wife, a widow), and for the war with Midian, told with restraint: the twelve thousand going out with
Phinehas and the trumpets, cities burning far off on the horizon, the long column of the prey coming to the camp, the
metals going through the fire, the spoil divided as a blueprint chart, and the officers' gold brought into the tent.
Nothing of the slaughter (31:7–8, 31:17) is drawn: those verses are words over landscape."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1, numbers1 as N
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art7 import coins, ban
from lev.art import GND, priest, altar
from lev.art4 import verdict, days
from lev.art5 import water, bathe
from num.art import ALL, standard, TRIBE_C
from num.art3 import scroll
from num.art5 import trumpet
def f(v): return f"{v:.1f}"
CY = B8.CY

def vow_box(x, y): return f'<rect x="{f(x - 16)}" y="{f(y - 14)}" width="32" height="20" rx="3" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></rect>' + label(x, y, "VOW", "#0D0D0F", 7)
def hush(x, y): return label(x, y, "…", "#FFD23F", 18)
def girl(p, x, y=86, s=0.3, flip=False): return woman(p, x, y, s, "#C2456A", flip=flip)
def wife(p, x, y=86, s=0.33, flip=False): return woman(p, x, y, s, "#6A3A5A", flip=flip)

def pg_heads(p):       return GND + A.moses(p, 70, 86, 0.36) + "".join(A.elder(c, i)(p, 150 + i * 40, 86, 0.32, flip=True) for i, c in enumerate(A.CLOTHS[:4]))
def pg_man_vow(p):     return GND + man(p, 110, 86, 0.38, "#5A3A22", up=[(-22, -158), (-6, -196), (8, -228)]) + vow_box(200, 50) + label(200, 96, "HE SHALL NOT BREAK HIS WORD", CY, 7)
def pg_father_peace(p): return GND + girl(p, 80) + vow_box(130, 40) + A.elder("#8A6A4A", 1)(p, 220, 86, 0.36, flip=True) + hush(250, 30) + verdict(272, 56, True)
def pg_father_no(p):   return GND + girl(p, 80) + vow_box(130, 40) + A.elder("#8A6A4A", 1)(p, 220, 86, 0.36, flip=True, up=[(-22, -158), (-34, -150), (-48, -140)]) + ban(130, 34, 18)
def pg_married(p):     return GND + wife(p, 90) + vow_box(140, 40) + man(p, 220, 86, 0.38, "#4A3A6A", flip=True) + hush(250, 30)
def pg_husband_no(p):  return GND + wife(p, 90) + vow_box(140, 40) + ban(140, 34, 18) + man(p, 220, 86, 0.38, "#4A3A6A", flip=True, up=[(-22, -158), (-34, -150), (-48, -140)])
def pg_widow(p):       return GND + woman(p, 120, 86, 0.34, "#3A3A4A") + vow_box(180, 40) + label(220, 96, "A WIDOW · DIVORCED", CY, 7)
def pg_house(p):       return GND + A.black_tent(80, 84, 90, 50) + wife(p, 150) + vow_box(190, 40) + man(p, 250, 86, 0.38, "#4A3A6A", flip=True)
def pg_void(p):        return GND + scroll(120, 70, 1.0) + '<path d="M90 36 L 150 76 M150 36 L 90 76" stroke="#D7261E" stroke-width="4"></path>' + man(p, 230, 86, 0.38, "#4A3A6A", flip=True)
def pg_day_to_day(p):  return GND + days(40, 30, 7, lit=7, w=14) + hush(170, 50) + man(p, 250, 86, 0.38, "#4A3A6A", flip=True)
def pg_bear(p):        return GND + man(p, 120, 86, 0.38, "#4A3A6A") + label(220, 50, "HE SHALL BEAR", "#FFD23F", 9) + label(220, 64, "HER INIQUITY", CY, 8)
def pg_statutes(p):    return GND + scroll(110, 74, 1.2, "THESE ARE THE STATUTES") + wife(p, 220) + man(p, 260, 86, 0.38, "#4A3A6A", flip=True)

# ---- the war with Midian -------------------------------------------------------------------------------------------
def going_out(p, w, h, seed):
    """Twelve thousand armed for war, a thousand of every tribe, with Phinehas, the vessels of the sanctuary, and the
    trumpets for the alarm in his hand."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.16, 16, color="#FF8A3D", op=0.3), hills(w, h, h * 0.46, seed, color="#8A5A3A", amp=14), ground(w, h, h * 0.54, "#C8A06A", dy=0)]
    s = fit(b, h * 0.44)
    tribes = list(TRIBE_C)[:13]
    for k in range(3):
        y = h * (0.66 + k * 0.1)
        for i in range(12):
            x = w * (0.02 + i * 0.06) + k * 10
            o.append(man(p, x, y, fit(y, y - h * (0.16 + k * 0.04)), r.choice(A.HEBREW), up=[(-22, -158), (-26, -200), (-28, -236)]))
    for i, t in enumerate(("JUDAH", "REUBEN", "EPHRAIM", "DAN")):
        o.append(standard(w * (0.08 + i * 0.18), h * 0.68, min(1.1, h / 340), TRIBE_C[t], pole=60))
    x = w * 0.84
    o.append(Q.son_priest(p, x, b, s, up=[(-22, -158), (2, -170), (20, -176)], flip=True) + trumpet(x - 22 * s, b - 176 * s, s * 0.6, rot=194))
    return "".join(o)

def burning(w, h, seed):
    """All their cities and all their encampments burnt with fire: smoke rising far off on the horizon, nothing near."""
    r = random.Random(seed)
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#4A2A2A"></rect>', V.rays(w * 0.5, h * 0.62, 30, 20, w, color="#FF6A2A", op=0.15),
         hills(w, h, h * 0.62, seed, color="#2A1A1A", amp=10), ground(w, h, h * 0.7, "#3A2A2A", dy=0)]
    for i in range(6):
        x = w * (0.08 + i * 0.16) + r.uniform(-20, 20)
        o.append(E.blaze(x, h * 0.64, w * 0.05, h * 0.08, seed + i, n=5))
        o.append("".join(f'<ellipse cx="{f(x + k * 12)}" cy="{f(h * (0.5 - k * 0.1))}" rx="{f(w * 0.04 + k * 6)}" ry="{f(h * 0.05)}" fill="#6A6460" opacity="{0.5 - k * 0.08:.2f}"></ellipse>' for k in range(4)))
    return "".join(o)

def prey(p, w, h, seed, meet=False):
    """The captives, the prey and the spoil coming to the camp in the plains of Moab: a long column of flocks and herds
    and people at a distance (meet=True: Moses, Eleazar and the princes going out to meet them without the camp)."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.14, h * 0.18, 16, color="#FF8A3D", op=0.3), ground(w, h, h * 0.46, "#C8A06A", dy=0)]
    for i in range(26):
        t = i / 25; x = w * (0.98 - 0.66 * t); y = h * (0.5 + 0.12 * t)
        kind = i % 4
        s = 0.12 + 0.12 * t
        if kind == 0: o.append(E.sheep(x, y, s * 1.2))
        elif kind == 1: o.append(S1.cow(x, y, s * 0.7, color="#8A5A30", patch="#E8E2D6"))
        elif kind == 2: o.append(N.ass(x, y, s * 0.8))
        else: o.append(woman(p, x, y, fit(y, y - h * 0.14), r.choice(["#8A3A5A", "#5A4A3A", "#4A3A6A"])))
    if meet:
        s = fit(b, h * 0.42)
        o.append(A.moses(p, w * 0.1, b, s) + Q.high_priest(p, w * 0.2, b, s * 0.98))
        for i in range(3): o.append(A.elder(r.choice(A.CLOTHS), i)(p, w * (0.28 + i * 0.06), b, s * 0.95))
    return "".join(o)

def through_fire(w, h):
    """The gold, the silver, the brass, the iron, the tin and the lead go through the fire; all that abideth not the fire
    goes through the water."""
    o = [B8.bp(w, h), B8.title_bar(w, "THROUGH THE FIRE · THROUGH THE WATER")]
    metals = [("GOLD", "#E8B830"), ("SILVER", "#C8C8D0"), ("BRASS", "#B87333"), ("IRON", "#6A6A72"), ("TIN", "#A8B0B8"), ("LEAD", "#5A5A66")]
    bw = w * 0.06
    for i, (nm, c) in enumerate(metals):
        x = w * (0.5 + i * 0.075); y = h * 0.5
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(bw)}" height="{f(h * 0.14)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>' + label(x + bw / 2, y + h * 0.22, nm, CY, 7))
    o.append(E.blaze(w * 0.72, h * 0.48, w * 0.44, h * 0.16, 4, n=9))
    o.append(water(w * 0.74, h * 0.9, w * 0.4))
    o.append(label(w * 0.74, h * 0.98, "ALL THAT ABIDETH NOT THE FIRE", CY, 7.5))
    return "".join(o)

def spoil_chart(w, h, half=False):
    """The prey: 675,000 sheep, 72,000 oxen, 61,000 asses, 32,000 persons; divided in two halves, with Jehovah's tribute
    of one in five hundred from the warriors' half and one in fifty from the congregation's half."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE PREY DIVIDED · ONE OF FIVE HUNDRED · ONE OF FIFTY")]
    rows_ = [("SHEEP", 675000, 675, 6750), ("OXEN", 72000, 72, 720), ("ASSES", 61000, 61, 610), ("PERSONS", 32000, 32, 320)]
    x0 = w * 0.52; L = w * 0.34; rh = (h - 60) / 4
    for i, (nm, tot, t1, t2) in enumerate(rows_):
        y = 44 + i * rh + rh * 0.3; bl = L * (tot / 675000) ** 0.5; bh = min(rh * 0.36, 24)
        o.append(label(x0, y - 5, f"{nm} · {tot:,}", "#FFD23F", 9, "start", ls=0.06))
        o.append(f'<rect x="{f(x0)}" y="{f(y)}" width="{f(bl / 2)}" height="{f(bh)}" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.2"></rect>'
                 f'<rect x="{f(x0 + bl / 2)}" y="{f(y)}" width="{f(bl / 2)}" height="{f(bh)}" fill="#5A6E8A" stroke="#0D0D0F" stroke-width="1.2"></rect>')
        o.append(label(x0, y + bh + 12, f"TRIBUTE {t1} · TO THE LEVITES {t2}", CY, 7.5, "start", ls=0.04))
    o.append(label(x0, h - 8, "◼ THE MEN OF WAR", "#D7261E", 8, "start") + label(x0 + L * 0.6, h - 8, "◼ THE CONGREGATION", "#8FB8E8", 8, "start"))
    return "".join(o)

def gold(w, h):
    """The officers' oblation: jewels of gold, ankle-chains, bracelets, signet-rings, ear-rings and armlets — 16,750
    shekels, brought into the tent of meeting for a memorial."""
    o = [B8.bp(w, h), B8.title_bar(w, "JEHOVAH'S OBLATION · 16,750 SHEKELS OF GOLD")]
    r = random.Random(7)
    for i in range(36):
        x = w * (0.56 + (i % 6) * 0.07); y = h * (0.2 + (i // 6) * 0.13); k = 1.8
        kind = i % 3
        if kind == 0: o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(9 * k)}" fill="none" stroke="#E8B830" stroke-width="5"></circle>')
        elif kind == 1: o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(12 * k)}" ry="{f(6 * k)}" fill="none" stroke="#E8B830" stroke-width="4"></ellipse><circle cx="{f(x)}" cy="{f(y - 6 * k)}" r="5" fill="#D7261E" stroke="#0D0D0F" stroke-width="1"></circle>')
        else: o.append(f'<path d="M{f(x - 10 * k)} {f(y)} C {f(x - 4 * k)} {f(y + 10 * k)} {f(x + 4 * k)} {f(y + 10 * k)} {f(x + 10 * k)} {f(y)}" fill="none" stroke="#E8B830" stroke-width="4"></path>')
    return "".join(o)
