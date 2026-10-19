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
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Burning Fiery Furnace", "range": "Daniel 3–4", "bible_chapters": [3, 4],
     "blurb": "The image of gold in the plain of Dura, and the cornet, flute, harp, sackbut, psaltery and dulcimer; three men who would not bow down — our God whom we serve is able to deliver us, but if not; the furnace heated seven times more, and four men loose walking in the midst of the fire; then the king's own letter: the tree whose height reached unto heaven, the watcher and the holy one, is not this great Babylon?, seven times, and the King of heaven praised."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Den of Lions", "range": "Daniel 5–6", "bible_chapters": [5, 6],
     "blurb": "Belshazzar's feast with the vessels of the temple, and the writing upon the plaster of the wall; the queen remembers Daniel — let thy gifts be to thyself: MENE, MENE, TEKEL, UPHARSIN; in that night Belshazzar slain; then Darius the Mede, the presidents' plot and the interdict signed; Daniel at his windows open toward Jerusalem; the den and the sealed stone; O Daniel, servant of the living God — my God hath sent his angel, and hath shut the lions' mouths."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Ancient of Days", "range": "Daniel 7–8", "bible_chapters": [7, 8],
     "blurb": "The four winds upon the great sea and four great beasts coming up, the lion, the bear, the leopard, and the fourth with iron teeth and ten horns; thrones placed, and one that was ancient of days did sit — his throne was fiery flames; one like unto a son of man with the clouds of heaven; a time and times and half a time; then by the river Ulai the ram with two horns and the he-goat from the west, two thousand and three hundred evenings and mornings, and Gabriel: understand, O son of man."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "Seventy Weeks", "range": "Daniel 9–10", "bible_chapters": [9, 10],
     "blurb": "Jeremiah's seventy years, and Daniel in sackcloth and ashes: we have sinned, and have dealt perversely — O Lord, hear; O Lord, forgive; Gabriel caused to fly swiftly about the time of the evening oblation: seventy weeks are decreed upon thy people; then by the great river Hiddekel a man clothed in linen, his face as the appearance of lightning — the prince of Persia withstood me, but Michael came to help me; O man greatly beloved, fear not."},
  ],
}
