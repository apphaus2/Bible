"""2 Samuel volume, Chapter 8 — The Mount of Olives (2 Samuel 15–16). Every verse, word for word from ref/asv.
Absalom's chariot and fifty runners; beside the way of the gate — oh that I were made judge in the land; so Absalom stole the
hearts of the men of Israel; Absalom is king in Hebron; arise, and let us flee; Ittai the Gittite — whether for death or for
life; the brook Kidron and the ark carried back; the ascent of the mount of Olives, weeping, barefoot (the digest's panels);
Hushai sent back; Ziba's asses; Shimei cursing and casting stones; Long live the king; Ahithophel's counsel (16:22 words
over a tent on the roof)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, cp, says, caps, over, face, drawn, D, F, DAVID_OLD, DAVID_OLD_ALARM, DAVID_OLD_WEEP, ABSALOM, ABSALOM_SLY, ABISHAI, MESSENGER,
                        RED, COLD, GOLDEN)
from sa2 import ch07 as _prev

v, sp = G.v, G.span
ITTAI = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#1F5FAD", band=True, light="#FFC14D")
HUSHAI = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#7A6A5A", brow="sorrow", light="#9AA8C8")
AHITHOPHEL = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#2A2A4A", cord=True, brow="scowl", light="#FF8A3D")
ZIBA = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#7A5A3A", cord=True, light="#FFC14D")
SHIMEI = F("adam", skin="#C47A5A", shadow="#5A2A1E", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2SA-C08-00-Title", "Chapter 8 · The Mount of Olives", title=True)
def title(n):
    bg, art = D("B4", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A4A"></rect><g transform="translate(0 280)">{art(760, 800)}</g>')
    return chapter_title(8, "第八話", "The Mount of Olives", "2 Samuel 15 – 16", svg, "#2A2A4A", v("15:30", to="wept as he went up;"), "2 Samuel · Volume Ten")


SEGS = [drawn([caps("15:1")], "2SAM 15:1", lambda w, h: K.chariot_runners("cr8", w, h, 801), "#FFE680", head="He Stole the Hearts", stamp=15),
        over([cp("15:2", to="and said,"), say("15:2", frm="Of what city", to="art thou?"), cp("15:2", frm="And he said,", to="And he said,"), say("15:2", frm="Thy servant is")], "2SAM 15:2", "B2", 0),
        over([cp("15:3", to="said unto him,"), say("15:3", frm="See,"), cp("15:4", to="said moreover,"), say("15:4", frm="Oh that")], "2SAM 15:3–4", "B2", 1),
        over([caps("15:5-6")], "2SAM 15:5–6", "B2", 2),
        face([cp("15:7", to="unto the king,"), ("say", v("15:7", frm="I pray thee,") + " " + v("15:8")), cp("15:9", to="said unto him,"), say("15:9", frm="Go in peace.", to="Go in peace."),
              cp("15:9", frm="So he arose")], "2SAM 15:7–9", ABSALOM_SLY),
        over([cp("15:10", to="saying,"), say("15:10", frm="As soon as"), caps("15:11")], "2SAM 15:10–11", "B3", 0, head="Absalom Is King in Hebron"),
        face([caps("15:12")], "2SAM 15:12", AHITHOPHEL),
        face([cp("15:13", to="saying,"), say("15:13", frm="The hearts"), cp("15:14", to="at Jerusalem,"), say("15:14", frm="Arise,")], "2SAM 15:13–14", DAVID_OLD_ALARM, bg=RED),
        drawn([cp("15:15", to="unto the king,"), say("15:15", frm="Behold,"), caps("15:16-17")], "2SAM 15:15–17", below(lambda w, h: K.gate_out("go8", w, h, 802), 0.3), "#C8B8C8"),
        drawn([caps("15:18")], "2SAM 15:18", lambda w, h: K.march_by("mb8", w, h, 803), "#E8C8A0"),
        face([cp("15:19", to="to Ittai the Gittite,"), ("say", v("15:19", frm="Wherefore") + " " + v("15:20"))], "2SAM 15:19–20", DAVID_OLD, head="Ittai the Gittite"),
        face([cp("15:21", to="and said,"), say("15:21", frm="As Jehovah liveth,"), cp("15:22", to="to Ittai,"), say("15:22", frm="Go and pass over.", to="Go and pass over."),
              cp("15:22", frm="And Ittai the Gittite")], "2SAM 15:21–22", ITTAI),
        over([caps("15:23")], "2SAM 15:23", "B4", 0, head="The Brook Kidron"),
        drawn([caps("15:24")], "2SAM 15:24", lambda w, h: K.ark_kidron("ak8", w, h, 804), "#8A9AB8"),
        face([cp("15:25", to="unto Zadok,"), ("say", v("15:25", frm="Carry back") + " " + v("15:26"))], "2SAM 15:25–26", DAVID_OLD),
        face([cp("15:27", to="the priest,"), ("say", v("15:27", frm="Art thou not") + " " + v("15:28")), caps("15:29")], "2SAM 15:27–29", DAVID_OLD),
        over([caps("15:30")], "2SAM 15:30", "B4", 1, head="The Ascent of the Mount of Olives"),
        face([cp("15:31", to="saying,"), say("15:31", frm="Ahithophel is", to="with Absalom."), cp("15:31", frm="And David said,", to="And David said,"), say("15:31", frm="O Jehovah,")],
             "2SAM 15:31", DAVID_OLD_WEEP, bg=COLD),
        face([caps("15:32")], "2SAM 15:32", HUSHAI, bg=COLD),
        face([cp("15:33", to="said unto him,"), ("say", v("15:33", frm="If thou") + " " + sp("15:34-36"))], "2SAM 15:33–36", DAVID_OLD),
        drawn([caps("15:37"), caps("16:1")], "2SAM 15:37–16:1", below(lambda w, h: K.ziba_asses("za8", w, h, 805), 0.3), "#E8B880", head="Ziba", stamp=16),
        face([cp("16:2", to="unto Ziba,"), say("16:2", frm="What meanest", to="by these?"), cp("16:2", frm="And Ziba said,", to="And Ziba said,"), say("16:2", frm="The asses")], "2SAM 16:2", ZIBA),
        face([cp("16:3", to="And the king said,"), say("16:3", frm="And where is", to="master's son?"), cp("16:3", frm="And Ziba said unto the king,", to="unto the king,"), say("16:3", frm="Behold,"),
              cp("16:4", to="to Ziba,"), say("16:4", frm="Behold,", to="Mephibosheth."), cp("16:4", frm="And Ziba said,", to="And Ziba said,"), say("16:4", frm="I do obeisance;")], "2SAM 16:3–4", DAVID_OLD),
        drawn([caps("16:5-6")], "2SAM 16:5–6", below(lambda w, h: K.shimei("sm8", w, h, 806), 0.3), "#C8B8A0", head="Shimei"),
        face([cp("16:7", to="when he cursed,"), ("say", v("16:7", frm="Begone,") + " " + v("16:8"))], "2SAM 16:7–8", SHIMEI, bg=RED),
        face([cp("16:9", to="unto the king,"), say("16:9", frm="Why should")], "2SAM 16:9", ABISHAI, bg=RED),
        face([cp("16:10", to="And the king said,"), say("16:10", frm="What have I"), cp("16:11", to="and to all his servants,"), ("say", v("16:11", frm="Behold,") + " " + v("16:12"))],
             "2SAM 16:10–12", DAVID_OLD_WEEP, bg=COLD),
        drawn([caps("16:13-14")], "2SAM 16:13–14", below(lambda w, h: K.shimei("sm8b", w, h, 807), 0.3), "#C8B8A0"),
        face([caps("16:15"), cp("16:16", to="said unto Absalom,"), say("16:16", frm="Long live")], "2SAM 16:15–16", HUSHAI, head="Long Live the King"),
        face([cp("16:17", to="to Hushai,"), say("16:17", frm="Is this")], "2SAM 16:17", ABSALOM),
        face([cp("16:18", to="unto Absalom,"), ("say", v("16:18", frm="Nay;") + " " + v("16:19"))], "2SAM 16:18–19", HUSHAI),
        face([cp("16:20", to="to Ahithophel,"), say("16:20", frm="Give your"), cp("16:21", to="unto Absalom,"), say("16:21", frm="Go in unto")], "2SAM 16:20–21", AHITHOPHEL, bg=RED),
        drawn([caps("16:22-23")], "2SAM 16:22–23", lambda w, h: K.roof_tent(w, h, 808), "#5A3A5A")]
PG.extend(pack(SEGS, "2SA-C08-D", PG.next(), end=end_mark("NEXT · O MY SON ABSALOM", "right: 10px; bottom: 34px")))
