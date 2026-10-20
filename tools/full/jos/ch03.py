"""Joshua volume, Chapter 3 — The Walls of Jericho (Joshua 6–7). Every verse, word for word from ref/eng-asv.
Seven priests with seven trumpets of rams' horns before the ark, six days once about the city and the seventh day seven
times; the great shout and the wall fallen down flat (6:21 is words over the dust, nothing drawn); Rahab brought out;
the city burnt. Then Achan and the devoted thing: the flight before Ai, Joshua fallen before the ark, the lot taken tribe
by tribe to Achan, the mantle and the wedge of gold hid in his tent, and the heap of stones in the valley of Achor (7:25
is words only, over the heap)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from genesis.ch03 import hud
from genesis.ch04 import COLD
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D, ACHAN
from jos import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOS-C03-00-Title", "Chapter 3 · The Walls of Jericho", title=True)
def title(n):
    bg, art = D("P06", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#D7261E"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(3, "第三話", "The Walls of Jericho", "Joshua 6 – 7", svg, "#D7261E", v("6:5", frm="all the people shall shout", to="fall down flat,"), "Joshua · Volume Six")


SEGS = [over([caps("6:1"), cp("6:2", to="unto Joshua,"), gd("6:2", frm="See,")], "JOSH 6:1–2", "P05", 0, head="The Walls of Jericho", stamp=6),
        over([gods("6:3-5")], "JOSH 6:3–5", "P05", 1),
        face([cp("6:6", to="said unto them,"), say("6:6", frm="Take up"), cp("6:7", to="unto the people,"), say("6:7", frm="Pass on")], "JOSH 6:6–7", "lead"),
        drawn([caps("6:8-9")], "JOSH 6:8–9", lambda w, h: K.procession("pr3", w, h, 311), "#8FD0E2"),
        face([cp("6:10", to="saying,"), say("6:10", frm="Ye shall not"), caps("6:11")], "JOSH 6:10–11", "calm"),
        drawn([caps("6:12-14")], "JOSH 6:12–14", lambda w, h: K.procession("pr3b", w, h, 312), "#8FD0E2", extra=hud("SIX DAYS", "left: 14px; bottom: 14px", size=20)),
        over([caps("6:15")], "JOSH 6:15", "P05", 2, extra=hud("SEVEN TIMES", "right: 14px; bottom: 40px", size=20)),
        face([cp("6:16"), says("6:17-19")], "JOSH 6:16–19", "lead", head="Shout; for Jehovah Hath Given You the City"),
        over([caps("6:20")], "JOSH 6:20", "P06", 0, head="The Wall Fell Down Flat"),
        over([caps("6:21")], "JOSH 6:21", "P06", 1),
        drawn([cp("6:22", to="spied out the land,"), say("6:22", frm="Go into"), caps("6:23")], "JOSH 6:22–23", lambda w, h: K.rahab_out("ro3", w, h, 313), "#E8A35A", head="Rahab"),
        drawn([caps("6:24-25")], "JOSH 6:24–25", lambda w, h: K.burning(w, h, 314), "#2A0A0A"),
        face([cp("6:26", to="saying,"), say("6:26", frm="Cursed be"), caps("6:27")], "JOSH 6:26–27", "lead"),
        drawn([caps("7:1")], "JOSH 7:1", lambda w, h: K.devoted(w, h, 315), "#2A1408", head="The Devoted Thing", stamp=7),
        drawn([cp("7:2", to="saying,"), say("7:2", frm="Go up", to="spy out the land."), cp("7:2", frm="And the men went up"), cp("7:3", to="said unto him,"), say("7:3", frm="Let not")],
              "JOSH 7:2–3", lambda w, h: K.ai("ai3", w, h, 316), "#F3D8A0"),
        drawn([caps("7:4-5")], "JOSH 7:4–5", lambda w, h: K.ai("ai3b", w, h, 317, rout=True), "#F3D8A0"),
        drawn([caps("7:6")], "JOSH 7:6", lambda w, h: K.fallen("fl3", w, h, 318), "#3A1A2E"),
        face([cp("7:7", to="And Joshua said,"), ("say", v("7:7", frm="Alas,") + " " + sp("7:8-9"))], "JOSH 7:7–9", "grief", head="Israel Hath Sinned"),
        face([cp("7:10", to="unto Joshua,"), gd("7:10", frm="Get thee up;"), gods("7:11-12")], "JOSH 7:10–12", "awe"),
        drawn([gods("7:13-15")], "JOSH 7:13–15", lambda w, h: X.cosmic(w, h), "#0B0B2A"),
        drawn([caps("7:16-18")], "JOSH 7:16–18", lambda w, h: K.lot(w, h), "#0B1A2E", head="Achan Was Taken"),
        face([cp("7:19", to="unto Achan,"), say("7:19", frm="My son,")], "JOSH 7:19", "grief"),
        face([cp("7:20", to="and said,"), ("say", v("7:20", frm="Of a truth") + " " + v("7:21"))], "JOSH 7:20–21", ACHAN, bg=COLD),
        drawn([caps("7:22-23")], "JOSH 7:22–23", lambda w, h: K.devoted(w, h, 319), "#2A1408"),
        drawn([caps("7:24"), cp("7:25", to="And Joshua said,"), say("7:25", frm="Why hast", to="this day."), cp("7:25", frm="And all Israel"), caps("7:26")], "JOSH 7:24–26",
              lambda w, h: K.achor(w, h, 320), "#4A2A3A", head="The Valley of Achor")]
PG.extend(pack(SEGS, "JOS-C03-D", PG.next(), end=end_mark("NEXT · AI AND THE GIBEONITES", "right: 10px; bottom: 34px")))
