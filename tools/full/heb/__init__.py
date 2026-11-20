"""The Hebrews volume of the full edition (the Epistle to the Hebrews): metadata, the volume cover, and the chapter plans
(ch01.py … ch04.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit; the letter box, the sealed scroll, the doxology panel),
as Romans and Galatians are — with one difference: Hebrews names no writer, so no writer is drawn. There is no face of Paul,
no study, no scribe: every panel is a drawing (K.D), a plate, or a glory panel, and the letter's own words go in the kit's
letter boxes (parchment, a sepia rule down the left edge), untailed, over the old covenant's images made visible. The book
opens on the letter itself, a sealed scroll carried along the road to a city on its hill, and closes on Timothy set at
liberty (13:23) and "they of Italy" (13:24).

The Voice box and the song box. Hebrews is mostly scripture quoted as God speaking; each quotation was set case by case:
  * the Voice box (God's own words, first person, or addressed by him to the Son): 1:5 (both sayings), 1:6, 1:8–9, 1:10–12,
    1:13; 3:7–11 and its repetitions 3:15, 4:3, 4:5, 4:7 ("To-day if ye shall hear his voice … they shall not enter into my
    rest": the Holy Spirit's words, God speaking of "my works", "my ways", "my rest"); 5:5, 5:6, 7:17 and 7:21's oath (Thou
    art a priest for ever); 6:14 (Surely blessing I will bless thee); 8:5 (See, saith he, that thou make all things); 8:8–12
    and 10:16–17 (the new covenant); 10:30 (Vengeance belongeth unto me); 10:37–38 (my righteous one shall live by faith);
    11:18 (In Isaac shall thy seed be called); 12:20 (the word enjoined at Sinai: if even a beast touch the mountain); 12:26
    (Yet once more will I make to tremble); 13:5 (I will in no wise fail thee);
  * song boxes (scripture quoted in the third person, or by a man): 1:7 (Who maketh his angels winds); 2:6–8 (What is man);
    4:4 (And God rested on the seventh day); 7:21's opening (The Lord sware and will not repent himself); 9:20 (Moses: This is
    the blood of the covenant); 10:30b (The Lord shall judge his people); 12:5–6 (My son, regard not lightly); 12:21 (Moses:
    I exceedingly fear and quake); 13:6 (The Lord is my helper);
  * ordinary speech balloons (Christ's words, as the kit sets them): 2:12–13 (I will declare thy name unto my brethren …
    Behold, I and the children whom God hath given me) and 10:5–7, 10:9 (Lo, I am come to do thy will).

Restraint: God is never drawn — light, a throne standing empty in light, fire, the Voice box. The devil (2:14) is words only.
Angels are figures of white light with a gold rim and no face (no wings: the text gives none). Jesus, where he is drawn, is
the risen Christ in white light (co1.art5.risen_fig: ntcast's look); his death (2:9, 12:2, 13:12) only the hill of the three
crosses far off under a darkened sky. Sacrifices are altars, smoke and vessels: no beast slain and no blood drawn — "blood"
(9:7–28, 10:4, 10:19, 12:24, 13:11–12, 13:20) is in the words only; the high priest goes in with a censer and the bowl.
10:26–31 (judgment) is words over fire on a dark field; 11:35–38 (tortured, stoned, sawn asunder, slain with the sword) words
over empty places — the desert, the mountains, the caves and dens of the earth; 12:4 (not yet resisted unto blood) words
over the empty stadium track; 12:5–11 (chastening) words over a household at peace, no blow drawn; 12:16 Esau and his mess of
pottage, no more; 13:4 words over a shut door. Rahab is drawn as Joshua draws her (her window and its scarlet line).

Drawings: see heb/art.py … art4.py; the cast as the Old Testament volumes and ntcast draw them (Moses as Exodus draws him,
Aaron in the high priest's garments with the white mitre, Abraham's grey beard and slate-blue robe, Melchizedek in white
with a gold band and crown, Esau's red curls, the three men at Mamre white with gold rims and no faces).

Plan (7,030 words, four chapters): 1 Better than the Angels (1–4) · 2 A Priest for Ever after the Order of Melchizedek (5–8)
· 3 The Way into the Holy Place (9–10) · 4 So Great a Cloud of Witnesses (11–13)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("HEB")

META = {
  "id": "hebrews", "order": 58, "name": "Hebrews", "kanji": "ヘブル人への手紙", "thumb": "vol-hebrews-", "book": "HEB",
  "title": "Hebrews Volume", "volume": "Volume Fifty-Eight",
  "lede": "The fifty-eighth book of the Bible, in full: the letter to the Hebrews — God, who spake of old time unto the fathers in the prophets, hath spoken unto us in his Son, better than the angels; to-day if ye shall hear his voice; the word of God sharper than any two-edged sword; a great high priest, a priest for ever after the order of Melchizedek; the true tabernacle and the new covenant; the way into the holy place through the veil; faith, the assurance of things hoped for, and so great a cloud of witnesses; let us run with patience the race, looking unto Jesus; mount Zion and the heavenly Jerusalem; and the great shepherd of the sheep, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Better than the Angels", "range": "Hebrews 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "God, having of old time spoken unto the fathers in the prophets, hath at the end of these days spoken unto us in his Son, the effulgence of his glory; better than the angels — Thou art my Son, let all the angels of God worship him, sit thou on my right hand; so great a salvation; Jesus crowned with glory and honor; Moses faithful in all his house; to-day if ye shall hear his voice, harden not your hearts; a sabbath rest for the people of God; the word of God sharper than any two-edged sword; the throne of grace."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "A Priest for Ever after the Order of Melchizedek", "range": "Hebrews 5–8", "bible_chapters": [5, 6, 7, 8],
     "blurb": "Every high priest taken from among men; thou art a priest for ever after the order of Melchizedek; milk and solid food; press on unto perfection; the oath to Abraham, surely blessing I will bless thee; the hope as an anchor of the soul, entering within the veil; Melchizedek king of Salem meeting Abraham, the tenth part of all; priests many in number, hindered by death, and one that abideth for ever; the pattern showed thee in the mount; the new covenant, I will put my laws into their mind."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Way into the Holy Place", "range": "Hebrews 9–10", "bible_chapters": [9, 10],
     "blurb": "The first tabernacle: the candlestick, the table and the showbread, the golden altar of incense, the ark of the covenant with the pot of manna, Aaron's rod that budded and the tables of the covenant, the cherubim of glory overshadowing the mercy-seat; the high priest alone, once in the year; Christ come through the greater tabernacle, not made with hands, into heaven itself; lo, I am come to do thy will; one sacrifice for sins for ever; a new and living way through the veil; my righteous one shall live by faith."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "So Great a Cloud of Witnesses", "range": "Hebrews 11–13", "bible_chapters": [11, 12, 13],
     "blurb": "Faith is assurance of things hoped for: Abel, Enoch, Noah; Abraham going out not knowing whither, Sarah, Isaac offered up; Isaac, Jacob and Joseph; Moses hid, choosing ill treatment with the people of God, the passover, the Red sea; Jericho's walls and Rahab; Gideon, Barak, Samson, Jephthah, David, Samuel and the prophets; let us run with patience the race, looking unto Jesus; the chastening of the Lord; Esau; not unto Sinai's fire but unto mount Zion, the heavenly Jerusalem; our God is a consuming fire; entertaining angels unawares; without the gate; the great shepherd of the sheep."},
  ],
}
META["chapters"] = [c for c in META["chapters"] if (pathlib.Path(__file__).parent / f"{c['module']}.py").exists()]   # TEMP while building
