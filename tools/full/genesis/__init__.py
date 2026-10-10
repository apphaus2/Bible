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
  ],
}
