"""The 1 Thessalonians volume of the full edition (the First Epistle of Paul to the Thessalonians): metadata, the volume
cover, and the chapter plans (ch01.py, ch02.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces=True and clip=True: face panels sized to
their words, drawings clipped to their panels), as Galatians is. A letter has no narration: every word of the ASV here is
the letter — "Paul, and Silvanus, and Timothy" (1:1) writing to the church of the Thessalonians — in letter boxes
(parchment, a sepia rule down the left edge, a short tail toward Paul where his face is drawn). 1 Thessalonians quotes no
scripture and no word of God in the first person, so it has no song box and no Voice box; "the word of the Lord" of 4:15
is the letter's own words.

The setting (Acts 17:1–10, 18:5): the letter written at Corinth soon after Paul was driven from Thessalonica, when Silas
and Timothy had come down from Macedonia. It opens in the study at Corinth by lamplight (epistle.study, the window on the
Acrocorinth): Paul dictating, Timothy (Acts' look: young, beardless, bareheaded, light-brown hair, a grey-blue tunic) on
the mat writing, Silvanus (Silas: Acts' blue headcloth and robe, a black beard) standing by; then the letter's road from
Corinth by Athens and Berœa to Thessalonica on Acts' map.

Paul's face is earnest gold (PAUL: 1:5–7, 5:11–15) or by lamplight (PAUL_LAMP: 2:3–6), white with joy at 2:13–14,
grieving blue at 3:3–5 (afflictions, the tempter); never stern. The pages are chosen by hand (common.paged): each page's
drawings grow or shrink together to fill it, the words and faces keeping their size.

Drawings (th1.art, on Galatians' and Acts' drawings and the epistle kit): the harbour of Thessalonica, ships putting out
across the gulf under Olympus (1:8, the word sounded forth); a household shrine of idols left empty, the family turned to the dawn (1:9–10); the
empty stocks of Philippi, the rods laid by (2:2); a nurse with her own children by lamplight (2:7); Paul and Silvanus at
the tent-cloth by night, the lamp lit (2:9); Paul exhorting the church in Jason's house, the brethren about him (2:11); the
road out of Thessalonica by night (Acts' drawing: "drove out us", 2:15); the road north at dusk, the gate shut, no one on
it (2:17–18); a victor's wreath in light (2:19); the Acropolis, Paul left alone and Timothy setting out (3:1–2); Timothy
come back to Corinth with the good tidings, at the study's door (3:6); Paul praying at the study's window by night
(3:10). 1 Thessalonians 4–5: the study, the letter read back
(4:1); a plain house front by day (4:3–7); brethren come in from another city welcomed at Jason's door (4:9–10); a man
at his own work, a potter at his wheel (4:11); the tombs at dusk (4:13);
the shout, the trump and the dead in Christ rising (4:16–17) as light breaking in the clouds over the opened tombs, the
trumpet's blast and small figures of the risen caught up toward the light; the dark house and the open door (5:2); the
night and the day, the sleepers' shut house and the watchman on the wall at dawn (5:4–7); the breastplate and the helmet
as a plate of Romans' armour stand (5:8); the short commands as a plate of seven medallions (5:16–22); the epistle read unto
all the brethren and the holy kiss as two brethren greeting (5:26–27); the benedictions over the light (3:11–13, 5:23–24,
5:28).

1 Thessalonians' cast, each the same everywhere: Paul only ever the kit's PAUL faces and epistle.paul_fig; Silvanus and
Timothy as Acts draws them (faces act.common.SILAS and TIMOTHY; figures on epistle.robed); Jason of Thessalonica (Acts
17:5–9), the church's host, an off-white headcloth, a dark beard, an olive-grey robe; the Thessalonians in cool or
off-white headcloths and cool veils (a warm scarf reads as long hair).

Restraint: 2:2 ("shamefully treated at Philippi") is words over the empty stocks and the rods laid by, no one in them;
2:15 ("killed the Lord Jesus and the prophets, and drove out us") is words over the empty road by night; 2:18 ("Satan
hindered us") and 3:5 ("the tempter") are words only, over the shut gate and beside Paul's face — Satan is never drawn;
4:3–7 (fornication, lust, uncleanness) is words over a plain house front, its door shut; 5:3 (sudden destruction, travail)
is words over the dark house. God is never drawn: "the Lord himself shall descend from heaven" (4:16) is light breaking in
the clouds, the archangel's voice only words, the trump of God a trumpet's blast across the sky with no one sounding it;
Christ is not drawn there, only light. The dead in Christ rising are small figures in white light going up from the open
tombs, no faces.

Plan (1,836 words, two chapters): 1 Turned unto God from Idols (1–3) · 2 The Trump of God (4–5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1TH")

META = {
  "id": "1thessalonians", "order": 52, "name": "1 Thessalonians", "kanji": "テサロニケ人への第一の手紙", "thumb": "vol-1thessalonians-", "book": "1TH",
  "title": "1 Thessalonians Volume", "volume": "Volume Fifty-Two",
  "lede": "The fifty-second book of the Bible, in full: Paul's first letter to the church of the Thessalonians, written at Corinth with Silvanus and Timothy soon after he was driven from Thessalonica — ye turned unto God from idols, gentle as a nurse, working night and day, as a father with his own children, Timothy sent and his good tidings, study to be quiet and to work with your hands, them that fall asleep, the shout, the voice of the archangel and the trump of God, caught up in the clouds, the day of the Lord as a thief in the night, sons of light, the breastplate of faith and love and the helmet of hope, rejoice always, pray without ceasing, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Turned unto God from Idols", "range": "1 Thessalonians 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Paul, and Silvanus, and Timothy, unto the church of the Thessalonians — the letter written at Corinth; your work of faith and labor of love and patience of hope; from you hath sounded forth the word of the Lord; ye turned unto God from idols, to wait for his Son from heaven; shamefully treated at Philippi; gentle as a nurse with her own children; working night and day; as a father with his own children; Satan hindered us; ye are our glory and our joy; left behind at Athens alone, we sent Timothy; and Timothy came even now unto us with glad tidings; now we live, if ye stand fast in the Lord."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Trump of God", "range": "1 Thessalonians 4–5", "bible_chapters": [4, 5],
     "blurb": "How ye ought to walk and to please God; this is the will of God, even your sanctification; study to be quiet, and to work with your hands; concerning them that fall asleep, that ye sorrow not, even as the rest, who have no hope; the Lord himself shall descend from heaven, with a shout, with the voice of the archangel, and with the trump of God, and we shall be caught up in the clouds; the day of the Lord so cometh as a thief in the night; ye are all sons of light; the breastplate of faith and love, and for a helmet, the hope of salvation; rejoice always, pray without ceasing, in everything give thanks; salute all the brethren with a holy kiss."},
  ],
}
