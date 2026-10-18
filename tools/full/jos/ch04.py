"""Joshua volume, Chapter 4 — Ai and the Gibeonites (Joshua 8–9). Every verse, word for word from ref/asv.
The ambush behind the city laid out as a technical map; the feigned flight and the javelin stretched out toward Ai; the city
set on fire (the slaughter of 8:21–26 and the king of Ai in 8:29 are words over the smoke and the heap: nothing of it
drawn); the altar of unhewn stones in mount Ebal and the law read before Gerizim and Ebal; then the Gibeonites with their
mouldy bread and rent wine-skins, the covenant made without asking counsel of Jehovah, and the hewers of wood and drawers
of water."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from deu import art as DA
from genesis.ch03 import hud
from genesis.ch04 import COLD
from genesis.ch07 import RED
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, GIBEONITE, ELEAZAR
from jos import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("JOS-C04-00-Title", "Chapter 4 · Ai and the Gibeonites", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3B86A"></rect><g transform="translate(0 380)">{K.javelin("t4", 760, 700, 401)}</g>')
    return chapter_title(4, "第四話", "Ai and the Gibeonites", "Joshua 8 – 9", svg, "#F3B86A", v("8:18", frm="Stretch out the javelin", to="toward Ai;"), "Joshua · Volume Six")


SEGS = [face([cp("8:1", to="unto Joshua,"), gd("8:1", frm="Fear not,"), gd("8:2")], "JOSH 8:1–2", "awe", head="Set Thee an Ambush", stamp=8),
        drawn([caps("8:3"), cp("8:4", to="saying,"), ("say", v("8:4", frm="Behold,") + " " + sp("8:5-8"))], "JOSH 8:3–8", K.below(lambda w, h: K.ai_plan(w, h), 0.56), MAP),
        drawn([caps("8:9-13")], "JOSH 8:9–13", K.below(lambda w, h: K.ai_plan(w, h), 0.3), MAP),
        drawn([caps("8:14-17")], "JOSH 8:14–17", K.below(lambda w, h: K.ai_plan(w, h, stage=1), 0.36), MAP, head="They Left the City Open"),
        drawn([cp("8:18", to="unto Joshua,"), gd("8:18", frm="Stretch out", to="into thy hand."), cp("8:18", frm="And Joshua stretched")], "JOSH 8:18",
              lambda w, h: K.javelin("jv4", w, h, 411), "#F3B86A"),
        drawn([caps("8:19-22")], "JOSH 8:19–22", lambda w, h: K.burning(w, h, 412, city="ai"), "#2A0A0A", head="The Smoke of the City"),
        drawn([caps("8:23-27")], "JOSH 8:23–27", lambda w, h: K.burning(w, h, 413, city="ai"), "#2A0A0A", extra=hud("12,000", "left: 14px; bottom: 14px", size=20)),
        drawn([caps("8:28-29")], "JOSH 8:28–29", lambda w, h: K.ruin_heap(w, h, 414), "#4A2A3A"),
        drawn([caps("8:30-32")], "JOSH 8:30–32", lambda w, h: DA.stones_written(w, h, 415), "#E8C8A0", head="An Altar in Mount Ebal"),
        drawn([caps("8:33-35")], "JOSH 8:33–35", lambda w, h: DA.gerizim_ebal(w, h, 416), "#F3D8A0"),
        drawn([caps("9:1-2")], "JOSH 9:1–2", lambda w, h: K.kings_afar("ka4", w, h, 417), "#3A1A2E", head="They Did Work Wilily", stamp=9),
        drawn([caps("9:3-5")], "JOSH 9:3–5", lambda w, h: K.gibeonites("gb4", w, h, 418), "#E8C88A"),
        face([cp("9:6", to="to the men of Israel,"), say("9:6", frm="We are come"), cp("9:7", to="unto the Hivites,"), say("9:7", frm="Peradventure")], "JOSH 9:6–7", GIBEONITE),
        face([cp("9:8", to="And they said unto Joshua,"), say("9:8", frm="We are thy servants.", to="We are thy servants."), cp("9:8", frm="And Joshua said unto them,", to="And Joshua said unto them,"), say("9:8", frm="Who are ye?")],
             "JOSH 9:8", "calm"),
        face([cp("9:9", to="said unto him,"), ("say", v("9:9", frm="From a very") + " " + sp("9:10-13"))], "JOSH 9:9–13", GIBEONITE, bg=COLD),
        drawn([caps("9:14-15")], "JOSH 9:14–15", lambda w, h: K.provision(w, h, 419), "#3A2A1E"),
        drawn([caps("9:16-18")], "JOSH 9:16–18", K.below(lambda w, h: K.four_cities(w, h), 0.4), MAP, head="Let Them Live"),
        face([cp("9:19", to="unto all the congregation,"), ("say", v("9:19", frm="We have sworn") + " " + v("9:20")), cp("9:21", to="said unto them,"),
              say("9:21", frm="Let them live:", to="Let them live:"), cp("9:21", frm="so they became")], "JOSH 9:19–21", ELEAZAR),
        face([cp("9:22", to="saying,"), ("say", v("9:22", frm="Wherefore") + " " + v("9:23"))], "JOSH 9:22–23", "lead"),
        face([cp("9:24", to="and said,"), ("say", v("9:24", frm="Because it was") + " " + v("9:25"))], "JOSH 9:24–25", GIBEONITE, bg=RED),
        drawn([caps("9:26-27")], "JOSH 9:26–27", lambda w, h: K.hewers("hw4", w, h, 420), "#F3D8A0")]
PG.extend(pack(SEGS, "JOS-C04-D", PG.next(), end=end_mark("NEXT · THE SUN STOOD STILL", "right: 10px; bottom: 34px")))
