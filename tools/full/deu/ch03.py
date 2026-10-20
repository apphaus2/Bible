"""Deuteronomy volume, Chapter 3 — Hear, O Israel (Deuteronomy 5–6). Every verse, word for word from ref/eng-asv.
The ten commandments repeated at Horeb (Voice boxes with the kanji numerals 一…十 over the two tables), the people afar
off, and the Shema: Hear, O Israel, on the door-posts and the gates, and the son's question. Laid out by discourse.pack."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import exodus4 as E4
from fx import chapter_title, end_mark
from discourse import seg, pack
from deu import G, art as K, art3 as K3
from deu.common import say, gd, cp, says, gods, caps
from num.pages import Pages
from genesis.ch02 import DUSK, SKY
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from deu import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
M, MS, MG = K.MOSES_CALM, K.MOSES_STERN, K.MOSES_GRIEF
NUM = lambda k: E4.numeral(k, "left: 16px; bottom: 10px", size=56)
TBL = lambda w, h: K3.tables(w, h, 3)


@P("DEU-C03-00-Title", "Chapter 3 · Hear, O Israel", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A0E1E"></rect>' + f'<g transform="translate(0 380)">{K3.tables(760, 700, 301)}</g>'
    return chapter_title(3, "第三話", "Hear, O Israel", "Deuteronomy 5 – 6", svg, "#1A0E1E", v("6:4"), "Deuteronomy · Volume Five")


SEGS = [
    seg(None, "DEUT 5:1", art=lambda w, h: K.address("f1", w, h, 311, raise_hand=True), bg="#F3D8A0", h=330, head="Jehovah Our God Made a Covenant", stamp=5),
    seg([cp("5:1", to="said unto them,"), say("5:1", frm="Hear, O Israel,"), says("5:2-3"), say("5:4"), say("5:5")], "DEUT 5:1–5", tok=M, bg=GOLDEN),
    seg([gods("5:6-7")], "DEUT 5:6–7", art=TBL, bg="#1A0E1E", extra=NUM(1), head="The Ten Words"),
    seg([gods("5:8-10")], "DEUT 5:8–10", extra=NUM(2)),
    seg([gd("5:11")], "DEUT 5:11", art=TBL, bg="#1A0E1E", extra=NUM(3)),
    seg([gods("5:12-15")], "DEUT 5:12–15", extra=NUM(4), head="Observe the Sabbath Day"),
    seg([gd("5:16")], "DEUT 5:16", art=TBL, bg="#1A0E1E", extra=NUM(5)),
    seg([gd("5:17")], "DEUT 5:17", extra=NUM(6), head="Thou Shalt Not"),
    seg([gd("5:18")], "DEUT 5:18", extra=NUM(7)),
    seg([gd("5:19")], "DEUT 5:19", extra=NUM(8)),
    seg([gd("5:20")], "DEUT 5:20", extra=NUM(9), head="Neither Shalt Thou Covet"),
    seg([gd("5:21")], "DEUT 5:21", art=TBL, bg="#1A0E1E", extra=NUM(10)),
    seg([says("5:22")], "DEUT 5:22", tok=M, bg=GOLDEN),
    seg([says("5:23-27")], "DEUT 5:23–27", art=lambda w, h: K3.afar("f6", w, h, 361), bg="#2A0A0A", head="Go Thou Near"),
    seg([say("5:28", to="said unto me,"), gd("5:28", frm="I have heard"), gods("5:29-31")], "DEUT 5:28–31", tok=M, bg=GOLDEN),
    seg([says("5:32-33")], "DEUT 5:32–33", tok=MS, bg=RED),
    seg([says("6:1-3")], "DEUT 6:1–3", tok=M, bg=GOLDEN, head="Hear, O Israel", stamp=6),
    seg([says("6:4-5")], "DEUT 6:4–5", art=lambda w, h: K.address("f9", w, h, 391, raise_hand=True), bg="#F3D8A0", hi=30),
    seg([says("6:6-9")], "DEUT 6:6–9", art=lambda w, h: K3.doorposts("f10", w, h, 3101), bg=SKY),
    seg([says("6:10-12")], "DEUT 6:10–12", tok=M, bg=GOLDEN, head="Beware Lest Thou Forget Jehovah"),
    seg([says("6:13-16")], "DEUT 6:13–16", tok=MS, bg=RED),
    seg([says("6:17-19")], "DEUT 6:17–19", tok=M, bg=GOLDEN),
    seg([says("6:20-21")], "DEUT 6:20–21", art=lambda w, h: K3.household("f14", w, h, 3141), bg=DUSK, head="When Thy Son Asketh Thee"),
    seg([says("6:22-25")], "DEUT 6:22–25", tok=M, bg=GOLDEN),
]
PG.extend(pack(SEGS, "DEU-C03-D", PG.next(), end=end_mark("NEXT · A PEOPLE FOR HIS OWN POSSESSION", "right: 10px; top: 10px")))
