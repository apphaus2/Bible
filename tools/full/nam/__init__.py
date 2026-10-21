"""The Nahum volume of the full edition: metadata, the volume cover, and the one chapter (ch01.py).

Built on the minor prophets' kit (oba/minor.py). The prophet's song of Jehovah's vengeance and the taunt over Nineveh are
song lines; Jehovah's own words (1:12–14, 2:13, 3:5–7) are in the Voice box. Nahum the Elkoshite: a grey beard and a
charcoal headcloth with a cord (nam.common.NAHUM). The fall of Nineveh is words over the city and its river gates (nam/art.py:
the whirlwind, the flood, the chariots raging by torchlight, the gates of the rivers opened, the spoil, the empty den of
the lions, the chariots burning in the smoke). Restraint: 3:3 (the heap of corpses) is words over the walls by night with
flashes of steel; 3:10 (No-amon's children) is words over the empty temple pylons by the Nile; no one slain is drawn. God
is never drawn: his way is the whirlwind and the storm.

Plan (1,232 words, one chapter): 1 The Burden of Nineveh (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("NAM")

META = {
  "id": "nahum", "order": 34, "name": "Nahum", "kanji": "ナホム書", "thumb": "vol-nahum-", "book": "NAM",
  "title": "Nahum Volume", "volume": "Volume Thirty-Four",
  "lede": "The thirty-fourth book of the Bible, in full: the burden of Nineveh, the book of the vision of Nahum the Elkoshite — Jehovah hath his way in the whirlwind and in the storm; behold, upon the mountains the feet of him that bringeth good tidings; the chariots rage in the streets, the gates of the rivers are opened; woe to the bloody city — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Burden of Nineveh", "range": "Nahum 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Jehovah is a jealous God and avengeth; he hath his way in the whirlwind and in the storm, and the clouds are the dust of his feet; Jehovah is good, a stronghold in the day of trouble; behold, upon the mountains the feet of him that bringeth good tidings; he that dasheth in pieces is come up — the chariots rage in the streets, the gates of the rivers are opened, and the palace is dissolved; where is the den of the lions?; woe to the bloody city; art thou better than No-amon?; thy shepherds slumber, O king of Assyria."},
  ],
}
