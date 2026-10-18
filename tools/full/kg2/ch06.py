"""2 Kings volume, Chapter 6 — Joash (2 Kings 11–12). Every verse, word for word from ref/asv.
Athaliah destroys the seed royal (11:1 words only); Jehosheba hides the child Joash six years in the house of Jehovah;
Jehoiada's covenant with the captains and the guard set about the king; the crown and the testimony — long live the king;
Athaliah crying Treason! treason! (11:16, 11:20 words over the horses' entry, empty); the house of Baal broken down; the
boy king of seven years. Then Jehoash and the breaches of the house: Jehoiada's chest with a hole in its lid; the workmen who
dealt faithfully; the hallowed things sent to Hazael; and Joash's end (12:20–21 words over the house of Millo)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, JEHOIADA, ATHALIAH, JOASH, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2KI-C06-00-Title", "Chapter 6 · Joash", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 320)">{K.child_king("t6", 760, 760, 601, athaliah=True)}</g>')
    return chapter_title(6, "第六話", "Joash", "2 Kings 11 – 12", svg, "#2C7DA8", v("11:12", frm="Long live the king."), "2 Kings · Volume Twelve")


SEGS = [face([caps("11:1")], "2KGS 11:1", ATHALIAH, bg=RED, head="Athaliah", stamp=11),
        drawn([caps("11:2-3")], "2KGS 11:2–3", below(lambda w, h: K.hidden_child("hc6", w, h, 602), 0.26), "#3A2A2A", head="Hid Six Years"),
        face([caps("11:4"), cp("11:5", to="saying,"), joined("say", ("11:5", "This is the thing"), "11:6", "11:7", "11:8")], "2KGS 11:4–8", JEHOIADA, head="Jehoiada the Priest"),
        drawn([caps("11:9-11")], "2KGS 11:9–11", below(lambda w, h: K.child_king("ck6", w, h, 603), 0.3), "#8FD0E2"),
        drawn([cp("11:12", to="and said,"), say("11:12", frm="Long live")], "2KGS 11:12", lambda w, h: K.child_king("ck6b", w, h, 604), "#8FD0E2", head="Long Live the King"),
        drawn([caps("11:13"), cp("11:14", to="and cried,"), say("11:14", frm="Treason!")], "2KGS 11:13–14", below(lambda w, h: K.child_king("ck6c", w, h, 605, athaliah=True), 0.3), "#8FD0E2"),
        face([cp("11:15", to="and said unto them,"), say("11:15", frm="Have her forth", to="with the sword."), cp("11:15", frm="For the priest said,", to="For the priest said,"), say("11:15", frm="Let her not")],
             "2KGS 11:15", JEHOIADA, bg=RED),
        drawn([caps("11:16")], "2KGS 11:16", lambda w, h: K.horses_entry(w, h, 606), "#5A4A5A"),
        drawn([caps("11:17-18")], "2KGS 11:17–18", below(lambda w, h: K.baal_house("bh6", w, h, 607, broken=True), 0.36), "#5A2A3A"),
        drawn([caps("11:19-21")], "2KGS 11:19–21", below(lambda w, h: K.judgment_porch("jp6", w, h, 608), 0.36), "#5A2A1E")]
PG.extend(pack(SEGS, "2KI-C06-D", PG.next()))
SEGS2 = [face([caps("12:1-3"), cp("12:4", to="said to the priests,"), joined("say", ("12:4", "All the money"), "12:5")], "2KGS 12:1–5", JOASH, head="The Breaches of the House", stamp=12),
         face([caps("12:6"), cp("12:7", to="and said unto them,"), say("12:7", frm="Why repair"), caps("12:8")], "2KGS 12:6–8", JOASH),
         drawn([caps("12:9-10")], "2KGS 12:9–10", below(lambda w, h: K.chest("cs6", w, h, 609), 0.3), "#8FD0E2", head="A Chest with a Hole in the Lid"),
         drawn([caps("12:11-14")], "2KGS 12:11–14", below(lambda w, h: K.repairers("rp6", w, h, 610), 0.4), "#8FD0E2"),
         drawn([caps("12:15-16")], "2KGS 12:15–16", below(lambda w, h: K.chest("cs6b", w, h, 611), 0.24), "#8FD0E2"),
         drawn([caps("12:17-18")], "2KGS 12:17–18", below(lambda w, h: K.K2.vessels(w, h, 612), 0.34), "#2A1A3A", head="Hazael"),
         drawn([caps("12:19-21")], "2KGS 12:19–21", lambda w, h: K.millo(w, h, 613), "#3A1A2A")]
PG.extend(pack(SEGS2, "2KI-C06-E", PG.next(), end=end_mark("NEXT · THE BONES OF ELISHA", "right: 10px; bottom: 34px")))
