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

BRIDE_C, BELOVED_C = "#8A1A3A", "#E8E2D6"

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

# ---- Song of Solomon 3 --------------------------------------------------------------------------------------------------
def _cut(ref, a, b=None, after=None): return G.v(ref, frm=a, to=b or a, after=after)

def night_streets(p, w, h, seed):
    """By night I sought him; I will go about the city, in the streets and in the broad ways; the watchmen that go about the
    city found me: the city at night, the watchmen with torches on the wall, the bride small in the empty street below."""
    o = [mk.defs(p, *ALL), city_night(w, h, seed)]
    for i, x in enumerate((0.2, 0.62)):
        o.append(J1.torchbearer(p, w * x, h * 0.9 - 12, fit(h * 0.9, h * 0.76), flip=i == 1, seed=seed + i))
    o.append(f'<rect x="-10" y="{f(h * 0.94)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3040"></rect>' + bride_fig(p, w * 0.84, h * 0.995, fit(h, h * 0.86), flip=True))
    return "".join(o)

def litter(p, w, h, seed):
    """Who is this that cometh up from the wilderness like pillars of smoke? Behold, it is the litter of Solomon; threescore
    mighty men are about it, every man hath his sword upon his thigh: columns of incense smoke over the wilderness, the
    curtained litter on its bearers' shoulders, mighty men before and behind it."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8A06A", "#F3E0B0"), hills(w, h, h * 0.5, seed, color="#B8906A", amp=12, step=90), ground(w, h, h * 0.58, "#D8B880", dy=0)]
    for k in range(5):
        x = w * (0.3 + k * 0.1)
        o.append(f'<path d="M{f(x)} {f(h * 0.66)} C {f(x - 30)} {f(h * 0.46)} {f(x + 30)} {f(h * 0.3)} {f(x - 10 + k * 6)} {f(-10)}" stroke="#E8E2E6" stroke-width="{f(18 + k * 3)}" fill="none" opacity="0.45" stroke-linecap="round"></path>')
    s = fit(b, max(h * 0.4, b - 200))
    lx = w * 0.5
    for dx in (-60, 60):
        o.append(man(p, lx + dx * s, b, s * 0.9, "#8A5A30", up=[(-22, -158), (-22, -176), (-14, -190)]))
    o.append(f'<path d="M{f(lx - 110 * s)} {f(b - 176 * s)} L {f(lx + 110 * s)} {f(b - 176 * s)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>'
             f'<rect x="{f(lx - 60 * s)}" y="{f(b - 260 * s)}" width="{f(120 * s)}" height="{f(84 * s)}" fill="#7A2A6A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(lx - 70 * s)} {f(b - 260 * s)} L {f(lx)} {f(b - 300 * s)} L {f(lx + 70 * s)} {f(b - 260 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(lx + q * s)} {f(b - 260 * s)} L {f(lx + q * s)} {f(b - 176 * s)}" stroke="#C8C8D0" stroke-width="{f(4 * s)}"></path>' for q in (-56, 56)))
    for i in range(5):
        o.append(warrior(p, w * (0.04 + i * 0.07), b - (i % 2) * 6, s * 0.86, WAR[i % 4]) + warrior(p, w * (0.96 - i * 0.07), b - (i % 2) * 6, s * 0.86, WAR[(i + 1) % 4]))
    return "".join(o)

PALANQUIN = [_cut("3:9", "wood of Lebanon"), _cut("3:10", "silver"), _cut("3:10", "gold"), _cut("3:10", "purple")]
def palanquin(w, h, seed=1):
    """King Solomon made himself a palanquin of the wood of Lebanon; the pillars of silver, the bottom of gold, the seat of
    purple: a blueprint elevation with its parts named."""
    o = [bp(w, h)]
    cx, base = w * 0.5, h * 0.84; pw, ph = min(w * 0.5, h * 0.9), h * 0.66
    x0, x1, top = cx - pw / 2, cx + pw / 2, base - ph
    o.append(f'<rect x="{f(x0 - 20)}" y="{f(base - ph * 0.16)}" width="{f(pw + 40)}" height="{f(ph * 0.16)}" fill="#E8B830" fill-opacity="0.25" stroke="#FFD23F" stroke-width="2"></rect>'
             f'<rect x="{f(x0 + pw * 0.18)}" y="{f(base - ph * 0.36)}" width="{f(pw * 0.64)}" height="{f(ph * 0.2)}" fill="#7A2A6A" fill-opacity="0.5" stroke="#C88AE0" stroke-width="2"></rect>'
             f'<path d="M{f(x0 - 30)} {f(top + ph * 0.12)} L {f(cx)} {f(top - ph * 0.04)} L {f(x1 + 30)} {f(top + ph * 0.12)} Z" fill="none" stroke="{CYAN}" stroke-width="2.4"></path>')
    for x in (x0, x1):
        o.append(f'<rect x="{f(x - 7)}" y="{f(top + ph * 0.12)}" width="14" height="{f(ph * 0.72)}" fill="#E8E8F0" fill-opacity="0.35" stroke="#E8E8F0" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(x0 - 70)} {f(base - ph * 0.08)} L {f(x1 + 70)} {f(base - ph * 0.08)}" stroke="{CYAN}" stroke-width="3"></path>')
    names = [n.upper() for n in PALANQUIN]
    o.append(tag(cx, top + ph * 0.04, names[0], x1 + 40, top - 4, color=CYAN) + tag(x1, top + ph * 0.4, names[1], x1 + 40, top + ph * 0.36, color="#E8E8F0")
             + tag(cx + pw * 0.3, base - ph * 0.08, names[2], x1 + 40, base - ph * 0.02, color=GOLD) + tag(cx - pw * 0.2, base - ph * 0.26, names[3], x0 - 40, base - ph * 0.4, color="#C88AE0"))
    return "".join(o)

def crowned(p, w, h, seed):
    """Go forth, O ye daughters of Zion, and behold king Solomon, with the crown wherewith his mother hath crowned him in the
    day of his espousals: the king crowned before his gate, the daughters of Zion coming out to behold him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), S4.gatehouse(w * 0.3, h * 0.84, w * 0.5, h * 0.6), ground(w, h, h * 0.84, "#C8B88A", dy=0)]
    s = fit(b, max(h * 0.42, b - 210))
    o.append(beloved_fig(p, w * 0.3, b, s, crowned=True))
    cl = ["#3A5AAA", "#2A7A7A", "#C2456A", "#E8A317", "#7A3BA8"]
    for i in range(5):
        o.append(woman(p, w * (0.56 + i * 0.09), b - (i % 2) * 6, s * 0.92, cl[i], flip=True))
    return "".join(o)

# ---- Song of Solomon 4 --------------------------------------------------------------------------------------------------
def _goats(n, x0, x1, y0, y1, seed, color="#2A2220"):
    r = random.Random(seed)
    return "".join(E.sheep(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(0.3, 0.45), flip=r.random() < 0.5, wool=color, face="#1A1210") for _ in range(n))

CELL = {
  "dove_veil": '<path d="M-60 -60 L 60 -60 L 60 60 L -60 60 Z" fill="#E8E2F0" opacity="0.35"></path>' + dove(0, 20, 1.6) + "".join(f'<path d="M{x} -60 L {x} 60" stroke="#F3EFE6" stroke-width="1.2" opacity="0.7"></path>' for x in range(-56, 60, 10)),
  "gilead": '<path d="M-64 50 L -40 -20 L 0 -44 L 30 -10 L 64 30 L 64 50 Z" fill="#7A8A4A" stroke="#E8C88A" stroke-width="2"></path>' + _goats(8, -40, 40, -10, 34, 3),
  "ewes": '<ellipse cx="0" cy="40" rx="60" ry="12" fill="#2C9DB8" stroke="#8FD0E2" stroke-width="2"></ellipse>' + "".join(E.sheep(x, y, 0.45, flip=x > 0) for x, y in ((-40, 20), (-20, 22), (14, 14), (34, 16), (-6, 0), (20, -4))),
  "scarlet": '<path d="M-60 -30 C -30 -50 -10 -10 20 -30 C 40 -44 50 -36 60 -40" stroke="#B5121B" stroke-width="5" fill="none"></path>'
             '<path d="M-30 50 A 40 40 0 0 1 50 50 Z" fill="#E86A6A" stroke="#0D0D0F" stroke-width="2"></path><path d="M-24 50 A 34 34 0 0 1 44 50 Z" fill="#F3D8D0" stroke="#0D0D0F" stroke-width="1.4"></path>'
             + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#B5121B" stroke="#0D0D0F" stroke-width="0.8"></circle>' for x, y in ((-10, 40), (0, 30), (10, 36), (20, 26), (24, 42), (4, 44), (-14, 46), (32, 44))),
  "tower": '<rect x="-24" y="-60" width="48" height="120" fill="#C8B08A" stroke="#E8C88A" stroke-width="2"></rect><path d="M-30 -60 L -30 -70 L -18 -70 L -18 -64 L -6 -64 L -6 -70 L 6 -70 L 6 -64 L 18 -64 L 18 -70 L 30 -70 L 30 -60 Z" fill="#C8B08A" stroke="#E8C88A" stroke-width="2"></path>'
           + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="#B87333" stroke="#0D0D0F" stroke-width="1.6"></circle>' for x in (-14, 0, 14) for y in (-40, -16, 8, 32)),
  "fawns": '<path d="M-64 54 L 64 54" stroke="#9CCB5E" stroke-width="4"></path>' + roe(-22, 50, 0.55, flip=False, color="#C8844A") + roe(22, 50, 0.55, flip=True, color="#C8844A")
           + "".join(flower(x, 56, 0.4, "lily") for x in (-56, -2, 50)),
}

def likeness(w, h, keys):
    """A plate of the likenesses (CELL keys), each drawn as the thing named."""
    return plate(w, h, [(CELL[k], "") for k in keys], cols=len(keys))

def myrrh_hill(w, h, seed):
    """Until the day be cool, and the shadows flee away, I will get me to the mountain of myrrh, and to the hill of
    frankincense: two hills at evening, thin smoke of myrrh and frankincense rising from them, the shadows long."""
    o = [sky(w, h, "#5A4A7A", "#F3B880"), sun(w * 0.86, h * 0.6, max(10, h * 0.05), color="#FF8A3D", op=0.3)]
    for x, c in ((0.3, "#8A6A5A"), (0.68, "#A8906A")):
        o.append(f'<path d="M{f(w * x - w * 0.3)} {f(h * 0.86)} C {f(w * x - w * 0.1)} {f(h * 0.3)} {f(w * x + w * 0.1)} {f(h * 0.3)} {f(w * x + w * 0.3)} {f(h * 0.86)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2.4"></path>')
        for k in range(3):
            o.append(f'<path d="M{f(w * x + (k - 1) * 14)} {f(h * 0.4)} C {f(w * x - 20 + k * 10)} {f(h * 0.3)} {f(w * x + 20)} {f(h * 0.2)} {f(w * x + (k - 1) * 20)} {f(h * 0.04)}" stroke="#F3EFE6" stroke-width="5" fill="none" opacity="0.5"></path>')
    o.append(ground(w, h, h * 0.84, "#5A4A4A", dy=0) + f'<path d="M{f(w * 0.3)} {f(h * 0.86)} L {f(-10)} {f(h * 0.98)} L {f(-10)} {f(h * 0.9)} Z" fill="#2A1E2A" opacity="0.5"></path>')
    return "".join(o)

PEAKS = [_cut("4:8", "Lebanon"), _cut("4:8", "Amana"), _cut("4:8", "Senir"), _cut("4:8", "Hermon")]
def leopard(x, y, s=1.0, flip=False):
    """A leopard lying along a rock, spotted, its tail hanging."""
    sx = -s if flip else s
    spots = "".join(f'<circle cx="{dx}" cy="{dy}" r="3" fill="#3A2A1A"></circle>' for dx, dy in ((-60, -30), (-40, -36), (-20, -30), (0, -36), (20, -30), (-50, -18), (-30, -20), (-10, -20), (10, -20), (30, -22)))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-80 0 C -86 -30 -60 -44 -20 -44 L 40 -42 C 60 -40 66 -20 62 0 Z" fill="#D8A040" stroke="#0D0D0F" stroke-width="2.2"></path>{spots}'
            '<path d="M-80 -6 C -96 0 -100 20 -94 36" stroke="#0D0D0F" stroke-width="7" fill="none"></path><path d="M-80 -6 C -96 0 -100 20 -94 36" stroke="#D8A040" stroke-width="4" fill="none"></path>'
            '<circle cx="64" cy="-30" r="16" fill="#D8A040" stroke="#0D0D0F" stroke-width="2"></circle><path d="M56 -44 L 58 -52 L 64 -46 M70 -44 L 74 -52 L 76 -42" fill="#D8A040" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<circle cx="70" cy="-32" r="2" fill="#0D0D0F"></circle><path d="M40 0 L 90 0 L 90 -6 L 44 -8 Z" fill="#D8A040" stroke="#0D0D0F" stroke-width="1.6"></path></g>')

def lebanon_peaks(w, h, seed):
    """Come with me from Lebanon; look from the top of Amana, from the top of Senir and Hermon, from the lions' dens, from the
    mountains of the leopards: the snowy ranges named one by one, a lion at the mouth of its den, a leopard on a ledge."""
    o = [sky(w, h, "#8FB8D8", "#E8F0F8")]
    for i, (x, hh) in enumerate(((0.14, 0.3), (0.38, 0.18), (0.62, 0.26), (0.86, 0.12))):
        px, py = w * x, h * hh
        o.append(f'<path d="M{f(px - w * 0.2)} {f(h * 0.7)} L {f(px)} {f(py)} L {f(px + w * 0.2)} {f(h * 0.7)} Z" fill="#6A7A8A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<path d="M{f(px - w * 0.05)} {f(py + (h * 0.7 - py) * 0.25)} L {f(px)} {f(py)} L {f(px + w * 0.05)} {f(py + (h * 0.7 - py) * 0.25)} L {f(px + w * 0.02)} {f(py + (h * 0.7 - py) * 0.2)} L {f(px - w * 0.02)} {f(py + (h * 0.7 - py) * 0.26)} Z" fill="#F3F8FA"></path>'
                 + label(px, py - 8, PEAKS[i].upper(), "#1A2A3A", max(8, min(11, w / 70))))
    o.append(ground(w, h, h * 0.7, "#7A8A6A", dy=0))
    k = min(1.2, h / 260)
    o.append(f'<path d="M{f(w * 0.04)} {f(h + 10)} L {f(w * 0.04)} {f(h * 0.76)} Q {f(w * 0.16)} {f(h * 0.64)} {f(w * 0.28)} {f(h * 0.76)} L {f(w * 0.28)} {f(h + 10)} Z" fill="#4A4A4A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.1)} {f(h + 10)} L {f(w * 0.1)} {f(h * 0.84)} Q {f(w * 0.16)} {f(h * 0.78)} {f(w * 0.22)} {f(h * 0.84)} L {f(w * 0.22)} {f(h + 10)} Z" fill="#1A1214"></path>'
             + JG2.lion(w * 0.16, h * 0.99, k * 0.6, roar=False))
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.86)} L {f(w * 0.96)} {f(h * 0.86)} L {f(w * 0.96)} {f(h + 10)} L {f(w * 0.56)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.2"></path>' + leopard(w * 0.76, h * 0.86, k * 0.7))
    return "".join(o)

def honey_milk(w, h, seed):
    """Thy lips drop as the honeycomb; honey and milk are under thy tongue; the smell of thy garments is like the smell of
    Lebanon; one chain of thy neck: a still life — a honeycomb dripping, a jar of milk, a sprig of cedar and a gold chain."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A2A"></rect>', f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(2.6, h / 200, w / 260)
    hx, hy = w * 0.28, h * 0.72
    for row in range(4):
        for col in range(5 - row % 2):
            x = hx + (col - 2) * 18 * k + (row % 2) * 9 * k; y = hy - 20 * k - row * 15 * k
            o.append(f'<path d="M{f(x - 9 * k)} {f(y)} L {f(x - 4.5 * k)} {f(y - 8 * k)} L {f(x + 4.5 * k)} {f(y - 8 * k)} L {f(x + 9 * k)} {f(y)} L {f(x + 4.5 * k)} {f(y + 8 * k)} L {f(x - 4.5 * k)} {f(y + 8 * k)} Z" fill="#E8B830" stroke="#8A5A10" stroke-width="1.4"></path>')
    for dx in (-20, 6, 30):
        o.append(f'<path d="M{f(hx + dx * k)} {f(hy - 12 * k)} c 3 8 3 14 0 18 c -3 -4 -3 -10 0 -18 Z" fill="#FFC14D" stroke="#8A5A10" stroke-width="1"></path>')
    o.append(jar(w * 0.56, h * 0.74, k * 1.1, "#F3EFE6") + f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.74 - 60 * k * 1.1)}" rx="{f(9 * k)}" ry="{f(3 * k)}" fill="#FFFFFF"></ellipse>')
    o.append(f'<g transform="translate({f(w * 0.8)} {f(h * 0.7 - 50 * k * 0.8)}) scale({f(k * 0.8)})">{CELL["cedars"]}</g>')
    for i in range(10):
        a = math.radians(200 + i * 14); x = w * 0.5 + w * 0.1 * math.cos(a); y = h * 0.96 + h * 0.06 * math.sin(a)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(6 * k)}" ry="{f(4 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(2.4 * k)}"></ellipse>')
    return "".join(o)

def garden_shut(w, h, seed):
    """A garden shut up, a spring shut up, a fountain sealed; a well of living waters, and flowing streams from Lebanon: a
    walled garden of pomegranates with its gate shut, a sealed well-head within, and streams coming down from the snowy
    mountains behind."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3F8E8"), f'<path d="M-10 {f(h * 0.4)} L {f(w * 0.2)} {f(h * 0.08)} L {f(w * 0.4)} {f(h * 0.3)} L {f(w * 0.6)} {f(h * 0.04)} L {f(w * 0.84)} {f(h * 0.32)} L {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.5)} L -10 {f(h * 0.5)} Z" fill="#7A8A9A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.16)} {f(h * 0.14)} L {f(w * 0.2)} {f(h * 0.08)} L {f(w * 0.24)} {f(h * 0.14)} Z M{f(w * 0.56)} {f(h * 0.1)} L {f(w * 0.6)} {f(h * 0.04)} L {f(w * 0.64)} {f(h * 0.1)} Z" fill="#F3F8FA"></path>',
         ground(w, h, h * 0.5, "#8AB05A", dy=0)]
    for x in (0.3, 0.62):
        o.append(f'<path d="M{f(w * x)} {f(h * 0.3)} C {f(w * x - 20)} {f(h * 0.4)} {f(w * x + 20)} {f(h * 0.5)} {f(w * x)} {f(h * 0.6)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>')
    wx0, wx1, wy = w * 0.08, w * 0.92, h * 0.6
    o.append(f'<rect x="{f(wx0)}" y="{f(wy)}" width="{f(wx1 - wx0)}" height="{f(h * 0.4)}" fill="#7AAA4A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(wx0 - 6)}" y="{f(wy - h * 0.05)}" width="{f(wx1 - wx0 + 12)}" height="{f(h * 0.05)}" fill="#A8906A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(wx0 + (wx1 - wx0) * q / 14)} {f(wy - h * 0.05)} L {f(wx0 + (wx1 - wx0) * q / 14)} {f(wy)}" stroke="#7A6A4A" stroke-width="1.4"></path>' for q in range(1, 14)))
    for _ in range(12):
        tx, ty = r.uniform(wx0 + 30, wx1 - 30), r.uniform(h * 0.7, h * 0.86)
        o.append(tree(tx, ty, min(0.4, h / 900), color="#2E6A32", seed=r.randint(1, 99))
                 + "".join(f'<circle cx="{f(tx + r.uniform(-14, 14))}" cy="{f(ty - r.uniform(40, 56) * min(0.4, h / 900) * 2.5)}" r="3.4" fill="#D7261E" stroke="#0D0D0F" stroke-width="0.8"></circle>' for _ in range(3)))
    o.append(f'<path d="M{f(wx0)} {f(wy)} L {f(wx0)} {f(h + 10)} M{f(wx1)} {f(wy)} L {f(wx1)} {f(h + 10)}" stroke="#A8906A" stroke-width="12"></path>'
             f'<rect x="{f(wx0 - 6)}" y="{f(h * 0.9)}" width="{f(wx1 - wx0 + 12)}" height="{f(h * 0.12)}" fill="#A8906A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.46)}" y="{f(h * 0.84)}" width="{f(w * 0.08)}" height="{f(h * 0.18)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.46)} {f(h * 0.92)} L {f(w * 0.54)} {f(h * 0.92)}" stroke="#2A1A10" stroke-width="5"></path>')
    wx, wy2 = w * 0.74, h * 0.8
    o.append(f'<ellipse cx="{f(wx)}" cy="{f(wy2)}" rx="{f(w * 0.06)}" ry="{f(h * 0.025)}" fill="#A89A8A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<rect x="{f(wx - w * 0.06)}" y="{f(wy2)}" width="{f(w * 0.12)}" height="{f(h * 0.05)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<circle cx="{f(wx)}" cy="{f(wy2 - 2)}" r="{f(h * 0.012 + 3)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

SPICES = [_cut("4:13", "pomegranates"), _cut("4:13", "Henna"), _cut("4:14", "Spikenard"), _cut("4:14", "saffron"), _cut("4:14", "Calamus"),
          _cut("4:14", "cinnamon"), _cut("4:14", "frankincense"), _cut("4:14", "Myrrh"), _cut("4:14", "aloes")]
def spices(w, h, seed=1):
    """An orchard of pomegranates, henna with spikenard, saffron, calamus and cinnamon, frankincense, myrrh and aloes: a plate
    of nine cells, each plant with its name."""
    def pom():
        return tree(0, 50, 0.6, color="#2E6A32", seed=4) + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#D7261E" stroke="#0D0D0F" stroke-width="1"></circle>' for x, y in ((-14, -20), (10, -14), (0, -30), (20, -28)))
    def reed(c, n=5, head=None):
        return "".join(f'<path d="M{-20 + i * 10} 50 L {-22 + i * 11} -30" stroke="{c}" stroke-width="4"></path>' + (head(-22 + i * 11, -30) if head else "") for i in range(n))
    cells = [pom(), flower(0, 54, 0.9, "henna", 2) + flower(-24, 54, 0.7, "henna", 3) + flower(24, 54, 0.7, "henna", 4),
             reed("#6A7A3A", head=lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="5" ry="12" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1"></ellipse>'),
             "".join(f'<path d="M{x} 50 L {x} 0" stroke="#5A8A3A" stroke-width="3"></path><path d="M{x} 0 C {x - 14} -14 {x - 10} -30 {x} -34 C {x + 10} -30 {x + 14} -14 {x} 0 Z" fill="#9A6AD0" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M{x} -10 L {x - 6} -26 M{x} -10 L {x + 6} -26" stroke="#E86A1E" stroke-width="2.4"></path>' for x in (-26, 0, 26)),
             reed("#7A9A4A", 6),
             "".join(f'<rect x="{-30 + i * 14}" y="-40" width="10" height="90" rx="5" fill="#A8603A" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(5)),
             tree(0, 50, 0.55, color="#7A8A5A", seed=6) + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#F3E8C0" stroke="#0D0D0F" stroke-width="0.8"></circle>' for x, y in ((-10, -10), (12, -18), (0, -40), (18, -2))),
             tree(0, 50, 0.55, color="#6A6A3A", seed=8) + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#B5652E" stroke="#0D0D0F" stroke-width="0.8"></circle>' for x, y in ((-12, -14), (10, -22), (2, -36))),
             "".join(f'<path d="M{x} 50 C {x - 6} 0 {x + 6} -20 {x} -40" stroke="#3F7A44" stroke-width="5" fill="none"></path><path d="M{x} -40 l -10 -14 M{x} -40 l 10 -14 M{x} -20 l -14 -8 M{x} -20 l 14 -8" stroke="#3F7A44" stroke-width="4"></path>' for x in (-20, 20))]
    return plate(w, h, [(c, n.upper()) for c, n in zip(cells, SPICES)], cols=9 if w / h > 3.2 else (5 if w / h > 1.2 else 3))

def winds_garden(p, w, h, seed):
    """Awake, O north wind; and come, thou south; blow upon my garden; let my beloved come into his garden: the winds from
    north and south blowing over the walled garden, the scents streaming out, the beloved at the open gate."""
    o = [mk.defs(p, *ALL), garden_shut(w, h, seed).replace('fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></rect>', 'fill="#1A1214" stroke="#0D0D0F" stroke-width="2.4"></rect>', 1)]
    o.append(route([(w * 0.02, h * 0.2), (w * 0.2, h * 0.36), (w * 0.36, h * 0.56)], color="#F3EFE6", sw=3, dash="10 6")
             + route([(w * 0.98, h * 0.24), (w * 0.8, h * 0.4), (w * 0.64, h * 0.58)], color="#FFD23F", sw=3, dash="10 6")
             + label(w * 0.06, h * 0.16, "N", "#F3EFE6", 12) + label(w * 0.94, h * 0.2, "S", "#FFD23F", 12))
    for k in range(4):
        x = w * (0.3 + k * 0.12)
        o.append(f'<path d="M{f(x)} {f(h * 0.64)} C {f(x + 10)} {f(h * 0.56)} {f(x - 10)} {f(h * 0.5)} {f(x + 16)} {f(h * 0.42)}" stroke="#F3D8E8" stroke-width="4" fill="none" opacity="0.7"></path>')
    s = fit(h * 0.99, h * 0.8)
    o.append(beloved_fig(p, w * 0.5, h * 0.99, s))
    return "".join(o)

# ---- Song of Solomon 5 --------------------------------------------------------------------------------------------------
def door_night(w, h, seed):
    """My beloved knocketh, my head is filled with dew; he put in his hand by the hole of the door; my fingers with liquid
    myrrh upon the handles of the bolt: the inside of a door by night, moonlight through the hole above the bolt, myrrh
    dripping from the bolt's handles, a lamp and a garment on its peg."""
    from genesis.art4 import clay_lamp
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2238"></rect>', ground(w, h, h * 0.9, "#1E1A28", dy=0)]
    dx0, dx1, dt = w * 0.34, w * 0.66, h * 0.06
    o.append(f'<rect x="{f(dx0 - 14)}" y="{f(dt - 14)}" width="{f(dx1 - dx0 + 28)}" height="{f(h * 0.9 - dt + 14)}" fill="#3A3040" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(dx0)}" y="{f(dt)}" width="{f(dx1 - dx0)}" height="{f(h * 0.9 - dt)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(dx0 + (dx1 - dx0) * q)} {f(dt)} L {f(dx0 + (dx1 - dx0) * q)} {f(h * 0.9)}" stroke="#4A3018" stroke-width="2"></path>' for q in (0.25, 0.5, 0.75)))
    hx, hy = w * 0.5, h * 0.42
    o.append(f'<circle cx="{f(hx)}" cy="{f(hy)}" r="{f(min(w, h) * 0.035)}" fill="#CFE0FF" stroke="#0D0D0F" stroke-width="2"></circle>'
             f'<path d="M{f(hx)} {f(hy)} L {f(hx - w * 0.2)} {f(h * 0.9)} L {f(hx + w * 0.2)} {f(h * 0.9)} Z" fill="#CFE0FF" opacity="0.08"></path>')
    by = h * 0.56
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(by)}" width="{f(w * 0.2)}" height="{f(h * 0.03)}" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(w * 0.44)}" y="{f(by - h * 0.03)}" width="{f(w * 0.02)}" height="{f(h * 0.09)}" fill="#A8A8B8" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             f'<rect x="{f(w * 0.54)}" y="{f(by - h * 0.03)}" width="{f(w * 0.02)}" height="{f(h * 0.09)}" fill="#A8A8B8" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    for x in (0.45, 0.55):
        for k in range(3):
            o.append(f'<path d="M{f(w * x)} {f(by + h * (0.07 + k * 0.05))} c 3 6 3 10 0 12 c -3 -2 -3 -6 0 -12 Z" fill="#C8A060" stroke="#6A4A10" stroke-width="0.8"></path>')
    o.append(clay_lamp(w * 0.16, h * 0.6, min(1.0, h / 300)) + f'<circle cx="{f(w * 0.16)}" cy="{f(h * 0.56)}" r="{f(min(w, h) * 0.2)}" fill="#FFC14D" opacity="0.1"></circle>'
             f'<path d="M{f(w * 0.82)} {f(h * 0.24)} L {f(w * 0.82)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<path d="M{f(w * 0.82)} {f(h * 0.3)} C {f(w * 0.76)} {f(h * 0.34)} {f(w * 0.75)} {f(h * 0.6)} {f(w * 0.76)} {f(h * 0.7)} L {f(w * 0.88)} {f(h * 0.7)} C {f(w * 0.89)} {f(h * 0.6)} {f(w * 0.88)} {f(h * 0.34)} {f(w * 0.82)} {f(h * 0.3)} Z" fill="{BRIDE_C}" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def walls_night(p, w, h, seed):
    """The watchmen that go about the city found me; the keepers of the walls took away my mantle from me: the city wall by
    night, the keepers with torches upon it, and a crimson mantle lying in the empty street below (told in words only)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#2A1E4A"), mk.stars(40, w, h * 0.4, seed)]
    wt = h * 0.36
    o.append(J.jericho(-10, w + 10, wt - h * 0.08, h * 0.72, seed, color="#5A4A5A", towers=3, houses=False))
    for i, x in enumerate((0.24, 0.5, 0.76)):
        o.append(J1.torchbearer(p, w * x, wt - h * 0.06, fit(wt - h * 0.06, wt - h * 0.24), flip=i % 2 == 1, seed=seed + i))
    o.append(ground(w, h, h * 0.72, "#2A2430", dy=0)
             + f'<path d="M{f(w * 0.4)} {f(h * 0.9)} C {f(w * 0.44)} {f(h * 0.84)} {f(w * 0.56)} {f(h * 0.86)} {f(w * 0.62)} {f(h * 0.82)} L {f(w * 0.66)} {f(h * 0.9)} C {f(w * 0.56)} {f(h * 0.94)} {f(w * 0.46)} {f(h * 0.94)} {f(w * 0.4)} {f(h * 0.9)} Z" fill="{BRIDE_C}" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

CELL.update({
  "gold": '<path d="M-50 40 L -40 10 L 40 10 L 50 40 Z M-30 10 L -22 -16 L 22 -16 L 30 10 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><path d="M-10 -16 L -4 -34 L 8 -34 L 14 -16" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6"></path>',
  "raven": '<path d="M-50 10 C -40 -20 0 -30 20 -20 L 40 -30 L 50 -24 L 36 -14 C 30 0 10 20 -20 20 L -50 40 L -40 16 Z" fill="#0D0D0F" stroke="#3A3A4A" stroke-width="2"></path><circle cx="34" cy="-24" r="2" fill="#F3EFE6"></circle>',
  "doves_brook": '<path d="M-64 40 C -30 30 30 50 64 36" stroke="#2C9DB8" stroke-width="10" fill="none"></path>' + dove(-20, 26, 1.1) + dove(24, 24, 1.1, flip=True),
  "spice_bed": '<rect x="-56" y="20" width="112" height="30" fill="#6A4A2A" stroke="#E8C88A" stroke-width="2"></rect>' + "".join(f'<path d="M{x} 20 L {x - 6} -20 M{x} 20 L {x + 6} -16 M{x} 20 L {x} -26" stroke="#5E8F26" stroke-width="3"></path><circle cx="{x}" cy="-26" r="4" fill="#C88AE0"></circle>' for x in (-40, -14, 12, 38)),
  "lily_myrrh": flower(0, 56, 1.2, "lily") + "".join(f'<path d="M{x} {y} c 2 5 2 8 0 10 c -2 -2 -2 -5 0 -10 Z" fill="#C8A060" stroke="#6A4A10" stroke-width="0.8"></path>' for x, y in ((-12, -40), (10, -30), (0, -20))),
  "rings": "".join(f'<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="#E8B830" stroke-width="6"></circle><circle cx="{x}" cy="{y - 16}" r="6" fill="#7AD0C0" stroke="#0D0D0F" stroke-width="1.4"></circle>' for x, y in ((-30, 0), (0, 24), (30, 0))),
  "ivory": '<path d="M-40 54 L -40 -20 C -40 -60 40 -60 40 -20 L 40 54 Z" fill="#F3EAD8" stroke="#E8C88A" stroke-width="2"></path><path d="M-30 50 L -30 -16 C -30 -46 30 -46 30 -16 L 30 50" fill="none" stroke="#C8B898" stroke-width="2"></path>'
            '<path d="M-30 10 L 30 10 M-30 26 L 30 26 M-30 42 L 30 42 M-14 -30 L 14 -30" stroke="#C8B898" stroke-width="2" fill="none"></path>'
            + "".join(f'<path d="M{x} {y - 6} L {x + 5} {y} L {x} {y + 6} L {x - 5} {y} Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.2"></path>' for x, y in ((-35, 30), (-35, 0), (-28, -30), (0, -46), (28, -30), (35, 0), (35, 30))),
  "marble": "".join(f'<rect x="{x - 12}" y="-50" width="24" height="86" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="2"></rect><rect x="{x - 18}" y="36" width="36" height="14" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>' for x in (-26, 26)),
  "cedars": "".join(f'<g transform="translate({x} 50) scale(0.5)"><path d="M0 0 L 0 -90" stroke="#5A3A22" stroke-width="8"></path>' + "".join(f'<path d="M{-60 + k * 8} {-30 - k * 22} L {60 - k * 8} {-30 - k * 22} L 0 {-50 - k * 22} Z" fill="#1F4A34" stroke="#0D0D0F" stroke-width="1.6"></path>' for k in range(4)) + '</g>' for x in (-30, 0, 30)),
})
