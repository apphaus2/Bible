"""1 Kings volume, Chapter 3 — An Understanding Heart (1 Kings 3–4). Every verse, word for word from ref/eng-asv.
Pharaoh's daughter; the thousand burnt-offerings at Gibeon; the dream by night — ask what I shall give thee; give thy servant
an understanding heart (God's words in the Voice box); the two women and the living child — fetch me a sword (held, not
used); the princes and the twelve officers as roll cells; every man under his vine and under his fig-tree; the provision
for one day; the stalls of horses; three thousand proverbs, and the cedar and the hyssop."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages, verse_cells
from deu.common import shade
from jos.art import below
from sa2 import art as K2
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, SOLOMON, SOLOMON_WISE, RED, COLD, GOLDEN)
from kg1 import ch02 as _prev

v, sp = G.v, G.span
MOTHER = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#1A1210", scarf="#8A3A4A", brow="sorrow", tear=True, light="#9AA8C8")
OTHER = F("eve", skin="#C98E66", shadow="#4A3A3A", hair="#1A1210", scarf="#4A5A3A", brow="scowl", light="#FF8A3D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0F0E2A"


@P("1KI-C03-00-Title", "Chapter 3 · An Understanding Heart", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0F0E2A"></rect><g transform="translate(0 300)">{K.dream("t3", 760, 780, 301)}</g>')
    return chapter_title(3, "第三話", "An Understanding Heart", "1 Kings 3 – 4", svg, "#0F0E2A", v("3:9", to="discern between good and evil;"), "1 Kings · Volume Eleven")


SEGS = [face([caps("3:1-3")], "1KGS 3:1–3", SOLOMON, head="Solomon Loved Jehovah", stamp=3),
        drawn([caps("3:4")], "1KGS 3:4", lambda w, h: K.gibeon("gb3", w, h, 302), "#FFB04A", head="Gibeon"),
        drawn([cp("3:5", to="and God said,"), gd("3:5", frm="Ask what")], "1KGS 3:5", lambda w, h: K.dream("dr3", w, h, 303), NIGHT),
        face([cp("3:6", to="And Solomon said,"), joined("say", ("3:6", "Thou hast showed"), "3:7")], "1KGS 3:6–7", SOLOMON_WISE, bg=NIGHT),
        face([says("3:8-9"), caps("3:10")], "1KGS 3:8–10", SOLOMON_WISE, bg=NIGHT),
        drawn([cp("3:11", to="said unto him,"), joined("god", ("3:11", "Because thou"), "3:12")], "1KGS 3:11–12", lambda w, h: K.dream("dr3b", w, h, 304), NIGHT),
        drawn([gods("3:13-14")], "1KGS 3:13–14", lambda w, h: K2.throne_glory(w, h, 305), "#14123A"),
        drawn([caps("3:15")], "1KGS 3:15", lambda w, h: K2.prayer("pr3", w, h, 306), "#3A1A2A"),
        drawn([caps("3:16"), cp("3:17", to="And the one woman said,"), joined("say", ("3:17", "Oh, my lord,"), "3:18")], "1KGS 3:16–18", below(lambda w, h: K.two_women("tw3", w, h, 307), 0.4), "#5A2A1E",
              head="The Living Child"),
        face([says("3:19-21")], "1KGS 3:19–21", MOTHER, bg=COLD),
        face([cp("3:22", to="And the other woman said,"), say("3:22", frm="Nay;", to="the dead is thy son."), cp("3:22", frm="And this said,", to="And this said,"),
              say("3:22", frm="No;", to="the living is my son."), cp("3:22", frm="Thus they spake")], "1KGS 3:22", OTHER, bg=RED),
        face([cp("3:23", to="Then said the king,"), say("3:23", frm="The one saith,"), cp("3:24", to="And the king said,"), say("3:24", frm="Fetch me a sword.", to="Fetch me a sword."),
              cp("3:24", frm="And they brought")], "1KGS 3:23–24", SOLOMON),
        drawn([cp("3:25", to="And the king said,"), say("3:25", frm="Divide")], "1KGS 3:25", below(lambda w, h: K.two_women("tw3b", w, h, 308, sword=True), 0.24), "#5A2A1E"),
        face([cp("3:26", to="and she said,"), say("3:26", frm="Oh, my lord,", to="slay it."), cp("3:26", frm="But the other said,", to="But the other said,"), say("3:26", frm="It shall be")],
             "1KGS 3:26", MOTHER, bg=COLD),
        face([cp("3:27", to="answered and said,"), say("3:27", frm="Give her"), caps("3:28")], "1KGS 3:27–28", SOLOMON_WISE)]
PG.extend(pack(SEGS, "1KI-C03-D", PG.next()))
OFFICERS = ([("The Princes", sp("4:1-6"), "1KGS 4:1–6", "#FFD23F", "The Princes and the Officers")]
            + [("Twelve Officers", sp("4:7-8"), "1KGS 4:7–8", "#FFB04A", None)]
            + verse_cells(G, "1KGS", 4, 9, 19, "Twelve Officers", "#FFB04A", budget=300))
PG.extend(roll_pages(OFFICERS, "1KI-C03-R", PG.next(), "1 Kings", "1KGS", tag="SOLOMON'S PRINCES AND OFFICERS · 1 KINGS 4", size=16, most=5))
SEGS2 = [drawn([caps("4:20-21")], "1KGS 4:20–21", lambda w, h: K.rejoicing("rj3", w, h, 309), "#FFE680", head="As the Sand by the Sea", stamp=4),
         drawn([caps("4:22-23")], "1KGS 4:22–23", below(lambda w, h: K2.provisions(w, h, 310), 0.2), "#E8B880"),
         drawn([caps("4:24-25")], "1KGS 4:24–25", below(lambda w, h: K.vine_fig("vf3", w, h, 311), 0.24), "#8FD0E2"),
         drawn([caps("4:26-28")], "1KGS 4:26–28", below(lambda w, h: K.stalls("st3", w, h, 312), 0.3), "#E8C8A0"),
         face([caps("4:29-31")], "1KGS 4:29–31", SOLOMON_WISE, head="The Wisdom of Solomon"),
         drawn([caps("4:32-34")], "1KGS 4:32–34", below(lambda w, h: K.nature(w, h), 0.4), "#1A1430")]
PG.extend(pack(SEGS2, "1KI-C03-E", PG.next(), end=end_mark("NEXT · THE HOUSE OF JEHOVAH", "right: 10px; bottom: 34px")))
