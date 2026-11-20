"""The James volume of the full edition (the Epistle of James): metadata, the volume cover, and the chapter plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit: the letter box, the study, the sealed scroll), as Paul's
letters are, but the writer is James, the Lord's brother, the James of Acts 15 and 21 and of Galatians 1:19 — "a servant of God
and of the Lord Jesus Christ" (1:1). Paul is never drawn in this volume. jas/common.py also holds the faces and looks of the
other writers of the general letters (Peter old, Silvanus, Mark, Jude), which 1 Peter, 2 Peter and Jude import.

A letter has no narration: every word of the ASV here is James writing to the twelve tribes of the Dispersion (letter boxes:
parchment, a sepia rule down the left edge, a short tail toward James where his face is drawn). The scriptures he quotes are
song boxes (2:8 "Thou shalt love thy neighbor as thyself", 2:23 "And Abraham believed God…", 4:6 "God resisteth the proud").
The commandments he cites inside his own sentence (2:11) stay in his letter box. There is no Voice box: James quotes no word
of God in the first person.

James' face is the Lord's brother as Acts draws him at Jerusalem (act.common.JAMES_LORD: a white headcloth with a cord, grey
hair and beard), in the kit's five lights: earnest (the Acts face itself), stern red at the rebukes (1:13–16, 2:5–7,
2:18–20, 3:14–16, 4:1–5 neighbours, 5:12), grieving blue at 3:9–10 and 4:8–10, white with joy at 1:2–5, gold elsewhere.
At a distance he is jas.art.james_fig (robed(): a stone-grey robe, the white headcloth, a grey mantle).

Drawings (jas.art): James writing at Jerusalem by lamplight, the temple through the window, a young scribe and two elders
of the church listening (the title page and the cover's still life); the twelve tribes of the Dispersion on Acts' map, rings
spreading from Jerusalem; the surge of the sea driven by the wind; the flower of the grass withering under the scorching sun;
the crown of life; the Father of lights — light only, from above, no figure; a man beholding his face in a bronze mirror and
going away; the fatherless and widows visited at their door; the rich man in fine clothing and the poor man in vile clothing
at the synagogue door; the royal law as a chain, one link broken; the brother and sister in want sent away with words;
Abraham offering up Isaac on the altar on the mount, the ram caught in the thicket (no knife drawn, Isaac standing unbound);
Rahab's window on Jericho's wall, the scarlet cord, the messengers gone another way; the horse's bit and the ship's rudder as
a plate; how much wood is kindled by how small a fire; every kind of beast, bird, creeping thing and thing in the sea tamed,
as a plate, the tongue untamed; the fountain, the fig, the olive and the vine as a plate; the fruit of righteousness sown in
peace; wars and fightings as words over an empty field of broken spears; draw nigh to God, a man kneeling under light; the
merchants setting out for the city and the vapor of the morning; the rich men's gold rusted and garments moth-eaten; the
mowers in the field and their hire kept back; the husbandman waiting for the early and latter rain; the patience of Job and
the end of the Lord (Job's look from job/: his flocks and his house restored); the elders anointing the sick with oil;
Elijah praying on Carmel, the little cloud and the rain (Kings' Elijah: the hairy brown mantle); a brother bringing back him
that erred from the way.

Restraint: 2:19 the demons are words only, beside James' stern face; 4:1–2 wars, fightings and killing are words over an
empty field at dusk, broken spears and smoke, no one in it; 4:7 the devil is words only; 5:5–6 the day of slaughter and the
righteous one killed are words over the empty field of the mowers; 2:15 the brother and sister in want are poorly clad, never
naked; 4:4 "ye adulteresses" words only. God is never drawn (1:17 the Father of lights is light; 5:4 the Lord of Sabaoth
hears: words); no angel or demon is drawn.

Plan (2,302 words, one chapter): 1 Doers of the Word (1–5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JAS")

META = {
  "id": "james", "order": 59, "name": "James", "kanji": "ヤコブの手紙", "thumb": "vol-james-", "book": "JAS",
  "title": "James Volume", "volume": "Volume Fifty-Nine",
  "lede": "The fifty-ninth book of the Bible, in full: the letter of James, a servant of God and of the Lord Jesus Christ, to the twelve tribes of the Dispersion — count it all joy, ask of God who giveth liberally, the flower of the grass, every good gift from the Father of lights, be ye doers of the word and not hearers only, no respect of persons, faith apart from works is dead, Abraham and Rahab, the tongue a little member and a fire, the wisdom that is from above, draw nigh to God, what is your life? a vapor, ye rich weep and howl, the patience of Job, the prayer of faith and Elijah praying for rain, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Doers of the Word", "range": "James 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "James, a servant of God and of the Lord Jesus Christ, to the twelve tribes of the Dispersion: count it all joy; he that doubteth is like the surge of the sea; the flower of the grass; the crown of life; every good gift from the Father of lights; be ye doers of the word, and not hearers only — a man beholding his face in a mirror; hold not the faith with respect of persons; faith apart from works is dead — Abraham offering Isaac, Rahab; the tongue a little member, a little fire kindling a great wood; the wisdom from above; draw nigh to God; what is your life? a vapor; ye rich, weep and howl; the husbandman waiteth for the early and latter rain; the patience of Job; the prayer of faith; Elijah prayed, and the heaven gave rain."},
  ],
}
