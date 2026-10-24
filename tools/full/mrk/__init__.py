"""The Mark volume of the full edition (the Gospel according to Mark): metadata, the volume cover, and the chapter plans
(ch01.py, ...).

Built as Matthew is, on the minor prophets' kit (oba/minor.py: Kit, page packing), and on Matthew's drawings (mrk.art starts
`from mat.art11 import *`: Galilee and its boats, the houses and synagogues, Jerusalem and the temple, Gethsemane,
Golgotha, the tomb); new drawings in mrk.art. Jesus and the recurring cast come only from tools/full/ntcast.py (faces JESUS,
JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN; jesus_fig at a distance). His words are ordinary speech
boxes. The Father's voice from heaven is the Voice box over light (the baptism, the cloud on the mountain); the Spirit at the
baptism is a dove of light; angels, and the young man in white at the tomb (16:5), are figures of white light with a gold
rim and no face. Satan is never drawn: the forty days are Jesus alone in the night wilderness with the wild beasts on the
ridges and the angels of light. Demons and unclean spirits are never drawn, nor any fit or convulsion: their words stand over
empty places or beside Jesus' face, and the healed are drawn at peace. The scripture Mark quotes is set in song boxes.

Mark's own cast (mrk.common), each the same in every chapter; the people Matthew also tells of keep Matthew's looks:
Jairus, the ruler of the synagogue — Matthew's ruler (dark-teal headcloth with a cord, brown beard); his daughter, twelve
years old, bareheaded, in white; the woman with the issue of blood — Matthew's (a slate-violet veil); the Syrophœnician
woman — Matthew's Canaanitish woman; the rich man — Matthew's rich young man (a plum headcloth with a band); the leper,
the scribes, the chief priests, the maid at the fire and the false witness — Matthew's. Mark's alone: the Gerasene man
(drawn only after, clothed and in his right mind: dark curls, a short black beard, a clean undyed robe); Bartimæus (a grey
cloak cast away, then a dark-brown beard and a mid-brown robe on the way); the deaf man of Decapolis (a sand-coloured
headcloth); the blind man of Bethsaida (an olive headcloth); the father of the boy (Matthew's); the scribe who answered
discreetly (slate-blue headcloth with a band, in a warm light); the poor widow (a black veil, a grey robe); Herodias (a
deep plum veil with a gold band) and her daughter (bareheaded, black hair, a gold fillet — at the feast only in words);
Herod the tetrarch from ntcast; Simon of Cyrene (Matthew's figure on the road); Joseph of Arimathæa (Matthew's);
Mary Magdalene from ntcast; Mary the mother of James (a brown veil) and Salome (an olive-green veil); the young man who
followed in a linen cloth is never drawn.

Restraint: the man of the tombs (5:2–5) is words only over the empty tombs and the broken chains and fetters on the rocks;
the swine are a herd running down the steep at a distance, the drowning words over the empty sea; then the man sitting
clothed. The unclean spirit at Capernaum (1:23–26) and the boy's spirit (9:17–27): words over the crowd and the
landscape, the boy drawn only standing at peace beside Jesus. Herodias' daughter's dance and John's death (6:21–29):
words only, over the banquet hall's empty table, the shut prison door and the tomb; nothing of the head or the platter
drawn. The arrest: the sword dropped in the torchlight, the blow in words; the young man who fled naked (14:51–52) words
over the dark garden. The scourging and the crown of thorns words over the empty court and the purple robe laid aside; the
crucifixion three crosses on the hill against a darkened sky, far off; his death words over the darkened hill and the rent
veil; the sealed tomb; the resurrection the stone rolled away, the young man of light, the empty tomb and the linen, then
Jesus risen in white light (16:9–20).

Five verse numbers have no text in the ASV (7:16, 9:44, 9:46, 11:26, 15:28: the USFM carries only a footnote), so the
coverage lists them as omitted, as Matthew's lists 17:21, 18:11 and 23:14.

Plan (14,856 words, nine chapters): 1 The Beginning of the Gospel (1–2) · 2 Peace, Be Still (3–4) · 3 Talitha Cumi
(5:1–6:29) · 4 It Is I (6:30–7:37) · 5 Thou Art the Christ (8:1–9:29) · 6 The Last Shall Be First (9:30–10:52) ·
7 Hosanna (11–12) · 8 Watch (13:1–14:42) · 9 He Is Risen (14:43–16:20)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("MRK")

META = {
  "id": "mark", "order": 41, "name": "Mark", "kanji": "マルコによる福音書", "thumb": "vol-mark-", "book": "MRK",
  "title": "Mark Volume", "volume": "Volume Forty-One",
  "lede": "The forty-first book of the Bible, in full: the gospel of Jesus Christ, the Son of God — the fishermen called by the sea of Galilee, the storm stilled, the dead raised and the multitudes fed, the way to Jerusalem, the cross and the empty tomb, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Beginning of the Gospel", "range": "Mark 1–2", "bible_chapters": [1, 2],
     "blurb": "John in the wilderness and the baptism in the Jordan — thou art my beloved Son; the forty days; the time is fulfilled; Simon and Andrew, James and John called from their nets — I will make you to become fishers of men; the synagogue at Capernaum, the fever, the leper; the palsied man let down through the roof; Levi at the place of toll; and the Son of man lord even of the sabbath."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Peace, Be Still", "range": "Mark 3–4", "bible_chapters": [3, 4],
     "blurb": "The withered hand on the sabbath; the multitude by the sea and the twelve appointed on the mountain; a house divided; whosoever shall do the will of God, the same is my brother; then the parables from a boat — the sower, the lamp, the seed growing secretly, the grain of mustard seed; and a great storm of wind: Teacher, carest thou not that we perish? Peace, be still."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Talitha Cumi", "range": "Mark 5:1–6:29", "bible_chapters": [5, 6], "span": ["5:1", "6:29"],
     "blurb": "The man of the tombs in the country of the Gerasenes — my name is Legion — and the swine down the steep into the sea, the man sitting clothed and in his right mind; the woman who touched his garment; Jairus' daughter — Talitha cumi; the prophet without honor at Nazareth; the twelve sent two by two; and John the Baptist beheaded at Herod's feast."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "It Is I", "range": "Mark 6:30–7:37", "bible_chapters": [6, 7], "span": ["6:30", "7:37"],
     "blurb": "Sheep not having a shepherd; five loaves and two fishes, the companies on the green grass and twelve basketfuls; walking upon the sea in the fourth watch — be of good cheer: it is I; the washing of hands and the tradition of men; the Syrophœnician woman — even the dogs under the table eat of the children's crumbs; and Ephphatha."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "Thou Art the Christ", "range": "Mark 8:1–9:29", "bible_chapters": [8, 9], "span": ["8:1", "9:29"],
     "blurb": "Four thousand fed; the leaven of the Pharisees; the blind man of Bethsaida — I see men, as trees, walking; at Cæsarea Philippi, who say ye that I am? — Thou art the Christ; take up his cross; the transfiguration on a high mountain, garments glistering, exceeding white, and a voice out of the cloud; and the boy below — I believe; help thou mine unbelief."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Last Shall Be First", "range": "Mark 9:30–10:52", "bible_chapters": [9, 10], "span": ["9:30", "10:52"],
     "blurb": "Who is the greatest? — a little child in the midst; the cup of cold water and the salt; what God hath joined together; suffer the little children; the rich man who went away sorrowful — with God all things are possible; the cup and the baptism of James and John; the Son of man came to minister; and blind Bartimæus by the way side at Jericho."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Hosanna", "range": "Mark 11–12", "bible_chapters": [11, 12],
     "blurb": "The colt and the garments in the way — Hosanna; blessed is he that cometh in the name of the Lord; the fig tree and the den of robbers; by what authority?; the husbandmen and the beloved son; Cæsar's and God's; the God of the living; the first commandment of all; David's son and David's Lord; and the poor widow's two mites."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Watch", "range": "Mark 13:1–14:42", "bible_chapters": [13, 14], "span": ["13:1", "14:42"],
     "blurb": "Not one stone upon another; the beginning of travail, the abomination of desolation, the Son of man coming in clouds; the fig tree's tender branch — watch; then the alabaster cruse at Bethany, Judas and the silver, the passover in the upper room — this is my body, this is my blood of the covenant; the cock crowing twice; and Gethsemane: Abba, Father, not what I will."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "He Is Risen", "range": "Mark 14:43–16:20", "bible_chapters": [14, 15, 16], "span": ["14:43", "16:20"],
     "blurb": "The kiss of Judas and the swords and staves; before the high priest — I am; Peter's three denials; Pilate and Barabbas; the purple and the crown of thorns; Golgotha, the darkness over the whole land and the veil of the temple rent — truly this man was the Son of God; the stone at the door of the tomb; and very early on the first day of the week: he is risen; he is not here; go ye into all the world, and preach the gospel to the whole creation."},
  ],
}
