"""Drawings for the Song of Solomon volume (chapter by chapter, added below), on top of Ecclesiastes' (ecc.art, which carries
chr2.art, chr1.art, kg2.art, kg1.art and 2 Samuel's drawings as K2).

Figures at a distance: the bride in a crimson robe (bride_fig), the beloved in a white tunic with a shepherd's staff
(beloved_fig; crowned=True for king Solomon in 3:11). The images of the song are landscapes, flowers and beasts: roe() a roe
or young hart (standing, grazing or leaping), dove(), flower() (rose, lily, henna, blossom), vine_rows(); and plates of
cells (plate()) for the likenesses — every one drawn as the thing named, never as a body."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ecc.art import *
from ecc.art import f, K2, K3, hgrad, tree, wind_lines, arc_pts, jar, loaf, flask, dog, lion_lying, scales
from genesis.art2 import fit, ground, hills, bird, birds, SKIN
from genesis.art3 import man, woman, sun, label, grid_bg, node, route, GREY_BEARD, STAFF, HOLD_STAFF
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as J1, judges2 as JG2, ruth1 as R1
import samuel1 as S1, samuel2 as S2, samuel3 as S3, samuel4 as S4, numbers1 as N, egypt as EG
from num.art import ALL
from sng import G

BRIDE_C, BELOVED_C = "#A82A4A", "#E8E2D6"

def bride_fig(p, x, y, s, flip=False, up=None):
    """The bride at a distance: a crimson robe, black hair, dark skin."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth=BRIDE_C, woman=True, hair="#0D0D0F", sw=3, flip=flip, up=up)

def beloved_fig(p, x, y, s, flip=False, up=None, staff=True, crowned=False):
    """The beloved at a distance: a white tunic, black hair, a shepherd's staff (crowned=True: the gold crown, no staff)."""
    extra = (S3.KING if crowned else "") + (STAFF if staff and not crowned else "")
    return mk.person(p, round(x), round(y), round(s, 3), body="#5A2A16", cloth=BELOVED_C if not crowned else "#7A1A2A", kind="Tunic", sw=3, flip=flip,
                     up=up or (HOLD_STAFF if staff and not crowned else None), extra=extra)

def roe(x, y, s=1.0, flip=False, hart=False, pose="stand", color="#B5743A"):
    """A roe (hart=True: a young hart with antlers) standing on (x, y), facing right; pose 'stand', 'graze' or 'leap'."""
    sx = -s if flip else s
    leg = {"stand": "M-30 -40 L -32 -14 L -36 18 M-22 -40 L -20 -14 L -22 18 M24 -40 L 22 -10 L 22 18 M30 -40 L 32 -10 L 36 18",
           "graze": "M-30 -40 L -32 -14 L -36 18 M-22 -40 L -20 -14 L -22 18 M24 -40 L 26 -10 L 24 18 M30 -40 L 34 -10 L 38 18",
           "leap": "M-30 -42 L -56 -30 L -82 -26 M-24 -42 L -50 -24 L -76 -18 M26 -44 L 46 -64 L 62 -52 M32 -42 L 54 -58 L 70 -44"}[pose]
    neck = "M28 -56 L 44 -86 L 56 -84 L 42 -50 Z" if pose != "graze" else "M28 -56 L 48 -30 L 58 -36 L 40 -60 Z"
    head = (52, -92) if pose != "graze" else (58, -28)
    hx, hy = head
    ant = (f'<path d="M{hx - 4} {hy - 8} L {hx - 10} {hy - 30} L {hx - 18} {hy - 38} M{hx - 10} {hy - 30} L {hx - 2} {hy - 40} M{hx + 2} {hy - 8} L {hx + 4} {hy - 30} L {hx + 12} {hy - 36}" '
           f'stroke="#5A3A22" stroke-width="3" fill="none" stroke-linecap="round"></path>') if hart else ""
    dy = -40 if pose == "leap" else -18
    return (f'<g transform="translate({f(x)} {f(y + dy * s)}) scale({f(sx)} {f(s)})' + (' rotate(-12)' if pose == "leap" else '') + '">'
            f'<path d="{leg}" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="{leg}" stroke="{color}" stroke-width="4" stroke-linecap="round"></path>'
            f'<path d="M-40 -48 C -40 -64 -20 -66 10 -64 C 30 -62 40 -56 36 -42 C 30 -34 -30 -32 -40 -48 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M-40 -54 L -48 -60 L -42 -48 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.2"></path>'
            f'<path d="{neck}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<ellipse cx="{hx}" cy="{hy}" rx="12" ry="8" fill="{color}" stroke="#0D0D0F" stroke-width="2" transform="rotate(20 {hx} {hy})"></ellipse>'
            f'<path d="M{hx - 6} {hy - 6} L {hx - 12} {hy - 18} L {hx - 2} {hy - 8} Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<circle cx="{hx + 3}" cy="{hy - 2}" r="1.8" fill="#0D0D0F"></circle>{ant}</g>')

def dove(x, y, s=1.0, flip=False, color="#E8E2D6"):
    """A dove perched, facing right; (x, y) its feet."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-26 -10 C -30 -24 -10 -34 8 -30 C 16 -40 30 -38 32 -28 L 40 -26 L 32 -22 C 30 -10 16 -2 0 -2 L -26 -2 L -40 4 L -36 -6 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
            f'<path d="M-16 -16 C -4 -24 10 -22 18 -16" stroke="#8A867E" stroke-width="2" fill="none"></path><circle cx="26" cy="-30" r="1.8" fill="#0D0D0F"></circle>'
            '<path d="M-2 -2 L -4 4 M6 -2 L 6 4" stroke="#C86A4A" stroke-width="2"></path></g>')

def flower(x, y, s=1.0, kind="rose", seed=1):
    """A flower on its stem, (x, y) where the stem meets the ground: rose (of Sharon), lily, henna (a pale cluster) or
    blossom (a white five-petal bloom)."""
    r = random.Random(seed)
    stem = f'<path d="M{f(x)} {f(y)} C {f(x - 4 * s)} {f(y - 30 * s)} {f(x + 4 * s)} {f(y - 60 * s)} {f(x)} {f(y - 80 * s)}" stroke="#3F7A44" stroke-width="{f(3 * s)}" fill="none"></path>'
    leaves = (f'<path d="M{f(x)} {f(y - 30 * s)} C {f(x + 14 * s)} {f(y - 40 * s)} {f(x + 24 * s)} {f(y - 36 * s)} {f(x + 28 * s)} {f(y - 44 * s)} C {f(x + 18 * s)} {f(y - 30 * s)} {f(x + 8 * s)} {f(y - 28 * s)} {f(x)} {f(y - 30 * s)} Z" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1.2"></path>'
              f'<path d="M{f(x)} {f(y - 50 * s)} C {f(x - 14 * s)} {f(y - 60 * s)} {f(x - 24 * s)} {f(y - 56 * s)} {f(x - 28 * s)} {f(y - 64 * s)} C {f(x - 18 * s)} {f(y - 50 * s)} {f(x - 8 * s)} {f(y - 48 * s)} {f(x)} {f(y - 50 * s)} Z" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1.2"></path>')
    cx, cy = x, y - 86 * s
    if kind == "rose":
        petals = "".join(f'<ellipse cx="{f(cx + 12 * s * math.cos(a))}" cy="{f(cy + 12 * s * math.sin(a))}" rx="{f(11 * s)}" ry="{f(9 * s)}" fill="#E8607A" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({math.degrees(a):.0f} {f(cx + 12 * s * math.cos(a))} {f(cy + 12 * s * math.sin(a))})"></ellipse>' for a in [k * 1.2566 for k in range(5)])
        head = petals + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(6 * s)}" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></circle>'
    elif kind == "lily":
        head = (f'<path d="M{f(cx)} {f(cy + 8 * s)} C {f(cx - 20 * s)} {f(cy)} {f(cx - 22 * s)} {f(cy - 16 * s)} {f(cx - 26 * s)} {f(cy - 24 * s)} C {f(cx - 12 * s)} {f(cy - 18 * s)} {f(cx - 6 * s)} {f(cy - 10 * s)} {f(cx)} {f(cy - 6 * s)} '
                f'C {f(cx + 6 * s)} {f(cy - 10 * s)} {f(cx + 12 * s)} {f(cy - 18 * s)} {f(cx + 26 * s)} {f(cy - 24 * s)} C {f(cx + 22 * s)} {f(cy - 16 * s)} {f(cx + 20 * s)} {f(cy)} {f(cx)} {f(cy + 8 * s)} Z" fill="#F8F6F0" stroke="#0D0D0F" stroke-width="1.6"></path>'
                f'<path d="M{f(cx)} {f(cy + 6 * s)} L {f(cx)} {f(cy - 26 * s)}" stroke="#F8F6F0" stroke-width="{f(9 * s)}" stroke-linecap="round"></path><path d="M{f(cx)} {f(cy - 26 * s)} L {f(cx)} {f(cy - 34 * s)}" stroke="#E8B830" stroke-width="{f(2 * s)}"></path>')
    elif kind == "henna":
        head = "".join(f'<circle cx="{f(cx + r.uniform(-16, 16) * s)}" cy="{f(cy + r.uniform(-14, 10) * s)}" r="{f(3.4 * s)}" fill="{r.choice(["#F8F0D0", "#F3E0A0", "#FFF8E8"])}" stroke="#8A7A4A" stroke-width="0.8"></circle>' for _ in range(18))
    else:
        petals = "".join(f'<circle cx="{f(cx + 7 * s * math.cos(a))}" cy="{f(cy + 7 * s * math.sin(a))}" r="{f(6 * s)}" fill="#FFF4F6" stroke="#C8A0A8" stroke-width="1"></circle>' for a in [k * 1.2566 for k in range(5)])
        head = petals + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(3 * s)}" fill="#E8607A"></circle>'
    return stem + leaves + head

def vine_rows(w, h, y0, y1, seed, rows=4, blossom=False, grapes=False):
    """Rows of vines on stakes across the ground between y0 and y1 (nearer rows lower and larger)."""
    r = random.Random(seed); o = []
    for k in range(rows):
        t = k / max(1, rows - 1); y = y0 + (y1 - y0) * t; sc = 0.5 + 0.7 * t; n = int(10 - 4 * t)
        o.append(f'<path d="M-10 {f(y - 18 * sc)} L {f(w + 10)} {f(y - 18 * sc)}" stroke="#5A3A22" stroke-width="{f(1.6 * sc)}"></path>')
        for i in range(n + 1):
            x = w * i / n + (k % 2) * w / n / 2
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 24 * sc)}" stroke="#5A3A22" stroke-width="{f(3 * sc)}"></path>'
                     f'<ellipse cx="{f(x)}" cy="{f(y - 24 * sc)}" rx="{f(22 * sc)}" ry="{f(12 * sc)}" fill="{r.choice(["#3F8A44", "#2E6A32", "#5E8F26"])}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
            if blossom:
                for _ in range(3):
                    o.append(f'<circle cx="{f(x + r.uniform(-16, 16) * sc)}" cy="{f(y - r.uniform(20, 32) * sc)}" r="{f(2.4 * sc)}" fill="#F8F0D0"></circle>')
            if grapes and r.random() < 0.6:
                o.append(f'<circle cx="{f(x + 8 * sc)}" cy="{f(y - 16 * sc)}" r="{f(4 * sc)}" fill="#5A1A6E" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    return "".join(o)

def plate(w, h, cells, cols=None, bg="#1A1430", line="#5A4A8A"):
    """A plate of cells: cells = [(svg in local units, about -60..60 each way, small label or "")]."""
    n = len(cells); cols = cols or (n if n <= 4 else math.ceil(n / 2))
    rows = math.ceil(n / cols)
    o = [grid_bg(w, h, color="#2A2A5A", bg=bg)]
    cw, ch = w / cols, h / rows
    s = min(cw, ch) / 150
    for i, (g, lab) in enumerate(cells):
        c, r_ = i % cols, i // cols
        x0, y0 = cw * c, ch * r_
        o.append(f'<rect x="{f(x0 + 5)}" y="{f(y0 + 5)}" width="{f(cw - 10)}" height="{f(ch - 10)}" fill="none" stroke="{line}" stroke-width="1.4"></rect>'
                 f'<g transform="translate({f(x0 + cw / 2)} {f(y0 + ch / 2 + (6 if lab else 0))})"><g transform="scale({f(s)})">{g}</g></g>')
        if lab: o.append(label(x0 + cw / 2, y0 + 20, lab, GOLD, max(8, min(10, cw / 14))))
    return "".join(o)

# ---- Song of Solomon 1 --------------------------------------------------------------------------------------------------
def vineyard_keeper(p, w, h, seed):
    """I am black, but comely, as the tents of Kedar, as the curtains of Solomon; they made me keeper of the vineyards: the
    bride among the vine rows under a scorching sun, the black tents of Kedar on the far hill at the left, Solomon's bright
    curtains on the right."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#FFF0C0"), sun(w * 0.5, h * 0.1, max(14, h * 0.08), color="#FFF4C2", op=0.5),
         hills(w, h, h * 0.36, seed, color="#C8A06A", amp=10, step=90)]
    for i in range(4):
        o.append(E4.tent(w * (0.06 + i * 0.07), h * 0.38, w * 0.08, h * 0.08, color="#1A1214", stripe="#3A2A2A"))
    for i in range(3):
        x = w * (0.72 + i * 0.09)
        o.append(f'<path d="M{f(x - w * 0.05)} {f(h * 0.4)} L {f(x)} {f(h * 0.28)} L {f(x + w * 0.05)} {f(h * 0.4)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 + "".join(f'<path d="M{f(x - w * 0.05 + q * w * 0.025)} {f(h * 0.4)} L {f(x)} {f(h * 0.28)}" stroke="#B5121B" stroke-width="2.4"></path>' for q in (1, 3)))
    o.append(ground(w, h, h * 0.42, "#B8A06A", dy=0) + vine_rows(w, h, h * 0.5, h * 0.98, seed, rows=4, grapes=True))
    s = fit(b, max(h * 0.42, b - 210))
    o.append(bride_fig(p, w * 0.42, b, s))
    return "".join(o)

def noon_flocks(p, w, h, seed):
    """Where thou makest it to rest at noon: the sun high, the flock lying in the shade of a great tree, the shepherds'
    tents beyond, the beloved standing by with his staff and the bride far off on the path."""
    r = random.Random(seed)
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3F0D8"), sun(w * 0.5, h * 0.06, max(12, h * 0.06), color="#FFF4C2", op=0.45),
         hills(w, h, h * 0.4, seed, color="#9AA06A", amp=12, step=90), ground(w, h, h * 0.48, "#C8B87A", dy=0)]
    for i in range(3):
        o.append(E4.tent(w * (0.66 + i * 0.1), h * 0.52, w * 0.1, h * 0.1, color="#3A2A22", stripe="#6A4A2A"))
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.82)}" rx="{f(w * 0.24)}" ry="{f(h * 0.08)}" fill="#6A7A3A" opacity="0.5"></ellipse>'
             + tree(w * 0.3, h * 0.82, min(1.4, h / 300), color="#3F7A44", seed=seed))
    for _ in range(9):
        x, y = w * r.uniform(0.12, 0.5), h * r.uniform(0.8, 0.92)
        o.append(E.sheep(x, y, min(0.5, h / 700), flip=r.random() < 0.5, wool=r.choice(["#E8E2D6", "#E8E2D6", "#3A2A22"])))
    s = fit(b, max(h * 0.42, b - 200))
    o.append(beloved_fig(p, w * 0.62, b, s) + bride_fig(p, w * 0.9, h * 0.62, fit(h * 0.62, h * 0.48), flip=True))
    return "".join(o)

def steed(w, h, seed):
    """I have compared thee, O my love, to a steed in Pharaoh's chariots; plaits of gold with studs of silver: a chariot
    horse of Egypt in its gold trappings on the left, a chain of gold plaits with silver studs on the right."""
    o = [sky(w, h, "#E8C890", "#F3E0B0"), sun(w * 0.86, h * 0.2, max(12, h * 0.06), color="#FFE680", op=0.35),
         EG.pyramid(w * 0.82, h * 0.7, w * 0.22, h * 0.3), ground(w, h, h * 0.7, "#D8B880", dy=0)]
    k = min(1.6, h / 220)
    o.append(E3.chariot(w * 0.36, h * 0.92, k * 0.9, color="#E8E2D6", driver="#B5652E"))
    cx, cy = w * 0.8, h * 0.84
    for i in range(9):
        a = math.radians(200 + i * 17.5); x = cx + w * 0.12 * math.cos(a); y = cy + h * 0.1 * math.sin(a) - h * 0.06
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(8 * k)}" ry="{f(5 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
                 + (f'<circle cx="{f(x)}" cy="{f(y + 6 * k)}" r="{f(3 * k)}" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="1"></circle>' if i % 2 else ""))
    return "".join(o)

def engedi(w, h, seed):
    """A cluster of henna-flowers in the vineyards of En-gedi: the terraced vineyards under the cliffs by the sea, henna
    bushes white with flower in the foreground."""
    r = random.Random(seed)
    o = [sky(w, h, "#E8B88A", "#F3E8C8"), f'<rect x="{f(w * 0.6)}" y="{f(h * 0.36)}" width="{f(w * 0.5)}" height="{f(h * 0.2)}" fill="#3A8AA8" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M-10 {f(h * 0.6)} L -10 {f(h * 0.12)} L {f(w * 0.2)} {f(h * 0.1)} L {f(w * 0.36)} {f(h * 0.2)} L {f(w * 0.52)} {f(h * 0.18)} L {f(w * 0.62)} {f(h * 0.4)} L {f(w * 0.64)} {f(h * 0.6)} Z" fill="#B5743A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for k in range(4):
        y = h * (0.26 + k * 0.08)
        o.append(f'<path d="M-10 {f(y)} L {f(w * (0.5 + k * 0.03))} {f(y + 4)}" stroke="#8A5A2A" stroke-width="2"></path>'
                 + "".join(f'<circle cx="{f(w * (0.02 + q * 0.06))}" cy="{f(y - 4)}" r="{f(5 + k)}" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1"></circle>' for q in range(int(8 + k * 0.5))))
    o.append(ground(w, h, h * 0.6, "#9CB86A", dy=0))
    for i in range(6):
        x = w * (0.08 + i * 0.17); y = h * (0.98 - (i % 2) * 0.05)
        for j in range(3):
            o.append(flower(x + (j - 1) * w * 0.03, y, min(0.9, h / 400), kind="henna", seed=seed + i * 3 + j))
    return "".join(o)

def bower(w, h, seed):
    """Our couch is green; the beams of our house are cedars, and our rafters are firs: a green bank under living cedars,
    fir boughs meeting overhead like rafters, two doves on a bough."""
    r = random.Random(seed)
    o = [sky(w, h, "#CFE8C8", "#F3F8E8"), ground(w, h, h * 0.72, "#7AAA4A", dy=0)]
    for x in (0.06, 0.3, 0.7, 0.94):
        o.append(f'<path d="M{f(w * x - 10)} {f(h + 10)} L {f(w * x - 6)} {f(h * 0.1)} L {f(w * x + 6)} {f(h * 0.1)} L {f(w * x + 10)} {f(h + 10)} Z" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></path>')
    for _ in range(26):
        x, y = r.uniform(-20, w + 20), r.uniform(-10, h * 0.22)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * r.uniform(0.07, 0.12))}" ry="{f(h * r.uniform(0.04, 0.07))}" fill="{r.choice(["#1F4A34", "#2E6A32", "#24503A"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    for x in (0.18, 0.82):
        o.append(f'<path d="M{f(w * x)} {f(h * 0.74)} L {f(w * x - w * 0.07)} {f(h * 0.74)} L {f(w * x)} {f(h * 0.3)} L {f(w * x + w * 0.07)} {f(h * 0.74)} Z" fill="#2E5A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    for _ in range(30):
        x, y = r.uniform(w * 0.04, w * 0.96), r.uniform(h * 0.91, h * 0.99)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="2.6" fill="{r.choice(["#FFD23F", "#F3EFE6", "#E85A7A"])}"></circle>')
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.82)} C {f(w * 0.4)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.74)} {f(w * 0.88)} {f(h * 0.82)} L {f(w * 0.88)} {f(h * 0.9)} L {f(w * 0.12)} {f(h * 0.9)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>')
    k = min(1.4, h / 260)
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.44)} L {f(w * 0.7)} {f(h * 0.4)}" stroke="#5A3A22" stroke-width="6"></path>' + dove(w * 0.46, h * 0.43, k) + dove(w * 0.56, h * 0.42, k, flip=True))
    return "".join(o)

def rose_lily(w, h, seed):
    """I am a rose of Sharon, a lily of the valleys; as a lily among thorns: a rose of Sharon in bloom on the left, and on
    the right a white lily standing among thorn branches."""
    r = random.Random(seed)
    o = [sky(w, h, "#CFE8C8", "#F8F0E0"), hills(w, h, h * 0.5, seed, color="#9CCB5E", amp=10, step=90), ground(w, h, h * 0.62, "#8AB05A", dy=0)]
    k = min(2.6, h / 120)
    o.append(flower(w * 0.28, h * 0.98, k, "rose", seed) + flower(w * 0.18, h * 0.98, k * 0.7, "rose", seed + 1))
    for _ in range(9):
        x0, y0 = w * r.uniform(0.56, 0.96), h * r.uniform(0.6, 0.98)
        a = r.uniform(-2.6, -0.5); L = w * r.uniform(0.08, 0.16)
        x1, y1 = x0 + L * math.cos(a), y0 + L * math.sin(a)
        o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#4A3A2A" stroke-width="3"></path>'
                 + "".join(f'<path d="M{f(x0 + (x1 - x0) * t)} {f(y0 + (y1 - y0) * t)} l {f(6 * math.cos(a + 1.2))} {f(6 * math.sin(a + 1.2))}" stroke="#4A3A2A" stroke-width="2"></path>' for t in (0.3, 0.55, 0.8)))
    o.append(flower(w * 0.76, h * 0.98, k * 1.05, "lily", seed))
    return "".join(o)

def apple_tree(p, w, h, seed):
    """As the apple-tree among the trees of the wood; he brought me to the banqueting-house, and his banner over me was
    love: an apple-tree red with fruit among the dark trees of the wood, its shade on the grass, and beyond it a pavilion
    with a crimson banner."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3F0D8"), ground(w, h, h * 0.6, "#8AB05A", dy=0)]
    for i in range(7):
        o.append(tree(w * (0.02 + i * 0.07) if i < 3 else w * (0.62 + (i - 3) * 0.1), h * (0.66 + (i % 2) * 0.03), min(0.9, h / 420), color="#1F4A34", kind="tall" if i % 2 else "round", seed=seed + i))
    tx, ty, k = w * 0.36, h * 0.94, min(1.6, h / 260)
    o.append(f'<ellipse cx="{f(tx)}" cy="{f(ty)}" rx="{f(w * 0.2)}" ry="{f(h * 0.04)}" fill="#4A6A2A" opacity="0.5"></ellipse>' + tree(tx, ty, k, color="#5E9F36", seed=seed))
    for _ in range(14):
        o.append(f'<circle cx="{f(tx + r.uniform(-40, 40) * k)}" cy="{f(ty - r.uniform(100, 150) * k)}" r="{f(5 * k)}" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    o.append(E4.tent(w * 0.8, h * 0.82, w * 0.22, h * 0.22, color="#E8D8B0", stripe="#B5121B")
             + f'<path d="M{f(w * 0.8)} {f(h * 0.6)} L {f(w * 0.8)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="4"></path><path d="M{f(w * 0.8)} {f(h * 0.3)} L {f(w * 0.92)} {f(h * 0.34)} L {f(w * 0.8)} {f(h * 0.4)} Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></path>')
    s = fit(ty, ty - h * 0.2)
    o.append(E.kneel(tx + 30 * k, ty, s, color=BRIDE_C, skin="#3A1E14", flip=True))
    return "".join(o)

def roes_field(w, h, seed):
    """By the roes, or by the hinds of the field: roes and hinds in a meadow at evening, one young hart looking up."""
    r = random.Random(seed)
    o = [sky(w, h, "#6A5A8A", "#F3C8A0"), sun(w * 0.8, h * 0.5, max(10, h * 0.05), color="#FFB04A", op=0.3), hills(w, h, h * 0.5, seed, color="#6A7A5A", amp=10, step=80),
         ground(w, h, h * 0.62, "#8AA05A", dy=0)]
    k = min(1.3, h / 230)
    for i, (x, y, pose, hart, fl) in enumerate(((0.2, 0.86, "graze", False, False), (0.42, 0.8, "stand", True, True), (0.62, 0.9, "graze", False, True), (0.84, 0.82, "stand", False, False))):
        o.append(roe(w * x, h * y, k * (0.8 + 0.2 * (y - 0.8) * 5), flip=fl, hart=hart, pose=pose, color=["#B5743A", "#A8682E", "#C8844A", "#B5743A"][i]))
    for _ in range(20):
        x, y = r.uniform(0, w), r.uniform(h * 0.66, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -3 -8 M{f(x)} {f(y)} l 3 -8" stroke="#5A7A3A" stroke-width="1.6"></path>')
    return "".join(o)

def leaping(w, h, seed):
    """The voice of my beloved! behold, he cometh, leaping upon the mountains; he standeth behind our wall, he looketh in at
    the windows: a young hart in mid-leap upon the hills, and in front the wall of the house with its lattice window."""
    o = [sky(w, h, "#8FD0E2", "#F3F0D8"), hills(w, h, h * 0.36, seed, color="#8A9A7A", amp=26, step=70), hills(w, h, h * 0.5, seed + 1, color="#7A9A5A", amp=18, step=90)]
    k = min(1.4, h / 240)
    o.append(roe(w * 0.4, h * 0.46, k * 0.9, hart=True, pose="leap"))
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(h * 0.44)}" width="{f(w * 0.5)}" height="{f(h * 0.6)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(w * 0.56)} {f(h * (0.5 + q * 0.08))} L {f(w + 10)} {f(h * (0.5 + q * 0.08))}" stroke="#A8906A" stroke-width="1.4"></path>' for q in range(6)))
    lx, ly, lw, lh = w * 0.7, h * 0.56, w * 0.16, h * 0.26
    o.append(f'<rect x="{f(lx)}" y="{f(ly)}" width="{f(lw)}" height="{f(lh)}" fill="#1A1214" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for i in range(1, 6):
        o.append(f'<path d="M{f(lx + lw * i / 6)} {f(ly)} L {f(lx + lw * i / 6)} {f(ly + lh)}" stroke="#8A5A30" stroke-width="3"></path>'
                 f'<path d="M{f(lx)} {f(ly + lh * i / 6)} L {f(lx + lw)} {f(ly + lh * i / 6)}" stroke="#8A5A30" stroke-width="3"></path>')
    o.append(ground(w, h, h * 0.96, "#9CB86A", dy=0))
    return "".join(o)

def spring(w, h, seed):
    """For, lo, the winter is past; the flowers appear on the earth; the time of the singing of birds is come, and the
    voice of the turtle-dove is heard; the fig-tree ripeneth her green figs, and the vines are in blossom: the last rain
    clouds going off to the right, a field of flowers, a fig-tree with green figs, vines in blossom, birds, and a turtle-dove."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3F8E8"), sun(w * 0.2, h * 0.16, max(12, h * 0.06), color="#FFE680", op=0.4)]
    for i in range(3):
        o.append(f'<ellipse cx="{f(w * (0.84 + i * 0.08))}" cy="{f(h * (0.12 + i * 0.04))}" rx="{f(w * 0.1)}" ry="{f(h * 0.06)}" fill="#8A9AAA" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(hills(w, h, h * 0.42, seed, color="#9CCB5E", amp=12, step=90) + ground(w, h, h * 0.5, "#8AC05A", dy=0))
    o.append(vine_rows(w * 0.5, h, h * 0.58, h * 0.72, seed, rows=2, blossom=True).replace("M-10", "M0"))
    fx, fy, k = w * 0.74, h * 0.82, min(1.3, h / 300)
    o.append(f'<path d="M{f(fx)} {f(fy)} C {f(fx - 6)} {f(fy - 60 * k)} {f(fx + 10)} {f(fy - 90 * k)} {f(fx)} {f(fy - 110 * k)}" stroke="#7A6A5A" stroke-width="{f(10 * k)}" fill="none"></path>')
    for _ in range(9):
        lx, ly = fx + r.uniform(-60, 60) * k, fy - r.uniform(90, 150) * k
        o.append(f'<path d="M{f(lx)} {f(ly)} l {f(-16 * k)} {f(-10 * k)} l {f(8 * k)} {f(-12 * k)} l {f(8 * k)} {f(6 * k)} l {f(8 * k)} {f(-6 * k)} l {f(8 * k)} {f(12 * k)} Z" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1.2"></path>')
    for _ in range(8):
        o.append(f'<circle cx="{f(fx + r.uniform(-50, 50) * k)}" cy="{f(fy - r.uniform(90, 140) * k)}" r="{f(5 * k)}" fill="#8AC05A" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append(f'<path d="M{f(fx)} {f(fy - 100 * k)} L {f(fx + 40 * k)} {f(fy - 116 * k)}" stroke="#7A6A5A" stroke-width="{f(4 * k)}"></path>' + dove(fx + 34 * k, fy - 116 * k, k * 0.9, color="#B8A8A0"))
    for _ in range(50):
        x, y = r.uniform(0, w), r.uniform(h * 0.76, h)
        c = r.choice(["#FFD23F", "#F3EFE6", "#E85A7A", "#C2456A", "#8A6AE0"])
        o.append(f'<path d="M{f(x)} {f(y)} l 0 -8" stroke="#3F7A44" stroke-width="1.6"></path><circle cx="{f(x)}" cy="{f(y - 9)}" r="3.4" fill="{c}" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    o.append(birds(6, w * 0.3, w * 0.7, h * 0.08, h * 0.3, seed))
    return "".join(o)

def dove_rock(w, h, seed):
    """O my dove, that art in the clefts of the rock, in the covert of the steep place: a sheer cliff of rock with a cleft,
    and a white dove sheltering in it."""
    o = [sky(w, h, "#8FD0E2", "#E8F6FA"), f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.26)} -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h + 10)} Z" fill="#A8806A" stroke="#0D0D0F" stroke-width="2.6"></path>']
    for k in range(6):
        o.append(f'<path d="M{f(w * (0.3 + k * 0.12))} -10 L {f(w * (0.28 + k * 0.12))} {f(h + 10)}" stroke="#8A6450" stroke-width="2"></path>')
    cx, cy = w * 0.58, h * 0.56
    o.append(f'<path d="M{f(cx - w * 0.1)} {f(cy + h * 0.08)} C {f(cx - w * 0.08)} {f(cy - h * 0.16)} {f(cx + w * 0.08)} {f(cy - h * 0.2)} {f(cx + w * 0.1)} {f(cy + h * 0.08)} Z" fill="#3A2420" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + dove(cx, cy + h * 0.06, min(2.0, h / 140)))
    return "".join(o)

def foxes(w, h, seed):
    """Take us the foxes, the little foxes, that spoil the vineyards; for our vineyards are in blossom: little foxes
    running between the blossoming vine rows."""
    o = [sky(w, h, "#8FD0E2", "#F3F0D8"), hills(w, h, h * 0.3, seed, color="#9AA06A", amp=10, step=90), ground(w, h, h * 0.36, "#B8A06A", dy=0),
         vine_rows(w, h, h * 0.46, h * 0.98, seed, rows=4, blossom=True)]
    k = min(1.4, h / 260)
    o.append(JG2.fox(w * 0.3, h * 0.84, k, brand=False) + JG2.fox(w * 0.66, h * 0.7, k * 0.8, flip=True, brand=False) + JG2.fox(w * 0.84, h * 0.94, k * 1.1, brand=False))
    return "".join(o)

def lilies_flock(p, w, h, seed):
    """He feedeth his flock among the lilies; until the day be cool, and the shadows flee away, be thou like a roe upon the
    mountains of Bether: the flock grazing in a valley of lilies at evening, long shadows, and a hart on the far mountains."""
    r = random.Random(seed)
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A7A", "#F3B880"), sun(w * 0.12, h * 0.46, max(10, h * 0.05), color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.36, seed, color="#5A4A6A", amp=30, step=70), hills(w, h, h * 0.5, seed + 1, color="#6A6A5A", amp=14, step=90), ground(w, h, h * 0.6, "#8A9A5A", dy=0)]
    o.append(roe(w * 0.7, h * 0.41, min(0.7, h / 500), hart=True, color="#2A1E2A"))
    for _ in range(14):
        o.append(flower(w * r.uniform(0.02, 0.98), h * r.uniform(0.7, 1.0), min(0.5, h / 600), "lily", seed))
    for _ in range(7):
        x, y = w * r.uniform(0.1, 0.6), h * r.uniform(0.72, 0.9)
        o.append(f'<ellipse cx="{f(x + 30)}" cy="{f(y)}" rx="40" ry="5" fill="#4A5A2A" opacity="0.5"></ellipse>' + E.sheep(x, y, min(0.5, h / 700)))
    s = fit(b, max(h * 0.42, b - 200))
    o.append(f'<path d="M{f(w * 0.78)} {f(b)} L {f(w * 0.98)} {f(b + 8)} L {f(w * 0.98)} {f(b + 16)} Z" fill="#3A3A2A" opacity="0.5"></path>' + beloved_fig(p, w * 0.78, b, s))
    return "".join(o)
