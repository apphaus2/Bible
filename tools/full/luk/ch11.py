"""Luke volume, Chapter 11 — The Prodigal Son (Luke 14–15). Every verse, word for word from ref/eng-asv.
The ruler's house on the sabbath: the man with the dropsy healed and let go; the ox fallen into a well; the chief seats and
the lowest place; bid the poor, the maimed, the lame, the blind; the great supper and the excuses — a field, five yoke of
oxen, a wife; the streets and lanes, the highways and hedges. Count the cost: the tower unfinished, the king with ten
thousand; salt that hath lost its savor. The publicans and sinners drawing near and the murmuring; the lost sheep carried
home on the shepherd's shoulders; the woman's lamp and broom and the piece found; and the prodigal son, scene by scene —
the portion divided, the far country lit at night (the riotous living and the harlots in words only), the famine, the
swine in a bare field and the young man among them, I will arise and go to my father, the father running while he was yet
afar off, the best robe and the ring and the shoes, the house lit with music and dancing, the elder brother angry in the
field, and the father come out to entreat him: this thy brother was dead, and is alive again."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art9 as A, ch10 as _prev
from luk.common import (K, Pages, D, F, Q, N, T, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        GUEST, PHARISEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C11-00-Title", "Chapter 11 · The Prodigal Son", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.prodigal("t11", 760, 780, 1501, stage="embrace")}</g>'
    return title(11, "The Prodigal Son", "Luke 14 – 15", svg, "#3A4A2A", v("15:24", frm="this my son was dead,", to="is found."))


SEGS = [D([cp("14:1"), cp("14:2")], lambda w, h: A.dropsy("dr1", w, h, 1401), "#B8987A", head="Is It Lawful to Heal on the Sabbath?", sky=14),
        F([N("14:3", "Pharisees, saying,")], JESUS),
        D([cp("14:4")], lambda w, h: A.dropsy("dr2", w, h, 1402, healed=True), "#B8987A"),
        D([N("14:5", "said unto them,"), cp("14:6")], lambda w, h: A.sheep_pit("sp1", w, h, 1403), "#8FD0E2"),
        D([N("14:7", "saying unto them,"), sy("14:8"), sy("14:9")], lambda w, h: A.wedding_hall("wh1", w, h, 1404, guests=True), "#5A3A2A", head="Friend, Go Up Higher"),
        F([sy("14:10"), sy("14:11")], JESUS_TEACH),
        F([N("14:12", "that had bidden him,"), sy("14:13"), sy("14:14")], JESUS),
        F([N("14:15", "said unto him,")], GUEST, bg=COLD, head="A Great Supper"),
        D([N("14:16", "said unto him,"), sy("14:17")], lambda w, h: A.wedding_hall("wh2", w, h, 1405), "#5A3A2A"),
        D([sy("14:18"), sy("14:19"), sy("14:20")], lambda w, h: A.excuses("ex1", w, h, 1406), "#2A2030", art_h=200),
        D([sy("14:21"), sy("14:22"), sy("14:23"), sy("14:24")], lambda w, h: A.highways("hw1", w, h, 1407), "#8FD0E2"),
        F([N("14:25", "said unto them,"), sy("14:26"), sy("14:27")], JESUS_STERN, bg=RED, head="Count the Cost"),
        D([sy("14:28"), sy("14:29"), sy("14:30")], lambda w, h: A.tower_cost("tc1", w, h, 1408), "#8FD0E2"),
        D([sy("14:31"), sy("14:32"), sy("14:33")], lambda w, h: A.wars_far("wf1", w, h, 1409), "#3A1A1A"),
        D([sy("14:34"), sy("14:35")], lambda w, h: A.salt("sa1", w, h, 1410), "#C8D8E2"),
        # Luke 15
        D([cp("15:1"), N("15:2", "murmured, saying,")], lambda w, h: A.at_meat("am1", w, h, 1501, pharisees=True), "#8A6A4A", head="That Which Was Lost", sky=15),
        D([cp("15:3"), sy("15:4")], lambda w, h: A.lost_sheep("ls1", w, h, 1502), "#5A6A9A"),
        D([sy("15:5"), sy("15:6"), sy("15:7")], lambda w, h: A.on_shoulders("os1", w, h, 1503), "#5A6A9A"),
        D([sy("15:8")], lambda w, h: A.lost_coin("lc1", w, h, 1504), "#5A4A48", head="The Piece Which I Had Lost", art_h=240),
        D([sy("15:9"), sy("15:10")], lambda w, h: A.lost_coin("lc2", w, h, 1505, found=True), "#5A4A48"),
        D([N("15:11", "And he said,"), sy("15:12")], lambda w, h: A.prodigal("pr1", w, h, 1511, stage="portion"), "#8FD0E2", head="A Certain Man Had Two Sons"),
        D([sy("15:13")], lambda w, h: A.prodigal("pr2", w, h, 1513, stage="far"), "#2A1A3A", art_h=240),
        D([sy("15:14")], lambda w, h: A.prodigal("pr3", w, h, 1514, stage="famine"), "#C8B898"),
        D([sy("15:15"), sy("15:16")], lambda w, h: A.prodigal("pr4", w, h, 1515, stage="swine"), "#C8B898", art_h=240),
        D([sy("15:17"), sy("15:18"), sy("15:19")], lambda w, h: A.prodigal("pr5", w, h, 1517, stage="arise"), "#C8B898", head="I Will Arise and Go to My Father"),
        D([sy("15:20", to="moved with compassion,")], lambda w, h: A.prodigal("pr6", w, h, 1520, stage="run"), "#8FD0E2", art_h=260),
        D([sy("15:20", frm="and ran,"), sy("15:21")], lambda w, h: A.prodigal("pr7", w, h, 1521, stage="embrace"), "#8FD0E2", art_h=240),
        D([sy("15:22"), sy("15:23"), sy("15:24")], lambda w, h: A.prodigal("pr8", w, h, 1522, stage="robe"), "#8FD0E2"),
        D([sy("15:25"), sy("15:26"), sy("15:27")], lambda w, h: A.prodigal("pr9", w, h, 1525, stage="elder"), "#4A3A6A", head="Thy Brother Was Dead, and Is Alive Again"),
        D([sy("15:28"), sy("15:29"), sy("15:30")], lambda w, h: A.prodigal("pr10", w, h, 1528, stage="entreat"), "#4A3A6A"),
        D([sy("15:31"), sy("15:32")], A.footed(lambda w, h: A.prodigal("pr11", w, h, 1531, stage="feast"), "#3A3028"), "#0B0B2A", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C11-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE RICH MAN AND LAZARUS")))
