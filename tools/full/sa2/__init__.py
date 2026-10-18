"""The 2 Samuel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Narrative throughout, laid out by discourse.pack with the sa2.common helpers (as 1 Samuel), lifting the digest's two
2 Samuel books ("A1".."A9": Saul mourned to the ewe lamb; "B1".."B9": Absalom to Araunah's threshing-floor) where they fit;
new drawings in sa2/art.py. David's lament (1:19–27) and his song (22) are in song boxes; God's words in the Voice box.
Restraint: the Amalekite's death (1:15), the twelve at Gibeon (2:16), Asahel (2:23), Abner (3:27), Ish-bosheth (4:7–12),
Uzzah (6:7), Uriah (11:17), Amnon (13:28–29), Absalom in the oak (18:14–15), Amasa (20:10), Sheba (20:22) and the sons of
Saul (21:9) are words over landscapes, gates, empty rooms, smoke or a heap of stones; 11:2–4 and 13:11–14 are words over an
empty roof and a shut door.

Plan (20,573 words, twelve chapters): 1 How Are the Mighty Fallen (1–2) · 2 Abner (3–4) · 3 The City of David (5–6) ·
4 For Ever (7–8) · 5 Mephibosheth (9–10) · 6 Thou Art the Man (11–12) · 7 Absalom (13–14) ·
8 The Mount of Olives (15–16) · 9 O My Son Absalom (17–18) · 10 The King Returned (19–20) · 11 Jehovah Is My
Rock (21–22) · 12 Which Cost Me Nothing (23–24)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2SA")

META = {
  "id": "2samuel", "order": 10, "name": "2 Samuel", "kanji": "サムエル記下", "thumb": "vol-2samuel-", "book": "2SA",
  "title": "2 Samuel Volume", "volume": "Volume Ten",
  "lede": "The tenth book of the Bible, in full: David king in Hebron and in Jerusalem, the ark brought up with dancing, Bath-sheba and Nathan, Absalom's rebellion, and the threshing-floor of Araunah, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "How Are the Mighty Fallen", "range": "2 Samuel 1–2", "bible_chapters": [1, 2],
     "blurb": "The Amalekite out of Saul's camp with the crown and the bracelet; David rends his clothes; the song of the bow — how are the mighty fallen!; David anointed king over Judah in Hebron and Ish-bosheth made king at Mahanaim; the twelve by the pool of Gibeon, Asahel light of foot as a wild roe, and Abner's cry: shall the sword devour for ever?"},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Abner", "range": "2 Samuel 3–4", "bible_chapters": [3, 4],
     "blurb": "Long war between the house of Saul and the house of David; Abner's wrath — am I a dog's head?; Michal taken from Paltiel, who followed her weeping to Bahurim; Abner's league and the feast in Hebron; Joab takes him aside in the gate; David follows the bier: should Abner die as a fool dieth?; Mephibosheth lamed in the flight, and Ish-bosheth slain at noon."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The City of David", "range": "2 Samuel 5–6", "bible_chapters": [5, 6],
     "blurb": "All the tribes at Hebron — we are thy bone and thy flesh — and David anointed king over Israel; the stronghold of Zion; Hiram's cedar; Baal-perazim and the sound of marching in the tops of the mulberry-trees; the ark on a new cart and Uzzah at the threshing-floor of Nacon; David dancing before Jehovah with all his might, and Michal at the window."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "For Ever", "range": "2 Samuel 7–8", "bible_chapters": [7, 8],
     "blurb": "I dwell in a house of cedar, but the ark of God dwelleth within curtains: the word of Jehovah to Nathan by night — I took thee from the sheepcote; he shall build a house for my name, and I will establish the throne of his kingdom for ever; David before Jehovah: who am I?; and David's wars from the Philistines to the River."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "Mephibosheth", "range": "2 Samuel 9–10", "bible_chapters": [9, 10],
     "blurb": "Is there yet any that is left of the house of Saul, that I may show him kindness for Jonathan's sake?; Ziba; Mephibosheth fallen on his face — fear not; he shall eat at my table as one of the king's sons; Hanun shames David's servants — tarry at Jericho until your beards be grown; Joab before Rabbah: be of good courage, and let us play the man."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Thou Art the Man", "range": "2 Samuel 11–12", "bible_chapters": [11, 12],
     "blurb": "At the time when kings go out to battle David tarried at Jerusalem; the roof at eventide and Bath-sheba; Uriah sleeping at the king's door; the letter sent by Uriah's hand; the poor man's one little ewe lamb — thou art the man; I have sinned against Jehovah; the child's seventh day, Solomon whom Jehovah loved, and the crown of Rabbah."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Absalom", "range": "2 Samuel 13–14", "bible_chapters": [13, 14],
     "blurb": "Amnon's sickness for his sister Tamar and Jonadab's subtle counsel; Tamar's cakes, the shut door, and her garment of divers colors rent; Absalom's two full years and the shearers' feast at Baal-hazor; Absalom fled to Geshur; the wise woman of Tekoa — we must needs die, and are as water spilt on the ground; and no blemish in him from the sole of his foot to the crown of his head."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "The Mount of Olives", "range": "2 Samuel 15–16", "bible_chapters": [15, 16],
     "blurb": "Absalom beside the way of the gate — oh that I were made judge in the land — steals the hearts of the men of Israel; Absalom is king in Hebron; arise, and let us flee; Ittai: whether for death or for life; the ark carried back over the Kidron; David going up the mount of Olives weeping and barefoot; Ziba's asses, Shimei's stones, and Ahithophel's counsel."},
  ],
}
