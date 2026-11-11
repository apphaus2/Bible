"""The Galatians volume of the full edition (the Epistle of Paul to the Galatians): metadata, the volume cover, and the
chapter plans (ch01.py, ch02.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit; the letter box, the study, the sealed scroll, the
doxology panel), as Romans is. A letter has no narration: every word of the ASV here is Paul writing to the churches of
Galatia (letter boxes: parchment, a sepia rule down the left edge, a short tail toward Paul where his face is drawn); the
scriptures he quotes are song boxes (3:6, 3:10–13, 4:27, 4:30, 5:14); God's own promise to Abraham in the first person (3:8,
"In thee shall all the nations be blessed") is the Voice box. His words to Cephas at Antioch (2:14–21) stay letter boxes,
since it is the letter that tells them, over the scene of Paul withstanding Peter before them all.

Galatians is the sternest letter: Paul's face is PAUL_STERN (red light) at 1:6–7, 2:3–5, 3:1–3, 5:2–6, 5:10–12 and 6:12–13,
earnest gold elsewhere, grieving blue at 4:12–20 (his infirmity among them and "my little children"), white with joy at
2:20–21, 4:6–7 and 5:24–26.

Drawings (gal.art, on Acts' drawings and the epistle kit): Paul and the brethren with him in the study, the letter's road
to the churches of Galatia (Antioch of Pisidia, Iconium, Lystra, Derbe) on Acts' map; an angel from heaven as a figure of
white light with a gold rim and no face, beside the true gospel's sealed roll (1:8); Saul laying waste the church and the
light on the Damascus road (Acts' drawings; Jesus is not drawn there); Arabia's desert and Damascus far off; fifteen days
with Cephas at Jerusalem, James the Lord's brother at the door; Syria and Cilicia on the map; Paul, Barnabas and Titus going
up to Jerusalem; the two apostleships as a plate (Peter to the circumcision, Paul to the Gentiles); the right hands of
fellowship given by James, Cephas and John to Paul and Barnabas between the pillars; Cephas drawing back from the Gentiles'
table at Antioch, and Paul withstanding him to the face; Galatians hearing Paul at Iconium (3:2–5); Abraham's tent under
the stars (3:6–7); the nations blessed in Abraham on the map (3:8); three crosses on a far hill under a darkened sky (3:13,
as CLAUDE.md allows the crucifixion to be shown); a man's covenant sealed, the seed and the seeds, and the 430 years as a
timeline plate (3:15–18); kept in ward (3:23); the law our tutor, a household slave walking a boy to school (3:24–25);
neither Jew nor Greek, bond nor free, male and female, as a plate (3:28). Galatians 4–6: the heir as a child under
guardians and stewards; the fulness of the time, the star over Bethlehem (no child drawn); days, months, seasons and years
as a plate; Hagar and Sarah with their sons (Genesis' looks: Hagar cerulean, Sarah's mulberry veil); mount Sinai in Arabia
under a dark sky and the Jerusalem that is above in light; the yoke of bondage broken; runners on the course; the leaven in
the lump; the law fulfilled in one word; the works of the flesh as words over a dark, empty street; the fruit of the
Spirit as a botanical plate of a tree bearing nine fruits; bearing one another's burdens; the sower and the reapers; the
large letters in Paul's own hand; the new creature, the dawn over a sown field.

Galatians' own cast, each the same everywhere: Paul only ever ntcast's PAUL faces (in epistle's five lights) and
epistle.paul_fig at a distance; Titus a Greek, bareheaded, short black hair, clean-shaven, a sand tunic with a blue mantle
(as 2 Corinthians draws him); Barnabas as Acts draws him (a green headcloth and robe, a brown beard); Peter (Cephas) in
ntcast's colours (a brown robe, dark hair, a grey-brown beard); John young and beardless in his rust robe; James the Lord's
brother as Acts draws him (white headcloth, grey beard) — not ntcast's James son of Zebedee, who was dead by then (Acts
12:2). A warm scarf would read as long hair: every headcloth and veil here is cool, dark or off-white, except Sarah's
mulberry veil, kept from Genesis.

Restraint: circumcision is never drawn — 2:3, 5:2–12 and 6:12–15 are words beside Paul's face or over plain scenes and
plates; 5:12 is words only, beside Paul's face; 5:15 (bite and devour) words only; the works of the flesh (5:19–21) are
words over a dark, empty street, no one in it; the persecution (1:13) is Acts' night street with the door broken in, no one
struck; the crucifixion (3:13) only three crosses far off against a darkened sky; Paul's infirmity (4:13–15) is told in
words, and the Galatians receiving him is a plain welcome at the gate; "the marks of Jesus" (6:17) words beside Paul's face,
no wounds drawn. God is never drawn (light, the Voice box); angels (1:8, 3:19, 4:14) are a figure of white light with a gold
rim and no face (1:8), or words only; Satan is never drawn.

Plan (3,126 words, two chapters): 1 Not from Men (1–3) · 2 The Fruit of the Spirit (4–6)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("GAL")

META = {
  "id": "galatians", "order": 48, "name": "Galatians", "kanji": "ガラテヤ人への手紙", "thumb": "vol-galatians-", "book": "GAL",
  "title": "Galatians Volume", "volume": "Volume Forty-Eight",
  "lede": "The forty-eighth book of the Bible, in full: Paul's letter to the churches of Galatia — an apostle not from men, the gospel he received through revelation of Jesus Christ, the right hands of fellowship and Cephas withstood at Antioch, justified by faith and not by the works of the law, the sons of Abraham, the law our tutor, all one in Christ Jesus, Hagar and Sarah, stand fast in freedom, walk by the Spirit and the fruit of the Spirit, bear one another's burdens, whatsoever a man soweth, and the large letters in his own hand, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Not from Men", "range": "Galatians 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Paul, an apostle, not from men, neither through man, unto the churches of Galatia; I marvel that ye are so quickly removing unto a different gospel; let him be anathema; the gospel came to me through revelation of Jesus Christ — the persecutor called on the Damascus road, Arabia, fifteen days with Cephas; Titus not compelled; the right hands of fellowship; Cephas withstood to the face at Antioch; I have been crucified with Christ; O foolish Galatians; Abraham believed God; Christ redeemed us from the curse of the law; the law our tutor; ye all are one man in Christ Jesus."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Fruit of the Spirit", "range": "Galatians 4–6", "bible_chapters": [4, 5, 6],
     "blurb": "The heir as a child under guardians; when the fulness of the time came, God sent forth his Son; Abba, Father; no longer a bondservant, but a son; my little children, of whom I am again in travail; Hagar and Sarah, the two covenants, the Jerusalem that is above; for freedom did Christ set us free: stand fast; a little leaven; thou shalt love thy neighbor as thyself; walk by the Spirit; the works of the flesh and the fruit of the Spirit; bear ye one another's burdens; whatsoever a man soweth, that shall he also reap; see with how large letters I write unto you with mine own hand."},
  ],
}
