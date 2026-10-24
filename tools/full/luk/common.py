"""Shared helpers for the Luke chapters: the book's Kit (Mark's MarkKit over oba.minor's Kit), the chapter title, the panel
builders D (words over a drawing) and F (words beside a face), Q (one verse cut into narration and speech at given phrases),
a chart page over roll cells (the genealogy), and the cast's faces — Jesus and the recurring New Testament cast only from
ntcast, the people Matthew and Mark also tell of with their faces (mat.common, mrk.common), Luke's own people below."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from oba.minor import F as face_of, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT, nxt, fin, _flat
from num.pages import Pages
from fx import chapter_title
from deu.common import shade
import speech
from asv import key
from ntcast import (JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN, PETER, PETER_GRIEF, ANDREW, JAMES, JOHN, MATTHEW,
                    THOMAS, PHILIP, JUDAS, MARY, MARY_GRIEF, MAGDALENE, MARTHA, BAPTIST, PHARISEE, CAIAPHAS, PILATE, HEROD, CENTURION, ROBES)
from mat.common import (SCRIBE, SCRIBE_STERN, PRIEST, SADDUCEE, BAPTIST_STERN, BAPTIST_HUMBLE, LEPER, LEPER_CLEAN, RULER, ISSUE, BLIND, JOHN_DISCIPLE,
                        CROWD_MAN, FATHER_BOY, RICH_YOUNG, RICH_SAD, MAID, WITNESS, CAIAPHAS_RENT, PILATE_TROUBLED, ARIMATHAEA, SOLDIER, COLLECTOR,
                        JUDAS_REMORSE, chart_roll)
from mrk.common import MarkKit, JAIRUS_GLAD, ISSUE_HEALED, GERASENE, GERASENE_PLEAD, HEROD_SORRY, BARTIMAEUS, BARTIMAEUS_SEE, WIDOW, MAGDALENE_GRIEF, SCRIBE_WISE
from luk import G

CODE = "LUKE"
K = MarkKit(G, CODE, "Luke")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j
v, sp = G.v, G.span
CREDIT = "Luke · Volume Forty-Two"

def title(num, name, rng, svg, bg, quote):
    """A chapter opener (第一話, 第二話, …)."""
    return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, shade(svg), bg, quote, CREDIT)

def drawn(lines, art, bg, art_h=240, size=17, sky=None, **kw):
    """K.drawn with room for a real picture (mrk.common.drawn, bound to Luke's Kit): the panel as tall as its words need at
    `size` px plus art_h for the drawing (pass h= to fix it). sky=n (or (n, "left")) sets chapter n's stamp at the top right
    (left) of the drawing, just under the words, clear of the figures standing below."""
    if "h" not in kw:
        hw = speech._height(_flat(lines), 678, size)
        kw["h"] = int(max(hw + 44 + art_h, (hw + 40) / 0.6))
    if sky:
        n, side = sky if isinstance(sky, tuple) else (sky, "right")
        ls = _flat(lines); h = kw["h"]
        top = min(h * 0.62, speech._height(ls, 678, speech.fit(ls, 678, h * 0.62)) + 44)
        kw["extra"] = kw.get("extra", "") + mk.stamp(n, f"{side}: 18px; top: {top + 10:.0f}px")
    return K.drawn(lines, art, bg, **kw)

def D(lines, fn, bg, **k):
    """Words over a drawing fn(w, h) (the chapters' usual panel)."""
    return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})

def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k):
    """Words beside a face."""
    return K.face(lines, tok, bg=bg, **k)

KINDS = {"c": "cap", "s": "say", "g": "god", "n": "song"}
def Q(ref, *spec):
    """One verse cut at phrases into boxes of alternating kinds: Q("1:13", "c", "said unto him,", "s") is the narration up to
    and including "said unto him," then the speech to the end of the verse; Q("1:60", "c", "and said,", "s", "John.", "c") …
    Kinds: c caption, s speech, g the Voice box, n song. Each cut starts exactly where the last one ended."""
    t = G.verses[key(ref)]
    kinds, bounds = [KINDS.get(x, x) for x in spec[0::2]], spec[1::2]
    out, p = [], 0
    for i, kind in enumerate(kinds):
        while p < len(t) and t[p].isspace(): p += 1
        frm, after = (t[p:].split()[0], t[:p]) if p else (None, None)
        if i < len(bounds):
            e = t.find(bounds[i], p)
            if e < 0: raise ValueError(f"LUKE {ref}: {bounds[i]!r} not after {t[p:p + 30]!r}")
            to, e = bounds[i], e + len(bounds[i])
        else: to, e = None, len(t)
        out.append((kind, G.v(ref, frm=frm, to=to, after=after)))
        p = e
    return out

def N(ref, at, kind="s"):
    """The usual verse of speech: the narration up to `at`, then the words spoken (kind s, or g for the Voice, n for song)."""
    return Q(ref, "c", at, kind)

def S(a, b, kind="s"):
    """One box per verse, a..b of a chapter: S("6:20", 23)."""
    ch, x = a.split(":")
    return [(KINDS.get(kind, kind), G.v(f"{ch}:{k}")) for k in range(int(x), int(b) + 1)]

def C(a, b):
    """One caption per verse, a..b of a chapter."""
    return S(a, b, "c")

def cell(name, refs, accent="#FFD23F", frm=None, to=None):
    """A roll cell: a name over a run of whole verses ("3:23-26"), or cut at the ends with frm/to."""
    a, _, b = refs.partition("-")
    c = a.split(":")[0]; x = int(a.split(":")[1]); y = int(b) if b else x
    text = " ".join(v(f"{c}:{k}", frm=frm if k == x else None, to=to if k == y else None) for k in range(x, y + 1))
    return (name, text, f"{CODE} {a}" + (f"–{b}" if b else ""), accent)

# ---- Luke's own cast ---------------------------------------------------------------------------------------------------
# Zacharias the priest: white beard, priest's white headcloth with a blue band (the course of Abijah); dumb, then filled.
_ZA = dict(skin="#C98E66", shadow="#4A3A4A", hair="#D8D2C6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#E8E2D6", band=True)
ZACHARIAS = face_of("adam", light="#FFE680", **_ZA)
ZACHARIAS_AFRAID = face_of("adam", brow="sorrow", sweat=True, light="#FFF4C2", **dict(_ZA, skin="#C9A08A", shadow="#4A3A5A"))
ZACHARIAS_SING = face_of("adam", light="#FFF4C2", **_ZA)
# Elisabeth: grey hair, a deep teal veil.
_EL = dict(skin="#C98E66", shadow="#5A3A3A", hair="#9A948A", scarf="#1F5A5A")
ELISABETH = face_of("eve", light="#FFC14D", **_EL)
ELISABETH_JOY = face_of("eve", light="#FFF4C2", **_EL)
MARY_AWE = face_of("eve", skin="#D2A07E", shadow="#4A3A5A", hair="#2A1A10", scarf="#2A4A7A", brow="sorrow", light="#FFF4C2")
MARY_SING = face_of("eve", skin="#D2A07E", shadow="#6A4A3A", hair="#2A1A10", scarf="#2A4A7A", light="#FFF4C2")
# Joseph the husband of Mary: Matthew's (an ochre robe, a dark olive headcloth, a brown beard).
from mat.common import JOSEPH, JOSEPH_TROUBLED
# the shepherds: a brown headcloth with a cord, stubble; one older with a grey beard
SHEPHERD = face_of("adam", skin="#B98A6E", shadow="#2A2A4A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#6A5A3A", cord=True, brow="sorrow", light="#FFF4C2")
SHEPHERD_JOY = face_of("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFE680")
# Simeon: white hair and beard, a slate-blue headcloth with a cord.  Anna: very old, white hair, a dark-plum veil.
SIMEON = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#3A4A6A", cord=True, light="#FFF4C2")
ANNA = face_of("eve", skin="#B98A6E", shadow="#4A3A4A", hair="#D8D2C6", scarf="#3A2A3A", light="#FFE680")
# the boy Jesus at twelve: ntcast's Jesus look, young and beardless (shorter dark-brown hair, the same olive-brown skin).
from ntcast import _j as _jesus_face
JESUS_BOY = _jesus_face(beard=False, light="#FFF4C2")
DOCTOR = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3A4A6A", band=True, light="#FFE680")
# the people of Nazareth in the synagogue
NAZARENE = face_of("adam", skin="#B98A6E", shadow="#3A2A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#5A4A3A", cord=True, brow="scowl", light="#D7261E")
# Simon the Pharisee (7:36): Matthew's Pharisee look (white headcloth, grey beard); the woman with the ointment: a dark-indigo veil
SIMON_PHARISEE = PHARISEE
SINNER_WOMAN = face_of("eve", skin="#C98E66", shadow="#3A2A3A", hair="#1A1210", scarf="#2A2A4A", brow="sorrow", tear=True, light="#FFE680")
# the widow of Nain: a black veil, a dark-grey robe
NAIN_WIDOW = face_of("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#3A2A1E", scarf="#1E1E26", brow="sorrow", tear=True, light="#9AA8C8")
# Martha (ntcast) and Mary her sister: a soft rose-brown veil
MARY_BETHANY = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf="#7A4A5A", light="#FFE680")
# a lawyer (10:25, 11:45): a dark-green headcloth with a gold band, a black beard
LAWYER = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A4A3A", band=True, light="#FFC14D")
LAWYER_STERN = face_of("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A4A3A", band=True, brow="scowl", light="#D7261E")
# the woman in the multitude (11:27)
CROWD_WOMAN = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf="#4A5A6A", light="#FFE680")
# Zacchaeus: short, black curls and beard, a rich crimson-brown robe with a gold-trimmed teal headcloth
_ZC = dict(skin="#C98E66", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F5A6A", cord=True)
ZACCHAEUS = face_of("adam", light="#FFE680", **_ZC)
# the ruler (18:18): Matthew's rich young man; the blind man of Jericho: Mark's Bartimæus
# Cleopas: a brown headcloth with a cord, a greying beard; his companion bare-headed, young
CLEOPAS = face_of("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#5A4A3E", hl="#8A7A6E", beard=True, beard_color="#6A5A4E", scarf="#6A4A2A", cord=True, brow="sorrow", light="#9AA8C8")
CLEOPAS_JOY = face_of("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#5A4A3E", hl="#8A7A6E", beard=True, beard_color="#6A5A4E", scarf="#6A4A2A", cord=True, light="#FFE680")
# the malefactor who said, Jesus, remember me: words only over the hill (never drawn close)
HEROD_MOCK = face_of("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A1A4A", band=True, brow="scowl", light="#FFC14D")
