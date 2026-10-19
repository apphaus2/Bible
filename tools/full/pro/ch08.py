"""Proverbs volume, Chapter 8 — The Words of the Wise (Proverbs 22–24). Every verse, word for word from ref/asv.
Saying cells: a good name rather than great riches; train up a child; the sluggard's lion in the streets; then the words of
the wise (22:17–21, a drawn cell: elders at the gate, a youth listening), their sayings in small groups — the ancient
landmark, the ruler's table, riches flying away like an eagle, the rod of correction; who hath woe? (23:29–35, a drawn
cell: the red cup, the jar and the adder, the mast on the night sea — no drunkard drawn); the honeycomb; the righteous
falleth seven times; and the field of the sluggard grown over with thorns (24:30–34, a drawn cell)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C08-00-Title", "Chapter 8 · The Words of the Wise", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFE3B8"></rect><g transform="translate(0 280)">{K.wise_gate("t8", 760, 700, 801)}</g><rect x="0" y="910" width="760" height="170" fill="#C8A06A"></rect>')
    return chapter_title(8, "第八話", "The Words of the Wise", "Proverbs 22 – 24", svg, "#8A5A3A", v("22:17", to="words of the wise,"), "Proverbs · Volume Twenty")


ITEMS = (run(22, 1, 16, head="A Good Name", embs={3: "house", 4: "crown", 6: "family", 12: "rays", 13: "lion", 9: "bread"})
         + [cellv("22:17-21", art=lambda w, h: K.wise_gate("wg8", w, h, 802), bg="#FFE3B8", head="The Words of the Wise")]
         + run(22, 22, 29, groups=[(22, 23), (24, 25), (26, 27)], embs={22: "gate", 26: "bed"})
         + run(23, 1, 28, groups=[(1, 3), (4, 5), (6, 8), (10, 11), (13, 14), (15, 16), (17, 18), (19, 21), (22, 25), (26, 28)],
               embs={1: "feast", 4: "eagle", 6: "bread", 13: "rod", 15: "face_glad", 17: "rays", 19: "wine", 22: "family", 26: "pit"})
         + [cellv("23:29-35", art=lambda w, h: K.wine_mast("wm8", w, h, 803), bg="#2A1018", head="Who Hath Woe?")]
         + run(24, 1, 29, groups=[(1, 2), (3, 4), (5, 6), (8, 9), (10, 12), (13, 14), (15, 16), (17, 18), (19, 20), (21, 22), (23, 25), (28, 29)],
               embs={1: "houses", 3: "house", 5: "army", 7: "gate", 8: "face_fool", 10: "path_dark", 13: "honey", 15: "house", 17: "face_glad", 19: "lamps",
                     21: "throne", 23: "scales", 26: "face_wise", 27: "field", 28: "witness"}, head="Fret Not Thyself")
         + [cellv("24:30-34", art=lambda w, h: K.sluggard_field("sf8", w, h, 804), bg="#C8B8A0", head="The Field of the Sluggard")])
PG.extend(sayings(ITEMS, "PRO-C08-S", PG.next(), "A Good Name", end=end_mark("NEXT · APPLES OF GOLD", "right: 10px; bottom: 10px")))
