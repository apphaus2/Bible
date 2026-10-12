"""The Leviticus volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).
Almost all of Leviticus is law: it is set in Voice-box law cells (exo.kit.law_pages) with pictograms from lev/art.py, and
the narrative stretches (the consecration, Nadab and Abihu, the Day of Atonement, the blasphemer) as story pages."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("LEV")

META = {
  "id": "leviticus", "order": 3, "name": "Leviticus", "kanji": "レビ記", "thumb": "vol-leviticus-", "book": "LEV",
  "title": "Leviticus Volume", "volume": "Volume Three",
  "lede": "The third book of the Bible, in full: every law and every scene in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Offerings", "range": "Leviticus 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "Jehovah calls to Moses out of the tent of meeting: the burnt-offering of the herd, the flock and the birds, the meal-offering seasoned with salt, the peace-offerings, the sin-offering for the priest, the congregation, the ruler and the common people, and the trespass-offering with its fifth part."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Consecration", "range": "Leviticus 6–8", "bible_chapters": [6, 7, 8],
     "blurb": "The law of each offering — the fire on the altar that shall never go out, the portions of the priests, the sacrifice of thanksgiving, no fat and no blood, the wave-breast and the heave-thigh — and the seven days in which Moses washed, clothed and anointed Aaron and his sons."},
  ],
}
