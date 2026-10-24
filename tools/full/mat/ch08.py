"""Matthew volume, Chapter 8 — Hosanna to the Son of David (Matthew 21–22). Every verse, word for word from ref/eng-asv.
Bethphage and the ass and colt; Zechariah's words in a song box; the entry down the mount of Olives, garments and branches in
the way, Jerusalem across the valley; the city stirred at its gate; the temple court with the tables overthrown and the doves
loosed, then the blind and the lame and the children crying Hosanna; Bethany at evening; the fig tree with leaves only, and
withered. The chief priests' question; the two sons in the vineyard; the householder's vineyard with hedge, winepress and
tower — the beating and killing of the servants and the son told in his words over the vineyard gate standing empty at
dusk; the stone at the head of the corner. The king's marriage feast drawn through his words: the tables empty, the far city
burning in smoke (no one drawn), the highways, the guest without a wedding-garment, the door onto the outer darkness. The
denarius; the Sadducees' seven brethren over seven tombs; the great commandment over the two tables; David's Lord over the
psalm scroll."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art8 as A, ch07 as _prev
from mat.common import (K, Pages, drawn, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, PHARISEE, PRIEST, SCRIBE, SCRIBE_STERN, SADDUCEE, CROWD_MAN)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C08-00-Title", "Chapter 8 · Hosanna to the Son of David", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 250)">{A.entry("t8", 760, 620, 2101)}</g>'
    return title(8, "Hosanna to the Son of David", "Matthew 21 – 22", svg, "#2A3A5A", v("21:9", frm="Hosanna to the son", to="name of the Lord;"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b):
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

SEGS = [D([cp("21:1"), cp("21:2", to="saying unto them,"), sy("21:2", frm="Go into"), sy("21:3")], lambda w, h: A.bethphage("bp1", w, h, 2101), "#8FD0E2", head="Thy King Cometh", stamp=21),
        D([cp("21:4"), sg("21:5"), cp("21:6"), cp("21:7")], lambda w, h: A.prophecy("pp2", w, h, 2102, tone="day"), "#3A2A2A"),
        D([cp("21:8"), cp("21:9", to="saying,"), sy("21:9", frm="Hosanna")], lambda w, h: A.entry("en1", w, h, 2103), "#8FD0E2", art_h=300),
        D([cp("21:10", to="saying,"), sy("21:10", frm="Who is this?"), cp("21:11", to="said,"), sy("21:11", frm="This is")], lambda w, h: A.city_gate_stirred("gs1", w, h, 2104), "#8FD0E2"),
        D([cp("21:12"), cp("21:13", to="unto them,"), sy("21:13", frm="It is written")], lambda w, h: A.temple_court("tc1", w, h, 2105, cleansed=True), "#8FD0E2",
          head="A House of Prayer"),
        D([cp("21:14"), cp("21:15", to="saying,"), sy("21:15", frm="Hosanna", to="son of David;"), cp("21:15", frm="they were moved")], lambda w, h: A.temple_court("tc2", w, h, 2106, healing=True),
          "#8FD0E2"),
        F([cp("21:16", to="and said unto him,"), sy("21:16", frm="Hearest thou", to="are saying?")], PRIEST, bg=RED),
        F([cp("21:16", frm="And Jesus saith", to="saith unto them,"), sy("21:16", frm="Yea:")], JESUS),
        D([cp("21:17")], lambda w, h: A.bethany("by1", w, h, 2107), "#3A2A5A"),
        D([cp("21:18"), cp("21:19", to="saith unto it,"), sy("21:19", frm="Let there be", to="for ever."), cp("21:19", frm="And immediately")], lambda w, h: A.fig_by_way("fg1", w, h, 2108),
          "#8FD0E2", head="The Fig Tree"),
        D([cp("21:20", to="saying,"), sy("21:20", frm="How did")], lambda w, h: A.fig_by_way("fg2", w, h, 2109, withered=True), "#8FD0E2"),
        F([cp("21:21", to="said unto them,"), sy("21:21", frm="Verily"), sy("21:22")]),
        F([cp("21:23", to="and said,"), sy("21:23", frm="By what")], PRIEST, bg=RED, head="By What Authority?"),
        F([cp("21:24", to="said unto them,"), sy("21:24", frm="I also"), sy("21:25", to="or from men?")], JESUS),
        F([cp("21:25", frm="And they reasoned", to="saying,"), sy("21:25", frm="If we shall"), sy("21:26")], SCRIBE_STERN, bg=COLD),
        F([cp("21:27", to="and said,"), sy("21:27", frm="We know not.", to="We know not.")], PRIEST, bg=COLD),
        F([cp("21:27", frm="He also said", to="unto them,"), sy("21:27", frm="Neither tell")], JESUS_STERN, bg=RED),
        D(S("21:28", 30), lambda w, h: A.two_sons("tw1", w, h, 2110), "#8FD0E2", head="The Two Sons"),
        F([sy("21:31", to="his father?")], JESUS),
        F([cp("21:31", frm="They say,", to="They say,"), sy("21:31", frm="The first.", to="The first.")], PRIEST, bg=COLD),
        F([cp("21:31", frm="Jesus saith", to="unto them,"), sy("21:31", frm="Verily"), sy("21:32")]),
        D(S("21:33", 34), lambda w, h: A.vineyard_hedged("vh1", w, h, 2111), "#8FD0E2", head="The Husbandmen"),
        D(S("21:35", 39), lambda w, h: A.vineyard_hedged("vh2", w, h, 2112, tone="dusk", empty=True), "#2A1A3A"),
        F([sy("21:40")], JESUS),
        F([cp("21:41", to="They say unto him,"), sy("21:41", frm="He will")], PRIEST, bg=COLD),
        D([cp("21:42", to="saith unto them,"), sy("21:42", frm="Did ye never", to="in the scriptures,"), sg("21:42", frm="The stone"), sy("21:43"), sy("21:44")],
          lambda w, h: A.corner_stone("cs1", w, h, 2113), "#FFC890"),
        F([cp("21:45"), cp("21:46")], PHARISEE, bg=RED),
        # Matthew 22
        D([cp("22:1"), sy("22:2"), sy("22:3")], lambda w, h: A.wedding_hall("wh1", w, h, 2201), "#5A2A3A", head="The Marriage Feast", stamp=22),
        F(S("22:4", 5)),
        D(S("22:6", 7), lambda w, h: A.city_smoke("cs2", w, h, 2202), "#3A1A1A"),
        D(S("22:8", 10), lambda w, h: A.highways("hw1", w, h, 2203), "#8FD0E2"),
        D(S("22:11", 12), lambda w, h: A.wedding_hall("wh2", w, h, 2204, stranger=True), "#5A2A3A"),
        D(S("22:13", 14), lambda w, h: A.wedding_hall("wh3", w, h, 2205, guests=True, door=True), "#5A2A3A"),
        F([cp("22:15"), cp("22:16", to="saying,"), sy("22:16", frm="Teacher,"), sy("22:17")], SCRIBE, head="Render unto Cæsar"),
        F([cp("22:18", to="and said,"), sy("22:18", frm="Why make"), sy("22:19", to="tribute money."), cp("22:19", frm="And they brought")], JESUS_STERN, bg=RED),
        D([cp("22:20", to="saith unto them,"), sy("22:20", frm="Whose is"), cp("22:21", to="They say unto him,"), sy("22:21", frm="Cæsar's.", to="Cæsar's."),
           cp("22:21", frm="Then saith he", to="unto them,"), sy("22:21", frm="Render"), cp("22:22")], lambda w, h: A.denarius("dn1", w, h, 2206), "#2A1A2A"),
        F([cp("22:23"), cp("22:24", to="saying,"), sy("22:24", frm="Teacher,")], SADDUCEE, bg=RED, head="Whose Wife Shall She Be?"),
        D(S("22:25", 28), lambda w, h: A.seven_tombs("st1", w, h, 2207), "#3A2A4A"),
        F([cp("22:29", to="answered and said unto them,"), sy("22:29", frm="Ye do err"), sy("22:30"), sy("22:31"), gd("22:32", to="God of Jacob?"), sy("22:32", frm="God is not"), cp("22:33")], JESUS),
        F([cp("22:34"), cp("22:35"), sy("22:36")], PHARISEE, bg=RED, head="The Great Commandment"),
        D([cp("22:37", to="said unto him,"), sy("22:37", frm="Thou shalt love"), sy("22:38"), sy("22:39"), sy("22:40")], lambda w, h: A.tables_law("tl1", w, h, 2208), "#12113A"),
        F([cp("22:41"), cp("22:42", to="saying,"), sy("22:42", frm="What think", to="whose son is he?")], JESUS),
        F([cp("22:42", frm="They say unto him,", to="They say unto him,"), sy("22:42", frm="The son of David.")], PHARISEE, bg=RED),
        D([cp("22:43", to="He saith unto them,"), sy("22:43", frm="How then"), sg("22:44"), sy("22:45"), cp("22:46")], lambda w, h: A.psalm_scroll("ps1", w, h, 2209), "#1A1630")]
PG.extend(K.pack(SEGS, "MAT-C08-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE SON OF MAN COMETH")))
