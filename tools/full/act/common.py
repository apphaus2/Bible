"""Shared helpers for the Acts chapters: the book's Kit (Mark's MarkKit on oba.minor's Kit), the chapter title, the panel
builders D (words over a drawing) and F (words beside a face), and the cast's faces — Jesus, Peter, John, James, Paul and the
recurring New Testament cast only from ntcast, the people Matthew and Mark also tell of with their faces, Acts' own people
below (each the same in every chapter; their looks are listed in act/__init__.py)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from oba.minor import F as face_of, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT, nxt, fin, _flat
from num.pages import Pages
from fx import chapter_title
from deu.common import shade
import speech
from ntcast import (JESUS, JESUS_TEACH, JESUS_RISEN, PETER, PETER_GRIEF, ANDREW, JAMES, JOHN, MATTHEW, THOMAS, PHILIP, MARY, CAIAPHAS, PHARISEE,
                    CENTURION, PAUL, SAUL_PERSECUTOR, ROBES, _HELMET)
from mat.common import SCRIBE, SCRIBE_STERN, PRIEST, SADDUCEE, CROWD_MAN, SOLDIER
from mrk.common import MarkKit
from est.common import _crown
from act import G

CODE = "ACTS"
import re as _re
_COL = '<div style="position: absolute; left: 12px; top: 34px; bottom: 12px;'     # the column of words over a drawing (speech.orate, top=True)
_NOTCH = _re.compile(r'<div style="position: absolute; (?:left|right): -8px; top: 16px; width: 13px; height: 13px;[^"]*"></div>')

def untail(html):
    """Speech boxes over a drawing lose their notch (the speaker is not at the panel's edge there); speech beside a face keeps
    its notch toward the face."""
    out, i = [], 0
    while True:
        a = html.find(_COL, i)
        if a < 0: out.append(html[i:]); break
        b = html.find('</div>\n', a)
        out.append(html[i:a]); out.append(_NOTCH.sub("", html[a:b])); i = b
    return "".join(out)

class ActKit(MarkKit):
    def pack(self, *a, **k):
        return [(n, t, (lambda fn=fn: untail(fn()))) for n, t, fn in super().pack(*a, **k)]

K = ActKit(G, CODE, "Acts")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j
v, sp = G.v, G.span
CREDIT = "Acts · Volume Forty-Four"
WHITE_LIGHT = "radial-gradient(circle at 26% 46%, #FFFFFF 0 70px, #FFF8DC 220px, #F3E2B0 460px)"

def title(num, name, rng, svg, bg, quote):
    """A chapter opener (第一話, 第二話, …)."""
    return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, shade(svg), bg, quote, CREDIT)

STAMP_BAND = 66

def svg_stamp(n, x, y):
    """Chapter n's stamp drawn inside a drawing, its top-left corner at (x, y): the red-ruled paper label of mk.stamp."""
    kj = f"第{mk.kanji_num(n)}章"
    wd = max(92, 22 * len(kj) + 14)
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate(4 {wd / 2:.1f} 20)">'
            f'<rect x="0" y="0" width="{wd}" height="42" fill="#F3EFE6" stroke="#D7261E" stroke-width="2.5"></rect>'
            f'<text x="{wd / 2:.1f}" y="23" fill="#D7261E" font-family="Noto Sans JP, sans-serif" font-weight="900" font-size="18" text-anchor="middle">{kj}</text>'
            f'<text x="{wd / 2:.1f}" y="35" fill="#D7261E" font-family="IBM Plex Mono, monospace" font-weight="600" font-size="8" letter-spacing="1.3" text-anchor="middle">CHAPTER {n}</text></g>')

def with_stamp(fn, n, side="right"):
    """A drawing fn(w, h) set STAMP_BAND px lower, and chapter n's stamp in the band of plain panel colour left above it — so
    the stamp sits between the words and the picture, clear of every figure, wherever the packer sizes the panel."""
    def art(w, h):
        x = 16 if side == "left" else w - 124
        return f'<g transform="translate(0 {STAMP_BAND})">' + fn(w, h - STAMP_BAND) + '</g>' + svg_stamp(n, x, 10)
    return art

def drawn(lines, art, bg, art_h=240, size=17, sky=None, **kw):
    """K.drawn with room for a real picture (as Mark's): the panel as tall as its words need at `size` px plus art_h for the
    drawing (pass h= to fix it). sky=n (or (n, "left")) sets chapter n's stamp in a band of the panel's own colour between
    the words and the drawing, at the right (left), clear of the figures (the drawing moves down to make room)."""
    if "h" not in kw:
        hw = speech._height(_flat(lines), 678, size)
        kw["h"] = int(max(hw + 44 + art_h, (hw + 40) / 0.6)) + (STAMP_BAND if sky else 0)
    if sky:
        n, side = sky if isinstance(sky, tuple) else (sky, "right")
        art = with_stamp(art, n, side)
    return K.drawn(lines, art, bg, **kw)

def D(lines, fn, bg, **k):
    """Words over a drawing fn(w, h) (the chapters' usual panel)."""
    return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})

def F(lines, tok, bg=GOLDEN, **k):
    """Words beside a face."""
    return K.face(lines, tok, bg=bg, **k)

def S(a, b, kind="say"):
    """One box per verse, a..b of a chapter: S("4:21", 23)."""
    ch, x = a.split(":")
    f = {"say": sy, "song": sg, "cap": cp, "god": gd}[kind]
    return [f(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

def said(ref, to, frm, kind="say"):
    """The two halves of a verse of speech: the narration up to `to`, then the words from `frm`."""
    return [cp(ref, to=to), {"say": sy, "god": gd, "song": sg}[kind](ref, frm=frm)]

def crowned(tok, color="#E8B830"):
    """A king's gold diadem on a close-up face."""
    return tok + _crown(False, color)

def helmed(tok): return tok + _HELMET

# ---- Acts' own cast (faces) ---------------------------------------------------------------------------------------------
PETER_STERN = face_of("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#2A2420", hl="#6A645E", beard=True, beard_color="#4A4440", brow="scowl", light="#D7261E")
PETER_BOLD = face_of("adam", skin="#C8987A", shadow="#5A3A2A", hair="#2A2420", hl="#6A645E", beard=True, beard_color="#4A4440", light="#FFF4C2")
JOHN_BOLD = face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#5A4A3E", light="#FFF4C2")
PAUL_STERN = face_of("adam", skin="#C98E66", shadow="#4A2A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True, brow="scowl", light="#D7261E")
PAUL_GRIEF = face_of("adam", skin="#B98A6E", shadow="#3A2A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
PAUL_COLD = face_of("adam", skin="#B98A6E", shadow="#3A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True, light="#9AA8C8")
SAUL_BLIND = face_of("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True, brow="sorrow", blind=True, light="#9AA8C8")
JAMES_LORD = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#A8A296", scarf="#F3EFE6", cord=True, light="#FFF4C2")
MATTHIAS = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#8A6A3A", cord=True, light="#FFE680")
STEPHEN = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", light="#FFE680")
STEPHEN_STERN = face_of("adam", skin="#C98E66", shadow="#4A2A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", brow="scowl", light="#D7261E")
STEPHEN_GLORY =face_of("adam", skin="#E3B896", shadow="#A87A5A", hair="#2A1A10", hl="#6A5A4E", beard=True, beard_color="#2A1A10", light="#FFFFFF")
GAMALIEL = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#2A3A5A", band=True, light="#FFF4C2")
ANANIAS = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#5A5A3A", cord=True, light="#8A90B0")
SAPPHIRA = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf="#4A4A3A", light="#8A90B0")
PHILIP_EV = face_of("adam", skin="#C98E66", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#2A6A6A", cord=True, light="#FFE680")
SIMON_MAGUS = face_of("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#4A1A5A", band=True, light="#9A8AB0")
SIMON_AFRAID = face_of("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#4A1A5A", band=True, brow="sorrow", sweat=True, light="#9AA8C8")
ETHIOPIAN = face_of("adam", skin="#5A3A2A", shadow="#2A1A14", hair="#0D0D0F", hl="#2A2220", scarf="#F3EFE6", band=True, light="#FFE680")
ANANIAS_DAM = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3A4A5A", cord=True, light="#FFF4C2")
BARNABAS = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#4A2A1A", hl="#7A5A4A", beard=True, beard_color="#4A2A1A", scarf="#3A6A3A", cord=True, light="#FFC14D")
AENEAS = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", light="#FFF4C2")
CORNELIUS = helmed(face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#8A7A6A", hl="#B8AA9A", light="#FFE680"))
CORNELIUS_PRAY = helmed(face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#8A7A6A", hl="#B8AA9A", brow="sorrow", light="#FFF4C2"))
RHODA = face_of("eve", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", light="#FFE680")
AGRIPPA1 = crowned(face_of("adam", skin="#D9A27A", shadow="#5A2A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", light="#E8B830"))
AGRIPPA1_PROUD = crowned(face_of("adam", skin="#D9A27A", shadow="#5A2A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", brow="scowl", light="#D7261E"))
ELYMAS = face_of("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A1A3A", band=True, brow="scowl", light="#6A5A8A")
SERGIUS = face_of("adam", skin="#E3B08A", shadow="#8A5A4A", hair="#5A4A3A", hl="#8A7A6A", light="#FFE680")
SILAS = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#2A4A6A", cord=True, light="#FFC14D")
TIMOTHY = face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#3A2214", hl="#6A5A4E", light="#FFE680")
LYDIA = face_of("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#2A1A10", scarf="#4A2A6A", light="#FFE680")
JAILOR = face_of("adam", skin="#D9A27A", shadow="#4A3A4A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", brow="sorrow", sweat=True, light="#FFC14D")
JAILOR_GLAD = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", light="#FFE680")
MAGISTRATE = face_of("adam", skin="#E3B08A", shadow="#8A5A4A", hair="#6A645E", hl="#9A948A", brow="scowl", light="#D7261E")
ATHENIAN = face_of("adam", skin="#E3B08A", shadow="#7A5A4A", hair="#B8B2A6", hl="#E8E2D6", beard=True, beard_color="#C8C2B6", light="#FFE680")
GALLIO = face_of("adam", skin="#E3B08A", shadow="#8A5A4A", hair="#4A3A2A", hl="#7A6A5A", light="#FFC14D")
AQUILA = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#C8B080", cord=True, light="#FFE680")
PRISCILLA = face_of("eve", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", scarf="#3A6A8A", light="#FFE680")
APOLLOS = face_of("adam", skin="#A8704E", shadow="#4A2A1A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", light="#FFE680")
DEMETRIUS = face_of("adam", skin="#D9A27A", shadow="#5A3A2A", hair="#4A3A2A", hl="#7A6A5A", beard=True, beard_color="#4A3A2A", brow="scowl", light="#D7261E")
TOWNCLERK = face_of("adam", skin="#E3B08A", shadow="#7A5A4A", hair="#8A847A", hl="#B8B2A6", light="#FFC14D")
AGABUS = face_of("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#4A3A2A", cord=True, light="#FFF4C2")
LYSIAS = face_of("adam", skin="#E3B08A", shadow="#7A4A3A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", light="#FFC14D")
HIGH_PRIEST = face_of("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#F3EFE6", band=True, brow="scowl", light="#D7261E")
NEPHEW = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")
TERTULLUS = face_of("adam", skin="#E3B08A", shadow="#6A4A4A", hair="#2A1A10", hl="#5A4A3E", light="#D7261E")
FELIX = face_of("adam", skin="#E3B08A", shadow="#6A4A4A", hair="#4A3A2A", hl="#7A6A5A", stubble="#4A3A2A", light="#FFC14D")
FELIX_AFRAID = face_of("adam", skin="#D8A88A", shadow="#4A3A5A", hair="#4A3A2A", hl="#7A6A5A", stubble="#4A3A2A", brow="sorrow", sweat=True, light="#9AA8C8")
DRUSILLA = face_of("eve", skin="#D9A27A", shadow="#6A4A4A", hair="#1A1210", scarf="#1F5A5A", band=True, light="#FFC14D")
FESTUS = face_of("adam", skin="#E3B08A", shadow="#7A5A4A", hair="#8A7A6A", hl="#B8AA9A", light="#FFE680")
FESTUS_LOUD = face_of("adam", skin="#E3A88A", shadow="#7A4A4A", hair="#8A7A6A", hl="#B8AA9A", brow="scowl", light="#D7261E")
AGRIPPA2 = crowned(face_of("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", light="#FFC14D"))
BERNICE = face_of("eve", skin="#D9A27A", shadow="#5A3A4A", hair="#1A1210", scarf="#2A3A6A", band=True, light="#FFC14D")
JULIUS = helmed(face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", light="#FFC14D"))
JULIUS_COLD = helmed(face_of("adam", skin="#C8987A", shadow="#4A3A4A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", light="#9AA8C8"))
PUBLIUS = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#B8B2A6", hl="#E8E2D6", beard=True, beard_color="#C8C2B6", light="#FFE680")
ELDER = face_of("adam", skin="#B98A6E", shadow="#4A2A3A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#3A2A4A", band=True, brow="scowl", light="#D7261E")
JEW_ROME = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#5A5A6A", cord=True, light="#FFE680")
LAME = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", brow="sorrow", light="#FFC14D")
LAME_HEALED = face_of("adam", skin="#C8987A", shadow="#5A4A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", light="#FFF4C2")
