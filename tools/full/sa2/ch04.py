"""2 Samuel volume, Chapter 4 — For Ever (2 Samuel 7–8). Every verse, word for word from
ref/asv. I dwell in a house of cedar, but the ark of God dwelleth within curtains; the word of Jehovah to Nathan by night (the
Voice box) — I took thee from the sheepcote; he shall build a house for my name; I will be his father; David sitting before
Jehovah — who am I, O Lord Jehovah?; then David's wars as a technical map (8:2 words over Moab on the map), the shields
of gold, Toi's vessels dedicated unto Jehovah, and the officers of the kingdom."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, DAVID_KING, NATHAN, RED, COLD, GOLDEN)
from sa2 import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2SA-C04-00-Title", "Chapter 4 · For Ever", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 320)">{K.throne_glory(760, 760, 401)}</g>')
    return chapter_title(4, "第四話", "For Ever", "2 Samuel 7 – 8", svg, "#14123A", v("7:13"), "2 Samuel · Volume Ten")


SEGS = [over([caps("7:1"), cp("7:2", to="the prophet,"), say("7:2", frm="See now,")], "2SAM 7:1–2", "A5", 0, head="A House of Cedar", stamp=7),
        face([cp("7:3", to="to the king,"), say("7:3", frm="Go, do")], "2SAM 7:3", NATHAN),
        drawn([caps("7:4"), gods("7:5-7")], "2SAM 7:4–7", lambda w, h: K.nathan_night(w, h, 402), "#0F0E2A", head="The Word of Jehovah Came unto Nathan"),
        over([gods("7:8-10")], "2SAM 7:8–10", "A5", 1),
        drawn([gods("7:11-13")], "2SAM 7:11–13", lambda w, h: K.throne_glory(w, h, 403), "#14123A"),
        over([gods("7:14-16")], "2SAM 7:14–16", "A5", 1, align="xMidYMax"),
        face([caps("7:17")], "2SAM 7:17", NATHAN),
        over([cp("7:18", to="and he said,"), ("say", v("7:18", frm="Who am I,") + " " + v("7:19"))], "2SAM 7:18–19", "A5", 2, head="Who Am I, O Lord Jehovah?"),
        face([says("7:20-22")], "2SAM 7:20–22", DAVID_KING),
        drawn([says("7:23-24")], "2SAM 7:23–24", lambda w, h: K.prayer("pr4", w, h, 404), "#3A1A2A"),
        face([says("7:25-27")], "2SAM 7:25–27", DAVID_KING),
        drawn([says("7:28-29")], "2SAM 7:28–29", lambda w, h: K.prayer("pr4b", w, h, 405), "#3A1A2A"),
        drawn([caps("8:1-2")], "2SAM 8:1–2", below(lambda w, h: K.wars_map(w, h, hi=("GATH", "MOAB")), 0.3), MAP, head="Jehovah Gave Victory to David", stamp=8),
        drawn([caps("8:3-6")], "2SAM 8:3–6", below(lambda w, h: K.wars_map(w, h, hi=("ZOBAH", "DAMASCUS")), 0.36), MAP),
        drawn([caps("8:7-8")], "2SAM 8:7–8", lambda w, h: K.gold_shields(w, h, 406), "#3A2214"),
        drawn([caps("8:9-12")], "2SAM 8:9–12", lambda w, h: K.vessels(w, h, 407), "#2A1A3A"),
        drawn([caps("8:13-14")], "2SAM 8:13–14", below(lambda w, h: K.wars_map(w, h, hi=("VALLEY OF SALT",)), 0.2), MAP),
        drawn([caps("8:15-18")], "2SAM 8:15–18", below(lambda w, h: K.court("ct4", w, h, 408), 0.3), "#5A2A1E", head="Justice and Righteousness")]
PG.extend(pack(SEGS, "2SA-C04-D", PG.next(), end=end_mark("NEXT · MEPHIBOSHETH", "right: 10px; bottom: 34px")))
