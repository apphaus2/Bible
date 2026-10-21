"""Shared helpers for the Ezekiel chapters: line builders for discourse.pack, an automatic splitter for the book's narration
("And the word of Jehovah came unto me, saying," / "And he said unto me,") and Jehovah's words, run() that sets a run of
oracle verses as panels (Voice boxes beside Ezekiel's face or over a drawing), roll cells, and the cast's faces.

Ezekiel: a priest among the captives, grey-black beard, white headcloth with a blue cord."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F, CORD
from ezk.edisc import seg, pack as _pack
from jos.art import below
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from ezk import G

v, sp = G.v, G.span
CODE = "EZEK"
NIGHT = "linear-gradient(180deg, #05050A 0%, #12113A 60%, #2A1A5E 100%)"
AMBER = "radial-gradient(circle at 70% 30%, #FFF4C2 0 30px, #FFB04A 170px, #5A2A10 420px)"

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

# ---- the automatic splitter --------------------------------------------------------------------------------------------
LEAD = [re.compile(r"^(.*?(?:word of Jehovah (?:also |again )?came (?:again |also )?(?:unto|to) me|came the word of Jehovah (?:unto|to) me)[^,]*?, saying,)\s*"),
        re.compile(r"^((?:And |Then |Moreover |Furthermore |Again |So |But )?(?:he|Jehovah) (?:said|spake)(?: (?:also )?(?:unto|to|with) me)?,(?: and said unto me,)?)\s*"),
        re.compile(r"^((?:And|Then|Moreover|So|Again) said he (?:also )?unto me,)\s*"),
        re.compile(r"^(He said (?:also )?unto me,)\s*")]
SAID_I = re.compile(r"^((?:Then|And) said I,)\s*")

def pieces(ref, kind="god"):
    """A verse as [(kind, text)]: a narration lead ("the word of Jehovah came unto me, saying,") in a caption, the rest in
    `kind`. The cuts are taken with G.v, so coverage counts them."""
    t = G.verses[tuple(map(int, ref.split(":")))]
    m = SAID_I.match(t)
    if m:                                       # "Then said I, Ah Lord Jehovah! ..." — Ezekiel's own words
        return [("cap", v(ref, to=m.group(1))), ("say", v(ref, frm=t[m.end():]))]
    for rx in LEAD:
        m = rx.match(t)
        if m:
            lead = m.group(1); rest = t[m.end():]
            out = [("cap", v(ref, to=lead))]
            if rest.strip(): out.append((kind, v(ref, frm=rest)))
            return out
    return [(kind, v(ref))]

def refs_of(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]

def merge(lines):
    """Adjacent boxes of the same kind become one box."""
    out = []
    for kind, t in lines:
        if out and out[-1][0] == kind and kind != "raw": out[-1] = (kind, out[-1][1] + " " + t)
        else: out.append((kind, t))
    return out

def wl(refs, kind="god", ov=None):
    """The lines for a run of verses ("6:1-4"), split automatically; ov maps a ref to its own lines: a list of lines, a
    letter ("c" caption, "g" Voice box, "s" speech, "n" song) for the whole verse, or a tuple of (kind letter, phrase)
    parts for nv()."""
    ov = ov or {}
    out = []
    for r in refs_of(refs):
        o = ov.get(r)
        if o is None: out += pieces(r, kind)
        elif isinstance(o, str): out.append((KINDS[o], v(r)))
        elif isinstance(o, tuple): out += nv(r, *[(KINDS[a], b) for a, b in o])
        else: out += o
    return merge(out)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Ezekiel", code=CODE, **k)

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, k=None, full=False, **kw):
    """Words over a drawing: the drawing set in the space under the words (edisc.under), so the words never cover it;
    full=True lets it fill the whole panel behind the words (skies). k is accepted and ignored (older calls)."""
    kw.setdefault("hi", 19)
    return seg(lines, ref, bg=bg, art=art, under=not full, **kw)

def fz(refs, tok=None, bg=None, kind="god", ov=None, **k):
    """A run of verses beside a face (Ezekiel by default), split automatically."""
    return seg(wl(refs, kind, ov), label(refs), tok=tok or EZEKIEL, bg=bg or GOLDEN, **k)
def dz(refs, art, bg, kind="god", ov=None, k=None, **kw):
    """A run of verses over a drawing, split automatically."""
    return drawn(wl(refs, kind, ov), label(refs), art, bg, **kw)

def groups(c, a, b, budget=480, starts=()):
    """Verses c:a–b grouped into panels of about `budget` characters; a verse with "the word of Jehovah came unto me"
    starts a new panel, and so does a verse in `starts` (a verse a drawing belongs to) once the panel holds a third of the
    budget."""
    out, cur, n = [], [], 0
    for x in range(a, b + 1):
        t = G.verses[(c, x)]
        lead = bool(LEAD[0].match(t))
        if cur and (n + len(t) > budget or lead or (x in starts and n > budget * 0.34)):
            out.append(cur); cur, n = [], 0
        cur.append(x); n += len(t)
    if cur: out.append(cur)
    if len(out) > 1 and sum(len(G.verses[(c, x)]) for x in out[-1]) < budget * 0.3 and not LEAD[0].match(G.verses[(c, out[-1][0])]) \
            and not any(x in starts for x in out[-1]):
        last = out.pop(); out[-1] += last
    return [(g[0], g[-1]) for g in out]

def run(c, a, b, arts=(), faces=None, head=None, stamp=None, budget=480, pat="AF", kind="god", ov=None, heads=None, k=None, generic=()):
    """Verses c:a–b as panels: groups() of about `budget` characters, each over a drawing or beside a face (the next of
    faces: (tok, bg)). arts as a dict {verse: (bg, f(w, h))}: a panel holding that verse is drawn with it (each drawing
    once); a panel with none is a face, or the next of `generic` drawings when the panel before was a face too. arts as a
    list: drawings and faces alternate by the pattern pat ("AF"). The chapter stamp goes on the first panel when a == 1.
    heads maps a verse number to a page head starting there."""
    faces = faces or [(EZEKIEL, GOLDEN)]
    heads = dict(heads or {})
    if head: heads.setdefault(a, head)
    keyed = isinstance(arts, dict)
    starts = set(arts) | set(heads) if keyed else set(heads)
    segs, ai, fi, gi, used, last_face = [], 0, 0, 0, set(), False
    for i, (x, y) in enumerate(groups(c, a, b, budget, starts)):
        refs = f"{c}:{x}" + (f"-{y}" if y != x else "")
        kw = {}
        hd = next((heads[n] for n in range(x, y + 1) if n in heads), None)
        if hd: kw["head"] = hd
        if i == 0 and (stamp or (stamp is None and a == 1)): kw["stamp"] = stamp or c
        art = None
        if keyed:
            key = next((n for n in range(x, y + 1) if n in arts and n not in used), None)
            if key is not None: art = arts[key]; used.add(key)
            elif last_face and generic: art = generic[gi % len(generic)]; gi += 1
        elif arts and (pat[i % len(pat)] == "A" or not faces):
            art = arts[ai % len(arts)]; ai += 1
        if art:
            if len(art) > 2: kw["h"] = art[2]                          # (bg, f, h): a fixed panel height for a plate
            segs.append(dz(refs, art[1], art[0], kind=kind, ov=ov, **kw)); last_face = False
        else:
            tok, bg = faces[fi % len(faces)]; fi += 1
            segs.append(fz(refs, tok, bg, kind=kind, ov=ov, **kw)); last_face = True
    return segs

# ---- roll cells ---------------------------------------------------------------------------------------------------------
def cell(name, refs, accent="#FFD23F", head=None):
    """One roll cell: a name over verses refs ("2:3-8"), every word."""
    return (name, sp(refs), label(refs), accent, head)

def roll(items, prefix, start, tag, **k):
    from rolls import roll_pages
    return roll_pages(items, prefix, start, "Ezekiel", CODE, tag=tag, **k)

# ---- the cast -----------------------------------------------------------------------------------------------------------
BLUE_CORD = CORD.replace("#3A2214", "#1F5FAD")
def _ez(**k):
    base = dict(skin="#C98E66", shadow="#6A4A3A", hair="#3A3632", hl="#7A746E", beard=True, beard_color="#4A4640", scarf="#F3EFE6")
    base.update(k)
    return F("adam", **base) + BLUE_CORD
EZEKIEL = _ez(light="#FFE680")                                                       # calm, gold rim light
EZEKIEL_FIRE = _ez(skin="#E8A06A", shadow="#8A3A2A", light="#FFB04A", brow="sorrow")  # in the vision, lit by the fire
EZEKIEL_AWE = _ez(skin="#E8A06A", shadow="#8A3A2A", light="#FFD23F", brow="sorrow", sweat=True)
EZEKIEL_STERN = _ez(shadow="#5A1A16", brow="scowl", light="#D7261E")                 # set thy face against
EZEKIEL_GRIEF = _ez(skin="#B98A6E", shadow="#3A3A5A", brow="sorrow", light="#9AA8C8")
EZEKIEL_TEAR = _ez(skin="#B98A6E", shadow="#3A3A5A", brow="sorrow", tear=True, light="#9AA8C8")
ELDER = F("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#5A4A3A", cord=True, light="#FFE680")
ELDER2 = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3A4A6A", cord=True, brow="scowl", light="#FFC14D")
CAPTIVE = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", brow="sorrow", light="#9AA8C8")
PELATIAH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A2A2A", band=True, brow="scowl", light="#D7261E")

FZ = [(EZEKIEL, GOLDEN), (EZEKIEL_STERN, RED)]          # the usual alternation beside oracles
FG = [(EZEKIEL_GRIEF, COLD), (EZEKIEL, GOLDEN)]

def nv(ref, *parts):
    """One verse cut into boxes: parts = (kind, phrase) — each box runs from its phrase (None: the verse's start) to the
    next box's phrase: nv("8:5", ("cap", None), ("god", "Son of man,"), ("cap", "So I lifted"))."""
    t = G.verses[tuple(map(int, ref.split(":")))]
    idx, pos = [], 0
    for kind, ph in parts:
        i = 0 if ph is None else t.find(ph, pos)
        if i < 0: raise ValueError(f"EZK {ref}: {ph!r} not found")
        idx.append(i); pos = i + 1
    out = []
    for k, (kind, _) in enumerate(parts):
        seg_ = t[idx[k]:idx[k + 1] if k + 1 < len(idx) else len(t)].strip()
        out.append((kind, v(ref, frm=seg_, to=seg_)))
    return out

KINDS = {"c": "cap", "g": "god", "s": "say", "n": "song"}

def title_art(fn, top, h=700):
    """A chapter title's art: the drawing fn(w, h) under the title's dark band, the sky colour `top` above it, and a dark
    band at the foot so the quote and the credit read."""
    from deu.common import shade
    return shade(f'<rect x="0" y="0" width="760" height="1080" fill="{top}"></rect><g transform="translate(0 {1080 - h})">{fn(760, h)}</g>'
                 '<defs><linearGradient id="tfoot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0D0D0F" stop-opacity="0"></stop>'
                 '<stop offset="1" stop-color="#0D0D0F" stop-opacity="0.85"></stop></linearGradient></defs><rect x="0" y="900" width="760" height="180" fill="url(#tfoot)"></rect>')
