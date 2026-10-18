"""New drawings for Numbers chapter 2 (Numbers 3–4): the camp of the Levites about the tabernacle, the holy things wrapped
for the journey (each covering in its order and colour), the sons of Kohath bearing them, the burdens of Gershon and
Merari, the first-born set against the Levites, and the redemption-money."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, joshua1 as J, exodus3 as E3, exodus5 as V
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man
from exo import art as A, art8 as B8, art9 as Q
from exo.art7 import coins
from num.art import ALL, TRIBE_C, standard
def f(v): return f"{v:.1f}"
CY, GOLD, SILVER, BRASS, BLUE, PURPLE, SCARLET = B8.CY, B8.GOLD, B8.SILVER, B8.BRASS, B8.BLUE, B8.PURPLE, B8.SCARLET
SEAL = "#5A4A3A"                                    # the covering of sealskin
LEVI_C = {"GERSHON": "#5AC8C8", "KOHATH": "#E8B830", "MERARI": "#8A6A4A", "PRIESTS": "#F3EFE6"}

def levite_plan(w, h, hi=None, title="THE CAMP OF THE LEVITES · NUMBERS 3"):
    """The tabernacle with the Levites round about it: Gershon behind it westward, Kohath southward, Merari northward,
    and before it eastward Moses, Aaron and his sons. hi = "W" / "S" / "N" / "E" lights one side."""
    o = [B8.bp(w, h), B8.title_bar(w, title)]
    cx, cy = w * 0.5, h * 0.56; u = min(w / 11, (h - 40) / 7.2)
    o.append(f'<rect x="{f(cx - 2 * u)}" y="{f(cy - u)}" width="{f(4 * u)}" height="{f(2 * u)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(cx - 1.6 * u)}" y="{f(cy - 0.4 * u)}" width="{f(1.6 * u)}" height="{f(0.8 * u)}" fill="#8A3A2A" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             f'<rect x="{f(cx + 0.6 * u)}" y="{f(cy - 0.22 * u)}" width="{f(0.44 * u)}" height="{f(0.44 * u)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    fs = max(7, min(11, u * 0.3))
    sides = {"W": ("GERSHON · 7,500", LEVI_C["GERSHON"], (cx - 3.6 * u, cy - 1.6 * u, 1.3 * u, 3.2 * u)),
             "S": ("KOHATH · 8,600", LEVI_C["KOHATH"], (cx - 2.4 * u, cy + 1.4 * u, 4.8 * u, 1.2 * u)),
             "N": ("MERARI · 6,200", LEVI_C["MERARI"], (cx - 2.4 * u, cy - 2.6 * u, 4.8 * u, 1.2 * u)),
             "E": ("MOSES · AARON", LEVI_C["PRIESTS"], (cx + 2.3 * u, cy - 1.6 * u, 1.3 * u, 3.2 * u))}
    for k, (text, c, (x, y, bw, bh)) in sides.items():
        op = 1 if hi in (None, k) else 0.3
        dark = c in ("#E8B830", "#F3EFE6", "#5AC8C8")
        o.append(f'<g opacity="{op}"><rect x="{f(x)}" y="{f(y)}" width="{f(bw)}" height="{f(bh)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        if bw < bh:
            o.append(f'<g transform="translate({f(x + bw / 2)} {f(y + bh / 2)}) rotate(-90)">' + label(0, fs * 0.35, text, "#0D0D0F" if dark else "#F3EFE6", fs, ls=0.08) + '</g></g>')
        else:
            o.append(label(x + bw / 2, y + bh / 2 + fs * 0.35, text, "#0D0D0F" if dark else "#F3EFE6", fs, ls=0.08) + '</g>')
    o.append(label(cx, cy + u + fs + 4, "THE TABERNACLE", CY, fs * 0.85, ls=0.1))
    o.append(label(min(w - 14, cx + 4.2 * u), cy + 4, "E ▸", "#FFD23F", 10))
    return "".join(o)

# ---- the holy things wrapped for the journey ---------------------------------------------------------------------------
def _obj(kind, x, b, s):
    """The bare piece (front view), standing on y = b, about 100*s wide."""
    if kind == "ark":
        return (f'<rect x="{f(x - 50 * s)}" y="{f(b - 46 * s)}" width="{f(100 * s)}" height="{f(46 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>'
                f'<path d="M{f(x - 44 * s)} {f(b - 46 * s)} C {f(x - 40 * s)} {f(b - 80 * s)} {f(x - 10 * s)} {f(b - 70 * s)} {f(x - 4 * s)} {f(b - 50 * s)} M{f(x + 44 * s)} {f(b - 46 * s)} C {f(x + 40 * s)} {f(b - 80 * s)} {f(x + 10 * s)} {f(b - 70 * s)} {f(x + 4 * s)} {f(b - 50 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    if kind == "table":
        return (f'<rect x="{f(x - 50 * s)}" y="{f(b - 50 * s)}" width="{f(100 * s)}" height="{f(8 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>'
                f'<path d="M{f(x - 44 * s)} {f(b - 42 * s)} L {f(x - 44 * s)} {f(b)} M{f(x + 44 * s)} {f(b - 42 * s)} L {f(x + 44 * s)} {f(b)}" stroke="{GOLD}" stroke-width="{f(6 * s)}"></path>'
                + "".join(f'<rect x="{f(x + dx * s - 6 * s)}" y="{f(b - 64 * s)}" width="{f(12 * s)}" height="{f(14 * s)}" rx="{f(3 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></rect>' for dx in (-30, -10, 10, 30)))
    if kind == "lamp":
        o = [f'<path d="M{f(x)} {f(b)} L {f(x)} {f(b - 90 * s)}" stroke="{GOLD}" stroke-width="{f(6 * s)}"></path>']
        for k in (1, 2, 3):
            o.append(f'<path d="M{f(x)} {f(b - (30 + 6 * k) * s)} C {f(x - 14 * k * s)} {f(b - (30 + 6 * k) * s)} {f(x - 14 * k * s)} {f(b - 70 * s)} {f(x - 14 * k * s)} {f(b - 90 * s)} M{f(x)} {f(b - (30 + 6 * k) * s)} C {f(x + 14 * k * s)} {f(b - (30 + 6 * k) * s)} {f(x + 14 * k * s)} {f(b - 70 * s)} {f(x + 14 * k * s)} {f(b - 90 * s)}" fill="none" stroke="{GOLD}" stroke-width="{f(4 * s)}"></path>')
        o.append(f'<rect x="{f(x - 20 * s)}" y="{f(b - 6 * s)}" width="{f(40 * s)}" height="{f(6 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1"></rect>')
        return "".join(o)
    if kind == "altar_gold":
        return (f'<rect x="{f(x - 22 * s)}" y="{f(b - 70 * s)}" width="{f(44 * s)}" height="{f(70 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>'
                f'<path d="M{f(x - 22 * s)} {f(b - 70 * s)} L {f(x - 22 * s)} {f(b - 80 * s)} M{f(x + 22 * s)} {f(b - 70 * s)} L {f(x + 22 * s)} {f(b - 80 * s)}" stroke="{GOLD}" stroke-width="{f(5 * s)}"></path>')
    if kind == "vessels":
        return "".join(f'<path d="M{f(x + dx * s - 12 * s)} {f(b - 22 * s)} L {f(x + dx * s + 12 * s)} {f(b - 22 * s)} L {f(x + dx * s + 8 * s)} {f(b)} L {f(x + dx * s - 8 * s)} {f(b)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></path>' for dx in (-40, -14, 12, 38))
    if kind == "altar":
        return (f'<rect x="{f(x - 50 * s)}" y="{f(b - 56 * s)}" width="{f(100 * s)}" height="{f(56 * s)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></rect>'
                f'<path d="M{f(x - 50 * s)} {f(b - 30 * s)} L {f(x + 50 * s)} {f(b - 30 * s)}" stroke="#0D0D0F" stroke-width="1.2"></path>')
    if kind == "curtains":
        return "".join(f'<rect x="{f(x - 52 * s + i * 3 * s)}" y="{f(b - (12 + 12 * i) * s)}" width="{f(104 * s)}" height="{f(12 * s)}" rx="{f(4 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></rect>'
                       for i, c in enumerate(("#F3EFE6", BLUE, PURPLE, SCARLET, "#8A6A5A", "#8A3A2A", SEAL)))
    if kind == "boards":
        o = [f'<rect x="{f(x - 56 * s)}" y="{f(b - (10 + 9 * i) * s)}" width="{f(112 * s)}" height="{f(9 * s)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.2"></rect>' for i in range(6)]
        o += [f'<path d="M{f(x - 58 * s)} {f(b - 68 * s)} L {f(x + 58 * s)} {f(b - 68 * s)}" stroke="{GOLD}" stroke-width="{f(5 * s)}"></path>']
        o += [f'<rect x="{f(x + dx * s - 8 * s)}" y="{f(b - 10 * s)}" width="{f(16 * s)}" height="{f(10 * s)}" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1"></rect>' for dx in (-70, 70)]
        return "".join(o)
    return ""

def wrap_plate(w, h, title, kind, layers, staves=True, frame=False):
    """A blueprint plate: the piece bare at the left, wrapped at the right (the coverings shown as drapes in their order,
    outermost last), and a legend of the coverings with their colours. layers = [(name, colour)]."""
    o = [B8.bp(w, h), B8.title_bar(w, title)]
    n = len(layers); y0 = 52 + 16 * n
    if h > 300:                                       # tall: the bare piece above, the wrapped piece below, at the right
        R = (h - 24 - y0) / 2
        s = max(0.45, min(1.9, (R - 30) / (80 + 8 * n), 0.2 * w / (52 + 7 * n)))
        xb = xw = w * 0.76; bb, b = y0 + R - 4, y0 + 2 * R - 4
    else:
        b = h * 0.86; bb = b
        s = max(0.45, min(1.0, (b - y0) / (74 + 8 * n), w / 760))
        xb, xw = w * 0.62, w * 0.84
    o.append(_obj(kind, xb, bb, s) + label(xb, bb + 14, "BARE", CY, 8.5, ls=0.12))
    # the wrapped piece: each covering a little larger than the last
    for i, (_, c) in enumerate(layers):
        pad = (4 + 7 * i) * s; top = b - (64 + 8 * i) * s
        o.append(f'<path d="M{f(xw - 52 * s - pad)} {f(b)} L {f(xw - 50 * s - pad)} {f(top + 14 * s)} C {f(xw - 40 * s - pad)} {f(top)} {f(xw + 40 * s + pad)} {f(top)} {f(xw + 50 * s + pad)} {f(top + 14 * s)} L {f(xw + 52 * s + pad)} {f(b)} Z" '
                 f'fill="{c}" stroke="#0D0D0F" stroke-width="1.6" opacity="{0.92 if i == len(layers) - 1 else 0.85}"></path>')
    if staves:
        o.append(f'<path d="M{f(xw - 120 * s)} {f(b - 30 * s)} L {f(xw + 120 * s)} {f(b - 30 * s)}" stroke="{GOLD if kind != "altar" else BRASS}" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>')
    if frame:
        o.append(f'<path d="M{f(xw - 120 * s)} {f(b + 4)} L {f(xw + 120 * s)} {f(b + 4)} M{f(xw - 110 * s)} {f(b - 6)} L {f(xw + 110 * s)} {f(b - 6)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}"></path>')
    o.append(label(xw, b + 14, "WRAPPED FOR THE JOURNEY", CY, 8.5, ls=0.12))
    for i, (name, c) in enumerate(layers):                 # the legend, under the title at the right
        y = 44 + i * 16; x = w * 0.56
        o.append(f'<rect x="{f(x)}" y="{f(y - 9)}" width="12" height="10" fill="{c}" stroke="#0D0D0F" stroke-width="1"></rect>'
                 + label(x + 18, y, f"{i + 1} · {name}", CY, 8.5, "start", ls=0.08))
    return "".join(o)

def bearers(p, w, h, seed, cloth=BLUE, n=2):
    """The sons of Kohath bearing the ark, wrapped in its cloth of blue, upon their shoulders by the staves."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.16, 14, op=0.25), hills(w, h, h * 0.5, seed, color="#8A6A4A", amp=10), ground(w, h, h * 0.58, "#C8A06A", dy=0)]
    s = min(fit(b, h * 0.36), w / (n * 430))
    xs = [w * (k + 0.5) / n for k in range(n)]
    for x in xs:                                      # the wrapped ark and its staves, then the bearers in front
        gap = 150 * s; sh = b - 150 * s
        o.append(f'<path d="M{f(x - gap - 34 * s)} {f(sh + 10 * s)} L {f(x + gap + 34 * s)} {f(sh + 10 * s)}" stroke="{GOLD}" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>')
        o.append(f'<path d="M{f(x - 70 * s)} {f(sh + 14 * s)} L {f(x - 64 * s)} {f(sh - 50 * s)} C {f(x - 50 * s)} {f(sh - 70 * s)} {f(x + 50 * s)} {f(sh - 70 * s)} {f(x + 64 * s)} {f(sh - 50 * s)} L {f(x + 70 * s)} {f(sh + 14 * s)} Z" fill="{cloth}" stroke="#0D0D0F" stroke-width="2.4"></path>')
        o.append(mk.person(p, round(x - gap), b, round(s, 3), body="#2A140C", cloth="#C8B080", sw=3))
        o.append(mk.person(p, round(x + gap), b, round(s, 3), body="#2A140C", cloth="#C8B080", sw=3, flip=True))
    return "".join(o)

def aaron_sons(p, w, h, seed):
    """Aaron the high priest with his sons Eleazar and Ithamar before the tent; two empty places for Nadab and Abihu."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), ground(w, h, h * 0.6, "#C8B080", dy=0), V.tabernacle(w * 0.7, h * 0.64, w * 0.46, uid=p + "tb")]
    s = fit(b, h * 0.3)
    o.append(Q.high_priest(p, w * 0.22, b, s) + Q.son_priest(p, w * 0.36, b, s * 0.96, flip=True) + Q.son_priest(p, w * 0.46, b, s * 0.96, flip=True))
    for x in (0.56, 0.64):
        o.append(f'<path d="M{f(w * x - 18 * s)} {f(b)} L {f(w * x)} {f(b - 190 * s)} L {f(w * x + 18 * s)} {f(b)}" fill="none" stroke="#8A6A4A" stroke-width="2" stroke-dasharray="5 4"></path>')
    return "".join(o)

def firstborn_chart(w, h):
    """Levites 22,000 against the first-born males 22,273: the 273 over and above, to be redeemed."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE LEVITES FOR THE FIRST-BORN")]
    x0 = w * 0.08; x1 = w * 0.92; L = x1 - x0; y1, y2 = h * 0.42, h * 0.68; bh = h * 0.14
    scale = L / 22273
    o.append(f'<rect x="{f(x0)}" y="{f(y1)}" width="{f(22000 * scale)}" height="{f(bh)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             + label(x0 + 8, y1 + bh / 2 + 4, "THE LEVITES · 22,000", "#0D0D0F", 10, "start"))
    o.append(f'<rect x="{f(x0)}" y="{f(y2)}" width="{f(22000 * scale)}" height="{f(bh)}" fill="#5A6E8A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(x0 + 22000 * scale)}" y="{f(y2)}" width="{f(273 * scale + 4)}" height="{f(bh)}" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             + label(x0 + 8, y2 + bh / 2 + 4, "THE FIRST-BORN · 22,273", "#F3EFE6", 10, "start"))
    o.append(B8.tag(x0 + 22000 * scale + 2, y2 + bh, "273 · FIVE SHEKELS APIECE", x1 - 160, h * 0.94, color="#FFD23F"))
    return "".join(o)

def redemption(w, h):
    """A thousand three hundred and threescore and five shekels, after the shekel of the sanctuary, given unto Aaron."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE REDEMPTION-MONEY · 1,365 SHEKELS")]
    r = max(5, min(9, h / 40))
    for k in range(5):
        o.append(coins(w * (0.5 + k * 0.09), h * 0.86, 25, r=r))
    o.append(label(w * 0.72, h * 0.95, "273 × 5 SHEKELS · THE SHEKEL IS TWENTY GERAHS", CY, 8.5))
    return "".join(o)
