"""The Joel volume of the full edition: metadata, the volume cover, and the chapter plan (ch01.py).

Built with dan.kit (the Daniel volume's line and panel builders) and job.jdiscourse's packing. Joel's own words are song
boxes in his colour, tagged JOEL; Jehovah's words the Voice box; the priests' prayer (2:17) tagged THE PRIESTS. The
locusts are a technical plate of the four kinds and a swarm darkening the sky, never gory; the northern army driven into
the seas, the valley of Jehoshaphat and Tyre, Sidon and Philistia are maps; the Spirit poured out upon all flesh is light
coming down on old and young, sons and daughters, servants and handmaids; the wonders (blood, fire, pillars of smoke) are
a darkened sun and a red moon over smoke; God is never drawn.

Plan (1,982 words, one chapter): 1 The Day of Jehovah (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JOL")

META = {
  "id": "joel", "order": 29, "name": "Joel", "kanji": "ヨエル書", "thumb": "vol-joel-", "book": "JOL",
  "title": "Joel Volume", "volume": "Volume Twenty-Nine",
  "lede": "The twenty-ninth book of the Bible, in full: the palmer-worm, the locust, the canker-worm and the caterpillar; blow ye the trumpet in Zion, for the day of Jehovah cometh; rend your heart, and not your garments; I will pour out my Spirit upon all flesh; and multitudes, multitudes in the valley of decision, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Day of Jehovah", "range": "Joel 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The word of Jehovah to Joel: that which the palmer-worm hath left hath the locust eaten; the vine laid waste and the priests mourning; blow ye the trumpet in Zion — a day of darkness and gloominess, a great people and a strong; yet even now, rend your heart, and not your garments; I will restore to you the years that the locust hath eaten; I will pour out my Spirit upon all flesh; beat your plowshares into swords; multitudes, multitudes in the valley of decision; and the mountains shall drop down sweet wine."},
  ],
}
