"""Mark volume, Chapter 7 — Hosanna (Mark 11–12). Every verse, word for word from ref/eng-asv.
Bethphage and the colt tied at the door, loosed; the garments and the branches in the way, Hosanna, Jesus riding down the
mount of Olives toward the city; the temple at eventide; the fig tree with leaves only; the tables of the money-changers
overthrown and the doves loosed; the chief priests' council by night; the fig tree withered from the roots; the mountain
cast into the sea. By what authority?; the baptism of John. The vineyard hedged, the winepress and the tower; what the
husbandmen did to the servants and the beloved son is told in words only, over the vineyard at dusk with its gate open and
no one in it; the corner stone. The Pharisees and the Herodians; the denarius held up; the Sadducees and the seven tombs on
the hillside; the bush burning on the mount at night, God's words in the Voice box (the fire only drawn); the scribe who
answered discreetly beside his face, the two tables of the law in gold light; David's son and David's Lord over the open
psalm scroll; the long robes and the chief seats beside his stern face; the treasury, the rich casting in much, and the poor widow in her black
veil casting in two mites."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art7 as A, ch06 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, PRIEST, SCRIBE_STERN, SADDUCEE, HERODIAN, SCRIBE_WISE, WIDOW)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C07-00-Title", "Chapter 7 · Hosanna", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.entry("t7", 760, 780, 1107)}</g>'
    return title(7, "Hosanna", "Mark 11 – 12", svg, "#3A5A7A", v("11:9", frm="Hosanna;"))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("11:1"), cp("11:2", to="saith unto them,"), sy("11:2", frm="Go your way"), sy("11:3")], lambda w, h: A.bethphage("bp1", w, h, 1101), "#8FD0E2", head="Hosanna", sky=11),
        D([cp("11:4"), cp("11:5", to="said unto them,"), sy("11:5", frm="What do ye"), cp("11:6")], lambda w, h: A.bethphage("bp2", w, h, 1104), "#8FD0E2"),
        D([cp("11:7"), cp("11:8"), cp("11:9", to="cried,"), sy("11:9", frm="Hosanna;"), sy("11:10")], lambda w, h: A.entry("en1", w, h, 1107), "#8FD0E2", art_h=260),
        D([cp("11:11")], lambda w, h: A.temple_court("tc1", w, h, 1111), "#4A2A5A"),
        D([cp("11:12"), cp("11:13"), cp("11:14", to="said unto it,"), sy("11:14", frm="No man eat", to="for ever."), cp("11:14", frm="And his disciples")],
          lambda w, h: A.fig_by_way("fg1", w, h, 1112), "#8FD0E2", head="A House of Prayer"),
        D([cp("11:15"), cp("11:16")], lambda w, h: A.temple_court("tc2", w, h, 1115, cleansed=True), "#C8B898", art_h=240),
        F([cp("11:17", to="said unto them,"), sy("11:17", frm="Is it not written,")], JESUS_STERN, bg=RED),
        D([cp("11:18"), cp("11:19")], lambda w, h: A.priests_court("pc1", w, h, 1118), "#0B0B2A"),
        D([cp("11:20"), cp("11:21", to="saith unto him,"), sy("11:21", frm="Rabbi,")], lambda w, h: A.fig_by_way("fg2", w, h, 1120, withered=True), "#8FD0E2", head="Have Faith in God"),
        F([cp("11:22", to="saith unto them,"), sy("11:22", frm="Have faith")], JESUS),
        D([sy("11:23"), sy("11:24")], lambda w, h: A.mountain_move("mm1", w, h, 1123), "#5A3A6A"),
        F([sy("11:25")], JESUS_TEACH),
        D([cp("11:27"), cp("11:28", to="said unto him,"), sy("11:28", frm="By what authority")], lambda w, h: A.temple_court("tc3", w, h, 1127), "#C8B898", head="By What Authority?"),
        F([cp("11:29", to="said unto them,"), sy("11:29", frm="I will ask"), sy("11:30")], JESUS),
        F([cp("11:31", to="saying,"), sy("11:31", frm="If we shall say,"), sy("11:32", to="From men—"), cp("11:32", frm="they feared"), cp("11:33", to="and say,"),
           sy("11:33", frm="We know not.", to="We know not.")], PRIEST, bg=RED, h=360),
        F([cp("11:33", frm="And Jesus saith", to="unto them,"), sy("11:33", frm="Neither tell I")], JESUS_STERN, bg=RED),
        # Mark 12
        D([cp("12:1", to="in parables."), sy("12:1", frm="A man planted"), sy("12:2")], lambda w, h: A.vineyard_hedged("vh1", w, h, 1201), "#8FD0E2", head="The Beloved Son", stamp=12),
        D([sy("12:3"), sy("12:4"), sy("12:5")], lambda w, h: A.vineyard_hedged("vh2", w, h, 1203, tone="dusk", empty=True), "#4A2A5A"),
        F([sy("12:6"), sy("12:7"), sy("12:8")], JESUS_GRIEF, bg=COLD),
        D([sy("12:9"), sy("12:10", to="this scripture:"), sg("12:10", frm="The stone"), sg("12:11")], lambda w, h: A.corner_stone("cs1", w, h, 1209), "#5A3A6A"),
        F([cp("12:12")], SCRIBE_STERN, bg=RED),
        F([cp("12:13"), cp("12:14", to="say unto him,"), sy("12:14", frm="Teacher, we know"), sy("12:15", to="shall we not give?")], HERODIAN, head="Render unto Cæsar"),
        D([cp("12:15", frm="But he, knowing", to="said unto them,"), sy("12:15", frm="Why make ye"), cp("12:16", to="saith unto them,"), sy("12:16", frm="Whose is this", to="superscription?"),
           cp("12:16", frm="And they said", to="unto him,"), sy("12:16", frm="Cæsar's.")], lambda w, h: A.denarius("dn1", w, h, 1215), "#3A3A4A"),
        F([cp("12:17", to="said unto them,"), sy("12:17", frm="Render unto", to="that are God's."), cp("12:17", frm="And they marvelled")], JESUS),
        F([cp("12:18"), sy("12:19")], SADDUCEE, bg=RED, head="The God of the Living"),
        D([sy("12:20"), sy("12:21"), sy("12:22"), sy("12:23")], lambda w, h: A.seven_tombs("st1", w, h, 1220), "#3A2A4A"),
        F([cp("12:24", to="said unto them,"), sy("12:24", frm="Is it not"), sy("12:25")], JESUS_TEACH),
        D([sy("12:26", to="saying,"), gd("12:26", frm="I am the God"), sy("12:27")], lambda w, h: A.the_bush("bu1", w, h, 1226), "#0B0B2A", art_h=220),
        F([cp("12:28", to="asked him,"), sy("12:28", frm="What commandment")], SCRIBE_WISE, head="The First Commandment"),
        D([cp("12:29", to="Jesus answered,"), sy("12:29", frm="The first is,"), sy("12:30"), sy("12:31")], lambda w, h: A.tables_law("tl1", w, h, 1229), "#3A2A1A"),
        F([cp("12:32", to="said unto him,"), sy("12:32", frm="Of a truth,"), sy("12:33")], SCRIBE_WISE),
        F([cp("12:34", to="said unto him,"), sy("12:34", frm="Thou art not far", to="kingdom of God."), cp("12:34", frm="And no man")], JESUS),
        D([cp("12:35", to="in the temple,"), sy("12:35", frm="How say"), sy("12:36", to="Holy Spirit,"), sg("12:36", frm="The Lord said"), sy("12:37", to="his son?"),
           cp("12:37", frm="And the common")], lambda w, h: A.psalm_scroll("ps1", w, h, 1235), "#2A1A3A", head="David's Son"),
        F([cp("12:38", to="he said,"), sy("12:38", frm="Beware"), sy("12:39"), sy("12:40")], JESUS_STERN, bg=RED),
        D([cp("12:41"), cp("12:42")], lambda w, h: A.treasury("tr1", w, h, 1241), "#D8C8A8", head="Two Mites", art_h=220),
        D([cp("12:43", to="said unto them,"), sy("12:43", frm="Verily"), sy("12:44")], lambda w, h: A.treasury("tr2", w, h, 1243, rich=False), "#D8C8A8", art_h=220)]
PG.extend(K.pack(SEGS, "MRK-C07-D", PG.next(), most=4, lone=1.0, end=nxt("NEXT · WATCH")))
