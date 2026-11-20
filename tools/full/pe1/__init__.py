"""The 1 Peter volume of the full edition (the First Epistle General of Peter): metadata, the volume cover, and the chapter
plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit), as Paul's letters are, but the writer is Peter, "an
apostle of Jesus Christ" (1:1), now old, writing "by Silvanus" (5:12) from "Babylon" — Rome — with "Mark my son" (5:13).
Paul is never drawn in this volume. Peter's faces and the looks of Silvanus and Mark are kept in jas/common.py with the other
writers of the general letters.

A letter has no narration: every word of the ASV here is Peter writing to the elect sojourners of the Dispersion (letter
boxes, tailed toward Peter's face). The scriptures he quotes are song boxes (1:24–25 "All flesh is as grass", 2:7 "The
stone which the builders rejected", 2:8 "A stone of stumbling", 3:10–12 "He that would love life", 5:5 "God resisteth the
proud"); God's own words in the first person are the Voice box (1:16 "Ye shall be holy; for I am holy", 2:6 "Behold, I lay
in Zion a chief corner stone").

Peter's face is ntcast's PETER grown old — the same face and skin, bareheaded, his hair and beard grey — in the kit's five
lights (jas.common: PETER_OLD gold, PETER_LAMP, PETER_GRIEF, PETER_JOY white, PETER_STERN red): white with joy at the living
hope (1:3–5), 1:20–23, 3:18–19 and 4:10–11; stern at 1:13–15 and 4:4–6, 4:15–16, 5:8–9; grieving at 2:18–20 (servants
suffering wrongfully); gold elsewhere. At a distance he is jas.art.peter_fig (ntcast's brown robe, grey hair and beard).
Silvanus is Acts' Silas (a blue headcloth and robe, a black beard), writing on his mat; Mark is Acts' John Mark (an olive-khaki
robe, bareheaded, dark-brown hair), now with a short beard.

Drawings (pe1.art): Peter at Babylon (Rome) by lamplight, Silvanus writing and Mark standing by, Rome's temple through the
window (the title page, and 5:12–13 with the sealed letter given); the letter's road from Rome to Pontus, Galatia,
Cappadocia, Asia and Bithynia on Acts' map; the goldsmith's crucible over the fire, the gold proved and poured; the prophets
searching the scroll by lamplight, figures of light (angels, faceless) bending to look into it; a lamb without blemish as an
emblem on a plate, silver and gold set aside (no slaughter); the grass withering and the word of the Lord abiding, an open
scroll in the light; a mother with her newborn babe; living stones built up a spiritual house; the chief corner stone, the
stone the builders rejected and the stone of stumbling as a masonry plate; a royal priesthood called out of darkness into
light; sojourners and pilgrims on the road; honor all men, love the brotherhood, fear God, honor the king, as a plate of four;
three crosses far off under a darkened sky (2:24, as Galatians draws it); the Shepherd and Bishop of souls — Jesus as
ntcast draws him, the straying sheep returning to him; a wife's quiet household; Sarah at the tent door, Abraham coming home
(Genesis' looks); a husband and wife at prayer; a believer giving answer for the hope that is in him; the ark riding the
water, eight souls; the dark street of the Gentiles' revellings (Galatians' empty street); brethren at one table, using
hospitality; the furnace of the fiery trial; the faithful Creator, dawn over land and sea; an elder tending the flock; the
crown of glory that fadeth not away; the doxology over the light; the brethren greeting one another.

Restraint: 2:24 the cross only as three crosses far off against a darkened sky, no figure on them, "by whose stripes ye were
healed" words only; 3:18 "put to death in the flesh" words beside Peter's face; 3:19–20 the spirits in prison words only, the
drawing is the ark on the waters; 4:3 lasciviousness, revellings, carousings, idolatries are words over a dark, empty street;
4:15 murderer and thief words only; 5:8 "your adversary the devil, as a roaring lion" words only beside Peter's stern face —
neither the devil nor a lion is drawn; 3:3 the braiding of hair and the jewels of gold are words, the wife drawn plainly
veiled. God is never drawn (light; the Voice box); angels (1:12, 3:22) are figures of white light with no face, or words.

Plan (2,426 words, one chapter): 1 Living Stones (1–5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1PE")

META = {
  "id": "1peter", "order": 60, "name": "1 Peter", "kanji": "ペテロの第一の手紙", "thumb": "vol-1peter-", "book": "1PE",
  "title": "1 Peter Volume", "volume": "Volume Sixty",
  "lede": "The sixtieth book of the Bible, in full: Peter's first letter, to the elect sojourners of the Dispersion in Pontus, Galatia, Cappadocia, Asia and Bithynia — a living hope, faith more precious than gold proved by fire, ye shall be holy, the precious blood as of a lamb without blemish, all flesh is as grass, living stones and the chief corner stone, a royal priesthood, sojourners and pilgrims, honor the king, who his own self bare our sins upon the tree, the Shepherd and Bishop of your souls, eight souls saved through water, the fiery trial, tend the flock of God, your adversary as a roaring lion, by Silvanus from Babylon with Mark my son, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Living Stones", "range": "1 Peter 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "Peter, an apostle of Jesus Christ, to the elect sojourners of the Dispersion: begotten again unto a living hope; the proof of your faith more precious than gold proved by fire; the prophets searched, and angels desire to look into it; ye shall be holy, for I am holy; redeemed with precious blood, as of a lamb without blemish; all flesh is as grass, but the word of the Lord abideth; living stones, the chief corner stone; a royal priesthood, out of darkness into his marvellous light; honor the king; Christ bare our sins upon the tree, the Shepherd and Bishop of your souls; wives and husbands; eight souls saved through water; the fiery trial; tend the flock of God, the crown of glory; casting all your anxiety upon him; by Silvanus, from Babylon, and Mark my son."},
  ],
}
