"""2 Kings volume, Chapter 7 — The Bones of Elisha (2 Kings 13–14). Every verse, word for word from ref/eng-asv.
The reigns of Jehoahaz and Jehoash of Israel as roll cells; Elisha sick unto death — my father, my father; the arrow of
victory out of the window eastward, and the ground smitten thrice; the man cast into Elisha's sepulchre who revived; then
Amaziah of Judah; the thistle and the cedar of Lebanon; Beth-shemesh and the wall of Jerusalem broken down four hundred
cubits; Azariah; Jeroboam the son of Joash restoring the border (a technical map)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, ELISHA_OLD, JOASH, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch06 as _prev

v, sp = G.v, G.span
JOASH_I = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, brow="sorrow", tear=True, light="#9AA8C8")
JEHOASH_I = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, brow="scowl", light="#FFC14D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2KI-C07-00-Title", "Chapter 7 · The Bones of Elisha", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A2A1E"></rect><g transform="translate(0 320)">{K.arrow_window("t7", 760, 760, 701)}</g>')
    return chapter_title(7, "第七話", "The Bones of Elisha", "2 Kings 13 – 14", svg, "#5A2A1E", v("13:17", frm="Jehovah's arrow of victory,", to="over Syria;"), "2 Kings · Volume Twelve")


R = [reign("Jehoahaz, King of Israel", "13:1-4", judah=False, head="The Kings of Judah and of Israel"), reign("Jehoahaz", "13:5-9", judah=False),
     reign("Jehoash, King of Israel", "13:10-13", judah=False)]
PG.extend(reign_pages(R, "2KI-C07-R", PG.next()))
SEGS = [face([cp("13:14", to="and said,"), say("13:14", frm="My father,")], "2KGS 13:14", JOASH_I, bg=COLD, head="The Arrow of Victory", stamp=13),
        face([cp("13:15", to="And Elisha said unto him,"), say("13:15", frm="Take bow", to="and arrows;"), cp("13:15", frm="and he took unto him"), cp("13:16", to="to the king of Israel,"),
              say("13:16", frm="Put thy hand", to="upon the bow;"), cp("13:16", frm="and he put his hand upon it.")], "2KGS 13:15–16", ELISHA_OLD),
        drawn([cp("13:17", to="And he said,"), say("13:17", frm="Open the window", to="eastward;"), cp("13:17", frm="and he opened it.", to="Then Elisha said,"), say("13:17", frm="Shoot;", to="Shoot;"),
               cp("13:17", frm="and he shot.", to="And he said,"), say("13:17", frm="Jehovah's arrow")], "2KGS 13:17", below(lambda w, h: K.arrow_window("aw7", w, h, 702), 0.36), "#5A2A1E"),
        drawn([cp("13:18", to="And he said,"), say("13:18", frm="Take the arrows;", to="Take the arrows;"), cp("13:18", frm="and he took them.", to="unto the king of Israel,"), say("13:18", frm="Smite upon", to="the ground;"),
               cp("13:18", frm="and he smote thrice,"), cp("13:19", to="and said,"), say("13:19", frm="Thou shouldest")], "2KGS 13:18–19", below(lambda w, h: K.arrow_window("aw7b", w, h, 703, ground_smite=True), 0.4), "#5A2A1E"),
        drawn([caps("13:20-21")], "2KGS 13:20–21", lambda w, h: K.elisha_tomb("et7", w, h, 704), "#4A2A3A", head="The Bones of Elisha"),
        drawn([caps("13:22-25")], "2KGS 13:22–25", below(lambda w, h: K.hazael_map(w, h), 0.3), MAP)]
PG.extend(pack(SEGS, "2KI-C07-D", PG.next()))
R2 = [reign("Amaziah, King of Judah", "14:1-4", head="Amaziah"), reign("Amaziah", "14:5-7")]
PG.extend(reign_pages(R2, "2KI-C07-S", PG.next()))
SEGS2 = [face([cp("14:8", to="saying,"), say("14:8", frm="Come,")], "2KGS 14:8", JOASH, head="The Thistle and the Cedar", stamp=14),
         drawn([cp("14:9", to="saying,"), joined("say", ("14:9", "The thistle"), "14:10")], "2KGS 14:9–10", below(lambda w, h: K.thistle_cedar(w, h, 705), 0.36), "#8FD0E2"),
         drawn([caps("14:11-12")], "2KGS 14:11–12", below(lambda w, h: K.three_kings("bs7", w, h, 706), 0.3), "#FFE6A0"),
         drawn([caps("14:13-14")], "2KGS 14:13–14", below(lambda w, h: K.wall_breach(w, h, 707), 0.3), "#5A4A5A")]
PG.extend(pack(SEGS2, "2KI-C07-E", PG.next()))
R3 = [reign("Jehoash", "14:15-16", judah=False), reign("Amaziah", "14:17-20"), reign("Azariah, King of Judah", "14:21-22"), reign("Jeroboam, King of Israel", "14:23-24", judah=False)]
PG.extend(reign_pages(R3, "2KI-C07-T", PG.next()))
SEGS3 = [drawn([caps("14:25-27")], "2KGS 14:25–27", below(lambda w, h: K.border_map(w, h), 0.3), MAP, head="Jeroboam the Son of Joash"),
         drawn([caps("14:28-29")], "2KGS 14:28–29", lambda w, h: K.samaria_hill("sm7", w, h, 708), "#8FD0E2")]
PG.extend(pack(SEGS3, "2KI-C07-F", PG.next(), end=end_mark("NEXT · AHAZ", "right: 10px; bottom: 34px")))
