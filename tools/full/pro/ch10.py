"""Proverbs volume, Chapter 10 — Bold as a Lion (Proverbs 28–29). Every verse, word for word from ref/eng-asv.
Saying cells: the wicked flee when no man pursueth, but the righteous are bold as a lion (a drawn cell: the lion on the rock,
a man in white standing firm, a far figure fleeing); a sweeping rain; a roaring lion and a ranging bear; he that tilleth his
land; the king by justice establisheth the land; scoffers set a city in a flame; where there is no vision, the people cast
off restraint; the fear of man bringeth a snare."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C10-00-Title", "Chapter 10 · Bold as a Lion", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8A3A2A"></rect><g transform="translate(0 300)">{K.bold_lion("t10", 760, 780, 1001)}</g>')
    return chapter_title(10, "第十話", "Bold as a Lion", "Proverbs 28 – 29", svg, "#8A3A2A", v("28:1", frm="But the righteous"), "Proverbs · Volume Twenty")


ITEMS = ([cellv("28:1", art=lambda w, h: K.bold_lion("bl10", w, h, 1002), bg="#8A3A2A", head="The Righteous Are Bold as a Lion")]
         + run(28, 2, 28, embs={4: "scroll", 9: "scroll", 13: "face_sad", 14: "rays", 15: "bear", 17: "grave", 20: "chest", 21: "scales", 22: "silver", 24: "family", 26: "fork"})
         + run(29, 1, 27, head="Where There Is No Vision",
               embs={1: "house_fallen", 2: "king_people", 3: "chest", 5: "snare", 6: "face_glad", 7: "poor", 8: "fire", 10: "lamps", 13: "sun", 18: "scroll", 19: "face_listen",
                     21: "family", 24: "witness", 25: "tower", 26: "rays"}))
PG.extend(sayings(ITEMS, "PRO-C10-S", PG.next(), "The Righteous Are Bold as a Lion", end=end_mark("NEXT · A WORTHY WOMAN", "right: 10px; bottom: 10px")))
