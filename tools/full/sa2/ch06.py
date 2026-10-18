"""2 Samuel volume, Chapter 6 — Thou Art the Man (2 Samuel 11–12). Every verse, word for word from ref/asv.
David tarried at Jerusalem; 11:2–4 words over the empty roof at eventide (the digest's panel: David alone, no one else
drawn); Uriah sleeping at the king's door — the ark, and Israel, and Judah, abide in booths; the letter; Uriah's death as
the digest's distant wall; the messenger; the thing displeased Jehovah. Nathan's ewe lamb, thou art the man, I have sinned;
the child's sickness and the seventh day (no child drawn: the lamp and the elders); Solomon, Jedidiah; the crown of Rabbah
(12:31 words over the city at dusk)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, DAVID_KING, DAVID_WRATH, DAVID_GRIEF, NATHAN, NATHAN_STERN, JOAB, MESSENGER,
                        RED, COLD, GOLDEN)
from sa2 import ch05 as _prev

v, sp = G.v, G.span
URIAH = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#8A2A2A", cord=True, light="#FFC14D")
SERVANT = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", brow="sorrow", light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0B0B2A"


@P("2SA-C06-00-Title", "Chapter 6 · Thou Art the Man", title=True)
def title(n):
    bg, art = D("A9", 0, "xMaxYMid")
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#C8402A"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(6, "第六話", "Thou Art the Man", "2 Samuel 11 – 12", svg, "#C8402A", v("12:7", frm="Thou art the man.", to="Thou art the man."), "2 Samuel · Volume Ten")


SEGS = [drawn([caps("11:1")], "2SAM 11:1", lambda w, h: K.rabbah("rb6", w, h, 601), "#8FD0E2", head="David Tarried at Jerusalem", stamp=11),
        over([caps("11:2"), cp("11:3", to="And one said,"), say("11:3", frm="Is not this"), caps("11:4")], "2SAM 11:2–4", "A7", 0),
        drawn([cp("11:5", to="and said,"), say("11:5", frm="I am with child.")], "2SAM 11:5", lambda w, h: K.nathan_night(w, h, 602), "#0F0E2A"),
        face([cp("11:6", to="saying,"), say("11:6", frm="Send me", to="Hittite."), cp("11:6", frm="And Joab sent"), caps("11:7"), cp("11:8", to="to Uriah,"), say("11:8", frm="Go down", to="wash thy feet."),
              cp("11:8", frm="And Uriah departed")], "2SAM 11:6–8", DAVID_KING, head="Uriah the Hittite"),
        drawn([caps("11:9"), cp("11:10", to="saying,"), say("11:10", frm="Uriah went not", to="unto his house,"), cp("11:10", frm="David said unto Uriah,", to="unto Uriah,"), say("11:10", frm="Art thou not")],
              "2SAM 11:9–10", below(lambda w, h: K.uriah_door("ud6", w, h, 603), 0.4), "#14123A"),
        face([cp("11:11", to="unto David,"), say("11:11", frm="The ark,")], "2SAM 11:11", URIAH),
        face([cp("11:12", to="to Uriah,"), say("11:12", frm="Tarry here", to="let thee depart."), cp("11:12", frm="So Uriah abode"), caps("11:13")], "2SAM 11:12–13", DAVID_KING),
        over([caps("11:14"), cp("11:15", to="saying,"), say("11:15", frm="Set ye")], "2SAM 11:14–15", "A7", 1, head="The Letter"),
        over([caps("11:16-17")], "2SAM 11:16–17", "A7", 2),
        face([caps("11:18"), cp("11:19", to="saying,"), ("say", v("11:19", frm="When thou") + " " + sp("11:20-21"))], "2SAM 11:18–21", JOAB, bg=RED),
        face([caps("11:22"), cp("11:23", to="unto David,"), ("say", v("11:23", frm="The men prevailed") + " " + v("11:24"))], "2SAM 11:22–24", MESSENGER),
        face([cp("11:25", to="unto the messenger,"), say("11:25", frm="Thus shalt thou say")], "2SAM 11:25", DAVID_KING),
        over([caps("11:26-27")], "2SAM 11:26–27", "A7", 3),
        over([cp("12:1", to="said unto him,"), say("12:1", frm="There were two men")], "2SAM 12:1", "A8", 0, head="The Ewe Lamb", stamp=12),
        over([says("12:2-4")], "2SAM 12:2–4", "A8", 1),
        over([cp("12:5", to="to Nathan,"), ("say", v("12:5", frm="As Jehovah") + " " + v("12:6"))], "2SAM 12:5–6", "A8", 2),
        over([cp("12:7", to="And Nathan said to David,"), say("12:7", frm="Thou art the man.", to="Thou art the man.")], "2SAM 12:7", "A9", 0, head="Thou Art the Man"),
        face([say("12:7", frm="Thus saith Jehovah,", to="the God of Israel,"), ("god", v("12:7", frm="I anointed") + " " + v("12:8"))], "2SAM 12:7–8", NATHAN_STERN),
        over([gods("12:9-10")], "2SAM 12:9–10", "A9", 1),
        face([say("12:11", to="Thus saith Jehovah,"), ("god", v("12:11", frm="Behold,") + " " + v("12:12"))], "2SAM 12:11–12", NATHAN_STERN, bg=NIGHT),
        over([cp("12:13", to="unto Nathan,"), say("12:13", frm="I have sinned", to="against Jehovah.")], "2SAM 12:13", "A9", 2),
        over([cp("12:13", frm="And Nathan said unto David,", to="unto David,"), ("say", v("12:13", frm="Jehovah also") + " " + v("12:14"))], "2SAM 12:13–14", "A9", 3),
        drawn([caps("12:15-17")], "2SAM 12:15–17", lambda w, h: K.night_vigil("nv6", w, h, 604), "#1A1430"),
        face([cp("12:18", to="for they said,"), say("12:18", frm="Behold, while")], "2SAM 12:18", SERVANT, bg=COLD, head="The Seventh Day"),
        face([cp("12:19", to="unto his servants,"), say("12:19", frm="Is the child dead?", to="Is the child dead?"), cp("12:19", frm="And they said,", to="And they said,"), say("12:19", frm="He is dead.")],
             "2SAM 12:19", DAVID_GRIEF, bg=COLD),
        drawn([caps("12:20")], "2SAM 12:20", lambda w, h: K.prayer("pr6", w, h, 605), "#3A1A2A"),
        face([cp("12:21", to="unto him,"), say("12:21", frm="What thing")], "2SAM 12:21", SERVANT, bg=COLD),
        face([cp("12:22", to="And he said,"), ("say", v("12:22", frm="While the child") + " " + v("12:23"))], "2SAM 12:22–23", DAVID_GRIEF, bg=COLD),
        over([caps("12:24-25")], "2SAM 12:24–25", "A9", 4),
        ]
SEGS2 = [drawn([caps("12:26"), cp("12:27", to="and said,"), ("say", v("12:27", frm="I have fought") + " " + v("12:28"))], "2SAM 12:26–28", below(lambda w, h: K.rabbah("rb6b", w, h, 606), 0.3), "#8FD0E2",
              head="The City of Waters"),
        drawn([caps("12:29-30")], "2SAM 12:29–30", lambda w, h: K.crown_talent(w, h, 607), "#2A1A3A"),
        drawn([caps("12:31")], "2SAM 12:31", lambda w, h: K.rabbah("rb6c", w, h, 608, camp=False, dusk=True), "#3A1A2A")]
PG.extend(pack(SEGS, "2SA-C06-D", PG.next()))
PG.extend(pack(SEGS2, "2SA-C06-E", PG.next(), end=end_mark("NEXT · ABSALOM", "right: 10px; bottom: 34px")))
