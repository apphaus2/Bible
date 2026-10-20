"""Proverbs volume, Chapter 5 — A Tree of Life (Proverbs 13–15). Every verse, word for word from ref/eng-asv.
Saying cells: a wise son heareth his father's instruction; the lamp of the wicked put out; hope deferred, and the desire
come a tree of life (a drawn cell); the fountain of life; every wise woman buildeth her house; where no oxen are, the crib
is clean; a soft answer turneth away wrath; the eyes of Jehovah in every place (rays of light, God never drawn); a dinner
of herbs; the way of the sluggard as a hedge of thorns."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C05-00-Title", "Chapter 5 · A Tree of Life", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 280)">{K.tree_of_life("t5", 760, 700, 501)}</g><rect x="0" y="910" width="760" height="170" fill="#9CCB5E"></rect>')
    return chapter_title(5, "第五話", "A Tree of Life", "Proverbs 13 – 15", svg, "#5A8FC8", v("15:4", to="tree of life;"), "Proverbs · Volume Twenty")


ITEMS = (run(13, 1, 11, head="A Wise Son Heareth His Father's Instruction")
         + [cellv("13:12", art=lambda w, h: K.tree_of_life("tl5", w, h, 502), bg="#8FD0E2")]
         + run(13, 13, 25, embs={14: "fountain"})
         + run(14, 1, 35, head="Every Wise Woman Buildeth Her House", embs={1: "woman", 27: "fountain", 30: "face_glad", 34: "king_people"})
         + run(15, 1, 33, head="A Soft Answer Turneth Away Wrath", embs={3: "rays", 17: "feast", 27: "gift"}))
PG.extend(sayings(ITEMS, "PRO-C05-S", PG.next(), "A Wise Son Heareth His Father's Instruction", end=end_mark("NEXT · THE LOT IS CAST INTO THE LAP", "right: 10px; bottom: 10px")))
