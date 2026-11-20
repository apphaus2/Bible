"""The 1 John volume of the full edition (the First Epistle General of John): metadata, the volume cover, and the chapter
plans (ch01.py, ch02.py).

Built on the letters' shared kit, tools/full/epistle.py, by way of jn1.common.JohnKit (EpistleKit with faces sized to their
words, drawings clipped to their panels, and a page's spare height given to its drawings rather than to a face panel that
ends the page). A letter has no narration: every word of the ASV here is John writing to his little children (letter boxes:
parchment, a sepia rule down the left edge, a short tail toward John where his face is drawn). 1 John quotes no scripture and
no words of God in the first person, so there is no song box and no Voice box.

John the elder (jn1.common, shared with 2 and 3 John): the same John as ntcast's JOHN, the beloved disciple who was young and
beardless in the Gospels, now very old at Ephesus — ntcast JOHN's features and skin, white hair lying close to the head, a
long white beard, the lines of age at the brow and the eye, bareheaded. His faces in five lights, as epistle.py builds Paul's:
JOHN_OLD earnest gold (1:8–10, 3:4–6, 4:4–6, 4:19–21, 5:9–12), JOHN_LAMP lamplight (2:3–6, 3:19–22), JOHN_STERN red light
beside the last hour, the antichrist and the devil (2:18–19, 2:22–25, 3:7–10), JOHN_GRIEF blue (5:16–17), JOHN_JOY white
(2:28–29, 4:11–13). At a distance john_fig: a faded rust robe (the Gospels' rust robe worn pale), a slate-grey mantle, a
staff; standing to dictate in the study at Ephesus (study_john: the young scribe on his mat, the window on the theatre and
Diana's temple), seated at his table in 2 and 3 John. Paul is never drawn in these volumes.

Drawings (jn1.art, on Galatians' and Acts' drawings and the epistle kit): that which was from the beginning as three
remembered scenes of the Gospel in framed insets — Jesus teaching by the sea, the young John and Peter at his feet (heard);
Jesus on the beach at daybreak (seen); the risen Lord in the shut room, Thomas reaching out his hand (handled) — drawn anew on
the kit figures (John's volume's own disciples are older blob figures), Jesus in ntcast's look (jesus_r, co1's risen_fig);
"God is light" as light only; the brethren walking out of the night into the morning; an Advocate with the Father — Jesus
risen before the empty throne of light, the world below; dawn over Ephesus (the true light already shineth); walking in
darkness by night; little children, fathers and young men as a plate; the world passing away (a market thinning into haze);
the anointing as a horn of oil pouring gold; the church hearing the letter read; the church's children under the stars
(behold what manner of love); Jesus risen on the hill (we shall see him even as he is); Cain's field; three crosses far off;
the brother at the rich man's shut door; the brethren at supper; the assayer's touchstone, balance and crucible (prove the
spirits); God is love as a warm light on the brethren; Bethlehem under its star (the Son sent: Galatians' drawing); Jesus
on the beach (we have beheld); perfect love casteth out fear (a child running into its mother's arms at a lit door); the
victor's wreath; the water, the blood and the Spirit as three medallions; the study (the letter read back; the sealed letter
given to the bearer); idols on their plinths and a cold altar.

Restraint: God is never drawn — "God is light" is light only, "God is love" a light with no figure in it, the Father's throne
empty and full of light. The evil one, the devil and the antichrist (2:13–14, 2:18, 2:22, 3:8–12, 4:3, 5:18–19) are words
only, beside John's face or over drawings with no such figure. Cain (3:12) is Genesis' angry, marked face in a framed
portrait beside an empty field — two altars, one smoke rising and one beaten down, a mattock in the furrow — and "whosoever
hateth his brother is a murderer" (3:15) is words over the same field by night; no deed, no Abel, no blood. "He laid down his
life for us" (3:16) is three crosses far off under a darkened sky, nothing on them. The water and the blood (5:6–8) are a
pitcher pouring water and a cup — nothing drawn as blood; the Spirit a dove of light. The rich man shutting up his compassion
(3:17) is a shut door and a man sitting by it with his hand out, no one struck or driven away.

A warm scarf would read as long hair: every headcloth and veil here is cool, dark or off-white.

Plan (2,480 words, two chapters): 1 God Is Light (1 John 1–2) · 2 God Is Love (1 John 3–5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1JN")

META = {
  "id": "1john", "order": 62, "name": "1 John", "kanji": "ヨハネの第一の手紙", "thumb": "vol-1john-", "book": "1JN",
  "title": "1 John Volume", "volume": "Volume Sixty-Two",
  "lede": "The sixty-second book of the Bible, in full: the first letter of John — that which was from the beginning, which we have heard, which we have seen with our eyes, and our hands handled; God is light, and in him is no darkness at all; an Advocate with the Father; the darkness is passing away, and the true light already shineth; little children, fathers, young men; love not the world; it is the last hour; behold what manner of love the Father hath bestowed upon us; we shall be like him; not as Cain; prove the spirits; God is love; perfect love casteth out fear; the water and the blood; little children, guard yourselves from idols, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "God Is Light", "range": "1 John 1–2", "bible_chapters": [1, 2],
     "blurb": "That which was from the beginning, that which we have heard, that which we have seen with our eyes, and our hands handled, concerning the Word of life; that our joy may be made full; God is light, and in him is no darkness at all; if we walk in the light, we have fellowship one with another; if we confess our sins, he is faithful and righteous to forgive us; we have an Advocate with the Father, Jesus Christ the righteous; the darkness is passing away, and the true light already shineth; he that hateth his brother walketh in the darkness; I write unto you, little children, fathers, young men; love not the world, for the world passeth away; it is the last hour, and many antichrists have arisen; ye have an anointing from the Holy One; abide in him."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "God Is Love", "range": "1 John 3–5", "bible_chapters": [3, 4, 5],
     "blurb": "Behold what manner of love the Father hath bestowed upon us, that we should be called children of God; we shall be like him, for we shall see him even as he is; not as Cain, who slew his brother; hereby know we love, because he laid down his life for us; let us not love in word, but in deed and truth; prove the spirits, whether they are of God; beloved, let us love one another, for God is love; God sent his only begotten Son into the world; there is no fear in love: perfect love casteth out fear; we love, because he first loved us; this is the victory that hath overcome the world, even our faith; the Spirit, and the water, and the blood; that ye may know that ye have eternal life; little children, guard yourselves from idols."},
  ],
}
