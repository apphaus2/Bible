"""The Revelation volume of the full edition (Volume Sixty-Six, the last book of the Bible): metadata, the volume cover,
and the chapter plans (ch01.py …).

Revelation is a vision told by John ("I saw …", "I heard …"), closest to Daniel's and Ezekiel's: it is built on the
epistle kit's panels (rev.common.RevKit, on epistle.EpistleKit and Mark's packer), not as a letter. John's narration goes in
captions; the voices he hears in ordinary balloons, a speaker's tag on the panel (RevKit.SPK: Jesus Christ, an angel, one of
the elders, the four living creatures, a voice from heaven …); the songs of heaven (4:8, 4:11, 5:9–13, 7:10–12, 11:15–18,
12:10–12, 15:3–4, 19:1–8) in song boxes; the words of God, the one sitting on the throne, in the Voice box over light
(1:8; 16:1 and 16:17, the voice out of the temple, from the throne; 18:4–20, "come forth, my people"; 21:5–8). Jesus'
words (1:11, 1:17–3:22, 16:15, 22:7, 22:12–16, 22:20) are ordinary balloons.

The people: John, very old, exiled on Patmos — ntcast's JOHN grown old: white hair and a long white beard (rev.common.JOHN_OLD,
JOHN_AWE, JOHN_GRIEF; at a distance rev.art.john_fig, robed in ntcast's rust with a grey mantle, white hair and beard).
Jesus as ntcast draws him, risen (co1.art5.risen_fig): olive-brown skin, dark-brown hair and beard, white robe and pale
mantle, in blinding white light; the Son of man of 1:12–20 is that man among the seven golden candlesticks, the seven
stars in his right hand, a golden girdle at the breast — his eyes as a flame of fire, his feet like burnished brass, the
sharp two-edged sword out of his mouth and his face as the sun are given in the words only, never drawn. Angels are
figures of white light with a gold rim and no faces (rev.art.angel, on epistle.robed), wings only where the text gives
them (none in Revelation's angels; the living creatures' six wings). The twenty-four elders: robed figures in white with
golden crowns on thrones in a ring. The four living creatures: heraldic plates of light (a lion, a calf, a man's face,
a flying eagle, six wings, full of eyes), as Daniel's beasts are heraldic plates.

Restraint (CLAUDE.md; every call made in this volume):
- God is never drawn: the throne is an empty throne in light with the rainbow like an emerald, the sea of glass, the
  seven lamps, lightnings and thunders (4:2–6, 20:11); his words are the Voice box over light.
- Satan is never drawn: the great red dragon (12:3–17, 13:2–4, 16:13, 20:2) is words over a red, star-torn sky; no
  dragon, no serpent. The demons (the unclean spirits like frogs, 16:13–14) are words only.
- The beasts (13, 17) and the false prophet are heraldic plates in the style of Daniel's beasts, never monsters doing
  violence; the mark and 666 a technical plate (13:16–18).
- Babylon the great harlot (17–18): no woman drawn — the golden cup on the scarlet heraldic beast, the seven mountains,
  the city; her fall as the smoke of the burning city seen far off by kings, merchants and shipmasters standing afar.
- The woman arrayed with the sun (12): a figure of light at a distance, robed; the travail and the birth in words only.
- Violence, death and judgment in words over landscapes, sky, sea, fire, smoke and empty places (each panel's choice is
  in its chapter's docstring).

Plan (12,155 words, six chapters)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("REV")

META = {
  "id": "revelation", "order": 66, "name": "Revelation", "kanji": "ヨハネの黙示録", "thumb": "vol-revelation-", "book": "REV",
  "title": "Revelation Volume", "volume": "Volume Sixty-Six",
  "lede": "The sixty-sixth and last book of the Bible, in full: John on Patmos and the Son of man among the seven golden candlesticks, the letters to the seven churches, the throne in heaven and the Lamb that was slain, the seals, the trumpets and the bowls, the woman and the beasts, the fall of Babylon, the Word of God on the white horse, the thousand years, and the new heaven and the new earth and the holy city, new Jerusalem, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "I Am the Alpha and the Omega", "range": "Revelation 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The Revelation of Jesus Christ, sent by his angel unto his servant John; grace and peace to the seven churches that are in Asia; behold, he cometh with the clouds; I am the Alpha and the Omega, saith the Lord God; John in the isle that is called Patmos, in the Spirit on the Lord's day; seven golden candlesticks and one like unto a son of man in the midst of them — fear not; I am the first and the last; then the letters to the angels of the churches in Ephesus, Smyrna, Pergamum, Thyatira, Sardis, Philadelphia and Laodicea: he that hath an ear, let him hear; behold, I stand at the door and knock."},
  ],
}
