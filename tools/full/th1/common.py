"""Shared helpers for the 1 Thessalonians chapters: the letter's kit (epistle.EpistleKit, its faces sized to their words and
its drawings clipped to their panels), its line builders and panels, Paul's faces in his lights (from epistle), and the
faces of Silvanus and Timothy as Acts draws them."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from th1 import G

CODE = "1TH"
K = EpistleKit(G, CODE, "1 Thessalonians", credit="1 Thessalonians · Volume Fifty-Two", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj = K.lt, K.lts, K.ltj, K.lp, K.lj
F = K.F

def D(lines, fn, bg, art_h=200, **kw):
    """K.D, remembering how much of the panel is its drawing (art_h, the part paged() may grow or shrink to fill a page)."""
    s = K.D(lines, fn, bg, art_h=art_h, **kw)
    if "h" not in kw: s["flex"] = min(art_h, s["h"] - 150)
    return s

def glory(lines, flex=200, **kw):
    """K.glory, its burst of light free to grow or shrink by up to `flex` px to fill a page (paged())."""
    s = K.glory(lines, **kw)
    s["flex"] = min(flex, s["h"] - 100)
    return s

def pic(fn, bg, h, **kw):
    """K.pic, the whole drawing free to grow or shrink (paged())."""
    s = K.pic(fn, bg, h, **kw)
    s["flex"] = h - 120
    return s
v, sp = G.v, G.span

def title(num, name, rng, svg, bg, quote):
    """K.title, the name a little smaller when it would run to three lines at the opener's 96 px."""
    return K.title(num, name, rng, svg, bg, quote, size=80 if len(name) > 22 else None)

def lps(*refs, most=280):
    """Paragraphs across a chapter break: lps("2:19-20", "3:1") (K.lp keeps to one chapter)."""
    return [x for r in refs for x in lp(r, most=most)]

def paged(K, groups, prefix, start, end=""):
    """K.pack with the pages chosen by hand: groups is a list of pages, each a list of panels (the last panel of a page takes
    whatever room is left). The drawings of a page (D's art_h, glory's light, pic) grow or shrink together, in proportion,
    until the page is full; the words and the faces keep their heights. Faces alternate sides as K.pack sets
    them; boxes over drawings lose their tails. Returns [(file, board title, fn)] like K.pack."""
    from discourse import pack as _pack
    from epistle import untail
    import asv
    nf = 0
    for g in groups:
        for s_ in g:
            if s_["tok"]:
                if s_["flip"] is None: s_["flip"] = nf % 2 == 1
                nf += 1
    out, head = [], ""
    for i, g in enumerate(groups):
        room = 1022 - 12 * (len(g) - 1)
        flex = sum(s_.get("flex", 0) for s_ in g)
        fixed = sum(s_["h"] - s_.get("flex", 0) for s_ in g)
        assert flex, f"page {i + 1} of {prefix} has nothing that can grow"
        k = (room - fixed) / flex
        lo, hi = (0.6, 2.2) if asv.LANG == "en" else (0.3, 3.5)     # a translation runs longer or shorter than the ASV
        assert lo < k < hi, f"page {i + 1} of {prefix}: its drawings would be scaled by {k:.2f}"
        for s_ in g:
            s_["h"] = int(s_["h"] - s_.get("flex", 0) + s_.get("flex", 0) * k)
        pages = _pack(g, prefix, start + len(out), book=K.book, code=K.code, budget=10 ** 9, most=99, default_head=head,
                      end=end if i == len(groups) - 1 else "")
        assert len(pages) == 1, f"page {i + 1} of {prefix} would not fit on one page"
        for name, t, fn in pages:
            out.append((f"{prefix}-P{len(out) + 1:02d}-" + name.split("-P01-", 1)[1], t, (lambda fn=fn: untail(fn()))))
        head = next((s["head"] for s in reversed(g) if s["head"]), head)
    return out

# ---- the others the letter names (faces) ---------------------------------------------------------------------------------
from act.common import SILAS as SILVANUS, TIMOTHY                                        # as Acts draws them
