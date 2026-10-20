"""2 Samuel volume, Chapter 11 — Jehovah Is My Rock (2 Samuel 21–22). Every verse, word for word from ref/eng-asv.
The famine for Saul's bloody house and the Gibeonites; 21:9 words over the mountain at barley harvest (no one drawn);
Rizpah on her sackcloth upon the rock; the bones of Saul and Jonathan buried in Zela; the four sons of the giant — thou
shalt go no more out with us, that thou quench not the lamp of Israel. Then David's song in song boxes over the waves of
death, the storm (God never drawn), the large place, the lamp, the hinds' feet on the high places."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, sg, sgs, says, caps, over, face, drawn, D, F, DAVID_OLD, DAVID_KING, MEPHIBOSHETH, RED, COLD, GOLDEN)
from sa2 import ch10 as _prev

v, sp = G.v, G.span
GIBEONITE = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#3A4A3A", cord=True, brow="scowl", light="#FF8A3D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2SA-C11-00-Title", "Chapter 11 · Jehovah Is My Rock", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{K.hinds("t11", 760, 780, 1101)}</g>')
    return chapter_title(11, "第十一話", "Jehovah Is My Rock", "2 Samuel 21 – 22", svg, "#4A7A9A", v("22:2", frm="Jehovah is my rock,"), "2 Samuel · Volume Ten")


SEGS = [drawn([cp("21:1", to="And Jehovah said,"), gd("21:1", frm="It is for Saul,")], "2SAM 21:1", lambda w, h: K.famine(w, h, 1102), "#FFF4C2", head="The Gibeonites", stamp=21),
        face([caps("21:2"), cp("21:3", to="unto the Gibeonites,"), say("21:3", frm="What shall I do")], "2SAM 21:2–3", DAVID_OLD),
        face([cp("21:4", to="said unto him,"), say("21:4", frm="It is no matter", to="in Israel."), cp("21:4", frm="And he said,", to="And he said,"), say("21:4", frm="What ye shall say,"),
              cp("21:5", to="unto the king,"), ("say", v("21:5", frm="The man") + " " + v("21:6", to="the chosen of Jehovah.")), cp("21:6", frm="And the king said,", to="And the king said,"),
              say("21:6", frm="I will give them.")], "2SAM 21:4–6", GIBEONITE, bg=RED),
        face([caps("21:7")], "2SAM 21:7", MEPHIBOSHETH, bg=COLD),
        drawn([caps("21:8-9")], "2SAM 21:8–9", lambda w, h: K.harvest_mount(w, h, 1103), "#C8B8A0"),
        drawn([caps("21:10")], "2SAM 21:10", lambda w, h: K.rizpah("rz11", w, h, 1104), "#5A4A5A", head="Rizpah"),
        drawn([caps("21:11-14")], "2SAM 21:11–14", lambda w, h: JA.cave(w, h, 1105, sealed=True, dusk=True), "#4A2A3A"),
        drawn([caps("21:15-16"), cp("21:17", to="saying,"), say("21:17", frm="Thou shalt go no more")], "2SAM 21:15–17", below(lambda w, h: K.giant("gt11", w, h, 1106), 0.3), "#E8B880",
              head="The Sons of the Giant"),
        drawn([caps("21:18-22")], "2SAM 21:18–22", below(lambda w, h: K.giant("gt11b", w, h, 1107, fallen=True), 0.3), "#E8B880"),
        face([caps("22:1"), cp("22:2", to="and he said,"), sg("22:2", frm="Jehovah is my rock,"), sg("22:3"), sg("22:4")], "2SAM 22:1–4", DAVID_OLD, head="Jehovah Is My Rock", stamp=22),
        drawn(sgs("22:5-7"), "2SAM 22:5–7", lambda w, h: K.waves(w, h, 1108), "#0B1A2E"),
        drawn(sgs("22:8-13"), "2SAM 22:8–13", lambda w, h: K.storm(w, h, 1109), "#0B0B2A"),
        drawn(sgs("22:14-16"), "2SAM 22:14–16", lambda w, h: K.storm(w, h, 1110, sea=True), "#0B0B2A"),
        drawn(sgs("22:17-20"), "2SAM 22:17–20", lambda w, h: K.large_place(w, h, 1111), "#8FD0E2"),
        face(sgs("22:21-25"), "2SAM 22:21–25", DAVID_KING),
        drawn(sgs("22:26-31"), "2SAM 22:26–31", lambda w, h: K.lamp(w, h, 1112), "#0B0B1A"),
        drawn(sgs("22:32-37"), "2SAM 22:32–37", below(lambda w, h: K.hinds("hd11", w, h, 1113), 0.5), "#8FD0E2"),
        drawn(sgs("22:38-43"), "2SAM 22:38–43", lambda w, h: JA.armed("ar11", w, h, 1114, tribes=()), "#F3D8A0"),
        drawn(sgs("22:44-46"), "2SAM 22:44–46", lambda w, h: K.wars_map(w, h, hi=("GATH", "MOAB", "RABBAH OF AMMON", "DAMASCUS", "ZOBAH", "HAMATH", "VALLEY OF SALT", "AMALEK")), MAP),
        face(sgs("22:47-51"), "2SAM 22:47–51", DAVID_OLD)]
PG.extend(pack(SEGS, "2SA-C11-D", PG.next(), end=end_mark("NEXT · WHICH COST ME NOTHING", "right: 10px; bottom: 34px")))
