"""Deuteronomy volume, Chapter 8 — Justice, Only Justice (Deuteronomy 16 – 18). Every verse, word for word from ref/eng-asv.
The statutes as spoken law cells (deu.common.law_chapter: exo.kit.law_pages with spoken=True, pictograms by picto.pick)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from deu import G, art as K
from deu.common import law_chapter
from deu import ch07 as _prev

SECTIONS = [(16, 1, 8, "The Passover"), (16, 9, 12, "The Feast of Weeks"), (16, 13, 17, "The Feast of Tabernacles"), (16, 18, 22, "Judges and Officers"), (17, 1, 7, "Thou Shalt Not Sacrifice a Blemish"), (17, 8, 13, "If There Arise a Matter Too Hard"), (17, 14, 20, "A King over Thee"), (18, 1, 8, "The Priests the Levites"), (18, 9, 14, "Thou Shalt Not Learn to Do"), (18, 15, 22, "A Prophet Like unto Me"), ]
START, PAGES = law_chapter(_prev, 8, "第八話", "Justice, Only Justice", "Deuteronomy 16 – 18", SECTIONS,
                           K.address("t08", 760, 660, 801), "#F3D8A0", G.v("16:20"), "When Thou Goest Forth to Battle", "DEU-C08")
