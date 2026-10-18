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
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Jehovah Bless Thee", "range": "Numbers 5–6", "bible_chapters": [5, 6],
     "blurb": "The unclean put out without the camp; restitution with the fifth part; the law of jealousy and the water of bitterness; the vow of a Nazirite — no wine, no razor, no dead body — and the blessing put upon the children of Israel: Jehovah bless thee, and keep thee."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Offerings of the Princes", "range": "Numbers 7–8", "bible_chapters": [7, 8],
     "blurb": "Six covered wagons and twelve oxen; the twelve princes, each on his day, with a silver platter, a silver bowl and a golden spoon full of incense, for the dedication of the altar; the Voice from above the mercy-seat; the seven lamps; and the Levites cleansed and waved before Jehovah."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Cloud and the Trumpets", "range": "Numbers 9–10", "bible_chapters": [9, 10],
     "blurb": "The passover in the wilderness of Sinai, and a second passover for the men unclean by the dead; the cloud upon the tabernacle by day and the appearance of fire by night; two trumpets of silver; the camps setting forward by their standards; Hobab; and Rise up, O Jehovah."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Graves of Lust", "range": "Numbers 11–12", "bible_chapters": [11, 12],
     "blurb": "The fire at Taberah; who shall give us flesh to eat?; the manna like coriander seed; Moses' burden and the seventy elders on whom the Spirit rested; Eldad and Medad; the quails and the graves of Kibroth-hattaavah; and Miriam, leprous as white as snow, shut up without the camp seven days."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The Twelve Spies", "range": "Numbers 13–14", "bible_chapters": [13, 14],
     "blurb": "Twelve men sent to spy out the land of Canaan; the cluster of Eshcol borne upon a staff between two; the evil report, the children of Anak, and we were as grasshoppers; Joshua and Caleb: an exceeding good land; Moses' plea, I have pardoned; forty years in the wilderness; and the defeat at Hormah."},
  ],
}
