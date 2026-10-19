"""Drawings for the Esther volume (all new), on top of 2 Chronicles' (chr2.art carries chr1.art, kg2.art, kg1.art and 2 Samuel's
drawings as K2).

Shushan the palace: Persian pillared halls (pcol: a fluted shaft on a bell base under the double-bull capital), hangings of
white, green and blue on cords of purple to silver rings, a pavement of red, white, yellow and black marble (pavement), a
frieze of glazed rosettes. The king's gate with its winged bulls (kings_gate). Figures at a distance: Ahasuerus in purple
with the Persian crown (ahas), Vashti in gold (queen(..., VASHTI_C)), Esther in azure, crowned from 2:17 (queen(..., ESTHER_C)),
Mordecai in olive green, in sackcloth (state="sack") or in royal apparel of blue and white (state="royal"), Haman in dark red
(haman), beardless chamberlains (chamberlain)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel3 as S3, samuel4 as S4b, judges1 as J1, numbers1 as N
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import man, woman, sun, label, grid_bg, node, route
from exo import art as A
from num.art import ALL
from jos.art import crowd_at, below

INK, GOLD_C, CREAM = "#0D0D0F", "#E8B830", "#F3EFE6"
AHAS_C, VASHTI_C, ESTHER_C, MORD_C, SACK_C, HAMAN_C, ZERESH_C = "#4A1A6A", "#C8962E", "#2E7DB8", "#4A6A4A", "#6A5E4A", "#8A1A1A", "#5A1A3A"
CHAMB = ["#E8E2D6", "#C8A06A", "#2A5A6A", "#7A5A8A", "#A85A3A", "#5A7A9A", "#8A8A4A"]
PRINCE = ["#1F3A7A", "#6A2A4A", "#2A5A4A", "#7A4A1A", "#3A3A6A", "#5A1A2A", "#4A5A2A"]
MARBLE = ["#B5323A", "#F3EFE6", "#E8C040", "#2A2A30"]

PCROWN = ('<path d="M-12 -194 L -12 -214 L -7 -214 L -7 -208 L -2.5 -208 L -2.5 -216 L 2.5 -216 L 2.5 -208 L 7 -208 L 7 -214 L 12 -214 L 12 -194 Z" '
          'fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6" stroke-linejoin="round"></path>')
GREY_BEARD = A.WHITE_BEARD.replace("#E8E2D6", "#6A645E")

def ahas(p, x, y, s, flip=False, up=None, extra=""):
    """Ahasuerus at a distance: a purple robe, black beard, the Persian crown."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=AHAS_C, sw=3, flip=flip, up=up, extra=A.BLACK_BEARD + PCROWN + extra)

def queen(p, x, y, s, cloth, flip=False, up=None, crown=True, extra=""):
    """Vashti (gold) or Esther (azure) at a distance; crown=False for Esther before 2:17."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, woman=True, hair="#1A1210", sw=3, flip=flip, up=up,
                     extra=(PCROWN.replace("-194", "-186") if crown else "") + extra)

def mordecai(p, x, y, s, flip=False, up=None, state="plain"):
    """Mordecai at a distance: olive green; state "sack" (sackcloth, ashes on the head) or "royal" (white and blue, a great crown)."""
    cloth = {"plain": MORD_C, "sack": SACK_C, "royal": CREAM}[state]
    head = A.headcloth({"plain": MORD_C, "sack": SACK_C, "royal": "#1F5FAD"}[state], cord=None if state == "sack" else "#3A2214")
    extra = head + GREY_BEARD
    if state == "sack":
        extra += '<path d="M-12 -196 C -4 -202 6 -202 12 -196" fill="none" stroke="#B8B2A6" stroke-width="4" stroke-dasharray="2 3"></path>'
    if state == "royal":
        extra += PCROWN.replace("-194", "-190").replace("-214", "-218").replace("-216", "-222").replace("-208", "-212")
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, sw=3, flip=flip, up=up, extra=extra)

def haman(p, x, y, s, flip=False, up=None, covered=False):
    """Haman at a distance: dark red, a black beard, a gold band; covered=True: his head covered in mourning."""
    band = '<path d="M-14 -192 C -6 -196 6 -196 14 -192" fill="none" stroke="#E8B830" stroke-width="3"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=HAMAN_C, sw=3, flip=flip, up=up,
                     extra=A.headcloth("#3A3438" if covered else HAMAN_C, cord=None) + ("" if covered else band) + A.BLACK_BEARD)

def chamberlain(p, x, y, s, cloth, flip=False, up=None, kind="Tunic"):
    """A beardless chamberlain of the king's house: headcloth and tunic in one colour."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind=kind, sw=3, flip=flip, up=up, extra=A.headcloth(cloth, cord="#E8B830"))

def prince(p, x, y, s, cloth, flip=False, up=None):
    """A prince of Persia and Media: a long robe, black beard, headcloth with a gold band."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, sw=3, flip=flip, up=up, extra=A.headcloth(cloth, cord="#E8B830") + A.BLACK_BEARD)

def guard(p, x, y, s, cloth="#5A7A9A", flip=False):
    """One of the king's guard: a tunic, a headcloth and a spear."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, extra=A.headcloth(cloth, cord="#E8B830") + A.BLACK_BEARD + E4.SPEAR)

def behind(fig, x0, x1, y, depth, color="#C8962E", rim="#E8E2D6"):
    """A couch (gold or silver) set in front of a figure, so the figure sits on it: the couch covers the legs."""
    return fig + (f'<path d="M{f(x0)} {f(y)} L {f(x0)} {f(y - depth * 1.3)} C {f(x0)} {f(y - depth * 1.8)} {f(x0 + depth * 0.5)} {f(y - depth * 1.8)} {f(x0 + depth * 0.5)} {f(y - depth * 1.2)} '
                  f'L {f(x1)} {f(y - depth * 1.2)} L {f(x1)} {f(y)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></path>'
                  f'<path d="M{f(x0 + depth * 0.5)} {f(y - depth * 0.7)} L {f(x1)} {f(y - depth * 0.7)}" stroke="{rim}" stroke-width="2" opacity="0.6"></path>'
                  + "".join(f'<rect x="{f(x - 3)}" y="{f(y)}" width="6" height="{f(depth * 0.4)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.4"></rect>' for x in (x0 + 6, x1 - 8)))

# ---- architecture ---------------------------------------------------------------------------------------------------------
BULL = ("M-38 26 C -42 14 -38 4 -28 2 L -9 2 L -9 10 L 9 10 L 9 2 L 28 2 C 38 4 42 14 38 26 Z")
def pcol(x, base, top, s=1.0, color="#E8DCC8", shade="#B8A888"):
    """A Persian column from base up to top: a bell base, a fluted shaft, the volute block and the double-bull capital."""
    cap = top + 52 * s
    o = [f'<path d="M{f(x - 18 * s)} {f(base)} C {f(x - 16 * s)} {f(base - 14 * s)} {f(x - 10 * s)} {f(base - 20 * s)} {f(x - 9 * s)} {f(base - 24 * s)} '
         f'L {f(x + 9 * s)} {f(base - 24 * s)} C {f(x + 10 * s)} {f(base - 20 * s)} {f(x + 16 * s)} {f(base - 14 * s)} {f(x + 18 * s)} {f(base)} Z" fill="{shade}" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<rect x="{f(x - 8 * s)}" y="{f(cap)}" width="{f(16 * s)}" height="{f(base - 24 * s - cap)}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></rect>',
         "".join(f'<path d="M{f(x + d * s)} {f(cap + 4)} L {f(x + d * s)} {f(base - 26 * s)}" stroke="{shade}" stroke-width="{f(max(1, 1.4 * s))}"></path>' for d in (-4, 0, 4)),
         f'<rect x="{f(x - 6 * s)}" y="{f(cap)}" width="{f(12 * s)}" height="{f(4 * s)}" fill="{shade}"></rect>']
    o.append(f'<g transform="translate({f(x)} {f(top)}) scale({f(s)})">'
             '<rect x="-10" y="26" width="20" height="26" fill="' + color + '" stroke="#0D0D0F" stroke-width="2"></rect>'
             '<circle cx="-5" cy="34" r="4" fill="none" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="5" cy="34" r="4" fill="none" stroke="#0D0D0F" stroke-width="1.6"></circle>'
             '<path d="M-10 44 L 10 44" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<path d="{BULL}" fill="{color}" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
             + "".join(f'<g transform="scale({k} 1)"><path d="M32 6 C 40 2 50 6 50 14 C 50 22 44 24 38 20 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
                       '<path d="M38 6 C 40 -2 48 -6 52 -2" fill="none" stroke="#0D0D0F" stroke-width="2.4" stroke-linecap="round"></path>'
                       '<circle cx="44" cy="11" r="1.6" fill="#0D0D0F"></circle>'
                       '<path d="M24 16 L 24 26 M30 16 L 30 26" stroke="#0D0D0F" stroke-width="1.6"></path></g>' for k in (1, -1))
             + '</g>')
    return "".join(o)

def pavement(w, h, y0, rows=7, seed=1):
    """The pavement of red, white, yellow and black marble, in perspective from y0 down to the bottom edge."""
    vx, vy = w * 0.5, y0 - (h - y0) * 2.2
    xb = [-w * 1.2 + j * (w * 3.4 / 16) for j in range(17)]
    def at(xx, y): return vx + (xx - vx) * (y - vy) / (h - vy)
    ys = [y0 + (h + 6 - y0) * ((i / rows) ** 1.35) for i in range(rows + 1)]
    o = []
    for i in range(rows):
        for j in range(16):
            a, b = ys[i], ys[i + 1]
            pts = [(at(xb[j], a), a), (at(xb[j + 1], a), a), (at(xb[j + 1], b), b), (at(xb[j], b), b)]
            o.append(f'<path d="M{" L ".join(f"{f(x)} {f(y)}" for x, y in pts)} Z" fill="{MARBLE[(i + j * 3) % 4]}" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o)

def frieze(w, y, hh, color="#1F5FAD"):
    """A band of glazed brick with gold rosettes."""
    o = [f'<rect x="-10" y="{f(y)}" width="{f(w + 20)}" height="{f(hh)}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></rect>']
    r = hh * 0.3
    for i in range(int(w / (hh * 0.9)) + 2):
        cx = i * hh * 0.9 + hh * 0.3
        o.append(f'<circle cx="{f(cx)}" cy="{f(y + hh / 2)}" r="{f(r)}" fill="#E8C040" stroke="#0D0D0F" stroke-width="1.2"></circle>'
                 f'<circle cx="{f(cx)}" cy="{f(y + hh / 2)}" r="{f(r * 0.4)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></circle>')
    return "".join(o)

def hangings(xs, y, drop, seed=1):
    """Hangings of white cloth, of green and of blue between the columns at xs, fastened with cords of purple to silver rings."""
    o = []
    for a, b in zip(xs, xs[1:]):
        for k, col in enumerate(("#F3EFE6", "#3A8A5A", "#2A5AA8")):
            d = drop * (1 - k * 0.22); yy = y + k * 6
            o.append(f'<path d="M{f(a)} {f(yy)} C {f(a + (b - a) * 0.3)} {f(yy + d)} {f(b - (b - a) * 0.3)} {f(yy + d)} {f(b)} {f(yy)} '
                     f'L {f(b)} {f(yy + 8)} C {f(b - (b - a) * 0.3)} {f(yy + d + 14)} {f(a + (b - a) * 0.3)} {f(yy + d + 14)} {f(a)} {f(yy + 8)} Z" fill="{col}" stroke="#0D0D0F" stroke-width="1.8"></path>')
    for x in xs:
        o.append(f'<path d="M{f(x)} {f(y + 2)} L {f(x)} {f(y + 22)}" stroke="#6A2A8A" stroke-width="4"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="6" fill="#D8DCE4" stroke="#0D0D0F" stroke-width="1.8"></circle>')
    return "".join(o)

def hall(p, w, h, seed, n=4, floor=0.7, hang=True, dusk=False, wall=None):
    """A pillared hall of Shushan the palace: the back wall with its frieze, n columns, the hangings and the marble pavement."""
    fy = h * floor
    o = [mk.defs(p, *ALL), K2.sky(w, h, *(("#5A3A5A", "#C88A6A") if dusk else (wall or ("#C8B08A", "#EADCC0")))),
         frieze(w, fy - h * 0.2, h * 0.07), f'<rect x="-10" y="{f(fy - h * 0.13)}" width="{f(w + 20)}" height="{f(h * 0.13)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="1.6"></rect>',
         pavement(w, h, fy, seed=seed)]
    s = min(1.6, h / 330)
    xs = [w * (i + 0.5) / n for i in range(n)]
    for x in xs: o.append(pcol(x, fy + 4, -6, s))
    o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(12 + 6)}" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></rect>')
    if hang: o.append(hangings(xs, h * 0.16, h * 0.14, seed))
    return "".join(o)

# ---- Esther 1 -----------------------------------------------------------------------------------------------------------------
EMPIRE = [("INDIA", 0.9, 0.42), ("PERSIA", 0.66, 0.6), ("MEDIA", 0.6, 0.22), ("BABYLON", 0.44, 0.4), ("JERUSALEM", 0.26, 0.48),
          ("EGYPT", 0.16, 0.66), ("ETHIOPIA", 0.2, 0.9)]
def empire_map(w, h, posts=False, hi=None, isles=False, seed=7):
    """The kingdom of Ahasuerus as a technical map: a hundred and seven and twenty provinces from India unto Ethiopia, Shushan
    the palace lit; posts=True: the posts riding out from Shushan to every province; isles=True: the isles of the sea."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 {f(h * 0.2)} C {f(w * 0.08)} {f(h * 0.3)} {f(w * 0.12)} {f(h * 0.42)} {f(w * 0.1)} {f(h * 0.56)} L -10 {f(h * 0.6)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.56)} {f(h * 0.62)} C {f(w * 0.62)} {f(h * 0.7)} {f(w * 0.72)} {f(h * 0.78)} {f(w * 0.84)} {f(h * 0.82)} L {f(w * 0.84)} {f(h * 0.92)} C {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.6)} {f(h * 0.8)} {f(w * 0.52)} {f(h * 0.68)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.24)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.3)} {f(h * 0.62)}" fill="none" stroke="#2C9DB8" stroke-width="5"></path>')
    r = random.Random(seed)
    for _ in range(127):                                   # the provinces, one dot each
        a = r.uniform(0, 2 * math.pi); d = r.uniform(0.12, 1) ** 0.6
        x, y = w * 0.54 + math.cos(a) * w * 0.4 * d, h * 0.52 + math.sin(a) * h * 0.38 * d
        o.append(f'<rect x="{f(x - 2)}" y="{f(y - 2)}" width="4" height="4" fill="#FFD23F" opacity="0.55"></rect>')
    sx, sy = w * 0.56, h * 0.5
    if posts:
        for nm, x, y in EMPIRE:
            o.append(route([(sx, sy), (w * x, h * y)], color="#FFD23F"))
    if isles:
        for i, (x, y) in enumerate(((0.04, 0.3), (0.08, 0.4), (0.03, 0.48), (0.74, 0.88), (0.8, 0.86))):
            o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * y)}" rx="{f(w * 0.018)}" ry="{f(h * 0.02)}" fill="#C8A06A" stroke="#FFD23F" stroke-width="1.4"></ellipse>')
        o.append(label(w * 0.05, h * 0.16, "THE ISLES OF THE SEA", "#8FD0E2", 8, "start"))
    for nm, x, y in EMPIRE:
        o.append(node(w * x, h * y, nm, "#FFD23F" if nm == hi else "#8FD0E2", r=4, dy=-10, size=8))
    o.append(node(sx, sy, "SHUSHAN", "#D7261E", r=7, dy=-14, size=11))
    o.append(label(w * 0.34, h * 0.96, "127 PROVINCES · FROM INDIA UNTO ETHIOPIA", "#FFD23F", 9, "start"))
    return "".join(o)

def throne_hall(p, w, h, seed, princes=6, cast=None):
    """The king on his throne in the hall, the princes and nobles of the provinces standing before him."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=4, floor=0.66)]
    k = min(1.3, h / 300)
    o.append(S3.throne(w * 0.82, b, k))
    o.append(ahas(p, w * 0.82, b - 46 * k, fit(b, h * 0.28) * 0.78))
    s = fit(b, max(h * 0.4, b - 210))
    for i in range(princes):
        x = w * (0.08 + i * 0.11)
        o.append(prince(p, x, b - (i % 2) * 10, s * (0.9 + (i % 2) * 0.05), PRINCE[i % 7], flip=False))
    return "".join(o)

def garden_feast(p, w, h, seed):
    """The feast in the court of the garden: guests on couches of gold and silver under the hangings, on the marble pavement."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=3, floor=0.62, wall=("#8FD0E2", "#E8F0D8"))]
    r = random.Random(seed)
    s = fit(b, max(h * 0.44, b - 200))
    for i in range(4):
        x0 = w * (0.04 + i * 0.25); y = b - (i % 2) * 14
        figs = "".join((man if r.random() < 0.7 else woman)(p, x0 + 30 + j * 34, y - 18, s * 0.8, r.choice(PRINCE + A.HEBREW)) for j in range(3))
        o.append(behind(figs, x0, x0 + w * 0.21, y, 26 * min(1.4, s * 1.4), color=["#E8B830", "#C8CCD4"][i % 2]))
    return "".join(o)

def vessel(x, y, s, kind, color="#E8B830"):
    """One vessel of gold (diverse one from another): bowl, rhyton, cup, ewer, amphora."""
    shapes = {"bowl": "M-30 -24 L 30 -24 C 28 -6 16 0 0 0 C -16 0 -28 -6 -30 -24 Z",
              "rhyton": "M-14 -60 L 14 -60 L 12 -30 C 10 -14 4 -6 -6 -2 C -14 2 -22 -2 -24 -10 C -18 -10 -12 -16 -12 -30 Z",
              "cup": "M-18 -64 L 18 -64 C 16 -40 8 -30 4 -26 L 4 -8 L 14 0 L -14 0 L -4 -8 L -4 -26 C -8 -30 -16 -40 -18 -64 Z",
              "ewer": "M-10 -70 L 10 -70 L 8 -58 C 22 -48 24 -22 14 -8 L 14 0 L -14 0 L -14 -8 C -24 -22 -22 -48 -8 -58 Z M10 -66 C 24 -70 30 -64 26 -54",
              "amphora": "M-8 -80 L 8 -80 L 8 -70 C 24 -62 26 -30 12 -10 L 10 0 L -10 0 L -12 -10 C -26 -30 -24 -62 -8 -70 Z"}
    o = f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{shapes[kind]}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
    o += '<path d="M-10 -40 C -6 -46 0 -48 4 -46" fill="none" stroke="#FFF4C2" stroke-width="3" opacity="0.7" stroke-linecap="round"></path>'
    if kind == "rhyton": o += '<circle cx="-20" cy="-8" r="5" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></circle>'
    if kind in ("bowl", "cup", "rhyton"): o += f'<ellipse cx="0" cy="{-24 if kind == "bowl" else -64 if kind == "cup" else -60}" rx="{28 if kind == "bowl" else 16 if kind == "cup" else 13}" ry="4" fill="#8A0E16" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
    return o + "</g>"

def vessels(w, h, seed):
    """Royal wine in vessels of gold, the vessels being diverse one from another, on a low table."""
    o = [K2.sky(w, h, "#3A1A2A", "#8A4A3A"), V.rays(w * 0.5, h * 0.7, 30, 20, max(w, h), color="#FFC14D", op=0.12),
         f'<rect x="{f(w * 0.04)}" y="{f(h * 0.8)}" width="{f(w * 0.92)}" height="{f(h * 0.06)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.04)}" y="{f(h * 0.86)}" width="{f(w * 0.92)}" height="{f(h * 0.2)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    k = min(1.6, h / 150)
    for i, kind in enumerate(("amphora", "cup", "rhyton", "bowl", "ewer", "cup", "rhyton")):
        o.append(vessel(w * (0.1 + i * 0.13), h * 0.8, k * (0.9 if i % 2 else 1.0), kind, ["#E8B830", "#D8A030", "#F0C848"][i % 3]))
    return "".join(o)

def women_feast(p, w, h, seed):
    """Vashti's feast for the women in the royal house: the queen crowned on a couch of gold, the women about her."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=3, floor=0.64, wall=("#C88A9A", "#F0D8C8"))]
    s = fit(b, max(h * 0.42, b - 210))
    o.append(behind(queen(p, w * 0.5, b - 20, s * 0.9, VASHTI_C), w * 0.38, w * 0.62, b, 30 * min(1.4, s * 1.4)))
    r = random.Random(seed)
    for i, x in enumerate((0.08, 0.2, 0.78, 0.9)):
        o.append(behind(woman(p, w * x, b - 16 - (i % 2) * 8, s * 0.78, r.choice(["#C2456A", "#5A6E8A", "#E8D8B0", "#7A3A6A", "#3A8A7A"])),
                        w * (x - 0.06), w * (x + 0.06), b - (i % 2) * 8, 22 * min(1.4, s * 1.4), color="#C8CCD4"))
    return "".join(o)

def seven(p, w, h, seed, who="chamberlains"):
    """The king merry with wine on his couch and the seven chamberlains standing before him (who="princes": the seven
    princes of Persia and Media, who saw the king's face)."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=4, floor=0.64)]
    k = min(1.3, h / 300)
    if who == "princes":
        o.append(S3.throne(w * 0.12, b, k) + ahas(p, w * 0.12, b - 46 * k, fit(b, h * 0.26) * 0.8))
    else:
        s0 = fit(b, h * 0.3)
        o.append(behind(ahas(p, w * 0.12, b - 24, s0 * 0.86), w * 0.02, w * 0.24, b, 30 * min(1.4, s0 * 1.4)))
        o.append(vessel(w * 0.26, b, min(1.2, h / 260), "rhyton"))
    s = fit(b, max(h * 0.44, b - 200))
    for i in range(7):
        x = w * (0.36 + i * 0.09)
        o.append((prince(p, x, b - (i % 2) * 8, s, PRINCE[i], flip=True) if who == "princes" else chamberlain(p, x, b - (i % 2) * 8, s * 0.95, CHAMB[i], flip=True)))
    return "".join(o)

def scribes(p, w, h, seed, ring=False):
    """The king's scribes writing letters into every province according to the writing thereof, and to every people after
    their language; ring=True: the king's ring sealing them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8B08A", "#EADCC0"), frieze(w, h * 0.12, h * 0.07),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></rect>']
    s = min(1.6, (b - h * 0.3) / 125)
    for i in range(5):
        x = w * (0.08 + i * 0.17)
        o.append(E.kneel(x, b, s * 0.8, color=PRINCE[i], skin="#B98A6E"))
        o.append(f'<rect x="{f(x + 18 * s)}" y="{f(b - 46 * s)}" width="{f(60 * s)}" height="{f(10 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        o.append(S3.letter(x + 48 * s, b - 58 * s, s * 0.42, rot=-4, text=True))
    for j, y in enumerate((0.3, 0.42)):                    # the many scripts on the wall-board
        for i in range(8):
            o.append(f'<path d="M{f(w * (0.06 + i * 0.115))} {f(h * y)} l {f(w * 0.08)} 0" stroke="#5A3A22" stroke-width="2.4" stroke-dasharray="{["3 2", "6 3", "1 3", "8 2"][(i + j) % 4]}"></path>')
    if ring: o.append(signet(w * 0.86, h * 0.36, min(1.0, h / 360)))
    return "".join(o)

def signet(x, y, s=1.0):
    """The king's ring: a heavy gold ring with its seal-stone."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><circle cx="0" cy="0" r="40" fill="none" stroke="#0D0D0F" stroke-width="18"></circle>'
            '<circle cx="0" cy="0" r="40" fill="none" stroke="#E8B830" stroke-width="13"></circle>'
            '<path d="M-26 -26 C -10 -40 10 -40 26 -26" fill="none" stroke="#FFF4C2" stroke-width="3" opacity="0.7"></path>'
            '<rect x="-22" y="-72" width="44" height="34" rx="6" fill="#2C4A8A" stroke="#0D0D0F" stroke-width="3"></rect>'
            '<path d="M-12 -60 L 0 -50 L 12 -60 M-8 -48 L 8 -48" stroke="#8FD0E2" stroke-width="2.4" fill="none"></path></g>')

def posts(p, w, h, seed, n=4):
    """The posts riding out on horseback from Shushan the palace with the letters, the gate behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E0B0"), kings_gate_bg(w * 0.16, h * 0.74, w * 0.34, h * 0.56), ground(w, h, h * 0.74, "#C8A06A", dy=0)]
    s = min(1.3, (b - h * 0.4) / 140)
    for i in range(n):
        x = w * (0.42 + i * 0.16); y = b - (i % 2) * 18
        o.append(rider(p, x, y, s * (0.92 + (i % 2) * 0.08), ["#5A7A9A", "#7A3A2A", "#4A5A3A", "#6A4A7A"][i % 4]))
    for i in range(6):
        o.append(f'<path d="M{f(w * (0.36 + i * 0.1))} {f(b - 20 - (i % 3) * 30)} l {f(-w * 0.08)} 0" stroke="#F3EFE6" stroke-width="3" stroke-linecap="round" opacity="0.8"></path>')
    return "".join(o)

def rider(p, x, y, s, cloth, horse="#5A3A22", letter=True, flip=False, crown=None):
    """A man on horseback (a post with a letter in his hand, or Mordecai): the rider sits over the horse's back."""
    sx = -1 if flip else 1
    up = [(-22, -158), (-30, -186), (-26, -212)] if letter else None
    ex = (A.headcloth(cloth, cord="#E8B830") + (S3.letter(-26, -222, 0.28) if letter else ""))
    o = mk.person(p, round(x + sx * 4 * s), round(y - 74 * s), round(s * 0.66, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, up=up, extra=ex, flip=flip)
    o += E3.horse(x, y, s, color=horse, flip=flip)
    return o

def kings_gate_bg(x, base, w, h, lit=False):
    """The king's gate of Shushan seen whole: a great square gatehouse with its tall portal, winged bulls on either side of
    the way, a frieze along the top and stepped battlements."""
    o = [f'<rect x="{f(x - w / 2)}" y="{f(base - h)}" width="{f(w)}" height="{f(h)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         "".join(f'<path d="M{f(x - w / 2 + i * w / 7)} {f(base - h)} l 0 {f(-h * 0.06)} l {f(w / 21)} 0 l 0 {f(-h * 0.04)} l {f(w / 21)} 0 l 0 {f(h * 0.04)} l {f(w / 21)} 0 l 0 {f(h * 0.06)} Z" '
                 f'fill="#C8B08A" stroke="#0D0D0F" stroke-width="2"></path>' for i in range(7)),
         frieze_band(x - w / 2, base - h * 0.92, w, h * 0.08),
         f'<path d="M{f(x - w * 0.16)} {f(base)} L {f(x - w * 0.16)} {f(base - h * 0.62)} L {f(x + w * 0.16)} {f(base - h * 0.62)} L {f(x + w * 0.16)} {f(base)} Z" '
         f'fill="{"#FFC14D" if lit else "#2A1A14"}" stroke="#0D0D0F" stroke-width="2.4"></path>']
    k = h / 220
    for sx in (-1, 1):
        o.append(lamassu(x + sx * w * 0.32, base - h * 0.04, k * 0.9, flip=sx < 0))
    return "".join(o)

def frieze_band(x, y, w, hh):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(hh)}" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.6"></rect>'
            + "".join(f'<circle cx="{f(x + (i + 0.5) * w / 10)}" cy="{f(y + hh / 2)}" r="{f(hh * 0.28)}" fill="#E8C040" stroke="#0D0D0F" stroke-width="1"></circle>' for i in range(10)))

LAMASSU = ("M-46 0 L -46 -46 C -46 -58 -38 -64 -26 -64 L 22 -64 C 30 -64 36 -70 38 -78 L 38 -104 L 58 -104 L 58 -64 C 58 -56 54 -50 50 -48 L 50 0 L 40 0 L 40 -30 L 30 -30 L 30 0 L 20 0 "
           "L 20 -34 L -18 -34 L -18 0 L -28 0 L -28 -32 L -36 -32 L -36 0 Z")
def lamassu(x, y, s, flip=False, color="#B8A07A"):
    """A winged bull with a man's head, carved in relief beside the gate (stone colour, no features)."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="{LAMASSU}" fill="{color}" stroke="#0D0D0F" stroke-width="{f(2 / s)}" stroke-linejoin="round"></path>'
            f'<path d="M-24 -64 C -20 -98 4 -120 34 -118 L 30 -100 C 10 -100 -4 -86 -6 -64 Z" fill="{color}" stroke="#0D0D0F" stroke-width="{f(2 / s)}"></path>'
            + "".join(f'<path d="M{-18 + i * 9} -66 C {-14 + i * 9} -84 {-6 + i * 9} -96 {4 + i * 8} -104" fill="none" stroke="#0D0D0F" stroke-width="{f(1.2 / s)}" opacity="0.6"></path>' for i in range(4))
            + f'<path d="M38 -104 L 38 -116 L 58 -116 L 58 -104" fill="{color}" stroke="#0D0D0F" stroke-width="{f(2 / s)}"></path>'
            f'<path d="M40 -82 L 40 -62 L 56 -62 L 56 -82 Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="{f(1.4 / s)}"></path>'
            f'<circle cx="52" cy="-92" r="2" fill="#0D0D0F"></circle></g>')

# ---- Esther 2 -----------------------------------------------------------------------------------------------------------------
def cypress(x, y, s=1.0, color="#2E5A3A"):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><rect x="-4" y="-16" width="8" height="16" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></rect>'
            f'<path d="M0 -150 C 14 -120 22 -60 16 -16 L -16 -16 C -22 -60 -14 -120 0 -150 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M0 -130 C 6 -100 8 -60 6 -24" fill="none" stroke="#1F4A34" stroke-width="2"></path></g>')

def womens_house(p, w, h, seed, mordecai_out=False, n=6):
    """The house of the women: a walled garden court with a pool and cypresses, arched doors, the maidens walking, Hegai the
    keeper at the door; mordecai_out=True: Mordecai walking before the court, the low wall between."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8D0"),
         f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#E8D8B8" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         frieze(w, h * 0.2, h * 0.05, color="#2A8A8A")]
    for i in range(5):
        x = w * (0.1 + i * 0.2)
        o.append(f'<path d="M{f(x - w * 0.045)} {f(h * 0.7)} L {f(x - w * 0.045)} {f(h * 0.42)} C {f(x - w * 0.045)} {f(h * 0.33)} {f(x + w * 0.045)} {f(h * 0.33)} {f(x + w * 0.045)} {f(h * 0.42)} L {f(x + w * 0.045)} {f(h * 0.7)} Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.7, "#9CCB5E", dy=0))
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.8)}" rx="{f(w * 0.2)}" ry="{f(h * 0.05)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for x in (0.06, 0.94, 0.3, 0.7):
        o.append(cypress(w * x, h * 0.74, min(1.1, h / 300)))
    s = fit(b, max(h * 0.5, b - 180))
    r = random.Random(seed)
    if mordecai_out:
        o.append(woman(p, w * 0.3, h * 0.78, s * 0.6, "#C2456A") + queen(p, w * 0.42, h * 0.78, s * 0.62, ESTHER_C, crown=False) + woman(p, w * 0.62, h * 0.78, s * 0.6, "#E8D8B0"))
        o.append(f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2"></rect>')
        o.append(ground(w, h, h * 0.88, "#C8A06A", dy=0))
        o.append(mordecai(p, w * 0.8, b + 4, s * 0.95, flip=True))
    else:
        o.append(chamberlain(p, w * 0.1, b, s, "#E8E2D6", kind="Robe"))
        for i in range(n):
            x = w * (0.26 + i * 0.12)
            o.append(queen(p, x, b - (i % 2) * 14, s * (0.88 - (i % 2) * 0.06), ESTHER_C, crown=False) if i == 1 else
                     woman(p, x, b - (i % 2) * 14, s * (0.88 - (i % 2) * 0.06), r.choice(["#C2456A", "#E8D8B0", "#7A3A6A", "#3A8A7A", "#C8962E", "#E8E2D6"])))
    return "".join(o)

def perfumes(w, h, seed):
    """Twelve months of purification, six with oil of myrrh and six with sweet odors: jars of alabaster, a bowl of myrrh with
    its smoke, and a strip of the twelve months."""
    o = [K2.sky(w, h, "#3A2A3A", "#8A5A5A")]
    r = random.Random(seed)
    sh = h * 0.62
    o.append(f'<rect x="-10" y="{f(sh)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    k = min(1.4, h / 200)
    for i in range(7):
        x = w * (0.08 + i * 0.13); hh = (50 + r.uniform(0, 30)) * k; ww = (20 + r.uniform(0, 10)) * k
        col = ["#F3EFE6", "#E8D8C8", "#C8A06A", "#E8E2D6"][i % 4]
        o.append(f'<path d="M{f(x - ww * 0.3)} {f(sh - hh)} L {f(x + ww * 0.3)} {f(sh - hh)} L {f(x + ww * 0.3)} {f(sh - hh * 0.86)} C {f(x + ww)} {f(sh - hh * 0.7)} {f(x + ww)} {f(sh - hh * 0.1)} {f(x + ww * 0.4)} {f(sh)} '
                 f'L {f(x - ww * 0.4)} {f(sh)} C {f(x - ww)} {f(sh - hh * 0.1)} {f(x - ww)} {f(sh - hh * 0.7)} {f(x - ww * 0.3)} {f(sh - hh * 0.86)} Z" fill="{col}" stroke="#0D0D0F" stroke-width="2"></path>')
        if i in (2, 5):
            for j in range(4):
                o.append(f'<path d="M{f(x + j * 4)} {f(sh - hh - 6 - j * 14)} c 8 -8 -8 -14 0 -22" fill="none" stroke="#E8E2D6" stroke-width="2.4" opacity="{0.7 - j * 0.12:.2f}"></path>')
    y0, cw = h * 0.78, w * 0.9 / 12
    for i in range(12):
        col = "#FFD23F" if i < 6 else "#FF8ACA"
        o.append(f'<rect x="{f(w * 0.05 + i * cw + 2)}" y="{f(y0)}" width="{f(cw - 4)}" height="{f(h * 0.08)}" fill="{col}" fill-opacity="0.2" stroke="{col}" stroke-width="1.6"></rect>'
                 + label(w * 0.05 + i * cw + cw / 2, y0 + h * 0.055, str(i + 1), col, 10))
    o.append(label(w * 0.05 + 3 * cw, y0 + h * 0.15, "SIX MONTHS · OIL OF MYRRH", "#FFD23F", 9) + label(w * 0.05 + 9 * cw, y0 + h * 0.15, "SIX MONTHS · SWEET ODORS", "#FF8ACA", 9))
    return "".join(o)

def crowning(p, w, h, seed):
    """The king setting the royal crown upon Esther's head in the hall, the court looking on."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=4, floor=0.62)]
    s = fit(b, max(h * 0.3, b - 260))
    d = 64 * s
    hand = (-(d / s), -186)
    crown = (f'<g transform="translate({f(hand[0])} {f(hand[1] - 4)})">' + PCROWN.replace("-194", "0").replace("-214", "-18").replace("-216", "-22").replace("-208", "-14") + '</g>'
             f'<circle cx="{f(hand[0])}" cy="{f(hand[1] - 14)}" r="22" fill="#FFF4C2" opacity="0.3"></circle>')
    o.append(ahas(p, w * 0.4, b, s, flip=True, up=[(-22, -158), (-46, -200), hand], extra=crown))
    o.append(queen(p, w * 0.4 + d, b, s * 0.9, ESTHER_C, crown=False, flip=True))
    for i in range(4):
        o.append(prince(p, w * (0.76 + i * 0.07), b - (i % 2) * 8, s * 0.82, PRINCE[i], flip=True))
    o.append(chamberlain(p, w * 0.08, b, s * 0.86, "#E8E2D6", kind="Robe") + woman(p, w * 0.18, b, s * 0.8, "#C2456A") + woman(p, w * 0.26, b - 8, s * 0.76, "#E8D8B0"))
    return "".join(o)

def esther_feast(p, w, h, seed):
    """Esther's feast: the king and the queen on a couch of gold, the princes and servants at the tables, gifts carried in."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=4, floor=0.62)]
    s = fit(b, max(h * 0.42, b - 210))
    o.append(behind(ahas(p, w * 0.44, b - 22, s * 0.9) + queen(p, w * 0.56, b - 22, s * 0.84, ESTHER_C), w * 0.34, w * 0.66, b, 30 * min(1.4, s * 1.4)))
    r = random.Random(seed)
    for x0 in (0.02, 0.74):
        figs = "".join(prince(p, w * (x0 + 0.04 + j * 0.07), b - 18, s * 0.8, r.choice(PRINCE)) for j in range(3))
        o.append(behind(figs, w * x0, w * (x0 + 0.24), b, 24 * min(1.4, s * 1.4), color="#C8CCD4"))
    return "".join(o)

def kings_gate(p, w, h, seed, mord="sit", bowing=False, haman_by=False, others=0, sky=("#8FD0E2", "#F3E0B0")):
    """The king's gate: the gatehouse with its winged bulls, and before it Mordecai sitting (mord="sit"), standing ("stand"),
    in sackcloth crying ("sack"), or none; bowing=True: the king's servants bowed down; haman_by=True: Haman passing in."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, *sky), kings_gate_bg(w * 0.5, h * 0.74, w * 0.62, h * 0.62), ground(w, h, h * 0.74, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    if haman_by:
        o.append(haman(p, w * 0.5, h * 0.8, s * 0.7) + guard(p, w * 0.42, h * 0.8, s * 0.66) + guard(p, w * 0.58, h * 0.8, s * 0.66))
    if bowing:
        for i in range(4):
            o.append(N.prostrate(w * (0.18 + i * 0.1), b - (i % 2) * 10, s * 0.62, color=CHAMB[(i + 2) % 7], skin="#B98A6E", flip=True))
    for i in range(others):
        o.append(chamberlain(p, w * (0.1 + i * 0.08), b, s * 0.9, CHAMB[(i + 3) % 7]))
    if mord == "sit":
        o.append(E.kneel(w * 0.84, b, s * 0.7, color=MORD_C, skin="#B98A6E", flip=True))
    elif mord == "stand":
        o.append(mordecai(p, w * 0.84, b, s, flip=True))
    elif mord == "sack":
        o.append(mordecai(p, w * 0.7, b, s, state="sack", up=[(-22, -158), (-40, -196), (-48, -232)]))
    return "".join(o)

def threshold(p, w, h, seed):
    """Night at the threshold of the king's house: two chamberlains whispering in the shadow of a door, and Mordecai sitting
    in the gate, listening."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#0F0E2A", "#3A2A5A"), mk.stars(30, w, h * 0.3, seed),
         f'<rect x="{f(w * 0.08)}" y="{f(h * 0.16)}" width="{f(w * 0.5)}" height="{f(h * 0.76)}" fill="#3A2E3A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.22)} {f(h * 0.92)} L {f(w * 0.22)} {f(h * 0.42)} L {f(w * 0.44)} {f(h * 0.42)} L {f(w * 0.44)} {f(h * 0.92)} Z" fill="#FFC14D" stroke="#0D0D0F" stroke-width="2.4"></path>',
         pcol(w * 0.66, h * 0.94, h * 0.12, min(1.4, h / 330), color="#6A5A6A", shade="#4A3E4A"),
         ground(w, h, h * 0.92, "#2A2230", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(mk.person(p, round(w * 0.27), round(b), round(s, 3), body="#0D0D0F", cloth="#1A1420", kind="Tunic", sw=3)
             + mk.person(p, round(w * 0.37), round(b), round(s * 0.96, 3), body="#0D0D0F", cloth="#1A1420", kind="Tunic", sw=3, flip=True))
    o.append(E.kneel(w * 0.84, b, s * 0.66, color=MORD_C, skin="#8A6A5A", flip=True))
    return "".join(o)

def chronicles(w, h, seed, names=("MORDECAI", "BIGTHAN", "TERESH")):
    """The book of the chronicles before the king: an unrolled scroll on a reading desk, lines of script, a lamp."""
    o = [K2.sky(w, h, "#2A1A2A", "#6A4A3A"), V.rays(w * 0.82, h * 0.4, 24, 10, h * 0.8, color="#FFC14D", op=0.15)]
    x0, x1, y0, y1 = w * 0.1, w * 0.74, h * 0.24, h * 0.86
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="#F3E0B8" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(x0 - 12)}" y="{f(y0 - 8)}" width="16" height="{f(y1 - y0 + 16)}" rx="6" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(x1 - 4)}" y="{f(y0 - 8)}" width="16" height="{f(y1 - y0 + 16)}" rx="6" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
    r = random.Random(seed)
    rows = 8; dy = (y1 - y0 - 30) / rows
    for i in range(rows):
        y = y0 + 20 + i * dy
        xx = x0 + 18
        while xx < x1 - 30:
            l = r.uniform(14, 40)
            o.append(f'<path d="M{f(xx)} {f(y)} l {f(min(l, x1 - 24 - xx))} 0" stroke="#5A3A22" stroke-width="2.2"></path>'); xx += l + 8
        if i in (2, 3, 5) and names:
            nm = names[[2, 3, 5].index(i)]
            o.append(f'<rect x="{f(x0 + (x1 - x0) * 0.42)}" y="{f(y - dy * 0.42)}" width="{f((x1 - x0) * 0.36)}" height="{f(dy * 0.66)}" fill="#F3E0B8"></rect>'
                     + label(x0 + (x1 - x0) * 0.6, y + 3, nm, "#B5121B", max(8, min(12, dy * 0.42))))
    o.append(f'<path d="M{f(w * 0.82)} {f(h * 0.5)} C {f(w * 0.78)} {f(h * 0.5)} {f(w * 0.78)} {f(h * 0.56)} {f(w * 0.82)} {f(h * 0.56)} L {f(w * 0.9)} {f(h * 0.54)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>'
             + E.flame(w * 0.8, h * 0.5, 12, 26, 0.1))
    return "".join(o)

def shushan(w, h, seed, tone="day", smoke=False, glad=False):
    """Shushan the palace seen from the river: the city on its mound, the pillared halls of the palace on the citadel above,
    palms along the water. tone: day / dusk / night; smoke=True: smoke rising here and there over the city (9:6, 9:15)."""
    skies = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#3A2A5A", "#E88A5A"), "night": ("#0F0E2A", "#3A2A5A"), "glad": ("#FFE680", "#FFF4C2")}
    o = [K2.sky(w, h, *skies[tone])]
    if tone == "dusk": o.append(sun(w * 0.18, h * 0.5, 22, color="#FF8A3D", op=0.3))
    if tone == "glad": o.append(V.rays(w * 0.5, h * 0.2, 36, 30, max(w, h), color="#FFFFFF", op=0.25))
    dark = tone in ("dusk", "night")
    mound, city, pal = ("#5A3A3A", "#7A5A5A", "#8A6A6A") if dark else ("#B08A5A", "#D8B888", "#E8DCC8")
    o.append(f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.1)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.56)} {f(h * 0.4)} C {f(w * 0.76)} {f(h * 0.4)} {f(w * 0.9)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{mound}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(22):                                      # the houses of the city on the slopes
        x = r.uniform(0.02, 0.98) * w; y = h * (0.56 + r.uniform(0, 0.16)); bw = r.uniform(18, 36) * min(1.4, w / 600); bh = r.uniform(14, 28) * min(1.4, h / 300)
        if 0.3 * w < x < 0.8 * w and y < h * 0.6: continue
        o.append(f'<rect x="{f(x)}" y="{f(y - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{city}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 + (f'<rect x="{f(x + bw * 0.4)}" y="{f(y - bh * 0.6)}" width="{f(bw * 0.2)}" height="{f(bh * 0.3)}" fill="#FFC14D"></rect>' if dark and r.random() < 0.5 else ""))
    # the palace on the citadel: a platform, two halls of columns under flat roofs
    py = h * 0.4
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(py - h * 0.04)}" width="{f(w * 0.5)}" height="{f(h * 0.05)}" fill="{city}" stroke="#0D0D0F" stroke-width="2"></rect>')
    for x0, x1, hh in ((0.33, 0.58, 0.16), (0.6, 0.77, 0.12)):
        top = py - h * 0.04 - h * hh
        o.append(f'<rect x="{f(w * x0)}" y="{f(top - h * 0.03)}" width="{f(w * (x1 - x0))}" height="{f(h * 0.03)}" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></rect>')
        n = int((x1 - x0) * 40)
        for i in range(n + 1):
            x = w * (x0 + (x1 - x0) * i / n)
            o.append(f'<rect x="{f(x - 2.5)}" y="{f(top)}" width="5" height="{f(h * hh)}" fill="{pal}" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    if smoke:
        for x in (0.2, 0.46, 0.86):
            for j in range(6):
                o.append(f'<circle cx="{f(w * x + j * 5)}" cy="{f(h * (0.56 - j * 0.07))}" r="{f(w * (0.02 + j * 0.006))}" fill="#4A4048" opacity="{0.6 - j * 0.08:.2f}"></circle>')
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{"#1F3A5A" if dark else "#2C9DB8"}" stroke="#0D0D0F" stroke-width="2"></path>')
    for x in (0.06, 0.14, 0.9):
        o.append(J1.palm(w * x, h * 0.86, min(0.6, h / 500)))
    return "".join(o)

# ---- Esther 5 (also the cover) --------------------------------------------------------------------------------------------
def seated_king(p, xk, bt, kk, up=None, extra="", fig=None):
    """Ahasuerus seated on the royal throne (the throne's foot at bt, scale kk): the throne, the king, then the seat and the
    front legs over his robe."""
    sk = 0.64 * kk
    yk = bt - 46 * kk
    o = S3.throne(xk, bt, kk) + (fig or ahas)(p, xk, yk, sk, up=up, extra=extra)
    o += (f'<rect x="{f(xk - 48 * kk)}" y="{f(bt - 78 * kk)}" width="{f(96 * kk)}" height="{f(14 * kk)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
          + "".join(f'<rect x="{f(xk + dx * kk)}" y="{f(bt - 64 * kk)}" width="{f(10 * kk)}" height="{f(64 * kk)}" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></rect>' for dx in (-44, 34))
          + f'<rect x="{f(xk - 30 * kk)}" y="{f(bt - 10 * kk)}" width="{f(60 * kk)}" height="{f(10 * kk)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return o, sk, yk

def inner_court(p, w, h, seed, stage="stand", fig=0.42):
    """Esther in her royal apparel standing in the inner court over against the king's house; the king on his royal throne.
    stage "stand" / "sceptre" (the golden sceptre held out) / "touch" (Esther drew near and touched the top of the sceptre)."""
    b = h * 0.92
    o = [hall(p, w, h, seed, n=3, floor=0.6)]
    se = h * fig / 200
    kk = (se * 0.95 * 195 - 10) / 124
    xk = w * 0.76
    o.append(f'<path d="M{f(xk - 90 * kk)} {f(b + 4)} L {f(xk - 80 * kk)} {f(b - 14 * kk)} L {f(xk + 120 * kk)} {f(b - 14 * kk)} L {f(xk + 130 * kk)} {f(b + 4)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>')
    bt = b - 14 * kk
    tip = None
    if stage == "stand":
        o.append(seated_king(p, xk, bt, kk)[0])
    else:
        hand, tl = (-70, -128), (-150, -84)
        sc = (f'<path d="M{hand[0] + 6} {hand[1]} L {tl[0]} {tl[1]}" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path>'
              f'<path d="M{hand[0] + 6} {hand[1]} L {tl[0]} {tl[1]}" stroke="#E8B830" stroke-width="4" stroke-linecap="round"></path>'
              f'<circle cx="{tl[0]}" cy="{tl[1]}" r="8" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></circle>')
        k_svg, sk, yk = seated_king(p, xk, bt, kk, up=[(-22, -158), (-48, -146), hand], extra=sc)
        tip = (xk + tl[0] * sk, yk + tl[1] * sk)
        o.append(f'<circle cx="{f(tip[0])}" cy="{f(tip[1])}" r="{f(30 * sk)}" fill="#FFF4C2" opacity="0.4"></circle>' + k_svg)
    if stage == "touch" and tip:
        xe = tip[0] - 70 * se
        hx, hy = -(tip[0] - xe) / se, (tip[1] - b) / se
        o.append(queen(p, xe, b, se, ESTHER_C, flip=True, up=[(-22, -158), ((-22 + hx) / 2, (-158 + hy) / 2 + 10), (hx, hy)]))
    else:
        o.append(queen(p, w * 0.26 if stage == "stand" else w * 0.34, b, se, ESTHER_C, flip=True))
    o.append(guard(p, w * 0.06, b, se * 1.02) + guard(p, w * 0.97, b, se * 1.02, flip=True))
    return "".join(o)
