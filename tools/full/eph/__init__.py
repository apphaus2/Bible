"""The Ephesians volume of the full edition (the Epistle of Paul to the Ephesians): metadata, the volume cover, and the
chapter plans (ch01.py, ch02.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit; the letter box, the study and its prison stages, the
sealed scroll, the doxology panel), with the kit's fit_faces and clip on (face panels only as tall as their words; every
drawing clipped to its panel). A letter has no narration: every word of the ASV here is Paul writing to the saints at
Ephesus (letter boxes: parchment, a sepia rule down the left edge, a short tail toward Paul where his face is drawn); the
scriptures he quotes are song boxes (4:8 "When he ascended on high", 5:14 "Awake, thou that sleepest", 5:31 "For this
cause shall a man leave his father and mother", 6:2–3 "Honor thy father and mother … that it may be well with thee").
There is no Voice box: the letter quotes no word of God spoken in the first person (4:8 and 5:14 are "he saith", a
scripture quoted, and stay song boxes).

Ephesians is written from prison: Paul "the prisoner of Christ Jesus" (3:1), "the prisoner in the Lord" (4:1), "an
ambassador in chains" (6:20), in his own hired dwelling at Rome with the soldier that guarded him (Acts 28:16, 20, 30). The
letter opens on the kit's prison stage — Paul sitting on a bench dictating, the soldier standing by him with his spear,
chained wrist to wrist, the scribe on his mat, the window on Rome — and comes back to it at 1:15–17 (Paul praying), 3:1
(the chain lying across the open letter), 3:14 (Paul bowing his knees, the guard by him), 4:1 (Paul standing, beseeching),
6:10–11 (Paul looking at the soldier he is chained to: their two faces), 6:18–20 (Paul in chains praying) and 6:21–22
(Paul giving the sealed letter to Tychicus at the door). Paul's face is PAUL (earnest gold) for most of his words, PAUL_JOY
(white light) at 1:7–10, 2:4–7 and 5:25–27, PAUL_LAMP at 3:8–12, PAUL_STERN at 4:29–32 and 6:9.

Drawings (eph.art, eph.art2, on Galatians' and Acts' drawings and the epistle kit): the letter's road from Rome by the
Appian Way to Brundisium, across to Macedonia, over to Troas and down to Ephesus; every spiritual blessing in the heavenly
places as light over the heavens; the seal and the earnest as a plate (1:13–14); "far above all rule" as a technical plate
of ranks of light under the right hand — no throne and no figure (1:20–23); "dead through your trespasses" as words over a
dark sky above the roofs of Ephesus, "the prince of the powers of the air" in words only; "his workmanship" as a
craftsman's plate (2:10); the temple courts in plan with the Gentiles' barrier (the soreg) whole (2:11–13) and then broken
down (2:14–18); the household of God as a masonry plate, the chief corner stone lit (2:19–22); the mystery hid for ages
and now revealed as a scroll unrolled from darkness into light (3:5–12); "the breadth and length and height and depth" as
a diagram whose axes run off the plate (3:18–19); the seven "ones" as an emblem plate (4:4–6); "he led captivity captive"
as a triumph of light, the fetters broken on the road, gifts of light falling to men below (4:8); the gifts as a plate
(4:11–13); a little boat tossed by wind and wave (4:14); the body fitly framed, its joints and bands, as a plate under a
head of light (4:15–16); the old man put off and the new put on as garments (4:22–24); the sun going down over the
harbour (4:26); incense rising in a column of light (5:1–2); children of light walking at sunrise (5:8–10); a sleeper and
the dawn at the open door (5:14); brethren singing psalms by lamplight, one sitting with a lyre (5:19); a husband and wife
at the door of their house, a plain household (5:22–24); a bridal veil and a burning lamp as an emblem (5:31–32); a father
sitting with his son at the scroll (6:1–4); a servant and his master in the court of a house (6:5–8); the spiritual hosts of
wickedness as words over darkness (6:12); THE WHOLE ARMOR OF GOD as the volume's set piece — the Roman soldier at full
height on a technical plate, each piece labelled from the text, the fiery darts striking the shield and quenched, no archer
(6:13–17); the benediction over the light (6:23–24).

Ephesians' own cast, each the same everywhere: Paul only ever ntcast's PAUL faces (in epistle's five lights) and
epistle.paul_fig at a distance (sitting on the bench in his dwelling, standing to beseech or to give the letter, kneeling
at 3:14); the soldier that guarded him (epistle.roman_guard: Acts' brass helmet with its red crest, a red cloak, a
red tunic and an iron cuirass, dark stubble; the GUARD face); Tychicus (eph.art.tychicus: an Asian brother — a slate-teal
headcloth with a dark cord, a short brown beard, a grey travelling cloak over a grey-blue robe; the TYCHICUS face); the
scribe at Rome, whom the letter does not name (a dark slate headcloth, a black beard: SCRIBE_LOOK). A warm scarf would read
as long hair: every headcloth and veil here is cool, dark or off-white.

Restraint: 2:1–3 ("the prince of the powers of the air", "children of wrath") words over a dark, empty sky above the roofs,
no figure in the sky; 4:17–19 (lasciviousness, uncleanness) and 5:3–7 (fornication, uncleanness) words over the dark, empty
streets of Ephesus at night; 5:11–12 ("the things which are done by them in secret") words over the dark room, only the
sleeper and the dawn drawn; 5:22–33 shows nothing intimate — a husband and wife standing apart at their door by day, and the
bride only as an emblem, a veil and a lamp, no bride's body; 6:5–9 (servants and masters) a plain household scene, a servant
carrying water and his master pointing the way, no blow, no rod, no chain; "the devil" (4:27, 6:11), "the evil one" (6:16)
and "the spiritual hosts of wickedness" (6:12) are words only, never drawn — the fiery darts are drawn striking the shield
and going out, with no archer; the blood of Christ (1:7, 2:13) and the cross (2:16) are words, the cross drawn nowhere.
God is never drawn: light, rays, a plate's empty gold field marked "THE RIGHT HAND" (1:20). Christ is not drawn in this
volume: "the head" (1:22, 4:15) is a disc of light on the plates; the ascension (4:8–10) is a road of light.
Paul's chain (Acts 28:20) is drawn wrist to wrist, never as a wound.

Plan (3,068 words, two chapters): 1 Rich in Mercy (1–3) · 2 The Whole Armor of God (4–6)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("EPH")

META = {
  "id": "ephesians", "order": 49, "name": "Ephesians", "kanji": "エペソ人への手紙", "thumb": "vol-ephesians-", "book": "EPH",
  "title": "Ephesians Volume", "volume": "Volume Forty-Nine",
  "lede": "The forty-ninth book of the Bible, in full: Paul's letter from his chains at Rome to the saints at Ephesus — every spiritual blessing in the heavenly places, sealed with the Holy Spirit of promise, Christ far above all rule, dead through trespasses and made alive by God rich in mercy, saved by grace through faith, the middle wall of partition broken down, built upon the corner stone, the breadth and length and height and depth of the love of Christ, one body and one Spirit, he led captivity captive, the old man put off and the new man put on, children of light, husbands and wives, children and fathers, servants and masters, the whole armor of God, and Tychicus sent with the letter, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Rich in Mercy", "range": "Ephesians 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Paul, an apostle of Christ Jesus, from his chains at Rome to the saints at Ephesus; every spiritual blessing in the heavenly places; chosen before the foundation of the world; sealed with the Holy Spirit of promise, the earnest of our inheritance; Christ raised far above all rule and authority; dead through trespasses, but God, being rich in mercy, made us alive together with Christ; by grace have ye been saved through faith; his workmanship; the middle wall of partition broken down; fellow-citizens with the saints, built upon Christ Jesus the chief corner stone; the mystery hid for ages; I bow my knees unto the Father; the breadth and length and height and depth; unto him be the glory."}
  ],
}
