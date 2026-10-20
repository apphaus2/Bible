"""1 Samuel volume, Chapter 5 — To Obey Is Better (1 Samuel 11–13). Every verse, word for word from ref/eng-asv.
Nahash at Jabesh-gilead (11:2 words only); Saul following the oxen, the yoke cut in pieces and sent (words over the field);
deliverance by the time the sun is hot; the kingdom renewed at Gilgal; Samuel's farewell — Whose ox have I taken? — and
thunder and rain in wheat harvest; Jonathan smites the garrison at Geba; the Philistines as the sand; Saul's burnt-offering at
Gilgal — Thou hast done foolishly; a man after his own heart; and no smith in all the land of Israel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from jos import art as JA
from jdg import art as JG
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_MAD, SAMUEL_OLD, SAMUEL_GRIEVED, JONATHAN, ISRAELITE,
                        RED, COLD, GOLDEN)
from sa1 import ch04 as _prev

v, sp = G.v, G.span
NAHASH = F("adam", skin="#B98A6E", shadow="#4A1A26", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A2A3A", band=True, brow="scowl", light="#D7261E")
ELDER = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#6A5A3A", cord=True, brow="sorrow", sweat=True, light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("1SA-C05-00-Title", "Chapter 5 · To Obey Is Better", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A2E4A"></rect><g transform="translate(0 340)">{K.harvest_thunder(760, 740, 501)}</g>')
    return chapter_title(5, "第五話", "To Obey Is Better", "1 Samuel 11 – 13", svg, "#2A2E4A", v("13:14", frm="Jehovah hath sought him", to="after his own heart,"), "1 Samuel · Volume Nine")


SEGS = [face([cp("11:1", to="said unto Nahash,"), say("11:1", frm="Make a covenant"), cp("11:2", to="said unto them,"), say("11:2", frm="On this condition")], "1SAM 11:1–2", NAHASH, bg=RED,
             head="Jabesh-gilead", stamp=11),
        face([cp("11:3", to="said unto him,"), say("11:3", frm="Give us"), caps("11:4")], "1SAM 11:3–4", ELDER, bg=COLD),
        drawn([cp("11:5", to="and Saul said,"), say("11:5", frm="What aileth", to="weep?"), cp("11:5", frm="And they told him"), caps("11:6")], "1SAM 11:5–6", lambda w, h: K.oxen_field("ox5", w, h, 511), "#F3B86A"),
        drawn([cp("11:7", to="by the hand of messengers, saying,"), say("11:7", frm="Whosoever", to="unto his oxen."), cp("11:7", frm="And the dread"), caps("11:8")], "1SAM 11:7–8",
              lambda w, h: JG.borders(w, h), "#0B1A2E"),
        drawn([cp("11:9", to="that came,"), say("11:9", frm="Thus shall ye", to="have deliverance."), cp("11:9", frm="And the messengers"), cp("11:10", to="said,"), say("11:10", frm="To-morrow")],
              "1SAM 11:9–10", lambda w, h: JA.ai("jb5", w, h, 512), "#F3D8A0"),
        drawn([caps("11:11")], "1SAM 11:11", lambda w, h: JA.night_march("nm5", w, h, 513), "#0F0E2A"),
        face([cp("11:12", to="unto Samuel,"), say("11:12", frm="Who is he"), cp("11:13", to="And Saul said,"), say("11:13", frm="There shall not")], "1SAM 11:12–13", SAUL_KING),
        drawn([cp("11:14", to="to the people,"), say("11:14", frm="Come,"), caps("11:15")], "1SAM 11:14–15", lambda w, h: JA.gilgal("gl5", w, h, 514, people=True), "#F3D8A0"),
        face([cp("12:1", to="unto all Israel,"), ("say", v("12:1", frm="Behold,") + " " + sp("12:2-3"))], "1SAM 12:1–3", SAMUEL_OLD, head="Whose Ox Have I Taken?", stamp=12),
        face([cp("12:4", to="And they said,"), say("12:4", frm="Thou hast not"), cp("12:5", to="said unto them,"), say("12:5", frm="Jehovah is witness", to="in my hand."),
              cp("12:5", frm="And they said,", to="And they said,"), say("12:5", frm="He is witness.")], "1SAM 12:4–5", ISRAELITE),
        face([cp("12:6", to="unto the people,"), ("say", v("12:6", frm="It is Jehovah") + " " + sp("12:7-9"))], "1SAM 12:6–9", SAMUEL_OLD),
        face([says("12:10-13")], "1SAM 12:10–13", SAMUEL_GRIEVED, bg=COLD),
        face([says("12:14-17")], "1SAM 12:14–17", SAMUEL_OLD),
        drawn([caps("12:18"), cp("12:19", to="unto Samuel,"), say("12:19", frm="Pray for")], "1SAM 12:18–19", lambda w, h: K.harvest_thunder(w, h, 515), "#2A2E4A", head="Thunder and Rain"),
        face([cp("12:20", to="unto the people,"), ("say", v("12:20", frm="Fear not:") + " " + sp("12:21-25"))], "1SAM 12:20–25", SAMUEL_OLD),
        drawn([caps("13:1-2"), cp("13:3", to="saying,"), say("13:3", frm="Let the Hebrews"), caps("13:4")], "1SAM 13:1–4", lambda w, h: JA.armed("gb5", w, h, 516, tribes=("BENJAMIN",)), "#F3D8A0",
              head="Thou Hast Done Foolishly", stamp=13),
        drawn([caps("13:5-7")], "1SAM 13:5–7", lambda w, h: JA.chariots("ch5", w, h, 517), "#8FD0E2"),
        drawn([caps("13:8"), cp("13:9", to="And Saul said,"), say("13:9", frm="Bring hither", to="peace-offerings."), cp("13:9", frm="And he offered"), caps("13:10")], "1SAM 13:8–10",
              lambda w, h: JA.hewers("al5", w, h, 518), "#F3D8A0"),
        face([cp("13:11", to="And Samuel said,"), say("13:11", frm="What hast thou done?", to="What hast thou done?"), cp("13:11", frm="And Saul said,", to="And Saul said,"),
              ("say", v("13:11", frm="Because I saw") + " " + v("13:12"))], "1SAM 13:11–12", SAUL_MAD, bg=RED),
        face([cp("13:13", to="said to Saul,"), ("say", v("13:13", frm="Thou hast done") + " " + v("13:14"))], "1SAM 13:13–14", SAMUEL_GRIEVED, bg=COLD),
        drawn([caps("13:15-18")], "1SAM 13:15–18", lambda w, h: JG.midian(w, h, 519), "#E8B880", head="No Smith in Israel"),
        drawn([caps("13:19-23")], "1SAM 13:19–23", lambda w, h: K.no_smith(w, h, 520), "#3A2218")]
PG.extend(pack(SEGS, "1SA-C05-D", PG.next(), end=end_mark("NEXT · JONATHAN AT MICHMASH", "right: 10px; bottom: 34px")))
