"""Joshua volume, Chapter 10 — Choose You This Day (Joshua 23–24), the last chapter of Joshua. Every verse, word for word
from ref/asv. Joshua old and well stricken in years: one man of you shall chase a thousand; I am going the way of all the
earth. At Shechem: Thus saith Jehovah — the fathers beyond the River, Egypt and the sea, Balaam, Jericho, the hornet, a land
whereon thou hadst not labored (Jehovah's words in Voice boxes over a journey map and the old drawings); choose you this day
whom ye will serve; the people's answer, the great stone under the oak; and the deaths of Joshua and Eleazar and the bones
of Joseph buried in Shechem (captions over the hill-country of Ephraim: no grave drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from num.pages import Pages
from num import art11 as N11
from num.art import ALL
from deu.common import shade
from exo import art4 as A4
from genesis import art as X, art3 as Z, art11 as GA
from genesis.ch04 import COLD
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D
from jos import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("JOS-C10-00-Title", "Chapter 10 · Choose You This Day", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect><g transform="translate(0 340)">{K.shechem("t10", 760, 740, 1001)}</g>')
    return chapter_title(10, "第十話", "Choose You This Day", "Joshua 23 – 24", svg, "#F3D8A0", v("24:15", frm="but as for me and my house,"), "Joshua · Volume Six")


SEGS = [face([caps("23:1"), cp("23:2", to="and said unto them,"), ("say", v("23:2", frm="I am old") + " " + sp("23:3-5"))], "JOSH 23:1–5", "old",
             head="I Am Old and Well Stricken in Years", stamp=23),
        face([says("23:6-10")], "JOSH 23:6–10", "old"),
        face([says("23:11-13")], "JOSH 23:11–13", "old"),
        face([says("23:14-16")], "JOSH 23:14–16", "old", head="The Way of All the Earth"),
        drawn([caps("24:1")], "JOSH 24:1", lambda w, h: K.shechem("sc10", w, h, 1011, stone=False), "#F3D8A0", head="Thus Saith Jehovah", stamp=24),
        drawn([cp("24:2", to="Thus saith Jehovah, the God of Israel,"), gd("24:2", frm="Your fathers"), gods("24:3-4")], "JOSH 24:2–4",
              K.below(lambda w, h: Z.journey_map(w, h, 1012, ["UR", "HARAN", "SHECHEM", "BETH-EL", "THE SOUTH", "EGYPT"], cur="EGYPT"), 0.4), MAP),
        drawn([gods("24:5-7")], "JOSH 24:5–7", lambda w, h: A4.sunk(w, h, 1013), "#0F4C68"),
        drawn([gods("24:8-10")], "JOSH 24:8–10", lambda w, h: mk.defs("bh10", *ALL) + N11.bare_height("bh10", w, h, 1014), "#2A2458"),
        drawn([gods("24:11-12")], "JOSH 24:11–12", lambda w, h: K.hornet(w, h, 1015), "#E8B880"),
        drawn([gods("24:13")], "JOSH 24:13", lambda w, h: K.vineyards(w, h, 1016), "#8FD0E2"),
        over([says("24:14-15")], "JOSH 24:14–15", "P08", 1, head="Choose You This Day"),
        drawn([cp("24:16", to="answered and said,"), ("say", v("24:16", frm="Far be it") + " " + sp("24:17-18"))], "JOSH 24:16–18",
              lambda w, h: K.shechem("sc10b", w, h, 1017, stone=False, joshua=False), "#F3D8A0"),
        face([cp("24:19", to="unto the people,"), ("say", v("24:19", frm="Ye cannot") + " " + v("24:20"))], "JOSH 24:19–20", "old"),
        face([cp("24:21", to="unto Joshua,"), say("24:21", frm="Nay;"), cp("24:22", to="unto the people,"), say("24:22", frm="Ye are witnesses", to="to serve him."),
              cp("24:22", frm="And they said,", to="And they said,"), say("24:22", frm="We are witnesses."), say("24:23", frm="Now therefore put away,", to="Now therefore put away,"),
              cp("24:23", frm="said he,", to="said he,"), say("24:23", frm="the foreign gods")], "JOSH 24:21–23", "old", head="Ye Are Witnesses"),
        drawn([cp("24:24", to="unto Joshua,"), say("24:24", frm="Jehovah our God"), caps("24:25-26")], "JOSH 24:24–26", lambda w, h: K.shechem("sc10c", w, h, 1018), "#F3D8A0"),
        face([cp("24:27", to="unto all the people,"), say("24:27", frm="Behold,"), caps("24:28")], "JOSH 24:27–28", "old", head="This Stone Shall Be a Witness"),
        drawn([caps("24:29-31")], "JOSH 24:29–31", lambda w, h: K.timnath("tm10", w, h, 1019, figure=False), "#F3D8A0", head="A Hundred and Ten Years Old"),
        drawn([caps("24:32-33")], "JOSH 24:32–33", lambda w, h: K.three_graves(w, h, 1020), "#3A2A4A")]
PG.extend(pack(SEGS, "JOS-C10-D", PG.next(), end=end_mark("END OF JOSHUA · NEXT · JUDGES", "right: 10px; bottom: 34px", ch="完")))
