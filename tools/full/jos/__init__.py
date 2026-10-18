"""The Joshua volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Joshua is narrative, then lists. The story chapters (1–11, 22–24) are laid out by discourse.pack: captions, speech boxes
beside a close-up face or over a drawing, Jehovah's words in Voice boxes. The lists — the kings smitten (12), the land that
remaineth (13), the borders and cities of the tribes (15–19), the cities of the Levites (21) — are roll pages (rolls.py):
one cell per border or group of cities, every word. Art: the digest's Jericho book is lifted where it fits (reuse.fill);
new drawings are in jos/art.py. Joshua as leader: rust-red headcloth with a cord, black beard (joshua1 tokens).

Plan (18,685 words, ten chapters): 1 Be Strong and of Good Courage (1–2) · 2 The Waters of the Jordan (3–5) ·
3 The Walls of Jericho (6–7) · 4 Ai and the Gibeonites (8–9) · 5 The Sun Stood Still (10–11) · 6 The Land That Remaineth
(12–14) · 7 The Lot of Judah (15–17) · 8 The Lots of the Seven Tribes (18–19) · 9 The Cities of Refuge (20–22) ·
10 Choose You This Day (23–24)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JOS")

META = {
  "id": "joshua", "order": 6, "name": "Joshua", "kanji": "ヨシュア記", "thumb": "vol-joshua-", "book": "JOS",
  "title": "Joshua Volume", "volume": "Volume Six",
  "lede": "The sixth book of the Bible, in full: Israel over the Jordan, Jericho, the conquest and the dividing of the land, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Be Strong and of Good Courage", "range": "Joshua 1–2", "bible_chapters": [1, 2],
     "blurb": "Moses my servant is dead: now therefore arise, go over this Jordan; be strong and of good courage. The two spies in Jericho, Rahab's house upon the wall, the stalks of flax on the roof, the cord through the window and the line of scarlet thread."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Waters of the Jordan", "range": "Joshua 3–5", "bible_chapters": [3, 4, 5],
     "blurb": "The ark goes before, and the waters that come down from above stand in one heap; all Israel passes over on dry ground; twelve stones out of the midst of the Jordan set up in Gilgal; the passover in the plains of Jericho, the manna ceased, and the prince of the host of Jehovah with his sword drawn."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Walls of Jericho", "range": "Joshua 6–7", "bible_chapters": [6, 7],
     "blurb": "Seven priests with seven trumpets of rams' horns compass the city seven days; the great shout, and the wall falls down flat; Rahab and her father's household saved alive. Then the devoted thing: the flight before Ai, the lot that takes Achan, the Babylonish mantle and the wedge of gold, and the valley of Achor."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Ai and the Gibeonites", "range": "Joshua 8–9", "bible_chapters": [8, 9],
     "blurb": "An ambush behind the city and the javelin stretched out toward Ai; the smoke of the city ascending up to heaven; an altar of unhewn stones in mount Ebal and the law read before all Israel; then the Gibeonites with mouldy bread and rent wine-skins, a covenant made without asking counsel at the mouth of Jehovah, and the hewers of wood and drawers of water."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Sun Stood Still", "range": "Joshua 10–11", "bible_chapters": [10, 11],
     "blurb": "Five kings against Gibeon; a night march from Gilgal and great stones from heaven; Sun, stand thou still upon Gibeon, and thou, Moon, in the valley of Aijalon; the cave at Makkedah; the southern cities taken one by one; then the kings of the north at the waters of Merom, Hazor burnt, and the land had rest from war."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Land That Remaineth", "range": "Joshua 12–14", "bible_chapters": [12, 13, 14],
     "blurb": "The kings smitten beyond the Jordan and the thirty and one kings on this side; Joshua old and well stricken in years, and very much land yet to be possessed; the inheritance of Reuben, Gad and the half-tribe of Manasseh beyond the Jordan; and Caleb at fourscore and five: give me this hill-country."},
  ],
}
