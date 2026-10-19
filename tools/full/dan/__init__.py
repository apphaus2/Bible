"""The Daniel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Daniel is told as narrative pages (1–6) and as visions (7–12) laid out by job.jdiscourse (dan.common.pack: the fewest pages on
which the words stay readable). Speech is set in song boxes in the speaker's colour, with the speaker's name tagged on the
panel (dan.common.SPK); the words of God in the Voice box; the angels' words (Gabriel, the man clothed in linen) in gold-ruled
boxes, the angels drawn only as figures of light. The visions are technical plates (dan.art): the image of gold, silver,
brass, iron and clay as a blueprint; the four beasts, the ram and the he-goat as heraldic emblems on a dark field, never
gory; the seventy weeks as a chart; the kings of the north and the south as a map and a board of turns.

Restraint: the wise men's death decree words over a sealed scroll; the mighty men slain by the flame (3:22) words over the
furnace mouth; the three in the fire unharmed with a fourth like a son of the gods shown only as a shape of light; the king's
madness (4:33) words over the field; the writing on the wall a script of light on the plaster with no hand drawn; Belshazzar's
death (5:30) words over the dark palace; the accusers cast to the lions (6:24) words over the sealed stone; the Ancient of
days only a throne of fiery flame and light, never a figure; God is never drawn.

Plan (11,685 words, six chapters): 1 A Stone Cut Out Without Hands (1–2) · 2 The Burning Fiery Furnace (3–4) · 3 The Den of
Lions (5–6) · 4 The Ancient of Days (7–8) · 5 Seventy Weeks (9–10) · 6 The Time of the End (11–12)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("DAN")

META = {
  "id": "daniel", "order": 27, "name": "Daniel", "kanji": "ダニエル書", "thumb": "vol-daniel-", "book": "DAN",
  "title": "Daniel Volume", "volume": "Volume Twenty-Seven",
  "lede": "The twenty-seventh book of the Bible, in full: Daniel and his companions in the court of Babylon, the image of gold, silver, brass, iron and clay, the burning fiery furnace, the writing on the wall, the den of lions, and the visions of the four beasts, the seventy weeks and the time of the end, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "A Stone Cut Out Without Hands", "range": "Daniel 1–2", "bible_chapters": [1, 2],
     "blurb": "Jerusalem besieged and the vessels carried to Shinar; Daniel, Hananiah, Mishael and Azariah in the king's palace, renamed, who would not defile themselves with the king's dainties — prove thy servants ten days; then Nebuchadnezzar's dream that none could tell, the decree to slay the wise men, the secret revealed in a vision of the night, and the great image: head of gold, breast of silver, belly of brass, legs of iron, feet of iron and clay, and the stone that became a great mountain."},
  ],
}
