"""Shared helpers for the Song of Solomon chapters: song-line builders for discourse.pack, drawings set under the words, page
grouping, and the three voices' faces (the bride, the beloved, the daughters of Jerusalem)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from sng import G

v, sp = G.v, G.span
CODE = "SONG"
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]
def sgs(refs): return [sg(r) for r in _refs(refs)]

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Song of Solomon", code=CODE, **k)

def paged(groups, prefix, start, end="", **k):
    """Pack each group of segments onto a page of its own (pack may still split a group that will not fit). The last head
    seen carries over to the following pages; the end mark goes on the last."""
    out, head = [], ""
    for i, g in enumerate(groups):
        out += pack(g, f"{prefix}{chr(65 + i)}", start + len(out), default_head=head, end=end if i == len(groups) - 1 else "", **k)
        head = next((s["head"] for s in reversed(g) if s["head"]), head)
    return out

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def under(fn, lines, k=None):
    """A drawing fn(w, h) set just under the column of words at the top of its panel (the words' height estimated for the
    panel's real size, as speech.orate sets them)."""
    import speech
    def art(w, h):
        kk = k
        if kk is None:
            bw = w - 24
            s = speech.fit(lines, bw, h * 0.62)
            kk = min(0.62, (speech._height(lines, bw, s) + 34 + 10) / h)
        return f'<g transform="translate(0 {h * kk:.1f})">' + fn(w, h * (1 - kk)) + '</g>'
    return art

def face(refs, tok, lines=None, bg=GOLDEN, **k):
    """A singer's face beside the lines: refs "1:2-4" (each verse its own song box) unless lines are given."""
    return seg(lines or sgs(refs), label(refs), tok=tok, bg=bg, **k)

def drawn(refs, art, bg, lines=None, k=None, **kw):
    """Song lines over a drawing fn(w, h): the words at the top, the drawing filling the room below."""
    lines = lines or sgs(refs)
    return seg(lines, label(refs), bg=bg, art=under(art, lines, k), **kw)

DUSK = "radial-gradient(circle at 70% 30%, #FFB04A 0 20px, #8A3A5A 200px, #1A1028 420px)"
ROSE = "radial-gradient(circle at 70% 30%, #FFE8EE 0 24px, #E87A9A 170px, #5A1A3A 420px)"
LEAF = "radial-gradient(circle at 70% 30%, #F3F8E8 0 24px, #9CCB5E 170px, #1F4A34 420px)"

# the bride: dark and comely, a crimson headscarf with a gold band
_B = dict(skin="#8E5A3A", shadow="#4E2E1E", hair="#0D0D0F", scarf="#4A1A3A", band=True)
BRIDE = F("eve", light="#FFC14D", **_B)
BRIDE_GLAD = F("eve", light="#FFE680", laugh=True, **_B)
BRIDE_NIGHT = F("eve", **dict(_B, skin="#6A4A5A", shadow="#2E1E3E"), brow="sorrow", light="#CFE0FF")
BRIDE_SAD = F("eve", **dict(_B, skin="#6A4A5A", shadow="#2E1E3E"), brow="sorrow", tear=True, light="#CFE0FF")
# the beloved: a shepherd-king, white and ruddy, black locks, a gold band
_L = dict(skin="#E3A57A", shadow="#A8684A", hair="#0D0D0F", hl="#3A3A4A", stubble="#1A1210", band=True)
BELOVED = F("adam", light="#FFE680", **_L)
BELOVED_NIGHT = F("adam", **dict(_L, skin="#9A8AA0", shadow="#4A3A5E"), light="#CFE0FF")
# the daughters of Jerusalem
DAUGHTER = F("eve", skin="#D9A27A", shadow="#A8684A", hair="#3A1E14", scarf="#3A5AAA", band=True, light="#FFF4C2")
DAUGHTER2 = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#1A1210", scarf="#2A7A7A", band=True, light="#FFF4C2")
