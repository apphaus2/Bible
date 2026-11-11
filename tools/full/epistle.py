"""The epistle kit: shared by the letters of the New Testament (Romans first, then 1 and 2 Corinthians, Galatians, …).
`from epistle import *` in a letter's common.py; drawings in its art.py start `from epistle import *` too (or from the
previous letter's art, which carries these).

A letter has no narration. Every word of scripture on its pages is one of three things:
  * the writer speaking to the reader — a LETTER box: warm parchment (#F6EEDA), a 2 px ink border, a sepia rule down the
    left edge, Archivo Narrow 700 (speech.py kind "letter"). Beside the writer's face the first letter box of the column
    carries a short sepia tail toward him (he dictates: Rom 16:22); over a drawing it is untailed;
  * scripture he quotes ("as it is written, …") — a song box, as Acts sets the speakers' quotations;
  * God's own words quoted in the first person ("I will have mercy on whom I have mercy", "As I live, saith the Lord") —
    the Voice box. Jesus' words, where a letter quotes them (1 Cor 11:24–25), are ordinary speech balloons (`say`).

    K = EpistleKit(G, "ROM", "Romans", credit="Romans · Volume Forty-Five")

Line builders (each a (kind, text) line cut from the ASV with G.v — never typed):
    K.lt(ref, frm=, to=, after=)   a letter box                 K.lts("1:8-10")  one letter box per verse
    K.ltj("1:8-10")                 one letter box for a run      K.lj(("1:17", None, "as it is written,"), "1:18")  one box from several cuts
    K.lp("1:24-31", most=280)       the verses as paragraphs: consecutive whole verses joined into boxes of up to ~280 letters
                                    (the usual builder: fewer, fuller boxes read as a letter and pack about 130 words a page)
    K.sg / K.sgs                   a song box (a quotation)      K.gd / K.gds   a Voice box (God speaking in the first person)
    K.sy                            a speech balloon (Jesus' words quoted)
    K.wq(ref, to, frm, kind="song") a verse in two boxes: the letter up to `to`, then the quotation from `frm` (song / god / say)
    K.qw(ref, to, frm, kind="song") the other way round: the quotation up to `to`, then the letter from `frm` ("…, even as it is written.")
Panels (discourse segments; a page holds two to four, packed by K.pack):
    K.F(lines, tok, bg=GOLD_BG, hi=18)  the words beside a face (tok: one of the faces below, or the letter's own cast), at
                                    most hi px
    K.D(lines, fn, bg, sky=n, art_h=130, size=15, h=)  the words over a drawing fn(w, h): the words at `size` px at most, the
                                    drawing at least art_h tall below them (give maps, plates and the study ~200–280);
                                    sky=n (or (n, "left")) sets chapter n's stamp in a band between the words and the drawing
    K.glory(lines, bg=GLORY_BG, h=) a doxology or benediction: the words over a burst of light (no figure), a gold inner frame
    K.pic(fn, bg, h)                a drawing with no words
    K.pack(segs, prefix, start, end=, most=4, lone=0.5, face_min=230)   the panels into pages (Mark's and Acts' packer:
                                    fewest, fullest pages, no drawing squeezed to a strip, no face panel under face_min px;
                                    tails removed from boxes over drawings)
    K.title(num, name, rng, svg, bg, quote)               a chapter opener (第一話 …) with the letter's credit
    nxt(text) / fin(text)           the end marks (つづく / 完) for the last panel of a chapter / of the letter
Faces (tok= for K.F), each with its background: Paul as ntcast draws him, in his moods —
    PAUL + GOLD_BG (earnest) · PAUL_LAMP + LAMP_BG (dictating by lamplight) · PAUL_GRIEF + GRIEF_BG (grieving: Rom 9:1–3)
    PAUL_JOY + JOY_BG (white light: Rom 8:31–39, 11:33–36) · PAUL_STERN + STERN_BG (warning, rebuke)
Drawings (svg strings; p is a prefix unique to the panel; w, h the panel's size):
    study(p, w, h, seed, stage=, scribe=, bearer=, night=, window=, writer=paul, fig_h=250)   the opening scene (also a
        good "Paul speaking" panel anywhere in a letter, between the face panels): the writer dictating, the scribe
        writing at a low table by lamplight. stage "dictate" (the writer standing, his hand out), "read" (the scribe holds
        up the sheet, the writer listening), "give" (the writer hands the sealed scroll to the bearer at the door).
        scribe / bearer: dicts of colours (cloth, head; bearer veil) or None (TERTIUS_LOOK, PHOEBE_LOOK are Romans');
        window "city" (roofs and a citadel by night); fig_h the tallest a figure may stand (a title page: ~330)
    still_life(w, h, seed, sealed=True, night=True)   the letter on the table: the rolled scroll tied and sealed, the reed
        pen, the inkpot, the lamp (an opening's or an ending's picture panel)
    sealed_scroll(x, y, s, rot=0, seal=SEAL)   a rolled letter tied with a cord and sealed with red clay
    open_letter(x, y, w, h, rows=7, seed=1)    a sheet of papyrus with lines of writing (no words)
    reed_pen(x, y, s, rot=-30) · inkpot(x, y, s) · lamp_glow(x, y, r, uid)
    letter_road(w, h, route, title, box=, places=, hi=)   the letter's road on Acts' map projection (act.geo): route a list
        of place names or (lon, lat) points, lit red
    plate_bg(w, h, title)           the technical-annotation ground for a diagram (navy grid, gold title bar); put the
        drawing on it with tag() callouts and dim() lines (exo.art8) — labels are svg text, not scripture
    radiance(w, h, seed, cx=0.5, cy=0.86, color=)   the burst of light behind a doxology
Greetings (Rom 16, 1 Cor 16, Col 4 …):
    greetings(items, prefix, start, book, code, head=, end=)  pages of cells, one per person greeted, packed by height:
        items = [(name, tag, lines, portrait), …] — name in Anton and tag (one short line, e.g. "16:3–5 · IN CHRIST JESUS")
        are labels (data-label); lines are the verse(s) as letter boxes; portrait(p, w, h) draws the person small (a figure
        at a distance on a coloured ground, or an emblem) in the cell's left square. Returns [(file, board title, fn)] like
        K.pack, so PG.extend(greetings(...)) puts them in the chapter.
    portrait(fig, bg=, floor=)      a portrait function from fig(p, x, y, s) (any act.art / rom.art figure)"""
import sys, pathlib, math, random, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "kit"))
import mk, exodus as E
import speech
from discourse import seg, _sizes, _heights
from fx import chapter_title, page, new, vref
from deu.common import shade
from genesis.ch02 import W1, rows
from genesis.art2 import fit, ground, SKIN
from genesis.art3 import grid_bg, node, route, label
from genesis.art4 import clay_lamp
from oba.minor import F as face_of, GOLDEN, COLD, RED, DUSK, DAWN, NIGHT, nxt, fin, _flat, halo, rays, starfield
from mrk.common import MarkKit
from num.art import ALL
from jer.art import glow
from mat.art import room, woman_fig, UP_BLESS, UP_HIGH, UP_TOUCH, UP_CALL
from job.art import seated
from exo.art8 import tag, dim, title_bar
from act import geo
from act.art import man_fig, paul, f, INK

# ---- the letter box line kind, and the kit -------------------------------------------------------------------------------
_COL = '<div style="position: absolute; left: 12px; top: 34px; bottom: 12px;'      # a column of words over a drawing (speech.orate, top=True)
_NOTCH = re.compile(r'<div style="position: absolute; (?:left|right): -8px; top: 16px; width: 13px; height: 13px;[^"]*"></div>')
_TAIL = re.compile(r'<div style="position: absolute; (?:left|right): -9px; top: 14px; width: 14px; height: 14px; background: #7A4A2A;[^"]*"></div>')

def untail(html):
    """Boxes over a drawing lose their notch or tail (no one is speaking from the panel's edge there); beside a face they
    keep it."""
    out, i = [], 0
    while True:
        a = html.find(_COL, i)
        if a < 0: out.append(html[i:]); break
        b = html.find('</div>\n', a)
        out.append(html[i:a]); out.append(_TAIL.sub("", _NOTCH.sub("", html[a:b]))); i = b
    return "".join(out)

def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]

STAMP_BAND = 66
GOLD_BG = GOLDEN
LAMP_BG = "radial-gradient(circle at 72% 34%, #FFE6A0 0 18px, #E0902E 150px, #5A2A14 330px, #1E100A 470px)"
GRIEF_BG = "radial-gradient(circle at 70% 30%, #D8E4FF 0 18px, #4A5A9A 190px, #101838 430px)"
JOY_BG = "radial-gradient(circle at 70% 36%, #FFFFFF 0 80px, #FFF8DC 230px, #F3E2B0 470px)"
STERN_BG = RED
GLORY_BG = "linear-gradient(180deg, #1A1440 0%, #3A2A6A 46%, #C8803A 100%)"
PARCHMENT, SEPIA, SEAL = "#F6EEDA", "#7A4A2A", "#B5121B"

class EpistleKit(MarkKit):
    """oba.minor.Kit (by way of Mark's MarkKit) with the letter's line kinds and panels; see the module docstring."""
    def __init__(self, G, code, book, credit=""):
        super().__init__(G, code, book); self.credit = credit

    # lines
    def lt(self, ref, frm=None, to=None, after=None): return ("letter", self.G.v(ref, frm=frm, to=to, after=after))
    def lts(self, refs): return [self.lt(r) for r in _refs(refs)]
    def ltj(self, refs): return ("letter", self.G.span(refs))
    def lp(self, refs, most=280):
        """The verses as paragraphs: consecutive verses joined into letter boxes of up to about `most` letters each (a verse
        is never split; a longer verse has a box of its own)."""
        rs = _refs(refs); out, cur, n = [], [], 0
        for r in rs:
            c, x = map(int, r.split(":")); t = len(self.G.verses[(c, x)])
            if cur and n + t > most: out.append(cur); cur, n = [], 0
            cur.append(r); n += t
        if cur: out.append(cur)
        return [self.lt(g[0]) if len(g) == 1 else self.ltj(f"{g[0]}-{g[-1].split(':')[1]}") for g in out]
    def lj(self, *parts): return self.j("letter", *parts)
    def wq(self, ref, to, frm, kind="song"):
        return [self.lt(ref, to=to), {"song": self.sg, "god": self.gd, "say": self.sy, "letter": self.lt}[kind](ref, frm=frm)]
    def qw(self, ref, to, frm, kind="song"):
        return [{"song": self.sg, "god": self.gd, "say": self.sy}[kind](ref, to=to), self.lt(ref, frm=frm)]

    # panels
    def F(self, lines, tok, bg=GOLD_BG, **k):
        """The words beside a face."""
        k.setdefault("hi", 18)
        return self.face(lines, tok, bg=bg, **k)

    def D(self, lines, fn, bg, art_h=130, size=15, sky=None, ref=None, **kw):
        """The words over a drawing fn(w, h): the words at `size` px at most (they shrink only if they must), the drawing
        below them at least art_h tall — the panel as tall as both need (pass h= to fix it); sky=n (or (n, "left")) puts
        chapter n's stamp in a band between the words and the drawing."""
        lab = self.label(); ls = _flat(lines)
        if "h" not in kw:
            hw = speech._height(ls, 678, size) + 44
            kw["h"] = int(max(hw + art_h, hw / 0.62)) + (STAMP_BAND if sky else 0)
        if sky:
            n, side = sky if isinstance(sky, tuple) else (sky, "right")
            fn = with_stamp(fn, n, side)
        return seg(ls, ref or lab, bg=bg, art=under(fn, ls, size) if ls else fn, hi=size, **kw)

    def glory(self, lines, bg=GLORY_BG, h=None, seed=1, **kw):
        """A doxology or benediction: the words over a burst of light rising from the foot of the panel, a gold inner frame."""
        lab = self.label(); lines = _flat(lines)
        def art(w, hh): return radiance(w, hh, seed) + f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(hh - 16)}" fill="none" stroke="#FFD23F" stroke-width="2"></rect>'
        if h is None:
            h = int(speech._height(lines, 678, 17) / 0.6 + 120)
        return seg(lines, kw.pop("ref", None) or lab, bg=bg, art=art, h=h, **kw)

    def title(self, num, name, rng, svg, bg, quote):
        """A chapter opener (第一話, 第二話, …) with the letter's credit."""
        return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, shade(svg), bg, quote, self.credit)

    def pack(self, segs, prefix, start, end="", default_head=None, min_size=12.5, most=4, budget=1150, min_art=200, lone=0.5, keep=0.8, face_min=230):
        """Mark's packer (fewest, fullest pages; every panel's words at min_size or more; a drawing at least min_art tall and
        keeping `keep` of the height it asked for) with one more rule: a face panel at least face_min tall, so a face is
        never squeezed to a strip. Boxes over drawings lose their tails."""
        from discourse import _chars, pack as _pack
        def fits(g):
            if len(g) == 1: return True
            if min(_sizes(g)) < min_size: return False
            hs = _heights(g)
            return (all(hh >= (min_art if s["tok"] is None and s["art"] is not None else face_min if s["tok"] else 170) for s, hh in zip(g, hs))
                    and all(hh >= keep * s["h"] for s, hh in zip(g, hs) if s["h"]))
        n, INF = len(segs), float("inf")
        best, cut = [0.0] + [INF] * n, [0] * (n + 1)
        for j in range(1, n + 1):
            for i in range(max(0, j - most), j):
                g = segs[i:j]; chars = sum(_chars(x) for x in g)
                if best[i] == INF or (len(g) > 1 and (chars > budget or not fits(g))): continue
                under_ = max(0.0, (budget * 0.8 - chars) / budget)
                cost = best[i] + 1 + 3 * under_ * under_ + sum(0.25 for x in g[1:] if x["head"]) + (lone if len(g) == 1 else 0)
                if cost < best[j]: best[j], cut[j] = cost, i
        groups, j = [], n
        while j > 0: groups.insert(0, segs[cut[j]:j]); j = cut[j]
        out, head = [], default_head or ""
        for i, g in enumerate(groups):
            pages = _pack(g, prefix, start + len(out), book=self.book, code=self.code, budget=10 ** 9, most=99, default_head=head,
                          end=end if i == len(groups) - 1 else "")
            for name, t, fn in pages:
                out.append((f"{prefix}-P{len(out) + 1:02d}-" + name.split("-P01-", 1)[1], t, (lambda fn=fn: untail(fn()))))
            head = next((s["head"] for s in reversed(g) if s["head"]), head)
        return out

def under(fn, lines, hi=16):
    """A drawing fn(w, h) set just under the column of words at the top of its panel (oba.minor.under, with the words' size
    capped at hi as the panel sets them)."""
    def art(w, h):
        bw = w - 24
        s = speech.fit(lines, bw, h * 0.62, hi=hi)
        kk = min(0.62, (speech._height(lines, bw, s) + 34 + 10) / h)
        return f'<g transform="translate(0 {h * kk:.1f})">' + fn(w, h * (1 - kk)) + '</g>'
    return art

def svg_stamp(n, x, y):
    """Chapter n's stamp drawn inside a drawing, its top-left corner at (x, y) (mk.stamp's red-ruled label, as Acts')."""
    kj = f"第{mk.kanji_num(n)}章"
    wd = max(92, 22 * len(kj) + 14)
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate(4 {wd / 2:.1f} 20)">'
            f'<rect x="0" y="0" width="{wd}" height="42" fill="#F3EFE6" stroke="#D7261E" stroke-width="2.5"></rect>'
            f'<text x="{wd / 2:.1f}" y="23" fill="#D7261E" font-family="Noto Sans JP, sans-serif" font-weight="900" font-size="18" text-anchor="middle">{kj}</text>'
            f'<text x="{wd / 2:.1f}" y="35" fill="#D7261E" font-family="IBM Plex Mono, monospace" font-weight="600" font-size="8" letter-spacing="1.3" text-anchor="middle">CHAPTER {n}</text></g>')

def with_stamp(fn, n, side="right"):
    """A drawing set STAMP_BAND px lower, chapter n's stamp in the band left above it (clear of every figure)."""
    def art(w, h):
        x = 16 if side == "left" else w - 124
        return f'<g transform="translate(0 {STAMP_BAND})">' + fn(w, h - STAMP_BAND) + '</g>' + svg_stamp(n, x, 10)
    return art

# ---- Paul's faces ------------------------------------------------------------------------------------------------------
_P = dict(skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True)
def _paul(**k): return face_of("adam", **{**_P, **k})
from ntcast import PAUL                                                                    # earnest, gold light (ntcast)
PAUL_LAMP = _paul(skin="#D49468", shadow="#4A2618", light="#FF9A3D")
PAUL_GRIEF = _paul(skin="#B98A6E", shadow="#3A2A3A", brow="sorrow", tear=True, light="#9AA8C8")   # as Acts draws him grieving
PAUL_JOY = _paul(skin="#E3B896", shadow="#A87A5A", light="#FFFFFF")
PAUL_STERN = _paul(shadow="#4A2A2A", brow="scowl", light="#D7261E")                      # as Acts draws him stern

# ---- small things ------------------------------------------------------------------------------------------------------
def lamp_glow(x, y, r, uid, color="#FFC14D", op=0.55):
    return glow(x, y, r, color, op, uid)

def reed_pen(x, y, s=1.0, rot=-30):
    """A reed pen, its cut nib at (x, y)."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})"><path d="M0 0 L 4 -6 L 4 -70 L -4 -70 L -4 -6 Z" fill="#C8A060" stroke="{INK}" stroke-width="1.4"></path>'
            '<path d="M-4 -40 L 4 -40 M-4 -58 L 4 -58" stroke="#8A6A3A" stroke-width="1.4"></path></g>')

def inkpot(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-10 0 L 10 0 L 12 -14 C 12 -20 8 -22 6 -22 L -6 -22 C -8 -22 -12 -20 -12 -14 Z" fill="#3A2A2A" stroke="{INK}" stroke-width="1.6"></path>'
            '<ellipse cx="0" cy="-22" rx="6" ry="2" fill="#0D0D0F"></ellipse></g>')

def open_letter(x, y, w, h, rows=7, seed=1, color="#EADBB4"):
    """A sheet of papyrus (its top-left corner at x, y) with rows of writing, no words."""
    r = random.Random(seed)
    o = [f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{color}" stroke="{INK}" stroke-width="1.8"></rect>',
         f'<path d="M{f(x + w * 0.33)} {f(y)} L {f(x + w * 0.33)} {f(y + h)} M{f(x + w * 0.66)} {f(y)} L {f(x + w * 0.66)} {f(y + h)}" stroke="#C8B488" stroke-width="1"></path>']
    for k in range(rows):
        yy = y + h * (k + 0.8) / (rows + 0.6); xx = x + w * 0.08
        while xx < x + w * 0.9:
            L = w * r.uniform(0.05, 0.16)
            o.append(f'<path d="M{f(xx)} {f(yy)} l {f(min(L, x + w * 0.92 - xx))} 0" stroke="#4A3020" stroke-width="{f(max(1.0, h / 70))}"></path>'); xx += L + w * 0.03
    return "".join(o)

def sealed_scroll(x, y, s=1.0, rot=0, seal=SEAL, cord="#8A5A30"):
    """A letter rolled and tied with a cord, a red clay seal on the knot; (x, y) its middle."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})">'
            f'<rect x="-60" y="-14" width="120" height="28" rx="4" fill="#EADBB4" stroke="{INK}" stroke-width="2.4"></rect>'
            '<ellipse cx="60" cy="0" rx="6" ry="14" fill="#D8C49A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            '<path d="M-52 -8 L 52 -8 M-52 6 L 52 6" stroke="#C8B488" stroke-width="1.2"></path>'
            f'<path d="M-6 -15 L -6 15 M6 -15 L 6 15" stroke="{cord}" stroke-width="3"></path>'
            f'<path d="M0 10 C -8 26 -14 30 -20 36 M0 10 C 6 26 12 32 18 38" stroke="{cord}" stroke-width="2.6" fill="none"></path>'
            f'<circle cx="0" cy="8" r="11" fill="{seal}" stroke="{INK}" stroke-width="2"></circle>'
            '<circle cx="0" cy="8" r="6" fill="none" stroke="#7A0A10" stroke-width="1.6"></circle></g>')

def radiance(w, h, seed=1, cx=0.5, cy=0.86, color="#FFF4C2"):
    """The burst of light behind a doxology: rays from a low sun of white-gold light, stars above (no figure)."""
    x, y = w * cx, h * cy
    return (starfield(w, h, seed, int(w * h / 9000) + 20, 0.55) + halo(x, y, max(w, h) * 0.7, "#FFE680", 0.55)
            + rays(x, y, 36, h * 0.08, max(w, h) * 1.3, color, 0.28, 5) + halo(x, y, max(w, h) * 0.22, "#FFFFFF", 0.9))

def plate_bg(w, h, title=None, step=24):
    """The technical-annotation ground: a navy grid and a gold title bar (svg text, a label)."""
    import exo.art8 as B
    B._W[0] = w
    return grid_bg(w, h, color="#1E3A5A", step=step, bg="#0B1A2E") + (title_bar(w, title) if title else "")

def letter_road(w, h, route_, title=None, box=(11.0, 25.5, 35.6, 43.0), places=None, hi=None, regions=("ITALY", "ACHAIA", "MACEDONIA")):
    """The letter's road on the map of Acts (act.geo): route_ a list of place names or (lon, lat) points, drawn lit red."""
    pl = places if places is not None else tuple(p for p in route_ if isinstance(p, str))
    return geo.med_map(w, h, box=box, places=pl, routes=[route_], hi=hi if hi is not None else (pl[0], pl[-1]) if pl else (), regions=regions,
                       title=title, red=True)

# ---- the opening scene --------------------------------------------------------------------------------------------------
TERTIUS_LOOK = dict(cloth="#3A5A5A", head="#1F4A4A")                 # Romans: a young scribe, dark-teal headcloth
PHOEBE_LOOK = dict(cloth="#7A7A84", veil="#1F2F6A")                  # Romans: deep-blue veil, grey travelling cloak

def _window(w, h, x, y, ww, hh, night, seed):
    """A window on the city: flat roofs, and the citadel on its rock with a temple (Corinth's Acrocorinth) against the sky."""
    sky_ = ("#0B0B2A", "#2A2050") if night else ("#8FD0E2", "#F3E8C8")
    uid = f"win{seed}"
    o = [f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}"></rect></clipPath>'
         f'<linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky_[0]}"></stop><stop offset="1" stop-color="{sky_[1]}"></stop></linearGradient></defs>',
         f'<g clip-path="url(#{uid})"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="url(#{uid}g)"></rect>']
    if night: o.append(f'<g transform="translate({f(x)} {f(y)})">' + mk.stars(int(ww * hh / 900) + 6, ww, hh * 0.5, seed) + '</g>')
    rock = "#2A2440" if night else "#9A8A6A"
    o.append(f'<path d="M{f(x - 4)} {f(y + hh * 0.66)} L {f(x + ww * 0.3)} {f(y + hh * 0.34)} L {f(x + ww * 0.52)} {f(y + hh * 0.26)} L {f(x + ww * 0.74)} {f(y + hh * 0.38)} '
             f'L {f(x + ww + 4)} {f(y + hh * 0.6)} L {f(x + ww + 4)} {f(y + hh + 4)} L {f(x - 4)} {f(y + hh + 4)} Z" fill="{rock}" stroke="{INK}" stroke-width="1.6"></path>')
    tx, ty, tw = x + ww * 0.52, y + hh * 0.26, ww * 0.2
    o.append(f'<path d="M{f(tx - tw / 2)} {f(ty)} L {f(tx)} {f(ty - tw * 0.3)} L {f(tx + tw / 2)} {f(ty)} Z" fill="{"#8A8090" if night else "#E8DCC0"}" stroke="{INK}" stroke-width="1.2"></path>'
             + "".join(f'<path d="M{f(tx - tw / 2 + tw * k / 4)} {f(ty)} L {f(tx - tw / 2 + tw * k / 4)} {f(ty + tw * 0.4)}" stroke="{"#8A8090" if night else "#E8DCC0"}" stroke-width="{f(max(1.5, tw / 14))}"></path>' for k in range(5)))
    r = random.Random(seed)
    xx = x - 6
    while xx < x + ww:
        bw = ww * r.uniform(0.14, 0.26); bh = hh * r.uniform(0.12, 0.26)
        o.append(f'<rect x="{f(xx)}" y="{f(y + hh - bh)}" width="{f(bw)}" height="{f(bh + 4)}" fill="{"#3A3050" if night else "#E8D8B0"}" stroke="{INK}" stroke-width="1.2"></rect>')
        if night and r.random() < 0.6: o.append(f'<rect x="{f(xx + bw * 0.4)}" y="{f(y + hh - bh * 0.7)}" width="{f(bw * 0.18)}" height="{f(bh * 0.24)}" fill="#FFC14D"></rect>')
        xx += bw
    o.append('</g>' + f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(x + ww / 2)} {f(y)} L {f(x + ww / 2)} {f(y + hh)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<rect x="{f(x - 8)}" y="{f(y + hh)}" width="{f(ww + 16)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def _scribe_at_table(p, x, b, s, look, writing=True, holding=False):
    """The scribe sitting on the floor facing right, a low table before him with the sheet on it, the reed pen in his hand."""
    o = [seated(x, b, s * 0.86, look["cloth"], head=look["head"], beard=None, bowed=writing)]
    tx0, tx1, ty = x + 58 * s, x + 150 * s, b - 34 * s
    o.append(f'<rect x="{f(tx0)}" y="{f(ty)}" width="{f(tx1 - tx0)}" height="{f(7 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(lx)}" y="{f(ty + 7 * s)}" width="{f(6 * s)}" height="{f(27 * s)}" fill="#5A2E16" stroke="{INK}" stroke-width="1.6"></rect>' for lx in (tx0 + 6 * s, tx1 - 12 * s)))
    if holding:
        o.append(open_letter(x + 24 * s, b - 98 * s, 40 * s, 50 * s, rows=5, seed=int(x)))
    else:
        o.append(f'<g transform="rotate(-4 {f(tx0 + 40 * s)} {f(ty)})">' + open_letter(tx0 + 4 * s, ty - 4 * s, 70 * s, 5 * s, rows=1, seed=int(x)) + '</g>')
        o.append(f'<path d="M{f(tx0 + 10 * s)} {f(ty - 3 * s)} l {f(60 * s)} {f(-4 * s)}" stroke="#EADBB4" stroke-width="{f(4 * s)}"></path>')
    o.append(inkpot(tx1 - 20 * s, ty, s * 0.8))
    if writing: o.append(reed_pen(x + 40 * s, b - 56 * s, s * 0.6, rot=30))
    return "".join(o)

def study(p, w, h, seed, stage="dictate", scribe=TERTIUS_LOOK, bearer=None, night=True, window="city", writer=paul, fig_h=250):
    """The letter written: a room of a house by lamplight, the writer standing and dictating, the scribe sitting at a low
    table writing (stage "dictate"); "read" the scribe holding up the sheet, the writer listening; "give" the writer
    handing the sealed scroll to the bearer standing at the open door (bearer: a dict cloth, veil — a woman — or cloth,
    head — a man)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E" if night else "#D8C098", floor="#3A2A20" if night else "#8A6A4A")]
    if window: o.append(_window(w, h, w * 0.66, h * 0.18, w * 0.22, h * 0.34, night, seed))
    s = fit(b, max(h * 0.3, b - fig_h))
    lx, ly = w * 0.46, b - 34 * s * 0.9
    if night: o.append(lamp_glow(lx, ly - 30 * s, max(w, h) * 0.5, f"{p}lg", op=0.5))
    if stage == "give":
        door_x = w * 0.62
        o.append(f'<rect x="{f(door_x)}" y="{f(h * 0.26)}" width="{f(w * 0.2)}" height="{f(b - h * 0.26)}" fill="{"#2A3A6A" if night else "#FFE6A0"}" stroke="{INK}" stroke-width="2.4"></rect>')
        if night: o.append(f'<g transform="translate({f(door_x)} {f(h * 0.26)})">' + mk.stars(8, w * 0.2, (b - h * 0.26) * 0.5, seed + 3) + '</g>')
        o.append(writer(p, w * 0.42, b, s, up=[(22, -158), (46, -150), (70, -156)]))
        o.append(sealed_scroll(w * 0.42 + 80 * s, b - 160 * s, s * 0.34, rot=-10))
        if bearer:
            if "veil" in bearer: o.append(woman_fig(p, w * 0.7, b, s * 0.94, bearer["cloth"], bearer["veil"], flip=True, up=[(-22, -158), (-40, -144), (-60, -150)]))
            else: o.append(man_fig(p, w * 0.7, b, s, bearer["cloth"], head=bearer.get("head"), bd=bearer.get("beard"), flip=True, up=[(-22, -158), (-40, -144), (-60, -150)]))
        if scribe: o.append(_scribe_at_table(p, w * 0.08, b, s, scribe, writing=False))
        o.append(clay_lamp(w * 0.08 + 120 * s, b - 34 * s - 6 * s, s * 0.7))
        return "".join(o)
    # dictate / read: the writer at the left facing right, the scribe facing him across the table
    o.append(writer(p, w * 0.2, b, s, up=[(22, -158), (46, -150), (70, -158)] if stage == "dictate" else None))
    if scribe:
        sx = w * 0.56
        o.append(f'<g transform="translate({f(2 * sx)} 0) scale(-1 1)">' + _scribe_at_table(p, sx, b, s, scribe, writing=stage == "dictate", holding=stage == "read") + '</g>')
        o.append(clay_lamp(sx - 104 * s, b - 34 * s - 6 * s, s * 0.7))
    if bearer:
        if "veil" in bearer: o.append(woman_fig(p, w * 0.9, b, s * 0.94, bearer["cloth"], bearer["veil"], flip=True))
        else: o.append(man_fig(p, w * 0.9, b, s, bearer["cloth"], head=bearer.get("head"), bd=bearer.get("beard"), flip=True))
    return "".join(o)

def still_life(w, h, seed, sealed=True, night=True):
    """The letter on the table: the rolled scroll tied and sealed (or the sheet lying open), the reed pen, the inkpot, the lamp."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#3A2418" if night else "#C8A878"}"></rect>']
    ty = h * 0.62
    if night: o.append(lamp_glow(w * 0.78, ty - h * 0.12, max(w, h) * 0.6, f"sl{seed}", op=0.55))
    o.append(f'<path d="M-10 {f(ty)} L {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M-10 {f(ty + 8)} L {f(w + 10)} {f(ty + 8)}" stroke="#8A5A30" stroke-width="2"></path>')
    k = min(w / 520, h / 260)
    if sealed: o.append(sealed_scroll(w * 0.44, ty + h * 0.12, k * 1.6, rot=-6))
    else: o.append(f'<g transform="rotate(-3 {f(w * 0.4)} {f(ty)})">' + open_letter(w * 0.18, ty + h * 0.04, w * 0.42, h * 0.26, rows=6, seed=seed) + '</g>')
    o.append(inkpot(w * 0.7, ty + h * 0.14, k * 1.4) + reed_pen(w * 0.72, ty + h * 0.2, k * 1.2, rot=64) + clay_lamp(w * 0.82, ty + h * 0.06, k * 1.3))
    return "".join(o)

# ---- greetings ------------------------------------------------------------------------------------------------------------
_PW = 150                                                            # the portrait square's width in a greeting cell

def portrait(fig, bg=("#8FD0E2", "#F3E8C8"), floor="#C8B07A"):
    """A portrait for a greeting cell: fig(p, x, y, s) standing on a floor before a two-tone ground."""
    def draw(p, w, h):
        b = h * 0.94
        s = fit(b, b - min(h * 0.74, 170))
        return (mk.defs(p, *ALL, "ManUp", "WomanUp") + f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{bg[0]}"></rect>'
                + f'<rect x="0" y="{f(h * 0.55)}" width="{f(w)}" height="{f(h * 0.45)}" fill="{bg[1]}"></rect>'
                + f'<rect x="0" y="{f(b - 6)}" width="{f(w)}" height="{f(h - b + 6)}" fill="{floor}"></rect>' + fig(p, w * 0.5, b, s))
    return draw

def _cell_need(lines, s):
    return speech._height(lines, W1 - _PW - 30, s) + 46

def _cell(name, tg, lines, art, h, s, p, accent="#7A4A2A"):
    bw = W1 - _PW - 30
    svg = (f'<rect x="0" y="0" width="{W1}" height="{f(h)}" fill="#E8DCC0"></rect>'
           f'<svg x="0" y="0" width="{_PW}" height="{f(h)}" viewBox="0 0 {_PW} {f(h)}" preserveAspectRatio="xMidYMid slice">{art(p, _PW, h)}</svg>'
           f'<path d="M{_PW} 0 L {_PW} {f(h)}" stroke="{INK}" stroke-width="3"></path>')
    fs = min(s, speech.fit(lines, bw, h - 40))
    items = [re.sub(r"font-size: [\d.]+px", f"font-size: {fs}px", it, count=1) for it in speech.column(lines, bw, 10 ** 6, side=None)]
    head = (f'<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 10px">'
            f'<span data-label style="font-family: Anton, sans-serif; font-size: 22px; line-height: 1; letter-spacing: 0.04em; text-transform: uppercase; color: {accent}">{name}</span>'
            f'<span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.16em; white-space: nowrap; color: #4A3A2A">{tg}</span></div>')
    over = (f'\n    <div style="position: absolute; left: {_PW + 14}px; right: 12px; top: 9px; bottom: 9px; display: flex; flex-direction: column; justify-content: center; gap: 7px">'
            + head + "".join(items) + '</div>\n')
    return new("#E8DCC0", W1, h, svg, over)

def greetings(items, prefix, start, book, code, head="Salute", end="", size=15, most=6, accent="#7A4A2A"):
    """Pages of greeting cells (see the module docstring). A page takes cells while they fit at `size` px (at most `most`);
    each page then sets its type as large as its cells allow (up to 19 px)."""
    room = 1022
    groups, cur = [], []
    for it in items:
        need = lambda g, s: sum(max(118, _cell_need(x[2], s)) for x in g) + 12 * (len(g) - 1)
        if cur and (len(cur) == most or need(cur + [it], size) > room): groups.append(cur); cur = []
        cur.append(it)
    if cur: groups.append(cur)
    out = []
    for k, g in enumerate(groups):
        s = 19.0
        while s > 11 and sum(max(118, _cell_need(x[2], s)) for x in g) + 12 * (len(g) - 1) > room - (64 if end and k == len(groups) - 1 else 0): s -= 0.5
        needs = [max(118, _cell_need(x[2], s)) for x in g]
        spare = room - 12 * (len(g) - 1) - sum(needs)
        hs = [round(n + spare * n / sum(needs)) for n in needs]
        hs[-1] = None
        t, hh = rows(*hs)
        body = "".join(_cell(nm, tg, ls, art, hx, s, f"{prefix.lower().replace('-', '')}{k}{i}", accent) for i, ((nm, tg, ls, art), hx) in enumerate(zip(g, hh)))
        if end and k == len(groups) - 1:
            body = body[:body.rfind("  </div>")] + end + body[body.rfind("  </div>"):]
        refs = [x[1].split(" · ")[0] for x in g]
        a, z = refs[0].split("–")[0], refs[-1].split("–")[-1]
        rng = a if a == z else (f"{a}–{z.split(':')[-1]}" if ":" not in z or z.split(":")[0] == a.split(":")[0] else f"{a}–{z}")
        title = f"{book} {rng} — {head}"
        slug = re.sub(r"[^A-Za-z]", "", head.title())[:18]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head}", (lambda title=title, t=t, body=body, n=start + k: page(title, t, body, n))))
    return out
