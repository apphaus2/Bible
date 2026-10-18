"""The 1 Kings volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative laid out by discourse.pack with the kg1.common helpers (as 2 Samuel). There is no digest book for 1 Kings, so every
drawing is new (kg1/art.py), reusing the 2 Samuel, 1 Samuel, Judges and Joshua drawings where they fit. The temple and its
vessels (6–7) are blueprint plates; Solomon's prayer (8) is speech panels; God's words always the Voice box. Restraint:
Adonijah, Joab and Shimei (2:25, 2:34, 2:46), the man of God and the lion (13:24), the prophets of Baal at the brook Kishon
(18:40) and Naboth (21:13), Ahab's death and the dogs (22:35–38) are words over altars, roads, empty fields or a chariot.

Plan (24,286 words, fourteen chapters): 1 Long Live King Solomon (1) · 2 Show Thyself a Man (2) · 3 An Understanding Heart
(3–4) · 4 The House of Jehovah (5–6) · 5 The Pillars and the Sea (7) · 6 The Glory of Jehovah (8) · 7 The Queen of Sheba
(9–10) · 8 His Heart Turned Away (11) · 9 To Your Tents, O Israel (12–13) · 10 Ahijah's Word (14–15) · 11 Elijah (16–17) ·
12 The Fire of Jehovah (18) · 13 A Still Small Voice (19–20) · 14 Naboth's Vineyard (21–22)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1KI")

META = {
  "id": "1kings", "order": 11, "name": "1 Kings", "kanji": "列王記上", "thumb": "vol-1kings-", "book": "1KI",
  "title": "1 Kings Volume", "volume": "Volume Eleven",
  "lede": "The eleventh book of the Bible, in full: Solomon's wisdom and the house of Jehovah, the kingdom torn in two, and Elijah on mount Carmel, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Long Live King Solomon", "range": "1 Kings 1", "bible_chapters": [1],
     "blurb": "King David old and stricken in years, and Abishag the Shunammite; Adonijah exalts himself — I will be king — and feasts by the stone of Zoheleth; Nathan and Bath-sheba go in to the king; assuredly Solomon thy son shall reign after me; Solomon on the king's mule down to Gihon, the horn of oil, and long live king Solomon; Adonijah holds the horns of the altar."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Show Thyself a Man", "range": "1 Kings 2", "bible_chapters": [2],
     "blurb": "David's charge to Solomon — be thou strong therefore, and show thyself a man; David sleeps with his fathers; Adonijah asks for Abishag, and the throne set for the king's mother at Solomon's right hand; Abiathar sent home to Anathoth; Joab at the horns of the altar; and Shimei, who passed over the brook Kidron."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "An Understanding Heart", "range": "1 Kings 3–4", "bible_chapters": [3, 4],
     "blurb": "A thousand burnt-offerings at Gibeon and the dream by night — ask what I shall give thee; give thy servant an understanding heart; the two women and the living child — divide the living child in two; the princes and the twelve officers; every man under his vine and under his fig-tree; three thousand proverbs, from the cedar of Lebanon to the hyssop in the wall."},
  ],
}
