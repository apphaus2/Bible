"""2 Chronicles volume, Chapter 4 — Rehoboam (2 Chronicles 10–12). Every verse, word for word from ref/eng-asv.
Rehoboam at Shechem and Jeroboam come out of Egypt; the counsel of the old men and of the young men — my little finger is
thicker than my father's loins; whips and scorpions; every man to your tents, O Israel; Hadoram stoned (10:18 words only)
and the king fled; Shemaiah's word — ye shall not fight against your brethren; the cities for defence as a map; the priests
and Levites coming to Judah; Maacah and Abijah; then Shishak king of Egypt, the princes humbled — Jehovah is righteous; the
shields of gold taken and shields of brass made in their stead."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from kg1.ch09 import YOUNG
from chr2 import G, art as K
from chr2.common import pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, REHOBOAM, JEROBOAM, ISRAELITE, PROPHET, COLD, GOLDEN, RED
from chr2 import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT = "#0B1A2E", "#0F0E2A"
SHEMAIAH = PROPHET


@P("2CH-C04-00-Title", "Chapter 4 · Rehoboam", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{JA.shechem("t4", 760, 820, 401, stone=False, joshua=False)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(4, "第四話", "Rehoboam", "2 Chronicles 10 – 12", svg, "#3A5A7A", v("10:16", frm="every man to your tents,", to="O Israel:"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("10:1-3"), says("10:4")], "2CHR 10:1–4", below(lambda w, h: JA.shechem("sh4", w, h, 402, stone=False, joshua=False), 0.5), "#8FD0E2", head="Rehoboam at Shechem", stamp=10),
        face([cp("10:5", to="And he said unto them,"), say("10:5", frm="Come again", to="after three days."), cp("10:5", frm="And the people departed."), cp("10:6", to="saying,"),
              say("10:6", frm="What counsel")], "2CHR 10:5–6", REHOBOAM),
        drawn([cp("10:7", to="saying,"), say("10:7", frm="If thou be kind"), caps("10:8")], "2CHR 10:7–8", below(lambda w, h: K.counsel("co4", w, h, 403), 0.4), "#5A2A1E",
              head="The Counsel of the Old Men"),
        drawn([cp("10:9", to="And he said unto them,"), say("10:9", frm="What counsel", to="saying,"), say("10:9", frm="Make the yoke")], "2CHR 10:9",
              below(lambda w, h: K.counsel("co4b", w, h, 404, young=True), 0.36), "#5A2A1E"),
        face([cp("10:10", to="spake unto him, saying,"), joined("say", ("10:10", "Thus shalt thou"), "10:11")], "2CHR 10:10–11", YOUNG, bg=RED),
        face([cp("10:12", to="saying,"), say("10:12", frm="Come to me again"), caps("10:13"), cp("10:14", to="saying,"), say("10:14", frm="My father made"), caps("10:15")], "2CHR 10:12–15",
             REHOBOAM, bg=RED, head="Whips and Scorpions"),
        face([cp("10:16", to="saying,"), say("10:16", frm="What portion", to="see to thine own house, David."), cp("10:16", frm="So all Israel departed")], "2CHR 10:16", ISRAELITE, bg=RED,
             head="To Your Tents, O Israel"),
        drawn([caps("10:17-19")], "2CHR 10:17–19", below(lambda w, h: K.to_tents("tt4", w, h, 405), 0.3), "#C8B8A0")]
PG.extend(pack(SEGS, "2CH-C04-D", PG.next()))
SEGS2 = [drawn([caps("11:1-3"), gods("11:4")], "2CHR 11:1–4", lambda w, h: K.K2.nathan_night(w, h, 406), NIGHT, head="Ye Shall Not Fight against Your Brethren", stamp=11),
         drawn([caps("11:5-10")], "2CHR 11:5–10", below(lambda w, h: K.judah_forts(w, h), 0.3), MAP, head="Cities for Defence"),
         drawn([caps("11:11-12")], "2CHR 11:11–12", below(lambda w, h: K.K2.gold_shields(w, h, 407), 0.3), "#3A2214"),
         drawn([caps("11:13-17")], "2CHR 11:13–17", below(lambda w, h: K.calves("cv4", w, h, 408), 0.5), "#5A3A5A")]
PG.extend(pack(SEGS2, "2CH-C04-E", PG.next()))
R = cells(11, 18, 23, "The House of Rehoboam", "#FFD23F", head="Maacah the Daughter of Absalom", budget=560)
PG.extend(roll(R, "2CH-C04-R", PG.next(), "THE HOUSE OF REHOBOAM · 2 CHRONICLES 11"))
SEGS3 = [drawn([caps("12:1-4")], "2CHR 12:1–4", below(lambda w, h: K.shishak("sk4", w, h, 409), 0.36), "#FFE680", head="Shishak King of Egypt", stamp=12),
         face([cp("12:5", to="and said unto them,"), say("12:5", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("12:5", frm="Ye have forsaken me,")], "2CHR 12:5", SHEMAIAH),
         face([cp("12:6", to="and they said,"), say("12:6", frm="Jehovah is righteous.")], "2CHR 12:6", REHOBOAM, bg=COLD),
         drawn([cp("12:7", to="saying,"), gd("12:7", frm="They have humbled"), gods("12:8")], "2CHR 12:7–8", lambda w, h: K.K2.nathan_night(w, h, 410), NIGHT),
         drawn([caps("12:9")], "2CHR 12:9", below(lambda w, h: K.shishak("sk4b", w, h, 411), 0.3), "#FFE680"),
         drawn([caps("12:10-12")], "2CHR 12:10–12", below(lambda w, h: K.brass_shields(w, h, 412), 0.36), "#3A2214", head="Shields of Brass"),
         face([caps("12:13-16")], "2CHR 12:13–16", REHOBOAM, bg=COLD)]
PG.extend(pack(SEGS3, "2CH-C04-F", PG.next(), end=end_mark("NEXT · ABIJAH AND ASA", "right: 10px; bottom: 34px")))
