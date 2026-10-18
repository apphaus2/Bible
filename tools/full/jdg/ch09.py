"""Judges volume, Chapter 9 — Gibeah (Judges 19). Every verse, word for word from ref/asv.
The Levite and his concubine; the days of eating and drinking at Beth-lehem-judah; Jebus passed by at evening; no man in
Gibeah taking them in, and the old man from the field. Restraint: the men of the city are dark silhouettes with torches
before a shut door (genesis.art4.mob_at_door, as at Sodom); 19:24–28 are words over the shut door by night and at the
dawning, with no one drawn; 19:29–30 are words over a technical figure of twelve routes to the borders of Israel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from num.pages import Pages
from num.art import ALL
from deu.common import shade
from genesis import art4 as GA4
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, face, drawn, F, RED, COLD, GOLDEN
from jdg import ch08 as _prev

v, sp = G.v, G.span
LEVITE = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#5A6E8A", cord=True, light="#FFC14D")
FATHER = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#D8D2C6", hl="#A8A296", beard=True, beard_color="#D8D2C6", scarf="#7A5A3A", cord=True, light="#FFE680")
SERVANT = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FF8A3D")
OLD_MAN = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#6A6A4A", cord=True, light="#FF8A3D")
DUSK = "#6A3A4A"
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JDG-C09-00-Title", "Chapter 9 · Gibeah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#B5524A"></rect><g transform="translate(0 360)">{K.travellers("t9", 760, 720, 901, city=True)}</g>')
    return chapter_title(9, "第九話", "Gibeah", "Judges 19", svg, "#B5524A", v("19:30", frm="consider it,"), "Judges · Volume Seven")


SEGS = [drawn([caps("19:1-3")], "JDG 19:1–3", lambda w, h: K.travellers("tr9", w, h, 911, dusk=False), "#F3D8A0", head="A Certain Levite", stamp=19),
        drawn([caps("19:4"), cp("19:5", to="unto his son-in-law,"), say("19:5", frm="Strengthen")], "JDG 19:4–5", lambda w, h: K.bethlehem_meal("bm9", w, h, 912), "#5A3A2A"),
        face([cp("19:6", to="unto the man,"), say("19:6", frm="Be pleased,"), caps("19:7"), cp("19:8", to="the damsel's father said,"), say("19:8", frm="Strengthen thy heart,", to="until the day declineth;"),
              cp("19:8", frm="and they did eat")], "JDG 19:6–8", FATHER),
        face([cp("19:9", to="said unto him,"), say("19:9", frm="Behold, now")], "JDG 19:9", FATHER),
        drawn([caps("19:10"), cp("19:11", to="unto his master,"), say("19:11", frm="Come, I pray thee,")], "JDG 19:10–11", lambda w, h: K.travellers("tr9b", w, h, 913, city=True), "#B5524A",
              head="Gibeah, Which Belongeth to Benjamin"),
        face([cp("19:12", to="said unto him,"), say("19:12", frm="We will not"), cp("19:13", to="unto his servant,"), say("19:13", frm="Come and let us")], "JDG 19:12–13", LEVITE),
        drawn([caps("19:14-15")], "JDG 19:14–15", lambda w, h: K.empty_street("es9", w, h, 914), DUSK),
        face([caps("19:16"), cp("19:17", to="and the old man said,"), say("19:17", frm="Whither goest")], "JDG 19:16–17", OLD_MAN),
        face([cp("19:18", to="said unto him,"), ("say", v("19:18", frm="We are passing") + " " + v("19:19"))], "JDG 19:18–19", LEVITE),
        face([cp("19:20", to="And the old man said,"), say("19:20", frm="Peace be"), caps("19:21")], "JDG 19:20–21", OLD_MAN),
        drawn([cp("19:22", to="saying,"), say("19:22", frm="Bring forth")], "JDG 19:22", lambda w, h: GA4.mob_at_door("mb9", w, h, 915), "#14123A", head="The Men of the City"),
        face([cp("19:23", to="and said unto them,"), ("say", v("19:23", frm="Nay,") + " " + v("19:24"))], "JDG 19:23–24", OLD_MAN, bg=RED),
        drawn([caps("19:25")], "JDG 19:25", lambda w, h: K.shut_door(w, h, 916), "#14123A"),
        drawn([caps("19:26-27")], "JDG 19:26–27", lambda w, h: K.shut_door(w, h, 917, dawn=True), "#7A7A8A", head="In the Dawning of the Day"),
        drawn([cp("19:28", to="And he said unto her,"), say("19:28", frm="Up,", to="be going;"), cp("19:28", frm="but none answered:")], "JDG 19:28",
              lambda w, h: K.shut_door(w, h, 918, dawn=True), "#7A7A8A"),
        drawn([caps("19:29"), cp("19:30", to="said,"), say("19:30", frm="There was no such")], "JDG 19:29–30", K.below(lambda w, h: K.borders(w, h), 0.36), "#0B1A2E",
              head="Consider It, Take Counsel, and Speak")]
PG.extend(pack(SEGS[:-1], "JDG-C09-D", PG.next()))
PG.extend(pack(SEGS[-1:], "JDG-C09-E", PG.next(), end=end_mark("NEXT · NO KING IN ISRAEL", "right: 10px; bottom: 34px")))
