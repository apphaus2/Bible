"""The Obadiah volume of the full edition: metadata, the volume cover, and the one chapter (ch01.py).

The first of the short prophets built here, so it carries their shared helpers: oba/minor.py (Kit — line builders, label
worked out from the cuts, pack and paged; cover_page; vista(), a landscape composer; plate() for vision plates; crag(),
walls(), ruin(), fires(), vines(), fig_tree(), scroll(), cup(), eagle() …). Jonah to Malachi import it.

Jehovah's words to Edom are in the Voice box; the prophet's own words (1:1's "We have heard tidings", 1:17–21) are song
lines. Obadiah: a black beard, a dark green headcloth with a cord (oba.common.OBADIAH). Edom is the red rock with its
dwellings cut into the cliff, an eagle's nest among the stars; the day of Jerusalem's calamity is words over the city's
smoke across the valley and an empty crossway. God is never drawn.

Plan (647 words, one chapter): 1 The Clefts of the Rock (1)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("OBA")

META = {
  "id": "obadiah", "order": 31, "name": "Obadiah", "kanji": "オバデヤ書", "thumb": "vol-obadiah-", "book": "OBA",
  "title": "Obadiah Volume", "volume": "Volume Thirty-One",
  "lede": "The thirty-first book of the Bible, in full: the vision of Obadiah concerning Edom — thou that dwellest in the clefts of the rock, though thou set thy nest among the stars; the day of thy brother's calamity; the day of Jehovah near upon all the nations; and saviours on mount Zion, and the kingdom shall be Jehovah's — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Clefts of the Rock", "range": "Obadiah 1", "bible_chapters": [1],
     "blurb": "The vision of Obadiah: an ambassador sent among the nations against Edom; the pride of thy heart hath deceived thee, O thou that dwellest in the clefts of the rock — though thy nest be set among the stars, I will bring thee down from thence; the violence done to thy brother Jacob in the day of his calamity; as thou hast done, it shall be done unto thee; the house of Jacob a fire, the house of Esau stubble; and the kingdom shall be Jehovah's."},
  ],
}
