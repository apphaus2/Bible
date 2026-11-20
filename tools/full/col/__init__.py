"""The Colossians volume of the full edition (the Epistle of Paul to the Colossians): metadata, the volume cover, and the
chapter plans (ch01.py, ch02.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces and clip), and on Philippians, the first
of the prison letters: col.common takes the cast from php.common, col.art its drawings from php.art2 (`from php.art2 import
*`). A letter has no narration: every word of the ASV here is Paul writing to the saints at Colossæ (letter boxes, a short
tail toward Paul where his face is drawn). Colossians quotes no scripture and gives no word of God in the first person: no
song boxes, no Voice box. The greetings of 4:10–14 are epistle.greetings() cells, each with its man's face.

Written from Paul's bonds at Rome (4:3, 4:18) and carried by Tychicus with Onesimus (4:7–9): the volume opens on the prison
stage (Paul chained to the soldier, Timothy writing on his mat) and ends on Paul's own hand writing the salutation, the iron
cuff on his wrist and the chain running off the table ("Remember my bonds").

Paul's face: by lamplight praying at 1:9–12 and 4:2–4, white with joy at 1:28–29 and 2:9–10, stern red at 2:20–23 ("handle
not, nor taste, nor touch"), earnest gold elsewhere.

Drawings (col.art): the prison study at Rome; the letter's road from Rome by Brundisium, Corinth and Ephesus up the Lycus to
Colossæ; Epaphras telling Paul of the church at Colossæ (1:7–8); a road out of a dark country into the dawn (1:13); the Son,
the image of the invisible God, as the light at the centre of all things created, a plate — thrones, dominions,
principalities and powers four lights with no form, the things visible (sun, moon, stars, sea, mountains, trees, beasts,
birds, fishes, man) about them (1:15–17); three crosses far off with a broad light breaking behind them (1:20); Paul hearing
his letter read back in his bonds (1:24–25); the mystery, the sealed chest and the chest opened in light (1:26–27); the Lycus
valley — Laodicea, Hierapolis with its white terraces, Colossæ under snowy Mount Cadmus (2:1); a tree's deep roots and a wall
going up course by course (2:7); the philosophers' colonnade (2:8, 1 Corinthians' drawing); buried with him in baptism, the
sealed tomb and the river (2:12, 1 Corinthians' and Romans' drawings); the bond nailed to the cross, a written sheet blotted
out on a rough beam, no one on it (2:14); a triumph under a Roman arch (2:15, 2 Corinthians' drawing); meat, drink, a feast
day, a new moon and the sabbath casting their shadows away from the light, a plate (2:16–17); the head and the body knit
together by joints and bands, a plate (2:19); the earth at evening and the heavens opened in light, no one drawn there
(3:1–4); the vices as words over a dark, empty street (3:5–8, Galatians' drawing); the old garment cast down and the new
white robe (3:9–10); five robes on a rail and love the gold girdle over them, a plate (3:12–14); the church singing psalms
by lamplight (3:16, 1 Corinthians' drawing); a man and his wife at their door with their children (3:18–21, 1 Corinthians'
drawing); a servant carrying water and the master paying wages (3:22–4:1); the salt bowl on the table and two men talking in
the street (4:6); Tychicus taking the sealed letter from Paul in the doorway, Onesimus ready for the road (4:7–9); the two
letters going between Colossæ and Laodicea (4:16); Paul's own hand and his chain (4:18).

The cast (php.common, the same in all three prison letters): Paul only ever the kit's faces and epistle.paul_fig, chained
to epistle.roman_guard; Timothy (Acts); Epaphras an indigo headcloth, dark-grey beard; Tychicus a slate-teal headcloth with
a cord, short brown beard, grey travelling cloak; Onesimus young, bareheaded, short black curls, an undyed tunic; Aristarchus
bareheaded, black hair and beard; Mark (Acts' colours) young with a stubble; Jesus called Justus an off-white headcloth with
a blue band; Luke bareheaded, greying hair and beard; Demas young, clean-shaven, light-brown hair. No warm headcloths.

Restraint: the vices of 3:5–8 (fornication, uncleanness, passion …) are words only, over a dark, empty street with every door
shut; "the wrath of God" (3:6) words only; circumcision (2:11) is never drawn — the panel shows the sealed tomb and the river
of 2:12; the cross only far off (1:20), and at 2:14 only a beam with the bond nailed to it, no figure; the triumph (2:15) is a
procession of standards under the arch, no captives drawn; angels (1:16, 2:18) are words only, or the four formless lights of
the plate; the household (3:18–4:1) is plain scenes — at the door, at the well, wages paid — nothing harsh; Paul's bonds are
the chain at his wrist, nothing more. God is never drawn (light); Christ is drawn only as light (1:15–17, 3:1).

Plan (2,001 words, two chapters): 1 The Image of the Invisible God (1–2) · 2 Seek the Things That Are Above (3–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("COL")

META = {
  "id": "colossians", "order": 51, "name": "Colossians", "kanji": "コロサイ人への手紙", "thumb": "vol-colossians-", "book": "COL",
  "title": "Colossians Volume", "volume": "Volume Fifty-One",
  "lede": "The fifty-first book of the Bible, in full: Paul's letter from his bonds at Rome to the saints at Colossæ, carried by Tychicus and Onesimus — the image of the invisible God, the firstborn of all creation, in whom all things were created and in whom all things consist; peace through the blood of his cross; Christ in you, the hope of glory; rooted and builded up in him; buried with him in baptism; the bond nailed to the cross; a shadow of the things to come; seek the things that are above; put off the old man and put on the new; love, the bond of perfectness; wives, husbands, children, fathers, servants and masters; speech seasoned with salt; the greetings of Aristarchus, Mark, Justus, Epaphras, Luke and Demas; and remember my bonds, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Image of the Invisible God", "range": "Colossians 1–2", "bible_chapters": [1, 2],
     "blurb": "Paul and Timothy to the saints at Colossæ — the letter written in his bonds at Rome; the gospel bearing fruit in all the world, as ye learned of Epaphras; delivered out of the power of darkness into the kingdom of the Son of his love; who is the image of the invisible God, the firstborn of all creation, for in him were all things created, thrones or dominions or principalities or powers, and in him all things consist; the head of the body, the church; peace through the blood of his cross; the mystery hid for ages, Christ in you, the hope of glory; for them at Laodicea; rooted and builded up in him; philosophy and vain deceit; buried with him in baptism; the bond nailed to the cross; a shadow of the things to come, but the body is Christ's; handle not, nor taste, nor touch."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Seek the Things That Are Above", "range": "Colossians 3–4", "bible_chapters": [3, 4],
     "blurb": "If then ye were raised together with Christ, seek the things that are above; put to death your members which are upon the earth; ye have put off the old man and put on the new; put on a heart of compassion, kindness, lowliness, meekness, longsuffering, and above all these things love, the bond of perfectness; psalms and hymns and spiritual songs; wives, husbands, children, fathers; servants and masters; continue stedfastly in prayer, for which I am also in bonds; let your speech be always with grace, seasoned with salt; Tychicus and Onesimus sent; Aristarchus my fellow-prisoner, Mark, Jesus called Justus, Epaphras, Luke the beloved physician, and Demas; read it also at Laodicea; say to Archippus, fulfil thy ministry; the salutation of me Paul with mine own hand — remember my bonds."},
  ],
}
