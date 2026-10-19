"""2 Chronicles volume, Chapter 11 — The Passover of Hezekiah (2 Chronicles 30–31). Every verse, word for word from ref/asv.
The letters sent from Beer-sheba even to Dan — ye children of Israel, turn again unto Jehovah (a map of the posts); laughed
to scorn, yet some humbled themselves and came; the altars cast into the Kidron; the passover in the second month — the
good Jehovah pardon every one that setteth his heart to seek God; seven days, and other seven days, with gladness: since
the time of Solomon there was not the like in Jerusalem; then the pillars broken in pieces, the courses appointed, and the
heaps of the first-fruits and the tithes — that which is left is this great store; and Hezekiah did it with all his heart."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, F, HEZEKIAH, MESSENGER, COLD, GOLDEN, RED)
from chr2 import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
AZARIAH_ZADOK = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#F3EFE6", band=True, light="#FFE680")


@P("2CH-C11-00-Title", "Chapter 11 · The Passover of Hezekiah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.feast_tents("t11", 760, 820, 1101)}</g><rect x="0" y="0" width="760" height="262" fill="#FFB04A"></rect>')
    return chapter_title(11, "第十一話", "The Passover of Hezekiah", "2 Chronicles 30 – 31", svg, "#C8702A", v("30:26", to="great joy in Jerusalem;"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("30:1-5")], "2CHR 30:1–5", below(lambda w, h: K.posts_map(w, h), 0.44), MAP, head="Turn Again unto Jehovah", stamp=30),
        face([cp("30:6", to="saying,"), say("30:6", frm="Ye children"), says("30:7")], "2CHR 30:6–7", MESSENGER),
        face([says("30:8-9")], "2CHR 30:8–9", MESSENGER),
        drawn([caps("30:10-12")], "2CHR 30:10–12", below(lambda w, h: K.posts_map(w, h, scorn=True), 0.3), MAP),
        drawn([caps("30:13-14")], "2CHR 30:13–14", below(lambda w, h: K.kidron_fire(w, h, 1102), 0.3), "#3A2A3A", head="The Feast of Unleavened Bread"),
        drawn([caps("30:15-17")], "2CHR 30:15–17", below(lambda w, h: K.altar_service("as11", w, h, 1103), 0.44), "#5A4A6A"),
        face([cp("30:18", to="saying,"), joined("say", ("30:18", "The good Jehovah"), "30:19"), caps("30:20")], "2CHR 30:18–20", HEZEKIAH, head="The Good Jehovah Pardon Every One"),
        drawn([caps("30:21-22")], "2CHR 30:21–22", below(lambda w, h: K.singers("sg11", w, h, 1104, n=8, top=0.5), 0.4), "#FFB04A"),
        drawn([caps("30:23-25")], "2CHR 30:23–25", below(lambda w, h: K.feast_tents("ft11", w, h, 1105), 0.44), "#FFB04A"),
        drawn([caps("30:26-27")], "2CHR 30:26–27", lambda w, h: K.court_scene("cs11", w, h, 1106, cloud=True), "#E8E2D6", head="Not the Like in Jerusalem")]
PG.extend(pack(SEGS, "2CH-C11-D", PG.next()))
SEGS2 = [drawn([caps("31:1")], "2CHR 31:1", below(lambda w, h: K.asa_idol("ai11", w, h, 1107), 0.4), "#3A2A3A", head="The Pillars Broken in Pieces", stamp=31),
         drawn([caps("31:2-4")], "2CHR 31:2–4", below(lambda w, h: K.opening("op11", w, h, 1108), 0.5), "#5A4A7A"),
         drawn([caps("31:5-8")], "2CHR 31:5–8", below(lambda w, h: K.heaps("hp11", w, h, 1109), 0.46), "#8FD0E2", head="Heaps"),
         face([caps("31:9"), cp("31:10", to="answered him and said,"), say("31:10", frm="Since the people")], "2CHR 31:9–10", AZARIAH_ZADOK)]
PG.extend(pack(SEGS2, "2CH-C11-E", PG.next()))
R = cells(31, 11, 19, "The Oblations and the Tithes", "#FFD23F", head="Chambers in the House of Jehovah", budget=560) + [cell("With All His Heart", "31:20-21", "#9CCB5E")]
PG.extend(roll(R, "2CH-C11-R", PG.next(), "THE OBLATIONS AND THE TITHES · 2 CHRONICLES 31", end=end_mark("NEXT · SENNACHERIB", "right: 40px; bottom: 50px")))
