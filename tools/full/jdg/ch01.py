"""Judges volume, Chapter 1 — After the Death of Joshua (Judges 1–2). Every verse, word for word from ref/eng-asv.
Judah shall go up; Adoni-bezek (1:6–7 are words over his empty table: nothing of the maiming drawn); Jerusalem, Hebron,
Othniel and Achsah's springs; Beth-el taken by its entrance; the tribes that drove not out the Canaanites as roll cells;
the angel of Jehovah at Bochim; Joshua's death, a generation that knew not Jehovah, the Baalim, and the round of the judges
as a technical diagram."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages
from deu.common import shade
from deu import art4 as D4
from genesis import art as X
from jos import art as JA
from jos.art import below
from jdg import G, art as K
from discourse import seg
from jdg.common import pack, say, gd, cp, says, gods, caps, face, drawn, KING_CANAAN, CALEB_OLD, ACHSAH, RED, COLD

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)
MAP = "#0B1A2E"


@P("JDG-C01-00-Title", "Chapter 1 · After the Death of Joshua", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A3450"></rect><g transform="translate(0 340)">{K.bochim("t1", 760, 740, 101)}</g>')
    return chapter_title(1, "第一話", "After the Death of Joshua", "Judges 1 – 2", svg, "#3A3450", v("2:16"), "Judges · Volume Seven")


SEGS = [drawn([cp("1:1", to="saying,"), say("1:1", frm="Who shall"), cp("1:2", to="And Jehovah said,"), gd("1:2", frm="Judah shall")], "JDG 1:1–2",
              lambda w, h: JA.shiloh("sh1", w, h, 111), "#E8D8B0", head="Who Shall Go Up for Us First?", stamp=1),
        drawn([cp("1:3", to="unto Simeon his brother,"), say("1:3", frm="Come up", to="into thy lot."), cp("1:3", frm="So Simeon"), caps("1:4-5")], "JDG 1:3–5",
              lambda w, h: JA.armed("ar1", w, h, 112, tribes=("JUDAH", "SIMEON")), "#F3D8A0"),
        drawn([caps("1:6"), cp("1:7", to="And Adoni-bezek said,"), say("1:7", frm="Threescore", to="requited me."), cp("1:7", frm="And they brought")], "JDG 1:6–7",
              lambda w, h: K.empty_table(w, h, 113), "#2A1418"),
        drawn([caps("1:8-11")], "JDG 1:8–11", lambda w, h: JA.burning(w, h, 114, city="jerusalem"), "#2A0A0A"),
        face([cp("1:12", to="And Caleb said,"), say("1:12", frm="He that smiteth"), caps("1:13"), cp("1:14", to="said unto her,"), say("1:14", frm="What wouldest")],
             "JDG 1:12–14", CALEB_OLD, head="Give Me Also Springs of Water"),
        face([cp("1:15", to="said unto him,"), say("1:15", frm="Give me", to="springs of water."), cp("1:15", frm="And Caleb gave")], "JDG 1:15", ACHSAH),
        drawn([caps("1:16-21")], "JDG 1:16–21", lambda w, h: JA.hebron("hb1", w, h, 115), "#F3D8A0"),
        drawn([caps("1:22-23"), cp("1:24", to="said unto him,"), say("1:24", frm="Show us"), caps("1:25-26")], "JDG 1:22–26", lambda w, h: JA.ai("ai1", w, h, 116), "#F3D8A0",
              head="Beth-el")]
PG.extend(pack(SEGS, "JDG-C01-D", PG.next()))

C = "#FF8A3D"
DROVE = [("Manasseh", sp("1:27-28"), "JDG 1:27–28", "#B8B8E0", "They Drove Not Out the Canaanites"), ("Ephraim", v("1:29"), "JDG 1:29", "#B8B8E0", None),
         ("Zebulun", v("1:30"), "JDG 1:30", "#5AC8C8", None), ("Asher", sp("1:31-32"), "JDG 1:31–32", "#E8C88A", None),
         ("Naphtali", v("1:33"), "JDG 1:33", "#D8E4F0", None), ("Dan", sp("1:34-35"), "JDG 1:34–35", "#7AA8FF", None),
         ("The Amorites", v("1:36"), "JDG 1:36", C, None)]
PG.extend(roll_pages(DROVE, "JDG-C01-R", PG.next(), "Judges", "JDG", tag="THEY DROVE NOT OUT THE CANAANITES · JUDGES 1"))

SEGS2 = [drawn([cp("2:1", to="And he said,"), gd("2:1", frm="I made you"), gods("2:2-3")], "JDG 2:1–3", lambda w, h: K.bochim("bo1", w, h, 117), "#3A3450",
               head="Bochim", stamp=2),
         drawn([caps("2:4-5")], "JDG 2:4–5", lambda w, h: D4.weeping(w, h, 118), "#3A3450"),
         drawn([caps("2:6-10")], "JDG 2:6–10", lambda w, h: JA.three_graves(w, h, 119), "#3A2A4A", head="Another Generation"),
         drawn([caps("2:11-15")], "JDG 2:11–15", lambda w, h: K.baalim(w, h, 120), "#5A1A2A"),
         drawn([caps("2:16-19")], "JDG 2:16–19", NIGHTA, "#0B0B2A", head="Jehovah Raised Up Judges"),
         seg(None, "JDG 2:16–19", art=lambda w, h: K.cycle(w, h), bg=MAP, h=360),
         drawn([cp("2:20", to="and he said,"), gd("2:20", frm="Because"), gods("2:21-22"), caps("2:23")], "JDG 2:20–23", lambda w, h: K.baalim(w, h, 121), "#5A1A2A", head="That by Them I May Prove Israel")]
PG.extend(pack(SEGS2, "JDG-C01-E", PG.next(), end=end_mark("NEXT · DEBORAH", "right: 10px; bottom: 34px")))
