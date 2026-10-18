"""Joshua volume, Chapter 6 — The Land That Remaineth (Joshua 12–14). Every verse, word for word from ref/asv.
The kings smitten beyond the Jordan (a map), then the thirty and one kings west of the Jordan as a roll page of cells,
two kings to a cell as the verses give them; Jehovah's word to Joshua, old and well stricken in years, and the land that yet
remaineth (a map); the inheritance of Reuben, Gad and the half-tribe of Manasseh beyond the Jordan as roll cells; the lot
by Eleazar and Joshua; and Caleb, fourscore and five years old: give me this hill-country — Hebron."""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages
from deu.common import shade
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, CALEB_OLD
from jos import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("JOS-C06-00-Title", "Chapter 6 · The Land That Remaineth", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(0 300)">{K.land_taken(760, 780)}</g>')
    return chapter_title(6, "第六話", "The Land That Remaineth", "Joshua 12 – 14", svg, "#0B1A2E", v("13:1", frm="there remaineth yet"), "Joshua · Volume Six")


SEGS = [drawn([caps("12:1-3")], "JOSH 12:1–3", K.below(lambda w, h: K.east_map(w, h), 0.3), MAP, head="The Kings of the Land", stamp=12),
        drawn([caps("12:4-6")], "JOSH 12:4–6", K.below(lambda w, h: K.east_map(w, h), 0.26), MAP),
        drawn([caps("12:7-8")], "JOSH 12:7–8", K.below(lambda w, h: K.land_taken(w, h), 0.3), MAP)]
PG.extend(pack(SEGS, "JOS-C06-D", PG.next()))

def kings(ref):
    return " · ".join(re.findall(r"king of ([A-Z][\w-]+)", v(ref)))
KINGS = [(kings(f"12:{n}"), v(f"12:{n}"), f"JOSH 12:{n}", "#FFD23F" if n % 2 else "#FF8A3D", "All the Kings Thirty and One" if n == 9 else None) for n in range(9, 25)]
PG.extend(roll_pages(KINGS, "JOS-C06-K", PG.next(), "Joshua", "JOSH", tag="THE KINGS WEST OF THE JORDAN · JOSHUA 12", ncol=2, most=16))

SEGS2 = [face([cp("13:1", to="said unto him,"), gd("13:1", frm="Thou art old"), gods("13:2-4")], "JOSH 13:1–4", "old", head="There Remaineth Yet Very Much Land", stamp=13),
         drawn([gods("13:5-7")], "JOSH 13:5–7", K.below(lambda w, h: K.remaineth_map(w, h), 0.32), MAP)]
PG.extend(pack(SEGS2, "JOS-C06-E", PG.next()))

R, GD, MA, LV, X = "#FF6A5A", "#FFB04A", "#B8B8E0", "#FF8A3D", "#8FD0E2"
EAST = [("Beyond the Jordan", sp("13:8-12"), "JOSH 13:8–12", X, "Beyond the Jordan Eastward"),
        ("Geshur · Maacath", v("13:13"), "JOSH 13:13", X, None),
        ("Levi", v("13:14"), "JOSH 13:14", LV, None),
        ("Reuben", sp("13:15-20"), "JOSH 13:15–20", R, None),
        ("Reuben", sp("13:21-23"), "JOSH 13:21–23", R, None),
        ("Gad", sp("13:24-28"), "JOSH 13:24–28", GD, None),
        ("Half Manasseh", sp("13:29-31"), "JOSH 13:29–31", MA, None),
        ("Beyond the Jordan", v("13:32"), "JOSH 13:32", X, None),
        ("Levi", v("13:33"), "JOSH 13:33", LV, None)]
PG.extend(roll_pages(EAST, "JOS-C06-R", PG.next(), "Joshua", "JOSH", tag="THE INHERITANCE BEYOND THE JORDAN · JOSHUA 13"))

SEGS3 = [drawn([caps("14:1-5")], "JOSH 14:1–5", lambda w, h: K.gilgal("gg6", w, h, 611), "#F3D8A0", head="Give Me This Hill-country", stamp=14),
         face([cp("14:6", to="said unto him,"), ("say", v("14:6", frm="Thou knowest") + " " + sp("14:7-9"))], "JOSH 14:6–9", CALEB_OLD),
         face([says("14:10-12")], "JOSH 14:10–12", CALEB_OLD),
         drawn([caps("14:13-15")], "JOSH 14:13–15", lambda w, h: K.hebron("hb6", w, h, 612), "#F3D8A0")]
PG.extend(pack(SEGS3, "JOS-C06-F", PG.next(), end=end_mark("NEXT · THE LOT OF JUDAH", "right: 10px; bottom: 34px")))
