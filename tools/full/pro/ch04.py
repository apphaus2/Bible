"""Proverbs volume, Chapter 4 — A Wise Son (Proverbs 10–12). Every verse, word for word from ref/asv.
The proverbs of Solomon begin: one saying to a cell, each under its emblem (pro.common.sayings; the emblem picked from the
saying's own words or named here) — the wise son and the glad father, the diligent hand, the mouth of the righteous a well
of life, the false balance and the just weight, the jewel of gold in a swine's snout, the tree of life, the crown of her
husband, the lamp, the field."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C04-00-Title", "Chapter 4 · A Wise Son", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 280)">{K.father_son("t4", 760, 700, 401)}</g><rect x="0" y="910" width="760" height="170" fill="#E8C88A"></rect>')
    return chapter_title(4, "第四話", "A Wise Son", "Proverbs 10 – 12", svg, "#5A8FC8", v("10:1", frm="A wise son"), "Proverbs · Volume Twenty")


ITEMS = ([cellv("10:1", art=lambda w, h: K.father_son("fs4", w, h, 402), head="A Wise Son Maketh a Glad Father")]
         + run(10, 2, 32)
         + run(11, 1, 31, head="A False Balance", embs={1: "scales", 22: "swine"})
         + run(12, 1, 28, head="Whoso Loveth Correction", embs={4: "crown", 28: "path_light"}))
PG.extend(sayings(ITEMS, "PRO-C04-S", PG.next(), "A Wise Son Maketh a Glad Father", end=end_mark("NEXT · A TREE OF LIFE", "right: 10px; bottom: 10px")))
