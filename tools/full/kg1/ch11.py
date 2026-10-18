"""1 Kings volume, Chapter 11 — Elijah (1 Kings 16–17). Every verse, word for word from ref/asv.
Jehu's word against Baasha (the Voice box); the reigns of Elah, Zimri seven days (16:18 words over the king's house burning),
Tibni and Omri, the hill Samaria bought for two talents; Ahab and Jezebel and the altar of Baal; Hiel and Jericho. Then
Elijah the Tishbite before Ahab — there shall not be dew nor rain; the brook Cherith and the ravens; the widow of Zarephath,
the jar of meal and the cruse of oil; the widow's son revived — see, thy son liveth."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from sa2 import art as K2
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, AHAB, ELIJAH, ELIJAH_FIRE, WIDOW, reign, reign_pages, RED, COLD, GOLDEN)
from kg1 import ch10 as _prev

v, sp = G.v, G.span
JEHU_P = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#3A4A3A", cord=True, light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C11-00-Title", "Chapter 11 · Elijah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{K.cherith("t11", 760, 780, 1101)}</g>')
    return chapter_title(11, "第十一話", "Elijah", "1 Kings 16 – 17", svg, "#4A6A8A", v("17:6", to="in the evening;"), "1 Kings · Volume Eleven")


SEGS = [face([cp("16:1"), gods("16:2-4")], "1KGS 16:1–4", JEHU_P, bg=NIGHT, head="Jehu the Son of Hanani", stamp=16)]
PG.extend(pack(SEGS, "1KI-C11-D", PG.next()))
R1 = [reign("Baasha", "16:5-7", judah=False), reign("Elah, King of Israel", "16:8-10", judah=False), reign("Zimri", "16:11-14", judah=False),
      reign("Zimri, Seven Days in Tirzah", "16:15-17", judah=False)]
PG.extend(reign_pages(R1, "1KI-C11-R", PG.next()))
SEGS2 = [drawn([caps("16:18-20")], "1KGS 16:18–20", lambda w, h: JA.burning(w, h, 1102, city="tirzah"), "#2A0A0A"),
         drawn([caps("16:21-24")], "1KGS 16:21–24", below(lambda w, h: K.samaria_hill("sm11", w, h, 1103), 0.36), "#8FD0E2", head="Omri and the Hill Samaria"),
         drawn([caps("16:25-28")], "1KGS 16:25–28", below(lambda w, h: K.samaria_hill("sm11b", w, h, 1104), 0.4), "#8FD0E2"),
         drawn([caps("16:29-33")], "1KGS 16:29–33", below(lambda w, h: K.baal_altar("ba11", w, h, 1105), 0.4), "#5A2A3A", head="Ahab and Jezebel"),
         drawn([caps("16:34")], "1KGS 16:34", lambda w, h: K2.rabbah("jr11", w, h, 1106, camp=False, dusk=True), "#3A1A2A"),
         face([cp("17:1", to="said unto Ahab,"), say("17:1", frm="As Jehovah,")], "1KGS 17:1", ELIJAH_FIRE, bg=RED, head="Elijah the Tishbite", stamp=17),
         drawn([cp("17:2"), gods("17:3-4"), caps("17:5-6")], "1KGS 17:2–6", below(lambda w, h: K.cherith("ch11", w, h, 1107), 0.44), "#8FD0E2", head="The Brook Cherith"),
         drawn([caps("17:7"), cp("17:8"), gods("17:9")], "1KGS 17:7–9", below(lambda w, h: K.cherith("ch11b", w, h, 1108, dry=True), 0.4), "#FFE6A0"),
         drawn([cp("17:10", to="and said,"), say("17:10", frm="Fetch me"), cp("17:11", to="and said,"), say("17:11", frm="Bring me")], "1KGS 17:10–11",
               below(lambda w, h: K.zarephath("zp11", w, h, 1109), 0.36), "#FFE6A0", head="The Widow of Zarephath"),
         face([cp("17:12", to="And she said,"), say("17:12", frm="As Jehovah thy God")], "1KGS 17:12", WIDOW, bg=COLD),
         face([cp("17:13", to="unto her,"), say("17:13", frm="Fear not;"), say("17:14", to="For thus saith Jehovah, the God of Israel,"), gd("17:14", frm="The jar of meal")], "1KGS 17:13–14", ELIJAH),
         drawn([caps("17:15-16")], "1KGS 17:15–16", lambda w, h: K.jar_cruse(w, h, 1110), "#3A2A1E"),
         face([caps("17:17"), cp("17:18", to="unto Elijah,"), say("17:18", frm="What have I")], "1KGS 17:17–18", WIDOW, bg=COLD, head="See, Thy Son Liveth"),
         drawn([cp("17:19", to="And he said unto her,"), say("17:19", frm="Give me thy son.", to="Give me thy son."), cp("17:19", frm="And he took him"), cp("17:20", to="and said,"),
                say("17:20", frm="O Jehovah")], "1KGS 17:19–20", below(lambda w, h: K.upper_chamber("uc11", w, h, 1111), 0.4), "#D8B88A"),
         drawn([cp("17:21", to="and said,"), say("17:21", frm="O Jehovah"), caps("17:22")], "1KGS 17:21–22", below(lambda w, h: K.upper_chamber("uc11b", w, h, 1112), 0.34), "#D8B88A"),
         drawn([cp("17:23", to="and Elijah said,"), say("17:23", frm="See,")], "1KGS 17:23", below(lambda w, h: K.upper_chamber("uc11c", w, h, 1113, down=True), 0.3), "#D8B88A"),
         face([cp("17:24", to="to Elijah,"), say("17:24", frm="Now I know")], "1KGS 17:24", WIDOW)]
PG.extend(pack(SEGS2, "1KI-C11-E", PG.next(), end=end_mark("NEXT · THE FIRE OF JEHOVAH", "right: 10px; bottom: 34px")))
