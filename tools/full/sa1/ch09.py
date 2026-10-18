"""1 Samuel volume, Chapter 9 — Saul Hath Slain His Thousands (1 Samuel 18–19). Every verse, word for word from ref/asv.
The soul of Jonathan knit with the soul of David, the robe, the sword and the bow (the digest's panels); the women with
timbrels — Saul hath slain his thousands, and David his ten thousands; the spear cast to the wall; Merab and Michal, and the
dowry (18:25–27 words over the camp); Jonathan pleading for David; the spear in the wall again; Michal letting David down
through the window and the teraphim in the bed; and Saul among the prophets at Naioth (19:24 words over the company)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jdg import art as JG
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_MAD, DAVID, DAVID_BOLD, JONATHAN, ISRAELITE, RED, COLD, GOLDEN)
from discourse import seg
from sa1 import ch08 as _prev

v, sp = G.v, G.span
MICHAL = F("eve", skin="#D9A27A", shadow="#8A5A5A", hair="#1A1210", scarf="#8A1A2A", band=True, light="#FFC14D")
SERVANT = F("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1SA-C09-00-Title", "Chapter 9 · Saul Hath Slain His Thousands", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3B86A"></rect><g transform="translate(0 360)">{K.women_singing("t9", 760, 720, 901)}</g>')
    return chapter_title(9, "第九話", "Saul Hath Slain His Thousands", "1 Samuel 18 – 19", svg, "#F3B86A", v("18:7", frm="Saul hath slain"), "1 Samuel · Volume Nine")


SEGS = [over([caps("18:1-2")], "1SAM 18:1–2", "B8", 0, head="The Soul of Jonathan", stamp=18),
        over([caps("18:3-4")], "1SAM 18:3–4", "B8", 2),
        drawn([caps("18:5-6"), cp("18:7", to="and said,"), say("18:7", frm="Saul hath slain")], "1SAM 18:5–7", lambda w, h: K.women_singing("ws9", w, h, 911), "#F3B86A",
              head="His Thousands and His Ten Thousands"),
        face([cp("18:8", to="and he said,"), say("18:8", frm="They have ascribed"), caps("18:9")], "1SAM 18:8–9", SAUL_MAD, bg=RED),
        over([caps("18:10"), cp("18:11", to="for he said,"), say("18:11", frm="I will smite", to="to the wall."), cp("18:11", frm="And David avoided")], "1SAM 18:10–11", "B8", 3),
        drawn([caps("18:12-16")], "1SAM 18:12–16", lambda w, h: JA.armed("dv9", w, h, 912, tribes=("JUDAH", "EPHRAIM")), "#F3D8A0"),
        face([cp("18:17", to="said to David,"), say("18:17", frm="Behold,", to="Jehovah's battles."), cp("18:17", frm="For Saul said,", to="For Saul said,"), say("18:17", frm="Let not my hand")],
             "1SAM 18:17", SAUL_KING, head="Michal, Saul's Daughter"),
        face([cp("18:18", to="unto Saul,"), say("18:18", frm="Who am I,"), caps("18:19-20")], "1SAM 18:18–20", DAVID),
        face([cp("18:21", to="And Saul said,"), say("18:21", frm="I will give him", to="against him."), cp("18:21", frm="Wherefore Saul said", to="to David,"), say("18:21", frm="Thou shalt this day"),
              cp("18:22", to="saying,"), say("18:22", frm="Commune")], "1SAM 18:21–22", SAUL_MAD, bg=RED),
        face([cp("18:23", to="And David said,"), say("18:23", frm="Seemeth it"), cp("18:24", to="saying,"), say("18:24", frm="On this manner")], "1SAM 18:23–24", DAVID),
        face([cp("18:25", to="And Saul said,"), say("18:25", frm="Thus shall ye", to="the king's enemies."), cp("18:25", frm="Now Saul thought")], "1SAM 18:25", SAUL_MAD, bg=RED),
        drawn([caps("18:26-30")], "1SAM 18:26–30", lambda w, h: JG.midian(w, h, 913, night_=True), "#14123A"),
        face([caps("19:1"), cp("19:2", to="saying,"), ("say", v("19:2", frm="Saul my father") + " " + v("19:3"))], "1SAM 19:1–3", JONATHAN, head="Let Not the King Sin", stamp=19),
        face([cp("19:4", to="and said unto him,"), ("say", v("19:4", frm="Let not the king") + " " + v("19:5"))], "1SAM 19:4–5", JONATHAN),
        face([cp("19:6", to="and Saul sware,"), say("19:6", frm="As Jehovah liveth,"), caps("19:7-8")], "1SAM 19:6–8", SAUL_KING),
        over([caps("19:9-10")], "1SAM 19:9–10", "B8", 3, head="Through the Window"),
        face([cp("19:11", to="told him, saying,"), say("19:11", frm="If thou save")], "1SAM 19:11", MICHAL, bg=COLD),
        drawn([caps("19:12")], "1SAM 19:12", lambda w, h: K.let_down("ld9", w, h, 914), "#14123A"),
        drawn([caps("19:13"), cp("19:14", to="she said,"), say("19:14", frm="He is sick."), cp("19:15", to="saying,"), say("19:15", frm="Bring him up"), caps("19:16")], "1SAM 19:13–16",
              lambda w, h: K.teraphim_bed(w, h, 915), "#3A2A2A"),
        face([cp("19:17", to="And Saul said unto Michal,"), say("19:17", frm="Why hast thou", to="he is escaped?"), cp("19:17", frm="And Michal answered Saul,", to="answered Saul,"),
              say("19:17", frm="He said unto me,")], "1SAM 19:17", MICHAL, bg=COLD),
        face([caps("19:18"), cp("19:19", to="saying,"), say("19:19", frm="Behold,"), caps("19:20-21")], "1SAM 19:18–21", SAUL_KING, head="Is Saul Also among the Prophets?"),
        seg(None, "1SAM 19:20", art=lambda w, h: K.naioth("nt9", w, h, 916), bg="#F3B86A", h=300),
        face([cp("19:22", to="and he asked and said,"), say("19:22", frm="Where are", to="and David?"), cp("19:22", frm="And one said,", to="And one said,"), say("19:22", frm="Behold, they are"),
               caps("19:23"), cp("19:24", to="all that night."), cp("19:24", frm="Wherefore they say,", to="Wherefore they say,"), say("19:24", frm="Is Saul also")], "1SAM 19:22–24", SAUL_MAD, bg=RED)]
PG.extend(pack(SEGS[:-3], "1SA-C09-D", PG.next()))
PG.extend(pack(SEGS[-3:-1], "1SA-C09-E", PG.next()))
PG.extend(pack(SEGS[-1:], "1SA-C09-F", PG.next(), default_head="Is Saul Also among the Prophets?", end=end_mark("NEXT · JONATHAN AND DAVID", "right: 10px; bottom: 34px")))
