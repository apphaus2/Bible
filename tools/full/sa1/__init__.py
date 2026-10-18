"""The 1 Samuel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative throughout, laid out by discourse.pack with the sa1.common helpers (as Judges), lifting the digest's two 1 Samuel
books ("A1".."A9": Hannah to Saul anointed; "B1".."B10": David to Gilboa) where they fit; new drawings in sa1/art.py.
Hannah's song (2:1–10) and David's words are in song boxes and speech boxes; God's words in the Voice box. Restraint:
Eli's death (4:18) is the overturned seat by the gate; Agag (15:33), Goliath's head (17:46, 17:51, 17:54, 17:57), the
priests of Nob (22:18–19), the Amalekite raid's dead and Saul's death on Gilboa (31) are words over landscapes, a fallen
giant, smoke, or the crown and spear on the mountain.

Plan (24,830 words, fourteen chapters): 1 Hannah (1–2) · 2 Speak, Jehovah (3–5) · 3 Give Us a King (6–8) · 4 Saul
Anointed (9–10) · 5 To Obey Is Better (11–13) · 6 Jonathan at Michmash (14) · 7 Jehovah Looketh on the Heart (15–16) ·
8 Goliath (17) · 9 Saul Hath Slain His Thousands (18–19) · 10 Jonathan and David (20–21) · 11 The Cave (22–24) ·
12 Abigail (25–26) · 13 The Witch of Endor (27–29) · 14 Mount Gilboa (30–31)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1SA")

META = {
  "id": "1samuel", "order": 9, "name": "1 Samuel", "kanji": "サムエル記上", "thumb": "vol-1samuel-", "book": "1SA",
  "title": "1 Samuel Volume", "volume": "Volume Nine",
  "lede": "The ninth book of the Bible, in full: Hannah's son Samuel, the ark among the Philistines, Saul the first king, and David the shepherd, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Hannah", "range": "1 Samuel 1–2", "bible_chapters": [1, 2],
     "blurb": "Hannah in bitterness of soul at Shiloh, her vow, and Eli marking her mouth; Samuel born and lent to Jehovah — for this child I prayed; Hannah's song; the sons of Eli and the flesh-hook; the child Samuel in his linen ephod; and the man of God: them that honor me I will honor."},
  ],
}
