"""1 Samuel volume, Chapter 12 — Abigail (1 Samuel 25–26). Every verse, word for word from ref/asv.
Samuel's death; Nabal shearing in Carmel and his railing — Who is David?; Abigail's two hundred loaves and her ride down the
covert of the mountain; at David's feet — the soul of my lord shall be bound in the bundle of life; Blessed be thy discretion;
Nabal's heart died within him (25:38 words only); Abigail taken to wife. Then the hill of Hachilah: Saul asleep among the
wagons, the spear stuck in the ground at his head and the cruse of water; Destroy him not; David crying from the mountain top;
I have played the fool."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from deu import art4 as D4
from genesis import art as X
from jdg import art as JG
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_WEEP, DAVID, DAVID_BOLD, DAVID_GRIEVED, RED, COLD, GOLDEN)
from sa1 import ch11 as _prev

v, sp = G.v, G.span
NABAL = F("adam", skin="#C47A5A", shadow="#5A2A1E", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#8A6A2A", band=True, brow="scowl", light="#FF8A3D")
ABIGAIL = F("eve", skin="#D9A27A", shadow="#8A5A4A", hair="#1A1210", scarf="#E8B830", light="#FFE680")
SHEPHERD = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
ABISHAI = F("adam", skin="#C98E66", shadow="#5A2A1E", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", brow="scowl", light="#9AA8C8")
ABNER = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#5A5A2A", cord=True, light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1SA-C12-00-Title", "Chapter 12 · Abigail", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#E8B880"></rect><g transform="translate(0 360)">{K.abigail_gifts("t12", 760, 720, 1201)}</g>')
    return chapter_title(12, "第十二話", "Abigail", "1 Samuel 25 – 26", svg, "#E8B880", v("25:33", to="thou,"), "1 Samuel · Volume Nine")


SEGS = [drawn([caps("25:1")], "1SAM 25:1", lambda w, h: D4.weeping(w, h, 1211), "#3A3450", head="Samuel Died", stamp=25),
        drawn([caps("25:2-4")], "1SAM 25:2–4", lambda w, h: K.shearing("sh12", w, h, 1212), "#8FD0E2", head="Nabal"),
        face([cp("25:5", to="unto the young men,"), say("25:5", frm="Get you up"), ("say", v("25:6") + " " + v("25:7") + " " + v("25:8"))], "1SAM 25:5–8", DAVID),
        face([caps("25:9"), cp("25:10", to="and said,"), ("say", v("25:10", frm="Who is David?") + " " + v("25:11")), caps("25:12")], "1SAM 25:9–12", NABAL, bg=RED),
        face([cp("25:13", to="unto his men,"), say("25:13", frm="Gird ye", to="his sword."), cp("25:13", frm="And they girded")], "1SAM 25:13", DAVID_BOLD, bg=RED),
        face([cp("25:14", to="saying,"), ("say", v("25:14", frm="Behold,") + " " + sp("25:15-17"))], "1SAM 25:14–17", SHEPHERD, head="Abigail"),
        drawn([caps("25:18"), cp("25:19", to="unto her young men,"), say("25:19", frm="Go on", to="after you."), cp("25:19", frm="But she told not"), caps("25:20")], "1SAM 25:18–20",
              lambda w, h: K.abigail_gifts("ag12", w, h, 1213), "#E8B880"),
        face([cp("25:21", to="Now David had said,"), ("say", v("25:21", frm="Surely") + " " + v("25:22"))], "1SAM 25:21–22", DAVID_BOLD, bg=RED),
        drawn([caps("25:23"), cp("25:24", to="and said,"), say("25:24", frm="Upon me,")], "1SAM 25:23–24", lambda w, h: K.at_feet("af12", w, h, 1214), "#E8B880"),
        face([says("25:25-27")], "1SAM 25:25–27", ABIGAIL, head="The Bundle of Life"),
        face([says("25:28-31")], "1SAM 25:28–31", ABIGAIL),
        face([cp("25:32", to="to Abigail,"), ("say", v("25:32", frm="Blessed be") + " " + v("25:33") + " " + v("25:34")), cp("25:35", to="and he said unto her,"), say("25:35", frm="Go up")],
             "1SAM 25:32–35", DAVID),
        drawn([caps("25:36-38")], "1SAM 25:36–38", lambda w, h: K.empty_seat(w, h, 1215), "#5A2A3A"),
        face([cp("25:39", to="he said,"), say("25:39", frm="Blessed be Jehovah,", to="his own head."), cp("25:39", frm="And David sent"), cp("25:40", to="saying,"),
              say("25:40", frm="David hath sent")], "1SAM 25:39–40", DAVID, head="She Became His Wife"),
        face([cp("25:41", to="and said,"), say("25:41", frm="Behold,"), caps("25:42-44")], "1SAM 25:41–44", ABIGAIL),
        drawn([cp("26:1", to="saying,"), say("26:1", frm="Doth not"), caps("26:2-5")], "1SAM 26:1–5", lambda w, h: JG.dens(w, h, 1216), "#8A6A4A", head="The Hill of Hachilah", stamp=26),
        face([cp("26:6", to="saying,"), say("26:6", frm="Who will go", to="to the camp?"), cp("26:6", frm="And Abishai said,", to="And Abishai said,"), say("26:6", frm="I will go down")],
             "1SAM 26:6", DAVID),
        drawn([caps("26:7")], "1SAM 26:7", lambda w, h: K.saul_asleep("sa12", w, h, 1217), NIGHT),
        face([cp("26:8", to="to David,"), say("26:8", frm="God hath")], "1SAM 26:8", ABISHAI, bg=COLD, head="Destroy Him Not"),
        face([cp("26:9", to="to Abishai,"), say("26:9", frm="Destroy"), cp("26:10", to="And David said,"), ("say", v("26:10", frm="As Jehovah") + " " + v("26:11"))], "1SAM 26:9–11", DAVID, bg=COLD),
        drawn([caps("26:12")], "1SAM 26:12", lambda w, h: K.saul_asleep("sa12b", w, h, 1218, taken=True), NIGHT),
        drawn([caps("26:13"), cp("26:14", to="saying,"), say("26:14", frm="Answerest", to="Abner?"), cp("26:14", frm="Then Abner answered", to="and said,"), say("26:14", frm="Who art thou")],
              "1SAM 26:13–14", lambda w, h: K.hilltop_cry("hc12", w, h, 1219), "#2A2458", head="The King's Spear"),
        face([cp("26:15", to="to Abner,"), ("say", v("26:15", frm="Art not thou") + " " + v("26:16"))], "1SAM 26:15–16", DAVID_BOLD),
        face([cp("26:17", to="and said,"), say("26:17", frm="Is this thy voice,", to="my son David?"), cp("26:17", frm="And David said,", to="And David said,"), say("26:17", frm="It is my voice,")],
             "1SAM 26:17", SAUL_KING),
        face([cp("26:18", to="And he said,"), ("say", v("26:18", frm="Wherefore") + " " + v("26:19") + " " + v("26:20"))], "1SAM 26:18–20", DAVID),
        face([cp("26:21", to="Then said Saul,"), say("26:21", frm="I have sinned:")], "1SAM 26:21", SAUL_WEEP, bg=COLD, head="I Have Played the Fool"),
        face([cp("26:22", to="and said,"), ("say", v("26:22", frm="Behold the spear,") + " " + v("26:23") + " " + v("26:24"))], "1SAM 26:22–24", DAVID),
        face([cp("26:25", to="to David,"), say("26:25", frm="Blessed be thou,", to="surely prevail."), cp("26:25", frm="So David went")], "1SAM 26:25", SAUL_WEEP, bg=COLD)]
PG.extend(pack(SEGS, "1SA-C12-D", PG.next(), end=end_mark("NEXT · THE WITCH OF ENDOR", "right: 10px; bottom: 34px")))
