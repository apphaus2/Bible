"""Deuteronomy volume, Chapter 4 — A People for His Own Possession (Deuteronomy 7–8). Every verse, word for word from
ref/eng-asv. Moses' words in speech panels (deu.common.auto), with pictures between: the seven nations, the hornet, the manna
in the wilderness, the good land of wheat and barley, vines and fig-trees and pomegranates, and the flinty rock."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from discourse import seg, pack
from deu import G, art as K
from deu.common import shade, auto, says
from exo import art as A, art5 as A5, art7 as A7
from num import art7 as N7
from num.pages import Pages
from num.art import ALL
from genesis.ch02 import SKY
from genesis.ch03 import SAND
from deu import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MIX = ("calm", "stern", "calm", "fire")


@P("DEU-C04-00-Title", "Chapter 4 · A People for His Own Possession", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect>' + f'<g transform="translate(0 380)">{N7.hill_country(760, 700, 401)}</g>')
    return chapter_title(4, "第四話", "A People for His Own Possession", "Deuteronomy 7 – 8", svg, SKY, v("7:6", frm="Jehovah thy God hath chosen thee"), "Deuteronomy · Volume Five")


ADDR = ("#F3D8A0", lambda w, h: K.address("ad4", w, h, 419))
LAND = (SKY, lambda w, h: N7.hill_country(w, h, 414))
SEGS = ([seg(None, "DEUT 7:1", art=lambda w, h: A.peoples_map(w, h, 411), bg="#0B1A2E", h=260, head="Seven Nations Greater and Mightier", stamp=7)]
        + auto(7, 1, 11, MIX, arts=[ADDR])
        + auto(7, 12, 21, ("calm", "fire"), head="The Hornet")
        + [seg(None, "DEUT 7:20", art=lambda w, h: A7.hornets(w, h, 412), bg=SAND, h=240)]
        + auto(7, 22, 26, ("stern",))
        + [seg(None, "DEUT 8:3", art=lambda w, h: mk.defs("g8", *ALL) + A5.gathering("g8", w, h, 413),
               bg=SAND, h=260, head="Man Doth Not Live by Bread Only", stamp=8)]
        + auto(8, 1, 10, ("calm", "grief"), arts=[LAND], every=3)
        + auto(8, 11, 20, ("stern", "calm", "grief"), head="Beware Lest Thou Forget", arts=[ADDR]))
PG.extend(pack(SEGS, "DEU-C04-D", PG.next(), end=end_mark("NEXT · THE TABLES OF STONE", "right: 10px; top: 10px")))
