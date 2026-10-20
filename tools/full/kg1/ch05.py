"""1 Kings volume, Chapter 5 — The Pillars and the Sea (1 Kings 7). Every verse, word for word from ref/eng-asv.
Solomon's own house thirteen years: the house of the forest of Lebanon on four rows of cedar pillars, the porch of judgment,
costly stones; Hiram of Tyre, the worker in brass; the pillars Jachin and Boaz with their nets, pomegranates and lily-work;
the molten sea upon twelve oxen; the ten bases and lavers; all cast in the clay ground of the Jordan; the vessels of gold —
all as blueprint plates."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import art as K2
from kg1 import G, art as K
from kg1.common import (pack, caps, cp, face, drawn, SOLOMON, RED, COLD, GOLDEN)
from kg1 import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = "#0B1A2E"
def plate(lines, ref, fn, k=0.34, **kw): return drawn(lines, ref, below(fn, k), INK, **kw)


@P("1KI-C05-00-Title", "Chapter 5 · The Pillars and the Sea", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(0 280)">{K.pillar_elev(760, 800, names=True)}</g>')
    return chapter_title(5, "第五話", "The Pillars and the Sea", "1 Kings 7", svg, "#0B1A2E", v("7:21", frm="and he set up the right pillar"), "1 Kings · Volume Eleven")


SEGS = [plate([caps("7:1-3")], "1KGS 7:1–3", lambda w, h: K.forest_house(w, h), k=0.24, head="Solomon's House", stamp=7),
        plate([caps("7:4-6")], "1KGS 7:4–6", lambda w, h: K.forest_house(w, h), k=0.26),
        drawn([caps("7:7-8")], "1KGS 7:7–8", below(lambda w, h: K.judgment_porch("jp5", w, h, 501), 0.26), "#5A2A1E"),
        plate([caps("7:9-12")], "1KGS 7:9–12", lambda w, h: K.great_stones(w, h), k=0.4),
        drawn([caps("7:13-14")], "1KGS 7:13–14", below(lambda w, h: K.casting("cs5", w, h, 502), 0.24), "#5A2A1E", head="Hiram of Tyre"),
        plate([caps("7:15-18")], "1KGS 7:15–18", lambda w, h: K.pillar_elev(w, h), k=0.32, head="The Pillars"),
        plate([caps("7:19-22")], "1KGS 7:19–22", lambda w, h: K.pillar_elev(w, h, names=True), k=0.3),
        plate([caps("7:23-24")], "1KGS 7:23–24", lambda w, h: K.molten_sea(w, h), k=0.2, head="The Molten Sea"),
        plate([caps("7:25-26")], "1KGS 7:25–26", lambda w, h: K.molten_sea(w, h), k=0.24),
        plate([caps("7:27-30")], "1KGS 7:27–30", lambda w, h: K.base_laver(w, h, laver=False), k=0.34, head="The Ten Bases"),
        plate([caps("7:31-33")], "1KGS 7:31–33", lambda w, h: K.base_laver(w, h, laver=False), k=0.34),
        plate([caps("7:34-37")], "1KGS 7:34–37", lambda w, h: K.base_laver(w, h, laver=False), k=0.36),
        plate([caps("7:38-39")], "1KGS 7:38–39", lambda w, h: K.court_plan(w, h), k=0.26, head="The Ten Lavers"),
        plate([caps("7:40-44")], "1KGS 7:40–44", lambda w, h: K.base_laver(w, h), k=0.4),
        drawn([caps("7:45-47")], "1KGS 7:45–47", below(lambda w, h: K.casting("cs5b", w, h, 503), 0.3), "#5A2A1E"),
        plate([caps("7:48-50")], "1KGS 7:48–50", lambda w, h: K.gold_vessels(w, h), k=0.38, head="The Vessels of Gold"),
        drawn([caps("7:51")], "1KGS 7:51", below(lambda w, h: K2.vessels(w, h, 504), 0.3), "#2A1A3A")]
PG.extend(pack(SEGS, "1KI-C05-D", PG.next(), end=end_mark("NEXT · THE GLORY OF JEHOVAH", "right: 10px; bottom: 34px")))
