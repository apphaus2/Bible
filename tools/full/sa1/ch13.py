"""1 Samuel volume, Chapter 13 — The Witch of En-dor (1 Samuel 27–29). Every verse, word for word from ref/eng-asv.
David among the Philistines: Achish gives him Ziklag; the raids (27:9, 27:11 words over the dens of the south); Achish's
trust. Then Saul before Shunem and Gilboa, Jehovah answering him not; the woman with a familiar spirit at En-dor by night;
an old man covered with a robe rising out of the earth (a pale shape, no face); to-morrow shalt thou and thy sons be with
me; the fatted calf and the bread; and the princes of the Philistines sending David back from Aphek."""
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
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_MAD, SAUL_WEEP, SAMUEL_GRIEVED, DAVID, DAVID_BOLD, PHILISTINE,
                        RED, COLD, GOLDEN)
from sa1 import ch12 as _prev

v, sp = G.v, G.span
ACHISH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#1F5FAD", band=True, light="#FFC14D")
WITCH = F("eve", skin="#B98A7E", shadow="#3A2A4A", hair="#6A6460", scarf="#3A2A4A", brow="sorrow", sweat=True, light="#9AA8C8")
SERVANT = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", light="#9AA8C8")
SAMUEL_SHADE = F("adam", skin="#C8D0E8", shadow="#6A6A9A", hair="#E8ECF8", hl="#B8C0D8", beard=True, beard_color="#E8ECF8", scarf="#B8C0E0", light="#E8ECF8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#1A1420"


@P("1SA-C13-00-Title", "Chapter 13 · The Witch of En-dor", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#1A1420"></rect><g transform="translate(0 340)">{K.endor("t13", 760, 740, 1301)}</g>')
    return chapter_title(13, "第十三話", "The Witch of En-dor", "1 Samuel 27 – 29", svg, "#1A1420", v("28:14", frm="An old man cometh up;", to="covered with a robe."), "1 Samuel · Volume Nine")


SEGS = [face([cp("27:1", to="in his heart,"), say("27:1", frm="I shall now perish")], "1SAM 27:1", DAVID, bg=COLD, head="Ziklag", stamp=27),
        face([caps("27:2-4"), cp("27:5", to="unto Achish,"), say("27:5", frm="If now"), caps("27:6-7")], "1SAM 27:2–7", ACHISH),
        drawn([caps("27:8-9")], "1SAM 27:8–9", lambda w, h: JG.dens(w, h, 1311), "#8A6A4A"),
        face([cp("27:10", to="And Achish said,"), say("27:10", frm="Against whom", to="to-day?"), cp("27:10", frm="And David said,", to="And David said,"), say("27:10", frm="Against the South"),
              cp("27:11", to="saying,"), say("27:11", frm="Lest they", to="So did David,"), cp("27:11", frm="and so hath been"), cp("27:12", to="saying,"), say("27:12", frm="He hath made")],
             "1SAM 27:10–12", ACHISH),
        face([cp("28:1", to="And Achish said unto David,"), say("28:1", frm="Know thou"), cp("28:2", to="to Achish,"), say("28:2", frm="Therefore thou", to="will do."),
              cp("28:2", frm="And Achish said to David,", to="said to David,"), say("28:2", frm="Therefore will I")], "1SAM 28:1–2", ACHISH, head="Saul Inquired of Jehovah", stamp=28),
        drawn([caps("28:3-6")], "1SAM 28:3–6", lambda w, h: JA.chariots("sh13", w, h, 1312), "#8FD0E2"),
        face([cp("28:7", to="unto his servants,"), say("28:7", frm="Seek me", to="inquire of her."), cp("28:7", frm="And his servants said", to="said to him,"), say("28:7", frm="Behold, there is")],
             "1SAM 28:7", SAUL_MAD, bg=COLD),
        drawn([cp("28:8", to="and he said,"), say("28:8", frm="Divine unto me,")], "1SAM 28:8", lambda w, h: K.endor("en13", w, h, 1313, rising=False), NIGHT, head="En-dor"),
        face([cp("28:9", to="said unto him,"), say("28:9", frm="Behold, thou knowest"), cp("28:10", to="saying,"), say("28:10", frm="As Jehovah liveth,")], "1SAM 28:9–10", WITCH, bg=COLD),
        face([cp("28:11", to="Then said the woman,"), say("28:11", frm="Whom shall", to="unto thee?"), cp("28:11", frm="And he said,", to="And he said,"), say("28:11", frm="Bring me up Samuel."),
              cp("28:12", to="saying,"), say("28:12", frm="Why hast thou")], "1SAM 28:11–12", WITCH, bg=COLD),
        drawn([cp("28:13", to="And the king said unto her,"), say("28:13", frm="Be not afraid:", to="what seest thou?"), cp("28:13", frm="And the woman said unto Saul,", to="unto Saul,"),
               say("28:13", frm="I see a god"), cp("28:14", to="And he said unto her,"), say("28:14", frm="What form", to="of?"), cp("28:14", frm="And she said,", to="And she said,"),
               say("28:14", frm="An old man", to="with a robe."), cp("28:14", frm="And Saul perceived")], "1SAM 28:13–14", lambda w, h: K.endor("en13b", w, h, 1314), NIGHT),
        face([cp("28:15", to="said to Saul,"), say("28:15", frm="Why hast thou disquieted", to="to bring me up?")], "1SAM 28:15", SAMUEL_SHADE, bg="#2A2A4A", head="To-morrow Shalt Thou Be with Me"),
        face([cp("28:15", frm="And Saul answered,", to="And Saul answered,"), say("28:15", frm="I am sore distressed;")], "1SAM 28:15", SAUL_WEEP, bg=COLD),
        face([cp("28:16", to="And Samuel said,"), ("say", v("28:16", frm="Wherefore") + " " + sp("28:17-19"))], "1SAM 28:16–19", SAMUEL_SHADE, bg="#2A2A4A"),
        face([caps("28:20"), cp("28:21", to="and said unto him,"), ("say", v("28:21", frm="Behold,") + " " + v("28:22"))], "1SAM 28:20–22", WITCH, bg=COLD),
        drawn([cp("28:23", to="and said,"), say("28:23", frm="I will not eat.", to="I will not eat."), cp("28:23", frm="But his servants,"), caps("28:24-25")], "1SAM 28:23–25", lambda w, h: K.unleavened(w, h, 1315), "#2A1A18"),
        drawn([caps("29:1-2"), cp("29:3", to="Then said the princes of the Philistines,"), say("29:3", frm="What do these", to="Hebrews here?"),
               cp("29:3", frm="And Achish said", to="the Philistines,"), say("29:3", frm="Is not this David,")], "1SAM 29:1–3", lambda w, h: JA.armed("ap13", w, h, 1316, tribes=()), "#F3D8A0",
              head="Make the Man Return", stamp=29),
        face([cp("29:4", to="said unto him,"), ("say", v("29:4", frm="Make the man") + " " + v("29:5"))], "1SAM 29:4–5", PHILISTINE, bg=RED),
        face([cp("29:6", to="and said unto him,"), ("say", v("29:6", frm="As Jehovah") + " " + v("29:7"))], "1SAM 29:6–7", ACHISH),
        face([cp("29:8", to="unto Achish,"), say("29:8", frm="But what have I")], "1SAM 29:8", DAVID),
        face([cp("29:9", to="said to David,"), ("say", v("29:9", frm="I know") + " " + v("29:10")), caps("29:11")], "1SAM 29:9–11", ACHISH)]
PG.extend(pack(SEGS, "1SA-C13-D", PG.next(), end=end_mark("NEXT · MOUNT GILBOA", "right: 10px; bottom: 34px")))
