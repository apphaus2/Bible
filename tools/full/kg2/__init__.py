"""The 2 Kings volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative laid out by discourse.pack with the kg2.common helpers (as 1 Kings, whose faces and drawings it reuses: kg1.common,
kg1.art); new drawings in kg2/art.py. The reigns of the kings are roll cells (kg2.common.reign: Judah gold, Israel red).
Restraint: the fifties consumed (1:10–12), the she-bears (2:24), the king of Moab's son (3:27), the siege's famine (6:28–29),
Jezebel (9:33–37), the heads at Jezreel (10:7–8), Athaliah (11:16), the sons of Zedekiah (25:7) are words over landscapes,
walls, windows, gates or smoke; God is never drawn.

Plan (23,321 words, thirteen chapters): 1 The Chariot of Fire (1–2) · 2 The Pot of Oil (3–4) · 3 Naaman (5–6) · 4 The
Siege of Samaria (7–8) · 5 Jehu (9–10) · 6 Joash (11–12) · 7 The Bones of Elisha (13–14) · 8 Ahaz (15–16) · 9 Carried Away
into Assyria (17) · 10 Hezekiah (18–19) · 11 The Shadow on the Dial (20–21) · 12 Josiah (22–23) · 13 The Fall of Jerusalem
(24–25)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2KI")

META = {
  "id": "2kings", "order": 12, "name": "2 Kings", "kanji": "列王記下", "thumb": "vol-2kings-", "book": "2KI",
  "title": "2 Kings Volume", "volume": "Volume Twelve",
  "lede": "The twelfth book of the Bible, in full: Elijah taken up in the whirlwind, Elisha's wonders, Jehu's furious driving, Hezekiah and Josiah, and Jerusalem burned by Babylon, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Chariot of Fire", "range": "2 Kings 1–2", "bible_chapters": [1, 2],
     "blurb": "Ahaziah fallen through the lattice inquires of Baal-zebub; a hairy man girt with a girdle of leather; fire from heaven on the captains of fifty; then Gilgal, Beth-el and Jericho — I will not leave thee; the Jordan divided by the mantle; a double portion of thy spirit; a chariot of fire and horses of fire, and Elijah went up by a whirlwind into heaven."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Pot of Oil", "range": "2 Kings 3–4", "bible_chapters": [3, 4],
     "blurb": "Three kings in the wilderness of Edom without water — bring me a minstrel; the valley full of trenches and the water red as blood; the widow's pot of oil and the borrowed vessels; the great woman of Shunem and the little chamber on the wall; my head, my head; it is well; the child sneezed seven times; death in the pot, and twenty loaves for a hundred men."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Naaman", "range": "2 Kings 5–6", "bible_chapters": [5, 6],
     "blurb": "Naaman the leper and the little maiden of Israel; go and wash in the Jordan seven times — are not Abanah and Pharpar better?; his flesh came again like the flesh of a little child; Gehazi's lie and the leprosy white as snow; the axe-head that swam; Dothan and the mountain full of horses and chariots of fire; and the siege of Samaria."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Siege of Samaria", "range": "2 Kings 7–8", "bible_chapters": [7, 8],
     "blurb": "To-morrow a measure of fine flour for a shekel — if Jehovah should make windows in heaven; four leprous men at the gate and the camp of the Syrians empty in the twilight; this day is a day of good tidings; the Shunammite's land restored; Hazael and the forty camels' burden, and the man of God wept; and the kings Jehoram and Ahaziah of Judah."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "Jehu", "range": "2 Kings 9–10", "bible_chapters": [9, 10],
     "blurb": "The vial of oil poured on Jehu's head in an inner chamber — I have anointed thee king over Israel; is it peace?; the driving is like the driving of Jehu the son of Nimshi, for he driveth furiously; the portion of Naboth; Jezebel at the window; the seventy sons; and the house of Baal broken down."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Joash", "range": "2 Kings 11–12", "bible_chapters": [11, 12],
     "blurb": "Athaliah destroys the seed royal, and Jehosheba hides the child Joash six years in the house of Jehovah; Jehoiada's covenant with the captains; the crown and the testimony — long live the king; Athaliah's cry, Treason! treason!; then Jehoash and the breaches of the house, the chest with a hole in its lid, and the hallowed things sent to Hazael."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The Bones of Elisha", "range": "2 Kings 13–14", "bible_chapters": [13, 14],
     "blurb": "Elisha sick unto death — my father, my father, the chariots of Israel; the arrow of victory shot out of the window eastward, and the ground smitten thrice; the dead man who touched the bones of Elisha and revived; Amaziah and the parable of the thistle and the cedar of Lebanon; the wall of Jerusalem broken down; and Jeroboam the son of Joash."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Ahaz", "range": "2 Kings 15–16", "bible_chapters": [15, 16],
     "blurb": "Azariah the leper king in his separate house; Zechariah, Shallum, Menahem, Pekahiah and Pekah, king after king in Samaria; Pul and Tiglath-pileser of Assyria; then Ahaz — I am thy servant and thy son; the altar after the fashion of the altar at Damascus, and the sea set down from off the brazen oxen."},
  ],
}
