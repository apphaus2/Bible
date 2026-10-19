"""The Zechariah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py … ch04.py).

Built on the minor prophets' kit (oba/minor.py). Zechariah tells his night visions in the first person: his narration is in
captions, his questions and the angels' answers in speech boxes, Jehovah's words in the Voice box. Zechariah: a black
beard and a slate-teal headcloth with a cord (ezr.common.ZECHARIAH). The visions are luminous symbolic plates (zec.art.vision:
a night field with a faint grid, the drawing glowing, a numbered title tag): the horses among the myrtles, the four horns
and the four smiths, the measuring line and the wall of fire, Joshua the high priest, the stone of seven eyes, the
candlestick and the two olive-trees, the flying roll, the ephah, the four chariots. Angels are shapes of white light with
no faces; the adversary of 3:1 a faceless shadow; God is never drawn. Restraint: the slain of 11:4–9 and 13:7–9 and the
plague of 14:12 are words over empty pasture, the scattered flock and the bare hills.

Plan (6,322 words, four chapters): 1 The Night Visions (1–4) · 2 The Four Chariots (5–8) · 3 Thy King Cometh (9–11) ·
4 The Day of Jehovah (12–14)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ZEC")

META = {
  "id": "zechariah", "order": 38, "name": "Zechariah", "kanji": "ゼカリヤ書", "thumb": "vol-zechariah-", "book": "ZEC",
  "title": "Zechariah Volume", "volume": "Volume Thirty-Eight",
  "lede": "The thirty-eighth book of the Bible, in full: the night visions of Zechariah — the horses among the myrtles, the measuring line, Joshua the high priest, the candlestick of gold and the two olive-trees, the flying roll and the four chariots; then thy king cometh unto thee, lowly, and riding upon an ass; the thirty pieces of silver; a fountain opened; and the day of Jehovah, when his feet shall stand upon the mount of Olives — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Night Visions", "range": "Zechariah 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "Return unto me, and I will return unto you; a man riding upon a red horse among the myrtle-trees in the bottom; four horns and four smiths; a man with a measuring line — I will be unto her a wall of fire round about; Joshua the high priest in filthy garments, and a clean mitre upon his head; the stone with seven eyes; a candlestick all of gold and two olive-trees — not by might, nor by power, but by my Spirit, saith Jehovah of hosts."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Four Chariots", "range": "Zechariah 5–8", "bible_chapters": [5, 6, 7, 8],
     "blurb": "A flying roll, twenty cubits long; the ephah and the woman sitting in it, carried to the land of Shinar; four chariots coming out from between two mountains of brass; crowns for Joshua — behold, the man whose name is the Branch; the men of Bethel asking of the fasts — execute true judgment, and show kindness; I am returned unto Zion: old men and old women in the streets of Jerusalem, and boys and girls playing; ten men shall take hold of the skirt of a Jew."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Thy King Cometh", "range": "Zechariah 9–11", "bible_chapters": [9, 10, 11],
     "blurb": "The burden upon Hadrach, Tyre and the Philistines; rejoice greatly, O daughter of Zion: behold, thy king cometh unto thee, lowly, and riding upon an ass, even upon a colt the foal of an ass; prisoners of hope; ask ye of Jehovah rain in the time of the latter rain; I will hiss for them and gather them; open thy doors, O Lebanon; the flock of slaughter, the two staves Beauty and Bands, and the thirty pieces of silver cast unto the potter."},
    # {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Day of Jehovah", "range": "Zechariah 12–14", "bible_chapters": [12, 13, 14],
     # "blurb": "Jerusalem a cup of reeling and a burdensome stone; they shall look unto me whom they have pierced, and mourn, every family apart; in that day a fountain opened for sin and for uncleanness; smite the shepherd, and the sheep shall be scattered; his feet shall stand upon the mount of Olives, and it shall be cleft in the midst; living waters shall go out from Jerusalem; Jehovah shall be King over all the earth; and upon the bells of the horses, HOLY UNTO JEHOVAH."},
  ],
}
