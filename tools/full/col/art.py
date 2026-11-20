"""Drawings for the Colossians volume, on Philippians' (`from php.art2 import *`: the prison study at Rome, the cast of the
prison letters, and through it 1 Corinthians', Acts' and the epistle kit's drawings) — the letter's road to Colossæ, the
Lycus valley (Laodicea, Hierapolis and Colossæ under Mount Cadmus), the Son as the light at the centre of all things
created (a plate; God never drawn), the bond nailed to the cross, the shadow and the body, the head and the body knit
together, the things above, the old garment put off and the new put on, the household, speech seasoned with salt, and
Paul's own hand and his chain. Every function takes (p, w, h, seed, ...) or (w, h, ...)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from php.art2 import *
from php.art import f, INK, _defs
from co1.art import wise_disputer
from co1.art2 import household, bondservant
from co1.art4 import assembly
from co1.art5 import sealed_tomb, cells
from rom.art2 import baptism

geo.LABEL_AT.setdefault("COLOSSÆ", (8, 12, "start"))
geo.LABEL_AT.setdefault("BRUNDISIUM", (0, 16, "middle"))

# ---- Colossians 1 -------------------------------------------------------------------------------------------------------------
def colossae_road(w, h):
    """To the saints and faithful brethren in Christ that are at Colossæ: the letter's road from Rome down the Appian Way to
    Brundisium, over the sea by Corinth to Ephesus, and up the valley of the Mæander and the Lycus to Colossæ."""
    rt = ["ROME", (14.8, 41.1), "BRUNDISIUM", (19.6, 39.6), (21.2, 37.8), "CORINTH", (24.8, 37.6), "EPHESUS", (28.1, 37.85), "COLOSSÆ"]
    return letter_road(w, h, rt, title="COLOSSIANS 1:2 · TO THE SAINTS … AT COLOSSÆ", box=(11.5, 30.5, 36.6, 42.6),
                       places=("ROME", "BRUNDISIUM", "CORINTH", "EPHESUS", "COLOSSÆ"), hi=("ROME", "COLOSSÆ"),
                       regions=("ITALY", ("ACHAIA", 22.0, 38.6), ("ASIA", 28.4, 39.0), ("MACEDONIA", 22.4, 41.2)))

def epaphras_tells(p, w, h, seed):
    """Even as ye learned of Epaphras our beloved fellow-servant … who also declared unto us your love in the Spirit (1:7–8):
    the room at Rome, Paul sitting chained to the soldier, Timothy on his mat, and Epaphras come from Colossæ standing to
    tell them of the church there."""
    def ep(p_, x, y, s, flip=False):
        return epaphras(p_, x - 0.02 * w, y, s, up=[(-22, -158), (-46, -146), (-66, -156)])
    return prison_study(p, w, h, seed, stage="prison_read", others=(ep,))

def out_of_darkness(w, h, seed):
    """Who delivered us out of the power of darkness, and translated us into the kingdom of the Son of his love (1:13): one
    land seen from a height — at the left under a black sky a dark country of bare rock, at the right the dawn come up over
    a green country and a walled city in the light; a road running out of the dark into the light, no one on it."""
    uid = f"od{seed}"
    o = [f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#05050E"></stop><stop offset="0.45" stop-color="#1A1830"></stop>'
         f'<stop offset="0.7" stop-color="#FFB07A"></stop><stop offset="1" stop-color="#FFF4C2"></stop></linearGradient></defs>'
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>']
    o.append(halo(w * 0.86, h * 0.5, h * 0.7, "#FFE680", 0.5) + rays(w * 0.86, h * 0.5, 18, h * 0.1, h * 1.1, "#FFF4C2", 0.3, 4))
    o.append(f'<g opacity="0.85">' + mk.stars(40, w * 0.4, h * 0.4, seed) + '</g>')
    o.append(f'<path d="M-10 {f(h * 0.62)} L {f(w * 0.08)} {f(h * 0.44)} L {f(w * 0.16)} {f(h * 0.54)} L {f(w * 0.26)} {f(h * 0.4)} L {f(w * 0.38)} {f(h * 0.58)} L {f(w * 0.5)} {f(h * 0.6)} '
             f'C {f(w * 0.7)} {f(h * 0.54)} {f(w * 0.85)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.52)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#14121E" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.6)} C {f(w * 0.7)} {f(h * 0.54)} {f(w * 0.85)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.52)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.46)} {f(h + 10)} Z" fill="#6A9A4A" stroke="{INK}" stroke-width="2"></path>')
    from oba.minor import walls
    o.append(walls(w * 0.74, w * 0.96, h * 0.56, h * 0.14, seed, towers=2))
    o.append(f'<path d="M{f(w * 0.04)} {f(h + 10)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.74)} {f(w * 0.84)} {f(h * 0.57)}" fill="none" stroke="#C8B088" stroke-width="{f(h * 0.05)}" opacity="0.9"></path>')
    return "".join(o)

def cosmic(w, h, title=True):
    """Who is the image of the invisible God, the firstborn of all creation; for in him were all things created, in the
    heavens and upon the earth, things visible and things invisible, whether thrones or dominions or principalities or powers
    (1:15–17): a plate — at the centre a light (the Son, drawn only as light; the Father never drawn), and about it the rings of
    all things: the inner ring, things invisible, thrones, dominions, principalities, powers, as four lights with no form; the
    outer, things visible, the sun and moon and stars, the sea, the mountains, the trees, the beasts and birds and fishes and
    men; lines of light from the centre to all of them."""
    o = [plate_bg(w, h, "COLOSSIANS 1:15–17 · THE FIRSTBORN OF ALL CREATION" if title else None)]
    cx, cy = w / 2, 30 + (h - 30) / 2
    R = min(w * 0.42, (h - 50) / 2)
    r1, r2 = R * 0.42, R * 0.86
    for r, col in ((r2, CY), (r1, GOLD)):
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="{col}" stroke-width="1.6" stroke-dasharray="6 5"></circle>')
    # the four powers: lights with no form on the inner ring
    for i, nm in enumerate(("THRONES", "DOMINIONS", "PRINCIPALITIES", "POWERS")):
        a = math.radians(-135 + i * 90)
        x, y = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(x)} {f(y)}" stroke="#FFE680" stroke-width="1.2" opacity="0.6"></path>' + halo(x, y, 16, "#FFF4C2", 0.6)
                 + f'<circle cx="{f(x)}" cy="{f(y)}" r="5" fill="#FFFDF0"></circle>' + plate_label(x, y + (22 if y > cy else -14), nm, GOLD, 8.5))
    # the things visible on the outer ring, each a small emblem
    def emblem(kind, x, y, k):
        if kind == "sun": return halo(x, y, 12 * k, "#FFE680", 0.7) + f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(7 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="1"></circle>'
        if kind == "moon": return f'<path d="M{f(x + 4 * k)} {f(y - 8 * k)} A {f(8 * k)} {f(8 * k)} 0 1 0 {f(x + 4 * k)} {f(y + 8 * k)} A {f(6 * k)} {f(6 * k)} 0 1 1 {f(x + 4 * k)} {f(y - 8 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></path>'
        if kind == "stars": return "".join(f'<circle cx="{f(x + dx * k)}" cy="{f(y + dy * k)}" r="{f(1.8 * k)}" fill="#F3EFE6"></circle>' for dx, dy in ((-6, -4), (5, -6), (0, 2), (-4, 7), (7, 5)))
        if kind == "sea": return "".join(f'<path d="M{f(x - 10 * k)} {f(y + j * 5 * k)} c {f(3 * k)} {f(-3 * k)} {f(7 * k)} {f(-3 * k)} {f(10 * k)} 0 c {f(3 * k)} {f(3 * k)} {f(7 * k)} {f(3 * k)} {f(10 * k)} 0" stroke="#8FD0E2" stroke-width="1.6" fill="none"></path>' for j in (-1, 0, 1))
        if kind == "mountain": return f'<path d="M{f(x - 12 * k)} {f(y + 8 * k)} L {f(x - 2 * k)} {f(y - 8 * k)} L {f(x + 3 * k)} {f(y)} L {f(x + 6 * k)} {f(y - 4 * k)} L {f(x + 12 * k)} {f(y + 8 * k)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="1"></path>'
        if kind == "tree": return f'<path d="M{f(x)} {f(y + 9 * k)} L {f(x)} {f(y)}" stroke="#6A4A2A" stroke-width="{f(2.4 * k)}"></path><circle cx="{f(x)}" cy="{f(y - 3 * k)}" r="{f(7 * k)}" fill="#4A8A3A" stroke="{INK}" stroke-width="1"></circle>'
        if kind == "bird": return f'<path d="M{f(x - 10 * k)} {f(y)} C {f(x - 5 * k)} {f(y - 6 * k)} {f(x - 2 * k)} {f(y - 4 * k)} {f(x)} {f(y)} C {f(x + 2 * k)} {f(y - 4 * k)} {f(x + 5 * k)} {f(y - 6 * k)} {f(x + 10 * k)} {f(y)}" stroke="#F3EFE6" stroke-width="1.8" fill="none"></path>'
        if kind == "fish": return f'<path d="M{f(x - 9 * k)} {f(y)} C {f(x - 4 * k)} {f(y - 6 * k)} {f(x + 4 * k)} {f(y - 6 * k)} {f(x + 6 * k)} {f(y)} C {f(x + 4 * k)} {f(y + 6 * k)} {f(x - 4 * k)} {f(y + 6 * k)} {f(x - 9 * k)} {f(y)} Z M{f(x + 6 * k)} {f(y)} L {f(x + 11 * k)} {f(y - 4 * k)} L {f(x + 11 * k)} {f(y + 4 * k)} Z" fill="#8FD0E2" stroke="{INK}" stroke-width="1"></path>'
        if kind == "beast": return f'<path d="M{f(x - 10 * k)} {f(y + 6 * k)} L {f(x - 9 * k)} {f(y - 2 * k)} C {f(x - 4 * k)} {f(y - 5 * k)} {f(x + 4 * k)} {f(y - 5 * k)} {f(x + 7 * k)} {f(y - 3 * k)} L {f(x + 11 * k)} {f(y - 8 * k)} L {f(x + 12 * k)} {f(y - 2 * k)} L {f(x + 8 * k)} {f(y + 1 * k)} L {f(x + 8 * k)} {f(y + 6 * k)}" fill="#C8A06A" stroke="{INK}" stroke-width="1"></path>'
        if kind == "man": return f'<circle cx="{f(x)}" cy="{f(y - 7 * k)}" r="{f(3.4 * k)}" fill="#C98E66" stroke="{INK}" stroke-width="1"></circle><path d="M{f(x - 5 * k)} {f(y + 9 * k)} L {f(x - 4 * k)} {f(y - 3 * k)} L {f(x + 4 * k)} {f(y - 3 * k)} L {f(x + 5 * k)} {f(y + 9 * k)} Z" fill="#7A8A9A" stroke="{INK}" stroke-width="1"></path>'
        return ""
    kinds = ["sun", "moon", "stars", "bird", "mountain", "tree", "beast", "man", "fish", "sea"]
    k = max(1.0, R / 120)
    for i, kind in enumerate(kinds):
        a = math.radians(-90 + i * 36)
        x, y = cx + r2 * math.cos(a), cy + r2 * math.sin(a)
        o.append(f'<path d="M{f(cx + r1 * math.cos(a))} {f(cy + r1 * math.sin(a))} L {f(x)} {f(y)}" stroke="#8FD0E2" stroke-width="1" opacity="0.5"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(15 * k)}" fill="#10243A" stroke="{CY}" stroke-width="1.2"></circle>' + emblem(kind, x, y, k))
    # the light at the centre
    o.append(halo(cx, cy, R * 0.34, "#FFE680", 0.75) + rays(cx, cy, 24, R * 0.08, R * 0.36, "#FFF4C2", 0.6, 2.4) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 0.09)}" fill="#FFFDF0"></circle>')
    o.append(plate_label(cx, cy + R * 0.2 + 8, "IN HIM ALL THINGS CONSIST", "#F3EFE6", 8.5))
    o.append(plate_label(14, 44, "THINGS INVISIBLE", GOLD, 8.5, anchor="start") + plate_label(14, 58, "THINGS VISIBLE", CY, 8.5, anchor="start"))
    o.append(plate_label(w - 14, 44, "IN THE HEAVENS", "#F3EFE6", 8.5, anchor="end") + plate_label(w - 14, 58, "UPON THE EARTH", "#F3EFE6", 8.5, anchor="end"))
    return "".join(o)

def peace_cross(w, h, seed):
    """Having made peace through the blood of his cross … whether things upon the earth, or things in the heavens (1:20):
    the hill of the three crosses far off under a darkened sky, small and dark, nothing in detail; and from behind the hill a
    broad light breaking, reaching across the earth below and up into the heavens."""
    o = [sky(w, h, "#05050E", "#3A1E2A"), halo(w * 0.5, h * 0.62, h * 0.9, "#FFE680", 0.45), rays(w * 0.5, h * 0.62, 26, h * 0.12, h * 1.3, "#FFF4C2", 0.25, 5)]
    hx = w * 0.5
    o.append(f'<path d="M{f(hx - w * 0.56)} {f(h * 0.86)} C {f(hx - w * 0.24)} {f(h * 0.56)} {f(hx + w * 0.24)} {f(h * 0.56)} {f(hx + w * 0.56)} {f(h * 0.86)} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2430" stroke="{INK}" stroke-width="2"></rect>')
    k = max(0.35, h / 520)
    for dx, hh in ((-0.07, 50), (0, 66), (0.07, 50)):
        x, y = hx + dx * w, h * 0.62 + (4 if dx else 0)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - hh * k)} M{f(x - hh * k * 0.3)} {f(y - hh * k * 0.72)} L {f(x + hh * k * 0.3)} {f(y - hh * k * 0.72)}" stroke="#0D0D0F" stroke-width="{f(5 * k)}"></path>')
    return "".join(o)

def mystery(w, h, seed):
    """The mystery which hath been hid for ages and generations: but now hath it been manifested … Christ in you, the hope of
    glory (1:26–27): one panel in two — at the left a dark vault and a chest shut and sealed under the dust of ages; at the
    right the chest standing open, a roll lifted out of it in a blaze of light, and the light going out over the nations."""
    o = []
    def vault(p, cw, ch, open_):
        k = min(cw, ch) / 220
        bg = "#0D0D18" if not open_ else "#2A2A5A"
        s = [f'<rect x="-10" y="-10" width="{f(cw + 20)}" height="{f(ch + 20)}" fill="{bg}"></rect>',
             f'<rect x="-10" y="{f(ch * 0.74)}" width="{f(cw + 20)}" height="{f(ch)}" fill="{"#1A1820" if not open_ else "#3A3448"}" stroke="{INK}" stroke-width="2"></rect>']
        if open_: s.append(halo(cw / 2, ch * 0.5, ch * 0.7, "#FFE680", 0.6) + rays(cw / 2, ch * 0.5, 22, ch * 0.1, ch * 1.0, "#FFF4C2", 0.35, 3))
        bx, by, bw, bh = cw / 2 - 60 * k, ch * 0.74 - 50 * k, 120 * k, 50 * k
        s.append(f'<rect x="{f(bx)}" y="{f(by)}" width="{f(bw)}" height="{f(bh)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(bx)} {f(by + bh * 0.3)} L {f(bx + bw)} {f(by + bh * 0.3)}" stroke="#C8963E" stroke-width="{f(3 * k)}"></path>')
        if open_:
            s.append(f'<path d="M{f(bx)} {f(by)} L {f(bx - 10 * k)} {f(by - 40 * k)} L {f(bx + bw - 10 * k)} {f(by - 40 * k)} L {f(bx + bw)} {f(by)} Z" fill="#7A5A3A" stroke="{INK}" stroke-width="2"></path>'
                     + f'<g transform="translate({f(cw / 2)} {f(by - 26 * k)})">' + f'<rect x="{f(-36 * k)}" y="{f(-12 * k)}" width="{f(72 * k)}" height="{f(24 * k)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.6"></rect>'
                     + "".join(f'<path d="M{f(-28 * k)} {f(j * 6 * k - 6 * k)} L {f(28 * k)} {f(j * 6 * k - 6 * k)}" stroke="#4A3020" stroke-width="1.2"></path>' for j in range(3)) + '</g>')
        else:
            s.append(f'<path d="M{f(bx)} {f(by)} L {f(bx + 8 * k)} {f(by - 14 * k)} L {f(bx + bw - 8 * k)} {f(by - 14 * k)} L {f(bx + bw)} {f(by)} Z" fill="#5A3A1E" stroke="{INK}" stroke-width="2"></path>'
                     f'<circle cx="{f(cw / 2)}" cy="{f(by + bh * 0.3)}" r="{f(8 * k)}" fill="{SEAL}" stroke="{INK}" stroke-width="1.6"></circle>')
            r = random.Random(seed)
            s += [f'<path d="M{f(r.uniform(0, cw))} {f(r.uniform(0, ch * 0.7))} l {f(r.uniform(10, 40))} {f(r.uniform(-4, 4))}" stroke="#3A3A4A" stroke-width="1" opacity="0.6"></path>' for _ in range(14)]
        return "".join(s)
    o.append(cells("my", w, h, [lambda p, cw, ch: vault(p, cw, ch, False), lambda p, cw, ch: vault(p, cw, ch, True)]))
    o.append(plate_label(w * 0.25, 22, "HID FOR AGES AND GENERATIONS", "#8FA0C0", 9, halo_="#0D0D18") + plate_label(w * 0.75, 22, "NOW MANIFESTED", "#FFF4C2", 9.5, halo_="#2A2A5A"))
    return "".join(o)

# ---- Colossians 2 -------------------------------------------------------------------------------------------------------------
def lycus_valley(p, w, h, seed, letters=False, names=True):
    """The valley of the Lycus in the morning: Mount Cadmus with snow on its top behind, the river winding down the plain;
    Colossæ at the foot of the mountain, Laodicea on its low hill across the river, Hierapolis on the far slope with the white
    terraces of its springs below it, each named. letters=True: the two letters going between Colossæ and Laodicea (4:16),
    dashed arrows with a sealed scroll on each."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8")]
    o.append(f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.18)} {f(h * 0.18)} L {f(w * 0.3)} {f(h * 0.24)} L {f(w * 0.42)} {f(h * 0.12)} L {f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.7)} {f(h * 0.36)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.6)} L -10 {f(h * 0.6)} Z" fill="#7A7A8A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.36)} {f(h * 0.17)} L {f(w * 0.42)} {f(h * 0.12)} L {f(w * 0.49)} {f(h * 0.21)} L {f(w * 0.45)} {f(h * 0.19)} L {f(w * 0.42)} {f(h * 0.22)} L {f(w * 0.39)} {f(h * 0.18)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=10, step=80) + ground(w, h, h * 0.58, "#A8B87A", dy=0))
    o.append(f'<path d="M-10 {f(h * 0.9)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.5)} {f(h * 0.74)} C {f(w * 0.7)} {f(h * 0.76)} {f(w * 0.8)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.62)}" fill="none" stroke="#4A8AB8" stroke-width="{f(max(4, h * 0.02))}"></path>')
    # Hierapolis on the far slope (right), its white terraces
    hx, hy = w * 0.82, h * 0.5
    o.append("".join(f'<rect x="{f(hx - w * 0.1 + j * 6)}" y="{f(hy + j * h * 0.025)}" width="{f(w * 0.18 - j * 10)}" height="{f(h * 0.025)}" fill="#F3EFE6" stroke="#8A9AA0" stroke-width="1"></rect>' for j in range(5)))
    o.append(town_hill(hx, hy - h * 0.01, w * 0.07, h * 0.08, seed, color="#9A9A7A"))
    o.append(town_hill(w * 0.3, h * 0.66, w * 0.1, h * 0.1, seed + 1, color="#9A8A6A"))       # Laodicea on its low hill
    o.append(town_hill(w * 0.58, h * 0.6, w * 0.08, h * 0.08, seed + 2, color="#8A8A6A"))     # Colossæ under the mountain
    pts = {"COLOSSÆ": (w * 0.58, h * 0.6), "LAODICEA": (w * 0.3, h * 0.66), "HIERAPOLIS": (hx, hy - h * 0.06)}
    for nm, (x, y) in (pts.items() if names else ()):
        o.append(plate_label(x, y + h * 0.12 if nm != "HIERAPOLIS" else y - h * 0.08, nm, "#F3EFE6", 10, halo_="#2A2A1A"))
    if letters:
        (x1, y1), (x2, y2) = pts["COLOSSÆ"], pts["LAODICEA"]
        for sgn, dy in ((1, -0.06), (-1, 0.05)):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + h * dy * 2.4
            a, b_ = ((x1, y1 - h * 0.05), (x2, y2 - h * 0.05)) if sgn > 0 else ((x2, y2 - h * 0.02), (x1, y1 - h * 0.02))
            o.append(f'<path d="M{f(a[0])} {f(a[1])} Q {f(mx)} {f(my)} {f(b_[0])} {f(b_[1])}" fill="none" stroke="#D7261E" stroke-width="3" stroke-dasharray="8 6"></path>'
                     + sealed_scroll(mx, (a[1] + b_[1]) / 2 + (my - (a[1] + b_[1]) / 2) / 2, 0.36, rot=-8))
    return "".join(o)

def rooted(p, w, h, seed):
    """Rooted and builded up in him, and established in your faith (2:7): one panel in two — at the left a tree standing in
    the field, the ground cut away to show its roots going down deep; at the right a house going up course by course on its
    stone foundation, a mason's level laid on the wall."""
    def tree_(p_, cw, ch):
        gy = ch * 0.56
        s = [sky(cw, ch, "#8FD0E2", "#F3E8C8"), f'<rect x="-10" y="{f(gy)}" width="{f(cw + 20)}" height="{f(ch)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>',
             f'<rect x="-10" y="{f(gy)}" width="{f(cw + 20)}" height="{f(ch * 0.04)}" fill="#6A9A4A"></rect>']
        x = cw / 2
        r = random.Random(seed)
        for i in range(9):                                     # the roots
            ang = math.radians(r.uniform(40, 140)); L = ch * r.uniform(0.18, 0.4)
            s.append(f'<path d="M{f(x)} {f(gy)} C {f(x + math.cos(ang) * L * 0.3)} {f(gy + L * 0.4)} {f(x + math.cos(ang) * L * 0.8)} {f(gy + L * 0.6)} {f(x + math.cos(ang) * L)} {f(gy + math.sin(ang) * L)}" '
                     f'fill="none" stroke="#3A2414" stroke-width="{f(r.uniform(2, 5))}"></path>')
        s.append(f'<path d="M{f(x - 8)} {f(gy)} L {f(x - 6)} {f(ch * 0.26)} L {f(x + 6)} {f(ch * 0.26)} L {f(x + 8)} {f(gy)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>')
        for dx, dy, rr in ((0, 0.18, 0.16), (-0.18, 0.24, 0.12), (0.18, 0.24, 0.12), (-0.08, 0.1, 0.11), (0.1, 0.12, 0.1)):
            s.append(f'<circle cx="{f(x + dx * cw)}" cy="{f(ch * dy)}" r="{f(ch * rr)}" fill="#4A8A3A" stroke="{INK}" stroke-width="1.6"></circle>')
        return "".join(s)
    def house_(p_, cw, ch):
        gy = ch * 0.84
        s = [sky(cw, ch, "#8FD0E2", "#F3E8C8"), ground(cw, ch, gy, "#C8B07A", dy=0)]
        x0, x1 = cw * 0.18, cw * 0.82
        bh = ch * 0.07
        for j in range(7):
            y = gy - (j + 1) * bh
            col = "#8A8478" if j < 2 else "#D8C8A0"
            xs = x0 + (bh * 0.6 if j % 2 else 0)
            while xs < x1 - 2:
                bw = min(bh * 2.2, x1 - xs)
                s.append(f'<rect x="{f(xs)}" y="{f(y)}" width="{f(bw)}" height="{f(bh)}" fill="{col}" stroke="{INK}" stroke-width="1.4"></rect>')
                xs += bw
        top = gy - 7 * bh
        s.append(f'<path d="M{f(x0 + cw * 0.1)} {f(top - 8)} L {f(x0 + cw * 0.36)} {f(top - 8)}" stroke="#C8A060" stroke-width="5"></path>'
                 f'<circle cx="{f(x0 + cw * 0.23)}" cy="{f(top - 8)}" r="3" fill="#8FD0E2"></circle>')
        s.append(f'<rect x="{f(cw * 0.46)}" y="{f(gy - 4 * bh)}" width="{f(cw * 0.12)}" height="{f(4 * bh)}" fill="#3A2214" stroke="{INK}" stroke-width="1.6"></rect>')
        return "".join(s)
    return cells(p, w, h, [tree_, house_]) + plate_label(w * 0.25, 22, "ROOTED", "#F3EFE6", 10, halo_="#3A2A1A") + plate_label(w * 0.75, 22, "BUILDED UP", "#F3EFE6", 10, halo_="#3A2A1A")

def buried_raised(p, w, h, seed):
    """Having been buried with him in baptism, wherein ye were also raised with him (2:12): one panel in two — at the left
    the tomb hewn in the rock at evening, the great stone rolled to its door and sealed (1 Corinthians' drawing); at the right
    the river at dawn, a man going down into the water and another beside him (Romans' drawing)."""
    return cells(p, w, h, [lambda p_, cw, ch: sealed_tomb(p_, cw, ch, seed), lambda p_, cw, ch: baptism(p_, cw, ch, seed + 1)])

def bond_nailed(w, h, seed):
    """Having blotted out the bond written in ordinances that was against us … and he hath taken it out of the way, nailing
    it to the cross (2:14): a rough beam of wood across the evening sky, and on it the bond — a written sheet, its writing
    blotted out with a dark wash — fixed with a great iron nail through it. No one on the beam."""
    o = [sky(w, h, "#2A1A3A", "#C8682E"), halo(w * 0.7, h * 0.7, h * 0.6, "#FFC14D", 0.35)]
    by = h * 0.36
    o.append(f'<path d="M-10 {f(by)} L {f(w + 10)} {f(by - h * 0.04)} L {f(w + 10)} {f(by + h * 0.18)} L -10 {f(by + h * 0.22)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="3"></path>')
    r = random.Random(seed)
    for _ in range(12):                                        # the grain of the wood
        y = by + r.uniform(0.02, 0.18) * h; x = r.uniform(0, w * 0.9)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(40, 120))} {f(-r.uniform(0, 6))}" stroke="#4A2E18" stroke-width="1.4"></path>')
    sw_, sh_ = min(w * 0.3, h * 0.7), min(h * 0.62, w * 0.36)
    sx, sy = w * 0.5 - sw_ / 2, by - sh_ * 0.18
    o.append(f'<g transform="rotate(-4 {f(w * 0.5)} {f(sy + sh_ / 2)})">' + open_letter(sx, sy, sw_, sh_, rows=9, seed=seed)
             + f'<rect x="{f(sx + sw_ * 0.06)}" y="{f(sy + sh_ * 0.1)}" width="{f(sw_ * 0.88)}" height="{f(sh_ * 0.8)}" fill="#2A1A10" opacity="0.55"></rect>'
             + '</g>')
    nx, ny = w * 0.5, sy + sh_ * 0.14                           # the nail
    o.append(f'<circle cx="{f(nx)}" cy="{f(ny)}" r="{f(max(6, h * 0.03))}" fill="#5A5A64" stroke="{INK}" stroke-width="2"></circle>'
             f'<circle cx="{f(nx - 2)}" cy="{f(ny - 2)}" r="{f(max(2, h * 0.008))}" fill="#9A9AA4"></circle>')
    return "".join(o)

def shadow_body(w, h):
    """Let no man therefore judge you in meat, or in drink, or in respect of a feast day or a new moon or a sabbath day:
    which are a shadow of the things to come; but the body is Christ's (2:16–17): a plate — five things on a ledge, each
    named (bread and meat, a cup, a festal palm, the new moon, the sabbath lamps), a light at the right casting their long
    shadows to the left; the light is named the body."""
    o = [plate_bg(w, h, "COLOSSIANS 2:16–17 · A SHADOW OF THE THINGS TO COME")]
    ly = h - 52
    o.append(f'<rect x="10" y="{f(ly)}" width="{f(w - 20)}" height="10" fill="#3A3018" stroke="{GOLD}" stroke-width="1.4"></rect>')
    lx, lyy = w - 60, ly - (h - 90) * 0.5
    o.append(halo(lx, lyy, 70, "#FFE680", 0.7) + rays(lx, lyy, 20, 14, 80, "#FFF4C2", 0.5, 2) + f'<circle cx="{f(lx)}" cy="{f(lyy)}" r="12" fill="#FFFDF0"></circle>')
    o.append(plate_label(lx, lyy + 40, "THE BODY", GOLD, 9) + plate_label(lx, lyy + 52, "IS CHRIST'S", GOLD, 9))
    names = ["MEAT", "DRINK", "A FEAST DAY", "A NEW MOON", "A SABBATH"]
    n = len(names)
    span = w - 150
    k = min(1.0, (h - 100) / 140)
    for i, nm in enumerate(names):
        x = 40 + span * (i + 0.5) / n
        hh = 40 * k
        # the shadow: thrown to the left along the ledge, away from the light
        L = 40 + (lx - x) * 0.32
        o.append(f'<path d="M{f(x - 10)} {f(ly)} L {f(x - 10 - L)} {f(ly)} L {f(x - 10 - L * 0.9)} {f(ly - hh * 0.5)} L {f(x - 8)} {f(ly - hh)} Z" fill="#05101C" opacity="0.8"></path>')
        if i == 0: o.append(f'<ellipse cx="{f(x)}" cy="{f(ly - 10 * k)}" rx="{f(18 * k)}" ry="{f(10 * k)}" fill="#C88A4A" stroke="{INK}" stroke-width="1.4"></ellipse>')
        if i == 1: o.append(f'<path d="M{f(x - 10 * k)} {f(ly - 34 * k)} L {f(x + 10 * k)} {f(ly - 34 * k)} C {f(x + 10 * k)} {f(ly - 20 * k)} {f(x + 4 * k)} {f(ly - 16 * k)} {f(x + 2 * k)} {f(ly - 14 * k)} L {f(x + 2 * k)} {f(ly - 4 * k)} L {f(x + 8 * k)} {f(ly)} L {f(x - 8 * k)} {f(ly)} L {f(x - 2 * k)} {f(ly - 4 * k)} L {f(x - 2 * k)} {f(ly - 14 * k)} C {f(x - 4 * k)} {f(ly - 16 * k)} {f(x - 10 * k)} {f(ly - 20 * k)} {f(x - 10 * k)} {f(ly - 34 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></path>')
        if i == 2: o.append(f'<path d="M{f(x)} {f(ly)} L {f(x)} {f(ly - 46 * k)}" stroke="#6A8A3A" stroke-width="{f(2.4 * k)}"></path>'
                            + "".join(f'<path d="M{f(x)} {f(ly - (12 + j * 8) * k)} l {f(sg * 12 * k)} {f(-8 * k)}" stroke="#4A8A3A" stroke-width="{f(3 * k)}"></path>' for j in range(4) for sg in (-1, 1)))
        if i == 3: o.append(f'<path d="M{f(x + 4 * k)} {f(ly - 40 * k)} A {f(14 * k)} {f(14 * k)} 0 1 0 {f(x + 4 * k)} {f(ly - 12 * k)} A {f(11 * k)} {f(11 * k)} 0 1 1 {f(x + 4 * k)} {f(ly - 40 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.2"></path>')
        if i == 4: o.append(clay_lamp(x - 10 * k, ly - 6 * k, 0.5 * k) + clay_lamp(x + 12 * k, ly - 6 * k, 0.5 * k))
        o.append(plate_label(x, ly + 26, nm, "#F3EFE6", 8.5))
    return "".join(o)

def knit_body(w, h, seed):
    """Not holding fast the Head, from whom all the body, being supplied and knit together through the joints and bands,
    increaseth with the increase of God (2:19): a plate — the head a light at the top, and from it the body of many members,
    each a small light, joined one to another by gold bands and to the head, branching downward and growing."""
    o = [plate_bg(w, h, "COLOSSIANS 2:19 · KNIT TOGETHER THROUGH THE JOINTS AND BANDS")]
    hx, hy = w * 0.5, 64
    r = random.Random(seed)
    levels = [1, 3, 5, 7]
    nodes = [[(hx, hy)]]
    for li, n in enumerate(levels[1:], 1):
        y = hy + li * (h - hy - 40) / (len(levels) - 0.6)
        row = [(w * 0.5 + (j - (n - 1) / 2) * w * 0.12 + r.uniform(-8, 8), y + r.uniform(-6, 6)) for j in range(n)]
        nodes.append(row)
    for li in range(1, len(nodes)):
        for j, (x, y) in enumerate(nodes[li]):
            prev = nodes[li - 1]
            near = sorted(prev, key=lambda q: abs(q[0] - x))[:2]
            for (px, py) in near:
                o.append(f'<path d="M{f(px)} {f(py)} L {f(x)} {f(y)}" stroke="{GOLD}" stroke-width="2.2" opacity="0.8"></path>')
            if j:
                qx, qy = nodes[li][j - 1]
                o.append(f'<path d="M{f(qx)} {f(qy)} L {f(x)} {f(y)}" stroke="{CY}" stroke-width="1.6" stroke-dasharray="4 3"></path>')
    for li, row in enumerate(nodes):
        for (x, y) in row:
            if li == 0: o.append(halo(x, y, 40, "#FFE680", 0.7) + f'<circle cx="{f(x)}" cy="{f(y)}" r="10" fill="#FFFDF0"></circle>')
            else: o.append(halo(x, y, 14, "#FFF4C2", 0.4) + f'<circle cx="{f(x)}" cy="{f(y)}" r="5" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></circle>')
    o.append(plate_label(hx + 30, hy + 4, "THE HEAD", GOLD, 9, anchor="start"))
    o.append(plate_label(14, h - 18, "THE INCREASE OF GOD", CY, 9, anchor="start"))
    return "".join(o)

# ---- Colossians 3 -------------------------------------------------------------------------------------------------------------
def things_above(w, h, seed):
    """Seek the things that are above, where Christ is, seated on the right hand of God. Set your mind on the things that are
    above, not on the things that are upon the earth (3:1–2): below, the earth at evening — the fields, a town, its roads;
    above, the clouds parted and the heavens open in gold light (no one drawn in it)."""
    o = [sky(w, h, "#FFF4C2", "#5A4A7A"), halo(w * 0.5, -h * 0.1, h * 0.8, "#FFFDF0", 0.7), rays(w * 0.5, -h * 0.1, 30, h * 0.1, h * 1.2, "#FFFDF0", 0.3, 5)]
    r = random.Random(seed)
    for j in range(7):                                         # the bank of cloud, parted in the middle
        side = -1 if j % 2 == 0 else 1
        cx = w * 0.5 + side * w * r.uniform(0.18, 0.46); cy = h * r.uniform(0.38, 0.5)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * r.uniform(0.12, 0.2))}" ry="{f(h * r.uniform(0.05, 0.08))}" fill="#E8D8E8" stroke="{INK}" stroke-width="1.4" opacity="0.95"></ellipse>')
    o.append(f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3048"></rect>'
             + hills(w, h, h * 0.62, seed, color="#4A3A4A", amp=10, step=90) + ground(w, h, h * 0.7, "#5A4A3A", dy=0))
    from oba.minor import walls
    o.append(walls(w * 0.58, w * 0.86, h * 0.72, h * 0.08, seed, lit=True, towers=2, color="#7A6A5A"))
    for j in range(4):
        o.append(f'<path d="M{f(-10)} {f(h * (0.78 + j * 0.06))} C {f(w * 0.3)} {f(h * (0.76 + j * 0.06))} {f(w * 0.6)} {f(h * (0.8 + j * 0.06))} {f(w + 10)} {f(h * (0.78 + j * 0.06))}" stroke="#4A3A2A" stroke-width="1.4" fill="none"></path>')
    return "".join(o)

def garments(p, w, h, seed):
    """Seeing that ye have put off the old man with his doings, and have put on the new man (3:9–10): a plain room in the
    morning light from the door, a man standing in a new white robe, drawing its mantle over his shoulder; the old garment,
    dark and worn, cast down on the floor behind him."""
    b = h * 0.94
    o = [_defs(p), room(w, h, b, wall="#D8C8A8", floor="#8A7A62"),
         f'<rect x="{f(w * 0.74)}" y="{f(h * 0.22)}" width="{f(w * 0.14)}" height="{f(b - h * 0.22)}" fill="#FFF4C2" stroke="{INK}" stroke-width="2"></rect>',
         halo(w * 0.81, h * 0.6, h * 0.6, "#FFF4C2", 0.4)]
    s = fit(b, b - min(h * 0.74, 214))
    ox = w * 0.24                                              # the old garment, crumpled on the floor
    o.append(f'<path d="M{f(ox - 70 * s)} {f(b)} C {f(ox - 60 * s)} {f(b - 30 * s)} {f(ox - 20 * s)} {f(b - 22 * s)} {f(ox)} {f(b - 34 * s)} C {f(ox + 24 * s)} {f(b - 26 * s)} {f(ox + 50 * s)} {f(b - 30 * s)} {f(ox + 66 * s)} {f(b)} Z" '
             f'fill="#3A3430" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(ox - 40 * s)} {f(b - 6 * s)} L {f(ox - 30 * s)} {f(b - 18 * s)} M{f(ox + 10 * s)} {f(b - 8 * s)} L {f(ox + 24 * s)} {f(b - 20 * s)}" stroke="#1A1614" stroke-width="2"></path>')
    o.append(robed(p, w * 0.5, b, s, "#FFFDF4", hair="#2A1A10", beard="#2A1A10", mantle="#E8E2D6", belt="#C8A060",
                   up=[(-22, -158), (-44, -138), (-60, -118)]))
    return "".join(o)

def garment_plate(w, h):
    """Put on therefore … a heart of compassion, kindness, lowliness, meekness, longsuffering … and above all these things
    put on love, which is the bond of perfectness (3:12–14): a plate — five robes hanging from a rail, each named, and a gold
    girdle laid across them all, named love."""
    o = [plate_bg(w, h, "COLOSSIANS 3:12–14 · PUT ON THEREFORE")]
    names = ["COMPASSION", "KINDNESS", "LOWLINESS", "MEEKNESS", "LONGSUFFERING"]
    cols = ["#5A7A9A", "#7A9A6A", "#9A8A6A", "#7A6A8A", "#6A8A8A"]
    ry = 54
    o.append(f'<path d="M20 {f(ry)} L {f(w - 20)} {f(ry)}" stroke="#C8A060" stroke-width="5"></path>')
    n = len(names); cw = (w - 40) / n
    gh = min(h - ry - 60, cw * 1.6)
    for i, (nm, c) in enumerate(zip(names, cols)):
        x = 20 + cw * (i + 0.5); gw = cw * 0.62
        o.append(f'<path d="M{f(x)} {f(ry)} L {f(x)} {f(ry + 10)}" stroke="#C8A060" stroke-width="2"></path>'
                 f'<path d="M{f(x - gw * 0.36)} {f(ry + 12)} L {f(x - gw * 0.5)} {f(ry + 12 + gh * 0.16)} L {f(x - gw * 0.34)} {f(ry + 12 + gh * 0.2)} L {f(x - gw * 0.4)} {f(ry + 12 + gh)} '
                 f'L {f(x + gw * 0.4)} {f(ry + 12 + gh)} L {f(x + gw * 0.34)} {f(ry + 12 + gh * 0.2)} L {f(x + gw * 0.5)} {f(ry + 12 + gh * 0.16)} L {f(x + gw * 0.36)} {f(ry + 12)} '
                 f'C {f(x + gw * 0.1)} {f(ry + 20)} {f(x - gw * 0.1)} {f(ry + 20)} {f(x - gw * 0.36)} {f(ry + 12)} Z" fill="{c}" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(plate_label(x, ry + 12 + gh + 16, nm, "#F3EFE6", 8.5))
    gy = ry + 12 + gh * 0.38
    o.append(f'<path d="M24 {f(gy)} C {f(w * 0.3)} {f(gy + 10)} {f(w * 0.7)} {f(gy - 6)} {f(w - 24)} {f(gy + 4)}" stroke="{INK}" stroke-width="14" fill="none"></path>'
             f'<path d="M24 {f(gy)} C {f(w * 0.3)} {f(gy + 10)} {f(w * 0.7)} {f(gy - 6)} {f(w - 24)} {f(gy + 4)}" stroke="#E8B830" stroke-width="10" fill="none"></path>')
    o.append(plate_label(w * 0.5, gy + 4, "LOVE · THE BOND OF PERFECTNESS", "#3A2A10", 9, halo_="#E8B830"))
    return "".join(o)

def servant_master(p, w, h, seed):
    """Servants, obey in all things them that are your masters … whatsoever ye do, work heartily, as unto the Lord …
    Masters, render unto your servants that which is just and equal (3:22–4:1): the court of a house in the morning, a servant
    carrying a water jar on his shoulder; the master at the door counting wages into another servant's hand; the light over
    the wall."""
    b = h * 0.93
    o = [_defs(p), court(w, h, b, seed, "day")]
    s = fit(b, b - min(h * 0.72, 210))
    jar_ = '<path d="M-72 -176 C -86 -176 -90 -158 -84 -150 L -60 -150 C -54 -158 -58 -176 -72 -176 Z" fill="#B85A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(robed(p, w * 0.22, b, s, "#C8B898", hair="#2A1A10", belt="#5A3A1E", flip=True, up=[(-22, -158), (-46, -170), (-64, -168)], extra=jar_))
    o.append(robed(p, w * 0.64, b, s, "#9A8A6A", hair="#1A1210", belt="#5A3A1E", flip=True, up=[(-22, -158), (-40, -134), (-58, -128)]))
    coins = "".join(f'<circle cx="{-62 + i * 4}" cy="{-126 - i * 2}" r="3" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.8"></circle>' for i in range(3))
    o.append(robed(p, w * 0.8, b, s, PHILEMON_LOOK["cloth"], head="#E8E2D6", cord="#5A4A3A", beard="#5A4A3A", mantle="#2A3A5A",
                   up=[(-22, -158), (-40, -136), (-62, -130)], extra=coins))
    return "".join(o)

def salt(p, w, h, seed):
    """Let your speech be always with grace, seasoned with salt (4:6): a table by the door of a house — a loaf, a small bowl
    heaped with white salt, a cup; through the open door, in the street, two men talking together."""
    b = h * 0.94
    o = [_defs(p), room(w, h, b, wall="#D8C098", floor="#8A6A4A")]
    dx, dw = w * 0.56, w * 0.36
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.14)}" width="{f(dw)}" height="{f(b - h * 0.14)}" fill="#8FD0E2" stroke="{INK}" stroke-width="3"></rect>')
    o.append(f'<g><clipPath id="{p}dr"><rect x="{f(dx)}" y="{f(h * 0.14)}" width="{f(dw)}" height="{f(b - h * 0.14)}"></rect></clipPath>'
             f'<g clip-path="url(#{p}dr)">' + houses(w, h, h * 0.6, seed, x0=dx - 20, x1=dx + dw + 20, hmin=0.24, hmax=0.38) + ground(w, h, h * 0.6, "#C8B898", dy=0))
    s2 = fit(b * 0.98, b * 0.98 - min(h * 0.46, 140))
    o.append(saint(p, dx + dw * 0.32, b * 0.98, s2, 3, flip=True, up=[(-22, -158), (-44, -150), (-62, -158)]) + saint(p, dx + dw * 0.7, b * 0.98, s2, 0))
    o.append('</g></g>')
    tx, ty, tw = w * 0.06, b - h * 0.24, w * 0.44
    o.append(f'<rect x="{f(tx)}" y="{f(ty)}" width="{f(tw)}" height="{f(h * 0.03)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(xx)}" y="{f(ty + h * 0.03)}" width="{f(w * 0.02)}" height="{f(b - ty - h * 0.03)}" fill="#4A2A14" stroke="{INK}" stroke-width="1.6"></rect>' for xx in (tx + w * 0.02, tx + tw - w * 0.04)))
    k = min(w, h) / 260
    o.append(f'<ellipse cx="{f(tx + tw * 0.24)}" cy="{f(ty - 10 * k)}" rx="{f(30 * k)}" ry="{f(13 * k)}" fill="#C88A4A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<path d="M{f(tx + tw * 0.52 - 18 * k)} {f(ty)} C {f(tx + tw * 0.52 - 20 * k)} {f(ty - 16 * k)} {f(tx + tw * 0.52 + 20 * k)} {f(ty - 16 * k)} {f(tx + tw * 0.52 + 18 * k)} {f(ty)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(tx + tw * 0.52 - 16 * k)} {f(ty - 12 * k)} C {f(tx + tw * 0.52 - 8 * k)} {f(ty - 26 * k)} {f(tx + tw * 0.52 + 8 * k)} {f(ty - 26 * k)} {f(tx + tw * 0.52 + 16 * k)} {f(ty - 12 * k)} Z" fill="#F8F8F4" stroke="{INK}" stroke-width="1.2"></path>'
             f'<path d="M{f(tx + tw * 0.8 - 9 * k)} {f(ty)} L {f(tx + tw * 0.8 - 11 * k)} {f(ty - 24 * k)} L {f(tx + tw * 0.8 + 11 * k)} {f(ty - 24 * k)} L {f(tx + tw * 0.8 + 9 * k)} {f(ty)} Z" fill="#B85A3A" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(plate_label(tx + tw * 0.52, ty - 34 * k, "SALT", "#F3EFE6", 9, halo_="#5A3A1E"))
    return "".join(o)

def sent_with(p, w, h, seed):
    """All my affairs shall Tychicus make known unto you … whom I have sent unto you … together with Onesimus (4:7–9): the
    room at Rome, Paul standing chained to the soldier, handing the sealed letter to Tychicus in the doorway, Onesimus beside
    him ready for the road, Timothy on his mat."""
    def ones(p_, x, y, s, flip=False): return onesimus(p_, w * 0.07, y, s, flip=True)     # at the left, ready for the road
    return prison_study(p, w, h, seed, stage="prison_give", scribe=False, bearer=tychicus, others=(ones,))

def own_hand(w, h, seed, ledger=False):
    """The salutation of me Paul with mine own hand. Remember my bonds (4:18): close over the table by lamplight, the last
    lines of the letter at the foot of the sheet, and Paul's own hand writing them with the reed pen, the iron cuff on his wrist
    and the chain running off the table. ledger=True (Philemon 18–19): the sheet a reckoning, a column of sums and the
    pledge written under them."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2418"></rect>', lamp_glow(w * 0.78, h * 0.3, max(w, h) * 0.6, f"oh{seed}", op=0.55)]
    ty = h * 0.3
    o.append(f'<path d="M-10 {f(ty)} L {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></path>')
    lw, lh = w * 0.56, h * 0.6
    lx, ly = w * 0.12, ty + h * 0.06
    o.append(f'<g transform="rotate(-3 {f(lx + lw / 2)} {f(ly + lh / 2)})">' + open_letter(lx, ly, lw, lh, rows=7 if not ledger else 4, seed=seed))
    if ledger:
        for j in range(4):
            yy = ly + lh * (0.55 + j * 0.09)
            o.append(f'<path d="M{f(lx + lw * 0.62)} {f(yy)} L {f(lx + lw * 0.86)} {f(yy)}" stroke="#4A3020" stroke-width="{f(max(1.2, h / 160))}"></path>'
                     f'<path d="M{f(lx + lw * 0.1)} {f(yy)} L {f(lx + lw * 0.4)} {f(yy)}" stroke="#4A3020" stroke-width="{f(max(1.2, h / 160))}" stroke-dasharray="6 4"></path>')
        o.append(f'<path d="M{f(lx + lw * 0.6)} {f(ly + lh * 0.9)} L {f(lx + lw * 0.88)} {f(ly + lh * 0.9)}" stroke="#4A3020" stroke-width="2.4"></path>')
    else:                                                       # the large letters of his own hand at the foot
        o.append(f'<path d="M{f(lx + lw * 0.1)} {f(ly + lh * 0.88)} C {f(lx + lw * 0.2)} {f(ly + lh * 0.8)} {f(lx + lw * 0.3)} {f(ly + lh * 0.95)} {f(lx + lw * 0.44)} {f(ly + lh * 0.86)}" stroke="#2A1A10" stroke-width="{f(max(2.4, h / 90))}" fill="none"></path>')
    o.append('</g>')
    o.append(clay_lamp(w * 0.82, ty + h * 0.08, max(0.8, h / 260)) + inkpot(w * 0.74, ty + h * 0.22, max(0.8, h / 260)))
    k = min(w, h) / 360
    o.append(hand_pen(lx + lw * (0.6 if ledger else 0.42), ly + lh * (0.62 if ledger else 0.6), k))
    return "".join(o)
