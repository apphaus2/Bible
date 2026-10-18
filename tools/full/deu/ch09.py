"""Deuteronomy volume, Chapter 9 — When Thou Goest Forth to Battle (Deuteronomy 19 – 21). Every verse, word for word from ref/asv.
The statutes as spoken law cells (deu.common.law_chapter: exo.kit.law_pages with spoken=True, pictograms by picto.pick)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from deu import G, art as K
from deu.common import law_chapter
from deu import ch08 as _prev

SECTIONS = [(19, 1, 13, "Three Cities"), (19, 14, 14, "Thy Neighbor's Landmark"), (19, 15, 21, "At the Mouth of Two Witnesses"), (20, 1, 9, "When Thou Goest Forth to Battle"), (20, 10, 20, "When Thou Drawest Nigh unto a City"), (21, 1, 9, "If One Be Found Slain"), (21, 10, 14, "A Captive Woman"), (21, 15, 17, "The Right of the First-born"), (21, 18, 21, "A Stubborn and Rebellious Son"), (21, 22, 23, "Hanged on a Tree"), ]
START, PAGES = law_chapter(_prev, 9, "第九話", "When Thou Goest Forth to Battle", "Deuteronomy 19 – 21", SECTIONS,
                           K.address("t09", 760, 660, 901), "#F3D8A0", G.v("20:1"), "Thou Shalt Not", "DEU-C09")
