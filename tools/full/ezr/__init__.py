"""The Ezra volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The returned exiles and the kings of Persia (ezr.common: the cast; ezr.art carries chr2.art, chr1.art, kg2.art and kg1.art).
The lists of the return (2, 8:1–14, 10:18–44) are roll cells and tally boards, every verse full; the Aramaic letters (4–7) are
drawn as sealed scrolls with the words in speech boxes. Restraint: no violence in the book is drawn; Ezra's grief (9:3) is
his face; the people trembling in the rain (10:9) are a wet square under a dark sky.

Plan (7,377 words, five chapters): 1 The Decree of Cyrus (1–2) · 2 The Foundation of the House (3–4) · 3 The House Finished
(5–6) · 4 Ezra the Scribe (7–8) · 5 The Strange Wives (9–10)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("EZR")

META = {
  "id": "ezra", "order": 15, "name": "Ezra", "kanji": "エズラ記", "thumb": "vol-ezra-", "book": "EZR",
  "title": "Ezra Volume", "volume": "Volume Fifteen",
  "lede": "The fifteenth book of the Bible, in full: the decree of Cyrus and the exiles going up to Jerusalem, the foundation of the house laid with shouting and weeping, the house finished in the days of Darius, and Ezra the scribe, ready in the law of Moses, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Decree of Cyrus", "range": "Ezra 1–2", "bible_chapters": [1, 2],
     "blurb": "In the first year of Cyrus king of Persia, Jehovah stirred up his spirit: whosoever there is among you of all his people, let him go up to Jerusalem; the vessels of the house of Jehovah numbered to Sheshbazzar; and the children of the province that went up out of the captivity, family by family, forty and two thousand three hundred and threescore."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Foundation of the House", "range": "Ezra 3–4", "bible_chapters": [3, 4],
     "blurb": "The people gathered as one man and the altar set upon its base; the foundation of the house laid with trumpets — for he is good — and the old men that had seen the first house weeping, so that the noise of the shout could not be told from the weeping; then the adversaries, the letter to Artaxerxes, and the work made to cease."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The House Finished", "range": "Ezra 5–6", "bible_chapters": [5, 6],
     "blurb": "Haggai and Zechariah prophesy, and the building begins again; Tattenai — who gave you a decree to build this house?; the elders answer, we are the servants of the God of heaven and earth; the roll found at Achmetha; Darius decrees, let the work of this house of God alone; the house finished, dedicated with joy, and the passover kept."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Ezra the Scribe", "range": "Ezra 7–8", "bible_chapters": [7, 8],
     "blurb": "Ezra, a ready scribe in the law of Moses, who had set his heart to seek the law of Jehovah, and to do it, and to teach; the letter of Artaxerxes, king of kings; blessed be Jehovah, who hath put such a thing in the king's heart; the river Ahava and the fast — I was ashamed to ask of the king a band of soldiers; the silver and the gold weighed to the priests; and Jerusalem."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Strange Wives", "range": "Ezra 9–10", "bible_chapters": [9, 10],
     "blurb": "The holy seed mingled with the peoples of the lands; Ezra rends his garment and sits confounded until the evening oblation — O my God, I am ashamed and blush to lift up my face to thee; the people weep very sore; Shecaniah — yet now there is hope for Israel; the great assembly trembling in the rain; and the names of those who had taken foreign wives."},
  ],
}
