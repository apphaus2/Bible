"""The 1 Chronicles volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The package is chr1 (a module name cannot start with a digit). The genealogies of 1–9 are roll pages (rolls.roll_pages,
rolls.verse_cells: every verse in full), each run opened by a lineage chart (chr1.art.lineage) under the first verses.
The story of David (10–29) runs alongside 2 Samuel, so it reuses 2 Samuel's faces and drawings (chr1.common takes the cast
from sa2.common and kg2.common; chr1.art re-exports kg2.art, which carries kg1.art, plus sa2.art as K2). The courses of
the priests, singers and porters (23–27) are roll cells. Restraint: Saul's death (10:4–6, 10:9–10) words over the crown and
spear on Gilboa; Uzza (13:10) words over the cart at the threshing-floor; 20:3 words only; the pestilence (21:14) words over
the silent tents; God is never drawn.

Plan (20,145 words, eleven chapters): 1 From Adam (1–2) · 2 The Sons of David (3–4) · 3 The Sons of Levi (5–6) · 4 They
That Dwelt in Jerusalem (7–9) · 5 David King over Israel (10–12) · 6 The Ark of God (13–16) · 7 Thy Throne for Ever
(17–20) · 8 The Threshing-floor of Ornan (21–22) · 9 The Courses (23–25) · 10 The Porters and the Captains (26–27) ·
11 Thine Is the Kingdom (28–29)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1CH")

META = {
  "id": "1chronicles", "order": 13, "name": "1 Chronicles", "kanji": "歴代志上", "thumb": "vol-1chronicles-", "book": "1CH",
  "title": "1 Chronicles Volume", "volume": "Volume Thirteen",
  "lede": "The thirteenth book of the Bible, in full: the generations from Adam, David king over all Israel, the ark brought up with singing, the covenant of an everlasting throne, and the house of Jehovah made ready for Solomon, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "From Adam", "range": "1 Chronicles 1–2", "bible_chapters": [1, 2],
     "blurb": "Adam, Seth, Enosh — the generations from the first man to Noah and his three sons; the nations of Japheth, Ham and Shem; Abraham, Isaac and Ishmael; Esau and the kings that reigned in Edom before any king reigned over Israel; the sons of Israel; and the house of Judah down to Jesse and David, the seventh son."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Sons of David", "range": "1 Chronicles 3–4", "bible_chapters": [3, 4],
     "blurb": "The sons born to David in Hebron and in Jerusalem; the kings of Judah from Solomon to Josiah, son after son; Jeconiah the captive and Zerubbabel; the families of Judah, and Jabez, more honorable than his brethren — oh that thou wouldest bless me indeed, and enlarge my border; the potters who dwelt with the king; and Simeon at the fat pasture of Gedor."},
  ],
}
