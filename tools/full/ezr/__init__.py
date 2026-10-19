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
  ],
}
