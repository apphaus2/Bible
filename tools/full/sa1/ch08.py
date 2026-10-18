"""1 Samuel volume, Chapter 8 — Goliath (1 Samuel 17). Every verse, word for word from ref/asv.
The vale of Elah, the champion of Gath in his brass; forty days; David sent with parched grain and loaves; the living God;
Eliab's anger; the lion and the bear; Saul's armor put off; five smooth stones; Am I a dog?; In the name of Jehovah of hosts —
the battle is Jehovah's; the stone in the forehead (the digest's David and Goliath book throughout). Restraint: 17:51 and
17:54, 17:57 (the head) are words over the fallen giant and the fleeing host — nothing of it drawn; Whose son art thou?"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, DAVID, DAVID_BOLD, GOLIATH, JESSE, ISRAELITE, RED, COLD, GOLDEN)
from sa1 import ch07 as _prev

v, sp = G.v, G.span
ELIAB = F("adam", skin="#C98E66", shadow="#5A2A1E", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", brow="scowl", light="#D7261E")
ABNER = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#5A5A2A", cord=True, light="#FFC14D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1SA-C08-00-Title", "Chapter 8 · Goliath", title=True)
def title(n):
    bg, art = D("B3", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8A3A2A"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(8, "第八話", "Goliath", "1 Samuel 17", svg, "#8A3A2A", v("17:47", frm="for the battle is Jehovah's,"), "1 Samuel · Volume Nine")


SEGS = [drawn([caps("17:1-3")], "1SAM 17:1–3", lambda w, h: JA.armed("el8", w, h, 811, tribes=("JUDAH", "BENJAMIN")), "#F3D8A0", head="The Vale of Elah", stamp=17),
        over([caps("17:4-7")], "1SAM 17:4–7", "B3", 0, head="A Champion out of Gath"),
        face([cp("17:8", to="said unto them,"), ("say", v("17:8", frm="Why are ye") + " " + v("17:9")), cp("17:10", to="And the Philistine said,"), say("17:10", frm="I defy")],
             "1SAM 17:8–10", GOLIATH, bg=RED),
        over([caps("17:11")], "1SAM 17:11", "B3", 2),
        drawn([caps("17:12-16")], "1SAM 17:12–16", D("B1", 3)[1], D("B1", 3)[0], head="Forty Days"),
        face([cp("17:17", to="unto David his son,"), ("say", v("17:17", frm="Take now") + " " + v("17:18")), caps("17:19")], "1SAM 17:17–19", JESSE),
        drawn([caps("17:20-24")], "1SAM 17:20–24", D("B3", 2)[1], D("B3", 2)[0]),
        face([cp("17:25", to="And the men of Israel said,"), say("17:25", frm="Have ye seen")], "1SAM 17:25", ISRAELITE, head="The Armies of the Living God"),
        over([cp("17:26", to="saying,"), say("17:26", frm="What shall be done")], "1SAM 17:26", "B4", 0),
        face([cp("17:27", to="saying,"), say("17:27", frm="So shall it"), cp("17:28", to="and he said,"), say("17:28", frm="Why art thou")], "1SAM 17:27–28", ELIAB, bg=RED),
        face([cp("17:29", to="And David said,"), say("17:29", frm="What have I"), caps("17:30-31")], "1SAM 17:29–31", DAVID),
        over([cp("17:32", to="said to Saul,"), say("17:32", frm="Let no man's")], "1SAM 17:32", "B4", 1, head="The Lion and the Bear"),
        over([cp("17:33", to="said to David,"), say("17:33", frm="Thou art not")], "1SAM 17:33", "B4", 2),
        over([cp("17:34", to="unto Saul,"), ("say", v("17:34", frm="Thy servant") + " " + v("17:35") + " " + v("17:36"))], "1SAM 17:34–36", "B4", 3),
        over([cp("17:37", to="And David said,"), say("17:37", frm="Jehovah that", to="this Philistine."), cp("17:37", frm="And Saul said unto David,", to="unto David,"),
              say("17:37", frm="Go,")], "1SAM 17:37", "B4", 4),
        over([caps("17:38"), cp("17:39", to="And David said unto Saul,"), say("17:39", frm="I cannot go", to="not proved them."), cp("17:39", frm="And David put them off")], "1SAM 17:38–39", "B5", 0,
             head="Five Smooth Stones"),
        over([cp("17:40", to="and his sling was in his hand:")], "1SAM 17:40", "B5", 1),
        over([cp("17:40", frm="and he drew near"), caps("17:41-42")], "1SAM 17:40–42", "B5", 2),
        face([cp("17:43", to="said unto David,"), say("17:43", frm="Am I a dog,", to="with staves?"), cp("17:43", frm="And the Philistine cursed"), cp("17:44", to="said to David,"),
              say("17:44", frm="Come to me,")], "1SAM 17:43–44", GOLIATH, bg=RED, head="In the Name of Jehovah of Hosts"),
        face([cp("17:45", to="to the Philistine,"), ("say", v("17:45", frm="Thou comest") + " " + v("17:46") + " " + v("17:47"))], "1SAM 17:45–47", DAVID_BOLD, bg=GOLDEN),
        over([caps("17:48")], "1SAM 17:48", "B7", 0, head="A Sling and a Stone"),
        over([cp("17:49", to="and smote the Philistine in his forehead;")], "1SAM 17:49", "B7", 1),
        over([cp("17:49", frm="and the stone sank")], "1SAM 17:49", "B7", 2),
        over([caps("17:50-51")], "1SAM 17:50–51", "B7", 2),
        over([caps("17:52-54")], "1SAM 17:52–54", "B7", 3),
        face([cp("17:55", to="the captain of the host,"), say("17:55", frm="Abner,", to="this youth?"), cp("17:55", frm="And Abner said,", to="And Abner said,"), say("17:55", frm="As thy soul"),
              cp("17:56", to="And the king said,"), say("17:56", frm="Inquire")], "1SAM 17:55–56", ABNER, head="Whose Son Art Thou?"),
        face([caps("17:57"), cp("17:58", to="said to him,"), say("17:58", frm="Whose son", to="young man?"), cp("17:58", frm="And David answered,", to="And David answered,"), say("17:58", frm="I am the son")],
             "1SAM 17:57–58", DAVID_BOLD)]
PG.extend(pack(SEGS, "1SA-C08-D", PG.next(), end=end_mark("NEXT · SAUL HATH SLAIN HIS THOUSANDS", "right: 10px; bottom: 34px")))
