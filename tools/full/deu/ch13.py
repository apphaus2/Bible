"""Deuteronomy volume, Chapter 13 — Choose Life (Deuteronomy 29–31). Every verse, word for word from ref/eng-asv.
The covenant in the land of Moab; the secret things; I have set before thee life and death, therefore choose life; Moses a
hundred and twenty years old, and Joshua charged before all Israel; the law written and given to the priests, read every
seventh year; Jehovah in the pillar of cloud at the Tent, the song foretold, and the book laid by the side of the ark."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from discourse import seg, pack
from deu import G, art as K, art2 as K2
from deu.common import shade, auto, say, gd, cp, says, gods, caps, MOODS
from exo import art5 as A5, art10 as A10
from num import art2 as N2, art13 as N13
from num.art import ALL
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import SKY, DUSK
from genesis.ch06 import GOLDEN
from deu import ch12 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
M, MS, MG = MOODS["calm"], MOODS["stern"], MOODS["grief"]
ADDR = ("#F3D8A0", lambda w, h: K.address("ad13", w, h, 1319))
NIGHTA = ("#0B0B2A", lambda w, h: X.cosmic(w, h))


@P("DEU-C13-00-Title", "Chapter 13 · Choose Life", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect>' + f'<g transform="translate(0 380)">{K.address("t13", 760, 700, 1301, raise_hand=True)}</g>')
    return chapter_title(13, "第十三話", "Choose Life", "Deuteronomy 29 – 31", svg, "#F3D8A0", v("30:19", frm="therefore choose life,"), "Deuteronomy · Volume Five")


SEGS = ([seg([cp("29:1"), cp("29:2", to="said unto them,"), ("say", v("29:2", frm="Ye have seen") + " " + sp("29:3-6"))], "DEUT 29:1–6", tok=M[0], bg=M[1], head="The Words of the Covenant", stamp=29)]
        + auto(29, 7, 13, ("calm", "fire"), arts=[ADDR], every=2)
        + auto(29, 14, 21, ("stern", "grief"), head="Lest There Should Be among You a Root", arts=[NIGHTA], every=3)
        + auto(29, 22, 29, ("grief", "calm"), head="The Secret Things", arts=[("#E8B880", lambda w, h: K.rain(w, h, 1321, shut=True))], every=3)
        + auto(30, 1, 10, ("calm", "fire"), head="When All These Things Are Come upon Thee", stamp=30, arts=[("#5A6E8A", lambda w, h: K.rain(w, h, 1322))], every=3)
        + auto(30, 11, 14, ("calm",), head="It Is Not Too Hard for Thee")
        + auto(30, 15, 20, ("fire", "calm"), head="Therefore Choose Life", arts=[ADDR], every=2)
        + [seg([cp("31:1"), cp("31:2", to="said unto them,"), ("say", v("31:2", frm="I am a hundred") + " " + sp("31:3-6"))], "DEUT 31:1–6", tok=MG[0], bg=MG[1], head="I Am a Hundred and Twenty Years Old", stamp=31),
           seg([cp("31:7", to="in the sight of all Israel,"), ("say", v("31:7", frm="Be strong") + " " + v("31:8"))], "DEUT 31:7–8", art=lambda w, h: N13.joshua_set("js13", w, h, 1323), bg=GOLDEN, head="Be Strong and of Good Courage"),
           seg([caps("31:9"), cp("31:10", to="saying,"), ("say", v("31:10", frm="At the end") + " " + sp("31:11-13"))], "DEUT 31:9–13", art=lambda w, h: N2.bearers("br13", w, h, 1324), bg="#C8A06A"),
           seg([gd("31:14", to="that I may give him a charge."), cp("31:14", frm="And Moses and Joshua"), cp("31:15")], "DEUT 31:14–15", art=lambda w, h: mk.defs("tw13", *ALL) + A10.tent_without("tw13", w, h, 1325, cloud=True), bg=SKY, head="Thy Days Approach That Thou Must Die"),
           seg([cp("31:16", to="unto Moses,"), gd("31:16", frm="Behold,"), gods("31:17-18")], "DEUT 31:16–18", hi=19),
           seg([gods("31:19-21")], "DEUT 31:19–21", head="Write Ye This Song"),
           seg([cp("31:22"), cp("31:23", to="and said,"), gd("31:23", frm="Be strong")], "DEUT 31:22–23", art=lambda w, h: mk.defs("tw13b", *ALL) + A10.tent_without("tw13b", w, h, 1326, cloud=True), bg=SKY),
           seg([says("31:24-25"), says("31:26-29")], "DEUT 31:24–29", tok=MS[0], bg=MS[1], head="By the Side of the Ark"),
           seg([caps("31:30")], "DEUT 31:30", art=ADDR[1], bg=ADDR[0])])
PG.extend(pack(SEGS, "DEU-C13-D", PG.next(), end=end_mark("NEXT · THE SONG OF MOSES", "right: 10px; bottom: 34px")))
