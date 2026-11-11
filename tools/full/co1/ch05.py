"""1 Corinthians volume, Chapter 5 — O Death, Where Is Thy Victory? (1 Corinthians 15–16). Every verse, word for word from
ref/eng-asv. 1 Corinthians 15: the gospel delivered (15:1–2); died, buried, raised — the three crosses far off, the sealed
tomb, the stone rolled away (15:3–4); the witnesses as greeting cells with their faces — Cephas, the twelve, the five hundred,
James, all the apostles, and Paul last of all (15:5–8); the sealed tomb at night (15:12–14); the tombs at dusk (15:18); the
firstfruits (15:20); the throne and the footstool, no figure (15:25); Psalm 8 in a song box (15:27); the theatre at Ephesus
empty, "fought with beasts" words only, Isaiah 22:13 in a song box (15:32); the grain of wheat (15:36–38); four fleshes
(15:39); the glory of sun, moon and stars (15:41); sown and raised (15:42–44); the earthy man and Jesus risen in white light,
Genesis 2:7 in a song box (15:45–47); the last trump over the opened tombs (15:52); the empty tomb and the folded linen, Isaiah
25:8 and Hosea 13:14 in song boxes (15:54–55); thanks be to God over the burst of light (15:57). 1 Corinthians 16: the
collection laid by on the first day of the week (16:2); the road through Macedonia (16:5–9); Timothy setting out and Apollos
at the quay (16:10–12); the greetings — Stephanas, Fortunatus and Achaicus, Aquila and Prisca, all the brethren (16:15–20);
Paul's own hand at the table (16:21–22); the grace (16:23–24)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co1 import G, art5 as A, ch04 as _prev
from co1.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, gd, sy, wq, qw, v, title, fin, greetings, face_portrait, PAUL, PAUL_LAMP,
                        PAUL_STERN, PAUL_JOY, PAUL_GRIEF, GOLD_BG, LAMP_BG, STERN_BG, JOY_BG, GRIEF_BG, CEPHAS, JOHN, ANDREW, JAMES_LORD, MATTHEW, THOMAS,
                        STEPHANAS, FORTUNATUS, ACHAICUS, AQUILA, PRISCILLA)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1CO-C05-00-Title", "Chapter 5 · O Death, Where Is Thy Victory?", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A6A"></rect><g transform="translate(0 300)">{A.last_trump(760, 780, 1501)}</g>'
    return title(5, "O Death, Where Is Thy Victory?", "1 Corinthians 15–16", svg, "#2A2A6A", v("15:55", to="where is thy victory?"))


def st(p, seed, **k): return lambda w, h: A.study_co1(p, w, h, seed, **k)

# 1 Corinthians 15:1–4
SEGS = [
    D(lp("15:1-2"), st("st15", 1501), "#3A2418", head="The Gospel Which I Preached", sky=15, art_h=260),
    D(lp("15:3-4"), lambda w, h: A.died_buried_raised("db1", w, h, 1503), "#05050E", head="Died, Buried, Raised", art_h=260),
]
PG.extend(K.pack(SEGS, "1CO-C05-D", PG.next(), lone=1.5))

# 15:5–8: the witnesses, as greeting cells
WITNESSES = [
    ("CEPHAS", "15:5 · HE APPEARED", [lt("15:5", to="Cephas;")], face_portrait(CEPHAS)),
    ("THE TWELVE", "15:5", [lt("15:5", frm="then to the twelve")], face_portrait(JOHN, ANDREW)),
    ("ABOVE FIVE HUNDRED", "15:6 · BRETHREN AT ONCE", [lt("15:6")], A.crowd_portrait(5, 2)),
    ("JAMES", "15:7", [lt("15:7", to="James;")], face_portrait(JAMES_LORD)),
    ("ALL THE APOSTLES", "15:7", [lt("15:7", frm="then to all the apostles")], face_portrait(MATTHEW, THOMAS)),
    ("PAUL", "15:8 · LAST OF ALL", [lt("15:8")], face_portrait(PAUL)),
]
K.label()                                                         # the cells carry their own references
PG.extend(greetings(WITNESSES, "1CO-C05-W", PG.next(), "1 Corinthians", "1CO", head="He Appeared"))

SEGS = [
    F(lp("15:9-11"), PAUL_GRIEF, bg=GRIEF_BG, head="The Least of the Apostles"),
    D(lp("15:12-14"), lambda w, h: A.sealed_tomb("tb1", w, h, 1512), "#2A1A3A", head="If Christ Hath Not Been Raised", art_h=240),
    F(lp("15:15-17"), PAUL_STERN, bg=STERN_BG),
    D(lp("15:18-19"), lambda w, h: A.sleepers(w, h, 1518), "#3A2A4A", art_h=230),
    D(lp("15:20-22"), lambda w, h: A.firstfruits("ff1", w, h, 1520), "#2A2A5A", head="Christ the Firstfruits", art_h=240),
    D(lp("15:23-26"), lambda w, h: A.throne("th1", w, h, 1523), "#2A3A7A", head="The Last Enemy", art_h=230),
    F([lt("15:27", to="For,"), sg("15:27", frm="He put all things", to="under his feet."), lt("15:27", frm="But when he saith,"), lt("15:28")], PAUL_JOY, bg=JOY_BG),
    F(lp("15:29-31"), PAUL),
    D([lt("15:32", to="If the dead are not raised,"), sg("15:32", frm="let us eat and drink"), lt("15:33"), lt("15:34")],
      lambda w, h: A.empty_theatre("et1", w, h, 1532), "#8FD0E2", art_h=240),
    D(lp("15:35-38"), lambda w, h: A.grain("gw1", w, h, 1535), "#3A2418", head="How Are the Dead Raised?", art_h=250),
    D([lt("15:39")], lambda w, h: A.fleshes("fl1", w, h, 1539), "#C8B080", art_h=220),
    D(lp("15:40-41"), lambda w, h: A.glories(w, h, 1540), "#05051A", head="One Star Differeth from Another", art_h=230),
    D(lp("15:42-44"), lambda w, h: A.sown_raised(w, h, 1542), "#3A2418", art_h=230),
    D([lt("15:45", to="So also it is written,"), sg("15:45", frm="The first man Adam", to="a living soul."), lt("15:45", frm="The last Adam")] + lp("15:46-47"),
      lambda w, h: A.earthy_heavenly("eh1", w, h, 1545), "#2A3A7A", head="The Last Adam", art_h=240),
    F(lp("15:48-50"), PAUL_JOY, bg=JOY_BG),
    D(lp("15:51-52"), lambda w, h: A.last_trump(w, h, 1551), "#2A2A6A", head="We Shall All Be Changed", art_h=250),
    D([lt("15:53"), lt("15:54", to="the saying that is written,"), sg("15:54", frm="Death is swallowed up"), sg("15:55")],
      lambda w, h: A.empty_tomb("tm1", w, h, 1553), "#FFF4C2", head="O Death, Where Is Thy Victory?", art_h=250),
    glory(lp("15:56-58")),
    # 1 Corinthians 16
    D(lp("16:1-4"), lambda w, h: A.collection("co1", w, h, 1601), "#C8A878", head="The Collection for the Saints", sky=16, art_h=240),
    D(lp("16:5-9"), lambda w, h: A.journey_plan(w, h), "#0B1A2E", head="A Great Door and Effectual", art_h=260),
    D(lp("16:10-12"), lambda w, h: A.brethren_sent("bs2", w, h, 1610), "#8FD0E2", head="Timothy and Apollos", art_h=240),
    F(lp("16:13-14"), PAUL),
]
PG.extend(K.pack(SEGS, "1CO-C05-E", PG.next(), lone=1.5))

GREET = [
    ("STEPHANAS", "16:15–16 · THE FIRSTFRUITS OF ACHAIA", lp("16:15-16"), face_portrait(STEPHANAS)),
    ("FORTUNATUS · ACHAICUS", "16:17–18 · AND STEPHANAS", lp("16:17-18"), A.three_portrait(STEPHANAS, FORTUNATUS, ACHAICUS)),
    ("AQUILA AND PRISCA", "16:19 · THE CHURCHES OF ASIA", [lt("16:19")], face_portrait(AQUILA, PRISCILLA)),
    ("ALL THE BRETHREN", "16:20 · A HOLY KISS", [lt("16:20")], A.crowd_portrait(6, 4)),
]
K.label()
PG.extend(greetings(GREET, "1CO-C05-G", PG.next(), "1 Corinthians", "1CO", head="Salute"))

SEGS = [
    D(lp("16:21-22"), lambda w, h: A.own_hand("oh1", w, h, 1621), "#3A2418", head="With Mine Own Hand", art_h=380),
    glory(lp("16:23-24"), h=330),
]
PG.extend(K.pack(SEGS, "1CO-C05-F", PG.next(), end=fin("END OF 1 CORINTHIANS · NEXT · 2 CORINTHIANS")))
