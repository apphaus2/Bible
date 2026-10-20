"""Proverbs volume, Chapter 6 — The Lot Is Cast into the Lap (Proverbs 16–18). Every verse, word for word from ref/eng-asv.
Saying cells: the plans of the heart and the answer of the tongue; a just balance and scales are Jehovah's; the sayings of
the king; pride goeth before destruction; pleasant words as a honeycomb; the hoary head a crown of glory; the lot cast into
the lap (a drawn cell: lots on a red cloth, light from above, God never drawn); a dry morsel and quietness; the refining
pot; a bear robbed of her whelps; the name of Jehovah a strong tower; a friend that sticketh closer than a brother."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C06-00-Title", "Chapter 6 · The Lot Is Cast into the Lap", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#12113A"></rect><g transform="translate(0 300)">{K.casting_lot("t6", 760, 700, 601)}</g><rect x="0" y="930" width="760" height="150" fill="#3A2A3A"></rect>')
    return chapter_title(6, "第六話", "The Lot Is Cast into the Lap", "Proverbs 16 – 18", svg, "#2A1A4A", v("16:33"), "Proverbs · Volume Twenty")


ITEMS = (run(16, 1, 32, head="Commit Thy Works unto Jehovah", embs={2: "scales", 8: "morsel", 11: "weights", 26: "bread"})
         + [cellv("16:33", art=lambda w, h: K.casting_lot("cl6", w, h, 602), bg="#12113A")]
         + run(17, 1, 28, head="Better Is a Dry Morsel", embs={6: "old"})
         + run(18, 1, 24, head="A Strong Tower", embs={11: "city", 21: "face_wise"}))
PG.extend(sayings(ITEMS, "PRO-C06-S", PG.next(), "Commit Thy Works unto Jehovah", end=end_mark("NEXT · THE KING'S HEART", "right: 10px; bottom: 10px")))
