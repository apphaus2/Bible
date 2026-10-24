"""The Luke volume of the full edition (the Gospel according to Luke): metadata, the volume cover, and the chapter plans
(ch01.py, ...).

Built as Matthew and Mark are, on the minor prophets' kit (oba/minor.py: Kit, page packing, through Mark's MarkKit), and on
their drawings (luk.art starts `from mrk.art9 import *`, which carries every drawing of Matthew and Mark: Galilee and its
boats, the houses and synagogues, Jerusalem and the temple, Gethsemane, Golgotha, the tomb); Luke's own drawings in luk.art,
luk.art2, …. Jesus and the recurring cast come only from tools/full/ntcast.py (faces JESUS, JESUS_TEACH, JESUS_STERN,
JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN; jesus_fig at a distance). His words are ordinary speech boxes. The Father's voice
from heaven is the Voice box over light (the baptism, the cloud on the mountain); the Spirit at the baptism is a dove of
light. Angels — Gabriel, the angel of the Lord and the multitude of the heavenly host over the shepherds, the angel in the
garden (22:43), the two men in dazzling apparel at the tomb — are figures of white light with a gold rim and no face, and
no wings (the text gives them none). Satan is never drawn: the temptation is Jesus alone in the wilderness, on the pinnacle
and on the high place, the devil's words over the empty land. Demons and unclean spirits are never drawn, nor any fit:
their words stand over empty places (never beside Jesus' face), and the healed are drawn at peace. Mary's song, Zacharias'
song, Simeon's song and the scripture Luke quotes are set in song boxes. The genealogy (3:23–38) is a lineage chart over
roll cells, every name in full.

Luke's own cast (luk.common), each the same in every chapter; the people Matthew and Mark also tell of keep their looks:
Zacharias the priest (white robe, a white headcloth with a band, a white beard); Elisabeth (grey hair, a deep teal veil);
Mary (ntcast: blue, a blue veil); Joseph (Matthew's: an ochre robe, a dark olive headcloth, a brown beard); Gabriel (white
light, no face); the shepherds (brown headcloths with cords, rough tunics, staves; one grey-bearded); the infant Jesus
always swaddled and small, in soft light, no face drawn; Simeon (white hair and beard, a slate-blue headcloth with a cord);
Anna (very old, white hair, a dark-plum veil); the boy Jesus at twelve (ntcast's Jesus look, young and beardless, in the
undyed robe); the doctors in the temple (Matthew's scribes); the people of Nazareth (dark headcloths, angry, at a
distance on the brow of the hill); Simon Peter and the sons of Zebedee (ntcast); the widow of Nain (a black veil, a dark-grey
robe) and her son (a sand tunic, drawn only sitting up and standing with her); Simon the Pharisee (Matthew's Pharisee); the
woman that was a sinner (a dark-indigo veil, always at his feet, veiled); Joanna and Susanna among the women (an amber and a
sage veil); the lawyer (a dark-green headcloth with a gold band, a black beard); the good Samaritan (a deep-red striped
cloak and a white headcloth, on his own beast); Martha (ntcast) and Mary her sister (a rose-brown veil, sitting at his
feet); the rich fool (a gold-banded purple headcloth); the woman bowed together (a grey veil; standing straight after);
the prodigal (a sand tunic; in the far country a torn grey tunic; home again in the best robe, white with a gold border),
his father (a white beard, a dark-blue robe) and his elder brother (a brown headcloth, a black beard); the rich man (purple
and fine linen) and Lazarus the beggar (a torn grey tunic, at the gate with the dogs; carried into the light); the ten lepers
(grey and ash, the one Samaritan in rust); the unrighteous judge (a black robe with a gold band) and the widow (Mark's poor
widow); the Pharisee (white) and the publican (a dark tunic, standing afar off) in the temple; Zacchaeus (short, black curls
and beard, a teal headcloth with a cord, a crimson-brown robe); the ruler (Matthew's rich young man); the blind man of Jericho
(Mark's Bartimæus); Herod the tetrarch (ntcast); Pilate (ntcast); Simon of Cyrene and Joseph of Arimathæa (Matthew's);
Cleopas (a brown headcloth with a cord, a greying beard) and his companion (bareheaded, young).

Restraint: the temptation's devil never drawn (above). Nazareth thrusting him out to the brow of the hill (4:29): the crowd
and the cliff edge from below, no one falling; he passes through the midst of them. The unclean spirit at Capernaum (4:33–
35) and Legion (8:26–39): words over the synagogue, the empty tombs and the empty sea, the swine down the steep at a distance,
the healed man sitting clothed at Jesus' feet. The widow of Nain: the bier carried out of the gate at a distance, then the
young man sitting up on it and given to his mother — no body close up. The sinful woman (7:36–50): at his feet with the
alabaster cruse, veiled, her weeping told in words. Herod beheading John (9:9): words only. The good Samaritan: the man
half dead by the road told in words, the road seen empty with his garments thrown down, then the Samaritan's beast and the
inn — no wounds. The Galileans whose blood Pilate mingled, the tower in Siloam (13:1–4): words over the empty court and the
fallen stones. The prodigal's swine are only a herd in a bare field. The rich man and Lazarus: Lazarus at the gate in a torn
tunic and the dogs (no sores drawn); his death and the rich man's burial words over the gate and a shut tomb; Hades words
over darkness and the great gulf (no one in torment drawn), Abraham's bosom as light far off across it. Lot's wife (17:32)
words only. Gethsemane: the angel of light, Jesus kneeling far off in the dark garden; the sweat as great drops of blood
(22:44) in words only. The servant's ear (22:50–51): the sword in the torchlight, the healing in words, no blood. The
mocking, the blows and the smiting (22:63–65) words over the shut door; Herod's soldiers and the gorgeous apparel (23:11)
words over Herod's empty hall with the bright robe laid down. The crucifixion only three crosses on the hill against a
darkened sky, from far off, no wounds or blood; the two malefactors' words over the hill; his death words over the darkened
hill and the rent veil; the sealed tomb. The resurrection: the stone rolled away, the two men in dazzling apparel as figures
of white light, the linen clothes laid by themselves; Jesus risen in white light on the road to Emmaus (their eyes holden),
at the table breaking the bread, in the midst of the eleven; the ascension at Bethany, Jesus in white light with his hands
lifted up, parted from them in a cloud of light (God never drawn).

Two verse numbers have no text in the ASV (17:36 and 23:17: the USFM carries only a footnote), so the coverage lists them as
omitted, as Matthew's and Mark's list theirs.

Plan (25,656 words, seventeen chapters): 1 Gabriel (1) · 2 Good Tidings of Great Joy (2) · 3 The Voice in the Wilderness
(3–4) · 4 Launch Out into the Deep (5–6) · 5 The Widow of Nain (7) · 6 The Sower (8) · 7 Thou Art the Christ (9) · 8 The
Good Samaritan (10) · 9 Teach Us to Pray (11) · 10 Consider the Lilies (12–13) · 11 The Prodigal Son (14–15) · 12 The Rich Man
and Lazarus (16–17) · 13 Zacchaeus (18–19) · 14 Render unto Cæsar (20–21) · 15 This Do in Remembrance of Me (22) · 16 Father,
Into Thy Hands (23) · 17 He Is Risen (24)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("LUK")

META = {
  "id": "luke", "order": 42, "name": "Luke", "kanji": "ルカによる福音書", "thumb": "vol-luke-", "book": "LUK",
  "title": "Luke Volume", "volume": "Volume Forty-Two",
  "lede": "The forty-second book of the Bible, in full: Gabriel in the temple and at Nazareth, the birth in Bethlehem and the shepherds, the Spirit of the Lord upon him at Nazareth, the widow of Nain and the woman with the ointment, the good Samaritan, the lost sheep, the lost coin and the prodigal son, Zacchaeus, the cross, and the road to Emmaus, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Gabriel", "range": "Luke 1", "bible_chapters": [1],
     "blurb": "To Theophilus, that thou mightest know the certainty; Zacharias burning incense in the temple and Gabriel that standeth in the presence of God — thy prayer is heard; Elisabeth hid five months; the angel sent to Nazareth — Hail, thou that art highly favored; behold, the handmaid of the Lord; the babe leaping in the womb; My soul doth magnify the Lord; his name is John; and Zacharias' song: the dayspring from on high hath visited us."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Good Tidings of Great Joy", "range": "Luke 2", "bible_chapters": [2],
     "blurb": "A decree from Cæsar Augustus; no room for them in the inn — the babe wrapped in swaddling clothes and laid in a manger; shepherds abiding in the field by night, the glory of the Lord round about them, and a multitude of the heavenly host: Glory to God in the highest; Mary pondering these sayings in her heart; Simeon in the temple — now lettest thou thy servant depart in peace; Anna the prophetess; and the boy of twelve among the teachers: knew ye not that I must be in my Father's house?"},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Voice in the Wilderness", "range": "Luke 3–4", "bible_chapters": [3, 4],
     "blurb": "The word of God came unto John in the wilderness — every valley shall be filled; what then must we do?; the heaven opened and the Spirit as a dove — thou art my beloved Son; the generations back to Adam, the son of God; forty days tempted of the devil — it is written; the book of Isaiah at Nazareth: the Spirit of the Lord is upon me; the brow of the hill, and he passing through the midst of them; the unclean demon at Capernaum, the fever rebuked, and the good tidings to the other cities also."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Launch Out into the Deep", "range": "Luke 5–6", "bible_chapters": [5, 6],
     "blurb": "By the lake of Gennesaret: Master, we toiled all night, and took nothing — the nets breaking, both boats filled; depart from me, for I am a sinful man; from henceforth thou shalt catch men; the leper made clean; the palsied man let down through the tiles; Levi's great feast; new wine into fresh wine-skins; the lord of the sabbath and the withered hand; the twelve named apostles; and on a level place: blessed are ye poor; love your enemies; good measure, running over; the mote and the beam; and the house founded upon the rock."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Widow of Nain", "range": "Luke 7", "bible_chapters": [7],
     "blurb": "The centurion's servant — Lord, I am not worthy that thou shouldest come under my roof; the gate of Nain, the only son of his mother carried out — Weep not; Young man, I say unto thee, Arise; John's messengers: art thou he that cometh?; a reed shaken with the wind; we piped unto you, and ye did not dance; and in the Pharisee's house the woman with the alabaster cruse at his feet: her sins, which are many, are forgiven; for she loved much — go in peace."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Sower", "range": "Luke 8", "bible_chapters": [8],
     "blurb": "The twelve and the women who ministered of their substance; the sower went forth to sow — the way side, the rock, the thorns and the good ground; a lamp on a stand; my mother and my brethren are these that hear the word of God; the storm on the lake — Master, master, we perish; Legion in the country of the Gerasenes, and the man sitting clothed and in his right mind; the woman who touched the border of his garment; and Jaïrus' daughter: Maiden, arise."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Thou Art the Christ", "range": "Luke 9", "bible_chapters": [9],
     "blurb": "The twelve sent forth to preach and to heal; Herod perplexed — John I beheaded: but who is this?; five loaves and two fishes, and twelve baskets; who say ye that I am? — The Christ of God; take up his cross daily; on the mountain his raiment white and dazzling, Moses and Elijah, a voice out of the cloud: This is my Son, my chosen: hear ye him; the boy healed; the least among you; his face set to go to Jerusalem; and no man, having put his hand to the plow, and looking back, is fit for the kingdom of God."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "The Good Samaritan", "range": "Luke 10", "bible_chapters": [10],
     "blurb": "The seventy sent two and two — the harvest indeed is plenteous, but the laborers are few; lambs in the midst of wolves; woe unto thee, Chorazin!; the seventy returned with joy — rejoice that your names are written in heaven; who is my neighbor? — a certain man going down from Jerusalem to Jericho, the priest and the Levite passing by on the other side, and a certain Samaritan moved with compassion: go, and do thou likewise; and Martha, Martha — Mary hath chosen the good part."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "Teach Us to Pray", "range": "Luke 11", "bible_chapters": [11],
     "blurb": "Lord, teach us to pray — Father, hallowed be thy name; the friend at midnight and three loaves; ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you; by the finger of God; the strong man fully armed; blessed are they that hear the word of God, and keep it; the sign of Jonah; the lamp of thy body is thine eye; and woe unto you Pharisees, and you lawyers, that took away the key of knowledge."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "Consider the Lilies", "range": "Luke 12–13", "bible_chapters": [12, 13],
     "blurb": "Five sparrows sold for two pence; the rich fool and his greater barns — Thou foolish one, this night is thy soul required of thee; consider the ravens, consider the lilies, how they grow; fear not, little flock; let your loins be girded about, and your lamps burning; fire upon the earth; the tower in Siloam; the barren fig tree spared a year; the woman bowed together eighteen years, loosed on the sabbath; the narrow door; go and say to that fox; and O Jerusalem, Jerusalem, as a hen gathereth her own brood under her wings."},
    {"module": "ch11", "dir": "chapter-11", "num": "11", "name": "The Prodigal Son", "range": "Luke 14–15", "bible_chapters": [14, 15],
     "blurb": "The man with the dropsy healed on the sabbath; friend, go up higher; a great supper and all the excuses — go out into the highways and hedges; count the cost of the tower; salt that hath lost its savor; the lost sheep laid on his shoulders, rejoicing; the woman who lit a lamp and swept the house for the piece of silver; and a certain man had two sons — the far country and the swine, I will arise and go to my father, while he was yet afar off his father ran and fell on his neck: this my son was dead, and is alive again; he was lost, and is found."},
    {"module": "ch12", "dir": "chapter-12", "num": "12", "name": "The Rich Man and Lazarus", "range": "Luke 16–17", "bible_chapters": [16, 17],
     "blurb": "The unrighteous steward and the debtors' bonds; ye cannot serve God and mammon; a certain rich man clothed in purple and fine linen, and a beggar named Lazarus laid at his gate — carried away by the angels into Abraham's bosom; between us and you there is a great gulf fixed; if they hear not Moses and the prophets; increase our faith — the sycamine tree; the ten lepers, and the one who turned back to give glory to God; the kingdom of God is within you; and as it was in the days of Noah, and in the days of Lot."},
    {"module": "ch13", "dir": "chapter-13", "num": "13", "name": "Zacchæus", "range": "Luke 18–19", "bible_chapters": [18, 19],
     "blurb": "The unrighteous judge and the widow; the Pharisee and the publican — God, be thou merciful to me a sinner; suffer the little children; one thing thou lackest; a camel through a needle's eye; the blind man by the way side at Jericho; Zacchæus, little of stature, in the sycomore tree — make haste, and come down; for to-day I must abide at thy house; the Son of man came to seek and to save that which was lost; the pounds; blessed is the King that cometh in the name of the Lord; he wept over the city; and a house of prayer."},
    {"module": "ch14", "dir": "chapter-14", "num": "14", "name": "Render unto Cæsar", "range": "Luke 20–21", "bible_chapters": [20, 21],
     "blurb": "By what authority doest thou these things?; the husbandmen and the beloved son; the stone which the builders rejected; whose image and superscription? — render unto Cæsar the things that are Cæsar's, and unto God the things that are God's; the God of the living; David's Lord; the poor widow who cast in all the living that she had; not one stone upon another; Jerusalem compassed with armies; the Son of man coming in a cloud with power and great glory; heaven and earth shall pass away: but my words shall not pass away; and watch ye at every season."},
  ],
}
