"""Deuteronomy volume, Chapter 7 — The Year of Release (Deuteronomy 13 – 15). Every verse, word for word from ref/asv.
The statutes as spoken law cells (deu.common.law_chapter: exo.kit.law_pages with spoken=True, pictograms by picto.pick)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from deu import G, art as K
from deu.common import law_chapter
from deu import ch06 as _prev

SECTIONS = [(13, 1, 5, "If There Arise a Prophet"), (13, 6, 11, "If Thy Brother Entice Thee"), (13, 12, 18, "In One of Thy Cities"), (14, 1, 2, "Ye Are the Children of Jehovah"), (14, 3, 21, "Thou Shalt Not Eat Any Abominable Thing"), (14, 22, 29, "The Tithe"), (15, 1, 11, "The Year of Release"), (15, 12, 18, "If Thy Brother Be Sold unto Thee"), (15, 19, 23, "The Firstling Males"), ]
START, PAGES = law_chapter(_prev, 7, "第七話", "The Year of Release", "Deuteronomy 13 – 15", SECTIONS,
                           K.address("t07", 760, 660, 701), "#F3D8A0", G.v("15:11"), "Justice, Only Justice", "DEU-C07")
