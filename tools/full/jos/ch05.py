"""Joshua volume, Chapter 5 — The Sun Stood Still (Joshua 10–11). Every verse, word for word from ref/eng-asv.
The five kings against Gibeon; the night march from Gilgal; the great stones from heaven at the descent of Beth-horon;
Sun, stand thou still upon Gibeon; the five kings hid in the cave at Makkedah (10:24–27 are words over the cave and its
stones: nothing of their deaths drawn); the southern cities taken one by one, as a campaign map; then Jabin of Hazor and
the kings of the north at the waters of Merom, the chariots burnt, Hazor burnt, the whole land taken, the Anakim cut off,
and the land had rest from war."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from deu import art as DA
from genesis.ch04 import COLD
from genesis.ch07 import RED
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D, GIBEONITE, KING_CANAAN
from jos import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
def camp(upto, hi, k=0.4): return K.below(lambda w, h: K.campaign(w, h, upto, hi), k)


@P("JOS-C05-00-Title", "Chapter 5 · The Sun Stood Still", title=True)
def title(n):
    bg, art = D("P07", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 360)">{art(760, 720)}</g>')
    return chapter_title(5, "第五話", "The Sun Stood Still", "Joshua 10 – 11", svg, "#8FD0E2", v("10:12", frm="Sun, stand thou still"), "Joshua · Volume Six")


SEGS = [face([caps("10:1-2"), cp("10:3"), say("10:4")], "JOSH 10:1–4", KING_CANAAN, bg=RED, head="Five Kings of the Amorites", stamp=10),
        drawn([caps("10:5")], "JOSH 10:5", lambda w, h: K.five_kings("fk5", w, h, 511), "#E8B880"),
        face([cp("10:6", to="saying,"), say("10:6", frm="Slack not")], "JOSH 10:6", GIBEONITE, bg=COLD),
        face([caps("10:7"), cp("10:8", to="unto Joshua,"), gd("10:8", frm="Fear them not:")], "JOSH 10:7–8", "awe"),
        drawn([caps("10:9-10")], "JOSH 10:9–10", lambda w, h: K.night_march("nm5", w, h, 512), "#0F0E2A"),
        drawn([caps("10:11")], "JOSH 10:11", lambda w, h: K.hailstones(w, h, 513), "#2A2E4A", head="Great Stones from Heaven"),
        over([cp("10:12", to="in the sight of Israel,"), say("10:12", frm="Sun, stand")], "JOSH 10:12", "P07", 0, head="Sun, Stand Thou Still"),
        over([caps("10:13-14")], "JOSH 10:13–14", "P07", 1),
        drawn([caps("10:15-16"), cp("10:17", to="saying,"), say("10:17", frm="The five kings")], "JOSH 10:15–17", lambda w, h: K.cave(w, h, 514), "#C8A06A",
              head="The Cave at Makkedah"),
        face([cp("10:18", to="And Joshua said,"), ("say", v("10:18", frm="Roll great") + " " + v("10:19"))], "JOSH 10:18–19", "lead"),
        drawn([caps("10:20-21")], "JOSH 10:20–21", lambda w, h: K.cave(w, h, 515, sealed=True), "#C8A06A"),
        face([cp("10:22", to="Then said Joshua,"), say("10:22", frm="Open the mouth"), caps("10:23")], "JOSH 10:22–23", "lead"),
        face([cp("10:24", to="that went with him,"), say("10:24", frm="Come near,", to="these kings."), cp("10:24", frm="And they came near,"),
              cp("10:25", to="said unto them,"), say("10:25", frm="Fear not,")], "JOSH 10:24–25", "lead"),
        drawn([caps("10:26-27")], "JOSH 10:26–27", lambda w, h: K.cave(w, h, 516, sealed=True, dusk=True), "#4A2A3A"),
        drawn([caps("10:28-35")], "JOSH 10:28–35", camp("EGLON", ("MAKKEDAH", "LIBNAH", "LACHISH", "EGLON"), 0.5), MAP, head="All These Kings and Their Land"),
        drawn([caps("10:36-43")], "JOSH 10:36–43", camp(None, ("HEBRON", "DEBIR"), 0.5), MAP),
        drawn([caps("11:1-5")], "JOSH 11:1–5", lambda w, h: K.chariots("ch5", w, h, 517), "#8FD0E2", head="The Waters of Merom", stamp=11),
        face([cp("11:6", to="unto Joshua,"), gd("11:6", frm="Be not afraid")], "JOSH 11:6", "awe"),
        drawn([caps("11:7-9")], "JOSH 11:7–9", lambda w, h: K.chariots("ch5b", w, h, 518, burning=True), "#2A0A0A"),
        drawn([caps("11:10-15")], "JOSH 11:10–15", lambda w, h: K.burning(w, h, 519, city="hazor"), "#2A0A0A", head="Hazor"),
        drawn([caps("11:16-20")], "JOSH 11:16–20", K.below(lambda w, h: K.land_taken(w, h), 0.42), MAP, head="So Joshua Took the Whole Land"),
        drawn([caps("11:21-23")], "JOSH 11:21–23", K.below(lambda w, h: DA.giants(w, h, 520), 0.36), "#3A2A3A")]
PG.extend(pack(SEGS, "JOS-C05-D", PG.next(), end=end_mark("NEXT · THE LAND THAT REMAINETH", "right: 10px; bottom: 34px")))
