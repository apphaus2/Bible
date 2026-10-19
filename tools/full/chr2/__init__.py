"""The 2 Chronicles volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The package is chr2 (a module name cannot start with a digit). Solomon's reign (1–9) reuses 1 Kings' blueprints and figures;
the kings of Judah (10–36) reuse 1 and 2 Kings' faces and drawings (chr2.common takes the cast from kg2.common; chr2.art
carries chr1.art, kg2.art and kg1.art). Lists are roll cells (chr2.common.cell/cells/roll; reigns as reign()). Restraint:
the slain of battle words over the plain and the smoke; Jehoram's sickness (21:18–19) words only; Zechariah stoned in the
court (24:21) words over the court; Amaziah's ten thousand (25:12) words over the rock; Uzziah's leprosy his face in pale
light; Manasseh's sons in the fire (33:6) words only; Josiah's wound at Megiddo (35:23–24) words over the chariot; the fall
of Jerusalem (36:17–19) words over the burning city; God is never drawn.

Plan (25,806 words, fourteen chapters): 1 Wisdom and Knowledge (1–4) · 2 The Glory Filled the House (5–7) · 3 The Queen of
Sheba (8–9) · 4 Rehoboam (10–12) · 5 Abijah and Asa (13–16) · 6 Jehoshaphat (17–19) · 7 The Battle Is Not Yours (20–21) ·
8 Joash (22–24) · 9 Amaziah and Uzziah (25–27) · 10 Ahaz and Hezekiah (28–29) · 11 The Passover of Hezekiah (30–31) ·
12 Sennacherib (32) · 13 Manasseh and Josiah (33–34) · 14 The Seventy Years (35–36)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2CH")

META = {
  "id": "2chronicles", "order": 14, "name": "2 Chronicles", "kanji": "歴代志下", "thumb": "vol-2chronicles-", "book": "2CH",
  "title": "2 Chronicles Volume", "volume": "Volume Fourteen",
  "lede": "The fourteenth book of the Bible, in full: Solomon's wisdom and the house of Jehovah filled with glory, the kings of Judah who sought Jehovah and those who forsook him, Hezekiah's passover and Josiah's book, and the seventy years of the land's sabbath, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Wisdom and Knowledge", "range": "2 Chronicles 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "Solomon at the high place at Gibeon, and in that night, ask what I shall give thee — give me now wisdom and knowledge; chariots and horsemen, and silver and gold as stones; Huram king of Tyre and the cedars of Lebanon; then the house of Jehovah on mount Moriah: the most holy house and its cherubim, Jachin and Boaz, the molten sea upon twelve oxen, and the vessels of gold."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Glory Filled the House", "range": "2 Chronicles 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "The ark brought into the oracle under the wings of the cherubim; the trumpeters and singers as one — for he is good, for his lovingkindness endureth for ever — and the house filled with a cloud; Solomon's prayer from the brazen scaffold; the fire came down from heaven; and Jehovah's answer by night: if my people, who are called by my name, shall humble themselves, and pray."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Queen of Sheba", "range": "2 Chronicles 8–9", "bible_chapters": [8, 9],
     "blurb": "Tadmor in the wilderness and the store-cities; Pharaoh's daughter brought up to her own house, for the places are holy whereunto the ark hath come; the ships of Ophir; then the queen of Sheba with hard questions — the half of the greatness of thy wisdom was not told me; the throne of ivory and its twelve lions; and Solomon slept with his fathers."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Rehoboam", "range": "2 Chronicles 10–12", "bible_chapters": [10, 11, 12],
     "blurb": "Rehoboam at Shechem: the counsel of the old men and of the young — my little finger is thicker than my father's loins; whips and scorpions; every man to your tents, O Israel; ye shall not fight against your brethren; the cities for defence and the Levites who came to Judah; Shishak king of Egypt — Jehovah is righteous; and shields of brass for the shields of gold."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "Abijah and Asa", "range": "2 Chronicles 13–16", "bible_chapters": [13, 14, 15, 16],
     "blurb": "Abijah upon mount Zemaraim — God is with us at our head — and the shout of Judah; Asa who sought Jehovah, and Zerah the Ethiopian with a thousand thousand: help us, O Jehovah our God, for we rely on thee; Azariah's word and the covenant sworn with trumpets; then Ramah, the silver sent to Ben-hadad, and Hanani the seer: the eyes of Jehovah run to and fro throughout the whole earth."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Jehoshaphat", "range": "2 Chronicles 17–19", "bible_chapters": [17, 18, 19],
     "blurb": "Jehoshaphat who walked in the first ways of David, and the princes and Levites teaching in the cities with the book of the law; then affinity with Ahab — I am as thou art; the four hundred prophets and Micaiah: as Jehovah liveth, what my God saith, that will I speak; the arrow at a venture; Jehu the seer; and the judges set city by city — ye judge not for man, but for Jehovah."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The Battle Is Not Yours", "range": "2 Chronicles 20–21", "bible_chapters": [20, 21],
     "blurb": "A great multitude from beyond the sea; Jehoshaphat's prayer — neither know we what to do, but our eyes are upon thee; Jahaziel: the battle is not yours, but God's — stand ye still, and see the salvation of Jehovah; the singers going out before the army, and the valley of Beracah; then Jehoram, Edom's revolt, and a writing from Elijah the prophet."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Joash", "range": "2 Chronicles 22–24", "bible_chapters": [22, 23, 24],
     "blurb": "Ahaziah and the house of Ahab; Athaliah destroys the seed royal, and Jehoshabeath hides the child Joash six years in the house of God; Jehoiada's covenant — long live the king; treason! treason!; the chest at the gate and the house restored; then, Jehoiada dead, Zechariah his son stoned in the court — Jehovah look upon it, and require it."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "Amaziah and Uzziah", "range": "2 Chronicles 25–27", "bible_chapters": [25, 26, 27],
     "blurb": "Amaziah, right but not with a perfect heart: the hundred talents — Jehovah is able to give thee much more than this; the gods of Seir; the thistle and the cedar; then Uzziah who sought God and loved husbandry, his towers and engines; his heart lifted up, the censer in the temple, and the leprosy in his forehead; and Jotham, who ordered his ways before Jehovah."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "Ahaz and Hezekiah", "range": "2 Chronicles 28–29", "bible_chapters": [28, 29],
     "blurb": "Ahaz who walked in the ways of the kings of Israel; Judah carried captive to Samaria, and Oded the prophet — send back the captives; the captives clothed and brought to Jericho, the city of palm-trees; the gods of Damascus and the doors shut; then Hezekiah opening the doors in the first month, the house cleansed, and the song of Jehovah with the trumpets."},
    {"module": "ch11", "dir": "chapter-11", "num": "11", "name": "The Passover of Hezekiah", "range": "2 Chronicles 30–31", "bible_chapters": [30, 31],
     "blurb": "Letters from Beer-sheba even to Dan — ye children of Israel, turn again unto Jehovah; laughed to scorn, yet some humbled themselves and came; the passover in the second month — the good Jehovah pardon every one that setteth his heart to seek God; great joy in Jerusalem, not the like since Solomon; and the heaps of the first-fruits and the tithes."},
    {"module": "ch12", "dir": "chapter-12", "num": "12", "name": "Sennacherib", "range": "2 Chronicles 32", "bible_chapters": [32],
     "blurb": "Sennacherib come into Judah; the fountains stopped and the wall built up — with him is an arm of flesh, but with us is Jehovah our God; whereon do ye trust?; the letters railing on Jehovah; Hezekiah and Isaiah cry to heaven, and the camp of Assyria cut off; Hezekiah sick and humbled; the upper spring of Gihon; and the ambassadors of Babylon."},
    {"module": "ch13", "dir": "chapter-13", "num": "13", "name": "Manasseh and Josiah", "range": "2 Chronicles 33–34", "bible_chapters": [33, 34],
     "blurb": "Manasseh's altars in the two courts and the graven image in the house of God; taken in chains to Babylon, he humbled himself greatly — then Manasseh knew that Jehovah he was God; Amon; then Josiah, who while yet young began to seek the God of David: I have found the book of the law; Huldah — because thy heart was tender; and the covenant read in the ears of all the people."},
    {"module": "ch14", "dir": "chapter-14", "num": "14", "name": "The Seventy Years", "range": "2 Chronicles 35–36", "bible_chapters": [35, 36],
     "blurb": "Josiah's passover, no passover like it since Samuel the prophet; Neco at Carchemish and the archers at Megiddo, and Jeremiah's lament; the last kings of Judah; the messengers mocked till there was no remedy; the house of God burned; the land keeping sabbath seventy years; and the proclamation of Cyrus king of Persia — let him go up."},
  ],
}
