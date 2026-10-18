"""The Deuteronomy volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Deuteronomy is Moses' discourses in the plains of Moab. His words are set in speech panels (speech.orate: his face, a
column of rounded speech boxes), with God's words in Voice boxes where he quotes Jehovah; flashback panels (Horeb, Kadesh,
Sihon and Og, the golden calf) reuse the Exodus and Numbers art. The laws of 12–26 are law cells in the spoken style
(exo.kit.law_pages(..., spoken=True)): they are Moses' words, so they are not set in the Voice box.

Plan (27,953 words, fifteen chapters): 1 These Are the Words (1–2) · 2 Take Heed to Thyself (3–4) · 3 Hear, O Israel (5–6) ·
4 A People for His Own Possession (7–8) · 5 The Tables of Stone (9–10) · 6 The Place Which Jehovah Shall Choose (11–12) ·
7 The Year of Release (13–15) · 8 Justice, Only Justice (16–18) · 9 When Thou Goest Forth to Battle (19–21) ·
10 Thou Shalt Not (22–23) · 11 The Basket of First-fruits (24–26) · 12 The Blessings and the Curses (27–28) ·
13 Choose Life (29–31) · 14 The Song of Moses (32) · 15 The Death of Moses (33–34)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("DEU")

META = {
  "id": "deuteronomy", "order": 5, "name": "Deuteronomy", "kanji": "申命記", "thumb": "vol-deuteronomy-", "book": "DEU",
  "title": "Deuteronomy Volume", "volume": "Volume Five",
  "lede": "The fifth book of the Bible, in full: Moses' words to Israel in the plains of Moab, every one in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "These Are the Words", "range": "Deuteronomy 1–2", "bible_chapters": [1, 2],
     "blurb": "In the fortieth year, beyond the Jordan, Moses begins to declare the law: Horeb, the judges, the spies and the evil report at Kadesh-barnea, the defeat at Hormah, the long way round Seir, Moab and Ammon, and Sihon king of Heshbon delivered up."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Take Heed to Thyself", "range": "Deuteronomy 3–4", "bible_chapters": [3, 4],
     "blurb": "Og king of Bashan and his bedstead of iron; the land beyond the Jordan given to Reuben, Gad and half Manasseh; Moses' prayer to go over, and Pisgah; ye saw no manner of form on the day that Jehovah spake unto you in Horeb; a devouring fire, a jealous God; and the cities of refuge beyond the Jordan."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Hear, O Israel", "range": "Deuteronomy 5–6", "bible_chapters": [5, 6],
     "blurb": "The covenant made at Horeb and the ten commandments spoken out of the midst of the fire; go thou near, and hear; Hear, O Israel: Jehovah our God is one Jehovah, and thou shalt love Jehovah thy God with all thy heart; the words upon the door-posts; and when thy son asketh thee in time to come."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "A People for His Own Possession", "range": "Deuteronomy 7–8", "bible_chapters": [7, 8],
     "blurb": "Seven nations greater and mightier than thou, and the hornet sent before thee; Jehovah set his love upon you, not because ye were more in number; the manna and the forty years — man doth not live by bread only; and a good land of wheat and barley, vines and fig-trees and pomegranates: beware lest thou forget."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Tables of Stone", "range": "Deuteronomy 9–10", "bible_chapters": [9, 10],
     "blurb": "Not for thy righteousness: the golden calf at Horeb remembered, the tables cast down and broken, Moses fallen down before Jehovah forty days and forty nights; the tables hewn again and put in the ark; and now, Israel, what doth Jehovah thy God require of thee?"},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Place Which Jehovah Shall Choose", "range": "Deuteronomy 11–12", "bible_chapters": [11, 12],
     "blurb": "A land of hills and valleys that drinketh water of the rain of heaven; lay up these my words in your heart; I set before you this day a blessing and a curse, on Gerizim and on Ebal; and the place which Jehovah your God shall choose out of all your tribes, to put his name there."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The Year of Release", "range": "Deuteronomy 13–15", "bible_chapters": [13, 14, 15],
     "blurb": "The prophet and the dreamer of dreams that saith, Let us go after other gods; ye are the children of Jehovah your God; the clean and the unclean; the tithe; at the end of every seven years a release, for the poor shall never cease out of the land; the Hebrew servant; and the firstlings."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Justice, Only Justice", "range": "Deuteronomy 16–18", "bible_chapters": [16, 17, 18],
     "blurb": "Three times in a year: the passover, the feast of weeks and the feast of tabernacles; judges and officers in all thy gates — justice, only justice; the matter too hard, the king that shall write him a copy of this law, the portion of the priests, the abominations of the nations, and a prophet like unto me."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "When Thou Goest Forth to Battle", "range": "Deuteronomy 19–21", "bible_chapters": [19, 20, 21],
     "blurb": "The cities of refuge, thy neighbor's landmark and the two witnesses; when thou goest forth to battle, be not afraid; the fruit-trees in a siege; the one found slain in the field; the captive woman, the right of the first-born, the stubborn son, and him that is hanged on a tree."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "Thou Shalt Not", "range": "Deuteronomy 22–23", "bible_chapters": [22, 23],
     "blurb": "Thy brother's ox gone astray, a battlement for thy roof, no mingled seed or stuff, fringes upon the four borders; the laws of marriage; who shall not enter into the assembly of Jehovah; the camp kept holy; the servant that is escaped, usury, vows, and thy neighbor's vineyard."},
    {"module": "ch11", "dir": "chapter-11", "num": "11", "name": "The Basket of First-fruits", "range": "Deuteronomy 24–26", "bible_chapters": [24, 25, 26],
     "blurb": "The bill of divorcement, the millstone taken to pledge, the hired servant's wages, the sheaf forgotten in the field for the sojourner, the fatherless and the widow; the ox that treadeth out the grain; just weights; remember what Amalek did; and the basket of first-fruits: A Syrian ready to perish was my father."},
  ],
}
