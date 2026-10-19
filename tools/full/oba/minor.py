"""Shared helpers for the twelve minor prophets' volumes (Obadiah onward import it: `from oba.minor import *`).

Kit(G, code, book) binds the line builders and packers to one book:
    K = Kit(G, "OBAD", "Obadiah")
    K.cp(ref, frm, to, after)  a narration caption          K.cps("1:1-3")  one caption per verse
    K.gd(...)                   a Voice box (Jehovah's words) K.gds("1:2-4")  one Voice box per verse
    K.sg(...)                   a song line (the prophet)     K.sgs("1:2-4")
    K.sy(...)                   a speech box                  K.sys("1:2-4")
    K.j(kind, *parts)           one box from several cuts: K.j("god", ("1:7", "Thus saith"), "1:8")
    K.face(lines, tok, ...)     a face beside the words      K.drawn(lines, art, bg, ...)  the words over a drawing
    K.pack(segs, prefix, start, end=...)   discourse.pack with the book's names
The panel's verse label is worked out from the cuts made for its lines (pass ref= to override).

cover_page(...) builds a volume cover; vista(w, h, seed, ...) composes a landscape (sky, hills, a far mountain or crag, a
walled city whole, burning or ruined, a river, the sea and ships, fields, trees, flocks and figures); plate(...) sets a
luminous symbolic drawing on a night grid (the visions). God is never drawn: his words are in the Voice box, and his
presence is light, cloud, storm or fire."""
import sys, pathlib, math, random, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J
from faces_ex import F
from discourse import seg, pack as _pack
import speech
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from genesis.art2 import fit, ground, hills, bird, birds, SKIN, WHITE_BEARD
from genesis.art3 import sun, label, man, woman, grid_bg, node, route, GREY_BEARD, flock
from exo import art as A
from num.art import ALL
from sa2.art import sky
from kg1.art import ship, temple_front, prophet_fig
from ecc.art import tree, wind_lines, hgrad
from job.art import smoke, clouds

def f(v): return f"{v:.1f}"
EP = ["", "第一話", "第二話", "第三話", "第四話", "第五話", "第六話"]
DUSK = "radial-gradient(circle at 70% 30%, #FFB04A 0 20px, #8A3A5A 200px, #1A1028 420px)"
DAWN = "radial-gradient(circle at 70% 30%, #FFF4C2 0 24px, #8FD0E2 170px, #2A4A6A 420px)"
NIGHT = "#0F0E2A"
BLACK_BEARD = A.BLACK_BEARD

# ---- lines and panels -----------------------------------------------------------------------------------------------------
def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]

def _flat(lines):
    out = []
    for l in lines:
        if isinstance(l, list): out += _flat(l)
        elif l: out.append(l)
    return out

class Kit:
    def __init__(self, G, code, book):
        self.G, self.code, self.book, self.ptr = G, code, book, 0

    # single cuts
    def cp(self, ref, frm=None, to=None, after=None): return ("cap", self.G.v(ref, frm=frm, to=to, after=after))
    def gd(self, ref, frm=None, to=None, after=None): return ("god", self.G.v(ref, frm=frm, to=to, after=after))
    def sg(self, ref, frm=None, to=None, after=None): return ("song", self.G.v(ref, frm=frm, to=to, after=after))
    def sy(self, ref, frm=None, to=None, after=None): return ("say", self.G.v(ref, frm=frm, to=to, after=after))
    # one box per verse
    def cps(self, refs): return [self.cp(r) for r in _refs(refs)]
    def gds(self, refs): return [self.gd(r) for r in _refs(refs)]
    def sgs(self, refs): return [self.sg(r) for r in _refs(refs)]
    def sys(self, refs): return [self.sy(r) for r in _refs(refs)]
    # one box for a run of verses
    def gdj(self, refs): return ("god", self.G.span(refs))
    def cpj(self, refs): return ("cap", self.G.span(refs))
    def j(self, kind, *parts):
        """One box from several cuts: j("god", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
        return (kind, " ".join(self.G.v(p) if isinstance(p, str) else self.G.v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

    def label(self):
        """The verses cut since the last panel, as 'OBAD 1:2–4' (or '1:16–2:2' across chapters)."""
        cuts = self.G.cuts[self.ptr:]; self.ptr = len(self.G.cuts)
        ks = sorted({tuple(map(int, r.split(":"))) for r, _ in cuts})
        if not ks: return None
        (c0, v0), (c1, v1) = ks[0], ks[-1]
        rng = f"{c0}:{v0}" if (c0, v0) == (c1, v1) else (f"{c0}:{v0}–{v1}" if c0 == c1 else f"{c0}:{v0}–{c1}:{v1}")
        return f"{self.code} {rng}"

    def face(self, lines, tok, bg=GOLDEN, ref=None, **k):
        lab = self.label()
        return seg(_flat(lines), ref or lab, tok=tok, bg=bg, **k)

    def drawn(self, lines, art, bg, ref=None, k=None, **kw):
        """Words at the top of the panel, the drawing fn(w, h) filling the room below them."""
        lab = self.label(); lines = _flat(lines)
        if "h" not in kw and lines and sum(len(t) for _, t in lines) < 160: kw["h"] = 250     # a short caption still gets a real picture
        return seg(lines, ref or lab, bg=bg, art=under(art, lines, k) if lines else art, **kw)

    def pic(self, art, bg, h, ref=None, **kw):
        """A picture panel without words, of height h."""
        return seg([], ref, bg=bg, art=art, h=h, **kw)

    def pack(self, segs, prefix, start, end="", default_head=None, min_size=12.5, most=3, budget=1150, min_art=200):
        """Group the panels into pages greedily: a panel joins the page while every panel's words still fit at min_size
        or more, the page holds fewer than `most` panels and about `budget` characters; a head starts a new page once
        the page holds a fair share of words. A lone short panel at the end joins the page before it when it fits."""
        from discourse import _sizes, _chars, _heights
        def fits(g):
            """Every panel's words at min_size or more, and every drawing tall enough to be a real picture."""
            if len(g) == 1: return True
            if min(_sizes(g)) < min_size: return False
            return all(hh >= (min_art if s["tok"] is None and s["art"] is not None else 170) for s, hh in zip(g, _heights(g)))
        n, INF = len(segs), float("inf")
        best, cut = [0.0] + [INF] * n, [0] * (n + 1)
        for j in range(1, n + 1):                      # best partition of segs[:j] into pages (fewest, fullest pages)
            for i in range(max(0, j - most), j):
                g = segs[i:j]; chars = sum(_chars(x) for x in g)
                if best[i] == INF or (len(g) > 1 and (chars > budget or not fits(g))): continue
                under = max(0.0, (budget * 0.8 - chars) / budget)
                cost = best[i] + 1 + 3 * under * under + sum(0.25 for x in g[1:] if x["head"])
                if cost < best[j]: best[j], cut[j] = cost, i
        groups, j = [], n
        while j > 0: groups.insert(0, segs[cut[j]:j]); j = cut[j]
        out, head = [], default_head or ""
        for i, g in enumerate(groups):
            pages = _pack(g, prefix, start + len(out), book=self.book, code=self.code, budget=10 ** 9, most=99, default_head=head,
                          end=end if i == len(groups) - 1 else "")
            for name, t, fn in pages:
                out.append((f"{prefix}-P{len(out) + 1:02d}-" + name.split("-P01-", 1)[1], t, fn))
            head = next((s["head"] for s in reversed(g) if s["head"]), head)
        return out

    def paged(self, groups, prefix, start, end="", **k):
        """Each group of segments on a page of its own (pack may still split one that will not fit)."""
        out, head = [], ""
        for i, g in enumerate(groups):
            out += self.pack(g, f"{prefix}{chr(65 + i)}", start + len(out), default_head=head, end=end if i == len(groups) - 1 else "", most=99, budget=10 ** 9, **k)
            head = next((s["head"] for s in reversed(g) if s["head"]), head)
        return out

def under(fn, lines, k=None):
    """A drawing fn(w, h) set just under the column of words at the top of its panel."""
    def art(w, h):
        kk = k
        if kk is None:
            bw = w - 24
            s = speech.fit(lines, bw, h * 0.62)
            kk = min(0.62, (speech._height(lines, bw, s) + 34 + 10) / h)
        return f'<g transform="translate(0 {h * kk:.1f})">' + fn(w, h * (1 - kk)) + '</g>'
    return art

def title(num, name, rng, svg, bg, quote, credit):
    return chapter_title(num, EP[num], name, rng, shade(svg), bg, quote, credit)

def nxt(text): return end_mark(text, "right: 10px; bottom: 34px")
def fin(text): return end_mark(text, "right: 10px; bottom: 34px", ch="完")

# ---- the cover ------------------------------------------------------------------------------------------------------------
def cover_page(name, vol_word, vol_no, chapters, kanji, romaji, quote, scene, bg="#1A1028", band="26,16,40"):
    """A volume cover: THE BOOK OF / NAME in Anton, the volume and chapters, the kanji block, one ASV line, a full-bleed
    scene (an svg string drawn at 760 × 1080)."""
    n = len(name)
    fs = min(150, int(640 / (0.5 * n)))
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">{scene}</svg>'
           f'<div style="position: absolute; left: 0; right: 0; top: 0; height: 470px; background: linear-gradient(180deg, rgba({band},1) 0%, rgba({band},0.82) 62%, rgba({band},0) 100%)"></div>')
    ks = "".join(f"<span>{c}</span>" for c in kanji)
    body = svg + f'''
  <div data-label="" style="position: absolute; top: 40px; left: 38px; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">THE BOOK OF</div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: {fs}px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">{name.upper()}</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>{vol_word}</span>
    <span style="font-weight: 500; opacity: 0.85">{chapters}</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.02; color: #F3EFE6">{ks}</span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.1em; color: #F3EFE6; text-align: center">{romaji}</span>
  </div>
  <div style="position: absolute; left: 38px; top: 322px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 330px; line-height: 1.45">{quote}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. {vol_no}</span>
  </div>'''
    root = f"position: relative; width: 760px; height: 1080px; overflow: hidden; background: {bg}; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page(f"{name} — {vol_word}", None, body, root_style=root)

# ---- drawing primitives ---------------------------------------------------------------------------------------------------
TONES = {"dawn": ("#2A2A5A", "#FFB07A"), "day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#2A1A3A", "#E8803A"), "night": ("#05051A", "#1E1650"),
         "storm": ("#14141E", "#4A4A5E"), "fire": ("#2A0A0A", "#C8401A"), "gold": ("#FFE680", "#FFC14D"), "grey": ("#4A4A5A", "#B8A8A0"),
         "desert": ("#FFE6A0", "#E8B880"), "dark": ("#05050E", "#1A1420"), "red": ("#3A0A10", "#8A2A1A"), "noon": ("#5AB0D8", "#FFF4C2")}
HILL = {"dawn": ("#3A2A4A", "#5A3A4A"), "day": ("#8A9A6A", "#6A8A4A"), "dusk": ("#4A2A3A", "#3A1E2A"), "night": ("#14142E", "#0D0D1E"),
        "storm": ("#2A2A36", "#1E1E28"), "fire": ("#3A1410", "#1E0A08"), "gold": ("#C8904A", "#A8703A"), "grey": ("#6A6060", "#4A4444"),
        "desert": ("#C8985A", "#B8804A"), "dark": ("#14101A", "#0A080E"), "red": ("#3A1418", "#24080C"), "noon": ("#9AA86A", "#7A8A4A")}
EARTH = {"dawn": "#6A4A4A", "day": "#B8A86A", "dusk": "#4A2E2A", "night": "#1A1830", "storm": "#2E2A2E", "fire": "#2A100C", "gold": "#C8A06A",
         "grey": "#7A6E64", "desert": "#D8B880", "dark": "#100C14", "red": "#2A1014", "noon": "#C8B87A"}

def glow(p, sd=6):
    return f'<defs><filter id="{p}gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{sd}" result="b"></feGaussianBlur><feMerge><feMergeNode in="b"></feMergeNode><feMergeNode in="SourceGraphic"></feMergeNode></feMerge></filter></defs>'

def halo(x, y, r, color="#FFE680", op=0.5):
    return "".join(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * k)}" fill="{color}" opacity="{op * (1.1 - k) / 1.1:.2f}"></circle>' for k in (1.0, 0.7, 0.45, 0.25))

def rays(x, y, n, r0, r1, color="#FFF4C2", op=0.3, sw=3, a0=0, a1=360):
    o = []
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * (i + 0.5) / n)
        o.append(f'<path d="M{f(x + r0 * math.cos(a))} {f(y + r0 * math.sin(a))} L {f(x + r1 * math.cos(a))} {f(y + r1 * math.sin(a))}" stroke="{color}" stroke-width="{sw}" opacity="{op}"></path>')
    return "".join(o)

def starfield(w, h, seed, n=60, y1=0.6):
    r = random.Random(seed)
    return "".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h * y1))}" r="{f(r.uniform(0.6, 2.0))}" fill="#F3EFE6" opacity="{r.uniform(0.4, 1):.2f}"></circle>' for _ in range(n))

def crag(x0, x1, base, top, seed, color="#B5583A", dark="#7A3420", doors=4):
    """Edom's rock: a red sandstone cliff with strata and dwellings cut into its face (the clefts of the rock)."""
    r = random.Random(seed); wd = x1 - x0
    pts = [(x0, base)]
    for i in range(9):
        t = (i + 0.5) / 9
        pts.append((x0 + wd * (t - 0.04 + r.uniform(-0.02, 0.02)), top + (base - top) * (0.25 * abs(t - 0.45) * 2 + r.uniform(0, 0.12))))
        pts.append((x0 + wd * (t + 0.03), top + (base - top) * (0.25 * abs(t - 0.45) * 2 + r.uniform(0.0, 0.08))))
    pts.append((x1, base))
    d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
    o = [f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for k in range(1, 7):                                   # strata
        y = top + (base - top) * k / 7
        o.append(f'<path d="M{f(x0 + wd * 0.04)} {f(y)} C {f(x0 + wd * 0.3)} {f(y - 8)} {f(x0 + wd * 0.6)} {f(y + 8)} {f(x1 - wd * 0.04)} {f(y - 2)}" stroke="{dark}" stroke-width="2" fill="none" opacity="0.6"></path>')
    for k in range(3):                                      # clefts
        cx = x0 + wd * r.uniform(0.15, 0.85)
        o.append(f'<path d="M{f(cx)} {f(top + (base - top) * 0.2)} L {f(cx + r.uniform(-14, 14))} {f(top + (base - top) * 0.55)} L {f(cx + r.uniform(-10, 10))} {f(base)}" stroke="#2A0E08" stroke-width="3" fill="none"></path>')
    s = min((base - top) / 300, wd / 640) * 0.8
    for i in range(doors):                                  # rock-cut houses
        cx = x0 + wd * (0.18 + 0.64 * i / max(1, doors - 1)); y = top + (base - top) * (0.42 + 0.3 * ((i * 7) % 3) / 3)
        dw, dh = 34 * s, 56 * s
        o.append(f'<path d="M{f(cx - dw)} {f(y)} L {f(cx - dw)} {f(y - dh)} L {f(cx)} {f(y - dh - 16 * s)} L {f(cx + dw)} {f(y - dh)} L {f(cx + dw)} {f(y)} Z" fill="#D8784A" stroke="#0D0D0F" stroke-width="1.8"></path>'
                 f'<rect x="{f(cx - dw * 0.36)}" y="{f(y - dh * 0.7)}" width="{f(dw * 0.72)}" height="{f(dh * 0.7)}" fill="#1A0A06"></rect>'
                 + "".join(f'<rect x="{f(cx + dx * dw * 0.8 - 3 * s)}" y="{f(y - dh)}" width="{f(6 * s)}" height="{f(dh)}" fill="#E8906A" stroke="#0D0D0F" stroke-width="1"></rect>' for dx in (-1, 1)))
    return "".join(o)

def eagle(x, y, s=1.0, color="#2A1A14", flip=False):
    """An eagle soaring, wings spread."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M0 0 C -20 -14 -50 -30 -96 -26 C -80 -18 -70 -12 -64 -4 C -76 -2 -86 4 -92 10 C -60 6 -30 4 -10 8 L -18 26 L 0 18 L 18 26 L 10 8 '
            'C 30 4 60 6 92 10 C 86 4 76 -2 64 -4 C 70 -12 80 -18 96 -26 C 50 -30 20 -14 0 0 Z" '
            f'fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M0 -4 C 4 -12 10 -14 14 -10 L 22 -8 L 14 -4 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>'
            '<path d="M22 -8 L 26 -6 L 21 -4 Z" fill="#E8B830"></path></g>')

def walls(x0, x1, base, hh, seed, color="#C8A878", lit=False, gate=True, houses=True, towers=3):
    """A walled city: houses behind, a wall with battlements and towers, a gate."""
    r = random.Random(seed); o = []; wd = x1 - x0
    if houses:
        x = x0 + 6
        while x < x1 - 20:
            bw = r.uniform(26, 54) * hh / 80; bh = r.uniform(0.5, 1.1) * hh
            o.append(f'<rect x="{f(x)}" y="{f(base - hh * 0.62 - bh)}" width="{f(bw)}" height="{f(bh + 4)}" fill="{r.choice(["#E8D0A0", "#D8C090", "#C8B088"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
            if r.random() < 0.6:
                o.append(f'<rect x="{f(x + bw * 0.4)}" y="{f(base - hh * 0.62 - bh + bh * 0.3)}" width="{f(max(3, bw * 0.16))}" height="{f(max(4, bh * 0.2))}" fill="{"#FFC14D" if lit else "#3A2214"}"></rect>')
            x += bw + r.uniform(-4, 6)
    top = base - hh * 0.62
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(wd)}" height="{f(hh * 0.62)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></rect>')
    bw = max(8, hh * 0.1); xx = x0
    while xx < x1 - bw:
        o.append(f'<rect x="{f(xx)}" y="{f(top - bw)}" width="{f(bw)}" height="{f(bw + 1)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></rect>'); xx += bw * 1.9
    for i in range(towers):
        tx = x0 + wd * (i + 0.5) / towers; tw = hh * 0.34
        o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(top - hh * 0.3)}" width="{f(tw)}" height="{f(hh * 0.92)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></rect>'
                 f'<rect x="{f(tx - tw * 0.12)}" y="{f(top - hh * 0.18)}" width="{f(tw * 0.24)}" height="{f(hh * 0.12)}" fill="{"#FFC14D" if lit else "#2A140C"}"></rect>')
    if gate:
        gx = x0 + wd * (0.5 / towers + 0.5 / towers) if towers > 1 else x0 + wd * 0.3
        gx = (x0 + wd * 0.5 / towers + x0 + wd * 1.5 / towers) / 2 if towers > 1 else x0 + wd * 0.3
        gw = hh * 0.22
        o.append(f'<path d="M{f(gx - gw)} {f(base)} L {f(gx - gw)} {f(base - hh * 0.36)} Q {f(gx)} {f(base - hh * 0.56)} {f(gx + gw)} {f(base - hh * 0.36)} L {f(gx + gw)} {f(base)} Z" fill="#1A0E08" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def fires(x0, x1, base, hh, seed, n=5):
    return "".join(E.blaze(x0 + (x1 - x0) * (i + 0.5) / n, base, (x1 - x0) / n * 1.2, hh * random.Random(seed + i).uniform(0.7, 1.1), seed + i, n=6) for i in range(n))

def smokes(xs, y, seed, k=1.0, color="#3A2A2E", op=0.6, n=8):
    return "".join(smoke(x, y, n, seed + i, color=color, op=op, k=k) for i, x in enumerate(xs))

def ruin(x0, x1, base, hh, seed, color="#A8906A"):
    """Broken walls and fallen stones (nothing living drawn)."""
    r = random.Random(seed); o = []
    x = x0
    while x < x1:
        bw = r.uniform(30, 70) * hh / 90; bh = r.uniform(0.2, 1.0) * hh
        jag = f"M{f(x)} {f(base)} L {f(x)} {f(base - bh)} L {f(x + bw * 0.3)} {f(base - bh * r.uniform(0.7, 1.0))} L {f(x + bw * 0.6)} {f(base - bh * r.uniform(0.5, 0.9))} L {f(x + bw)} {f(base - bh * r.uniform(0.2, 0.6))} L {f(x + bw)} {f(base)} Z"
        o.append(f'<path d="{jag}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>')
        x += bw + r.uniform(10, 40) * hh / 90
    for _ in range(int((x1 - x0) / 30)):
        cx = r.uniform(x0, x1); s = r.uniform(5, 12) * hh / 90
        o.append(f'<rect x="{f(cx)}" y="{f(base - s)}" width="{f(s * 1.6)}" height="{f(s)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({r.randint(-20, 20)} {f(cx)} {f(base)})"></rect>')
    return "".join(o)

def river(w, y, th, color="#2C7DA8", foam="#BFE6F2", seed=1):
    r = random.Random(seed)
    o = [f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - th * 0.4)} {f(w * 0.6)} {f(y + th * 0.4)} {f(w + 10)} {f(y)} L {f(w + 10)} {f(y + th)} C {f(w * 0.6)} {f(y + th * 1.3)} {f(w * 0.3)} {f(y + th * 0.6)} -10 {f(y + th)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>']
    for _ in range(6):
        x = r.uniform(0, w * 0.9)
        o.append(f'<path d="M{f(x)} {f(y + th * 0.5)} l {f(r.uniform(20, 50))} -2" stroke="{foam}" stroke-width="2" opacity="0.7"></path>')
    return "".join(o)

def sea(w, h, y, seed, color="#1F6F9A", deep="#0B2E4A", foam="#CFEFFF", rough=False):
    r = random.Random(seed)
    o = [f'<rect x="-10" y="{f(y)}" width="{f(w + 20)}" height="{f(h - y + 10)}" fill="{color}"></rect>',
         f'<rect x="-10" y="{f(y + (h - y) * 0.5)}" width="{f(w + 20)}" height="{f(h)}" fill="{deep}" opacity="0.5"></rect>']
    amp = 14 if rough else 4
    for k in range(7 if rough else 5):
        yy = y + (h - y) * (k + 0.5) / 7
        d = f"M-10 {f(yy)}" + "".join(f" Q {f(x + 20)} {f(yy - amp * r.uniform(0.6, 1.2))} {f(x + 40)} {f(yy)}" for x in range(-10, int(w) + 40, 40))
        o.append(f'<path d="{d}" stroke="{foam}" stroke-width="{2.4 if rough else 1.6}" fill="none" opacity="0.7"></path>')
    return "".join(o)

def grain(x0, x1, base, hh, seed, color="#E8C060", n=None):
    r = random.Random(seed); o = []
    n = n or int((x1 - x0) / 7)
    for i in range(n):
        x = x0 + (x1 - x0) * i / n + r.uniform(-2, 2); t = base - hh * r.uniform(0.75, 1.0)
        o.append(f'<path d="M{f(x)} {f(base)} L {f(x + r.uniform(-4, 4))} {f(t)}" stroke="#A8803A" stroke-width="1.6"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(t)}" rx="{f(hh * 0.035 + 1.5)}" ry="{f(hh * 0.09 + 3)}" fill="{color}" stroke="#7A5A1A" stroke-width="1"></ellipse>')
    return "".join(o)

def vines(x0, x1, y0, y1, seed, rows=3, fruit=True, bare=False):
    r = random.Random(seed); o = []
    for k in range(rows):
        y = y0 + (y1 - y0) * k / max(1, rows - 1); s = 0.6 + 0.5 * k / max(1, rows - 1)
        x = x0
        while x < x1:
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 30 * s)}" stroke="#5A3A22" stroke-width="{f(3 * s)}"></path>')
            if not bare:
                o.append(f'<ellipse cx="{f(x)}" cy="{f(y - 34 * s)}" rx="{f(20 * s)}" ry="{f(12 * s)}" fill="#3F7A34" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
                if fruit and r.random() < 0.7:
                    o.append("".join(f'<circle cx="{f(x + r.uniform(-8, 8) * s)}" cy="{f(y - 24 * s + r.uniform(0, 8) * s)}" r="{f(3 * s)}" fill="#5A1A5A"></circle>' for _ in range(4)))
            else:
                o.append(f'<path d="M{f(x)} {f(y - 28 * s)} l -12 -10 M{f(x)} {f(y - 26 * s)} l 12 -12" stroke="#5A3A22" stroke-width="2"></path>')
            x += 40 * s
    return "".join(o)

def fig_tree(x, y, s=1.0, bare=False, fruit=True, seed=1):
    r = random.Random(seed)
    o = f'<path d="M{f(x)} {f(y)} C {f(x - 6 * s)} {f(y - 40 * s)} {f(x + 6 * s)} {f(y - 70 * s)} {f(x)} {f(y - 90 * s)} M{f(x)} {f(y - 70 * s)} L {f(x - 40 * s)} {f(y - 110 * s)} M{f(x)} {f(y - 75 * s)} L {f(x + 44 * s)} {f(y - 112 * s)}" stroke="#6A5040" stroke-width="{f(8 * s)}" fill="none" stroke-linecap="round"></path>'
    if not bare:
        for _ in range(9):
            lx, ly = x + r.uniform(-60, 60) * s, y - r.uniform(96, 150) * s
            o += f'<path d="M{f(lx)} {f(ly)} c {f(-14 * s)} {f(-6 * s)} {f(-16 * s)} {f(-26 * s)} 0 {f(-30 * s)} c {f(16 * s)} {f(4 * s)} {f(14 * s)} {f(24 * s)} 0 {f(30 * s)} Z" fill="#3F7A34" stroke="#0D0D0F" stroke-width="1.6"></path>'
            if fruit and r.random() < 0.5:
                o += f'<circle cx="{f(lx + 6 * s)}" cy="{f(ly + 4 * s)}" r="{f(5 * s)}" fill="#6A3A6A" stroke="#0D0D0F" stroke-width="1"></circle>'
    return o

def olive(x, y, s=1.0, seed=1):
    return tree(x, y, s, color="#7A8A5A", seed=seed)

def figure(p, x, base, top, cloth="#6A5A4A", kind="man", flip=False, up=None, beard=None):
    """A standing figure on base reaching up to top: kind man / woman / prophet (headcloth and beard)."""
    s = fit(base, top)
    if kind == "woman": return woman(p, x, base, s, cloth, flip=flip, up=up)
    if kind == "prophet": return prophet_fig(p, x, base, s, cloth=cloth, flip=flip, up=up, beard=beard or BLACK_BEARD)
    return man(p, x, base, s, cloth, flip=flip, up=up)

def crowd(p, x0, x1, base, top, n, seed, colors=("#6A4A3A", "#3A4A6A", "#5A6A3A", "#7A3A3A", "#4A3A5A"), women=0.4, flip=False, up=None):
    r = random.Random(seed); o = []
    for i in range(n):
        x = x0 + (x1 - x0) * (i + 0.5) / n + r.uniform(-6, 6); b = base + r.uniform(-4, 4)
        kind = "woman" if r.random() < women else "man"
        o.append(figure(p, x, b, top + r.uniform(-6, 10), r.choice(colors), kind, flip=flip if flip is not None else r.random() < 0.5, up=up))
    return "".join(o)

def sheep_row(x0, x1, base, n, seed, s=0.5):
    r = random.Random(seed)
    return "".join(E.sheep(x0 + (x1 - x0) * (i + 0.5) / n + r.uniform(-8, 8), base + r.uniform(-6, 6), s * r.uniform(0.85, 1.1), flip=r.random() < 0.5) for i in range(n))

def bolt(x, y0, y1, seed, color="#FFF4C2", sw=4):
    r = random.Random(seed); pts = [(x, y0)]; y = y0
    while y < y1:
        y += (y1 - y0) / 6; pts.append((pts[-1][0] + r.uniform(-24, 24), y))
    d = "M" + " L ".join(f"{f(a)} {f(b)}" for a, b in pts)
    return f'<path d="{d}" stroke="{color}" stroke-width="{sw + 4}" fill="none" opacity="0.3"></path><path d="{d}" stroke="{color}" stroke-width="{sw}" fill="none"></path>'

def rain(w, h, seed, n=60, color="#BFD8F2", op=0.5):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(x)} {f(y)} l -6 22" stroke="{color}" stroke-width="1.6" opacity="{op}"></path>' for x, y in ((r.uniform(0, w + 30), r.uniform(-10, h)) for _ in range(n)))

def cup(x, y, s=1.0, color="#E8B830", spill=False):
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-40 -90 L 40 -90 C 36 -40 20 -30 8 -26 L 8 -6 L 30 0 L -30 0 L -8 -6 L -8 -26 C -20 -30 -36 -40 -40 -90 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.6"></path>'
         '<ellipse cx="0" cy="-90" rx="40" ry="8" fill="#5A0A1A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    if spill: o += '<path d="M36 -88 C 50 -80 52 -60 48 -40 C 46 -30 54 -22 50 -12" stroke="#7A0A1A" stroke-width="6" fill="none" stroke-linecap="round"></path>'
    return o + '</g>'

def scroll(x, y, w, h, color="#F3E8C8", lines=6, seal=None):
    """An open scroll (rolled at both ends) with ruled lines of writing (no words)."""
    o = [f'<rect x="{f(x - w / 2)}" y="{f(y - h / 2)}" width="{f(w)}" height="{f(h)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for side in (-1, 1):
        cx = x + side * w / 2
        o.append(f'<rect x="{f(cx - 10)}" y="{f(y - h / 2 - 8)}" width="20" height="{f(h + 16)}" rx="9" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.2"></rect>')
    for k in range(lines):
        yy = y - h / 2 + h * (k + 1) / (lines + 1)
        o.append(f'<path d="M{f(x - w / 2 + 18)} {f(yy)} L {f(x + w / 2 - 18 - (k % 3) * 14)} {f(yy)}" stroke="#3A2A1A" stroke-width="2.2" stroke-dasharray="10 4 22 4 6 4" opacity="0.8"></path>')
    if seal: o.append(f'<circle cx="{f(x + w * 0.3)}" cy="{f(y + h * 0.36)}" r="10" fill="{seal}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    return "".join(o)

def mount_zion(cx, base, wd, hh, seed, color="#8A6A4A", lit=False):
    """Mount Zion: a hill with the walled city on it and the house of Jehovah at the top."""
    o = [f'<path d="M{f(cx - wd)} {f(base)} C {f(cx - wd * 0.5)} {f(base - hh)} {f(cx + wd * 0.5)} {f(base - hh)} {f(cx + wd)} {f(base)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></path>']
    o.append(walls(cx - wd * 0.62, cx + wd * 0.62, base - hh * 0.5, hh * 0.32, seed, lit=lit, towers=3))
    o.append(temple_front(cx + wd * 0.1, base - hh * 0.72, wd * 0.36, seed))
    return "".join(o)

# ---- the composer -----------------------------------------------------------------------------------------------------------
def vista(w, h, seed, tone="day", horizon=0.62, sun_at=None, moon_at=None, stars=False, hills_n=2, far=None, city=None, cx=0.62, cw=0.5,
          river_=False, sea_=False, ships=0, fire=0, smoke_=0, ruins=False, field=None, trees=0, tree_kind="olive", sheep=0, birds_=0,
          rain_=False, bolts=0, people=None, p=None, eagle_=None, glow_at=None, ground_=True):
    """A landscape: far= 'crag' (Edom's rock), 'zion' (the mount with the city and the house), 'mount' (a high mountain),
    'carmel' (wooded heights); city= 'walls', 'lit', 'burning', 'ruin', 'empty' (gates open, no one); people= [(x, kind,
    cloth[, flip, up])] standing on the ground (kind man / woman / prophet / kneel)."""
    r = random.Random(seed)
    top, bot = TONES[tone]; hc1, hc2 = HILL[tone]; ec = EARTH[tone]
    y = h * horizon
    o = [mk.defs(p, *ALL) if p and people else "", sky(w, h, top, bot)]
    if stars: o.append(starfield(w, h, seed, 50, horizon))
    if glow_at: o.append(halo(w * glow_at[0], h * glow_at[1], max(w, h) * glow_at[2], color=glow_at[3] if len(glow_at) > 3 else "#FFE680", op=0.6))
    if sun_at: o.append(sun(w * sun_at[0], h * sun_at[1], max(14, min(w, h) * 0.07), color="#FFE680" if tone not in ("fire", "red", "dusk") else "#FF8A3D", op=0.5))
    if moon_at: o.append(J.moon(w * moon_at[0], h * moon_at[1], max(10, min(w, h) * 0.04)))
    if bolts:
        for i in range(bolts): o.append(bolt(w * r.uniform(0.15, 0.85), 0, y * r.uniform(0.6, 0.95), seed + i))
    if hills_n >= 2: o.append(hills(w, h, y - h * 0.08, seed, color=hc1, amp=18, step=80))
    if far == "crag": o.append(crag(w * (cx - cw / 2), w * (cx + cw / 2), y + h * 0.04, h * 0.1, seed))
    elif far == "zion": o.append(mount_zion(w * cx, y + h * 0.02, w * cw / 2, h * 0.4, seed, lit=tone in ("night", "dusk")))
    elif far == "mount": o.append(f'<path d="M{f(w * (cx - cw / 2))} {f(y + 4)} L {f(w * (cx - 0.04))} {f(h * 0.14)} L {f(w * cx)} {f(h * 0.1)} L {f(w * (cx + 0.05))} {f(h * 0.16)} L {f(w * (cx + cw / 2))} {f(y + 4)} Z" fill="{hc2}" stroke="#0D0D0F" stroke-width="2.2"></path>')
    if hills_n >= 1: o.append(hills(w, h, y, seed + 1, color=hc2, amp=12, step=70))
    if city:
        base = y + h * 0.05; hh = h * 0.26
        x0, x1 = w * (cx - cw / 2), w * (cx + cw / 2)
        if city == "ruin": o.append(ruin(x0, x1, base, hh * 0.8, seed))
        else: o.append(walls(x0, x1, base, hh, seed, lit=city in ("lit",), gate=True, towers=3 if cw > 0.35 else 2,
                             color="#8A6A5A" if city == "burning" else "#C8A878"))
        if city == "burning": o.append(fires(x0, x1, base - hh * 0.5, hh * 0.9, seed, n=5))
    if smoke_: o.append(smokes([w * r.uniform(0.15, 0.85) for _ in range(smoke_)], y, seed, k=max(0.6, h / 300)))
    if ground_: o.append(ground(w, h, y + h * 0.05, ec, dy=0))
    if river_: o.append(river(w, y + h * 0.1, h * 0.08, seed=seed))
    if sea_:
        o.append(sea(w, h, y + h * 0.02, seed, rough=tone in ("storm", "dark")))
        for i in range(ships): o.append(ship(w * (0.25 + 0.5 * i / max(1, ships - 1)) if ships > 1 else w * 0.5, y + h * 0.16, min(1.0, h / 400), flip=i % 2 == 1))
    if fire: o.append(fires(w * 0.02, w * 0.98, y + h * 0.1, h * 0.3, seed, n=fire))
    if field == "vines": o.append(vines(w * 0.04, w * 0.96, y + h * 0.12, h * 0.94, seed, rows=3))
    elif field == "bare": o.append(vines(w * 0.04, w * 0.96, y + h * 0.12, h * 0.94, seed, rows=3, bare=True))
    elif field == "grain": o.append(grain(-10, w + 10, y + h * 0.28, h * 0.2, seed) + grain(-10, w + 10, h * 0.98, h * 0.26, seed + 1))
    elif field == "stubble": o.append(grain(-10, w + 10, h * 0.96, h * 0.08, seed, color="#C8A060"))
    for i in range(trees):
        tx = w * (0.08 + 0.84 * (i + r.uniform(-0.2, 0.2)) / max(1, trees - 1)) if trees > 1 else w * 0.2
        k = min(1.0, h / 360) * r.uniform(0.7, 1.0)
        o.append(fig_tree(tx, h * 0.98, k, seed=seed + i) if tree_kind == "fig" else olive(tx, h * 0.98, k, seed=seed + i) if tree_kind == "olive" else tree(tx, h * 0.98, k, kind=tree_kind, seed=seed + i))
    if sheep: o.append(sheep_row(w * 0.1, w * 0.9, h * 0.92, sheep, seed, s=min(0.6, h / 600)))
    if birds_: o.append(birds(birds_, w * 0.1, w * 0.9, h * 0.08, h * 0.4, seed))
    if eagle_: o.append(eagle(w * eagle_[0], h * eagle_[1], eagle_[2] * min(1.0, h / 300)))
    if people:
        b = h * 0.96
        for spec in people:
            x, kind, cloth = spec[:3]; fl = spec[3] if len(spec) > 3 else False; up = spec[4] if len(spec) > 4 else None
            if kind == "kneel": o.append(E.kneel(w * x, b, fit(b, h * 0.5) * 0.9, color=cloth, flip=fl))
            else: o.append(figure(p, w * x, b, h * 0.36, cloth, kind, flip=fl, up=up))
    if rain_: o.append(rain(w, h, seed))
    return "".join(o)

def plate(p, w, h, body, title=None, tags=(), bg="#070720", grid="#1E2A5A", color="#8FD0E2"):
    """A luminous vision plate: a night grid, the drawing body (svg, already placed) glowing, a title tag and labels
    [(x, y, text)] in technical type."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{bg}"></rect>', grid_bg(w, h, color=grid, step=28, bg=bg) if True else "", glow(p, 5),
         f'<g filter="url(#{p}gl)">{body}</g>']
    if title: o.append(label(14, h - 14, title, color, 11))
    for x, y, t in tags: o.append(label(x, y, t, color, 10))
    return "".join(o)

UP_RIGHT = [(22, -158), (40, -176), (58, -196)]
UP_LEFT = [(-22, -158), (-40, -176), (-58, -196)]
