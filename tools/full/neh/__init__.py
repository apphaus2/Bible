"""The Nehemiah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Nehemiah tells his own story, so most narration is his, in captions; his prayers are his own words (speech boxes), and
God's words appear only where they are quoted (1:8–9, in the Voice box). God is never drawn. New drawings are in neh.art:
the palace at Shushan with its bull-capital columns, the cupbearer before Artaxerxes, the burned gates and the broken wall,
the night ride round the ruins, the plan of the wall and its gates (wall_plan, lit gate by gate for chapter 3 and with the
two companies of chapter 12), the builders with a weapon in one hand, the pulpit of wood, the booths. Lists are roll
cells (neh.common.cell/cells/roll) and tally boards. Restraint: 13:25 (he smote certain of them) is words only over the
shut gate; nothing else in the book is violent.

Plan (10,484 words, seven chapters): 1 The Wall of Jerusalem (1–2) · 2 The Builders (3–4) · 3 The Work Finished (5–6) ·
4 The Genealogy of the Return (7) · 5 The Book of the Law (8–9) · 6 The Sealed Covenant (10–11) · 7 The Dedication of the
Wall (12–13)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("NEH")

META = {
  "id": "nehemiah", "order": 16, "name": "Nehemiah", "kanji": "ネヘミヤ記", "thumb": "vol-nehemiah-", "book": "NEH",
  "title": "Nehemiah Volume", "volume": "Volume Sixteen",
  "lede": "The sixteenth book of the Bible, in full: Nehemiah the cupbearer weeping for Jerusalem, the night ride round the broken wall, the builders with a weapon in one hand, the wall finished in fifty and two days, Ezra reading the law from the pulpit of wood, the sealed covenant and the dedication of the wall with singing, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Wall of Jerusalem", "range": "Nehemiah 1–2", "bible_chapters": [1, 2],
     "blurb": "In Shushan the palace word comes from Judah: the wall of Jerusalem is broken down, and the gates thereof are burned with fire; Nehemiah weeps and prays; the cupbearer before Artaxerxes — why is thy countenance sad?; the king's letters and the captains; then by night, round the broken walls, and the call: let us rise up and build."},
  ],
}
