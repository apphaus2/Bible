"""Shared helpers for the Isaiah chapters: line builders for discourse.pack, the oracle runner S() that lays a run of
prophecy out as speech panels, and the cast's faces (Isaiah from 2 Kings, the kings of Judah, Rabshakeh).

    S("1:2-9", "god", [ISAIAH, A(K.vineyard, "#8FD0E2")], head="Ah Sinful Nation", pre=("say", "hath spoken:"))

S() cuts verses c:a–b into panels of about a page-third of words each (never splitting a verse) and gives each panel the
next look in turn: a face token (the prophet speaking: Voice-box words beside his face are Jehovah's words he delivers),
(face, bg), A(drawing, bg) (the words at the top of a drawing, the drawing pushed down below them), or None (the words over
the night sky). kind is the box for the run: "god" (Jehovah's own words, the Voice box), "say" (the prophet's own words),
"song" (a psalm or song), "cap" (narration). In a "god" run a verse that opens with "Thus saith Jehovah ...:" has that
formula set apart in a caption. kinds={verse: kind} overrides single verses; pre=(kind, phrase) sets the first verse's
opening through phrase in another box."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg
from isa.layout import pack as _pack
import speech
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from genesis.ch02 import NIGHT
from kg2.common import (HEZEKIAH, HEZEKIAH_GRIEF, HEZEKIAH_SICK, RABSHAKEH, ISAIAH, ELIAKIM, BABYLONIAN, ISRAELITE, MESSENGER, PROPHET)
from chr2.common import AHAZ, UZZIAH
from isa import G

v, sp = G.v, G.span
CODE = "ISA"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def sgs(refs): return ("song", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Isaiah", code=CODE, **k)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

# ---- the cast ------------------------------------------------------------------------------------------------------------
_IS = dict(skin="#B98A6E", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#4A3A6A", cord=True)
ISAIAH_STERN = F("adam", shadow="#4A2A3A", brow="scowl", light="#D7261E", **_IS)
ISAIAH_GRIEF = F("adam", shadow="#3A2A4A", brow="sorrow", tear=True, light="#9AA8C8", **_IS)
ISAIAH_AWE = F("adam", shadow="#3A3A5A", brow="sorrow", sweat=True, light="#FFD23F", **_IS)
ISAIAH_JOY = F("adam", shadow="#5A4A3A", light="#FFE680", **_IS)
SHEARJASHUB = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")
SHEBNA = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A5A1A", band=True, brow="scowl", light="#FFC14D")
WATCHMAN = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#5A6A8A", light="#9AA8C8")
CYRUS = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A2A6A", band=True, light="#FFE680")
ZION = F("eve", skin="#C98E66", shadow="#3A2A4A", hair="#1A1210", scarf="#3A4A7A", brow="sorrow", tear=True, light="#9AA8C8")
ZION_JOY = F("eve", skin="#D9A27A", shadow="#6A4A4A", hair="#1A1210", scarf="#3A4A7A", band=True, light="#FFE680")
BABYLON_Q = F("eve", skin="#D9A27A", shadow="#5A2A3A", hair="#0D0D0F", band=True, kohl=True, collar=True, brow="scowl", light="#D7261E")
KING_BABYLON = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#2A4A6A", band=True, brow="scowl", light="#D7261E")
KING_ASSYRIA = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#8A1A1A", band=True, brow="scowl", light="#D7261E")
HEZEKIAH_JOY = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#1F3A7A", band=True, light="#FFF4C2")
MOOD_BG = {ISAIAH: GOLDEN, ISAIAH_STERN: RED, ISAIAH_GRIEF: COLD, ISAIAH_AWE: GOLDEN, ISAIAH_JOY: GOLDEN, WATCHMAN: COLD, ZION: COLD, ZION_JOY: GOLDEN,
           BABYLON_Q: RED, KING_BABYLON: RED, RABSHAKEH: RED, HEZEKIAH_GRIEF: COLD, HEZEKIAH_SICK: COLD, SHEBNA: RED, AHAZ: RED, KING_ASSYRIA: RED}

# ---- segments ----------------------------------------------------------------------------------------------------------
def face(lines, ref, tok, bg=None, **k): return seg(lines, ref, tok=tok, bg=bg or MOOD_BG.get(tok, GOLDEN), **k)

class A:
    """A drawing look: fn(w, h) -> svg, set below the words; bg is the panel colour above the drawing; h: a fixed panel
    height (px), for a drawing that needs more room than the words would give it."""
    def __init__(self, fn, bg, k=None, h=None):
        self.fn, self.bg, self.k, self.h = fn, bg, k, h

def under(fn, lines, k=None):
    """fn pushed down below a column of words at the top of the panel (k: a fixed share instead of the estimate)."""
    def art(w, h):
        kk = k
        if kk is None:
            bw = w - 24
            s = speech.fit(lines, bw, h * 0.62)
            kk = min(0.6, max(0.1, (34 + speech._height(lines, bw, s) - 20) / h))
        return f'<g transform="translate(0 {h * kk:.1f})">' + fn(w, h * (1 - kk)) + '</g>'
    return art

def drawn(lines, ref, art, bg, **k):
    """Words at the top of a drawing: art is A(...), or fn(w, h) (pushed below the words), or a full-panel svg callable with full=True."""
    full = k.pop("full", False)
    if isinstance(art, A):
        if art.h and "h" not in k: k["h"] = art.h
        bg, kk, art = art.bg, art.k, art.fn
    else: kk = None
    return seg(lines, ref, bg=bg, art=art if full else under(art, lines, kk), **k)

def night(lines, ref, **k):
    """Words over the night sky (no face, no drawing)."""
    return seg(lines, ref, tok=None, bg=NIGHT, **k)

FORMULA = re.compile(r"^((?:(?:And|For|But|Therefore|Yea|Now|Moreover|Behold|Yet|now)[, ]+){0,2}(?:thus|Thus) (?:saith|hath said|said) (?:the Lord,? )?Jehovah)")

def _verse_lines(c, n, kind, pre=None):
    ref = f"{c}:{n}"
    t = G.verses[(c, n)]
    if pre:
        k0, phrase = pre
        head = v(ref, to=phrase)
        rest = t[t.index(phrase) + len(phrase):].strip()
        return [(k0, head)] + ([(kind, v(ref, frm=rest[:24], after=phrase))] if rest else [])
    if kind == "god":
        m = FORMULA.match(t)
        if m:
            i = t.find(":", m.end())
            j = t.find(",", m.end())
            end = i if 0 <= i < m.end() + 110 else (j if j >= 0 else -1)
            if 0 <= j < end and t[j + 1:].lstrip()[:1].isupper() and not t[j + 1:].lstrip().startswith("O "):   # "Thus saith Jehovah, Heaven is my throne": the words begin after the comma
                end = j
            if end < 0 or end > len(t) - 6: return [(kind, v(ref))]
            phrase = t[:end + 1]
            rest = t[end + 1:].strip()
            return [("cap", v(ref, to=phrase)), (kind, v(ref, frm=rest[:24], after=phrase))]
    return [(kind, v(ref))]

def _merge(lines):
    out = []
    for k, t in lines:
        if out and out[-1][0] == k and k != "song": out[-1] = (k, out[-1][1] + " " + t)
        else: out.append((k, t))
    return out

BUDGET = {"face": 540, "art": 400, "night": 600}

def _kind_of(look):
    return "night" if look is None else "art" if isinstance(look, A) else "face"

def S(refs, kind, looks, head=None, stamp=None, kinds=None, pre=None, budget=None, split=None, at=None, fallback=None):
    """A run of verses c:a–b as panels (see the module notes). split: verse numbers that must start a new panel;
    at={verse: look}: the panel holding that verse takes that look. Each drawing is used once: looks are taken in order,
    a drawing already used is skipped, and when only used drawings are left the faces (or fallback, else ISAIAH) cycle."""
    c, vs = refs.split(":")
    c = int(c)
    a, _, b = vs.partition("-")
    a, b = int(a), int(b or a)
    if not isinstance(looks, (list, tuple)) or (isinstance(looks, tuple) and len(looks) == 2 and isinstance(looks[1], str) and looks[1].startswith(("#", "linear", "radial"))):
        looks = [looks]
    looks = list(looks)
    at = dict(at or {})
    kinds = kinds or {}
    split = set(split or ()) | set(at)
    if stamp is None and a == 1: stamp = c
    faces = [l for l in looks if not isinstance(l, A)] or [fallback or ISAIAH]
    used, state = set(), {"ptr": 0, "face": 0}
    def next_look():
        for _ in range(len(looks)):
            l = looks[state["ptr"] % len(looks)]; state["ptr"] += 1
            if isinstance(l, A) and id(l) in used: continue
            if isinstance(l, A): used.add(id(l))
            return l
        l = faces[state["face"] % len(faces)]; state["face"] += 1
        return l
    groups, cur, n = [], [], 0
    chosen = []
    look_now = at.get(a) or next_look()
    if a in at: used.add(id(at[a]))
    for x in range(a, b + 1):
        t = G.verses[(c, x)]
        cap_ = budget or BUDGET[_kind_of(look_now)]
        if cur and (n + len(t) > cap_ or x in split):
            groups.append(cur); chosen.append(look_now); cur, n = [], 0
            if x in at: look_now = at[x]; used.add(id(look_now))
            else: look_now = next_look()
        cur.append(x); n += len(t)
    if cur: groups.append(cur); chosen.append(look_now)
    segs = []
    for gi, g in enumerate(groups):
        lines = []
        for x in g:
            lines += _verse_lines(c, x, kinds.get(x, kind), pre if (x == a and pre) else None)
        lines = _merge(lines)
        ref = f"{CODE} {c}:{g[0]}" + (f"–{g[-1]}" if len(g) > 1 else "")
        look = chosen[gi]
        kw = {}
        if gi == 0:
            if head: kw["head"] = head
            if stamp: kw["stamp"] = stamp
        if look is None: segs.append(night(lines, ref, **kw))
        elif isinstance(look, A): segs.append(drawn(lines, ref, look, None, **kw))
        elif isinstance(look, tuple): segs.append(face(lines, ref, look[0], bg=look[1], **kw))
        else: segs.append(face(lines, ref, look, **kw))
    return segs
