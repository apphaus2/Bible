"""The Ezekiel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Most of the book is Jehovah's words to Ezekiel, set in the Voice box beside Ezekiel's face or over a drawing (ezk.common.run()
splits each verse automatically: "And the word of Jehovah came unto me, saying," in a caption, "Son of man, ..." in the Voice
box). Ezekiel's own narration is in captions; Ezekiel: a priest among the captives, grey-black beard, white headcloth with a
blue cord (ezk.common.EZEKIEL...). The vision by the river Chebar: the four living creatures (bronze figures in fire, four
wings), the wheels full of eyes, the firmament like crystal, the throne of sapphire and above it only fire and amber light,
never a figure (ezk.art.throne). God is never drawn, not even a hand (2:9 is the roll alone in the light). Restraint: the
slaughter of chapter 9 is words over the empty court; Oholah and Oholibah (16, 23) words only over the cities; the death of
Ezekiel's wife (24:16–18) words over the empty house; the sword and the slain words over walls, smoke and empty streets;
the birds' feast of 39 words over the empty field. The nations are maps (Tyre as the ship of 27); the new temple of 40–48 is
blueprint plates (exo.art8 bp/dim/tag); the division of the land is a map of the tribes' portions.

Plan (39,297 words, eighteen chapters): 1 The Visions of God (1–3) · 2 The Siege on a Tile (4–7) · 3 The Glory Departs
(8–11) · 4 Stuff for Removing (12–14) · 5 The Vine and the Foundling (15–16) · 6 The Eagles and the Cedar (17–19) ·
7 A Sword, a Sword (20–21) · 8 Oholah and Oholibah (22–23) · 9 The Desire of Thine Eyes (24–25) · 10 The Ship of Tyre
(26–28) · 11 Pharaoh King of Egypt (29–32) · 12 The Watchman and the Shepherds (33–34) · 13 The Valley of Dry Bones
(35–37) · 14 Gog (38–39) · 15 The Measuring Reed (40–42) · 16 The Glory Returns (43–44) · 17 The Holy Oblation (45–46) ·
18 Jehovah Is There (47–48)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("EZK")

META = {
  "id": "ezekiel", "order": 26, "name": "Ezekiel", "kanji": "エゼキエル書", "thumb": "vol-ezekiel-", "book": "EZK",
  "title": "Ezekiel Volume", "volume": "Volume Twenty-Six",
  "lede": "The twenty-sixth book of the Bible, in full: the visions of God by the river Chebar, the watchman of the house of Israel, the glory departing from the temple, the parables and the burdens of the nations, the valley of dry bones, and the house of the vision with the river flowing from under its threshold, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Visions of God", "range": "Ezekiel 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Among the captives by the river Chebar the heavens were opened: a stormy wind out of the north, the four living creatures, the wheels with their rims full of eyes, the firmament like the terrible crystal, and above it a throne of sapphire, fire and brightness — the appearance of the likeness of the glory of Jehovah; the roll of a book eaten, in the mouth as honey; and I have made thee a watchman unto the house of Israel."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Siege on a Tile", "range": "Ezekiel 4–7", "bible_chapters": [4, 5, 6, 7],
     "blurb": "Take thee a tile, and portray upon it a city, even Jerusalem: the forts and the mound and the iron pan; the prophet lying on his left side and on his right, each day for a year; the bread of the siege by weight; the hair shaven with a sword and divided in three; set thy face toward the mountains of Israel; and an end, the end is come upon the four corners of the land."},
  ],
}
