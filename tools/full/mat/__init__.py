"""The Matthew volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Built on the minor prophets' kit (oba/minor.py: Kit, vista, page packing). Jesus and the recurring cast come only from
tools/full/ntcast.py (faces JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN; jesus_fig at a distance).
His words are ordinary speech boxes. The Father's voice from heaven is the Voice box over light; the Spirit at the baptism is
a dove of light; an angel of the Lord is a figure of white light with a gold rim and no face (mat.art.angel). The devil is
never drawn: his words stand over the empty wilderness, the pinnacle and the mountain, never beside a face, and Jesus is
alone in every picture of the temptation. Demons are never drawn: the healed are drawn at peace. The scripture Matthew
quotes as fulfilled is set in song boxes (sg), so it stands apart from the narration.

Matthew's own cast (mat.common): Joseph the husband of Mary, a brown beard and an ochre headcloth with a cord (ochre robe at a
distance); Mary from ntcast (blue); the wise-men, one dark-bearded in a purple headcloth, one white-bearded in teal, the third
in red at a distance, on camels; Herod the king, grey-bearded, a purple headcloth with a gold band (his son Herod the tetrarch
is ntcast.HEROD, black-bearded); the chief priests and scribes in white and slate-blue headcloths with bands.

Restraint: Herod's slaughter of the children (2:16) is words only, over Bethlehem's empty street at night with every door
shut; Rachel weeping (2:18) over the empty hills of Ramah; John's death (14:10–11) words over the prison; Judas's death
(27:5) words only over the potter's field; the scourging and the crown of thorns words over the empty court and the purple
robe laid aside; the crucifixion three crosses on the hill against a darkened sky, from a distance; his death words over the
darkened hill and the rent veil; the sealed tomb; the resurrection the stone rolled away, the empty tomb, then Jesus risen in
white light.

Plan (23,397 words, eleven chapters): 1 The Son of David (1–4) · 2 The Sermon on the Mount (5–7) · 3 The Harvest Is
Plenteous (8–10) · 4 Lord of the Sabbath (11–12) · 5 The Kingdom of Heaven Is Like (13–14) · 6 Thou Art the Christ (15–17) ·
7 The First Shall Be Last (18–20) · 8 Hosanna to the Son of David (21–22) · 9 The Son of Man Cometh (23–25) · 10 Gethsemane
(26) · 11 He Is Risen (27–28)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("MAT")

META = {
  "id": "matthew", "order": 40, "name": "Matthew", "kanji": "マタイによる福音書", "thumb": "vol-matthew-", "book": "MAT",
  "title": "Matthew Volume", "volume": "Volume Forty",
  "lede": "The fortieth book of the Bible and the first of the New Testament, in full: the book of the generation of Jesus Christ, the wise-men and the star, the voice in the wilderness, the sermon on the mount, the healings and the parables of the kingdom, the transfiguration, the entry into Jerusalem, the last supper and the cross, and the empty tomb — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Son of David", "range": "Matthew 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "The book of the generation of Jesus Christ, the son of David, the son of Abraham: three times fourteen generations; Joseph's dream — thou shalt call his name JESUS; Immanuel, God with us; the wise-men from the east and the star that stood over the young child; gold and frankincense and myrrh; the flight into Egypt and Rachel weeping for her children; John the Baptist in the wilderness; the heavens opened and the Spirit as a dove — this is my beloved Son; forty days in the wilderness — it is written; and the fishers of men by the sea of Galilee."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Sermon on the Mount", "range": "Matthew 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "He went up into the mountain and opened his mouth and taught them: blessed are the poor in spirit; ye are the salt of the earth, ye are the light of the world; not to destroy, but to fulfil; but I say unto you — love your enemies; when thou prayest, enter into thine inner chamber: Our Father who art in heaven; treasures in heaven; consider the lilies of the field; judge not; ask, and it shall be given you; the narrow gate; by their fruits ye shall know them; and the house built upon the rock."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Harvest Is Plenteous", "range": "Matthew 8–10", "bible_chapters": [8, 9, 10],
     "blurb": "Lord, if thou wilt, thou canst make me clean; the centurion — I have not found so great faith, no, not in Israel; the foxes have holes; the tempest and the great calm — what manner of man is this?; the Gadarenes and the swine; thy sins are forgiven, arise and walk; Matthew at the place of toll; new wine into fresh wine-skins; the border of his garment and the damsel that sleepeth; the harvest indeed is plenteous, but the laborers are few; and the twelve sent forth as sheep in the midst of wolves."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Lord of the Sabbath", "range": "Matthew 11–12", "bible_chapters": [11, 12],
     "blurb": "Art thou he that cometh, or look we for another?; a reed shaken with the wind; we piped unto you, and ye did not dance; woe unto thee, Chorazin; come unto me, all ye that labor and are heavy laden — my yoke is easy, and my burden is light; the grainfields on the sabbath — the Son of man is lord of the sabbath; stretch forth thy hand; a bruised reed shall he not break; a kingdom divided against itself; the sign of Jonah; and who is my mother? and who are my brethren?"},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Kingdom of Heaven Is Like", "range": "Matthew 13–14", "bible_chapters": [13, 14],
     "blurb": "Behold, the sower went forth to sow; the tares of the field; a grain of mustard seed; leaven hid in three measures of meal; a treasure hidden in the field and one pearl of great price; a net cast into the sea; a prophet is not without honor, save in his own country; Herod's birthday and the death of John; five loaves and two fishes, and twelve baskets full; and in the fourth watch of the night he came unto them, walking upon the sea — Lord, save me."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Thou Art the Christ", "range": "Matthew 15–17", "bible_chapters": [15, 16, 17],
     "blurb": "The tradition of the elders; if the blind guide the blind; the Canaanitish woman — even the dogs eat of the crumbs; seven loaves and seven baskets full; the signs of the times; the leaven of the Pharisees; at Cæsarea Philippi — but who say ye that I am? Thou art the Christ, the Son of the living God; get thee behind me; take up his cross; the high mountain, Moses and Elijah, and a voice out of the bright cloud — hear ye him; faith as a grain of mustard seed; and the shekel in the fish's mouth."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The First Shall Be Last", "range": "Matthew 18–20", "bible_chapters": [18, 19, 20],
     "blurb": "Who then is greatest in the kingdom of heaven? — a little child set in the midst; the ninety and nine and the one that goeth astray; where two or three are gathered together; seventy times seven, and the servant that owed ten thousand talents; what God hath joined together; suffer the little children; the rich young man — it is easier for a camel to go through a needle's eye; the laborers in the vineyard — the last shall be first; are ye able to drink the cup?; and the two blind men at Jericho."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Hosanna to the Son of David", "range": "Matthew 21–22", "bible_chapters": [21, 22],
     "blurb": "Thy King cometh unto thee, meek, and riding upon an ass; Hosanna to the son of David; my house shall be called a house of prayer; the fig tree withered away; by what authority doest thou these things?; the two sons; the husbandmen of the vineyard — the stone which the builders rejected; the marriage feast of the king's son — many are called, but few chosen; render unto Cæsar the things that are Cæsar's; in the resurrection whose wife shall she be?; and the great commandment."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "The Son of Man Cometh", "range": "Matthew 23–25", "bible_chapters": [23, 24, 25],
     "blurb": "Woe unto you, scribes and Pharisees, hypocrites! — blind guides, that strain out the gnat, and swallow the camel; whited sepulchres; O Jerusalem, Jerusalem, as a hen gathereth her chickens; not one stone upon another; wars and rumors of wars; the sun darkened and the Son of man coming on the clouds of heaven; as were the days of Noah; watch therefore; the ten virgins and the door that was shut; the talents — well done, good and faithful servant; and the sheep and the goats — inasmuch as ye did it unto one of these my brethren, even these least, ye did it unto me."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "Gethsemane", "range": "Matthew 26", "bible_chapters": [26],
     "blurb": "After two days the passover cometh; the alabaster cruse at Bethany; thirty pieces of silver; one of you shall betray me — is it I, Lord?; take, eat; this is my body — this is my blood of the covenant; before the cock crow, thou shalt deny me thrice; in Gethsemane — my Father, if it be possible, let this cup pass away from me: nevertheless, not as I will, but as thou wilt; could ye not watch with me one hour?; the kiss and the swords and staves; before Caiaphas — thou hast said; and Peter by the fire: I know not the man."},
  ],
}
