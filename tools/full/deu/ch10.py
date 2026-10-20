"""Deuteronomy volume, Chapter 10 — Thou Shalt Not (Deuteronomy 22 – 23). Every verse, word for word from ref/eng-asv.
The statutes as spoken law cells (deu.common.law_chapter: exo.kit.law_pages with spoken=True, pictograms by picto.pick)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from deu import G, art as K
from deu.common import law_chapter
from deu import ch09 as _prev

SECTIONS = [(22, 1, 4, "Thy Brother's Ox"), (22, 5, 12, "A Battlement for Thy Roof"), (22, 13, 30, "If Any Man Take a Wife"), (23, 1, 8, "The Assembly of Jehovah"), (23, 9, 14, "When Thou Goest Forth in Camp"), (23, 15, 25, "The Servant That Is Escaped"), ]
START, PAGES = law_chapter(_prev, 10, "第十話", "Thou Shalt Not", "Deuteronomy 22 – 23", SECTIONS,
                           K.address("t10", 760, 660, 1001), "#F3D8A0", G.v("22:4"), "The Basket of First-fruits", "DEU-C10")
