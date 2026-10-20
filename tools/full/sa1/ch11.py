"""1 Samuel volume, Chapter 11 — The Cave (1 Samuel 22–24). Every verse, word for word from ref/eng-asv.
The cave of Adullam and the four hundred; Saul under the tamarisk with his spear; Doeg the Edomite's report; Ahimelech's
answer; the priests of Nob (22:17–19 words over the smoke of Nob: nothing drawn); Abiathar escaped; Keilah and the ephod;
Jonathan in the wood of Ziph — thou shalt be king over Israel; the Ziphites; this side and that side of the mountain in Maon;
then the cave at En-gedi and the skirt of Saul's robe (the digest's panels) — Is this thy voice, my son David?"""
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
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_MAD, SAUL_WEEP, DAVID, DAVID_BOLD, DAVID_GRIEVED, JONATHAN,
                        RED, COLD, GOLDEN)
from sa1 import ch10 as _prev

v, sp = G.v, G.span
DOEG = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#3A1A10", hl="#5A3A2E", beard=True, beard_color="#3A1A10", scarf="#7A3A1A", cord=True, brow="scowl", light="#D7261E")
AHIMELECH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#C8C2B6", hl="#8A867E", beard=True, beard_color="#C8C2B6", scarf="#F3EFE6", band=True, light="#FFE680")
GAD = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#6A6460", hl="#8A867E", beard=True, beard_color="#6A6460", scarf="#5A6A3A", cord=True, light="#FFE680")
ZIPHITE = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#8A6A3A", cord=True, light="#FFC14D")
MAN = F("adam", skin="#B9785A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", light="#FF8A3D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("1SA-C11-00-Title", "Chapter 11 · The Cave", title=True)
def title(n):
    bg, art = D("B9", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#1A1412"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(11, "第十一話", "The Cave", "1 Samuel 22 – 24", svg, "#1A1412", v("24:6", frm="Jehovah forbid", to="Jehovah's anointed,"), "1 Samuel · Volume Nine")


SEGS = [drawn([caps("22:1-2")], "1SAM 22:1–2", lambda w, h: K.adullam("ad11", w, h, 1111), "#1A1412", head="The Cave of Adullam", stamp=22),
        face([cp("22:3", to="unto the king of Moab,"), say("22:3", frm="Let my father"), caps("22:4"), cp("22:5", to="unto David,"), say("22:5", frm="Abide not", to="land of Judah."),
              cp("22:5", frm="Then David departed,")], "1SAM 22:3–5", GAD),
        drawn([caps("22:6"), cp("22:7", to="stood about him,"), ("say", v("22:7", frm="Hear now,") + " " + v("22:8"))], "1SAM 22:6–8", lambda w, h: K.tamarisk("tm11", w, h, 1112), "#E8C88A",
              head="Doeg the Edomite"),
        face([cp("22:9", to="and said,"), ("say", v("22:9", frm="I saw") + " " + v("22:10"))], "1SAM 22:9–10", DOEG, bg=RED),
        face([caps("22:11"), cp("22:12", to="And Saul said,"), say("22:12", frm="Hear now,", to="son of Ahitub."), cp("22:12", frm="And he answered,", to="And he answered,"),
              say("22:12", frm="Here I am,"), cp("22:13", to="said unto him,"), say("22:13", frm="Why have ye")], "1SAM 22:11–13", SAUL_MAD, bg=RED),
        face([cp("22:14", to="and said,"), ("say", v("22:14", frm="And who") + " " + v("22:15"))], "1SAM 22:14–15", AHIMELECH),
        drawn([cp("22:16", to="And the king said,"), say("22:16", frm="Thou shalt"), cp("22:17", to="stood about him,"), say("22:17", frm="Turn,", to="disclose it to me."),
               cp("22:17", frm="But the servants"), cp("22:18", to="said to Doeg,"), say("22:18", frm="Turn thou,", to="the priests."), cp("22:18", frm="And Doeg"), caps("22:19")],
              "1SAM 22:16–19", lambda w, h: K.nob_smoke(w, h, 1113), "#2A0A0A"),
        face([caps("22:20-21"), cp("22:22", to="unto Abiathar,"), ("say", v("22:22", frm="I knew") + " " + v("22:23"))], "1SAM 22:20–23", DAVID_GRIEVED, bg=COLD),
        drawn([cp("23:1", to="saying,"), say("23:1", frm="Behold,"), cp("23:2", to="saying,"), say("23:2", frm="Shall I go", to="Philistines?"), cp("23:2", frm="And Jehovah said", to="unto David,"),
               gd("23:2", frm="Go,")], "1SAM 23:1–2", lambda w, h: K.ephod_inquire("ei11", w, h, 1114), "#2A1A3A", head="Keilah", stamp=23),
        face([cp("23:3", to="said unto him,"), say("23:3", frm="Behold,"), cp("23:4", to="and said,"), gd("23:4", frm="Arise,"), caps("23:5-6")], "1SAM 23:3–6", MAN),
        face([cp("23:7", to="And Saul said,"), say("23:7", frm="God hath"), caps("23:8")], "1SAM 23:7–8", SAUL_KING),
        drawn([cp("23:9", to="the priest,"), say("23:9", frm="Bring hither"), cp("23:10", to="Then said David,"), ("say", v("23:10", frm="O Jehovah,") + " " + v("23:11", to="tell thy servant.")),
               cp("23:11", frm="And Jehovah said,", to="And Jehovah said,"), gd("23:11", frm="He will come down."), cp("23:12", to="Then said David,"), say("23:12", frm="Will the men", to="hand of Saul?"),
               cp("23:12", frm="And Jehovah said,", to="And Jehovah said,"), gd("23:12", frm="They will")], "1SAM 23:9–12", lambda w, h: K.ephod_inquire("ei11b", w, h, 1115), "#2A1A3A"),
        drawn([caps("23:13-15")], "1SAM 23:13–15", lambda w, h: JG.dens(w, h, 1116), "#8A6A4A", head="The Wilderness of Ziph"),
        face([caps("23:16"), cp("23:17", to="said unto him,"), say("23:17", frm="Fear not;"), caps("23:18")], "1SAM 23:16–18", JONATHAN),
        face([cp("23:19", to="saying,"), ("say", v("23:19", frm="Doth not") + " " + v("23:20"))], "1SAM 23:19–20", ZIPHITE),
        face([cp("23:21", to="And Saul said,"), ("say", v("23:21", frm="Blessed be") + " " + sp("23:22-23"))], "1SAM 23:21–23", SAUL_KING),
        drawn([caps("23:24-26")], "1SAM 23:24–26", lambda w, h: K.maon("mn11", w, h, 1117), "#E8B880"),
        drawn([cp("23:27", to="saying,"), say("23:27", frm="Haste thee,"), caps("23:28-29")], "1SAM 23:27–29", lambda w, h: K.maon("mn11b", w, h, 1118), "#E8B880"),
        drawn([cp("24:1", to="saying,"), say("24:1", frm="Behold,"), caps("24:2-3")], "1SAM 24:1–3", lambda w, h: K.engedi_cave("ec11", w, h, 1119), "#1A1412", head="En-gedi", stamp=24),
        over([cp("24:4", to="said unto him,"), say("24:4", frm="Behold, the day", to="good unto thee."), cp("24:4", frm="Then David arose,")], "1SAM 24:4", "B9", 0),
        face([caps("24:5"), cp("24:6", to="unto his men,"), say("24:6", frm="Jehovah forbid")], "1SAM 24:5–6", DAVID_GRIEVED, bg=COLD),
        drawn([caps("24:7"), cp("24:8", to="saying,"), say("24:8", frm="My lord the king.", to="My lord the king."), cp("24:8", frm="And when Saul")], "1SAM 24:7–8", D("B9", 3)[1], D("B9", 3)[0],
              head="Is This Thy Voice, My Son David?"),
        face([cp("24:9", to="to Saul,"), ("say", v("24:9", frm="Wherefore") + " " + sp("24:10-11"))], "1SAM 24:9–11", DAVID),
        face([says("24:12-15")], "1SAM 24:12–15", DAVID_BOLD),
        face([cp("24:16", to="that Saul said,"), say("24:16", frm="Is this thy voice,", to="my son David?"), cp("24:16", frm="And Saul lifted"), cp("24:17", to="to David,"),
              ("say", v("24:17", frm="Thou art more") + " " + sp("24:18-21")), caps("24:22")], "1SAM 24:16–22", SAUL_WEEP, bg=COLD)]
PG.extend(pack(SEGS, "1SA-C11-D", PG.next(), end=end_mark("NEXT · ABIGAIL", "right: 10px; bottom: 34px")))
