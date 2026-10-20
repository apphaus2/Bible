"""Joshua volume, Chapter 7 — The Lot of Judah (Joshua 15–17). Every verse, word for word from ref/eng-asv.
The border of Judah round about and every city of Judah as roll cells (one cell per group of cities, as the verses count
them: "twenty and nine cities, with their villages"); between them Caleb at Hebron, Othniel and Achsah, and the upper and
nether springs; the lot of Joseph: Ephraim's border, Manasseh's, the daughters of Zelophehad before Eleazar and Joshua; and
the children of Joseph who are a great people: the forest and the chariots of iron."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages, verse_cells
from deu.common import shade
from genesis.ch04 import COLD
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, CALEB_OLD, ACHSAH, JOSEPHITE
from jos import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
JU, EP, MA, X = "#5AD87A", "#B8B8E0", "#9A9AD0", "#8FD0E2"
CODE = "JOSH"
def roll(items, prefix, tag): PG.extend(roll_pages(items, prefix, PG.next(), "Joshua", CODE, tag=tag))


@P("JOS-C07-00-Title", "Chapter 7 · The Lot of Judah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect><g transform="translate(0 380)">{K.springs("t7", 760, 700, 701)}</g>')
    return chapter_title(7, "第七話", "The Lot of Judah", "Joshua 15 – 17", svg, "#F3D8A0", v("15:19", frm="And he gave her"), "Joshua · Volume Six")


roll([("The South Border", sp("15:1-4"), "JOSH 15:1–4", JU, "The Border of Judah"),
      ("The East and North Border", sp("15:5-11"), "JOSH 15:5–11", JU, None),
      ("The West Border", v("15:12"), "JOSH 15:12", JU, None)], "JOS-C07-B", "THE LOT OF JUDAH · JOSHUA 15")

SEGS = [drawn([caps("15:13-15"), cp("15:16", to="And Caleb said,"), say("15:16", frm="He that smiteth")], "JOSH 15:13–16", lambda w, h: K.hebron("hb7", w, h, 711), "#F3D8A0",
              head="Give Me Also Springs of Water"),
        face([caps("15:17"), cp("15:18", to="and Caleb said,"), say("15:18", frm="What wouldest")], "JOSH 15:17–18", CALEB_OLD),
        face([cp("15:19", to="And she said,"), say("15:19", frm="Give me", to="springs of water."), cp("15:19", frm="And he gave her")], "JOSH 15:19", ACHSAH),
        drawn([caps("15:20")], "JOSH 15:20", lambda w, h: K.springs("sp7", w, h, 712), "#F3D8A0")]
PG.extend(pack(SEGS, "JOS-C07-D", PG.next()))

REGION = {21: "In the South", 33: "In the Lowland", 48: "In the Hill-country", 61: "In the Wilderness"}
def region(k): return max((v_, n) for v_, n in REGION.items() if v_ <= k)[1]
roll(verse_cells(G, CODE, 15, 21, 62, region, JU, head="The Cities of Judah", budget=420, brk=r"villages\.$|border thereof\.$")
     + [("Jerusalem", v("15:63"), "JOSH 15:63", "#FF8A3D", None)], "JOS-C07-C", "THE CITIES OF JUDAH · JOSHUA 15")

roll([("The Children of Joseph", sp("16:1-4"), "JOSH 16:1–4", EP, "The Lot of Joseph"),
      ("Ephraim", sp("16:5-8"), "JOSH 16:5–8", EP, None),
      ("Ephraim", sp("16:9-10"), "JOSH 16:9–10", EP, None),
      ("Manasseh", sp("17:1-2"), "JOSH 17:1–2", MA, None)], "JOS-C07-J", "THE LOT OF JOSEPH · JOSHUA 16–17")

SEGS2 = [drawn([caps("17:3"), cp("17:4", to="saying,"), say("17:4", frm="Jehovah commanded", to="among our brethren:"), cp("17:4", frm="therefore according")], "JOSH 17:3–4",
               lambda w, h: K.daughters("dz7", w, h, 713), "#E8C8A0", head="The Daughters of Zelophehad"),
         drawn([caps("17:5-6")], "JOSH 17:5–6", lambda w, h: K.daughters("dz7b", w, h, 714), "#E8C8A0")]
PG.extend(pack(SEGS2, "JOS-C07-E", PG.next()))

roll([("The Border of Manasseh", sp("17:7-10"), "JOSH 17:7–10", MA, "The Border of Manasseh"),
      ("In Issachar and in Asher", sp("17:11-13"), "JOSH 17:11–13", MA, None)], "JOS-C07-M", "THE LOT OF MANASSEH · JOSHUA 17")

SEGS3 = [face([cp("17:14", to="saying,"), say("17:14", frm="Why hast")], "JOSH 17:14", JOSEPHITE, head="Thou Art a Great People"),
         face([cp("17:15", to="said unto them,"), say("17:15", frm="If thou be")], "JOSH 17:15", "calm"),
         drawn([cp("17:16", to="said,"), say("17:16", frm="The hill-country")], "JOSH 17:16", lambda w, h: K.forest("fo7", w, h, 715), "#8FD0E2"),
         face([cp("17:17", to="saying,"), ("say", v("17:17", frm="Thou art") + " " + v("17:18"))], "JOSH 17:17–18", "lead")]
PG.extend(pack(SEGS3, "JOS-C07-F", PG.next(), end=end_mark("NEXT · THE LOTS OF THE SEVEN TRIBES", "right: 10px; bottom: 34px")))
