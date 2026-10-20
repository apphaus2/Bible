"""2 Chronicles volume, Chapter 12 — Sennacherib (2 Chronicles 32). Every verse, word for word from ref/eng-asv.
Sennacherib come into Judah; the fountains stopped — why should the kings of Assyria come, and find much water? (a plan);
the wall built up; be strong and of good courage, with him is an arm of flesh; Sennacherib's servants before the wall —
whereon do ye trust? (2 Kings' upper pool); the letters railing on Jehovah; Hezekiah and Isaiah crying to heaven; the angel
and the camp of the king of Assyria (32:21 words over the silent camp and Nineveh); Hezekiah sick and humbled; his riches and
store-houses; the upper spring of Gihon brought straight down; the ambassadors of Babylon — God left him, to try him."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, HEZEKIAH, HEZEKIAH_GRIEF, HEZEKIAH_SICK, RABSHAKEH, ISAIAH, ISRAELITE, COLD, GOLDEN, RED)
from chr2 import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK, MAP = "#0B1A2E", "#0B1A2E"


@P("2CH-C12-00-Title", "Chapter 12 · Sennacherib", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.upper_pool("t12", 760, 820, 1201)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(12, "第十二話", "Sennacherib", "2 Chronicles 32", svg, "#3A5A7A", v("32:8", to="our battles."), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("32:1-3")], "2CHR 32:1–3", below(lambda w, h: K.assyria_map(w, h, arrows=(("NINEVEH", "SAMARIA"),)), 0.3), MAP, head="Sennacherib King of Assyria", stamp=32),
        drawn([cp("32:4", to="saying,"), say("32:4", frm="Why should")], "2CHR 32:4", below(lambda w, h: K.stopped_springs(w, h), 0.2), INK),
        drawn([caps("32:5")], "2CHR 32:5", below(lambda w, h: K.towers_engines(w, h, 1202), 0.24), INK),
        face([caps("32:6"), joined("say", "32:7", ("32:8", "with him", "to fight our battles.")), cp("32:8", frm="And the people rested")], "2CHR 32:6–8", HEZEKIAH,
             head="With Us Is Jehovah Our God"),
        drawn([cp("32:9", to="saying,"), say("32:10", to="Thus saith Sennacherib king of Assyria,"), say("32:10", frm="Whereon")], "2CHR 32:9–10",
              below(lambda w, h: K.upper_pool("up12", w, h, 1203), 0.36), "#8FD0E2", head="Whereon Do Ye Trust?"),
        face([says("32:11-12")], "2CHR 32:11–12", RABSHAKEH, bg=RED),
        face([says("32:13-15")], "2CHR 32:13–15", RABSHAKEH, bg=RED),
        drawn([caps("32:16"), cp("32:17", to="saying,"), say("32:17", frm="As the gods")], "2CHR 32:16–17", below(lambda w, h: K.letter_spread("ls12", w, h, 1204), 0.4), "#5A3A2A"),
        drawn([caps("32:18-19")], "2CHR 32:18–19", below(lambda w, h: K.upper_pool("up12b", w, h, 1205), 0.3), "#8FD0E2"),
        face([caps("32:20")], "2CHR 32:20", ISAIAH, bg="#14123A", head="They Cried to Heaven"),
        drawn([caps("32:21")], "2CHR 32:21", below(lambda w, h: K.silent_camp("sc12", w, h, 1206), 0.36), "#8A8AA8"),
        drawn([caps("32:22-23")], "2CHR 32:22–23", below(lambda w, h: K.tribute("tb12", w, h, 1207), 0.3), "#FFE680")]
PG.extend(pack(SEGS, "2CH-C12-D", PG.next()))
SEGS2 = [face([caps("32:24-26")], "2CHR 32:24–26", HEZEKIAH_SICK, bg=COLD, head="Sick Even unto Death"),
         drawn([caps("32:27-29")], "2CHR 32:27–29", below(lambda w, h: K.stores(w, h, 1208), 0.4), "#3A2A1A", head="Exceeding Much Riches"),
         drawn([caps("32:30")], "2CHR 32:30", below(lambda w, h: K.stopped_springs(w, h, upper=True), 0.2), INK, head="The Upper Spring of Gihon"),
         drawn([caps("32:31")], "2CHR 32:31", below(lambda w, h: K.treasures("tr12b", w, h, 1209), 0.24), "#5A2A1E"),
         face([caps("32:32-33")], "2CHR 32:32–33", HEZEKIAH, bg=COLD)]
PG.extend(pack(SEGS2, "2CH-C12-E", PG.next(), end=end_mark("NEXT · MANASSEH AND JOSIAH", "right: 10px; bottom: 34px")))
