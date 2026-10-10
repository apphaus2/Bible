"""The Genesis volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("GEN")

META = {
  "id": "genesis", "order": 1, "name": "Genesis", "kanji": "創世記", "thumb": "vol-genesis-", "book": "GEN",
  "title": "Genesis Volume", "volume": "Volume One",
  "lede": "The first book of the Bible, in full: every scene and every line of dialogue in the words of the American Standard Version (1901).",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "In the Beginning", "range": "Genesis 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The six days and the seventh, the dust of the ground and the breath of life, the garden eastward in Eden, the woman, the serpent, the fruit, and the way east of Eden."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Cain to the Flood", "range": "Genesis 4–9", "bible_chapters": [4, 5, 6, 7, 8, 9],
     "blurb": "Cain and Abel, the mark of Cain and the city of Enoch, the book of the generations of Adam, Enoch who walked with God, the ark of gopher wood, the flood, the raven and the dove, and the bow in the cloud."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Babel to Abram's Covenant", "range": "Genesis 10–15", "bible_chapters": [10, 11, 12, 13, 14, 15],
     "blurb": "The table of the nations, Nimrod the mighty hunter, the tower of Babel, the generations of Shem, the call of Abram, Egypt and Pharaoh's house, Lot and the Plain, the war of the kings, Melchizedek, the stars, and the covenant between the pieces."},
  ],
}
