"""The Judges volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Judges is narrative throughout; every chapter is laid out by discourse.pack with the jdg.common line helpers (as Joshua),
lifting the digest's two Judges books (Deborah and Gideon; Samson) where they fit, with new drawings in jdg/art.py. The
lists of 1:27–36 are roll cells. The Song of Deborah (5) is in song boxes. Restraint: Adoni-bezek (1:6–7), Eglon (3:21–22),
Jael (4:21, 5:26–27), Abimelech's seventy brothers (9:5), Jephthah's daughter (11:39), Samson's slaughters and death, and all
of 19–21 (the concubine at Gibeah, the war against Benjamin) are words over landscapes, shut doors and distant silhouettes.

Plan (18,840 words, ten chapters): 1 After the Death of Joshua (1–2) · 2 Deborah (3–5) · 3 Gideon (6–7) · 4 Abimelech (8–9) ·
5 Jephthah (10–12) · 6 Samson (13–15) · 7 Delilah (16) · 8 Micah and the Danites (17–18) · 9 Gibeah (19) ·
10 Every Man Did That Which Was Right in His Own Eyes (20–21)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JDG")

META = {
  "id": "judges", "order": 7, "name": "Judges", "kanji": "士師記", "thumb": "vol-judges-", "book": "JDG",
  "title": "Judges Volume", "volume": "Volume Seven",
  "lede": "The seventh book of the Bible, in full: the judges Jehovah raised up, from Othniel to Samson, and the days when there was no king in Israel, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "After the Death of Joshua", "range": "Judges 1–2", "bible_chapters": [1, 2],
     "blurb": "Judah shall go up: Adoni-bezek, Jerusalem and Hebron, Othniel and Achsah's springs, Beth-el taken by its entrance, and the tribes that drove not out the Canaanites; the angel of Jehovah at Bochim, a generation that knew not Jehovah, and the judges Jehovah raised up."},
  ],
}
