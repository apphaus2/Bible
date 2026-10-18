"""The Ruth volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ch02.py).

Ruth is short (85 verses, 2,578 words) and told in dialogue, so both chapters are speech panels and the digest's Ruth book
lifted whole (rut.common.D("P05", 1)): Naomi (purple headscarf, grey hair; Mara weeping in cold light), Ruth (rose
headscarf), Orpah (saffron), Boaz (white headcloth, grey-brown beard). The generations of Perez (4:18–22) are a roll page.

Plan: 1 Whither Thou Goest (1–2) · 2 The Near Kinsman (3–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("RUT")

META = {
  "id": "ruth", "order": 8, "name": "Ruth", "kanji": "ルツ記", "thumb": "vol-ruth-", "book": "RUT",
  "title": "Ruth Volume", "volume": "Volume Eight",
  "lede": "The eighth book of the Bible, in full: Naomi and Ruth the Moabitess, the field of Boaz, and the near kinsman, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Whither Thou Goest", "range": "Ruth 1–2", "bible_chapters": [1, 2],
     "blurb": "Famine, Moab and three graves; Naomi turns home, Orpah kisses her, but Ruth clave unto her: whither thou goest, I will go. Call me Mara. Then the barley harvest, the field of Boaz, and under whose wings thou art come to take refuge."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Near Kinsman", "range": "Ruth 3–4", "bible_chapters": [3, 4],
     "blurb": "The threshing-floor at midnight and the skirt spread over the handmaid; six measures of barley; the near kinsman at the gate draws off his shoe; ye are witnesses; and Obed in Naomi's bosom, the father of Jesse, the father of David."},
  ],
}
