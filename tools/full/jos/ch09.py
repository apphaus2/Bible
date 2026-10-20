"""Joshua volume, Chapter 9 — The Cities of Refuge (Joshua 20–22). Every verse, word for word from ref/eng-asv.
The cities of refuge: the manslayer at the gate, the six cities on a map; the forty and eight cities of the Levites as roll
cells, by the lots of Aaron, Kohath, Gershon and Merari; there failed not aught of any good thing; then the two and a half
tribes sent home with much wealth, the great altar by the Jordan, Phinehas and the ten princes, the answer — the Mighty One,
God, Jehovah, he knoweth — and the altar called Ed."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from num import art7 as N7
from rolls import roll_pages, verse_cells
from deu.common import shade
from genesis.ch02 import SKY
from genesis.ch04 import COLD
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, PHINEHAS, REUBENITE
from jos import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
CODE, MAP = "JOSH", "#0B1A2E"


@P("JOS-C09-00-Title", "Chapter 9 · The Cities of Refuge", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#E8C88A"></rect><g transform="translate(0 360)">{K.refuge_gate("t9", 760, 720, 901)}</g>')
    return chapter_title(9, "第九話", "The Cities of Refuge", "Joshua 20 – 22", svg, "#E8C88A", v("20:3", frm="they shall be unto you"), "Joshua · Volume Six")


SEGS = [face([cp("20:1"), gods("20:2-3")], "JOSH 20:1–3", "awe", head="Assign You the Cities of Refuge", stamp=20),
        drawn([gods("20:4-6")], "JOSH 20:4–6", lambda w, h: K.refuge_gate("rg9", w, h, 911), "#E8C88A"),
        drawn([caps("20:7-9")], "JOSH 20:7–9", K.below(lambda w, h: K.refuge_map(w, h), 0.34), MAP),
        drawn([caps("21:1"), cp("21:2", to="saying,"), say("21:2", frm="Jehovah commanded"), caps("21:3")], "JOSH 21:1–3",
              lambda w, h: K.shiloh("sh9", w, h, 912), "#E8D8B0", head="Cities to Dwell In", stamp=21)]
PG.extend(pack(SEGS, "JOS-C09-D", PG.next()))

LV = "#FF8A3D"
LEVI = (verse_cells(G, CODE, 21, 4, 8, "The Lots of the Levites", LV, head="Forty and Eight Cities", budget=700)
        + verse_cells(G, CODE, 21, 9, 19, "The Children of Aaron", "#FFD23F", budget=520)
        + verse_cells(G, CODE, 21, 20, 26, "Kohath", LV, budget=600)
        + verse_cells(G, CODE, 21, 27, 33, "Gershon", "#5AC8C8", budget=600)
        + verse_cells(G, CODE, 21, 34, 40, "Merari", "#C8A06A", budget=800)
        + [("All the Cities of the Levites", sp("21:41-42"), "JOSH 21:41–42", LV, None)])
PG.extend(roll_pages(LEVI, "JOS-C09-L", PG.next(), "Joshua", CODE, tag="THE CITIES OF THE LEVITES · JOSHUA 21"))

SEGS2 = [drawn([caps("21:43-45")], "JOSH 21:43–45", lambda w, h: N7.hill_country(w, h, 913), SKY, head="All Came to Pass"),
         face([cp("22:1"), cp("22:2", to="and said unto them,"), ("say", v("22:2", frm="Ye have kept") + " " + sp("22:3-5")), caps("22:6")], "JOSH 22:1–6", "calm",
              head="An Altar by the Jordan", stamp=22),
         drawn([cp("22:7"), cp("22:8", to="saying,"), say("22:8", frm="Return with"), caps("22:9")], "JOSH 22:7–9", lambda w, h: K.armed("ar9", w, h, 914), "#F3D8A0"),
         drawn([caps("22:10"), cp("22:11", to="heard say,"), say("22:11", frm="Behold,"), caps("22:12")], "JOSH 22:10–12", lambda w, h: K.altar_ed("ed9", w, h, 915), "#F3B86A"),
         face([caps("22:13-15"), says("22:16-17")], "JOSH 22:13–17", PHINEHAS, head="What Trespass Is This?", hi=17),
         face([says("22:18-20")], "JOSH 22:18–20", PHINEHAS, bg=COLD, hi=17),
         face([caps("22:21"), says("22:22-25")], "JOSH 22:21–25", REUBENITE, head="The Mighty One, God, Jehovah, He Knoweth", hi=16),
         face([says("22:26-29")], "JOSH 22:26–29", REUBENITE, hi=16),
         face([caps("22:30"), cp("22:31", to="the children of Manasseh,"), say("22:31", frm="This day")], "JOSH 22:30–31", PHINEHAS, head="Ed"),
         drawn([caps("22:32-34")], "JOSH 22:32–34", lambda w, h: K.altar_ed("ed9b", w, h, 916, people=False), "#F3B86A")]
PG.extend(pack(SEGS2, "JOS-C09-E", PG.next(), budget=1800, end=end_mark("NEXT · CHOOSE YOU THIS DAY", "right: 10px; bottom: 34px")))
