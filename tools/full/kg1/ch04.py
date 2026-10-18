"""1 Kings volume, Chapter 4 — The House of Jehovah (1 Kings 5–6). Every verse, word for word from ref/asv.
Hiram king of Tyre and Solomon's message — I purpose to build a house for the name of Jehovah my God; cedar and fir out of
Lebanon, floated in rafts by sea; the levy and the hewers; great stones, costly stones. Then the house as blueprint plates:
the elevation and the plan, the side-chambers in section, stone made ready at the quarry, the word of Jehovah to Solomon
(the Voice box), cedar within carved with knops and open flowers, the oracle overlaid with pure gold, the two cherubim, the
doors of olive-wood and of fir, the inner court, and seven years in building."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import art as K2
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, SOLOMON, HIRAM, RED, COLD, GOLDEN)
from kg1 import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = "#0B1A2E"
def plate(lines, ref, fn, k=0.34, **kw): return drawn(lines, ref, below(fn, k), INK, **kw)


@P("1KI-C04-00-Title", "Chapter 4 · The House of Jehovah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(0 300)">{K.temple_elev(760, 780)}</g>')
    return chapter_title(4, "第四話", "The House of Jehovah", "1 Kings 5 – 6", svg, "#0B1A2E", v("6:14"), "1 Kings · Volume Eleven")


SEGS = [face([caps("5:1"), cp("5:2"), joined("say", "5:3", "5:4")], "1KGS 5:1–4", SOLOMON, head="Hiram King of Tyre", stamp=5),
        face([says("5:5-6")], "1KGS 5:5–6", SOLOMON),
        face([cp("5:7", to="and said,"), say("5:7", frm="Blessed be"), cp("5:8", to="saying,"), joined("say", ("5:8", "I have heard"), "5:9")], "1KGS 5:7–9", HIRAM),
        drawn([caps("5:10-12")], "1KGS 5:10–12", lambda w, h: K.lebanon("lb4", w, h, 401, rafts=True), "#1F6F9A", head="Cedar out of Lebanon"),
        drawn([caps("5:13-14")], "1KGS 5:13–14", below(lambda w, h: K.lebanon("lb4b", w, h, 402), 0.2), "#8FD0E2"),
        drawn([caps("5:15-18")], "1KGS 5:15–18", below(lambda w, h: K.hewers("hw4", w, h, 403), 0.28), "#E8C8A0"),
        plate([caps("6:1-3")], "1KGS 6:1–3", lambda w, h: K.temple_elev(w, h), k=0.26, head="The House of Jehovah", stamp=6),
        plate([caps("6:4-6")], "1KGS 6:4–6", lambda w, h: K.stories(w, h), k=0.3),
        plate([caps("6:7-8")], "1KGS 6:7–8", lambda w, h: K.no_tool(w, h), k=0.28),
        plate([caps("6:9-10")], "1KGS 6:9–10", lambda w, h: K.temple_plan(w, h), k=0.22),
        drawn([cp("6:11"), gods("6:12-13")], "1KGS 6:11–13", lambda w, h: K2.throne_glory(w, h, 404), "#14123A", head="The Word of Jehovah Came to Solomon"),
        plate([caps("6:14-15")], "1KGS 6:14–15", lambda w, h: K.cedar_within(w, h), k=0.3),
        plate([caps("6:16-19")], "1KGS 6:16–19", lambda w, h: K.temple_plan(w, h, oracle=True), k=0.36, head="The Oracle"),
        plate([caps("6:20-22")], "1KGS 6:20–22", lambda w, h: K.cedar_within(w, h, gold=True), k=0.36),
        plate([caps("6:23-26")], "1KGS 6:23–26", lambda w, h: K.cherubim(w, h), k=0.34, head="The Cherubim"),
        plate([caps("6:27-30")], "1KGS 6:27–30", lambda w, h: K.cherubim(w, h), k=0.38),
        plate([caps("6:31-32")], "1KGS 6:31–32", lambda w, h: K.doors(w, h), k=0.3, head="The Doors"),
        plate([caps("6:33-35")], "1KGS 6:33–35", lambda w, h: K.doors(w, h, folding=True), k=0.28),
        plate([caps("6:36")], "1KGS 6:36", lambda w, h: K.inner_court(w, h), k=0.2),
        plate([caps("6:37-38")], "1KGS 6:37–38", lambda w, h: K.years(w, h), k=0.3)]
PG.extend(pack(SEGS, "1KI-C04-D", PG.next(), end=end_mark("NEXT · THE PILLARS AND THE SEA", "right: 10px; bottom: 34px")))
