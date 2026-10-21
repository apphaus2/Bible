"""The Habakkuk volume of the full edition: metadata, the volume cover, and the one chapter (ch01.py).

Built on the minor prophets' kit (oba/minor.py). Habakkuk's complaints (1:2–4, 1:12–17) and his watch (2:1) are song lines
beside his face; Jehovah's answers (1:5–11, 2:2–20, the five woes) are in the Voice box; the prayer of chapter 3 is all in
song boxes. Habakkuk: white hair and beard, an indigo headcloth with a cord (hab.common.HABAKKUK), an indigo robe at a
distance on his watchtower (hab.art.hab_fig). God is never drawn: in the prayer he is a blaze of light behind Teman and
Paran, rays, bolts, the sun and moon standing still, the sea heaped up — never a figure.

Plan (1,440 words, one chapter): 1 The Watchtower (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("HAB")

META = {
  "id": "habakkuk", "order": 35, "name": "Habakkuk", "kanji": "ハバクク書", "thumb": "vol-habakkuk-", "book": "HAB",
  "title": "Habakkuk Volume", "volume": "Volume Thirty-Five",
  "lede": "The thirty-fifth book of the Bible, in full: the burden which Habakkuk the prophet did see — O Jehovah, how long shall I cry?; the Chaldeans, that bitter and hasty nation; I will stand upon my watch; write the vision, and make it plain upon tablets — the righteous shall live by his faith; and the prayer of Habakkuk: though the fig-tree shall not flourish, yet I will rejoice in Jehovah — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Watchtower", "range": "Habakkuk 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "O Jehovah, how long shall I cry, and thou wilt not hear?; lo, I raise up the Chaldeans, whose horses are swifter than leopards; art not thou from everlasting, O Jehovah my God?; I will stand upon my watch, and set me upon the tower; write the vision, and make it plain upon tablets, that he may run that readeth it — the righteous shall live by his faith; the five woes, and Jehovah in his holy temple; then the prayer of Habakkuk: God came from Teman; though the fig-tree shall not flourish, yet I will rejoice in Jehovah."},
  ],
}
