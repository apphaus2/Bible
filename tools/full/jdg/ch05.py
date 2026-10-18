"""Judges volume, Chapter 5 — Jephthah (Judges 10–12). Every verse, word for word from ref/asv.
Tola and Jair; Israel sold to the Philistines and Ammon, Go and cry unto the gods which ye have chosen; Jephthah the
Gileadite fetched out of the land of Tob; his message to the king of Ammon over the map of the way round Edom and Moab; the
vow; his daughter at the door with timbrels; two months upon the mountains (11:39 is words over the mountains: nothing of
the vow's end drawn); Shibboleth at the fords of the Jordan; and Ibzan, Elon and Abdon."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from deu import art as DA
from genesis import art as X
from jos import art as JA
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, face, drawn, ISRAELITE, RED, COLD, GOLDEN
from jdg.common import F
from jdg import ch04 as _prev

v, sp = G.v, G.span
JEPHTHAH = F("adam", skin="#B98A6E", shadow="#4A2A1A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#4A5A2A", cord=True, brow="scowl", light="#FF8A3D")
JEPHTHAH_GRIEF = F("adam", skin="#B98A7E", shadow="#3A3A5A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#4A5A2A", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
DAUGHTER = F("eve", skin="#D9A27A", shadow="#8A5A4A", hair="#1A1210", light="#FFE680")
ELDER = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#6A5A3A", cord=True, light="#FFC14D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)
MAP = "#0B1A2E"
J = "#FFD23F"


@P("JDG-C05-00-Title", "Chapter 5 · Jephthah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A6E8A"></rect><g transform="translate(0 340)">{K.mountains_women("t5", 760, 740, 501)}</g>')
    return chapter_title(5, "第五話", "Jephthah", "Judges 10 – 12", svg, "#5A6E8A", v("11:35", frm="I have opened my mouth", to="I cannot go back."), "Judges · Volume Seven")


SEGS = [drawn([caps("10:1-5")], "JDG 10:1–5", lambda w, h: K.ass_colts("ac5", w, h, 510), "#F3D8A0", head="Tola and Jair"),
        drawn([caps("10:6-9")], "JDG 10:6–9", lambda w, h: K.baalim(w, h, 511), "#5A1A2A", head="Go and Cry unto the Gods Which Ye Have Chosen", stamp=10),
        drawn([cp("10:10", to="saying,"), say("10:10", frm="We have sinned"), cp("10:11", to="children of Israel,"), gd("10:11", frm="Did not I"), gods("10:12-14")], "JDG 10:10–14",
              NIGHTA, "#0B0B2A"),
        drawn([cp("10:15", to="unto Jehovah,"), say("10:15", frm="We have sinned:"), caps("10:16-17"), cp("10:18", to="one to another,"), say("10:18", frm="What man")], "JDG 10:15–18",
              lambda w, h: JA.armed("ar5", w, h, 512, tribes=("GAD", "MANASSEH")), "#F3D8A0"),
        face([caps("11:1"), cp("11:2", to="and said unto him,"), say("11:2", frm="Thou shalt not"), caps("11:3-5")], "JDG 11:1–5", JEPHTHAH, bg=RED, head="Jephthah the Gileadite", stamp=11),
        face([cp("11:6", to="unto Jephthah,"), say("11:6", frm="Come and be")], "JDG 11:6", ELDER),
        face([cp("11:7", to="elders of Gilead,"), say("11:7", frm="Did not ye")], "JDG 11:7", JEPHTHAH, bg=RED),
        face([cp("11:8", to="unto Jephthah,"), say("11:8", frm="Therefore")], "JDG 11:8", ELDER),
        face([cp("11:9", to="elders of Gilead,"), say("11:9", frm="If ye bring"), cp("11:10", to="unto Jephthah,"), say("11:10", frm="Jehovah shall"), caps("11:11")], "JDG 11:9–11", JEPHTHAH),
        drawn([cp("11:12", to="saying,"), say("11:12", frm="What hast"), cp("11:13", to="messengers of Jephthah,"), say("11:13", frm="Because Israel"), caps("11:14")], "JDG 11:12–14",
              lambda w, h: K.tribute("tr5", w, h, 513), "#6A2A3A", head="Thus Saith Jephthah"),
        drawn([cp("11:15", to="Thus saith Jephthah:"), ("say", v("11:15", frm="Israel took") + " " + sp("11:16-18"))], "JDG 11:15–18", JA.below(lambda w, h: DA.map_moab(w, h), 0.5), MAP),
        drawn([says("11:19-22")], "JDG 11:19–22", JA.below(lambda w, h: DA.map_moab(w, h, hi=("SIHON",)), 0.5), MAP),
        face([says("11:23-27")], "JDG 11:23–27", JEPHTHAH),
        drawn([caps("11:28-29"), cp("11:30", to="and said,"), ("say", v("11:30", frm="If thou") + " " + v("11:31"))], "JDG 11:28–31", NIGHTA, "#0B0B2A", head="The Vow"),
        drawn([caps("11:32-33")], "JDG 11:32–33", lambda w, h: JA.burning(w, h, 514, city="aroer"), "#2A0A0A"),
        drawn([caps("11:34")], "JDG 11:34", lambda w, h: K.daughter_door("dd5", w, h, 515), "#F3B86A", head="His Daughter Came Out to Meet Him"),
        face([cp("11:35", to="and said,"), say("11:35", frm="Alas,")], "JDG 11:35", JEPHTHAH_GRIEF, bg=COLD),
        face([cp("11:36", to="said unto him,"), say("11:36", frm="My father,"), cp("11:37", to="unto her father,"), say("11:37", frm="Let this thing")], "JDG 11:36–37", DAUGHTER, bg=COLD),
        drawn([cp("11:38", to="And he said,"), say("11:38", frm="Go.", to="Go."), cp("11:38", frm="And he sent"), caps("11:39-40")], "JDG 11:38–40",
              lambda w, h: K.mountains_women("mw5", w, h, 516), "#5A6E8A"),
        face([cp("12:1", to="said unto Jephthah,"), say("12:1", frm="Wherefore")], "JDG 12:1", ISRAELITE, bg=RED, head="Shibboleth", stamp=12),
        face([cp("12:2", to="said unto them,"), ("say", v("12:2", frm="I and my") + " " + v("12:3"))], "JDG 12:2–3", JEPHTHAH),
        drawn([cp("12:4", to="because they said,"), say("12:4", frm="Ye are fugitives"), cp("12:5", to="said unto him,", ), say("12:5", frm="Art thou", to="an Ephraimite?"),
               cp("12:5", frm="If he said,", to="If he said,"), say("12:5", frm="Nay;")], "JDG 12:4–5", lambda w, h: K.fords("fo5", w, h, 517), "#E8C88A"),
        drawn([cp("12:6", to="then said they unto him,"), say("12:6", frm="Say now", to="Shibboleth;"), cp("12:6", frm="and he said", to="and he said"), say("12:6", frm="Sibboleth;", to="Sibboleth;"),
               cp("12:6", frm="for he could"), caps("12:7")], "JDG 12:6–7", lambda w, h: K.fords("fo5b", w, h, 518), "#E8C88A")]
SEGS += [drawn([caps("12:8-15")], "JDG 12:8–15", lambda w, h: K.ass_colts("ac5b", w, h, 519, n=8), "#F3D8A0", head="Ibzan, Elon and Abdon")]
PG.extend(pack(SEGS, "JDG-C05-D", PG.next(), end=end_mark("NEXT · SAMSON", "right: 10px; bottom: 34px")))
