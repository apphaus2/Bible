"""The Jeremiah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Prophecy is laid out like Deuteronomy's discourses (discourse.pack): Jehovah's words in the Voice box, set beside the
prophet's face or over drawings of the images (the almond rod, the caldron, the potter's wheel, the girdle, the yoke, the
two baskets of figs); Jeremiah's own words, complaints and prayers in speech boxes; narration in captions. jer.common.run()
cuts a run of verses into panels that alternate his face with the drawings. Jeremiah is a young prophet who grows grey
(jer.common.jer(age, mood): a dark blue-grey headcloth, beardless at his call, black-bearded, then grey). The oracles
against the nations (46–51) are technical maps. The fall of Jerusalem (39, 52) reuses 2 Kings' drawings (kg2.art
burning_city, siege_forts, captives, mizpah) and faces (Zedekiah, Gedaliah, Jehoiachin).

Restraint: sieges, slaughter and famine are words over walls, smoke and empty streets; the sons of Zedekiah slain and his
eyes put out (39:6–7, 52:10–11) words over the empty plain of Riblah; Gedaliah's murder (41:2–3) and the pit at Mizpah
(41:7–9) words over the shut house and the dark cistern; Jeremiah in the dungeon (38:6) the empty pit and the cords; God is
never drawn.

Plan (42,247 words, nineteen chapters): 1 The Almond Rod (1–3) · 2 Evil from the North (4–6) · 3 The Temple of Jehovah
(7–9) · 4 The Broken Covenant (10–12) · 5 The Marred Girdle (13–15) · 6 The Potter's House (16–18) · 7 The Earthen Bottle
(19–22) · 8 The Cup of the Wine of Wrath (23–25) · 9 The Yoke (26–28) · 10 A New Covenant (29–31) · 11 The Field at Anathoth
(32–33) · 12 The Roll (34–36) · 13 The Dungeon (37–39) · 14 Gedaliah (40–42) · 15 Into Egypt (43–45) · 16 Against the
Nations (46–48) · 17 Babylon Is Taken (49–50) · 18 The Hammer of the Whole Earth (51) · 19 The Fall of Jerusalem (52)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JER")

META = {
  "id": "jeremiah", "order": 24, "name": "Jeremiah", "kanji": "エレミヤ書", "thumb": "vol-jeremiah-", "book": "JER",
  "title": "Jeremiah Volume", "volume": "Volume Twenty-Four",
  "lede": "The twenty-fourth book of the Bible, in full: the young prophet set over the nations, the potter's house and the yoke, the roll burned in the fire, the prophet in the dungeon, the fall of Jerusalem and the flight into Egypt, the burdens of the nations, and the promise of a new covenant, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Almond Rod", "range": "Jeremiah 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Before I formed thee in the belly I knew thee — ah, Lord Jehovah! I know not how to speak, for I am a child; I have put my words in thy mouth; the rod of an almond-tree and the boiling caldron from the north; the kindness of thy youth; they have forsaken me, the fountain of living waters, and hewed them out broken cisterns; and return, O backsliding children."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Evil from the North", "range": "Jeremiah 4–6", "bible_chapters": [4, 5, 6],
     "blurb": "Blow ye the trumpet in the land, set up a standard toward Zion; a lion is gone up from his thicket; my anguish, my anguish! I beheld the earth, and, lo, it was waste and void; run ye to and fro through the streets of Jerusalem, if ye can find a man; peace, peace, when there is no peace; ask for the old paths; and a people cometh from the north country."},
  ],
}
