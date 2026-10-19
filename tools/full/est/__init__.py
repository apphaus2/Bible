"""The Esther volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

All new drawings (est/art.py): the palace of Shushan as Persian pillared halls with double-bull capitals, hangings of white,
green and blue and a pavement of red, white, yellow and black marble; the king's gate; the house of the women; the throne and
the golden sceptre; the banquets of wine; the empire from India unto Ethiopia as a technical map; Pur as a wheel of the twelve
months. The cast's faces are in est/common.py (crowned() sets a Persian crown on a face). The name of God is not in the book,
so there is no Voice box. Restraint: Bigthan and Teresh (2:23) words over the threshold and the book of the chronicles; the
gallows only ever a standing structure, Haman's death (7:10) words over the empty gallows at a distance; the slaying of ch. 9
words only over the city of Shushan and over the provinces on the map; the hanging of Haman's ten sons (9:14) words over the
gallows at a distance.

Plan (5,707 words, four chapters): 1 Vashti and Esther (1–2) · 2 For Such a Time as This (3–4) · 3 The King Could Not Sleep
(5–7) · 4 The Days of Purim (8–10)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("EST")

META = {
  "id": "esther", "order": 17, "name": "Esther", "kanji": "エステル記", "thumb": "vol-esther-", "book": "EST",
  "title": "Esther Volume", "volume": "Volume Seventeen",
  "lede": "The seventeenth book of the Bible, in full: the feast of Ahasuerus in Shushan the palace and the queen who would not come, Esther made queen instead of Vashti, Haman's lot and Mordecai's sackcloth, the golden sceptre held out, the night the king could not sleep, and the days of Purim, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Vashti and Esther", "range": "Esther 1–2", "bible_chapters": [1, 2],
     "blurb": "Ahasuerus who reigned from India even unto Ethiopia, and the feast in the court of the garden of the palace — hangings of white, green and blue, vessels of gold; Vashti the queen refused to come; the word of Memucan and letters into every province; then Mordecai the Benjamite and Hadassah, that is, Esther; the royal crown set upon her head; and two chamberlains at the threshold."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "For Such a Time as This", "range": "Esther 3–4", "bible_chapters": [3, 4],
     "blurb": "Haman advanced above all the princes, and Mordecai who bowed not down; Pur, that is, the lot, cast to the month Adar; the king's ring and letters to destroy all the Jews in one day; the king and Haman sat down to drink, but the city of Shushan was perplexed; Mordecai in sackcloth before the gate; who knoweth whether thou art not come to the kingdom for such a time as this?; and if I perish, I perish."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The King Could Not Sleep", "range": "Esther 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "Esther in her royal apparel in the inner court, and the golden sceptre held out — what wilt thou, queen Esther?; the banquet of wine; Zeresh and the gallows fifty cubits high; on that night could not the king sleep, and the book of the records was read; Haman leading Mordecai on the king's horse — thus shall it be done to the man whom the king delighteth to honor; the second banquet: an adversary and an enemy, even this wicked Haman; and Harbonah: behold also, the gallows."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Days of Purim", "range": "Esther 8–10", "bible_chapters": [8, 9, 10],
     "blurb": "The king's ring given to Mordecai; Esther at the king's feet — how can I endure to see the destruction of my kindred?; letters in the king's name and the posts on swift steeds; Mordecai in royal apparel of blue and white, and the Jews had light and gladness, and joy and honor; the thirteenth day of Adar turned to the contrary; days of feasting and gladness, of sending portions one to another and gifts to the poor; the second letter of Purim; and Mordecai next unto king Ahasuerus, speaking peace to all his seed."},
  ],
}
