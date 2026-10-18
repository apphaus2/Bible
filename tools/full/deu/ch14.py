"""Deuteronomy volume, Chapter 14 — The Song of Moses (Deuteronomy 32). Every verse, word for word from ref/asv.
The song in song boxes (speech.py "song" lines) over the rain on the grass, the Rock, the eagle over her young, the high
places and the fat of the land, the strange gods, the fire and the arrows, and the heavens; every third panel Moses' face;
then Set your heart unto all the words, and Jehovah's word to go up mount Nebo and die there."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus4 as E4, exodus5 as V
from fx import chapter_title, end_mark
from discourse import seg, pack
from deu import G, art as K, art2 as K2
from deu.common import shade, sing, say, gd, cp, says, gods, caps, MOODS
from exo import art6 as A6
from num import art7 as N7, art13 as N13
from num.art import ALL
from num.pages import Pages
from genesis import art as X
from genesis.art2 import ground, hills
from genesis.ch02 import SKY
from deu import ch13 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P

def rock(w, h):
    o = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="#5A6E8A"></rect>', V.rays(w * 0.5, h * 0.2, 30, 20, w, color="#FFF4C2", op=0.25)]
    o.append(f'<path d="M{w * 0.2:.1f} {h:.1f} L {w * 0.3:.1f} {h * 0.5:.1f} L {w * 0.46:.1f} {h * 0.36:.1f} L {w * 0.62:.1f} {h * 0.42:.1f} L {w * 0.78:.1f} {h * 0.62:.1f} L {w * 0.86:.1f} {h:.1f} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    return "".join(o)
def eagle(w, h):
    return (f'<rect x="0" y="0" width="{w}" height="{h}" fill="#8FD0E2"></rect>' + hills(w, h, h * 0.7, 3, color="#B5652E", amp=16)
            + A6.eagle(w * 0.5, h * 0.4, min(2.4, h / 120)) + A6.eagle(w * 0.3, h * 0.6, min(1.0, h / 260)) + A6.eagle(w * 0.72, h * 0.62, min(0.9, h / 280)))
def fire(w, h):
    import exodus as E
    return f'<rect x="0" y="0" width="{w}" height="{h}" fill="#2A0A0A"></rect>' + "".join(E.blaze(w * (0.1 + i * 0.2), h * 0.96, w * 0.18, h * 0.5, 30 + i) for i in range(5))
RAIN = ("#5A6E8A", lambda w, h: K.rain(w, h, 1411))
LAND = (SKY, lambda w, h: N7.hill_country(w, h, 1412))
NIGHTA = ("#0B0B2A", lambda w, h: X.cosmic(w, h))
ARTS1 = [RAIN, ("#5A6E8A", rock), NIGHTA, ("#8FD0E2", eagle), LAND]
ARTS2 = [("#2A2A3A", lambda w, h: K2.scattered(w, h, 1413)), ("#2A0A0A", fire), NIGHTA, ("#3A1A1A", lambda w, h: K.city_siege(w, h, 1414)), ("#5A6E8A", rock)]


@P("DEU-C14-00-Title", "Chapter 14 · The Song of Moses", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect>' + f'<g transform="translate(0 360)">{eagle(760, 720)}</g>'
    return chapter_title(14, "第十四話", "The Song of Moses", "Deuteronomy 32", shade(svg), "#8FD0E2", v("32:11"), "Deuteronomy · Volume Five")


SEGS = (sing(32, 1, 14, ARTS1, head="Give Ear, Ye Heavens", stamp=32)
        + sing(32, 15, 27, ARTS2, head="But Jeshurun Waxed Fat")
        + sing(32, 28, 43, ARTS2[::-1] + [RAIN], head="See Now That I, Even I, Am He")
        + [seg([caps("32:44-45"), cp("32:46", to="said unto them,"), ("say", v("32:46", frm="Set your heart") + " " + v("32:47"))], "DEUT 32:44–47", tok=MOODS["calm"][0], bg=MOODS["calm"][1], head="It Is Your Life"),
           seg([cp("32:48"), gods("32:49-52")], "DEUT 32:48–52", art=lambda w, h: f'<g transform="translate(0 {h * 0.36:.1f})">' + N13.abarim("ab14", w, h * 0.64, 1415) + '</g>', bg="#F3C88A")])
PG.extend(pack(SEGS, "DEU-C14-D", PG.next(), end=end_mark("NEXT · THE DEATH OF MOSES", "right: 10px; bottom: 34px")))
