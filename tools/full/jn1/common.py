"""Shared helpers for the letters of John (1 John, and 2 and 3 John, which import this module): the letter's kit
(JohnKit, on epistle.EpistleKit), its line builders and panels, and John's set — the elder.

John is the same John as ntcast's JOHN (the beloved disciple, young and beardless in the Gospels), now very old at Ephesus:
ntcast JOHN's features and skin, his hair gone white, a long white beard, the lines of age at the brow and the eye, bareheaded.
His faces in five lights, built as epistle.py's PAUL_* faces are, each with its background:
    JOHN_OLD + GOLD_BG (earnest) · JOHN_LAMP + LAMP_BG (writing by lamplight) · JOHN_GRIEF + GRIEF_BG (grieving)
    JOHN_JOY + JOY_BG (white light: "Behold what manner of love", "God is love") · JOHN_STERN + STERN_BG (warning)
At a distance: john_fig(p, x, y, s, flip=, up=, extra=, pose=, seat=, staff=) on epistle.robed(): a faded rust robe (the rust
robe of the Gospels, worn pale), a slate-grey mantle, white hair and a long white beard, a staff in his free hand when he
stands or walks; pose="sit" seated (no staff). Paul is never drawn in these volumes.

The others the letters name (faces for face panels and portraits, looks for the figures in jn1.art), each the same in every
volume; every headcloth and veil cool, dark or off-white (a warm one would read as long hair):
    LADY (2 John: the elect lady) a dark-blue veil, a slate-blue robe · GAIUS (3 John) a grey beard, an off-white headcloth ·
    DIOTREPHES (3 John) a black beard, a near-black headcloth with a gold band, a hard face · DEMETRIUS (3 John) a brown
    beard, a dark-teal headcloth."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG, nxt, fin, face_of, robed, face_portrait, portrait)
from num.pages import Pages
from genesis.art2 import SKIN
import speech
from oba.minor import _flat

# ---- John, the elder: his faces ---------------------------------------------------------------------------------------------
WHITE, WHITE_HL = "#ECE6DA", "#A8A296"
# a long white beard falling from the jaw to a point well below the chin, its strands, the moustache drooping into it
_LONG_BEARD = (
    '\n<path d="M152 226 C 150 262 158 302 170 338 C 180 366 194 386 210 398 C 220 384 228 362 236 338 C 246 312 254 292 251 280 '
    'C 248 270 244 262 240 260 C 236 262 238 270 232 274 C 226 286 214 292 200 290 C 186 286 172 264 164 238 C 160 232 156 228 152 226 Z" '
    f'fill="{WHITE}" stroke="#0D0D0F" stroke-width="1.8" stroke-linejoin="round"></path>'
    f'\n<g fill="none" stroke="{WHITE_HL}" stroke-width="1.3" stroke-linecap="round"><path d="M172 280 C 180 314 192 346 206 380"></path>'
    '<path d="M190 296 C 198 324 206 352 214 376"></path><path d="M208 300 C 214 324 220 346 224 362"></path><path d="M162 262 C 166 292 174 318 184 344"></path>'
    '<path d="M226 296 C 230 312 232 326 232 338"></path></g>'
    f'\n<path d="M212 238 C 222 230 240 230 247 238 C 250 246 246 256 240 262 C 236 254 228 250 214 246 Z" fill="{WHITE}" stroke="#0D0D0F" stroke-width="1.4"></path>'
    f'\n<path d="M236 252 L 226 251" stroke="#0D0D0F" stroke-width="1.6" stroke-linecap="round"></path>')
# the lines of age: two across the brow, crow's feet at the eye's outer corner, a fold under the eye
_AGE = ('\n<g fill="none" stroke="#6A4434" stroke-width="1.4" stroke-linecap="round" opacity="0.75">'
        '<path d="M206 128 C 214 124 222 124 230 127"></path><path d="M204 139 C 212 135 222 135 232 138"></path>'
        '<path d="M205 166 L 196 162"></path><path d="M204 172 L 194 173"></path><path d="M205 177 L 197 183"></path>'
        '<path d="M212 181 C 218 184 224 184 229 180"></path></g>')
# white hair lying closer to the head than the young man's curls (the same hairline), falling behind the ear to the neck
_HAIR = (f'<path d="M234 106 C 238 92 232 72 214 62 C 194 50 160 50 136 64 C 112 78 100 104 100 134 C 100 170 108 210 118 240 C 124 258 136 270 150 264 '
         f'C 146 240 144 220 148 200 C 150 170 160 146 176 132 C 196 118 214 110 234 106 Z" fill="{WHITE}" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
         f'\n  <g fill="none" stroke="{WHITE_HL}" stroke-width="1.5" stroke-linecap="round"><path d="M222 70 C 206 76 196 88 190 104"></path>'
         '<path d="M190 58 C 170 66 156 84 150 104"></path><path d="M140 72 C 124 92 118 116 118 140"></path><path d="M112 150 C 114 180 120 206 128 230"></path></g>\n')
_CURLS = re.compile(r'<path d="M234 106 C 240 96.*?</path>\n  <g fill="none" stroke="#[0-9A-Fa-f]{6}" stroke-width="1.5" stroke-linecap="round">.*?</g>\n', re.S)
_J = dict(skin="#D3A07E", shadow="#7A5244", hair=WHITE, hl=WHITE_HL)                 # ntcast JOHN's skin, a little paler; white hair
def _john(**k): return _CURLS.sub(lambda m: _HAIR, face_of("adam", **{**_J, **k}), count=1) + _AGE + _LONG_BEARD

JOHN_OLD = _john(light="#FFE680")                                                      # earnest, gold light
JOHN_LAMP = _john(skin="#DCA070", shadow="#5A3020", light="#FF9A3D")                   # writing by lamplight
JOHN_GRIEF = _john(skin="#BE9A86", shadow="#4A3A4A", brow="sorrow", tear=True, light="#9AA8C8")
JOHN_JOY = _john(skin="#E6BE9E", shadow="#A87A5A", light="#FFFFFF")
JOHN_STERN = _john(shadow="#5A3030", brow="scowl", light="#D7261E")

# ---- John at a distance -------------------------------------------------------------------------------------------------------
JOHN_LOOK = dict(cloth="#9A5E48", hair=WHITE, beard=WHITE, mantle="#5E6A7A", belt="#5A3A2A")
# a long white beard on the figure (in robed()'s units, over robed()'s beard: the chin at about (0, -172))
_FIG_BEARD = (f'<path d="M-11 -174 C -12 -160 -5 -140 0 -124 C 5 -140 12 -160 11 -174 C 6 -167 -6 -167 -11 -174 Z" fill="{WHITE}" stroke="#0D0D0F" stroke-width="1.4"></path>'
              f'<path d="M-4 -164 L -1 -136 M4 -164 L 2 -138" stroke="{WHITE_HL}" stroke-width="1"></path>')
# a staff held in the hanging hand (+x side, the hand at (28.5, -90)), the hand drawn again over it
_STAFF = ('<path d="M28 -182 L 33 0" stroke="#0D0D0F" stroke-width="7.4" stroke-linecap="round"></path>'
          '<path d="M28 -182 L 33 0" stroke="#8A6A3A" stroke-width="4.4" stroke-linecap="round"></path>'
          f'<ellipse cx="29.5" cy="-92" rx="4.6" ry="6.5" fill="{SKIN}" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')

def john_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool", staff=True):
    """John the elder at a distance (see the module docstring); needs mk.defs(p, *num.art.ALL, "ManUp", "WomanUp")."""
    L = JOHN_LOOK
    st = _STAFF if staff and pose != "sit" else ""
    return robed(p, x, y, s, L["cloth"], hair=L["hair"], beard=L["beard"], mantle=L["mantle"], belt=L["belt"], flip=flip, up=up,
                 extra=_FIG_BEARD + st + extra, pose=pose, seat=seat)

def john_writer(p, x, y, s, flip=False, up=None, extra=""):
    """John as study()'s writer (writer=): standing, his hand out, his staff in the other hand."""
    return john_fig(p, x, y, s, flip=flip, up=up, extra=extra)

# ---- the others the letters name -----------------------------------------------------------------------------------------------
LADY_LOOK = dict(cloth="#5A6A8A", veil="#1F2F5A", mantle="#3A4660")                    # 2 John: the elect lady
GAIUS_LOOK = dict(cloth="#6A5A4A", head="#E8E2D6", cord="#5A4A3A", beard="#9A948A", mantle="#4A5A6A")
DIOTREPHES_LOOK = dict(cloth="#3A2A3A", head="#22222E", cord="#C8963E", beard="#1A1210", mantle="#5A1A2A")
DEMETRIUS_LOOK = dict(cloth="#4A6A6A", head="#2A5A5A", cord="#13302E", beard="#4A2E1E", mantle="#6A5A44")

LADY = face_of("eve", skin="#D9A27A", shadow="#8A5A4A", hair="#2A1A10", scarf=LADY_LOOK["veil"], light="#FFE680")
LADY_JOY = face_of("eve", skin="#E3B08A", shadow="#A87A5A", hair="#2A1A10", scarf=LADY_LOOK["veil"], light="#FFFFFF")
GAIUS = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair=GAIUS_LOOK["beard"], hl="#C8C2B6", beard=True, scarf=GAIUS_LOOK["head"], cord=True, light="#FFE680")
DIOTREPHES = face_of("adam", skin="#B97A5A", shadow="#4A2222", hair=DIOTREPHES_LOOK["beard"], hl="#3A2A1E", beard=True, scarf=DIOTREPHES_LOOK["head"], band=True,
                     brow="scowl", light="#D7261E")
DEMETRIUS = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair=DEMETRIUS_LOOK["beard"], hl="#7A5A4A", beard=True, scarf=DEMETRIUS_LOOK["head"], cord=True, light="#FFF4C2")

# ---- the kit: face panels sized to their words, the room left on a page given to its drawings ------------------------------------
class JohnKit(EpistleKit):
    """EpistleKit with face panels sized to their words (fit_faces) and drawings clipped to their panels (clip), and one change
    to the packing: the page's spare height goes to its drawings, not to a face panel that happens to end the page. (The
    kit's page layout gives the last panel whatever room is left, so a page of a drawing and then a face would set the face
    in a tall panel of empty light; here, on a page that ends with a fixed-height face panel, the drawings are made flexible
    so they take the room, and the face keeps the height its words asked for.) The grouping is EpistleKit.pack's own."""
    def pack(self, segs, prefix, start, end="", default_head=None, min_size=12.5, most=4, budget=1150, min_art=200, lone=0.5, keep=0.8, face_min=230):
        from discourse import _chars, _sizes, _heights, pack as _pack
        from epistle import untail
        nf = 0
        for s_ in segs:
            if s_["tok"]:
                if s_["flip"] is None: s_["flip"] = nf % 2 == 1
                nf += 1
        def fits(g):
            if len(g) == 1: return True
            if min(_sizes(g)) < min_size: return False
            hs = _heights(g)
            return (all(hh >= (min_art if s["tok"] is None and s["art"] is not None else face_min if s["tok"] else 170) for s, hh in zip(g, hs))
                    and all(hh >= keep * s["h"] for s, hh in zip(g, hs) if s["h"]))
        n, INF = len(segs), float("inf")
        best, cut = [0.0] + [INF] * n, [0] * (n + 1)
        for j in range(1, n + 1):
            for i in range(max(0, j - most), j):
                g = segs[i:j]; chars = sum(_chars(x) for x in g)
                if best[i] == INF or (len(g) > 1 and (chars > budget or not fits(g))): continue
                under_ = max(0.0, (budget * 0.8 - chars) / budget)
                cost = best[i] + 1 + 3 * under_ * under_ + sum(0.25 for x in g[1:] if x["head"]) + (lone if len(g) == 1 else 0)
                if cost < best[j]: best[j], cut[j] = cost, i
        groups, j = [], n
        while j > 0: groups.insert(0, segs[cut[j]:j]); j = cut[j]
        out, head = [], default_head or ""
        for i, g in enumerate(groups):
            if len(g) > 1 and g[-1]["tok"] and g[-1]["h"] and any(s["tok"] is None and s["art"] is not None for s in g[:-1]):
                g = [dict(s, h=None) if s["tok"] is None and s["art"] is not None else s for s in g]
            pages = _pack(g, prefix, start + len(out), book=self.book, code=self.code, budget=10 ** 9, most=99, default_head=head,
                          end=end if i == len(groups) - 1 else "")
            for name, t, fn in pages:
                out.append((f"{prefix}-P{len(out) + 1:02d}-" + name.split("-P01-", 1)[1], t, (lambda fn=fn: untail(fn()))))
            head = next((s["head"] for s in reversed(g) if s["head"]), head)
        return out

def kit(G, code, book, credit):
    """The letter's kit (JohnKit), face panels sized to their words and drawings clipped to their panels."""
    return JohnKit(G, code, book, credit=credit, fit_faces=True, clip=True)

# ---- 1 John's kit ---------------------------------------------------------------------------------------------------------------
from jn1 import G
CODE = "1JN"
K = kit(G, CODE, "1 John", "1 John · Volume Sixty-Two")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title, pic = K.D, K.F, K.glory, K.title, K.pic
v, sp = G.v, G.span
