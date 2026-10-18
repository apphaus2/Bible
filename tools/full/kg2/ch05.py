"""2 Kings volume, Chapter 5 — Jehu (2 Kings 9–10). Every verse, word for word from ref/asv.
The young prophet's vial of oil in an inner chamber — I have anointed thee king; this mad fellow; garments on the top of
the stairs — Jehu is king; the watchman in Jezreel — is it peace?; the driving is like the driving of Jehu, for he driveth
furiously; the portion of Naboth (9:24–27 words over the two chariots in the field); Jezebel at the window — is it peace,
thou Zimri? (9:33–37 words over the empty window and gate); the seventy sons (10:6–8 words over the gate at dawn); the
brethren of Ahaziah and Jehonadab; the house of Baal (10:25 words only) broken down; Hazael in the borders (a map)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, ELISHA, JEHU, JEHU_KING, JORAM_AFRAID, JEZEBEL, WATCHMAN, JEHONADAB, SONS_PROPHETS, MESSENGER, CAPTAIN,
                        reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"
MAP = "#0B1A2E"


@P("2KI-C05-00-Title", "Chapter 5 · Jehu", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFE6A0"></rect><g transform="translate(0 340)">{K.watchtower("t5", 760, 740, 501)}</g>')
    return chapter_title(5, "第五話", "Jehu", "2 Kings 9 – 10", svg, "#B5652E", v("9:20", frm="for he driveth furiously."), "2 Kings · Volume Twelve")


SEGS = [face([cp("9:1", to="and said unto him,"), joined("say", ("9:1", "Gird up"), "9:2", ("9:3", "Then take", "and pour it on his head, and say,")), say("9:3", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"),
              gd("9:3", frm="I have anointed", to="king over Israel."), say("9:3", frm="Then open")], "2KGS 9:1–3", ELISHA,
             head="I Have Anointed Thee King", stamp=9),
        face([caps("9:4"), cp("9:5", to="and he said,"), say("9:5", frm="I have an errand", to="O captain."), cp("9:5", frm="And Jehu said,", to="And Jehu said,"), say("9:5", frm="Unto which", to="of us all?"),
              cp("9:5", frm="And he said,", to="And he said,", after="of us all?"), say("9:5", frm="To thee,", after="of us all?")], "2KGS 9:4–5", SONS_PROPHETS),
        drawn([cp("9:6", to="and said unto him,"), say("9:6", frm="Thus saith Jehovah,", to="the God of Israel,"), gd("9:6", frm="I have anointed"), gods("9:7-9"), gd("9:10", to="none to bury her."),
               cp("9:10", frm="And he opened")], "2KGS 9:6–10", below(lambda w, h: K.inner_chamber("ic5", w, h, 502), 0.56), "#4A3A30"),
        face([cp("9:11", to="and one said unto him,"), say("9:11", frm="Is all well?", to="to thee?"), cp("9:11", frm="And he said unto them,", to="unto them,"), say("9:11", frm="Ye know"),
              cp("9:12", to="And they said,"), say("9:12", frm="It is false;", to="tell us now."), cp("9:12", frm="And he said,", to="And he said,"), say("9:12", frm="Thus and thus", to="saying,"),
              say("9:12", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("9:12", frm="I have anointed")], "2KGS 9:11–12", JEHU),
        drawn([cp("9:13", to="saying,"), say("9:13", frm="Jehu is king.")], "2KGS 9:13", below(lambda w, h: K.stairs_garments("sg5", w, h, 503), 0.2), "#8FD0E2", head="Jehu Is King"),
        face([caps("9:14"), cp("9:15", to="king of Syria.)"), cp("9:15", frm="And Jehu said,", to="And Jehu said,"), say("9:15", frm="If this be"), caps("9:16")], "2KGS 9:14–16", JEHU_KING),
        drawn([cp("9:17", to="and said,"), say("9:17", frm="I see a company.", to="I see a company."), cp("9:17", frm="And Joram said,", to="And Joram said,"), say("9:17", frm="Take a horseman,")], "2KGS 9:17",
              below(lambda w, h: K.watchtower("wt5", w, h, 504), 0.3), "#FFE6A0", head="He Driveth Furiously"),
        face([cp("9:18", to="and said,"), say("9:18", frm="Thus saith the king,", to="Is it peace?"), cp("9:18", frm="And Jehu said,", to="And Jehu said,"), say("9:18", frm="What hast thou", to="behind me."),
              cp("9:18", frm="And the watchman told,", to="saying,"), say("9:18", frm="The messenger")], "2KGS 9:18", JEHU),
        face([cp("9:19", to="and said,"), say("9:19", frm="Thus saith the king,", to="Is it peace?"), cp("9:19", frm="And Jehu answered,", to="And Jehu answered,"), say("9:19", frm="What hast thou"),
              cp("9:20", to="saying,"), say("9:20", frm="He came even")], "2KGS 9:19–20", WATCHMAN),
        face([cp("9:21", to="And Joram said,"), say("9:21", frm="Make ready.", to="Make ready."), cp("9:21", frm="And they made ready"), cp("9:22", to="that he said,"), say("9:22", frm="Is it peace,", to="Jehu?"),
              cp("9:22", frm="And he answered,", to="And he answered,"), say("9:22", frm="What peace,"), cp("9:23", to="and said to Ahaziah,"), say("9:23", frm="There is treachery,")], "2KGS 9:21–23", JORAM_AFRAID, bg=COLD),
        drawn([caps("9:24"), cp("9:25", to="his captain,"), joined("say", ("9:25", "Take up,"), ("9:26", "Surely", "saith Jehovah; and I will requite thee in this plat, saith Jehovah.")),
               say("9:26", frm="Now therefore")], "2KGS 9:24–26", below(lambda w, h: K.naboth_plat("np5", w, h, 505), 0.5), "#3A2A4A"),
        drawn([cp("9:27", to="and said,"), say("9:27", frm="Smite him also", to="in the chariot:"), cp("9:27", frm="and they smote him"), caps("9:28-29")], "2KGS 9:27–29",
              lambda w, h: K.ramoth("rm5", w, h, 506, dusk=True), "#2A1A2A"),
        drawn([caps("9:30"), cp("9:31", to="she said,"), say("9:31", frm="Is it peace,"), cp("9:32", to="and said,"), say("9:32", frm="Who is on my side?", to="who?"), cp("9:32", frm="And there looked out")],
              "2KGS 9:30–32", below(lambda w, h: K.jezebel_window("jw5", w, h, 507), 0.36), "#C8B8A0", head="Jezebel"),
        drawn([cp("9:33", to="And he said,"), say("9:33", frm="Throw her down.", to="Throw her down."), cp("9:33", frm="So they threw her down;"), cp("9:34", to="and he said,"), say("9:34", frm="See now")],
              "2KGS 9:33–34", lambda w, h: K.jezebel_window("jw5b", w, h, 508, empty=True), "#C8B8A0"),
        face([caps("9:35"), cp("9:36", to="And he said,"), joined("say", ("9:36", "This is the word"), "9:37")], "2KGS 9:35–37", JEHU, bg=RED),
        drawn([cp("10:1", to="saying,"), joined("say", "10:2", "10:3")], "2KGS 10:1–3", below(lambda w, h: K.letters(w, h, 509), 0.5), "#3A1A2A", head="Seventy Sons", stamp=10),
        face([cp("10:4", to="and said,"), say("10:4", frm="Behold,"), cp("10:5", to="sent to Jehu, saying,"), say("10:5", frm="We are thy servants,")], "2KGS 10:4–5", MESSENGER, bg=COLD),
        drawn([cp("10:6", to="saying,"), say("10:6", frm="If ye be", to="by to-morrow this time."), cp("10:6", frm="Now the king's sons,"), caps("10:7"), cp("10:8", to="saying,"),
               say("10:8", frm="They have brought", to="the king's sons."), cp("10:8", frm="And he said,", to="And he said,"), say("10:8", frm="Lay ye them")], "2KGS 10:6–8", lambda w, h: K.gate_dawn(w, h, 510), "#5A5A7A"),
        face([cp("10:9", to="and said to all the people,"), joined("say", ("10:9", "Ye are righteous:"), "10:10"), caps("10:11")], "2KGS 10:9–11", JEHU_KING, bg=RED),
        face([caps("10:12"), cp("10:13", to="and said,"), say("10:13", frm="Who are ye?", to="Who are ye?"), cp("10:13", frm="And they answered,", to="And they answered,"), say("10:13", frm="We are the brethren"),
              cp("10:14", to="And he said,"), say("10:14", frm="Take them alive.", to="Take them alive."), cp("10:14", frm="And they took them alive,")], "2KGS 10:12–14", JEHU),
        face([cp("10:15", to="and said to him,"), say("10:15", frm="Is thy heart right,", to="with thy heart?"), cp("10:15", frm="And Jehonadab answered,", to="And Jehonadab answered,"), say("10:15", frm="It is.", to="give me thy hand."),
              cp("10:15", frm="And he gave him"), cp("10:16", to="And he said,"), say("10:16", frm="Come with me,", to="for Jehovah."), cp("10:16", frm="So they made him"), caps("10:17")], "2KGS 10:15–17", JEHONADAB,
             head="Jehonadab the Son of Rechab"),
        drawn([cp("10:18", to="and said unto them,"), joined("say", ("10:18", "Ahab served"), ("10:19", "Now therefore", "he shall not live.")), cp("10:19", frm="But Jehu did it")], "2KGS 10:18–19",
              below(lambda w, h: K.baal_house("bh5", w, h, 511), 0.44), "#C8B8A0", head="The House of Baal"),
        face([cp("10:20", to="And Jehu said,"), say("10:20", frm="Sanctify", to="for Baal."), cp("10:20", frm="And they proclaimed it."), caps("10:21"), cp("10:22", to="over the vestry,"),
              say("10:22", frm="Bring forth", to="worshippers of Baal."), cp("10:22", frm="And he brought them forth")], "2KGS 10:20–22", JEHU),
        face([cp("10:23", to="unto the worshippers of Baal,"), say("10:23", frm="Search,"), cp("10:24", to="and said,"), say("10:24", frm="If any")], "2KGS 10:23–24", JEHU),
        drawn([cp("10:25", to="to the guard and to the captains,"), say("10:25", frm="Go in,", to="let none come forth."), cp("10:25", frm="And they smote them"), caps("10:26-28")], "2KGS 10:25–28",
              lambda w, h: K.baal_house("bh5b", w, h, 512, broken=True), "#5A2A3A"),
        drawn([caps("10:29"), cp("10:30", to="said unto Jehu,"), gd("10:30", frm="Because thou"), caps("10:31")], "2KGS 10:29–31", below(lambda w, h: K.calves("cv5", w, h, 513, people=False), 0.5), "#5A3A5A"),
        drawn([caps("10:32-33")], "2KGS 10:32–33", below(lambda w, h: K.hazael_map(w, h), 0.4), MAP),
        drawn([caps("10:34-36")], "2KGS 10:34–36", lambda w, h: K.samaria_hill("sm5", w, h, 514), "#8FD0E2")]
PG.extend(pack(SEGS, "2KI-C05-D", PG.next(), end=end_mark("NEXT · JOASH", "right: 10px; bottom: 34px")))
