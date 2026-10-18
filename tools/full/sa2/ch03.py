"""2 Samuel volume, Chapter 3 — The City of David (2 Samuel 5–6). Every verse, word for word from ref/asv.
All the tribes at Hebron — we are thy bone and thy flesh; David anointed king over Israel (the digest's panels); the
stronghold of Zion taken from the Jebusites; Hiram's cedar; the sons born in Jerusalem; Baal-perazim and the sound of
marching in the tops of the mulberry-trees; the ark on the new cart, Uzzah at the threshing-floor of Nacon (6:7 words over
the cart under a dark sky); three months in the house of Obed-edom; David dancing before Jehovah in a linen ephod, and
Michal at the window."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from sa1 import art as K1
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, says, caps, over, face, drawn, D, DAVID_KING, DAVID_WRATH, MICHAL, ISRAELITE, RED, COLD, GOLDEN)
from sa2 import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2SA-C03-00-Title", "Chapter 3 · The City of David", title=True)
def title(n):
    bg, art = D("A3", 2)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFB04A"></rect><g transform="translate(0 360)">{art(760, 720)}</g>')
    return chapter_title(3, "第三話", "The City of David", "2 Samuel 5 – 6", svg, "#FFB04A", v("6:14", to="with all his might;"), "2 Samuel · Volume Ten")


SEGS = [face([cp("5:1", to="saying,"), ("say", v("5:1", frm="Behold,") + " " + v("5:2"))], "2SAM 5:1–2", ISRAELITE, head="King over All Israel", stamp=5),
        over([caps("5:3")], "2SAM 5:3", "A2", 0),
        over([caps("5:4-5")], "2SAM 5:4–5", "A2", 1),
        drawn([cp("5:6", to="saying,"), say("5:6", frm="Except thou", to="come in hither;"), cp("5:6", frm="thinking,")], "2SAM 5:6",
              below(lambda w, h: K.jebus("jb3", w, h, 301), 0.3), "#8FD0E2", head="The Stronghold of Zion"),
        over([caps("5:7"), cp("5:8", to="on that day,"), say("5:8", frm="Whosoever", to="David's soul."), cp("5:8", frm="Wherefore they say,", to="Wherefore they say,"),
              say("5:8", frm="There are the blind")], "2SAM 5:7–8", "A2", 2),
        over([caps("5:9-12")], "2SAM 5:9–12", "A2", 3),
        drawn([caps("5:13-16")], "2SAM 5:13–16", below(lambda w, h: K.sons_hebron(w, h, K.SONS_J, hi="SOLOMON"), 0.36), "#1A1430"),
        drawn([caps("5:17-18")], "2SAM 5:17–18", lambda w, h: JA.armed("rp3", w, h, 302, tribes=()), "#F3D8A0", head="Baal-perazim"),
        drawn([cp("5:19", to="saying,"), say("5:19", frm="Shall I go up", to="into my hand?"), cp("5:19", frm="And Jehovah said unto David,", to="unto David,"), gd("5:19", frm="Go up;")],
              "2SAM 5:19", lambda w, h: K1.ephod_inquire("ei3", w, h, 303), "#2A1A3A"),
        drawn([cp("5:20", to="and he said,"), say("5:20", frm="Jehovah hath broken", to="breach of waters."), cp("5:20", frm="Therefore he called"), caps("5:21")], "2SAM 5:20–21",
              lambda w, h: K.breach(w, h, 304), "#2A3A5A"),
        drawn([caps("5:22"), cp("5:23", to="he said,"), ("god", v("5:23", frm="Thou shalt not") + " " + v("5:24")), caps("5:25")], "2SAM 5:22–25",
              lambda w, h: K.mulberry("mb3", w, h, 305), "#14123A", head="The Tops of the Mulberry-trees"),
        over([caps("6:1-2")], "2SAM 6:1–2", "A3", 0, head="The Ark of God", stamp=6),
        over([caps("6:3-5")], "2SAM 6:3–5", "A3", 1),
        drawn([caps("6:6-7")], "2SAM 6:6–7", lambda w, h: K.nacon("nc3", w, h, 306), "#2A2A4A", head="Perez-uzzah"),
        face([caps("6:8"), cp("6:9", to="and he said,"), say("6:9", frm="How shall")], "2SAM 6:8–9", DAVID_WRATH, bg=COLD),
        drawn([caps("6:10-11"), cp("6:12", to="saying,"), say("6:12", frm="Jehovah hath blessed", to="because of the ark of God.")], "2SAM 6:10–12",
              below(lambda w, h: K.obed_edom("oe3", w, h, 307), 0.3), "#FFE680", head="The House of Obed-edom"),
        over([cp("6:12", frm="And David went"), caps("6:13")], "2SAM 6:12–13", "A3", 2),
        over([caps("6:14-15")], "2SAM 6:14–15", "A4", 0, head="David Danced before Jehovah"),
        over([caps("6:16")], "2SAM 6:16", "A4", 1),
        drawn([caps("6:17-19")], "2SAM 6:17–19", below(lambda w, h: K.tent_ark("tk3", w, h, 308), 0.36), "#FFB04A"),
        face([cp("6:20", to="and said,"), say("6:20", frm="How glorious")], "2SAM 6:20", MICHAL, bg=RED, head="Before Jehovah"),
        face([cp("6:21", to="unto Michal,"), ("say", v("6:21", frm="It was before") + " " + v("6:22"))], "2SAM 6:21–22", DAVID_KING),
        over([caps("6:23")], "2SAM 6:23", "A4", 2)]
PG.extend(pack(SEGS, "2SA-C03-D", PG.next(), end=end_mark("NEXT · FOR EVER", "right: 10px; bottom: 34px")))
