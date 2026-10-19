"""The Psalms volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Every psalm opens with its head (PSALM N, 第N篇, and the superscription cut from ref/asv by psa.text — superscriptions are
not verses in asv.Book, so they are labels); its verses are song boxes (psa.layout "song" lines, one poetic line to a row)
over drawings taken from the psalm (psa.art.SCENES: the tree by the streams, the shepherd and the still waters, the
heavens, the deep, the hart at the brooks, the sparrow at the altar, the harp on the willows …) or beside the singer's face
(David from 2 Samuel; Asaph, the sons of Korah, Heman and Ethan as Levite singers in white; Moses for Psalm 90; Solomon for
72 and 127). God's words quoted in a psalm go in the Voice box. God is never drawn: light, rays, cloud, storm and creation.
Restraint: enemies, battle and death are words over landscapes, empty places and smoke; 137:9 words over the rock.

Plan (42,342 words, fifteen chapters, by the five books of the Psalter): Book I — 1 Blessed Is the Man (1–12) · 2 The
Heavens Declare (13–22) · 3 Jehovah Is My Shepherd (23–33) · 4 Wait for Jehovah (34–41); Book II — 5 As the Hart Panteth
(42–50) · 6 A Clean Heart (51–62) · 7 Let God Arise (63–72); Book III — 8 Whom Have I in Heaven (73–78) · 9 How Amiable
Are Thy Tabernacles (79–89); Book IV — 10 Our Dwelling-place (90–100) · 11 Bless Jehovah, O My Soul (101–106); Book V —
12 They That Go Down to the Sea (107–118) · 13 Thy Word Is a Lamp (119) · 14 Songs of Ascents (120–137) · 15 Praise Ye
Jehovah (138–150)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("PSA")

META = {
  "id": "psalms", "order": 19, "name": "Psalms", "kanji": "詩篇", "thumb": "vol-psalms-", "book": "PSA",
  "title": "Psalms Volume", "volume": "Volume Nineteen",
  "lede": "The nineteenth book of the Bible, in full: the hundred and fifty psalms in their five books — the blessed man and the tree by the streams, the heavens declaring the glory of God, Jehovah my shepherd, the hart panting after the water brooks, the harps hung on the willows, the songs of ascents and the last great hallelujahs — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Blessed Is the Man", "range": "Psalms 1–12", "bible_chapters": list(range(1, 13)),
     "blurb": "Book I opens: the blessed man like a tree planted by the streams of water, and the wicked like the chaff; why do the nations rage — thou art my son; I laid me down and slept; in the morning will I order my prayer; every night make I my bed to swim; when I consider thy heavens, what is man?; the lurking lion and the net; and the words of Jehovah, pure words, as silver tried in a furnace."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Heavens Declare", "range": "Psalms 13–22", "bible_chapters": list(range(13, 23)),
     "blurb": "How long, O Jehovah?; the fool hath said in his heart, There is no God; who shall sojourn in thy tabernacle?; the lines are fallen unto me in pleasant places; hide me under the shadow of thy wings; Jehovah is my rock and my fortress — the cords of death, the earth that shook, the large place; the heavens declare the glory of God; some trust in chariots; and my God, my God, why hast thou forsaken me?"},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Jehovah Is My Shepherd", "range": "Psalms 23–33", "bible_chapters": list(range(23, 34)),
     "blurb": "Jehovah is my shepherd; I shall not want — green pastures, still waters, the valley of the shadow of death, a table before me; lift up your heads, O ye gates; Jehovah is my light and my salvation; the voice of Jehovah breaketh the cedars; weeping may tarry for the night, but joy cometh in the morning; into thy hand I commend my spirit; blessed is he whose transgression is forgiven; and sing unto him a new song."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Wait for Jehovah", "range": "Psalms 34–41", "bible_chapters": list(range(34, 42)),
     "blurb": "The close of Book I: O taste and see that Jehovah is good; the angel of Jehovah encampeth round about them that fear him; with thee is the fountain of life — in thy light shall we see light; fret not thyself because of evil-doers; I have been young, and now am old; every man walketh in a vain show; I waited patiently for Jehovah, and he brought me up out of a horrible pit; and blessed be Jehovah, the God of Israel, from everlasting and to everlasting."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "As the Hart Panteth", "range": "Psalms 42–50", "bible_chapters": list(range(42, 51)),
     "blurb": "Book II opens with the sons of Korah: as the hart panteth after the water brooks; deep calleth unto deep; oh send out thy light and thy truth; the king's wedding song and the queen in gold of Ophir; God is our refuge and strength — there is a river, the streams whereof make glad the city of God; be still, and know that I am God; walk about Zion; man that is in honor abideth not; and Asaph: every beast of the forest is mine, and the cattle upon a thousand hills."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "A Clean Heart", "range": "Psalms 51–62", "bible_chapters": list(range(51, 63)),
     "blurb": "Have mercy upon me, O God — purify me with hyssop, and I shall be clean; create in me a clean heart; I am like a green olive-tree in the house of God; oh that I had wings like a dove!; put thou my tears into thy bottle; in the cave — be thou exalted, O God, above the heavens; they go round about the city like dogs; Moab is my washpot; lead me to the rock that is higher than I; and my soul waiteth in silence for God only."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Let God Arise", "range": "Psalms 63–68", "bible_chapters": list(range(63, 69)),
     "blurb": "My soul thirsteth for thee in a dry and weary land; thy lovingkindness is better than life; thou visitest the earth, and waterest it — the pastures are clothed with flocks; he turned the sea into dry land; God be merciful unto us, and bless us; and let God arise, let his enemies be scattered — the chariots of God, the singers before, the damsels playing with timbrels."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "He Shall Have Dominion", "range": "Psalms 69–72", "bible_chapters": list(range(69, 73)),
     "blurb": "The close of Book II: save me, O God, for the waters are come in unto my soul; make haste to help me; now also when I am old and grayheaded, forsake me not; and Solomon's psalm — he shall come down like rain upon the mown grass, he shall have dominion from sea to sea, the kings of Sheba and Seba shall offer gifts. The prayers of David the son of Jesse are ended."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "Whom Have I in Heaven", "range": "Psalms 73–78", "bible_chapters": list(range(73, 79)),
     "blurb": "Book III opens with Asaph: until I went into the sanctuary of God — whom have I in heaven but thee?; they have set thy sanctuary on fire; in the hand of Jehovah there is a cup; in Salem is his tabernacle; the waters saw thee, O God; and the dark sayings of old — the sea divided, the rock cleft in the wilderness, bread from heaven, the wonders in the field of Zoan, and David taken from the sheepfolds."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "How Amiable Are Thy Tabernacles", "range": "Psalms 79–89", "bible_chapters": list(range(79, 90)),
     "blurb": "The close of Book III: they have laid Jerusalem in heaps; give ear, O Shepherd of Israel — thou broughtest a vine out of Egypt; blow the trumpet at the new moon; God standeth in the congregation of God; they are confederate against thee; how amiable are thy tabernacles — the sparrow hath found her a house; mercy and truth are met together; glorious things are spoken of thee, O city of God; Heman's cry from the lowest pit; and I will sing of the lovingkindness of Jehovah for ever."},
  ],
}
