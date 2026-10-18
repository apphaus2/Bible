"""1 Kings volume, Chapter 7 — The Queen of Sheba (1 Kings 9–10). Every verse, word for word from ref/asv.
Jehovah appearing to Solomon the second time — I have hallowed this house; but if ye shall turn away (the Voice box); the
cities of Cabul; the levy and the cities Solomon built (a technical map); the navy at Ezion-geber and the gold of Ophir. Then
the queen of Sheba with her very great train — the half was not told me; the almug-trees; the bucklers of beaten gold; the
throne of ivory with its twelve lions; the navy of Tarshish; silver as stones in Jerusalem; horses out of Egypt."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import art as K2
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, SOLOMON, HIRAM, SHEBA, RED, COLD, GOLDEN)
from kg1 import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK, MAP = "#0B1A2E", "#0B1A2E"


@P("1KI-C07-00-Title", "Chapter 7 · The Queen of Sheba", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFB04A"></rect><g transform="translate(0 340)">{K.sheba_train("t7", 760, 740, 701)}</g>')
    return chapter_title(7, "第七話", "The Queen of Sheba", "1 Kings 9 – 10", svg, "#C8702A", v("10:7", frm="behold, the half"), "1 Kings · Volume Eleven")


SEGS = [drawn([caps("9:1-2"), cp("9:3", to="said unto him,"), gd("9:3", frm="I have heard")], "1KGS 9:1–3", lambda w, h: K.dream("dr7", w, h, 702), "#0F0E2A", head="The Second Time", stamp=9),
        drawn([gods("9:4-5")], "1KGS 9:4–5", lambda w, h: K2.throne_glory(w, h, 703), "#14123A"),
        drawn([gods("9:6-7")], "1KGS 9:6–7", lambda w, h: K.court_scene("cs7", w, h, 704, crowd=False), "#8FD0E2"),
        drawn([gods("9:8-9")], "1KGS 9:8–9", lambda w, h: K2.rabbah("rb7", w, h, 705, camp=False, dusk=True), "#3A1A2A"),
        drawn([caps("9:10-12")], "1KGS 9:10–12", below(lambda w, h: K.cabul("cb7", w, h, 706), 0.36), "#C8C0B0", head="The Land of Cabul"),
        face([cp("9:13", to="And he said,"), say("9:13", frm="What cities"), cp("9:13", frm="And he called"), caps("9:14")], "1KGS 9:13–14", HIRAM),
        drawn([caps("9:15-19")], "1KGS 9:15–19", below(lambda w, h: K.cities_map(w, h), 0.36), MAP, head="The Levy"),
        drawn([caps("9:20-23")], "1KGS 9:20–23", below(lambda w, h: K.hewers("hw7", w, h, 707), 0.36), "#E8C8A0"),
        drawn([caps("9:24-25")], "1KGS 9:24–25", below(lambda w, h: K.court_scene("sm7", w, h, 708, smoke=True), 0.3), "#8FD0E2"),
        drawn([caps("9:26-28")], "1KGS 9:26–28", below(lambda w, h: K.navy("nv7", w, h, 709), 0.26), "#8FD0E2", head="The Gold of Ophir"),
        drawn([caps("10:1-3")], "1KGS 10:1–3", below(lambda w, h: K.sheba_train("st7", w, h, 710), 0.3), "#FFB04A", head="The Queen of Sheba", stamp=10),
        drawn([caps("10:4-5")], "1KGS 10:4–5", below(lambda w, h: K.sheba_court("sc7", w, h, 711), 0.26), "#5A2A1E"),
        face([cp("10:6", to="to the king,"), joined("say", ("10:6", "It was a true"), "10:7")], "1KGS 10:6–7", SHEBA, head="The Half Was Not Told Me"),
        face([says("10:8-9")], "1KGS 10:8–9", SHEBA),
        drawn([caps("10:10")], "1KGS 10:10", below(lambda w, h: K.sheba_court("sc7b", w, h, 712), 0.2), "#5A2A1E"),
        drawn([caps("10:11-12")], "1KGS 10:11–12", below(lambda w, h: K.navy("nv7b", w, h, 713, port=False), 0.3), "#8FD0E2"),
        drawn([caps("10:13")], "1KGS 10:13", lambda w, h: K.sheba_train("st7b", w, h, 714), "#FFB04A"),
        drawn([caps("10:14-17")], "1KGS 10:14–17", below(lambda w, h: K.gold_shields_king(w, h, 715), 0.36), "#3A2214", head="Six Hundred Threescore and Six Talents"),
        drawn([caps("10:18-20")], "1KGS 10:18–20", below(lambda w, h: K.ivory_throne(w, h), 0.24), INK, head="The Throne of Ivory"),
        drawn([caps("10:21-22")], "1KGS 10:21–22", below(lambda w, h: K.tarshish("ts7", w, h, 716), 0.28), "#8FD0E2"),
        drawn([caps("10:23-25")], "1KGS 10:23–25", below(lambda w, h: K.tribute("tb7", w, h, 717), 0.26), "#FFE680"),
        drawn([caps("10:26-29")], "1KGS 10:26–29", below(lambda w, h: K.stalls("st7c", w, h, 718), 0.2), "#E8C8A0")]
PG.extend(pack(SEGS, "1KI-C07-D", PG.next(), end=end_mark("NEXT · HIS HEART TURNED AWAY", "right: 10px; bottom: 34px")))
