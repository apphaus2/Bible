"""The Isaiah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Isaiah is prophecy, laid out like Moses' discourses in Deuteronomy: isa.common.S() cuts a run of verses into speech panels,
alternating the prophet's face (kg2.common.ISAIAH and its moods in isa.common) with drawings of the images (isa.art).
Jehovah's own words are in the Voice box, the prophet's in speech boxes, the psalms and songs in song lines, narration in
captions; a "Thus saith Jehovah" formula opening a verse is set apart as a caption. The burdens of the nations (13–23)
open on a technical map with the nation lit (isa.art.nations_map); the story of Hezekiah and Sennacherib (36–39) reuses
2 Kings' drawings and faces (kg2.art, kg2.common). Restraint: God is never drawn — the vision of 6 is light, smoke, an
empty throne and the seraphim's wings; judgments and battles are words over landscapes, smoke, ruins and empty cities;
the servant of 52:13–53:12 is never drawn (a lamb, a root out of dry ground, an empty grave in the rock); 63:1–6 is
the winepress alone; 66:24 is words over the valley outside the city.

Plan (36,642 words, eighteen chapters): 1 The Vineyard of Jehovah (1–5) · 2 Holy, Holy, Holy (6–9) · 3 The Root of
Jesse (10–12) · 4 How Art Thou Fallen (13–16) · 5 The Burden of Egypt (17–20) · 6 Watchman, What of the Night? (21–23) ·
7 Thy Dead Shall Live (24–27) · 8 In Returning and Rest (28–30) · 9 The Desert Shall Blossom (31–35) ·
10 On Whom Dost Thou Trust? (36–39) · 11 Comfort Ye My People (40–42) · 12 Ye Are My Witnesses (43–45) · 13 Go Ye Forth
from Babylon (46–48) · 14 A Light to the Gentiles (49–51) · 15 A Man of Sorrows (52–55) · 16 The Fast That I Have Chosen
(56–59) · 17 Arise, Shine (60–62) · 18 New Heavens and a New Earth (63–66)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ISA")

META = {
  "id": "isaiah", "order": 23, "name": "Isaiah", "kanji": "イザヤ書", "thumb": "vol-isaiah-", "book": "ISA",
  "title": "Isaiah Volume", "volume": "Volume Twenty-Three",
  "lede": "The twenty-third book of the Bible, in full: the vision of Isaiah the son of Amoz — the vineyard of Jehovah, the seraphim crying holy, holy, holy, the burdens of the nations, Hezekiah and the host of Sennacherib, comfort ye my people, the servant of Jehovah, and new heavens and a new earth, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Vineyard of Jehovah", "range": "Isaiah 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "Hear, O heavens, and give ear, O earth: the ox knoweth his owner, but Israel doth not know; come now, and let us reason together — though your sins be as scarlet, they shall be as white as snow; the mountain of Jehovah's house, and swords beaten into plowshares; the day of Jehovah upon all that is lifted up; the daughters of Zion; and the song of the vineyard that brought forth wild grapes."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Holy, Holy, Holy", "range": "Isaiah 6–9", "bible_chapters": [6, 7, 8, 9],
     "blurb": "In the year that king Uzziah died: the Lord upon a throne, high and lifted up, and the seraphim crying holy, holy, holy; woe is me; the live coal; here am I, send me; then Ahaz at the conduit of the upper pool — ask thee a sign; behold, a virgin shall conceive, and shall call his name Immanuel; the River to the neck; the people that walked in darkness have seen a great light; unto us a child is born."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Root of Jesse", "range": "Isaiah 10–12", "bible_chapters": [10, 11, 12],
     "blurb": "Ho Assyrian, the rod of mine anger — shall the axe boast itself against him that heweth therewith?; a remnant shall return; he is come to Aiath, he halteth at Nob; then a shoot out of the stock of Jesse: the wolf shall dwell with the lamb, and a little child shall lead them; an ensign for the nations; and the song of that day — with joy shall ye draw water out of the wells of salvation."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "How Art Thou Fallen", "range": "Isaiah 13–16", "bible_chapters": [13, 14, 15, 16],
     "blurb": "The burden of Babylon: the day of Jehovah, the sun darkened, the Medes stirred up, and Babylon, the glory of kingdoms, never inhabited; the parable against the king of Babylon — how art thou fallen from heaven, O day-star, son of the morning!; the burden of Philistia and the fiery flying serpent; and the burden of Moab — my heart soundeth like a harp for Moab."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Burden of Egypt", "range": "Isaiah 17–20", "bible_chapters": [17, 18, 19, 20],
     "blurb": "The burden of Damascus, a ruinous heap, and the gleanings of the olive-tree; the uproar of the nations chased as chaff; the land of the rustling of wings beyond the rivers of Ethiopia; the burden of Egypt — Jehovah rideth upon a swift cloud, the Nile dried up, an altar to Jehovah in the midst of Egypt, and a highway out of Egypt to Assyria; and Isaiah's sign, three years barefoot, against Egypt and Ethiopia."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Watchman, What of the Night?", "range": "Isaiah 21–23", "bible_chapters": [21, 22, 23],
     "blurb": "The burden of the wilderness of the sea — set a watchman: fallen, fallen is Babylon; the burden of Dumah — watchman, what of the night? the morning cometh, and also the night; the burden upon Arabia; the valley of vision — let us eat and drink, for to-morrow we shall die; Shebna's sepulchre, and the key of the house of David laid upon Eliakim; and the burden of Tyre — howl, ye ships of Tarshish."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Thy Dead Shall Live", "range": "Isaiah 24–27", "bible_chapters": [24, 25, 26, 27],
     "blurb": "Jehovah maketh the earth empty, and it reeleth to and fro like a hammock; then the song — O Jehovah, thou art my God; in this mountain a feast of fat things for all peoples: he hath swallowed up death for ever, and the Lord Jehovah will wipe away tears from off all faces; we have a strong city; thy dead shall live; leviathan the swift serpent; the vineyard of wine; and the great trumpet."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "In Returning and Rest", "range": "Isaiah 28–30", "bible_chapters": [28, 29, 30],
     "blurb": "Woe to the crown of pride of the drunkards of Ephraim; precept upon precept, line upon line; a covenant with death, and a tried stone laid in Zion, a precious corner-stone of sure foundation; Ho Ariel; a book that is sealed; shall the potter be esteemed as clay?; woe to the rebellious children that go down into Egypt; in returning and rest shall ye be saved; and a word behind thee — this is the way, walk ye in it."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "The Desert Shall Blossom", "range": "Isaiah 31–35", "bible_chapters": [31, 32, 33, 34, 35],
     "blurb": "Woe to them that go down to Egypt for help; a king shall reign in righteousness, as the shade of a great rock in a weary land; until the Spirit be poured upon us from on high; who among us can dwell with the devouring fire?; thine eyes shall see the king in his beauty, and Zion a tent that shall not be removed; the heavens rolled together as a scroll and the burden upon Edom; and the desert shall rejoice, and blossom as the rose, and the ransomed of Jehovah shall return with singing."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "On Whom Dost Thou Trust?", "range": "Isaiah 36–39", "bible_chapters": [36, 37, 38, 39],
     "blurb": "Sennacherib against the fortified cities of Judah, and Rabshakeh at the conduit of the upper pool — now on whom dost thou trust?; Hezekiah in sackcloth, the letter spread before Jehovah, and his prayer; the virgin daughter of Zion hath despised thee; the camp of the Assyrians at morning; Hezekiah sick unto death and the shadow returned ten steps on the dial; the writing of Hezekiah; and the envoys of Babylon."},
    {"module": "ch11", "dir": "chapter-11", "num": "11", "name": "Comfort Ye My People", "range": "Isaiah 40–42", "bible_chapters": [40, 41, 42],
     "blurb": "Comfort ye, comfort ye my people: the voice of one that crieth, prepare ye in the wilderness the way of Jehovah; all flesh is grass, but the word of our God shall stand forever; he will feed his flock like a shepherd; who hath measured the waters in the hollow of his hand?; they that wait for Jehovah shall mount up with wings as eagles; fear thou not, for I am with thee; behold my servant — a bruised reed will he not break; sing unto Jehovah a new song."},
    {"module": "ch12", "dir": "chapter-12", "num": "12", "name": "Ye Are My Witnesses", "range": "Isaiah 43–45", "bible_chapters": [43, 44, 45],
     "blurb": "Fear not, for I have redeemed thee: when thou passest through the waters, I will be with thee; ye are my witnesses, saith Jehovah; a way in the sea, and rivers in the desert; I am the first, and I am the last; the smith, the carpenter, and the tree half burned and half a god; I have blotted out, as a thick cloud, thy transgressions; Cyrus, my shepherd, mine anointed; I form the light, and create darkness; look unto me, and be ye saved, all the ends of the earth."},
    {"module": "ch13", "dir": "chapter-13", "num": "13", "name": "Go Ye Forth from Babylon", "range": "Isaiah 46–48", "bible_chapters": [46, 47, 48],
     "blurb": "Bel boweth down, Nebo stoopeth, their idols a burden to the weary beast; even to hoar hairs will I carry you; a ravenous bird from the east; come down, and sit in the dust, O virgin daughter of Babylon; let now the star-gazers save thee; I have chosen thee in the furnace of affliction; oh that thou hadst hearkened — then had thy peace been as a river; go ye forth from Babylon; there is no peace, saith Jehovah, to the wicked."},
    {"module": "ch14", "dir": "chapter-14", "num": "14", "name": "A Light to the Gentiles", "range": "Isaiah 49–51", "bible_chapters": [49, 50, 51],
     "blurb": "Listen, O isles: the servant hid as a polished shaft in the quiver — I will also give thee for a light to the Gentiles; to them that are bound, Go forth; can a woman forget her sucking child? yet will not I forget thee; thy walls are continually before me; he wakeneth mine ear morning by morning; I set my face like a flint; look unto the rock whence ye were hewn; awake, awake, put on strength, O arm of Jehovah; and the cup of staggering taken out of thy hand."},
    {"module": "ch15", "dir": "chapter-15", "num": "15", "name": "A Man of Sorrows", "range": "Isaiah 52–55", "bible_chapters": [52, 53, 54, 55],
     "blurb": "Awake, awake, put on thy strength, O Zion; how beautiful upon the mountains are the feet of him that bringeth good tidings; behold, my servant shall deal wisely — he was despised, and rejected of men, a man of sorrows; he was wounded for our transgressions; all we like sheep have gone astray; as a lamb that is led to the slaughter; sing, O barren, enlarge the place of thy tent; ho, every one that thirsteth, come ye to the waters; and the trees of the field shall clap their hands."},
    {"module": "ch16", "dir": "chapter-16", "num": "16", "name": "The Fast That I Have Chosen", "range": "Isaiah 56–59", "bible_chapters": [56, 57, 58, 59],
     "blurb": "Mine house shall be called a house of prayer for all peoples; his watchmen are blind, dumb dogs that cannot bark; I dwell in the high and holy place, with him also that is of a contrite and humble spirit; cry aloud, lift up thy voice like a trumpet; is not this the fast that I have chosen? to deal thy bread to the hungry — then shall thy light break forth as the morning; the repairer of the breach; and a Redeemer will come to Zion."},
    {"module": "ch17", "dir": "chapter-17", "num": "17", "name": "Arise, Shine", "range": "Isaiah 60–62", "bible_chapters": [60, 61, 62],
     "blurb": "Arise, shine; for thy light is come, and the glory of Jehovah is risen upon thee; nations shall come to thy light — the camels of Midian, the ships of Tarshish flying as doves to their windows; thy gates open continually; Jehovah thine everlasting light; the Spirit of the Lord Jehovah is upon me, to preach good tidings unto the meek, a garland for ashes; as a bride adorneth herself with her jewels; for Zion's sake will I not hold my peace; and cast up, cast up the highway."},
  ],
}
