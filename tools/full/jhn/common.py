"""Shared helpers for the John chapters: the book's Kit (mrk.common.MarkKit, on oba.minor's Kit), the chapter title, the
panel builders D (words over a drawing) and F (words beside a face), and the cast's faces — Jesus and the recurring New
Testament cast only from ntcast, the people Matthew and Mark also tell of with their faces (mat.common, mrk.common), John's
own people below."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from oba.minor import F as face_of, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT, nxt, fin, _flat
from num.pages import Pages
from fx import chapter_title
from deu.common import shade
import speech
from ntcast import (JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN, PETER, PETER_GRIEF, ANDREW, JAMES, JOHN, MATTHEW,
                    THOMAS, PHILIP, JUDAS, MARY, MARY_GRIEF, MAGDALENE, MARTHA, BAPTIST, PHARISEE, CAIAPHAS, PILATE, HEROD, CENTURION, ROBES)
from mat.common import (SCRIBE, SCRIBE_STERN, PRIEST, SADDUCEE, BAPTIST_STERN, BAPTIST_HUMBLE, CROWD_MAN, MAID, JOHN_DISCIPLE, WITNESS, CAIAPHAS_RENT, PILATE_TROUBLED,
                        ARIMATHAEA, SOLDIER)
from mrk.common import MarkKit, MAGDALENE_GRIEF
from jhn import G

CODE = "JOHN"

class JohnKit(MarkKit):
    """mrk.common.MarkKit, with one more cost in the page packing: a face panel stretched far beyond what its words need
    (the last panel of a page takes whatever room is left) costs `tall`, so a short speech does not end a page as a face
    filling half of it."""
    def pack(self, segs, prefix, start, end="", default_head=None, min_size=12.5, most=4, budget=1150, min_art=200, lone=0.5, keep=0.8, tall=0.7):
        from discourse import _sizes, _chars, _heights, _need, pack as _pack
        def fits(g):
            if len(g) == 1: return True
            if min(_sizes(g)) < min_size: return False
            hs = _heights(g)
            return (all(hh >= (min_art if s["tok"] is None and s["art"] is not None else 170) for s, hh in zip(g, hs))
                    and all(hh >= keep * s["h"] for s, hh in zip(g, hs) if s["h"]))
        def stretched(g):
            hs = _heights(g) if len(g) > 1 else [1022]
            return sum(tall for s, hh in zip(g, hs) if s["tok"] and hh > max(2.0 * _need(s), _need(s) + 280))
        n, INF = len(segs), float("inf")
        best, cut = [0.0] + [INF] * n, [0] * (n + 1)
        for j in range(1, n + 1):
            for i in range(max(0, j - most), j):
                g = segs[i:j]; chars = sum(_chars(x) for x in g)
                if best[i] == INF or (len(g) > 1 and (chars > budget or not fits(g))): continue
                under = max(0.0, (budget * 0.8 - chars) / budget)
                cost = (best[i] + 1 + 3 * under * under + sum(0.25 for x in g[1:] if x["head"]) + (lone if len(g) == 1 else 0) + stretched(g))
                if cost < best[j]: best[j], cut[j] = cost, i
        groups, j = [], n
        while j > 0: groups.insert(0, segs[cut[j]:j]); j = cut[j]
        out, head = [], default_head or ""
        for i, g in enumerate(groups):
            pages = _pack(g, prefix, start + len(out), book=self.book, code=self.code, budget=10 ** 9, most=99, default_head=head,
                          end=end if i == len(groups) - 1 else "")
            for name, t, fn in pages:
                out.append((f"{prefix}-P{len(out) + 1:02d}-" + name.split("-P01-", 1)[1], t, fn))
            head = next((s["head"] for s in reversed(g) if s["head"]), head)
        return out

K = JohnKit(G, CODE, "John")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j
v, sp = G.v, G.span
CREDIT = "John · Volume Forty-Three"
NIGHTF = "radial-gradient(circle at 70% 30%, #9AA8E8 0 14px, #2A2A6A 160px, #0B0B2A 400px)"           # behind a face at night
WHITE = "radial-gradient(circle at 26% 46%, #FFFFFF 0 70px, #FFF8DC 220px, #F3E2B0 460px)"     # behind JESUS_RISEN

def title(num, name, rng, svg, bg, quote):
    """A chapter opener (第一話, 第二話, …)."""
    return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, shade(svg), bg, quote, CREDIT)

def drawn(lines, art, bg, art_h=240, size=17, sky=None, **kw):
    """K.drawn with room for a real picture: the panel as tall as its words need at `size` px plus art_h for the drawing
    (pass h= to fix it). sky=n (or (n, "left")) sets chapter n's stamp at the top right (left) of the drawing, just under the
    words (in the sky or on a wall, clear of the figures below), instead of over the verse label."""
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

def S(a, b, kind="say"):
    """One box per verse, a..b of a chapter: S("4:21", 23)."""
    ch, x = a.split(":"); mk_ = {"say": sy, "cap": cp, "song": sg, "god": gd}[kind]
    return [mk_(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

def said(ref, to, frm, kind="say"):
    """The two halves of a verse of speech: the narration up to `to`, then the words from `frm`."""
    return [cp(ref, to=to), {"say": sy, "god": gd, "song": sg}[kind](ref, frm=frm)]

# ---- John's own cast ---------------------------------------------------------------------------------------------------
_NA = dict(skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#4A3A2A", scarf="#2E5A5A", cord=True)
NATHANAEL = face_of("adam", light="#FFE680", **_NA)
_NI = dict(skin="#C98E66", shadow="#3A3A5A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3E2C62", band=True)
NICODEMUS = face_of("adam", light="#9AA8E8", **_NI)                                  # by night
NICODEMUS_DAY = face_of("adam", light="#FFC14D", **_NI)
NICODEMUS_GRIEF = face_of("adam", brow="sorrow", light="#9AA8C8", **_NI)
JOHN_DISC = face_of("adam", skin="#9A6A4A", shadow="#4A2A1A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#4A4E5A", cord=True,
                    light="#FFC14D")                                                 # one of John's disciples (a cool slate headcloth)
LEVITE = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#E8E2D6", cord=True,
                 brow="scowl", light="#FFC14D")
RULER_FEAST = face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#6A645E", scarf="#E8D8B0", cord=True,
                      light="#FFE680")
_SA = dict(skin="#C98E66", shadow="#6A4A3A", hair="#2A1A10", scarf="#5A2E5E")
SAMARITAN = face_of("eve", light="#FFE680", **_SA)
SAMARITAN_AWE = face_of("eve", light="#FFF4C2", **_SA)
_NO = dict(skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#4A2A6A", band=True)
NOBLEMAN = face_of("adam", brow="sorrow", sweat=True, light="#9AA8C8", **_NO)
NOBLEMAN_GLAD = face_of("adam", light="#FFE680", **_NO)
_LA = dict(skin="#B98A6E", shadow="#4A3A4A", hair="#7A746E", hl="#A8A29A", beard=True, beard_color="#8A847A")
LAME = face_of("adam", brow="sorrow", light="#9AA8C8", **_LA)                      # the man at Bethesda
HEALED = face_of("adam", light="#FFE680", **_LA)
_BL = dict(skin="#B98A6E", shadow="#4A3A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#8A8680", cord=True)
BLIND = face_of("adam", blind=True, light="#9AA8C8", **_BL)                         # the man born blind
SEEING = face_of("adam", light="#FFE680", **_BL)
SEEING_BOLD = face_of("adam", brow="scowl", light="#FFC14D", **_BL)
PARENT = face_of("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#D8D2C6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#6A4A2A", cord=True,
                 brow="sorrow", sweat=True, light="#9AA8C8")
MOTHER_BL = face_of("eve", skin="#B98A6E", shadow="#4A3A3A", hair="#6A645E", scarf="#4A5232", brow="sorrow", light="#9AA8C8")
_MB = dict(skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf="#2E5A42")
MARYB = face_of("eve", light="#FFE680", **_MB)                                       # Mary of Bethany
MARYB_GRIEF = face_of("eve", brow="sorrow", tear=True, light="#9AA8C8", **_MB)
MARTHA_GRIEF = face_of("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#2A1A10", scarf="#8A6A2A", brow="sorrow", tear=True, light="#9AA8C8")
_LZ = dict(skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10")
LAZARUS = face_of("adam", light="#FFE680", **_LZ)                                    # at the supper (12:2)
MAGDALENE_JOY = face_of("eve", skin="#D9A27A", shadow="#7A4A3A", hair="#3A1E14", scarf="#8A2A3A", light="#FFFFFF")
GREEK = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#7A5A3A", hl="#A88A6A", stubble="#7A5A3A", light="#FFE680")
ANNAS = face_of("adam", skin="#C98E66", shadow="#4A2A3A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#F3EFE6", band=True,
                brow="scowl", light="#D7261E")
OFFICER = face_of("adam", skin="#B98A6E", shadow="#3A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A3A46", cord=True,
                  brow="scowl", light="#D7261E")
JEW = face_of("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#5E626E", cord=True,
              brow="scowl", light="#D7261E")                                       # "the Jews" who question him (a cool grey headcloth)
BROTHER = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#4A5A6A", cord=True,
                  brow="scowl", light="#FFC14D")                                    # one of his brethren (7:3)
JUDE = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#4A5A4A", cord=True, light="#FFC14D")   # Judas (not Iscariot)
CROWD = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#4E6A6A", cord=True,
                light="#FFE680")                                                    # one of the multitude
THOMAS_AWE = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#5A4A6A", cord=True, light="#FFFFFF")
PILATE_AFRAID = face_of("adam", skin="#E3B08A", shadow="#6A4A5A", hair="#4A3A2A", hl="#7A6A5A", brow="sorrow", sweat=True, light="#9AA8C8")
PETER_GLAD = face_of("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A2420", hl="#6A645E", beard=True, beard_color="#4A4440", light="#FFF4C2")
