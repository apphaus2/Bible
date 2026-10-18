"""The 2 Kings volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative laid out by discourse.pack with the kg2.common helpers (as 1 Kings, whose faces and drawings it reuses: kg1.common,
kg1.art); new drawings in kg2/art.py. The reigns of the kings are roll cells (kg2.common.reign: Judah gold, Israel red).
Restraint: the fifties consumed (1:10–12), the she-bears (2:24), the king of Moab's son (3:27), the siege's famine (6:28–29),
Jezebel (9:33–37), the heads at Jezreel (10:7–8), Athaliah (11:16), the sons of Zedekiah (25:7) are words over landscapes,
walls, windows, gates or smoke; God is never drawn.

Plan (23,321 words, thirteen chapters): 1 The Chariot of Fire (1–2) · 2 The Pot of Oil (3–4) · 3 Naaman (5–6) · 4 The
Siege of Samaria (7–8) · 5 Jehu (9–10) · 6 Joash (11–12) · 7 The Bones of Elisha (13–14) · 8 Ahaz (15–16) · 9 Carried Away
into Assyria (17) · 10 Hezekiah (18–19) · 11 The Shadow on the Dial (20–21) · 12 Josiah (22–23) · 13 The Fall of Jerusalem
(24–25)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2KI")

META = {
  "id": "2kings", "order": 12, "name": "2 Kings", "kanji": "列王記下", "thumb": "vol-2kings-", "book": "2KI",
  "title": "2 Kings Volume", "volume": "Volume Twelve",
  "lede": "The twelfth book of the Bible, in full: Elijah taken up in the whirlwind, Elisha's wonders, Jehu's furious driving, Hezekiah and Josiah, and Jerusalem burned by Babylon, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Chariot of Fire", "range": "2 Kings 1–2", "bible_chapters": [1, 2],
     "blurb": "Ahaziah fallen through the lattice inquires of Baal-zebub; a hairy man girt with a girdle of leather; fire from heaven on the captains of fifty; then Gilgal, Beth-el and Jericho — I will not leave thee; the Jordan divided by the mantle; a double portion of thy spirit; a chariot of fire and horses of fire, and Elijah went up by a whirlwind into heaven."},
  ],
}
