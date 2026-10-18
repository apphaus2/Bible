"""2 Kings volume, Chapter 4 — The Siege of Samaria (2 Kings 7–8). Every verse, word for word from ref/asv.
To-morrow a measure of fine flour for a shekel; if Jehovah should make windows in heaven; four leprous men at the gate — why
sit we here until we die?; the camp of the Syrians empty in the twilight; this day is a day of good tidings; the way full of
garments and vessels; the captain trodden in the gate (7:17, 7:20 words over the thronged gate). Then the Shunammite's land
restored; Hazael and the forty camels — the man of God wept; the coverlet (8:15 words over the bedchamber); the reigns of
Jehoram and Ahaziah of Judah as roll cells."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, ELISHA, ELISHA_STERN, JEHORAM, GEHAZI, LEPER, HAZAEL, LORD_CAPTAIN, SHUNAMMITE, MESSENGER,
                        reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("2KI-C04-00-Title", "Chapter 4 · The Siege of Samaria", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A4A"></rect><g transform="translate(0 340)">{K.empty_camp("t4", 760, 740, 401)}</g>')
    return chapter_title(4, "第四話", "The Siege of Samaria", "2 Kings 7 – 8", svg, "#2A2A4A", v("7:9", frm="this day is a day of good tidings,", to="good tidings,"), "2 Kings · Volume Twelve")


SEGS = [face([cp("7:1", to="And Elisha said,"), say("7:1", frm="Hear ye", to="thus saith Jehovah,"), gd("7:1", frm="To-morrow")], "2KGS 7:1", ELISHA, head="Windows in Heaven", stamp=7),
        face([cp("7:2", to="and said,"), say("7:2", frm="Behold, if Jehovah", to="might this thing be?"), cp("7:2", frm="And he said,", to="And he said,"), say("7:2", frm="Behold, thou shalt see")], "2KGS 7:2", LORD_CAPTAIN),
        drawn([cp("7:3", to="and they said one to another,"), say("7:3", frm="Why sit we")], "2KGS 7:3", below(lambda w, h: K.lepers_gate("lg4", w, h, 402), 0.3), "#3A2A4A", head="Four Leprous Men"),
        face([says("7:4")], "2KGS 7:4", LEPER, bg=COLD),
        drawn([caps("7:5"), cp("7:6", to="and they said one to another,"), say("7:6", frm="Lo,"), caps("7:7")], "2KGS 7:5–7", below(lambda w, h: K.empty_camp("ec4", w, h, 403), 0.4), "#2A2A4A"),
        drawn([caps("7:8")], "2KGS 7:8", below(lambda w, h: K.empty_camp("ec4b", w, h, 404, lepers=True), 0.2), "#2A2A4A"),
        face([cp("7:9", to="Then they said one to another,"), say("7:9", frm="We do not well;")], "2KGS 7:9", LEPER, head="A Day of Good Tidings"),
        drawn([cp("7:10", to="saying,"), say("7:10", frm="We came"), caps("7:11")], "2KGS 7:10–11", below(lambda w, h: K.lepers_gate("lg4b", w, h, 405), 0.36), "#3A2A4A"),
        face([cp("7:12", to="unto his servants,"), say("7:12", frm="I will now")], "2KGS 7:12", JEHORAM, bg=COLD),
        face([cp("7:13", to="answered and said,"), say("7:13", frm="Let some take,"), cp("7:14", to="saying,"), say("7:14", frm="Go and see.")], "2KGS 7:13–14", MESSENGER),
        drawn([caps("7:15-16")], "2KGS 7:15–16", below(lambda w, h: K.strewn_way(w, h, 406), 0.26), "#8FD0E2"),
        drawn([caps("7:17"), cp("7:18", to="to the king, saying,"), say("7:18", frm="Two measures"), cp("7:19", to="and said,"), say("7:19", frm="Now, behold,", to="might such a thing be?"),
               cp("7:19", frm="and he said,", to="and he said,"), say("7:19", frm="Behold, thou shalt see"), caps("7:20")], "2KGS 7:17–20", below(lambda w, h: K.gate_press("gp4", w, h, 407), 0.5), "#FFE6A0"),
        face([cp("8:1", to="saying,"), say("8:1", frm="Arise,"), caps("8:2-3")], "2KGS 8:1–3", ELISHA, head="Her House and Her Land", stamp=8),
        face([cp("8:4", to="saying,"), say("8:4", frm="Tell me,"), cp("8:5", to="And Gehazi said,"), say("8:5", frm="My lord,")], "2KGS 8:4–5", GEHAZI),
        face([cp("8:6", to="saying,"), say("8:6", frm="Restore")], "2KGS 8:6", JEHORAM),
        drawn([cp("8:7", to="saying,"), say("8:7", frm="The man of God"), cp("8:8", to="unto Hazael,"), say("8:8", frm="Take a present"), cp("8:9", to="and said,"), say("8:9", frm="Thy son")], "2KGS 8:7–9",
              below(lambda w, h: K.hazael("hz4", w, h, 408), 0.44), "#FFE6A0", head="Hazael"),
        face([cp("8:10", to="And Elisha said unto him,"), say("8:10", frm="Go, say"), caps("8:11")], "2KGS 8:10–11", ELISHA_STERN, bg=COLD),
        face([cp("8:12", to="And Hazael said,"), say("8:12", frm="Why weepeth", to="my lord?"), cp("8:12", frm="And he answered,", to="And he answered,"), say("8:12", frm="Because I know")], "2KGS 8:12", HAZAEL),
        face([cp("8:13", to="And Hazael said,"), say("8:13", frm="But what", to="great thing?"), cp("8:13", frm="And Elisha answered,", to="And Elisha answered,"), say("8:13", frm="Jehovah hath showed me")],
             "2KGS 8:13", ELISHA_STERN, bg=COLD),
        face([cp("8:14", to="who said to him,"), say("8:14", frm="What said", to="to thee?"), cp("8:14", frm="And he answered,", to="And he answered,"), say("8:14", frm="He told me")], "2KGS 8:14", HAZAEL),
        drawn([caps("8:15")], "2KGS 8:15", lambda w, h: K.coverlet(w, h, 409), "#2A1A2A")]
PG.extend(pack(SEGS, "2KI-C04-D", PG.next()))
R = [reign("Jehoram, King of Judah", "8:16-19", head="The Kings of Judah and of Israel"), reign("Jehoram", "8:20-24"), reign("Ahaziah, King of Judah", "8:25-27"), reign("Ahaziah", "8:28-29")]
PG.extend(reign_pages(R, "2KI-C04-R", PG.next(), end=end_mark("NEXT · JEHU", "right: 40px; bottom: 50px")))
