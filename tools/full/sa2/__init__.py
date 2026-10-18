"""The 2 Samuel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative throughout, laid out by discourse.pack with the sa2.common helpers (as 1 Samuel), lifting the digest's two
2 Samuel books ("A1".."A9": Saul mourned to the ewe lamb; "B1".."B9": Absalom to Araunah's threshing-floor) where they fit;
new drawings in sa2/art.py. David's lament (1:19–27) and his song (22) are in song boxes; God's words in the Voice box.
Restraint: the Amalekite's death (1:15), the twelve at Gibeon (2:16), Asahel (2:23), Abner (3:27), Ish-bosheth (4:7–12),
Uzzah (6:7), Uriah (11:17), Amnon (13:28–29), Absalom in the oak (18:14–15), Amasa (20:10), Sheba (20:22) and the sons of
Saul (21:9) are words over landscapes, gates, empty rooms, smoke or a heap of stones; 11:2–4 and 13:11–14 are words over an
empty roof and a shut door.

Plan (20,573 words, twelve chapters): 1 How Are the Mighty Fallen (1–2) · 2 Abner (3–4) · 3 The City of David (5–6) ·
4 Thy Throne Shall Be Established for Ever (7–8) · 5 Mephibosheth (9–10) · 6 Thou Art the Man (11–12) · 7 Absalom (13–14) ·
8 The Ascent of the Mount of Olives (15–16) · 9 O My Son Absalom (17–18) · 10 The King Returned (19–20) · 11 Jehovah Is My
Rock (21–22) · 12 Which Cost Me Nothing (23–24)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2SA")

META = {
  "id": "2samuel", "order": 10, "name": "2 Samuel", "kanji": "サムエル記下", "thumb": "vol-2samuel-", "book": "2SA",
  "title": "2 Samuel Volume", "volume": "Volume Ten",
  "lede": "The tenth book of the Bible, in full: David king in Hebron and in Jerusalem, the ark brought up with dancing, Bath-sheba and Nathan, Absalom's rebellion, and the threshing-floor of Araunah, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "How Are the Mighty Fallen", "range": "2 Samuel 1–2", "bible_chapters": [1, 2],
     "blurb": "The Amalekite out of Saul's camp with the crown and the bracelet; David rends his clothes; the song of the bow — how are the mighty fallen!; David anointed king over Judah in Hebron and Ish-bosheth made king at Mahanaim; the twelve by the pool of Gibeon, Asahel light of foot as a wild roe, and Abner's cry: shall the sword devour for ever?"},
  ],
}
