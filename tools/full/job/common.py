"""Shared helpers for the Job chapters: line builders for job.jdiscourse.pack, the speakers (name and colour), the poem
builders, and the cast's faces."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from job.jdiscourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from kg2.common import MESSENGER
from exo.art import HEM
from job import G

v, sp = G.v, G.span
CODE = "JOB"

# the speakers: the name on the tag and the colour of their song rule
SPK = {"job": ("JOB", "#D7261E"), "eli": ("ELIPHAZ THE TEMANITE", "#1F8A8A"), "bil": ("BILDAD THE SHUHITE", "#7A3BA8"),
       "zop": ("ZOPHAR THE NAAMATHITE", "#1F5FAD"), "elihu": ("ELIHU", "#3A8A3A"), "wife": ("HIS WIFE", "#5A6E6A"), "satan": ("SATAN", "#4A4A4A")}

def br(t):
    """Keep the poem's lines: a break before each line the ASV starts with a capital after a stop."""
    parts = re.split(r"(?<=[,;:.!?]) (?=[A-Z])", t)
    out = [parts[0]]
    for p in parts[1:]:                 # no line shorter than a few words ("Did I say, Give unto me?" stays one line)
        if len(out[-1]) < 24 or len(p) < 16: out[-1] += " " + p
        else: out.append(p)
    return "<br>".join(out)

def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]

def sg(ref, who="job", frm=None, to=None, after=None):
    """One verse (or a cut of one) of a speech as a song line in the speaker's colour, the poem's lines kept."""
    return ("song" + SPK[who][1], br(v(ref, frm=frm, to=to, after=after)))
def sgs(refs, who="job"): return [sg(r, who) for r in _refs(refs)]
def gdl(refs):
    """Jehovah's words, a Voice box a verse."""
    return [("god", v(r)) for r in _refs(refs)]

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 1.3)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Job", code=CODE, **k)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def face(lines, ref, tok, bg=GOLDEN, who=None, **k): return seg(lines, ref, tok=tok, bg=bg, who=SPK[who] if who else None, **k)
def low(fn, hmax=420):
    """A drawing f(w, h) kept to at most hmax high and set at the foot of a taller panel (the panel's bg fills above it, so
    give the panel the drawing's sky colour): words over a tall panel do not blow the drawing up."""
    def art(w, h):
        hh = min(h, hmax)
        return fn(w, hh) if hh == h else f'<g transform="translate(0 {h - hh:.1f})">' + fn(w, hh) + '</g>'
    return art
def drawn(lines, ref, art, bg, who=None, full=False, **k):
    """Words over a drawing; full=True lets the drawing fill a tall panel (skies, the heavens)."""
    return seg(lines, ref, bg=bg, art=art if full or art is None else low(art), who=SPK[who] if who else None, **k)

def pf(who, refs, tok, bg=GOLDEN, **k):
    """A speaker's verses beside his face."""
    return face(sgs(refs, who), label(refs), tok, bg=bg, who=who, **k)
def pd(who, refs, art, bg, **k):
    """A speaker's verses over a drawing."""
    return drawn(sgs(refs, who), label(refs), art, bg, who=who, **k)
def pf2(who, refs, tok, bg=GOLDEN, **k):
    """As pf, but the first verse of refs is the caption that opens the speech ("Then answered Eliphaz …")."""
    rs = _refs(refs)
    return face([cp(rs[0])] + [sg(r, who) for r in rs[1:]], label(refs), tok, bg=bg, who=who, **k)
def pd2(who, refs, art, bg, **k):
    rs = _refs(refs)
    return drawn([cp(rs[0])] + [sg(r, who) for r in rs[1:]], label(refs), art, bg, who=who, **k)

# ---- the cast ---------------------------------------------------------------------------------------------------------
# Job: grey hair and beard; in his prosperity a white headcloth with a gold band; afflicted, a hood of sackcloth, ash-grey light.
JOB = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", scarf="#F3EFE6", band=True, light="#FFE680")
JOB_ASH = F("adam", skin="#B8957E", shadow="#5A4A4A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", scarf="#5A5248", cord=True, brow="sorrow", light="#B8B4C8")
JOB_GRIEF = F("adam", skin="#B8957E", shadow="#4A3A4A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", scarf="#5A5248", cord=True, brow="sorrow", tear=True, light="#8A9AC8")
JOB_BOLD = F("adam", skin="#B8957E", shadow="#5A2A2A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", scarf="#5A5248", cord=True, brow="scowl", light="#FF6A4A")
JOB_HOPE = F("adam", skin="#C49A7E", shadow="#5A4A4A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", scarf="#5A5248", cord=True, light="#FFE680")
JOB_AWE = F("adam", skin="#C49A7E", shadow="#3A3A5A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", scarf="#5A5248", cord=True, brow="sorrow", sweat=True, light="#9FB8FF")
JOB_OLD = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#D8D2C6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#F3EFE6", band=True, light="#FFD23F")
WIFE = F("eve", skin="#C99A84", shadow="#5A3A3A", hair="#3A2A1E", scarf="#2A4A4A", brow="scowl", light="#B8B4C8") + HEM
# the three friends: Eliphaz (teal headcloth, gold band, white beard), Bildad (slate-purple, cord, grey beard), Zophar
# (deep blue, cord, black beard); Elihu young (dark green, gold band, stubble).
ELIPHAZ = F("adam", skin="#B98A6E", shadow="#3A4A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#1F5A5A", band=True, light="#FFC14D")
ELIPHAZ_STERN = F("adam", skin="#B98A6E", shadow="#3A2A2A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#1F5A5A", band=True, brow="scowl", light="#FF8A3D")
ELIPHAZ_NIGHT = F("adam", skin="#A89AA8", shadow="#2A2A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#1F5A5A", band=True, brow="sorrow", sweat=True, light="#9FB8FF")
BILDAD = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#7A746A", hl="#A8A29A", beard=True, beard_color="#8A847A", scarf="#4A3A6A", cord=True, light="#FFC14D")
BILDAD_STERN = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#7A746A", hl="#A8A29A", beard=True, beard_color="#8A847A", scarf="#4A3A6A", cord=True, brow="scowl", light="#D7261E")
ZOPHAR = F("adam", skin="#B98A6E", shadow="#3A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3F7A", cord=True, light="#FFE680")
ZOPHAR_STERN = F("adam", skin="#B98A6E", shadow="#3A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3F7A", cord=True, brow="scowl", light="#FF6A4A")
ELIHU = F("adam", skin="#D9A27A", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", scarf="#2A5A3A", band=True, light="#FFE680")
ELIHU_HOT = F("adam", skin="#D9A27A", shadow="#5A2A2A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", scarf="#2A5A3A", band=True, brow="scowl", light="#FF6A4A")
ELIHU_AWE = F("adam", skin="#C9A28A", shadow="#2A2A4A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", scarf="#2A5A3A", band=True, brow="sorrow", light="#9FB8FF")
NIGHT = "#0F0E2A"
ASH = "#5A5660"
