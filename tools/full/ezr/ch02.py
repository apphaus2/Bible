"""Ezra volume, Chapter 2 — The Foundation of the House (Ezra 3–4). Every verse, word for word from ref/eng-asv.
The people gathered as one man in the seventh month; the altar set upon its base, for fear was upon them; the feast of
tabernacles; cedars from Lebanon to Joppa; the foundation laid in the second year — for he is good; the shout of joy and the
weeping of the old men that had seen the first house, so that the people could not discern the noise; then the adversaries —
let us build with you; ye have nothing to do with us; the letter of Rehum and Shimshai to Artaxerxes and the king's answer
(sealed scrolls, the words in speech boxes); and the work ceased by force and power."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from faces_ex import F
from ezr import G, art as K
from ezr.common import pack, cp, say, sg, caps, says, drawn, face, joined, cell, cells, roll, ZERUBBABEL, JESHUA, ELDER, ARTAXERXES, PERSIAN, COLD, GOLDEN, RED
from ezr import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
ADVERSARY = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A6A3A", cord=True, brow="scowl", light="#D7261E")
REHUM = PERSIAN


@P("EZR-C02-00-Title", "Chapter 2 · The Foundation of the House", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.altar_ruins("t2", 760, 820, 201, foundation=True, weep=True)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(2, "第二話", "The Foundation of the House", "Ezra 3 – 4", svg, "#3A5A7A", v("3:11", frm="And all the people shouted"), "Ezra · Volume Fifteen")


SEGS = [drawn([caps("3:1-3")], "EZRA 3:1–3", below(lambda w, h: K.altar_ruins("ar2", w, h, 202), 0.4), "#8FD0E2", head="As One Man", stamp=3),
        drawn([caps("3:4-6")], "EZRA 3:4–6", below(lambda w, h: K.feast_tents("ft2", w, h, 203), 0.4), "#FFB04A"),
        drawn([caps("3:7")], "EZRA 3:7", below(lambda w, h: K.lebanon("lb2", w, h, 204, rafts=True), 0.3), "#8FD0E2"),
        face([caps("3:8-9")], "EZRA 3:8–9", ZERUBBABEL, head="The Foundation Laid"),
        drawn([caps("3:10"), cp("3:11", to="saying,"), say("3:11", frm="For he is good,", to="toward Israel."), cp("3:11", frm="And all the people")], "EZRA 3:10–11",
              below(lambda w, h: K.altar_ruins("ar2b", w, h, 205, foundation=True), 0.44), "#8FD0E2"),
        face([caps("3:12-13")], "EZRA 3:12–13", ELDER, bg=COLD, head="The Noise of the Weeping")]
PG.extend(pack(SEGS, "EZR-C02-D", PG.next()))
SEGS2 = [face([caps("4:1"), cp("4:2", to="and said unto them,"), say("4:2", frm="Let us build")], "EZRA 4:1–2", ADVERSARY, bg=RED, head="The Adversaries", stamp=4),
         face([cp("4:3", to="said unto them,"), say("4:3", frm="Ye have nothing"), caps("4:4-5")], "EZRA 4:3–5", ZERUBBABEL),
         drawn([caps("4:6-10")], "EZRA 4:6–10", below(lambda w, h: K.letter_scroll(w, h, 206), 0.44), "#2A1A2A", h=330)]
PG.extend(pack(SEGS2, "EZR-C02-E", PG.next(), by_need=False, min_size=None, budget=2400))
SEGS3 = [face([cp("4:11", to="unto Artaxerxes the king:"), say("4:11", frm="Thy servants"), says("4:12-13")], "EZRA 4:11–13", REHUM, bg=RED),
         face([says("4:14-16")], "EZRA 4:14–16", REHUM, bg=RED),
         drawn([cp("4:17", to="beyond the River:"), say("4:17", frm="Peace,"), says("4:18-19")], "EZRA 4:17–19", below(lambda w, h: K.letter_scroll(w, h, 207), 0.44), "#2A1A2A"),
         face([says("4:20-22")], "EZRA 4:20–22", ARTAXERXES),
         drawn([caps("4:23-24")], "EZRA 4:23–24", below(lambda w, h: K.work_ceased("wc2", w, h, 208), 0.3), "#6A6A8A", h=380)]
PG.extend(pack(SEGS3, "EZR-C02-F", PG.next(), default_head="The Letter to Artaxerxes", end=end_mark("NEXT · THE HOUSE FINISHED", "right: 10px; bottom: 34px")))
