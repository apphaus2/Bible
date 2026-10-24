"""Shared helpers for the Mark chapters: the book's Kit (oba.minor), the chapter title, the panel builders D (words over a
drawing) and F (words beside a face), and the cast's faces — Jesus and the recurring New Testament cast only from ntcast,
the people Matthew also tells of with Matthew's faces (mat.common), Mark's own people below."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from oba.minor import Kit, F as face_of, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT, nxt, fin
from num.pages import Pages
from fx import chapter_title
from deu.common import shade
import speech
from ntcast import (JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN, PETER, PETER_GRIEF, ANDREW, JAMES, JOHN, MATTHEW,
                    THOMAS, PHILIP, JUDAS, MARY, MARY_GRIEF, MAGDALENE, MARTHA, BAPTIST, PHARISEE, CAIAPHAS, PILATE, HEROD, CENTURION, ROBES)
from mat.common import (SCRIBE, SCRIBE_STERN, PRIEST, SADDUCEE, BAPTIST_STERN, BAPTIST_HUMBLE, LEPER, LEPER_CLEAN, RULER, ISSUE, BLIND, JOHN_DISCIPLE,
                        CROWD_MAN, CANAANITE, FATHER_BOY, RICH_YOUNG, RICH_SAD, MAID, WITNESS, CAIAPHAS_RENT, PILATE_TROUBLED, ARIMATHAEA, SOLDIER)
from mrk import G

CODE = "MARK"
K = Kit(G, CODE, "Mark")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j
v, sp = G.v, G.span
CREDIT = "Mark · Volume Forty-One"

def title(num, name, rng, svg, bg, quote):
    """A chapter opener (第一話, 第二話, …)."""
    return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, shade(svg), bg, quote, CREDIT)

def drawn(lines, art, bg, art_h=240, size=17, **kw):
    """K.drawn with room for a real picture: the panel as tall as its words need at `size` px plus art_h for the drawing
    (pass h= to fix it)."""
    if "h" not in kw:
        from oba.minor import _flat
        hw = speech._height(_flat(lines), 678, size)
        kw["h"] = int(max(hw + 44 + art_h, (hw + 40) / 0.6))       # the words get at most 62% of a panel over a drawing
    return K.drawn(lines, art, bg, **kw)

def D(lines, fn, bg, **k):
    """Words over a drawing fn(w, h) (the chapters' usual panel)."""
    return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})

def S(a, b):
    """One speech box per verse, a..b of a chapter: S("4:21", 23)."""
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

def said(ref, to, frm, kind="say"):
    """The two halves of a verse of speech: the narration up to `to`, then the words from `frm` (one call, two boxes)."""
    return [cp(ref, to=to), (sy if kind == "say" else gd if kind == "god" else sg)(ref, frm=frm)]

# ---- Mark's own cast ---------------------------------------------------------------------------------------------------
JAIRUS = RULER                                                                         # Matthew's "certain ruler" (9:18)
JAIRUS_GLAD = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#2A5A5A", cord=True, light="#FFF4C2")
ISSUE_HEALED = face_of("eve", skin="#C98E66", shadow="#5A4A4A", hair="#2A1A10", scarf="#6A5A7A", light="#FFF4C2")
_GER = dict(skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210")
GERASENE = face_of("adam", light="#FFF4C2", **_GER)                                     # clothed, and in his right mind
GERASENE_PLEAD = face_of("adam", brow="sorrow", light="#FFE680", **_GER)
HERODIAS = face_of("eve", skin="#D9A27A", shadow="#4A2A3A", hair="#1A1210", scarf="#4A1A3A", band=True, brow="scowl", light="#D7261E")
HEROD_SORRY = face_of("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A1A4A", band=True,
                      brow="sorrow", sweat=True, light="#9AA8C8")
DAMSEL_H = face_of("eve", skin="#E3B08A", shadow="#8A5A4A", hair="#1A1210", band=True, light="#FFC14D")   # Herodias' daughter
DEAF = face_of("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#C8B080", cord=True, light="#FFF4C2")
BETHSAIDA = face_of("adam", skin="#C98E66", shadow="#4A3A3A", hair="#3A2A1E", hl="#6A5A4E", stubble="#3A2A1E", scarf="#5A6A3A", cord=True, brow="sorrow", light="#9AA8C8")
BETHSAIDA_SEE = face_of("adam", skin="#C98E66", shadow="#5A4A3A", hair="#3A2A1E", hl="#6A5A4E", stubble="#3A2A1E", scarf="#5A6A3A", cord=True, light="#FFF4C2")
_BAR = dict(skin="#A87A5E", shadow="#4A3A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E")
BARTIMAEUS = face_of("adam", brow="sorrow", light="#FFC14D", **_BAR)
BARTIMAEUS_SEE = face_of("adam", light="#FFF4C2", **_BAR)
SCRIBE_WISE = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#3A4A6A", band=True, light="#FFF4C2")
HERODIAN = face_of("adam", skin="#D9A27A", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#5A1A4A", cord=True, light="#FFC14D")
WIDOW = face_of("eve", skin="#B98A6E", shadow="#4A3A4A", hair="#8A847A", scarf="#3E3E4E", brow="sorrow", light="#FFE680")
SALOME = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#3A2A1E", scarf="#4A5A2A", light="#FFE680")
MARY_JAMES = face_of("eve", skin="#B98A6E", shadow="#5A3A3A", hair="#3A3430", scarf="#5A3A22", light="#FFE680")
MAGDALENE_GRIEF = face_of("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#3A1E14", scarf="#8A2A3A", brow="sorrow", tear=True, light="#9AA8C8")
