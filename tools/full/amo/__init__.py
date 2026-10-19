"""The Amos volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ch02.py).

Built with dan.kit (the Daniel volume's line and panel builders) and job.jdiscourse's packing. Amos's own words are song
boxes in his colour, tagged AMOS; Jehovah's words (thus saith Jehovah …) the Voice box; Amaziah's words his own colour.
For three transgressions, yea, for four: a technical map of the nations round Israel, each lit in turn with fire on its
wall (amo.art.nations); the plumb-line as a blueprint of the wall and the line hanging, with no hand drawn (7:7); the
basket of summer fruit; Amaziah of Beth-el and the herdsman of Tekoa. Restraint: 1:13 and 2:1 words over the burning walls;
2:16 the mighty fleeing drawn clothed; 6:9–10 words over an empty house; 7:17 and 8:3 words over Beth-el and the silent
court; 9:1 the altar and its capitals only — the Lord is never drawn, nor any hand; God is never drawn.

Plan (4,163 words, two chapters): 1 For Three Transgressions (1–4) · 2 The Plumb-line (5–9)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("AMO")

META = {
  "id": "amos", "order": 30, "name": "Amos", "kanji": "アモス書", "thumb": "vol-amos-", "book": "AMO",
  "title": "Amos Volume", "volume": "Volume Thirty",
  "lede": "The thirtieth book of the Bible, in full: the herdsman of Tekoa — for three transgressions, yea, for four; the lion hath roared, who will not fear?; ye kine of Bashan; prepare to meet thy God, O Israel; let justice roll down as waters; the plumb-line, the basket of summer fruit and Amaziah of Beth-el; and the tabernacle of David raised up, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "For Three Transgressions", "range": "Amos 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "The words of Amos, among the herdsmen of Tekoa, two years before the earthquake: Jehovah will roar from Zion; for three transgressions of Damascus, of Gaza, of Tyre, of Edom, of Ammon, of Moab, of Judah — and of Israel, that sold the righteous for silver and the needy for a pair of shoes; shall two walk together, except they have agreed?; the lion hath roared, who will not fear?; ye kine of Bashan; yet have ye not returned unto me; prepare to meet thy God, O Israel."},
  ],
}
