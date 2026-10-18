"""Deuteronomy volume, Chapter 11 — The Basket of First-fruits (Deuteronomy 24 – 26). Every verse, word for word from ref/asv.
The statutes as spoken law cells (deu.common.law_chapter: exo.kit.law_pages with spoken=True, pictograms by picto.pick)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from deu import G, art as K
from deu.common import law_chapter
from deu import ch10 as _prev

SECTIONS = [(24, 1, 5, "A Bill of Divorcement"), (24, 6, 13, "No Man Shall Take the Mill"), (24, 14, 22, "Thou Shalt Not Oppress a Hired Servant"), (25, 1, 4, "Thou Shalt Not Muzzle the Ox"), (25, 5, 12, "If Brethren Dwell Together"), (25, 13, 19, "Just Weights and Remember Amalek"), (26, 1, 11, "The Basket of First-fruits"), (26, 12, 15, "The Year of Tithing"), (26, 16, 19, "A People for His Own Possession"), ]
START, PAGES = law_chapter(_prev, 11, "第十一話", "The Basket of First-fruits", "Deuteronomy 24 – 26", SECTIONS,
                           K.address("t11", 760, 660, 1101), "#F3D8A0", G.v("26:10"), "The Blessings and the Curses", "DEU-C11")
