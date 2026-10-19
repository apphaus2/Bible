"""Ezra volume, Chapter 3 — The House Finished (Ezra 5–6). Every verse, word for word from ref/asv.
Haggai and Zechariah prophesying; Zerubbabel and Jeshua build again; Tattenai — who gave you a decree?; but the eye of their
God was upon the elders; Tattenai's letter to Darius with the elders' answer — we are the servants of the God of heaven and
earth; the roll found at Achmetha, the decree of Cyrus with the measures of the house; Darius's decree — let the work of this
house of God alone (6:11 words only); the house finished in the sixth year of Darius; the dedication with joy; and the
passover of the children of the captivity."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from ezr import G, art as K
from ezr.common import (pack, cp, say, caps, says, drawn, face, joined, cell, cells, roll, ZERUBBABEL, JESHUA, HAGGAI, ZECHARIAH, TATTENAI, DARIUS, ELDER, COLD, GOLDEN, RED)
from ezr import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BOARD = "#1A1430"


@P("EZR-C03-00-Title", "Chapter 3 · The House Finished", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.court_scene("t3", 760, 820, 301, smoke=True)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(3, "第三話", "The House Finished", "Ezra 5 – 6", svg, "#3A5A7A", v("6:16", frm="kept the dedication"), "Ezra · Volume Fifteen")


SEGS = [face([caps("5:1")], "EZRA 5:1", HAGGAI, bg="#14123A", head="Haggai and Zechariah", stamp=5),
        drawn([caps("5:2")], "EZRA 5:2", below(lambda w, h: K.repairers("rp3", w, h, 302), 0.3), "#8FD0E2"),
        face([cp("5:3", to="and said thus unto them,"), say("5:3", frm="Who gave you"), caps("5:4-5")], "EZRA 5:3–5", TATTENAI, head="Tattenai"),
        drawn([caps("5:6"), cp("5:7", to="wherein was written thus:"), say("5:7", frm="Unto Darius")], "EZRA 5:6–7", below(lambda w, h: K.letter_scroll(w, h, 303), 0.4), "#2A1A2A",
              head="The Letter to Darius"),
        face([says("5:8-10")], "EZRA 5:8–10", TATTENAI),
        face([say("5:11", to="saying,"), say("5:11", frm="We are the servants"), says("5:12")], "EZRA 5:11–12", ELDER, bg=COLD),
        face([says("5:13-15")], "EZRA 5:13–15", ELDER, bg=COLD),
        face([says("5:16-17")], "EZRA 5:16–17", TATTENAI)]
PG.extend(pack(SEGS, "EZR-C03-D", PG.next()))
SEGS2 = [drawn([caps("6:1-2")], "EZRA 6:1–2", below(lambda w, h: K.letter_scroll(w, h, 304, seal="#B5121B"), 0.36), "#2A1A2A", head="The Roll at Achmetha", stamp=6),
         drawn([says("6:3-5")], "EZRA 6:3–5", below(lambda w, h: K.temple_plan(w, h), 0.5), "#0B1A2E"),
         face([says("6:6-8")], "EZRA 6:6–8", DARIUS, head="Let the Work of This House Alone"),
         face([says("6:9-10")], "EZRA 6:9–10", DARIUS),
         face([says("6:11-12")], "EZRA 6:11–12", DARIUS, bg=RED)]
PG.extend(pack(SEGS2, "EZR-C03-E", PG.next()))
SEGS3 = [
         drawn([caps("6:13-15")], "EZRA 6:13–15", below(lambda w, h: K.court_scene("cs3", w, h, 305, crowd=False), 0.4), "#8FD0E2", head="This House Was Finished"),
         drawn([caps("6:16-18")], "EZRA 6:16–18", below(lambda w, h: K.court_scene("cs3b", w, h, 306, smoke=True), 0.36), "#8FD0E2"),
         drawn([caps("6:19-22")], "EZRA 6:19–22", below(lambda w, h: K.feast_tents("ft3", w, h, 308), 0.44), "#FFB04A")]
PG.extend(pack(SEGS3, "EZR-C03-F", PG.next(), by_need=False, min_size=None, budget=2400, end=end_mark("NEXT · EZRA THE SCRIBE", "right: 10px; bottom: 34px")))
