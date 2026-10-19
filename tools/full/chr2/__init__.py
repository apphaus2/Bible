"""The 2 Chronicles volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The package is chr2 (a module name cannot start with a digit). Solomon's reign (1–9) reuses 1 Kings' blueprints and figures;
the kings of Judah (10–36) reuse 1 and 2 Kings' faces and drawings (chr2.common takes the cast from kg2.common; chr2.art
carries chr1.art, kg2.art and kg1.art). Lists are roll cells (chr2.common.cell/cells/roll; reigns as reign()). Restraint:
the slain of battle words over the plain and the smoke; Jehoram's sickness (21:18–19) words only; Zechariah stoned in the
court (24:21) words over the court; Amaziah's ten thousand (25:12) words over the rock; Uzziah's leprosy his face in pale
light; Manasseh's sons in the fire (33:6) words only; Josiah's wound at Megiddo (35:23–24) words over the chariot; the fall
of Jerusalem (36:17–19) words over the burning city; God is never drawn.

Plan (25,806 words, fourteen chapters): 1 Wisdom and Knowledge (1–4) · 2 The Glory Filled the House (5–7) · 3 The Queen of
Sheba (8–9) · 4 Rehoboam (10–12) · 5 Abijah and Asa (13–16) · 6 Jehoshaphat (17–19) · 7 The Battle Is Not Yours (20–21) ·
8 Joash (22–24) · 9 Amaziah and Uzziah (25–27) · 10 Ahaz and Hezekiah (28–29) · 11 The Passover of Hezekiah (30–31) ·
12 Sennacherib (32) · 13 Manasseh and Josiah (33–34) · 14 The Seventy Years (35–36)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2CH")

META = {
  "id": "2chronicles", "order": 14, "name": "2 Chronicles", "kanji": "歴代志下", "thumb": "vol-2chronicles-", "book": "2CH",
  "title": "2 Chronicles Volume", "volume": "Volume Fourteen",
  "lede": "The fourteenth book of the Bible, in full: Solomon's wisdom and the house of Jehovah filled with glory, the kings of Judah who sought Jehovah and those who forsook him, Hezekiah's passover and Josiah's book, and the seventy years of the land's sabbath, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Wisdom and Knowledge", "range": "2 Chronicles 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "Solomon at the high place at Gibeon, and in that night, ask what I shall give thee — give me now wisdom and knowledge; chariots and horsemen, and silver and gold as stones; Huram king of Tyre and the cedars of Lebanon; then the house of Jehovah on mount Moriah: the most holy house and its cherubim, Jachin and Boaz, the molten sea upon twelve oxen, and the vessels of gold."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Glory Filled the House", "range": "2 Chronicles 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "The ark brought into the oracle under the wings of the cherubim; the trumpeters and singers as one — for he is good, for his lovingkindness endureth for ever — and the house filled with a cloud; Solomon's prayer from the brazen scaffold; the fire came down from heaven; and Jehovah's answer by night: if my people, who are called by my name, shall humble themselves, and pray."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Queen of Sheba", "range": "2 Chronicles 8–9", "bible_chapters": [8, 9],
     "blurb": "Tadmor in the wilderness and the store-cities; Pharaoh's daughter brought up to her own house, for the places are holy whereunto the ark hath come; the ships of Ophir; then the queen of Sheba with hard questions — the half of the greatness of thy wisdom was not told me; the throne of ivory and its twelve lions; and Solomon slept with his fathers."},
  ],
}
