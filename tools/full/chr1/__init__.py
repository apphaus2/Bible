"""The 1 Chronicles volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The package is chr1 (a module name cannot start with a digit). The genealogies of 1–9 are roll pages (rolls.roll_pages,
rolls.verse_cells: every verse in full), each run opened by a lineage chart (chr1.art.lineage) under the first verses.
The story of David (10–29) runs alongside 2 Samuel, so it reuses 2 Samuel's faces and drawings (chr1.common takes the cast
from sa2.common and kg2.common; chr1.art re-exports kg2.art, which carries kg1.art, plus sa2.art as K2). The courses of
the priests, singers and porters (23–27) are roll cells. Restraint: Saul's death (10:4–6, 10:9–10) words over the crown and
spear on Gilboa; Uzza (13:10) words over the cart at the threshing-floor; 20:3 words only; the pestilence (21:14) words over
the silent tents; God is never drawn.

Plan (20,145 words, eleven chapters): 1 From Adam (1–2) · 2 The Sons of David (3–4) · 3 The Sons of Levi (5–6) · 4 They
That Dwelt in Jerusalem (7–9) · 5 David King over Israel (10–12) · 6 The Ark of God (13–16) · 7 Thy Throne for Ever
(17–20) · 8 The Threshing-floor of Ornan (21–22) · 9 The Courses (23–25) · 10 The Porters and the Captains (26–27) ·
11 Thine Is the Kingdom (28–29)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1CH")

META = {
  "id": "1chronicles", "order": 13, "name": "1 Chronicles", "kanji": "歴代志上", "thumb": "vol-1chronicles-", "book": "1CH",
  "title": "1 Chronicles Volume", "volume": "Volume Thirteen",
  "lede": "The thirteenth book of the Bible, in full: the generations from Adam, David king over all Israel, the ark brought up with singing, the covenant of an everlasting throne, and the house of Jehovah made ready for Solomon, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "From Adam", "range": "1 Chronicles 1–2", "bible_chapters": [1, 2],
     "blurb": "Adam, Seth, Enosh — the generations from the first man to Noah and his three sons; the nations of Japheth, Ham and Shem; Abraham, Isaac and Ishmael; Esau and the kings that reigned in Edom before any king reigned over Israel; the sons of Israel; and the house of Judah down to Jesse and David, the seventh son."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Sons of David", "range": "1 Chronicles 3–4", "bible_chapters": [3, 4],
     "blurb": "The sons born to David in Hebron and in Jerusalem; the kings of Judah from Solomon to Josiah, son after son; Jeconiah the captive and Zerubbabel; the families of Judah, and Jabez, more honorable than his brethren — oh that thou wouldest bless me indeed, and enlarge my border; the potters who dwelt with the king; and Simeon at the fat pasture of Gedor."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Sons of Levi", "range": "1 Chronicles 5–6", "bible_chapters": [5, 6],
     "blurb": "Reuben, whose birthright was given to the sons of Joseph; Gad in Bashan; the war with the Hagrites, for they cried to God in the battle; the two tribes and a half carried away beyond the river; then the sons of Levi: the high priests from Aaron to Jehozadak, the singers David set over the service of song, and the cities of the Levites."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "They That Dwelt in Jerusalem", "range": "1 Chronicles 7–9", "bible_chapters": [7, 8, 9],
     "blurb": "Issachar, Benjamin, Naphtali and Manasseh; Ephraim mourning many days, and Sheerah who built Beth-horon; the line from Ephraim to Joshua; Asher; Benjamin and the house of Saul; then all Israel reckoned by genealogies, and those who dwelt in Jerusalem: priests, Levites, and the porters on the four sides of the house, opening it morning by morning."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "David King over Israel", "range": "1 Chronicles 10–12", "bible_chapters": [10, 11, 12],
     "blurb": "Saul and his sons fallen on mount Gilboa, and the valiant men of Jabesh who buried their bones under the oak; then all Israel at Hebron — behold, we are thy bone and thy flesh; the stronghold of Zion; the mighty men, and the water of the well of Beth-lehem poured out unto Jehovah; thine are we, David; and three days of feasting, for there was joy in Israel."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Ark of God", "range": "1 Chronicles 13–16", "bible_chapters": [13, 14, 15, 16],
     "blurb": "Let us bring again the ark of our God: the new cart, Uzza at the threshing-floor of Chidon, and three months in the house of Obed-edom; Hiram's cedars and the sound of marching in the tops of the mulberry-trees; then the Levites bear the ark on their shoulders, the singers sound aloud, David dances, and Asaph sings — O give thanks unto Jehovah, for his lovingkindness endureth for ever."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Thy Throne for Ever", "range": "1 Chronicles 17–20", "bible_chapters": [17, 18, 19, 20],
     "blurb": "Lo, I dwell in a house of cedar, but the ark dwelleth under curtains; the word of God to Nathan by night — I will build thee a house, and I will establish his throne for ever; who am I, O Jehovah God?; David's wars and the shields of gold; Hanun and the messengers shamed; Joab before and behind; Rabbah and the crown of gold; and the sons of the giant in Gath."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "The Threshing-floor of Ornan", "range": "1 Chronicles 21–22", "bible_chapters": [21, 22],
     "blurb": "Satan moves David to number Israel; Joab's protest; I have done very foolishly; Gad and the three things; the pestilence, and it is enough, now stay thy hand; the angel's sword over Jerusalem; Ornan's threshing-floor bought for the full price, and the answer by fire from heaven; then the stores of gold and cedar, and David's charge to Solomon: arise and be doing."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "The Courses", "range": "1 Chronicles 23–25", "bible_chapters": [23, 24, 25],
     "blurb": "David old and full of days makes Solomon king; the Levites numbered and divided into courses, to stand every morning to thank and praise Jehovah, and likewise at even; the sons of Aaron divided by lot into four and twenty courses; and the sons of Asaph, Heman and Jeduthun set apart to prophesy with harps, lot by lot, twelve to each."},
  ],
}
