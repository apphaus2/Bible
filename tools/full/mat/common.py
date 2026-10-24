"""Shared helpers for the Matthew chapters: the book's Kit (oba.minor), the chapter title, a chart page over roll cells (the
genealogy), and the cast's faces — Jesus and the recurring New Testament cast only from ntcast, Matthew's own people below."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT, nxt, fin
from num.pages import Pages
from fx import chapter_title, page, new
from deu.common import shade
from genesis.ch02 import grid, rows
from genesis.ch03 import clan
import speech, rolls
from ntcast import (JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN, PETER, PETER_GRIEF, ANDREW, JAMES, JOHN, MATTHEW,
                    THOMAS, PHILIP, JUDAS, MARY, MARY_GRIEF, MAGDALENE, MARTHA, BAPTIST, PHARISEE, CAIAPHAS, PILATE, HEROD, CENTURION, ROBES)
from mat import G

CODE = "MATT"
K = Kit(G, CODE, "Matthew")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j
v, sp = G.v, G.span
CREDIT = "Matthew · Volume Forty"

def title(num, name, rng, svg, bg, quote):
    """A chapter opener (第一話, 第二話, …)."""
    return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, shade(svg), bg, quote, CREDIT)

def chart_roll(cells, chart, ch, title_, n, cap=None, bg="#0B1A2E", ref=None, tag="", end="", extra=""):
    """A page of a chart panel (chart(w, h) svg, ch px tall, a caption over its top) above roll cells (name, text, ref, accent),
    the cells' type as large as fits (up to 20px)."""
    room = 1022 - 22 - ch - 12 - 12 * (len(cells) - 1) - (60 if end else 0)
    s = 20.0
    while s > 10 and sum(rolls._rows(cells, s, 1)) > room: s -= 0.5
    rs = rolls._rows(cells, s, 1)
    if end: rs[-1] += 60
    over = ""
    if cap:
        over += (f'\n    <div style="position: absolute; left: 12px; right: 12px; top: 12px; display: flex">' + speech._cap(cap, 12.5) + '</div>')
    if ref: over += mk.ref(ref, "right: 12px; bottom: 12px", color="#0D0D0F", bg="#F3EFE6")
    panel = new(bg, 702, ch - 6, chart(702, ch - 6), over + extra)
    body = panel + grid([clan(nm, t, r, c, size=s) for nm, t, r, c in cells], " ".join(f"{x:.0f}fr" for x in rs), ncol=1)
    if tag:
        body += (f'\n  <div data-label style="position: absolute; left: 26px; right: 26px; top: 8px; text-align: center; font-size: 9px; font-weight: 600; '
                 f'letter-spacing: 0.24em; color: #6B6862">{tag}</div>')
    return page(title_, f"{ch}px minmax(0, 1fr)", body + end, n)

def drawn(lines, art, bg, art_h=240, size=17, **kw):
    """K.drawn with room for a real picture: the panel as tall as its words need at `size` px plus art_h for the drawing
    (pass h= to fix it)."""
    if "h" not in kw:
        from oba.minor import _flat
        kw["h"] = int(speech._height(_flat(lines), 678, size) + 44 + art_h)
    return K.drawn(lines, art, bg, **kw)

def cell(name, refs, accent="#FFD23F", frm=None, to=None):
    """A roll cell: a name over a verse cut or a run of whole verses ("1:2-5")."""
    if "-" in refs and frm is None and to is None: text = sp(refs)
    else:
        a, _, b = refs.partition("-")
        if b:
            c = a.split(":")[0]; x, y = int(a.split(":")[1]), int(b)
            parts = [v(f"{c}:{k}", frm=frm if k == x else None, to=to if k == y else None) for k in range(x, y + 1)]
            text = " ".join(parts)
        else: text = v(a, frm=frm, to=to)
    a, _, b = refs.partition("-")
    return (name, text, f"{CODE} {a}" + (f"–{b}" if b else ""), accent)

# ---- Matthew's own cast ------------------------------------------------------------------------------------------------
_JO = dict(skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#A8803A", cord=True)
JOSEPH = F("adam", light="#FFC14D", **_JO)                                            # the husband of Mary
JOSEPH_TROUBLED = F("adam", brow="sorrow", light="#9AA8C8", **_JO)
JOSEPH_DREAM = F("adam", **dict(_JO, skin="#A88A8E", shadow="#3A3A5A"), brow="sorrow", light="#E8ECF8")
MAGUS = F("adam", skin="#9A6A4A", shadow="#3A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A2A7A", band=True, light="#FFE680")
MAGUS2 = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#1F5A6A", band=True, light="#FFE680")
_HG = dict(skin="#C98E66", shadow="#4A2A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#5A1A4A", band=True)
HEROD_GREAT = F("adam", light="#FFC14D", **_HG)                                       # Herod the king (Matthew 2)
HEROD_TROUBLED = F("adam", brow="sorrow", sweat=True, light="#9AA8C8", **_HG)
HEROD_WROTH = F("adam", brow="scowl", light="#D7261E", **_HG)
SCRIBE = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#3A4A6A", band=True, light="#FFC14D")
SCRIBE_STERN = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#3A4A6A", band=True, brow="scowl", light="#D7261E")
PRIEST = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", band=True, light="#FFC14D")
SADDUCEE = F("adam", skin="#D9A27A", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A2A3A", band=True, brow="scowl", light="#FFC14D")
BAPTIST_STERN = F("adam", skin="#9A6A4A", shadow="#4A2A1A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", brow="scowl", light="#D7261E")
BAPTIST_HUMBLE = F("adam", skin="#9A6A4A", shadow="#4A2A1A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", brow="sorrow", light="#FFF4C2")
LEPER = F("adam", skin="#D8CCC4", shadow="#8A8088", hair="#5A4A3E", hl="#8A7A6E", stubble="#5A4A3E", brow="sorrow", light="#E8ECF8")
LEPER_CLEAN = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#5A4A3E", hl="#8A7A6E", stubble="#5A4A3E", light="#FFF4C2")
RULER = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#2A5A5A", cord=True, brow="sorrow", sweat=True, light="#9AA8C8")
ISSUE = F("eve", skin="#B98A6E", shadow="#4A3A4A", hair="#2A1A10", scarf="#6A5A7A", brow="sorrow", light="#FFE680")
BLIND = F("adam", skin="#A87A5E", shadow="#4A3A3A", hair="#4A3A2E", hl="#7A6A5E", beard=True, beard_color="#4A3A2E", scarf="#7A7A80", brow="sorrow", light="#9AA8C8")
JOHN_DISCIPLE = F("adam", skin="#9A6A4A", shadow="#4A2A1A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#7A5A3A", cord=True, light="#FFC14D")
CROWD_MAN = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFE680")
