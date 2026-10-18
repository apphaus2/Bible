"""The 1 Samuel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative throughout, laid out by discourse.pack with the sa1.common helpers (as Judges), lifting the digest's two 1 Samuel
books ("A1".."A9": Hannah to Saul anointed; "B1".."B10": David to Gilboa) where they fit; new drawings in sa1/art.py.
Hannah's song (2:1–10) and David's words are in song boxes and speech boxes; God's words in the Voice box. Restraint:
Eli's death (4:18) is the overturned seat by the gate; Agag (15:33), Goliath's head (17:46, 17:51, 17:54, 17:57), the
priests of Nob (22:18–19), the Amalekite raid's dead and Saul's death on Gilboa (31) are words over landscapes, a fallen
giant, smoke, or the crown and spear on the mountain.

Plan (24,830 words, fourteen chapters): 1 Hannah (1–2) · 2 Speak, Jehovah (3–5) · 3 Give Us a King (6–8) · 4 Saul
Anointed (9–10) · 5 To Obey Is Better (11–13) · 6 Jonathan at Michmash (14) · 7 Jehovah Looketh on the Heart (15–16) ·
8 Goliath (17) · 9 Saul Hath Slain His Thousands (18–19) · 10 Jonathan and David (20–21) · 11 The Cave (22–24) ·
12 Abigail (25–26) · 13 The Witch of Endor (27–29) · 14 Mount Gilboa (30–31)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1SA")

META = {
  "id": "1samuel", "order": 9, "name": "1 Samuel", "kanji": "サムエル記上", "thumb": "vol-1samuel-", "book": "1SA",
  "title": "1 Samuel Volume", "volume": "Volume Nine",
  "lede": "The ninth book of the Bible, in full: Hannah's son Samuel, the ark among the Philistines, Saul the first king, and David the shepherd, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Hannah", "range": "1 Samuel 1–2", "bible_chapters": [1, 2],
     "blurb": "Hannah in bitterness of soul at Shiloh, her vow, and Eli marking her mouth; Samuel born and lent to Jehovah — for this child I prayed; Hannah's song; the sons of Eli and the flesh-hook; the child Samuel in his linen ephod; and the man of God: them that honor me I will honor."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Speak, Jehovah", "range": "1 Samuel 3–5", "bible_chapters": [3, 4, 5],
     "blurb": "The lamp of God not yet gone out: Samuel, Samuel — speak; for thy servant heareth. The ark fetched from Shiloh and taken at Eben-ezer; Eli fallen by the gate; Ichabod, the glory is departed; Dagon fallen before the ark, and the ark carried about Ashdod, Gath and Ekron."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Give Us a King", "range": "1 Samuel 6–8", "bible_chapters": [6, 7, 8],
     "blurb": "The ark sent home on a new cart with golden tumors and mice, two milch kine lowing on the straight way to Beth-shemesh; Mizpah, the great thunder, and the stone Eben-ezer: hitherto hath Jehovah helped us. Then the elders at Ramah: make us a king to judge us like all the nations."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Saul Anointed", "range": "1 Samuel 9–10", "bible_chapters": [9, 10],
     "blurb": "Kish's asses lost, and Saul, higher than any of the people, sent to seek them; the seer at the high place and the thigh reserved for him; the vial of oil; the band of prophets — is Saul also among the prophets?; the lot at Mizpah, Saul hid among the baggage, and long live the king."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "To Obey Is Better", "range": "1 Samuel 11–13", "bible_chapters": [11, 12, 13],
     "blurb": "Nahash at Jabesh-gilead and Saul following the oxen out of the field; the kingdom renewed at Gilgal; Samuel's farewell — whose ox have I taken? — and thunder in wheat harvest; the Philistines as the sand at Michmash, Saul's burnt-offering, and a man after his own heart; no smith in all the land."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Jonathan at Michmash", "range": "1 Samuel 14", "bible_chapters": [14],
     "blurb": "Jonathan and his armorbearer climb between the crags Bozez and Seneh — there is no restraint to Jehovah to save by many or by few; the earth quaked; Saul's rash oath, the honey in the forest, the lot that took Jonathan, and the people who rescued him."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Jehovah Looketh on the Heart", "range": "1 Samuel 15–16", "bible_chapters": [15, 16],
     "blurb": "Saul spares Agag and the best of Amalek's flocks: what meaneth this bleating of the sheep? To obey is better than sacrifice; the skirt rent and the kingdom rent from Saul. Then Samuel at Beth-lehem with his horn of oil, Jesse's sons passing by, the youngest fetched from the sheep, and David's harp before Saul."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Goliath", "range": "1 Samuel 17", "bible_chapters": [17],
     "blurb": "The vale of Elah and the champion of Gath, six cubits and a span, defying the armies of Israel forty days; a shepherd boy with parched grain and loaves; the lion and the bear; five smooth stones out of the brook; in the name of Jehovah of hosts — for the battle is Jehovah's."},
  ],
}
