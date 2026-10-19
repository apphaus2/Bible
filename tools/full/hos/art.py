"""Drawings for the Hosea volume, on top of Daniel's (dan.art carries Esther's, 2 Chronicles', 1 Chronicles', 2 and 1 Kings'
and 2 Samuel's). Israel's land: terraced hills with olive trees and vines (land); Hosea at a distance in olive green with
a black beard (hosea_fig); Gomer in dark plum (gomer_fig). Plates for the children's names, the gifts taken back, the price
in silver and barley, and the things Israel shall abide without."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from dan.art import *
from dan.art import f, K2
from dan.art4 import lion_beast, bear_beast, leopard_beast, field as heraldic, wing
from ecc.art import tree
from sng.art import vine_rows, dove as sdove, rose_lily, lebanon_peaks
from genesis.art2 import bird
from job.art9 import jackal
from jos.art import crowd_at

HOS_C, GOMER_C = "#5E7A2A", "#3A1A3A"

def hosea_fig(p, x, y, s, flip=False, up=None):
    """Hosea at a distance: an olive robe and headcloth, a black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=HOS_C, sw=3, flip=flip, up=up, extra=A.headcloth("#3A4A22", cord="#2A1A10") + A.BLACK_BEARD)

def gomer_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=GOMER_C, woman=True, hair="#0D0D0F", sw=3, flip=flip, up=up)

def child_fig(p, x, y, s, cloth="#C8BCA6", flip=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=2.4, flip=flip)

def olive(x, y, s=1.0, seed=1):
    """An olive tree: a twisted grey trunk and a silvery-green crown."""
    r = random.Random(seed)
    o = [f'<path d="M{f(x - 6 * s)} {f(y)} C {f(x - 10 * s)} {f(y - 20 * s)} {f(x + 6 * s)} {f(y - 30 * s)} {f(x - 2 * s)} {f(y - 46 * s)} L {f(x + 6 * s)} {f(y - 46 * s)} C {f(x + 14 * s)} {f(y - 30 * s)} {f(x + 2 * s)} {f(y - 18 * s)} {f(x + 8 * s)} {f(y)} Z" fill="#6A5E4A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    for i in range(6):
        o.append(f'<ellipse cx="{f(x + r.uniform(-24, 24) * s)}" cy="{f(y - r.uniform(46, 70) * s)}" rx="{f(r.uniform(14, 22) * s)}" ry="{f(r.uniform(9, 13) * s)}" fill="{r.choice(("#7A8A5A", "#8A9A6A", "#6A7A4A"))}" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def land(w, h, seed, tone="day", olives=4, horizon=0.5):
    """Israel's hill country: layered hills with terraces, olive trees on the slopes."""
    skies = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#5A3A5A", "#E8A06A"), "night": ("#0F0E2A", "#3A2A5A"), "grey": ("#8A8A9A", "#C8C2B6"), "dawn": ("#9AB8D8", "#FFE8C0")}
    o = [K2.sky(w, h, *skies[tone])]
    if tone == "night": o.append(mk.stars(40, w, h * 0.4, seed))
    dark = tone in ("night", "dusk")
    o.append(hills(w, h, h * horizon, seed, "#7A6A6A" if dark else "#A8A07A", amp=14, step=110))
    o.append(hills(w, h, h * (horizon + 0.12), seed + 1, "#5A4A4A" if dark else "#8A9A5A", amp=12, step=90))
    for i in range(3):
        y = h * (horizon + 0.2 + i * 0.07)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 8)} {f(w * 0.6)} {f(y + 6)} {f(w + 10)} {f(y - 4)}" fill="none" stroke="{"#3A3030" if dark else "#6A7A3A"}" stroke-width="2"></path>')
    o.append(ground(w, h, h * (horizon + 0.3), "#5A4A3A" if dark else "#B89A6A", dy=-4))
    k = min(1.2, h / 300)
    for i in range(olives):
        o.append(olive(w * (0.08 + i * 0.27 + (i % 2) * 0.05), h * (horizon + 0.22 + (i % 2) * 0.05), k * (0.7 + (i % 3) * 0.1), seed + i))
    return "".join(o)

# ---- Hosea 1–3 ----------------------------------------------------------------------------------------------------------------
def hosea_land(p, w, h, seed):
    """Hosea in the land of Israel, Samaria on its hill far off."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), land(w, h, seed), J.city_hill(w * 0.76, h * 0.5, w * 0.16, h * 0.14, seed)]
    s = fit(b, b - h * 0.52)
    o.append(hosea_fig(p, w * 0.3, b, s))
    return "".join(o)

def house(p, w, h, seed, who=("hosea", "gomer"), child=0, babe=False, tone="day"):
    """Hosea's house: a stone house with a dark door; Hosea and Gomer before it; child = how many children beside them;
    babe=True: a child in Gomer's arms (a small bundle)."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), land(w, h, seed, tone=tone, olives=2, horizon=0.44)]
    hx, hw, ht = w * 0.62, w * 0.3, h * 0.44
    o.append(f'<rect x="{f(hx)}" y="{f(b - ht)}" width="{f(hw)}" height="{f(ht)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx - 6)}" y="{f(b - ht - 10)}" width="{f(hw + 12)}" height="12" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(hx + hw * 0.38)}" y="{f(b - ht * 0.6)}" width="{f(hw * 0.24)}" height="{f(ht * 0.6)}" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(hx + hw * 0.1)}" y="{f(b - ht * 0.8)}" width="{f(hw * 0.14)}" height="{f(ht * 0.16)}" fill="{"#FFC14D" if tone != "day" else "#3A2A1A"}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for i in range(int(hw / 18)):
        o.append(f'<path d="M{f(hx)} {f(b - ht + 14 + i * 14)} L {f(hx + hw * 0.36)} {f(b - ht + 14 + i * 14)}" stroke="#A8906A" stroke-width="1" opacity="0.7"></path>' if b - ht + 14 + i * 14 < b else "")
    s = fit(b, b - h * 0.5)
    if "hosea" in who: o.append(hosea_fig(p, w * 0.22, b, s))
    if "gomer" in who:
        o.append(gomer_fig(p, w * 0.38, b, s * 0.94, flip=True, up=[(-22, -152), (-8, -132), (8, -124)] if babe else None))
        if babe: o.append(f'<ellipse cx="{f(w * 0.38 - 4 * s)}" cy="{f(b - 128 * s)}" rx="{f(16 * s)}" ry="{f(10 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    for i in range(child):
        o.append(child_fig(p, w * (0.48 + i * 0.06), b, s * (0.5 + i * 0.04 if i < 2 else 0.4), ("#C8BCA6", "#E8C8C8", "#B8C8A8")[i]))
    return "".join(o)

KIDS = [("JEZREEL", "A SON", "1:4"), ("LO-RUHAMAH", "A DAUGHTER", "1:6"), ("LO-AMMI", "A SON", "1:9")]
def children_plate(w, h, lit=3, turned=False):
    """The children's names as a plate: Jezreel, Lo-ruhamah, Lo-ammi, lit one by one; turned=True: Ammi and Ruhamah, the
    names turned (2:1, 2:23)."""
    o = [grid_bg(w, h)]
    sz = max(10, min(15, h / 12))
    for i, (nm, kind, ref) in enumerate(KIDS):
        x = w * (0.18 + i * 0.32); on = i < lit
        c = "#FFD23F" if on else "#3A5A7A"
        o.append(f'<rect x="{f(x - w * 0.13)}" y="{f(h * 0.24)}" width="{f(w * 0.26)}" height="{f(h * 0.4)}" fill="#12113A" fill-opacity="0.6" stroke="{c}" stroke-width="{2 if on else 1.2}"></rect>'
                 + label(x, h * 0.42, nm, c, sz) + label(x, h * 0.54, kind, CYAN if on else "#3A5A7A", max(8, sz * 0.6)))
        if turned and i > 0:
            o.append(f'<path d="M{f(x - w * 0.1)} {f(h * 0.38)} L {f(x - w * 0.04)} {f(h * 0.38)}" stroke="#D7261E" stroke-width="3"></path>'
                     + label(x, h * 0.78, ("", "RUHAMAH", "AMMI")[i], "#9CCB5E", sz))
    return "".join(o)

def jezreel_bow(w, h, seed):
    """The valley of Jezreel, broad and green between the hills, a bow broken in two lying on the ground."""
    o = [land(w, h, seed, olives=0, horizon=0.42)]
    k = min(1.4, h / 220)
    cx, cy = w * 0.5, h * 0.86
    o.append(f'<path d="M{f(cx - 80 * k)} {f(cy)} C {f(cx - 70 * k)} {f(cy - 40 * k)} {f(cx - 30 * k)} {f(cy - 50 * k)} {f(cx - 6 * k)} {f(cy - 44 * k)}" fill="none" stroke="#6A3A1A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(cx + 6 * k)} {f(cy - 30 * k)} C {f(cx + 30 * k)} {f(cy - 30 * k)} {f(cx + 70 * k)} {f(cy - 20 * k)} {f(cx + 84 * k)} {f(cy + 4 * k)}" fill="none" stroke="#6A3A1A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(cx - 80 * k)} {f(cy)} L {f(cx - 20 * k)} {f(cy + 6 * k)}" stroke="#E8E2D6" stroke-width="1.4"></path>')
    o.append(label(w * 0.5, h * 0.36, "THE VALLEY OF JEZREEL", "#3A2A1A", max(8, min(11, h / 22))))
    return "".join(o)

def sand_sea(w, h, seed):
    """The sand of the sea, which cannot be measured nor numbered: a long shore under the stars."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0F0E2A", "#3A3A6A"), mk.stars(90, w, h * 0.5, seed),
         f'<path d="M-10 {f(h * 0.5)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.7)} C {f(w * 0.6)} {f(h * 0.64)} {f(w * 0.3)} {f(h * 0.74)} -10 {f(h * 0.68)} Z" fill="#1F3A6A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.68)} C {f(w * 0.3)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.64)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append("".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.72, h))}" r="0.9" fill="#8A6A4A"></circle>' for _ in range(int(w * h / 120))))
    return "".join(o)

def gathered(p, w, h, seed):
    """The children of Judah and the children of Israel gathered together under one head, going up from the land."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="dawn", olives=1), V.rays(w * 0.5, h * 0.2, 30, 10, w * 0.6, color="#FFF4C2", op=0.2)]
    o.append(crowd_at(p, w, h, seed, w * 0.04, w * 0.42, h * 0.72, b, 14, 0.2, 0.4, flip=False))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.58, w * 0.96, h * 0.72, b, 14, 0.2, 0.4, flip=True))
    o.append(route([(w * 0.24, h * 0.68), (w * 0.48, h * 0.5)], color="#FFD23F") + route([(w * 0.76, h * 0.68), (w * 0.52, h * 0.5)], color="#FFD23F")
             + label(w * 0.24, h * 0.46, "JUDAH", "#3A2A1A", 10) + label(w * 0.76, h * 0.46, "ISRAEL", "#3A2A1A", 10))
    return "".join(o)

def wilderness(w, h, seed, tone="day"):
    """A wilderness, a dry land: bare ridges, cracked ground, no tree."""
    r = random.Random(seed)
    skies = {"day": ("#E8C890", "#F8E8C0"), "dusk": ("#5A3A5A", "#E8A06A")}
    o = [K2.sky(w, h, *skies[tone]), sun(w * 0.8, h * 0.2, max(10, h * 0.05), color="#FFE680", op=0.3),
         hills(w, h, h * 0.52, seed, "#C8A070", amp=20, step=120), ground(w, h, h * 0.66, "#D8B080", dy=0)]
    for i in range(18):
        x = r.uniform(0, w); y = r.uniform(h * 0.7, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-20, 20))} {f(r.uniform(4, 10))} l {f(r.uniform(-14, 14))} {f(r.uniform(4, 10))}" stroke="#8A6A4A" stroke-width="1.4" fill="none"></path>')
    return "".join(o)

def thorn_hedge(w, h, seed):
    """I will hedge up thy way with thorns, and build a wall against her: a path running into a thick hedge of thorns and a
    stone wall across it."""
    r = random.Random(seed)
    o = [land(w, h, seed, olives=0, horizon=0.4),
         f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.36)} {f(h * 0.7)} {f(w * 0.46)} {f(h * 0.66)} L {f(w * 0.54)} {f(h * 0.66)} C {f(w * 0.5)} {f(h * 0.72)} {f(w * 0.36)} {f(h * 0.86)} {f(w * 0.36)} {f(h + 10)} Z" fill="#D8C090" stroke="#0D0D0F" stroke-width="1.6"></path>']
    o.append(f'<rect x="{f(w * 0.26)}" y="{f(h * 0.56)}" width="{f(w * 0.56)}" height="{f(h * 0.12)}" fill="#A89880" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(w * 0.26)} {f(h * (0.56 + i * 0.04))} L {f(w * 0.82)} {f(h * (0.56 + i * 0.04))}" stroke="#6A5A4A" stroke-width="1"></path>' for i in range(1, 3)))
    for i in range(60):
        x = r.uniform(w * 0.2, w * 0.9); y = r.uniform(h * 0.6, h * 0.82)
        a = r.uniform(0, math.pi * 2); l = r.uniform(10, 24) * min(1.4, h / 260)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(math.cos(a) * l)} {f(math.sin(a) * l)}" stroke="{r.choice(("#3A4A2A", "#4A3A2A", "#2A3A1A"))}" stroke-width="2.4" stroke-linecap="round"></path>')
    return "".join(o)

GIFTS = ["GRAIN", "NEW WINE", "OIL", "SILVER", "GOLD", "WOOL", "FLAX"]
def _gift(kind, x, y, k, c):
    st = f'fill="none" stroke="{c}" stroke-width="2"'
    if kind == "GRAIN": return "".join(f'<path d="M{f(x + d * k)} {f(y + 22 * k)} L {f(x + d * 0.4 * k)} {f(y - 20 * k)}" {st}></path><ellipse cx="{f(x + d * 0.4 * k)}" cy="{f(y - 24 * k)}" rx="{f(3 * k)}" ry="{f(8 * k)}" {st}></ellipse>' for d in (-10, 0, 10))
    if kind == "NEW WINE": return f'<path d="M{f(x - 10 * k)} {f(y - 22 * k)} L {f(x + 10 * k)} {f(y - 22 * k)} L {f(x + 8 * k)} {f(y - 14 * k)} C {f(x + 20 * k)} {f(y - 8 * k)} {f(x + 20 * k)} {f(y + 18 * k)} {f(x)} {f(y + 22 * k)} C {f(x - 20 * k)} {f(y + 18 * k)} {f(x - 20 * k)} {f(y - 8 * k)} {f(x - 8 * k)} {f(y - 14 * k)} Z" {st}></path>'
    if kind == "OIL": return f'<ellipse cx="{f(x)}" cy="{f(y + 8 * k)}" rx="{f(18 * k)}" ry="{f(12 * k)}" {st}></ellipse><path d="M{f(x + 16 * k)} {f(y + 4 * k)} L {f(x + 26 * k)} {f(y - 4 * k)}" {st}></path>' + E.flame(x + 28 * k, y - 4 * k, 4 * k, 10 * k, 1)
    if kind == "SILVER": return "".join(f'<ellipse cx="{f(x)}" cy="{f(y + 16 * k - i * 7 * k)}" rx="{f(14 * k)}" ry="{f(4 * k)}" {st}></ellipse>' for i in range(5))
    if kind == "GOLD": return f'<rect x="{f(x - 18 * k)}" y="{f(y - 2 * k)}" width="{f(36 * k)}" height="{f(14 * k)}" {st}></rect><rect x="{f(x - 12 * k)}" y="{f(y - 16 * k)}" width="{f(24 * k)}" height="{f(14 * k)}" {st}></rect>'
    if kind == "WOOL": return "".join(f'<circle cx="{f(x + dx * k)}" cy="{f(y + dy * k)}" r="{f(8 * k)}" {st}></circle>' for dx, dy in ((-8, 6), (8, 6), (0, -6)))
    return "".join(f'<path d="M{f(x - 14 * k + i * 7 * k)} {f(y + 22 * k)} C {f(x - 12 * k + i * 7 * k)} {f(y)} {f(x - 16 * k + i * 7 * k)} {f(y - 10 * k)} {f(x - 12 * k + i * 7 * k)} {f(y - 22 * k)}" {st}></path>' for i in range(5))

def gifts_plate(w, h, taken=False):
    """I gave her the grain, and the new wine, and the oil, and multiplied unto her silver and gold; taken=True: taken back
    in the time thereof (drawn in red, dashed)."""
    o = [grid_bg(w, h)]
    k = min(1.3, h / 140, w / 560)
    for i, g in enumerate(GIFTS):
        x = w * (0.08 + i * 0.14); y = h * 0.44
        c = "#FF8A6A" if taken else "#FFD23F"
        o.append(f'<g{" stroke-dasharray=\"5 4\" opacity=\"0.8\"" if taken else ""}>{_gift(g, x, y, k, c)}</g>' + label(x, h * 0.84, g, c, max(7, min(10, 8 * k))))
        if taken: o.append(f'<path d="M{f(x - 22 * k)} {f(y - 26 * k)} L {f(x + 22 * k)} {f(y + 26 * k)}" stroke="#D7261E" stroke-width="2.4"></path>')
    return "".join(o)

def waste_vines(w, h, seed):
    """Her vines and her fig-trees laid waste and made a forest: overgrown rows, a jackal among them at dusk."""
    o = [land(w, h, seed, tone="dusk", olives=0, horizon=0.36), vine_rows(w, h, h * 0.6, h * 0.95, seed, rows=4)]
    r = random.Random(seed)
    for i in range(40):
        x = r.uniform(0, w); y = r.uniform(h * 0.6, h)
        o.append(f'<path d="M{f(x)} {f(y)} c 6 -10 -4 -16 4 -26" stroke="#2A3A1A" stroke-width="2" fill="none"></path>')
    o.append(jackal(w * 0.7, h * 0.94, min(0.8, h / 300), flip=True))
    return "".join(o)

def door_hope(w, h, seed, named=True):
    """The valley of Achor for a door of hope: a stony valley in the wilderness and, in the rock, a doorway full of light."""
    o = [wilderness(w, h, seed, tone="dusk")]
    cx, by = w * 0.5, h * 0.8
    dw, dh = min(w * 0.14, h * 0.3), h * 0.46
    o.append(f'<path d="M{f(cx - w * 0.3)} {f(by)} L {f(cx - w * 0.16)} {f(h * 0.3)} L {f(cx + w * 0.16)} {f(h * 0.26)} L {f(cx + w * 0.32)} {f(by)} Z" fill="#8A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(V.rays(cx, by - dh * 0.5, 24, dw * 0.4, w * 0.6, color="#FFF4C2", op=0.25)
             + f'<path d="M{f(cx - dw / 2)} {f(by)} L {f(cx - dw / 2)} {f(by - dh * 0.8)} A {f(dw / 2)} {f(dw / 2)} 0 0 1 {f(cx + dw / 2)} {f(by - dh * 0.8)} L {f(cx + dw / 2)} {f(by)} Z" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if named: o.append(label(cx, h * 0.96, "THE VALLEY OF ACHOR · A DOOR OF HOPE", "#3A2A1A", max(8, min(11, h / 24))))
    return "".join(o)

def peace_land(w, h, seed):
    """A covenant with the beasts of the field, the birds and the creeping things; the bow and the sword broken out of the land:
    a quiet field, beasts lying down, birds, and a broken bow and sword in the grass."""
    from job.art11 import hind
    o = [land(w, h, seed, tone="dawn", olives=2)]
    k = min(1.0, h / 360)
    o.append(hind(w * 0.18, h * 0.9, k * 0.8) + hind(w * 0.32, h * 0.92, k * 0.6, fawn=True))
    o.append(lion_lying(w * 0.62, h * 0.94, k * 0.7, color="#C8A06A"))
    for i in range(5): o.append(bird(w * (0.2 + i * 0.14), h * (0.16 + (i % 2) * 0.06), 0.9))
    o.append(f'<path d="M{f(w * 0.82)} {f(h * 0.9)} l {f(40 * k)} {f(-6 * k)} M{f(w * 0.86)} {f(h * 0.94)} l {f(36 * k)} {f(4 * k)}" stroke="#8A9AA8" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def answer_chain(w, h):
    """I will answer the heavens, and they shall answer the earth; the earth the grain, the new wine and the oil; and they
    shall answer Jezreel: a chain of answering, as a chart."""
    o = [grid_bg(w, h)]
    steps = [("THE HEAVENS", 0.12), ("THE EARTH", 0.34), ("GRAIN · NEW WINE · OIL", 0.6), ("JEZREEL", 0.88)]
    for i, (t, x) in enumerate(steps):
        o.append(node(w * x, h * 0.5, t, "#FFD23F" if i < 3 else "#9CCB5E", r=8, dy=-16, size=max(8, min(11, h / 18))))
        if i: o.append(route([(w * steps[i - 1][1] + 14, h * 0.5), (w * x - 14, h * 0.5)], color="#8FD0E2"))
    o.append(label(w * 0.5, h * 0.84, "I WILL ANSWER, SAITH JEHOVAH", "#F3EFE6", max(8, min(10, h / 20))))
    return "".join(o)

def price_plate(w, h):
    """Fifteen pieces of silver, and a homer of barley, and a half-homer of barley, as a plate."""
    o = [grid_bg(w, h)]
    k = min(1.2, h / 160)
    for i in range(15):
        x = w * (0.08 + (i % 5) * 0.06); y = h * (0.3 + (i // 5) * 0.2)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(10 * k)}" fill="#C8D0D8" fill-opacity="0.3" stroke="#C8D0D8" stroke-width="2"></circle>')
    o.append(label(w * 0.2, h * 0.92, "FIFTEEN PIECES OF SILVER", "#C8D0D8", 9))
    for i, (x, sc, t) in enumerate(((0.56, 1.0, "A HOMER OF BARLEY"), (0.82, 0.7, "A HALF-HOMER"))):
        cx = w * x; cy = h * 0.6
        o.append(f'<path d="M{f(cx - 40 * k * sc)} {f(cy + 40 * k * sc)} L {f(cx - 30 * k * sc)} {f(cy - 30 * k * sc)} L {f(cx + 30 * k * sc)} {f(cy - 30 * k * sc)} L {f(cx + 40 * k * sc)} {f(cy + 40 * k * sc)} Z" fill="#E8C88A" fill-opacity="0.3" stroke="#E8C88A" stroke-width="2"></path>'
                 + label(cx, h * 0.92, t, "#E8C88A", 9))
    return "".join(o)

WITHOUT = ["KING", "PRINCE", "SACRIFICE", "PILLAR", "EPHOD", "TERAPHIM"]
def without_plate(w, h):
    """Many days without king, and without prince, and without sacrifice, and without pillar, and without ephod or teraphim:
    six empty frames, each struck through."""
    o = [grid_bg(w, h)]
    k = min(1.2, h / 150)
    for i, t in enumerate(WITHOUT):
        x = w * (0.09 + i * 0.164); y = h * 0.44
        o.append(f'<rect x="{f(x - w * 0.065)}" y="{f(h * 0.22)}" width="{f(w * 0.13)}" height="{f(h * 0.48)}" fill="none" stroke="#5A7A9A" stroke-width="1.4" stroke-dasharray="5 4"></rect>'
                 f'<path d="M{f(x - w * 0.05)} {f(h * 0.28)} L {f(x + w * 0.05)} {f(h * 0.64)}" stroke="#D7261E" stroke-width="2"></path>' + label(x, h * 0.15, t, CYAN, max(7, min(10, 8 * k))))
    return "".join(o)

def lily(x, y, s=1.0):
    """A white lily on its stalk."""
    return (f'<path d="M{f(x)} {f(y)} C {f(x + 2 * s)} {f(y - 20 * s)} {f(x - 2 * s)} {f(y - 40 * s)} {f(x)} {f(y - 54 * s)}" stroke="#3A6A2A" stroke-width="{f(2.4 * s)}" fill="none"></path>'
            f'<path d="M{f(x)} {f(y - 30 * s)} C {f(x - 14 * s)} {f(y - 34 * s)} {f(x - 18 * s)} {f(y - 24 * s)} {f(x - 20 * s)} {f(y - 18 * s)} C {f(x - 10 * s)} {f(y - 20 * s)} {f(x - 4 * s)} {f(y - 24 * s)} {f(x)} {f(y - 30 * s)} Z" fill="#4A8A3A" stroke="#0D0D0F" stroke-width="1"></path>'
            + "".join(f'<path d="M{f(x)} {f(y - 54 * s)} C {f(x + dx * 4 * s)} {f(y - 66 * s)} {f(x + dx * 12 * s)} {f(y - 70 * s)} {f(x + dx * 16 * s)} {f(y - 76 * s)} C {f(x + dx * 8 * s)} {f(y - 60 * s)} {f(x + dx * 4 * s)} {f(y - 56 * s)} {f(x)} {f(y - 54 * s)} Z" fill="#F8F4EC" stroke="#0D0D0F" stroke-width="1.2"></path>' for dx in (-1, -0.3, 0.3, 1))
            + f'<circle cx="{f(x)}" cy="{f(y - 58 * s)}" r="{f(2.4 * s)}" fill="#E8B830"></circle>')

def dew_land(w, h, seed):
    """I will be as the dew unto Israel: the hills at dawn, mist in the valleys, the grass beaded with dew, lilies in front."""
    r = random.Random(seed)
    o = [land(w, h, seed, tone="dawn", olives=3), sun(w * 0.72, h * 0.34, max(12, h * 0.04), color="#FFE680", op=0.35)]
    o.append(f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#FFFFFF" opacity="0.35"></rect>')
    for i in range(int(w / 5)):
        x = r.uniform(-10, w + 10); y = r.uniform(h * 0.82, h + 4); hh = r.uniform(10, 26) * min(1.5, h / 300)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + 2)} {f(y - hh * 0.5)} {f(x + 5)} {f(y - hh)} {f(x + 7)} {f(y - hh)}" stroke="{r.choice(("#4A7A2A", "#5E8F26", "#3A6A2A"))}" stroke-width="2" fill="none"></path>')
        if r.random() < 0.35: o.append(f'<circle cx="{f(x + 7)}" cy="{f(y - hh)}" r="2" fill="#E8F6FA" stroke="#8FD0E2" stroke-width="0.6"></circle>')
    k = min(1.4, h / 260)
    for x in (0.28, 0.4, 0.62, 0.74):
        o.append(lily(w * x, h * 0.99, k * (0.8 + (x * 10 % 3) * 0.1)))
    return "".join(o)

def bought(p, w, h, seed):
    """So I bought her to me: Hosea and the woman at the door of the house, the silver and the barley set down."""
    o = house(p, w, h, seed)
    b = h * 0.95; k = min(1.0, h / 300)
    o += "".join(f'<ellipse cx="{f(w * 0.3 + i * 6)}" cy="{f(b - 4 - i * 4)}" rx="{f(8 * k)}" ry="{f(3 * k)}" fill="#C8D0D8" stroke="#0D0D0F" stroke-width="1"></ellipse>' for i in range(5))
    o += f'<path d="M{f(w * 0.46)} {f(b)} L {f(w * 0.47)} {f(b - 30 * k)} L {f(w * 0.53)} {f(b - 30 * k)} L {f(w * 0.54)} {f(b)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    return o
