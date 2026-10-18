"""The Numbers volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Plan (32,032 words, sixteen chapters): 1 The Numbering (1–2) · 2 The Charge of the Levites (3–4) · 3 Jehovah Bless Thee (5–6) ·
4 The Offerings of the Princes (7–8) · 5 The Cloud and the Trumpets (9–10) · 6 Graves of Lust (11–12) · 7 The Twelve Spies (13–14) ·
8 Korah (15–17) · 9 The Water for Impurity (18–19) · 10 Meribah and the Serpent of Brass (20–21) · 11 Balaam (22–24) ·
12 Phinehas and the Second Numbering (25–26) · 13 The Daughters of Zelophehad (27–29) · 14 Vows and the War with Midian (30–31) ·
15 The Journeys (32–33) · 16 The Borders of the Land (34–36).
Lists (the census, the camp, the princes' offerings, the stations of 33) are set as cells, every verse in full; laws as
Voice-box law cells (exo.kit.law_pages)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("NUM")

META = {
  "id": "numbers", "order": 4, "name": "Numbers", "kanji": "民数記", "thumb": "vol-numbers-", "book": "NUM",
  "title": "Numbers Volume", "volume": "Volume Four",
  "lede": "The fourth book of the Bible, in full: every scene, every law and every line of dialogue in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Numbering", "range": "Numbers 1–2", "bible_chapters": [1, 2],
     "blurb": "In the wilderness of Sinai: take ye the sum of all the congregation; the twelve princes, the men of every tribe from twenty years old and upward that were able to go forth to war, six hundred thousand and three thousand and five hundred and fifty; the Levites about the tabernacle; and every man by his own standard, east, south, west and north."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Charge of the Levites", "range": "Numbers 3–4", "bible_chapters": [3, 4],
     "blurb": "The sons of Aaron, and Nadab and Abihu who died before Jehovah; the Levites given unto Aaron instead of all the first-born, Gershon westward, Kohath southward, Merari northward, the redemption of the two hundred and threescore and thirteen; and the ark, the table and the candlestick wrapped in blue, scarlet and sealskin for the sons of Kohath to bear."},
  ],
}
