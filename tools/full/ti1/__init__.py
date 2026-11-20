"""The 1 Timothy volume of the full edition (the First Epistle of Paul to Timothy): metadata, the volume cover, and the
chapter plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces and clip; the letter box, the sealed
scroll, the technical plate, the doxology panel), as Galatians is. A letter has no narration: every word of the ASV here is
Paul writing to Timothy (letter boxes: parchment, a sepia rule down the left edge, a short tail toward Paul where his face
is drawn). The scriptures he quotes are song boxes (5:18: the ox that treadeth out the corn, the laborer worthy of his
hire); so are the faithful sayings that read as hymns or creeds — "Christ Jesus came into the world to save sinners" (1:15)
and the mystery of godliness, "He who was manifested in the flesh … Received up in glory" (3:16). The doxologies (1:17,
6:15–16) are glory panels: the words over light, no figure.

The letter is to one man, so the reader stands where Timothy stands: the letter is written by Paul, free and on the road,
in a house in Macedonia (1:3); it goes by Troas across the sea to Ephesus; Timothy receives the sealed roll at his door in
Ephesus and reads it there (the window on the theatre and the temple of Diana), and he is drawn again where the letter
speaks to him — the good warfare (1:18), "let no man despise thy youth" (4:12), the laying on of the hands of the
presbytery (4:14), a little wine for his stomach's sake (5:23), "O Timothy, guard that which is committed unto thee"
(6:20). Paul's faces alternate with these: earnest gold, stern red at the false teachers and the warnings (1:6–7, 4:1–3,
5:6–8, 5:11–15, 6:3–5), grieving blue at "of whom I am chief" (1:15–16).

Drawings (ti1.art, on Galatians', Acts' and the Corinthian letters' drawings and the epistle kit): Paul writing alone in a
house in Macedonia; the letter's road from Philippi to Ephesus on Acts' map; Timothy receiving the roll at his door, and
reading it; the law is not made for a righteous man (1:9–10) as words over a dark, empty street; Saul laying waste the
church (Acts' night street, the door broken in, no one struck: 1:13); faith shipwrecked (1:19) as a broken hull on the
rocks, no one in the water; the church at prayer for kings and all in high place, seen from behind, the governor's hall
on the hill; one God and one mediator as a plate (light above, men below, Christ Jesus between them in ntcast's look);
men praying in every place, lifting up their hands; modest apparel as a plate of plain garments and good works, the
braided hair, gold, pearls and costly raiment set aside as things, worn by no one; the bishop and the deacons as plates
of their qualifications; the house of God, the pillar and ground of the truth, as a pillar plate; every creature of God
good, received with thanksgiving at the table; bodily exercise in the palæstra beside godliness at the lamp; Timothy young
before the elders; the hands of the presbytery laid on him; the church as a family (5:1–2); a widow indeed praying by
her lamp night and day; the widow enrolled as a plate of good works; the ox treading out the corn (5:18); the gate where
two or three witnesses stand; the cup of water and the little wine; a bondservant at the well; food and covering; the
love of money as a root of all kinds of evil (a botanical plate, the root under a heap of coins); the good fight of the
faith (the boxer); Christ Jesus before Pontius Pilate (John's prætorium); the blessed and only Potentate dwelling in
light unapproachable as light alone; the rich laying up a good foundation; the deposit guarded.

1 Timothy's cast (ti1.common, shared by 2 Timothy and Titus): Paul only ever ntcast's PAUL faces (in epistle's lights)
and epistle.paul_fig at a distance; Timothy as Acts draws him — young, beardless, bareheaded, brown hair, a grey-blue
tunic (act.common.TIMOTHY, co2.art.timothy_fig); the elders of Ephesus in cool and off-white headcloths; the women veiled
in cool, dark or off-white veils (a warm scarf would read as long hair).

Restraint: the lawless of 1:9–10 are words over a dark, empty street, no one in it; the persecution (1:13) is Acts' night
street with the door broken in, no one struck; the shipwreck of faith (1:19) a wreck on the rocks, no one drowning;
Hymenæus and Alexander delivered unto Satan (1:20), the devil's condemnation and snare (3:6–7), the seducing spirits and
doctrines of demons (4:1) and "turned aside after Satan" (5:15) are words only, beside Paul's face or over plain scenes —
Satan and demons are never drawn; Adam and Eve (2:13–14) words only; the women of 2:9 are never shown adorned: the
ornaments lie on the plate, worn by no one; the elect angels (5:21) words only; God is never drawn — "the King eternal,
immortal, invisible" (1:17) and "dwelling in light unapproachable; whom no man hath seen" (6:16) are light alone; the
crucifixion is not drawn (2:6 is words over the plate); Christ before Pilate (6:13) is John's quiet hall, Pilate and Jesus
standing, nothing of the scourging.

Plan (2,282 words, one chapter): 1 The Good Fight of the Faith (1–6)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1TI")

META = {
  "id": "1timothy", "order": 54, "name": "1 Timothy", "kanji": "テモテへの第一の手紙", "thumb": "vol-1timothy-", "book": "1TI",
  "title": "1 Timothy Volume", "volume": "Volume Fifty-Four",
  "lede": "The fifty-fourth book of the Bible, in full: Paul's first letter to Timothy, his true child in faith, left at Ephesus — the law is good, if a man use it lawfully; Christ Jesus came into the world to save sinners, of whom I am chief; war the good warfare; prayers for kings; one God, one mediator; the bishop and the deacons; the house of God, the pillar and ground of the truth; great is the mystery of godliness; let no man despise thy youth; widows and elders; godliness with contentment is great gain; the love of money is a root of all kinds of evil; fight the good fight of the faith; O Timothy, guard that which is committed unto thee, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Good Fight of the Faith", "range": "1 Timothy 1–6", "bible_chapters": [1, 2, 3, 4, 5, 6],
     "blurb": "Paul, an apostle, unto Timothy, my true child in faith; tarry at Ephesus and charge certain men not to teach a different doctrine; the law is not made for a righteous man; I was before a blasphemer, and a persecutor, howbeit I obtained mercy; Christ Jesus came into the world to save sinners, of whom I am chief; war the good warfare; supplications for kings; one God, one mediator, himself man, Christ Jesus; lifting up holy hands; the bishop and the deacons; the pillar and ground of the truth; the mystery of godliness; let no man despise thy youth; honor widows that are widows indeed; the laborer is worthy of his hire; use a little wine; godliness with contentment is great gain; the love of money is a root of all kinds of evil; fight the good fight of the faith; the blessed and only Potentate, dwelling in light unapproachable; guard that which is committed unto thee."},
  ],
}
