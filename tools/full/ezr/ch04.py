"""Ezra volume, Chapter 4 — Ezra the Scribe (Ezra 7–8). Every verse, word for word from ref/eng-asv.
Ezra's line back to Aaron the chief priest (a lineage chart); a ready scribe in the law of Moses, who had set his heart to
seek the law of Jehovah, and to do it, and to teach; the letter of Artaxerxes, king of kings (a sealed scroll, the decree in
speech boxes); blessed be Jehovah, who hath put such a thing in the king's heart; the heads of fathers' houses that went up
with him (roll cells); the river Ahava and the Levites sent for from Casiphia; the fast — I was ashamed to ask of the king a
band of soldiers; the silver and the gold weighed to the priests — ye are holy unto Jehovah; and the journey to Jerusalem."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from ezr import G, art as K
from ezr.common import (pack, cp, say, caps, says, drawn, face, joined, cell, cells, roll, EZRA, ARTAXERXES, COLD, GOLDEN, RED)
from ezr import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD = "#0B1A2E", "#1A1430"
LINE = ["EZRA", "SERAIAH", "AZARIAH", "HILKIAH", "SHALLUM", "ZADOK", "AHITUB", "AMARIAH", "AZARIAH", "MERAIOTH", "ZERAHIAH", "UZZI", "BUKKI", "ABISHUA",
        "PHINEHAS", "ELEAZAR", "AARON"]


@P("EZR-C04-00-Title", "Chapter 4 · Ezra the Scribe", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.book_found("t4", 760, 820, 401)}</g><rect x="0" y="0" width="760" height="262" fill="#3A2A1A"></rect>')
    return chapter_title(4, "第四話", "Ezra the Scribe", "Ezra 7 – 8", svg, "#3A2A1A", v("7:10"), "Ezra · Volume Fifteen")


SEGS = [drawn([caps("7:1-5")], "EZRA 7:1–5", below(lambda w, h: K.lineage(w, h, LINE, hi=("EZRA", "ZADOK", "AARON"), per=6, top=0.3, bot=0.9), 0.24), MAP, h=430,
              head="A Ready Scribe", stamp=7),
        face([caps("7:6-8")], "EZRA 7:6–8", EZRA),
        drawn([caps("7:9-10")], "EZRA 7:9–10", below(lambda w, h: K.return_caravan("rc4", w, h, 402), 0.3), "#FFC890"),
        drawn([cp("7:11"), say("7:12"), says("7:13")], "EZRA 7:11–13", below(lambda w, h: K.letter_scroll(w, h, 403), 0.44), "#2A1A2A", head="Artaxerxes, King of Kings"),
        face([says("7:14-16")], "EZRA 7:14–16", ARTAXERXES),
        face([says("7:17-20")], "EZRA 7:17–20", ARTAXERXES),
        face([says("7:21-24")], "EZRA 7:21–24", ARTAXERXES),
        face([says("7:25-26")], "EZRA 7:25–26", ARTAXERXES),
        face([joined("say", "7:27", ("7:28", "and hath extended", "mighty princes.")), cp("7:28", frm="And I was strengthened")], "EZRA 7:27–28", EZRA, head="Blessed Be Jehovah")]
PG.extend(pack(SEGS, "EZR-C04-D", PG.next()))
R = [cell("The Heads of Their Fathers' Houses", "8:1-2", "#FFD23F", head="They That Went Up with Me")] + cells(8, 3, 14, "With Him Were Reckoned", "#FFD23F", budget=440)
PG.extend(roll(R, "EZR-C04-R", PG.next(), "THE GENEALOGY OF THEM THAT WENT UP · EZRA 8"))
SEGS2 = [drawn([caps("8:15-17")], "EZRA 8:15–17", below(lambda w, h: K.ahava("ah4", w, h, 404), 0.44), "#8FD0E2", head="The River Ahava", stamp=8),
         drawn([caps("8:18-20")], "EZRA 8:18–20", below(lambda w, h: K.ahava("ah4b", w, h, 405), 0.4), "#8FD0E2"),
         drawn([caps("8:21"), cp("8:22", to="saying,"), say("8:22", frm="The hand of our God"), caps("8:23")], "EZRA 8:21–23", below(lambda w, h: K.ahava("ah4c", w, h, 406, fast=True), 0.44),
               "#5A4A7A", head="I Proclaimed a Fast"),
         drawn([caps("8:24-27")], "EZRA 8:24–27", below(lambda w, h: K.weighing("wg4", w, h, 407), 0.4), "#8A4A26", head="Holy unto Jehovah"),
         face([cp("8:28", to="And I said unto them,"), say("8:28", frm="Ye are holy"), says("8:29"), caps("8:30")], "EZRA 8:28–30", EZRA),
         drawn([caps("8:31-32")], "EZRA 8:31–32", below(lambda w, h: K.return_caravan("rc4b", w, h, 408), 0.3), "#FFC890"),
         drawn([caps("8:33-34")], "EZRA 8:33–34", below(lambda w, h: K.weighing("wg4b", w, h, 409), 0.36), "#8A4A26"),
         drawn([caps("8:35-36")], "EZRA 8:35–36", below(lambda w, h: K.court_scene("cs4", w, h, 410, smoke=True), 0.36), "#8FD0E2")]
PG.extend(pack(SEGS2, "EZR-C04-E", PG.next(), end=end_mark("NEXT · THE STRANGE WIVES", "right: 10px; bottom: 34px")))
