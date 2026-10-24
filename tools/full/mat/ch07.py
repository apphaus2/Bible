"""Matthew volume, Chapter 7 — The First Shall Be Last (Matthew 18–20). Every verse, word for word from ref/eng-asv.
The little child set in the midst; the millstone by the deep (no one drawn); the lost sheep on the mountains; two or three
gathered; seventy times seven and the parable of the king's reckoning, his words over the king's hall, the debtor seized by
the cloak in the street and the shut prison door (the tormentors are words only). Beyond the Jordan: one flesh; the little
children blessed; the rich young man beside his face and going away sorrowful; the camel and the needle's eye; the twelve
thrones, empty, in light. The vineyard drawn through the day — the hiring at dawn, the idle in the marketplace, the paying
at even. The road up to Jerusalem; the mother of the sons of Zebedee; the cup; the two blind men at Jericho. Verse 18:11
has no words in the ASV."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art7 as A, ch06 as _prev
from mat.common import (K, Pages, drawn, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, JOHN, PHARISEE, RICH_YOUNG, RICH_SAD, ZEBEDEE_MOTHER, BLIND)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C07-00-Title", "Chapter 7 · The First Shall Be Last", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A3A7A"></rect><g transform="translate(0 300)">{A.vineyard("t7", 760, 780, 2001, tone="dusk", hire=False, pay=True)}</g>'
    return title(7, "The First Shall Be Last", "Matthew 18 – 20", svg, "#2A2A5A", v("20:16"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b):
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

SEGS = [D([cp("18:1", to="saying,"), sy("18:1", frm="Who then"), cp("18:2"), cp("18:3", to="and said,"), sy("18:3", frm="Verily"), sy("18:4"), sy("18:5")],
          lambda w, h: A.child_midst("cm1", w, h, 1801), "#8FD0E2", head="As Little Children", stamp=18),
        D(S("18:6", 7), lambda w, h: A.millstone("ml1", w, h, 1802), "#2A2A4A"),
        F(S("18:8", 10), JESUS_STERN, bg=RED),
        D(S("18:12", 14), lambda w, h: A.lost_sheep("ls1", w, h, 1803), "#5A3A6A", head="The Ninety and Nine"),
        F(S("18:15", 17)),
        F(S("18:18", 20), JESUS),
        F([cp("18:21", to="said to him,"), sy("18:21", frm="Lord, how oft")], PETER, head="Seventy Times Seven"),
        F([cp("18:22", to="unto him,"), sy("18:22", frm="I say not")]),
        D(S("18:23", 27), lambda w, h: A.king_hall("kh1", w, h, 1804), "#2A3A5A"),
        D(S("18:28", 30), lambda w, h: A.seized("sz1", w, h, 1805), "#C8A890"),
        D(S("18:31", 33), lambda w, h: A.king_hall("kh2", w, h, 1806, kneel=False, angry=True), "#2A3A5A"),
        D(S("18:34", 35), lambda w, h: A.prison_door("pd3", w, h, 1807), "#5A5048"),
        # Matthew 19
        D([cp("19:1"), cp("19:2"), cp("19:3", to="and saying,"), sy("19:3", frm="Is it lawful")], lambda w, h: A.jordan("jd3", w, h, 1901, jesus_=True, crowd_n=6, john=False), "#8FD0E2",
          head="What God Hath Joined Together", stamp=19),
        F([cp("19:4", to="answered and said,"), sy("19:4", frm="Have ye not"), sy("19:5"), sy("19:6")]),
        F([cp("19:7", to="They say unto him,"), sy("19:7", frm="Why then")], PHARISEE, bg=RED),
        F([cp("19:8", to="He saith unto them,"), sy("19:8", frm="Moses for"), sy("19:9")], JESUS_STERN, bg=RED),
        F([cp("19:10", to="say unto him,"), sy("19:10", frm="If the case")], PETER),
        F([cp("19:11", to="said unto them,"), sy("19:11", frm="Not all men"), sy("19:12")]),
        D([cp("19:13"), cp("19:14", to="Jesus said,"), sy("19:14", frm="Suffer the"), cp("19:15")], lambda w, h: A.children_blessed("cb1", w, h, 1902), "#8FD0E2",
          head="Suffer the Little Children"),
        F([cp("19:16", to="and said,"), sy("19:16", frm="Teacher,")], RICH_YOUNG, head="One Thing Thou Lackest"),
        F([cp("19:17", to="said unto him,"), sy("19:17", frm="Why askest")]),
        F([cp("19:18", to="He saith unto him,"), sy("19:18", frm="Which?", to="Which?"), cp("19:18", frm="And Jesus said,", to="And Jesus said,"), sy("19:18", frm="Thou shalt not kill,"),
           sy("19:19")], JESUS),
        F([cp("19:20", to="saith unto him,"), sy("19:20", frm="All these")], RICH_YOUNG),
        F([cp("19:21", to="said unto him,"), sy("19:21", frm="If thou")]),
        D([cp("19:22")], lambda w, h: A.rich_away("ra1", w, h, 1903), "#4A2A5A"),
        D([cp("19:23", to="unto his disciples,"), sy("19:23", frm="Verily"), sy("19:24")], lambda w, h: A.needle("nd1", w, h, 1904), "#FFD89A"),
        F([cp("19:25", to="saying,"), sy("19:25", frm="Who then")], JOHN),
        F([cp("19:26", to="said to them,"), sy("19:26", frm="With men")], JESUS),
        F([cp("19:27", to="said unto him,"), sy("19:27", frm="Lo, we")], PETER),
        D([cp("19:28", to="said unto them,"), sy("19:28", frm="Verily"), sy("19:29"), sy("19:30")], lambda w, h: A.thrones("th1", w, h, 1905), "#12113A"),
        # Matthew 20
        D(S("20:1", 2), lambda w, h: A.vineyard("vy1", w, h, 2001), "#3A3A7A", head="The Laborers in the Vineyard", stamp=20),
        D(S("20:3", 5), lambda w, h: A.idle("id1", w, h, 2002), "#5AB0D8"),
        D(S("20:6", 7), lambda w, h: A.idle("id2", w, h, 2003, late=True), "#4A2A5A"),
        D(S("20:8", 10), lambda w, h: A.vineyard("vy2", w, h, 2004, tone="dusk", hire=False, pay=True), "#4A2A5A"),
        F(S("20:11", 12), PHARISEE, bg=RED),
        F(S("20:13", 16)),
        D([cp("20:17"), sy("20:18"), sy("20:19")], lambda w, h: A.to_jerusalem("tj2", w, h, 2005), "#4A2A5A",
          head="The Cup That I Am about to Drink"),
        D([cp("20:20"), cp("20:21", to="said unto her,"), sy("20:21", frm="What wouldest", to="What wouldest thou?"), cp("20:21", frm="She saith unto him,", to="She saith unto him,"),
           sy("20:21", frm="Command that")], lambda w, h: A.zebedee_mother("zm1", w, h, 2006), "#8FD0E2"),
        D([cp("20:22", to="answered and said,"), sy("20:22", frm="Ye know not", to="about to drink?"), cp("20:22", frm="They say unto him,", to="They say unto him,"),
           sy("20:22", frm="We are able."), cp("20:23", to="He saith unto them,"), sy("20:23", frm="My cup")], lambda w, h: A.the_cup("cu1", w, h, 2007), "#1A1630"),
        F([cp("20:24"), cp("20:25", to="and said,"), sy("20:25", frm="Ye know"), sy("20:26"), sy("20:27"), sy("20:28")], JESUS),
        D([cp("20:29"), cp("20:30", to="saying,"), sy("20:30", frm="Lord, have mercy"), cp("20:31", to="saying,"), sy("20:31", frm="Lord, have mercy")],
          lambda w, h: A.jericho("jr1", w, h, 2008), "#8FD0E2", head="Two Blind Men at Jericho"),
        D([cp("20:32", to="and said,"), sy("20:32", frm="What will"), cp("20:33", to="They say unto him,"), sy("20:33", frm="Lord, that"), cp("20:34")], lambda w, h: A.jericho("jr2", w, h, 2009, healed=True), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MAT-C07-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · HOSANNA TO THE SON OF DAVID")))
