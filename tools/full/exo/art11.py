"""New drawings for Exodus chapter 11 (Exodus 35–38): the congregation assembled, the willing offering carried in, the
wise-hearted women spinning, the gifts more than enough, the laver made of the women's mirrors, and the sum of the metals.
Scenes keep their figures in the right half (the words of a blueprint panel sit on the left), w x h panels."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, ruth1 as R
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman
from exo import art as A, art8 as B8, art9 as Q
def f(v): return f"{v:.1f}"

ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
WOMEN = ["#C2456A", "#5A6E8A", "#7A3A5A", "#2A5A6A", "#E8A317"]

def _scene(w, h, seed, base=0.9):
    b = h * base
    return b, [sun(w * 0.9, h * 0.16, 14, op=0.25), E4.sinai(w * 0.82, h * 0.54, w * 0.4, h * 0.44, seed, fire=False), ground(w, h, h * 0.54, "#8A6A4A", dy=0)]

def assembly(p, w, h, seed):
    """Moses assembled all the congregation: Moses with his hand raised before rows of the people."""
    r = random.Random(seed); b, o = _scene(w, h, seed)
    o.insert(0, mk.defs(p, *ALL))
    o.append(A.moses(p, w * 0.58, b, min(fit(b, h * 0.36), 1.1), up=T.POSES["raise"]))
    for row in range(2):
        for i in range(5):
            x = w * (0.66 + i * 0.07) + row * w * 0.03; y = b - row * h * 0.08; s = min(fit(y, h * 0.46), 1.0) * (1 - row * 0.15)
            o.append((woman if (i + row) % 2 else man)(p, x, y, s, r.choice(A.HEBREW + WOMEN), flip=True))
    return "".join(o)

def bringing(p, w, h, seed):
    """They came, both men and women, as many as were willing-hearted, and brought: a file of people with gifts toward a heap of gold, cloth and skins."""
    r = random.Random(seed); b, o = _scene(w, h, seed)
    o.insert(0, mk.defs(p, *ALL))
    hx = w * 0.62
    o.append(f'<path d="M{f(hx - 60)} {f(b + 4)} C {f(hx - 40)} {f(b - 50)} {f(hx + 40)} {f(b - 50)} {f(hx + 60)} {f(b + 4)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<rect x="{f(hx - 50 + i * 22)}" y="{f(b - 30 - (i % 2) * 10)}" width="20" height="14" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i, c in enumerate((B8.BLUE, B8.PURPLE, B8.SCARLET, B8.LINEN, "#A8322A")))
             + "".join(f'<circle cx="{f(hx + r.uniform(-40, 40))}" cy="{f(b - r.uniform(4, 30))}" r="4" fill="none" stroke="#FFF4C2" stroke-width="1.6"></circle>' for _ in range(10)))
    for i in range(5):
        x = w * (0.74 + i * 0.06); s = min(fit(b, h * 0.44), 1.0)
        o.append((woman if i % 2 else man)(p, x, b, s, r.choice(A.HEBREW + WOMEN), flip=True, up=[(-22, -158), (-36, -150), (-56, -150)]))
        o.append(f'<ellipse cx="{f(x - 58 * s)}" cy="{f(b - 150 * s)}" rx="{f(14 * s)}" ry="{f(9 * s)}" fill="{r.choice(["#E8B830", B8.BLUE, B8.SCARLET, "#C8C8D0"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def spindle(x, y, s, flip=False):
    """A drop spindle on its thread."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M0 -60 L 0 0" stroke="#F3EFE6" stroke-width="1.4"></path>'
            '<path d="M0 0 L 0 26" stroke="#8A5A3E" stroke-width="3"></path><ellipse cx="0" cy="18" rx="9" ry="4" fill="#B5793A" stroke="#0D0D0F" stroke-width="1.2"></ellipse></g>')

def spinning(p, w, h, seed, goats=False):
    """All the women that were wise-hearted did spin with their hands: women seated with spindles, skeins of blue, purple and scarlet; goats' hair."""
    r = random.Random(seed); b, o = _scene(w, h, seed)
    o.insert(0, mk.defs(p, *ALL))
    for i in range(3):
        x = w * (0.62 + i * 0.13); s = min(fit(b, h * 0.42), 1.0)
        o.append(woman(p, x, b, s, WOMEN[i], flip=i % 2 == 1, up=[(-22, -158), (-30, -186), (-40, -200)]) + spindle(x - 40 * s * (-1 if i % 2 else 1), b - 200 * s, s * 0.9))
        c = "#3A3430" if goats else [B8.BLUE, B8.PURPLE, B8.SCARLET][i]
        o.append("".join(f'<ellipse cx="{f(x + 30 * s)}" cy="{f(b - 6 - k * 6)}" rx="{f(14 * s)}" ry="{f(5 * s)}" fill="none" stroke="{c}" stroke-width="{f(4 * s)}"></ellipse>' for k in range(3)))
    if goats: o.append(E.sheep(w * 0.94, b, min(0.5, h / 400), wool="#3A3430", face="#1A1210"))
    return "".join(o)

def enough(p, w, h, seed):
    """The people bring much more than enough: gifts heaped past the workmen's benches; the proclamation through the camp."""
    r = random.Random(seed); b, o = _scene(w, h, seed)
    o.insert(0, mk.defs(p, *ALL))
    for k in range(3):
        hx = w * (0.62 + k * 0.12)
        o.append(f'<path d="M{f(hx - 50)} {f(b + 4)} C {f(hx - 34)} {f(b - 70)} {f(hx + 34)} {f(b - 70)} {f(hx + 50)} {f(b + 4)} Z" fill="{["#E8B830", "#C8C8D0", "#B87333"][k]}" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(A.son("#6A7AD8", 3)(p, w * 0.56, b, min(fit(b, h * 0.4), 1.0), up=T.POSES["raise"]))
    return "".join(o)

def mirrors(w, h, seed=38):
    """The laver of brass and its base of brass, of the mirrors of the ministering women: round brass mirrors beside the laver."""
    r = random.Random(seed); o = [B8.bp(w, h), B8.title_bar(w, "THE LAVER · OF THE MIRRORS OF THE MINISTERING WOMEN")]
    b = h * 0.9
    o.append(Q.laver_shape(w * 0.86, b, min(1.0, h / 260)))
    for i in range(6):
        x, y = w * (0.56 + (i % 3) * 0.07), h * (0.42 + (i // 3) * 0.24)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(min(22, h * 0.07))}" fill="#D8935A" stroke="#0D0D0F" stroke-width="2"></circle><circle cx="{f(x - 5)}" cy="{f(y - 5)}" r="{f(min(8, h * 0.025))}" fill="#FFF4C2" opacity="0.6"></circle>'
                 f'<path d="M{f(x)} {f(y + min(22, h * 0.07))} L {f(x)} {f(y + min(40, h * 0.12))}" stroke="#5A3A22" stroke-width="5"></path>')
    o.append(f'<path d="M{f(w * 0.74)} {f(h * 0.6)} L {f(w * 0.8)} {f(h * 0.6)}" stroke="#FFD23F" stroke-width="2.4"></path><path d="M{f(w * 0.8)} {f(h * 0.6)} l -8 -5 l 0 10 Z" fill="#FFD23F"></path>')
    return "".join(o)

def metals(w, h):
    """The sum of the things for the tabernacle: gold 29 talents 730 shekels; silver 100 talents 1,775 shekels; brass 70 talents 2,400 shekels."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE SUM · TALENTS")]
    rows_ = [("GOLD", 29, "29 TALENTS · 730 SHEKELS", B8.GOLD), ("SILVER", 100, "100 TALENTS · 1,775 SHEKELS", B8.SILVER), ("BRASS", 70, "70 TALENTS · 2,400 SHEKELS", B8.BRASS)]
    x0, bw = w * 0.62, w * 0.34; rh = min(60, (h - 60) / 3)
    for i, (nm, val, txt, c) in enumerate(rows_):
        y = 44 + i * rh
        o.append(label(x0 - 8, y + rh * 0.55, nm, B8.CY, 10, "end") + f'<rect x="{f(x0)}" y="{f(y + rh * 0.15)}" width="{f(bw * val / 100)}" height="{f(rh * 0.5)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 + label(x0, y + rh * 0.92, txt, "#FFD23F", 8, "start", ls=0.06))
    return "".join(o)

def census(w, h):
    """A beka a head, that is, half a shekel, for every one from twenty years old and upward: 603,550 men."""
    o = [B8.bp(w, h), B8.title_bar(w, "A BEKA A HEAD · 603,550")]
    cx, cy = w * 0.66, h * 0.5; r = min(h * 0.22, w * 0.06)
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{B8.SILVER}" stroke="#0D0D0F" stroke-width="2"></circle><path d="M{f(cx)} {f(cy - r)} L {f(cx)} {f(cy + r)}" stroke="#D7261E" stroke-width="2.4" stroke-dasharray="4 3"></path>'
             + label(cx, cy + r + 16, "½ SHEKEL", B8.CY, 9))
    for i in range(40):
        x = w * (0.78 + (i % 8) * 0.025); y = h * (0.28 + (i // 8) * 0.12)
        o.append(f'<circle cx="{f(x)}" cy="{f(y - 8)}" r="3" fill="#E8E2D6"></circle><path d="M{f(x - 3)} {f(y - 4)} L {f(x + 3)} {f(y - 4)} L {f(x + 4)} {f(y + 6)} L {f(x - 4)} {f(y + 6)} Z" fill="#E8E2D6"></path>')
    o.append(label(w * 0.87, h * 0.92, "20 YEARS OLD AND UPWARD", B8.CY, 8))
    return "".join(o)
