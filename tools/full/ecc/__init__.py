"""The Ecclesiastes volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The Preacher is Solomon old (kg2.common.SOLOMON_OLD and its moods in ecc.common): his words in speech boxes beside his face,
or as song lines over drawings of what he speaks of (ecc/art.py): the sun rising and going down, the wind going round, the
rivers running into the sea, the ruins of the former generations, his works and pools, a time to every purpose as a ring of
cells, the threefold cord, one among a thousand, the little city and the poor wise man, the almond-tree, the silver cord and
the golden bowl. Narration (1:1, 12:9–10) is in captions. God is never drawn; the dead and death are told in words over
roads, gates, graves and the dusk.

Plan (5,599 words, four chapters): 1 Vanity of Vanities (1–3) · 2 Two Are Better than One (4–6) · 3 A Good Name (7–9) ·
4 Remember Thy Creator (10–12)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ECC")

META = {
  "id": "ecclesiastes", "order": 21, "name": "Ecclesiastes", "kanji": "伝道の書", "thumb": "vol-ecclesiastes-", "book": "ECC",
  "title": "Ecclesiastes Volume", "volume": "Volume Twenty-One",
  "lede": "The twenty-first book of the Bible, in full: the words of the Preacher, the son of David, king in Jerusalem — vanity of vanities, a time to every purpose under heaven, two are better than one, a good name, and remember also thy Creator in the days of thy youth — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Vanity of Vanities", "range": "Ecclesiastes 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The words of the Preacher: vanity of vanities, all is vanity; the sun ariseth and goeth down, the wind turneth about, all the rivers run into the sea, and there is no new thing under the sun; his great works, his houses and pools and singers, and all a striving after wind; and for everything there is a season — a time to be born, and a time to die."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Two Are Better than One", "range": "Ecclesiastes 4–6", "bible_chapters": [4, 5, 6],
     "blurb": "The tears of the oppressed, and they had no comforter; better is a handful with quietness; one that is alone, and he hath not a second; two are better than one, and a threefold cord is not quickly broken; keep thy foot when thou goest to the house of God — let thy words be few; the sleep of a laboring man is sweet; naked shall he go again as he came; and his days as a shadow."},
  ],
}
