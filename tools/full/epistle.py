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
Faces alternate sides: K.pack sets every other face panel flip=True (the face at the right, the words at the left)
unless the panel gives flip= itself.
People (never blobs: drawn on the kit's MAN / WOMAN silhouettes, so shoulders, arms and waist show):
    robed(p, x, y, s, cloth, woman=, head=, cord=, veil=, hair=, beard=, mantle=, belt=, up=, flip=, extra=)  a person standing
        in a sleeved robe and long skirt that follow the body, hands and head showing (needs mk.defs(p, *ALL, "ManUp",
        "WomanUp")); up= arm points from (-22, -158) reach left, or right with flip=True; extra= svg in the figure's own
        units (a scroll in the hand at the arm's last point)
    paul_fig(p, x, y, s, flip=, up=, extra=)   Paul in ntcast's colours on robed(), a darker mantle
    scribe_seated(x, y, s, cloth=, head=, cord=, flip=, stage="write"|"read")  a scribe cross-legged on the floor, the roll
        across his knee and the reed pen on it ("write"), or the roll lifted to read it back
    face_portrait(tok, tok2=None)   a greeting cell's portrait: a shaded profile face (faces.face token), a second behind it
Furniture: pigeonholes(x, y, w, h) (scroll cubbies) · couch(x, y, w, s) · mat(x, y, w, s) · low_table(x, y, w, s) ·
    doorway(x, top, w, b, seed, night) (an open door onto the street, house fronts and lit windows beyond)
Drawings (svg strings; p is a prefix unique to the panel; w, h the panel's size):
    study(p, w, h, seed, stage=, scribe=, bearer=, night=, window=, writer=paul_fig, fig_h=)   the opening scene (also a
        good "Paul speaking" panel anywhere in a letter, between the face panels), close in — the figures stand about 72%
        of the drawing's height: the writer standing, the scribe cross-legged on a mat writing on the roll, a low table
        with the lamp and inkpot, a couch, pigeonholes of scrolls, the window on the city (the Acrocorinth). stage
        "dictate" (the writer's hand out), "read" (the scribe reads the roll back, the writer listening), "give" (the
        writer turns to the bearer standing in the open doorway onto the night street, the sealed scroll in her hand).
        scribe: dict(cloth, head, cord) (TERTIUS_LOOK) or False; bearer: dict(cloth, veil, mantle) for a woman
        (PHOEBE_LOOK) or dict(cloth, head, beard) for a man; fig_h a figure's height in px (default 72% of h)
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
        are labels (data-label); lines are the verse(s) as letter boxes; portrait(p, w, h) draws the person in the cell's
        left square — use face_portrait(TOKEN) (or face_portrait(A, B) for two). Returns [(file, board title, fn)] like
        K.pack, so PG.extend(greetings(...)) puts them in the chapter.
    portrait(fig, bg=, floor=)      a standing figure in the cell instead (fig(p, x, y, s), e.g. a robed() figure)"""
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
from mat.art import room, woman_fig, veil as _veil, UP_BLESS, UP_HIGH, UP_TOUCH, UP_CALL
from exo.art import headcloth, WHITE_BEARD
from ntcast import ROBES
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
        nf = 0
        for s_ in segs:                                # Paul's face alternates sides: left (words right), then right (words left)
            if s_["tok"]:
                if s_["flip"] is None: s_["flip"] = nf % 2 == 1
                nf += 1
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
TERTIUS_LOOK = dict(cloth="#3A5A5A", head="#1F4A4A", cord="#0D2A2A")                # Romans: a young scribe, dark-teal headcloth
PHOEBE_LOOK = dict(cloth="#7A7A84", veil="#1F2F6A", mantle="#5E5E6A")                 # Romans: deep-blue veil, grey travelling cloak

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

def robed(p, x, y, s, cloth, skin=SKIN, woman=False, head=None, cord="#2A1A10", veil=None, hair=None, beard=None, up=None, flip=False,
          mantle=None, belt=None, line=INK, extra=""):
    """A person standing, drawn on the kit's MAN / WOMAN silhouette (shoulders, arms, waist) so the garment follows the
    body: the sleeved robe is the silhouette itself below the neck, a long skirt falls from the waist, the hands and head
    show; head= a headcloth colour (cord= its cord, None for none), veil= a woman's veil, hair= bare hair, beard= a beard
    colour; mantle= a cloak over one shoulder; belt= a girdle; up= a free arm as mk.person, its points from the shoulder
    (-22, -158): it reaches to the left as drawn, to the right with flip=True (the other hand hangs). Needs mk.defs(p, *num.art.ALL,
    "ManUp", "WomanUp") in the panel. (x, y) is the ground under the feet; the figure is about 205 units tall at s = 1."""
    sx = -s if flip else s
    fig = ("Woman" if woman else "Man") + ("Up" if up else "")
    cid = f"{p}nk{abs(int(x))}x{abs(int(y))}"
    hx, hw = (24.5, 3.6) if woman else (28.5, 4.2)
    wx = 15 if woman else 19
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">',
         f'<defs><clipPath id="{cid}t"><rect x="-80" y="-167" width="160" height="61"></rect></clipPath>'      # the bodice and the upper arms
         f'<clipPath id="{cid}a"><rect x="-60" y="-110" width="{60 - wx - 1}" height="40"></rect><rect x="{wx + 1}" y="-110" width="{60 - wx - 1}" height="40"></rect></clipPath></defs>',
         f'<use href="#{p}{fig}" fill="{skin}" stroke="{line}" stroke-width="3"></use>',
         f'<use href="#{p}{fig}" fill="{cloth}" stroke="{line}" stroke-width="2.6" clip-path="url(#{cid}t)"></use>',
         f'<path d="M-{wx} -110 C -{wx + 6} -76 -{wx + 12} -36 -{wx + 15} 0 L {wx + 15} 0 C {wx + 12} -36 {wx + 6} -76 {wx} -110 Z" fill="{cloth}" stroke="{line}" stroke-width="2.6"></path>',
         f'<path d="M-6 -96 C -8 -60 -10 -30 -12 -2 M7 -90 C 8 -60 10 -30 13 -2" fill="none" stroke="{line}" stroke-width="1.2" opacity="0.45"></path>',
         f'<use href="#{p}{fig}" fill="{cloth}" stroke="{line}" stroke-width="2.6" clip-path="url(#{cid}a)"></use>',     # the sleeves over the skirt
         f'<path d="M-7 -166 L 0 -156 L 7 -166" fill="none" stroke="{line}" stroke-width="1.4"></path>']
    for side in ((1,) if up else (-1, 1)):
        o.append(f'<ellipse cx="{f(side * hx)}" cy="-90" rx="{hw}" ry="6.5" fill="{skin}" stroke="{line}" stroke-width="1.4"></ellipse>')
    if belt: o.append(f'<path d="M-{wx + 1} -108 C -6 -104 6 -104 {wx + 1} -108" fill="none" stroke="{belt}" stroke-width="3.4"></path>')
    if mantle:
        o.append(f'<path d="M-25 -162 C -12 -150 6 -118 16 -58 C 18 -40 20 -20 22 -4 L 34 -4 C 30 -40 26 -100 20 -150 C 8 -166 -14 -168 -25 -162 Z" '
                 f'fill="{mantle}" stroke="{line}" stroke-width="2.2"></path>')
    if up:
        d = "M" + " L ".join(f"{a} {b}" for a, b in up)
        o.append(f'<path d="{d}" fill="none" stroke="{line}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"></path>'
                 f'<path d="{d}" fill="none" stroke="{cloth}" stroke-width="9.5" stroke-linecap="round" stroke-linejoin="round"></path>'
                 f'<circle cx="{up[-1][0]}" cy="{up[-1][1]}" r="5" fill="{skin}" stroke="{line}" stroke-width="1.4"></circle>')
    if hair: o.append(f'<path d="M-13.5 -186 C -16 -206 16 -206 13.5 -186 L 14 -178 C 12.5 -175 11 -177 11 -181 C 8 -192 -8 -192 -11 -181 C -11 -177 -12.5 -175 -14 -178 Z" '
                      f'fill="{hair}" stroke="{line}" stroke-width="1.3"></path>')
    if beard: o.append(WHITE_BEARD.replace("#E8E2D6", beard))
    if veil: o.append(_veil(veil))
    if head: o.append(headcloth(head, cord=cord))
    return "".join(o) + extra + "</g>"

def paul_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Paul at a distance in the letters: ntcast's colours (a dark-brown robe and headcloth with a cord, a black beard), on
    the kit silhouette, a darker mantle over the shoulder."""
    return robed(p, x, y, s, ROBES["paul"], head="#5A4A3A", cord="#2A1A10", beard="#3A2A1A", mantle="#3E3228", belt="#2A1A10", flip=flip, up=up, extra=extra)

def scribe_seated(x, y, s, cloth="#3A5A5A", head="#1F4A4A", cord="#0D2A2A", skin=SKIN, flip=False, stage="write"):
    """A scribe sitting cross-legged on the floor, facing right, the roll open across his knee: stage "write" the reed pen
    in his hand on the roll; "read" the roll lifted before his face. (x, y) is the floor under him; about 128 units tall."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">',
         # crossed legs under the robe, the lap
         f'<path d="M-44 0 C -46 -18 -34 -34 -10 -36 L 34 -34 C 52 -32 60 -18 56 0 Z" fill="{cloth}" stroke="{INK}" stroke-width="2.6"></path>',
         f'<path d="M-30 -14 C -10 -24 20 -24 46 -12" fill="none" stroke="{INK}" stroke-width="1.3" opacity="0.5"></path>',
         f'<path d="M48 -4 C 58 -6 64 -2 62 2 L 46 2 Z" fill="{skin}" stroke="{INK}" stroke-width="1.4"></path>',
         # the back and chest, leaning a little toward the roll
         f'<path d="M-24 -34 C -30 -60 -28 -88 -14 -104 C -6 -110 6 -110 12 -102 C 20 -88 22 -60 18 -36 Z" fill="{cloth}" stroke="{INK}" stroke-width="2.6"></path>',
         f'<path d="M-4 -104 L 2 -96 L 8 -104" fill="none" stroke="{INK}" stroke-width="1.3"></path>',
         f'<path d="M-24 -40 C -6 -44 8 -44 18 -40" fill="none" stroke="#0D2A2A" stroke-width="3"></path>']
    hx, hy = (6, -118) if stage == "write" else (2, -122)
    o.append(f'<rect x="{hx - 5}" y="{hy + 8}" width="10" height="10" fill="{skin}"></rect>'
             f'<circle cx="{hx}" cy="{hy}" r="13" fill="{skin}" stroke="{INK}" stroke-width="2.2"></circle>'
             f'<path d="M{hx + 10} {hy - 2} l 5 4 l -5 2" fill="{skin}" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(f'<path d="M{hx - 15} {hy + 2} C {hx - 16} {hy - 22} {hx + 14} {hy - 24} {hx + 14} {hy - 4} L {hx + 8} {hy - 6} L {hx - 2} {hy - 10} L {hx - 8} {hy + 4} '
             f'L {hx - 14} {hy + 22} L {hx - 22} {hy + 20} Z" fill="{head}" stroke="{INK}" stroke-width="1.8"></path>'
             f'<path d="M{hx - 12} {hy - 10} C {hx - 4} {hy - 16} {hx + 6} {hy - 16} {hx + 13} {hy - 10}" fill="none" stroke="{cord}" stroke-width="2.6"></path>')
    if stage == "write":
        o.append(f'<path d="M14 -46 L 70 -50" stroke="#C8B488" stroke-width="2"></path>'
                 f'<rect x="14" y="-54" width="56" height="9" fill="#EADBB4" stroke="{INK}" stroke-width="1.6" transform="rotate(-4 42 -50)"></rect>'
                 f'<ellipse cx="14" cy="-48" rx="4" ry="7" fill="#D8C49A" stroke="{INK}" stroke-width="1.4"></ellipse>'
                 f'<ellipse cx="70" cy="-52" rx="4" ry="7" fill="#D8C49A" stroke="{INK}" stroke-width="1.4"></ellipse>'
                 + "".join(f'<path d="M{20 + k * 10} -52 l 6 0" stroke="#4A3020" stroke-width="1.4" transform="rotate(-4 42 -50)"></path>' for k in range(4)))
        arms = [((2, -96), (14, -72), (40, -60)), ((-12, -94), (-2, -68), (20, -56))]
        for pts in arms:
            d = "M" + " L ".join(f"{a} {b}" for a, b in pts)
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"></path>'
                     f'<path d="{d}" fill="none" stroke="{cloth}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"></path>'
                     f'<circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="4.6" fill="{skin}" stroke="{INK}" stroke-width="1.3"></circle>')
        o.append(f'<path d="M40 -61 L 54 -84" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"></path><path d="M40 -61 L 54 -84" stroke="#C8A060" stroke-width="2" stroke-linecap="round"></path>')
    else:
        o.append(f'<rect x="20" y="-126" width="12" height="46" fill="#EADBB4" stroke="{INK}" stroke-width="1.6"></rect>'
                 + "".join(f'<path d="M23 {-120 + k * 8} l 6 0" stroke="#4A3020" stroke-width="1.3"></path>' for k in range(5))
                 + f'<ellipse cx="26" cy="-128" rx="8" ry="3.4" fill="#D8C49A" stroke="{INK}" stroke-width="1.4"></ellipse>'
                 f'<ellipse cx="26" cy="-78" rx="8" ry="3.4" fill="#D8C49A" stroke="{INK}" stroke-width="1.4"></ellipse>')
        for pts in (((2, -96), (14, -84), (22, -110)), ((-10, -94), (6, -78), (22, -86))):
            d = "M" + " L ".join(f"{a} {b}" for a, b in pts)
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"></path>'
                     f'<path d="{d}" fill="none" stroke="{cloth}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"></path>'
                     f'<circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="4.6" fill="{skin}" stroke="{INK}" stroke-width="1.3"></circle>')
    return "".join(o) + "</g>"

def pigeonholes(x, y, w, h, seed=1):
    """A wall case of pigeonholes with rolled scrolls in them (their ends, tags hanging)."""
    r = random.Random(seed)
    cols, rows_ = max(3, int(w / 34)), max(2, int(h / 30))
    cw, ch = w / cols, h / rows_
    o = [f'<rect x="{f(x - 6)}" y="{f(y - 6)}" width="{f(w + 12)}" height="{f(h + 12)}" fill="#5A3418" stroke="{INK}" stroke-width="2.4"></rect>']
    for i in range(cols):
        for j in range(rows_):
            cx, cy = x + i * cw, y + j * ch
            o.append(f'<rect x="{f(cx + 2)}" y="{f(cy + 2)}" width="{f(cw - 4)}" height="{f(ch - 4)}" fill="#1E120A" stroke="{INK}" stroke-width="1.2"></rect>')
            for k in range(r.randint(1, 3)):
                rx = cx + cw * (0.3 + 0.22 * k); ry = cy + ch * 0.62
                o.append(f'<circle cx="{f(rx)}" cy="{f(ry)}" r="{f(min(cw, ch) * 0.17)}" fill="#E0CFA4" stroke="{INK}" stroke-width="1"></circle>')
                if r.random() < 0.4: o.append(f'<path d="M{f(rx)} {f(ry)} l 0 {f(ch * 0.3)}" stroke="#B5121B" stroke-width="1.4"></path>')
    return "".join(o)

def couch(x, y, w, s=1.0, color="#7A3A2A"):
    """A low couch (a reclining bench) with a cushion, its feet turned; (x, y) its left foot on the floor."""
    return (f'<rect x="{f(x)}" y="{f(y - 30 * s)}" width="{f(w)}" height="{f(10 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
            f'<rect x="{f(x + 4)}" y="{f(y - 42 * s)}" width="{f(w - 8)}" height="{f(13 * s)}" rx="{f(5 * s)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>'
            f'<path d="M{f(x)} {f(y - 30 * s)} C {f(x - 8 * s)} {f(y - 50 * s)} {f(x + 4 * s)} {f(y - 62 * s)} {f(x + 12 * s)} {f(y - 54 * s)} L {f(x + 12 * s)} {f(y - 30 * s)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></path>'
            + "".join(f'<rect x="{f(fx)}" y="{f(y - 20 * s)}" width="{f(7 * s)}" height="{f(20 * s)}" fill="#4A2412" stroke="{INK}" stroke-width="1.6"></rect>' for fx in (x + 6 * s, x + w - 13 * s)))

def mat(x, y, w, s=1.0, color="#8A6A3A"):
    """A woven floor mat, (x, y) its left end on the floor."""
    return (f'<path d="M{f(x)} {f(y)} L {f(x + 14 * s)} {f(y - 10 * s)} L {f(x + w + 14 * s)} {f(y - 10 * s)} L {f(x + w)} {f(y)} Z" fill="{color}" stroke="{INK}" stroke-width="1.8"></path>'
            + "".join(f'<path d="M{f(x + w * k / 9 + 2)} {f(y - 1)} l {f(12 * s)} {f(-8 * s)}" stroke="#6A4A22" stroke-width="1.2"></path>' for k in range(1, 9)))

def low_table(x, y, w, s=1.0):
    """A low table on the floor; (x, y) its left foot, the top at y - 30 s."""
    return (f'<rect x="{f(x)}" y="{f(y - 30 * s)}" width="{f(w)}" height="{f(7 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
            + "".join(f'<rect x="{f(lx)}" y="{f(y - 23 * s)}" width="{f(6 * s)}" height="{f(23 * s)}" fill="#5A2E16" stroke="{INK}" stroke-width="1.6"></rect>' for lx in (x + 5 * s, x + w - 11 * s)))

def doorway(x, top, w, b, seed, night=True):
    """An open doorway onto the street: the jambs and lintel, and through it the street by night (or day) — house fronts
    across the way with lit windows, the paving, the sky and stars."""
    uid = f"dw{seed}"
    hh = b - top
    o = [f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(top)}" width="{f(w)}" height="{f(hh)}"></rect></clipPath></defs><g clip-path="url(#{uid})">',
         f'<rect x="{f(x)}" y="{f(top)}" width="{f(w)}" height="{f(hh)}" fill="{"#141838" if night else "#8FD0E2"}"></rect>']
    if night: o.append(f'<g transform="translate({f(x)} {f(top)})">' + mk.stars(10, w, hh * 0.3, seed) + '</g>')
    r = random.Random(seed); xx = x - 4
    while xx < x + w:
        bw = w * r.uniform(0.3, 0.5); bh = hh * r.uniform(0.42, 0.62)
        o.append(f'<rect x="{f(xx)}" y="{f(b - hh * 0.16 - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{"#3A3456" if night else "#E8D8B0"}" stroke="{INK}" stroke-width="1.4"></rect>'
                 f'<rect x="{f(xx + bw * 0.3)}" y="{f(b - hh * 0.16 - bh * 0.72)}" width="{f(bw * 0.22)}" height="{f(bh * 0.18)}" fill="{"#FFC14D" if night and r.random() < 0.7 else "#2A2030"}" stroke="{INK}" stroke-width="1"></rect>')
        xx += bw
    o.append(f'<rect x="{f(x)}" y="{f(b - hh * 0.16)}" width="{f(w)}" height="{f(hh * 0.16)}" fill="{"#4A4458" if night else "#C8B898"}"></rect>'
             + "".join(f'<path d="M{f(x)} {f(b - hh * 0.16 * k / 3)} L {f(x + w)} {f(b - hh * 0.16 * k / 3)}" stroke="{INK}" stroke-width="0.8" opacity="0.5"></path>' for k in (1, 2)))
    if night: o.append(lamp_glow(x + w * 0.7, b - hh * 0.5, hh * 0.3, f"{uid}g", color="#FFC14D", op=0.35))
    o.append('</g>' + f'<rect x="{f(x - 10)}" y="{f(top - 12)}" width="{f(w + 20)}" height="12" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(jx)}" y="{f(top)}" width="10" height="{f(hh)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>' for jx in (x - 10, x + w)))
    return "".join(o)

def study(p, w, h, seed, stage="dictate", scribe=None, bearer=None, night=True, window="city", writer=None, fig_h=None):
    """The letter written: a room of a house by lamplight, close in, the people standing about 70% of the panel's height —
    stage "dictate": the writer standing at the left, his hand out, the scribe sitting cross-legged on a mat writing on the
    roll across his knee, a low table at his side with the lamp and the inkpot, a couch behind the writer, pigeonholes of
    scrolls and the window on the city (the Acrocorinth) on the wall; "read": the scribe holding the roll up to read it
    back, the writer listening; "give": the writer handing the sealed scroll to the bearer standing in the open doorway
    onto the night street. scribe: dict(cloth, head, cord) (TERTIUS_LOOK) or False for none; bearer: dict(cloth, veil) for
    a woman (PHOEBE_LOOK) or dict(cloth, head, beard) for a man; writer: fig(p, x, y, s, flip, up, extra) (paul_fig)."""
    scribe = TERTIUS_LOOK if scribe is None else scribe
    writer = writer or paul_fig
    b = h * 0.95
    s = (fig_h or h * 0.72) / 205
    k = s
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E" if night else "#D8C098", floor="#3A2A20" if night else "#8A6A4A")]
    if night: o.append(lamp_glow(w * 0.5, b - 60 * k, max(w, h) * 0.55, f"{p}lg", op=0.45))
    give = stage == "give"
    # the wall: pigeonholes and the window
    ph_w, ph_h = min(w * 0.2, 130 * k), min(h * 0.32, 80 * k)
    if give:
        o.append(pigeonholes(w * 0.36, b - 205 * k, ph_w, ph_h, seed))
        if window: o.append(_window(w, h, w * 0.06, b - 200 * k, min(w * 0.16, 110 * k), min(h * 0.36, 90 * k), night, seed))
        dx, dw = w * 0.68, min(w * 0.22, 120 * k)
        o.append(doorway(dx, b - 196 * k, dw, b, seed + 7, night))
    else:
        o.append(pigeonholes(w * 0.86 - ph_w, b - 205 * k, ph_w, ph_h, seed))
        if window: o.append(_window(w, h, w * 0.4, b - 210 * k, min(w * 0.17, 115 * k), min(h * 0.38, 95 * k), night, seed))
    o.append(mat(w * 0.44, b, 120 * k, k) if not give else mat(w * 0.06, b, 110 * k, k))
    if give:
        o.append(scribe_seated(w * 0.12, b - 4 * k, k, **{kk: vv for kk, vv in scribe.items() if kk in ("cloth", "head", "cord")}, stage="write") if scribe else "")
        o.append(low_table(w * 0.24, b, 46 * k, k) + clay_lamp(w * 0.24 + 23 * k, b - 31 * k, k * 0.5) + inkpot(w * 0.24 + 40 * k, b - 30 * k, k * 0.5))
        scroll_ = sealed_scroll(-70, -150, 0.3, rot=12)                     # the sealed letter in the bearer's hand
        o.append(writer(p, w * 0.5, b, s, flip=True, up=[(-22, -158), (-48, -150), (-72, -150)]))
        if bearer:
            reach = [(-22, -158), (-42, -146), (-62, -146)]
            bx = dx + dw * 0.5
            if "veil" in bearer: o.append(robed(p, bx, b, s * 0.94, bearer["cloth"], woman=True, veil=bearer["veil"], mantle=bearer.get("mantle"), up=reach, extra=scroll_))
            else: o.append(robed(p, bx, b, s, bearer["cloth"], head=bearer.get("head"), beard=bearer.get("beard"), up=reach, extra=scroll_))
        return "".join(o)
    o.append(couch(w * 0.02, b, min(w * 0.18, 120 * k), k))
    o.append(writer(p, w * 0.24, b, s, flip=True, up=[(-22, -158), (-48, -150), (-72, -160)] if stage == "dictate" else None))
    if scribe:
        sx = w * 0.56
        o.append(scribe_seated(sx, b - 4 * k, k, **{kk: vv for kk, vv in scribe.items() if kk in ("cloth", "head", "cord")}, flip=True,
                               stage="write" if stage == "dictate" else "read"))
        tx = (w * 0.24 + 76 * k + sx - 78 * k) / 2 - 26 * k             # the low table between them, the lamp and the inkpot on it
        o.append(low_table(tx, b, 52 * k, k) + clay_lamp(tx + 18 * k, b - 31 * k, k * 0.5) + inkpot(tx + 42 * k, b - 30 * k, k * 0.5))
    if bearer:
        bx = w * 0.92
        if "veil" in bearer: o.append(robed(p, bx, b, s * 0.94, bearer["cloth"], woman=True, veil=bearer["veil"], flip=True))
        else: o.append(robed(p, bx, b, s, bearer["cloth"], head=bearer.get("head"), beard=bearer.get("beard"), flip=True))
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

def face_portrait(tok, tok2=None, bg="radial-gradient", light="#FFE680", ground=("#3A2A3A", "#8A5A4A")):
    """A portrait for a greeting cell: a shaded profile face (a faces.face / ntcast-style token) looking right, as large as
    the cell allows, over a soft light; tok2 a second face set behind it, a little higher and to the right (a couple:
    Prisca and Aquila). Give each person their own cool, dark or off-white headcloth or veil in their face token."""
    def draw(p, w, h):
        uid = f"{p}fp"
        o = [f'<defs><radialGradient id="{uid}" cx="0.7" cy="0.3" r="0.9"><stop offset="0" stop-color="{light}"></stop><stop offset="0.45" stop-color="{ground[1]}"></stop>'
             f'<stop offset="1" stop-color="{ground[0]}"></stop></radialGradient></defs><rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="url(#{uid})"></rect>']
        if tok2:
            s2 = min(w / 300, (h + 10) / 420) * 0.92
            o.append(mk.face(tok2, f(w * 0.3 - 40 * s2), f(h - 380 * s2 - h * 0.1), round(s2, 3)))
        s = min(w / (330 if tok2 else 300), (h + 10) / 380)
        o.append(mk.face(tok, f(-40 * s - (w * 0.06 if tok2 else 0)), f(h - 380 * s + 6), round(s, 3)))
        return "".join(o)
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
    name, tg = (re.sub(r"&(?![#\w]+;)", "&amp;", t) for t in (name, tg))     # a bare "&" (PRISCA & AQUILA) breaks the EPUB's XHTML
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
