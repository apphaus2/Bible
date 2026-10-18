"""The Deuteronomy volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Deuteronomy is Moses' discourses in the plains of Moab. His words are set in speech panels (speech.orate: his face, a
column of rounded speech boxes), with God's words in Voice boxes where he quotes Jehovah; flashback panels (Horeb, Kadesh,
Sihon and Og, the golden calf) reuse the Exodus and Numbers art. The laws of 12–26 are law cells in the spoken style
(exo.kit.law_pages(..., spoken=True)): they are Moses' words, so they are not set in the Voice box.

Plan (27,953 words, fifteen chapters): 1 These Are the Words (1–2) · 2 Take Heed to Thyself (3–4) · 3 Hear, O Israel (5–6) ·
4 A People for His Own Possession (7–8) · 5 The Tables of Stone (9–10) · 6 The Place Which Jehovah Shall Choose (11–12) ·
7 The Year of Release (13–15) · 8 Justice, Only Justice (16–18) · 9 When Thou Goest Forth to Battle (19–21) ·
10 Thou Shalt Not (22–23) · 11 The Basket of First-fruits (24–26) · 12 The Blessings and the Curses (27–28) ·
13 Choose Life (29–31) · 14 The Song of Moses (32) · 15 The Death of Moses (33–34)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("DEU")

META = {
  "id": "deuteronomy", "order": 5, "name": "Deuteronomy", "kanji": "申命記", "thumb": "vol-deuteronomy-", "book": "DEU",
  "title": "Deuteronomy Volume", "volume": "Volume Five",
  "lede": "The fifth book of the Bible, in full: Moses' words to Israel in the plains of Moab, every one in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "These Are the Words", "range": "Deuteronomy 1–2", "bible_chapters": [1, 2],
     "blurb": "In the fortieth year, beyond the Jordan, Moses begins to declare the law: Horeb, the judges, the spies and the evil report at Kadesh-barnea, the defeat at Hormah, the long way round Seir, Moab and Ammon, and Sihon king of Heshbon delivered up."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Take Heed to Thyself", "range": "Deuteronomy 3–4", "bible_chapters": [3, 4],
     "blurb": "Og king of Bashan and his bedstead of iron; the land beyond the Jordan given to Reuben, Gad and half Manasseh; Moses' prayer to go over, and Pisgah; ye saw no manner of form on the day that Jehovah spake unto you in Horeb; a devouring fire, a jealous God; and the cities of refuge beyond the Jordan."},
  ],
}
