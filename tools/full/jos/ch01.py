"""Joshua volume, Chapter 1 — Be Strong and of Good Courage (Joshua 1–2). Every verse, word for word from ref/asv.
Jehovah's charge to Joshua after the death of Moses; the officers and the three days; Reuben, Gad and the half-tribe of
Manasseh to pass over armed; then the two spies at Jericho: Rahab's house upon the wall, the stalks of flax, the cord
through the window, the line of scarlet thread, three days in the mountain, and the report to Joshua."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from discourse import seg
from num.pages import Pages
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D, RAHAB, SPY, SPY2, JOSHUA, MOODS
from genesis.ch07 import RED
from genesis.ch04 import COLD

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0B0B2A"


@P("JOS-C01-00-Title", "Chapter 1 · Be Strong and of Good Courage", title=True)
def title(n):
    bg, art = D("P01", 1)
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect><g transform="translate(0 360)">{art(760, 720)}</g>'
    from deu.common import shade
    return chapter_title(1, "第一話", "Be Strong and of Good Courage", "Joshua 1 – 2", shade(svg), "#F3D8A0", v("1:9", frm="Be strong", to="neither be thou dismayed:"), "Joshua · Volume Six")


SEGS = [over([cp("1:1"), gods("1:2-5")], "JOSH 1:1–5", "P01", 0, head="Moses My Servant Is Dead", stamp=1),
        over([gods("1:6-9")], "JOSH 1:6–9", "P01", 1),
        face([cp("1:10"), says("1:11")], "JOSH 1:10–11", "lead", head="Within Three Days"),
        face([cp("1:12"), says("1:13-15")], "JOSH 1:12–15", "calm"),
        drawn([cp("1:16", to="saying,"), ("say", v("1:16", frm="All that") + " " + sp("1:17-18"))], "JOSH 1:16–18", lambda w, h: K.armed("ar1", w, h, 111), "#F3D8A0"),
        over([cp("2:1")], "JOSH 2:1", "P02", 0, head="Rahab", stamp=2),
        drawn([cp("2:2", to="saying,"), say("2:2", frm="Behold,"), cp("2:3", to="saying,"), say("2:3", frm="Bring forth")], "JOSH 2:2–3",
              lambda w, h: K.jericho_night("jn1", w, h, 121), NIGHT),
        face([cp("2:4", to="and she said,"), ("say", v("2:4", frm="Yea,") + " " + v("2:5"))], "JOSH 2:4–5", RAHAB, bg=RED),
        over([caps("2:6-7")], "JOSH 2:6–7", "P02", 1),
        face([cp("2:8"), cp("2:9", to="and she said unto the men,"), ("say", v("2:9", frm="I know") + " " + sp("2:10-11"))], "JOSH 2:8–11", RAHAB,
             head="Jehovah Your God, He Is God"),
        face([says("2:12-13")], "JOSH 2:12–13", RAHAB, bg=COLD),
        face([cp("2:14", to="said unto her,"), say("2:14", frm="Our life")], "JOSH 2:14", SPY),
        over([cp("2:15"), cp("2:16", to="And she said unto them,"), say("2:16", frm="Get you")], "JOSH 2:15–16", "P02", 3, head="The Line of Scarlet Thread"),
        face([cp("2:17", to="said unto her,"), ("say", v("2:17", frm="We will") + " " + sp("2:18-20"))], "JOSH 2:17–20", SPY2),
        drawn([cp("2:21", to="And she said,"), say("2:21", frm="According", to="so be it."), cp("2:21", frm="And she sent")], "JOSH 2:21",
              lambda w, h: K.scarlet(w, h, 122), "#8FD0E2"),
        drawn([caps("2:22-23")], "JOSH 2:22–23", lambda w, h: K.mountain_hide("mh1", w, h, 123), "#14123A"),
        drawn([cp("2:24", to="said unto Joshua,"), say("2:24", frm="Truly")], "JOSH 2:24", lambda w, h: K.report("rp1", w, h, 124), "#F3D8A0")]
PG.extend(pack(SEGS, "JOS-C01-D", PG.next(), end=end_mark("NEXT · THE WATERS OF THE JORDAN", "right: 10px; bottom: 34px")))
