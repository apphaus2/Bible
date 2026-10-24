"""Luke volume, Chapter 3 — The Voice in the Wilderness (Luke 3–4). Every verse, word for word from ref/eng-asv.
The fifteenth year of Tiberius: John in the wilderness and at the Jordan, Isaiah's words in song boxes; offspring of vipers
beside John's stern face; the axe at the root; the multitudes, the publicans and the soldiers asking, What must we do?; the
fan and the threshing-floor; Herod shutting John up in prison. The baptism: the heavens opened, the Spirit in a bodily form
as a dove of light, the Father's voice in the Voice box over the light. The generations from Jesus back to Adam, the son
of God, as one chart over roll cells (every name, every word). The temptation: Jesus alone in every picture, the devil never
drawn — his words over the empty stones, the kingdoms seen from the height, the pinnacle; Jesus' answers beside his face.
Galilee; the synagogue of Nazareth, the book of Isaiah unrolled (its words in song boxes), To-day hath this scripture been
fulfilled; the widow of Zarephath in the famine and Naaman at the Jordan; the brow of the hill — the crowd and the cliff edge
from below, no one falling; and Jesus passing through the midst of them. Capernaum: the unclean demon's cry over the
synagogue, never drawn and never beside Jesus' face, the rebuke beside his stern face, the man whole; Simon's wife's mother
raised; the sick at sunset; the desert place at day."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art2 as A, ch02 as _prev
from luk.common import (K, Pages, D, F, Q, N, cp, gd, sg, sy, v, title, nxt, chart_roll, cell, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN,
                        BAPTIST, BAPTIST_STERN, CROWD_MAN, COLLECTOR, SOLDIER, NAZARENE, HEROD)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("LUK-C03-00-Title", "Chapter 3 · The Voice in the Wilderness", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#FFD89A"></rect><g transform="translate(0 300)">{A.wilderness("t3", 760, 780, 301, crowd_n=5)}</g>'
    return title(3, "The Voice in the Wilderness", "Luke 3 – 4", svg, "#5A3A2A", v("3:4", frm="The voice of one", to="way of the Lord,"))


SEGS = [D([cp("3:1"), cp("3:2")], lambda w, h: A.wilderness("wl1", w, h, 301), "#FFD89A", head="The Word of God Came unto John", sky=3),
        D([cp("3:3"), N("3:4", "Isaiah the prophet,", "n"), sg("3:5"), sg("3:6")], lambda w, h: A.jordan("jd1", w, h, 302), "#8FD0E2"),
        F([N("3:7", "to be baptized of him,"), sy("3:8")], BAPTIST_STERN, bg=RED, head="Fruits Worthy of Repentance"),
        D([sy("3:9")], lambda w, h: A.axe_root("ax1", w, h, 303), "#3A1A1A"),
        D([N("3:10", "asked him, saying,"), N("3:11", "said unto them,")], lambda w, h: A.jordan("jd2", w, h, 304, crowd_n=9), "#8FD0E2", head="What Then Must We Do?"),
        F([N("3:12", "said unto him,"), N("3:13", "said unto them,")], COLLECTOR, bg=GOLDEN),
        F([Q("3:14", "c", "saying,", "s", "what must we do?", "c", "said unto them,", "s")], SOLDIER, bg=COLD),
        F([cp("3:15"), N("3:16", "saying unto them all,")], BAPTIST, head="He Shall Baptize You in the Holy Spirit"),
        D([sy("3:17"), cp("3:18")], lambda w, h: A.threshing("th1", w, h, 305), "#5A3A6A"),
        D([cp("3:19"), cp("3:20")], lambda w, h: A.prison("pr1", w, h, 306), "#2A2A4A"),
        D([cp("3:21"), Q("3:22", "c", "out of heaven,", "g")], lambda w, h: A.heavens_rent("ho1", w, h, 307), "#2A2A6A", head="Thou Art My Beloved Son", art_h=260)]
PG.extend(K.pack(SEGS, "LUK-C03-D", PG.next(), most=4, lone=0.5))

GEN = [cell("Jesus, the Son (as Was Supposed) of Joseph", "3:23-26", "#F3EFE6"),
       cell("Unto Zerubbabel, and Nathan", "3:27-31", "#8FD0E2"),
       cell("David, back to Abraham", "3:32-34", "#FFD23F"),
       cell("Back to Adam, the Son of God", "3:35-38", "#E8A0C8")]
K.label()                                          # the genealogy's cuts are on the chart page, not the next panel's label


@P("LUK-C03-E-P01-TheSonOfAdamTheSonOfGod", "The Son of Adam, the Son of God")
def generations(n):
    return chart_roll(GEN, lambda w, h: A.lineage(w, h, top=0.05), 470, "Luke 3:23–38 — The Son of Adam, the Son of God", n,
                      ref="LUKE 3:23–38", tag="THE GENERATIONS · LUKE 3")


SEGS = [D([cp("4:1"), cp("4:2")], lambda w, h: A.alone("al1", w, h, 401), NIGHT, head="Tempted of the Devil", sky=4),
        D([N("4:3", "said unto him,")], lambda w, h: A.stones_close("sc1", w, h, 402), "#5A3A5A"),
        F([N("4:4", "answered unto him,")], JESUS_TEACH),
        D([cp("4:5"), N("4:6", "said unto him,"), sy("4:7")], lambda w, h: A.high_mountain("hm1", w, h, 403), "#3A1A4A", head="All the Kingdoms of the World"),
        F([N("4:8", "said unto him,")], JESUS_STERN, bg=RED),
        D([N("4:9", "said unto him,"), sy("4:10"), sy("4:11")], lambda w, h: A.pinnacle("pn1", w, h, 404), "#2A3A7A", head="The Pinnacle of the Temple"),
        F([N("4:12", "said unto him,")], JESUS),
        D([cp("4:13")], lambda w, h: A.alone("al2", w, h, 405, tone="dawn"), "#3A2A5A"),
        D([cp("4:14"), cp("4:15")], lambda w, h: A.galilee("gl1", w, h, 406), "#8FD0E2", head="The Spirit of the Lord Is upon Me"),
        D([cp("4:16"), cp("4:17")], lambda w, h: A.reading("rd1", w, h, 407), "#C8B490", art_h=240),
        D([sg("4:18"), sg("4:19")], lambda w, h: A.reading("rd2", w, h, 408), "#C8B490"),
        D([cp("4:20"), N("4:21", "unto them,")], lambda w, h: A.reading("rd3", w, h, 409, seated_=True), "#C8B490"),
        F([Q("4:22", "c", "and they said,", "s")], NAZARENE, bg=COLD, head="No Prophet Is Acceptable in His Own Country"),
        F([N("4:23", "said unto them,"), N("4:24", "And he said,")], JESUS_STERN, bg=RED),
        D([sy("4:25"), sy("4:26")], lambda w, h: A.zarephath("zp1", w, h, 410), "#E8D8B0"),
        D([sy("4:27")], lambda w, h: A.naaman("nm1", w, h, 411), "#8FD0E2"),
        D([cp("4:28"), cp("4:29")], lambda w, h: A.brow("bw1", w, h, 412), "#5A3A5A", head="The Brow of the Hill", art_h=260),
        D([cp("4:30")], lambda w, h: A.through_midst("tm1", w, h, 413), "#3A2A5A", art_h=260),
        D([cp("4:31"), cp("4:32")], lambda w, h: A.synagogue("sy1", w, h, 414), "#C8B490", head="With Authority and Power"),
        D([cp("4:33"), sy("4:34")], lambda w, h: A.synagogue("sy2", w, h, 415, crowd_n=10), "#5A4A6A"),
        F([Q("4:35", "c", "saying,", "s", "come out of him.", "c")], JESUS_STERN, bg=RED),
        D([N("4:36", "one with another, saying,"), cp("4:37")], lambda w, h: A.synagogue_peace("sp1", w, h, 416), "#C8B490", art_h=240),
        D([cp("4:38"), cp("4:39")], lambda w, h: A.fever("fv1", w, h, 417), "#B8987A", head="He Rebuked the Fever"),
        D([cp("4:40"), Q("4:41", "c", "and saying,", "s", "Son of God.", "c")], lambda w, h: A.at_even("ae1", w, h, 418), "#4A2A5A", art_h=220),
        D([cp("4:42")], lambda w, h: A.before_day("bd1", w, h, 419, found=True), "#0B1A3A", head="To the Other Cities Also"),
        F([N("4:43", "said unto them,"), cp("4:44")], JESUS_TEACH)]
PG.extend(K.pack(SEGS, "LUK-C03-F", PG.next(), most=4, lone=0.5, end=nxt("NEXT · LAUNCH OUT INTO THE DEEP")))
