"""The Jonah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ch02.py).

Built on the minor prophets' kit (oba/minor.py). The story is told in captions and speech boxes, Jehovah's words in the
Voice box, Jonah's prayer from the fish's belly (2:2–9) in song lines. Jonah: a brown beard, a sea-blue headcloth with a
cord and a sea-blue robe at a distance (jon.common.JONAH, jon.art.jonah_fig). The great fish is a great whale-like fish
(jon.art.fish); Jonah inside it is only a dark shape, and his prayer is words over the deep, the weeds and the bars of the
earth. The ship in the tempest is wind and lightning, God never drawn; Nineveh in sackcloth, the king in ashes beside his
empty throne; the booth, the gourd, the worm and the sultry east wind.

Plan (1,313 words, two chapters): 1 The Great Fish (1–2) · 2 That Great City (3–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JON")

META = {
  "id": "jonah", "order": 32, "name": "Jonah", "kanji": "ヨナ書", "thumb": "vol-jonah-", "book": "JON",
  "title": "Jonah Volume", "volume": "Volume Thirty-Two",
  "lede": "The thirty-second book of the Bible, in full: Jonah fleeing unto Tarshish from the presence of Jehovah, the mighty tempest and the lot, three days and three nights in the belly of the great fish — salvation is of Jehovah — then Nineveh, that great city, in sackcloth and ashes, and the gourd that came up in a night and perished in a night — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Great Fish", "range": "Jonah 1–2", "bible_chapters": [1, 2],
     "blurb": "Arise, go to Nineveh, that great city — but Jonah rose up to flee unto Tarshish, and went down to Joppa; a great wind upon the sea, the mariners crying every man unto his god, and Jonah fast asleep; the lot fell upon Jonah — I am a Hebrew, and I fear Jehovah; take me up, and cast me forth into the sea; a great fish to swallow up Jonah, and his prayer out of the fish's belly: salvation is of Jehovah."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "That Great City", "range": "Jonah 3–4", "bible_chapters": [3, 4],
     "blurb": "The word of Jehovah the second time; yet forty days, and Nineveh shall be overthrown; the people of Nineveh believed God, and the king laid his robe from him and sat in ashes — who knoweth whether God will not turn and repent?; but it displeased Jonah exceedingly: doest thou well to be angry?; the booth on the east side of the city, the gourd, the worm and the sultry east wind; and should not I have regard for Nineveh, that great city?"},
  ],
}
