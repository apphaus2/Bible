"""The Zephaniah volume of the full edition: metadata, the volume cover, and the one chapter (ch01.py).

Built on the minor prophets' kit (oba/minor.py). Jehovah's words are in the Voice box; the prophet's own (the day of
Jehovah described, "seek ye Jehovah", the woe over the oppressing city, "sing, O daughter of Zion") are song lines.
Zephaniah, of the line of Hezekiah: a black beard and a plum headcloth with a cord (zep.common.ZEPHANIAH). The day of
Jehovah is darkness, clouds, the trumpet and the fire over the land; 1:17 is words over the burning land, no one drawn;
the nations are maps, saltpits and ruins. God is never drawn.

Plan (1,598 words, one chapter): 1 The Great Day of Jehovah (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ZEP")

META = {
  "id": "zephaniah", "order": 36, "name": "Zephaniah", "kanji": "ゼパニヤ書", "thumb": "vol-zephaniah-", "book": "ZEP",
  "title": "Zephaniah Volume", "volume": "Volume Thirty-Six",
  "lede": "The thirty-sixth book of the Bible, in full: the word of Jehovah which came unto Zephaniah in the days of Josiah — the great day of Jehovah is near, a day of wrath, a day of darkness and gloominess; seek ye Jehovah, all ye meek of the earth; woe to the oppressing city; and sing, O daughter of Zion, for Jehovah thy God is in the midst of thee — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Great Day of Jehovah", "range": "Zephaniah 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "I will utterly consume all things from off the face of the ground; them that worship the host of heaven upon the housetops; hold thy peace, for the day of Jehovah is at hand; I will search Jerusalem with lamps; the great day of Jehovah is near, a day of darkness and gloominess, a day of the trumpet and alarm; seek ye Jehovah, all ye meek of the earth; Gaza forsaken, Moab as Sodom, Nineveh a desolation; woe to the oppressing city; and sing, O daughter of Zion — he will rejoice over thee with joy, he will joy over thee with singing."},
  ],
}
