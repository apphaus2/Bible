"""The Isaiah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Isaiah is prophecy, laid out like Moses' discourses in Deuteronomy: isa.common.S() cuts a run of verses into speech panels,
alternating the prophet's face (kg2.common.ISAIAH and its moods in isa.common) with drawings of the images (isa.art).
Jehovah's own words are in the Voice box, the prophet's in speech boxes, the psalms and songs in song lines, narration in
captions; a "Thus saith Jehovah" formula opening a verse is set apart as a caption. The burdens of the nations (13–23)
open on a technical map with the nation lit (isa.art.nations_map); the story of Hezekiah and Sennacherib (36–39) reuses
2 Kings' drawings and faces (kg2.art, kg2.common). Restraint: God is never drawn — the vision of 6 is light, smoke, an
empty throne and the seraphim's wings; judgments and battles are words over landscapes, smoke, ruins and empty cities;
the servant of 52:13–53:12 is never drawn (a lamb, a root out of dry ground, an empty grave in the rock); 63:1–6 is
the winepress alone; 66:24 is words over the valley outside the city.

Plan (36,642 words, eighteen chapters): 1 The Vineyard of Jehovah (1–5) · 2 Holy, Holy, Holy (6–9) · 3 The Root of
Jesse (10–12) · 4 How Art Thou Fallen (13–16) · 5 The Burden of Egypt (17–20) · 6 Watchman, What of the Night? (21–23) ·
7 He Hath Swallowed Up Death (24–27) · 8 In Returning and Rest (28–30) · 9 The Desert Shall Blossom (31–35) ·
10 Whereon Dost Thou Trust? (36–39) · 11 Comfort Ye My People (40–42) · 12 Ye Are My Witnesses (43–45) · 13 Go Ye Forth
from Babylon (46–48) · 14 A Light to the Gentiles (49–51) · 15 A Man of Sorrows (52–55) · 16 The Fast That I Have Chosen
(56–59) · 17 Arise, Shine (60–62) · 18 New Heavens and a New Earth (63–66)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ISA")

META = {
  "id": "isaiah", "order": 23, "name": "Isaiah", "kanji": "イザヤ書", "thumb": "vol-isaiah-", "book": "ISA",
  "title": "Isaiah Volume", "volume": "Volume Twenty-Three",
  "lede": "The twenty-third book of the Bible, in full: the vision of Isaiah the son of Amoz — the vineyard of Jehovah, the seraphim crying holy, holy, holy, the burdens of the nations, Hezekiah and the host of Sennacherib, comfort ye my people, the servant of Jehovah, and new heavens and a new earth, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Vineyard of Jehovah", "range": "Isaiah 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "Hear, O heavens, and give ear, O earth: the ox knoweth his owner, but Israel doth not know; come now, and let us reason together — though your sins be as scarlet, they shall be as white as snow; the mountain of Jehovah's house, and swords beaten into plowshares; the day of Jehovah upon all that is lifted up; the daughters of Zion; and the song of the vineyard that brought forth wild grapes."},
  ],
}
