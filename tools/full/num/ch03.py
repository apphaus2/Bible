"""Numbers volume, Chapter 3 — Jehovah Bless Thee (Numbers 5–6). Every verse, word for word from ref/asv.
The unclean put out of the camp (a story page), restitution, the law of jealousy and the vow of a Nazirite as law cells
(exo.kit.law_pages, pictograms in num/art3.py), and Aaron's blessing as a closing splash."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import new, vref, page, chapter_title, end_mark, cap, god
from exo.kit import law_pages, set_book
from num import G, art as K, art3 as K3
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, W1, NIGHT, SKY
from genesis.ch03 import SAND
from genesis.ch06 import GOLDEN
from num import ch02 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SAY = "And Jehovah spake unto Moses, saying,"


@P("NUM-C03-00-Title", "Chapter 3 · Jehovah Bless Thee", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2458"></rect>' + f'<g transform="translate(0 300)">{K3.blessing("t3", 760, 780, 301)}</g>'
    return chapter_title(3, "第三話", "Jehovah Bless Thee", "Numbers 5 – 6", svg, "#2A2458", v("6:24"), "Numbers · Volume Four")


@P("NUM-C03-P01-Without", "Without the Camp")
def p01(n):
    t, h = rows(None, 420)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), mk.stamp(5, "right: 14px; top: 12px") + cap(v("5:1"), "left: 12px; top: 12px", size=11)
             + god(sp("5:2-3"), "left: 12px; top: 50px", size=21, maxw=600) + vref("NUM 5:1–3", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K3.without("c3b", W1, h[1], 312), cap(v("5:4"), "right: 12px; top: 12px", size=12, maxw=380) + vref("NUM 5:4", "right: 12px; bottom: 12px"))
    return page("Numbers 5:1–4 — Without the Camp", t, r1 + r2, n)


LAWS = [
    ("WHEN A MAN OR WOMAN SHALL COMMIT ANY SIN", "5:5-6", K3.pg_trespass, SAY, "If a Man Trespass"),
    ("RESTITUTION · THE FIFTH PART", "5:7", K3.pg_restitution, "", None),
    ("NO KINSMAN", "5:8", K3.pg_no_kinsman, "", None),
    ("THE PRIEST'S", "5:9-10", K3.pg_hallowed, "", None),
    ("IF ANY MAN'S WIFE GO ASIDE", "5:11-13", K3.pg_hid, SAY, "The Law of Jealousy"),
    ("THE SPIRIT OF JEALOUSY", "5:14", K3.pg_jealous, "", None),
    ("A MEAL-OFFERING OF JEALOUSY", "5:15", K3.pg_barley, "", None),
    ("BEFORE JEHOVAH", "5:16-17", K3.pg_holy_water, "", None),
    ("THE WATER OF BITTERNESS", "5:18", K3.pg_bitter, "", None),
    ("IF NO MAN HAVE LAIN WITH THEE", "5:19", K3.pg_swear, "", None),
    ("THE OATH OF CURSING", "5:20-22", K3.pg_amen, "", None),
    ("IN A BOOK", "5:23-24", K3.pg_blot, "", None),
    ("THE MEMORIAL", "5:25-26", K3.pg_handful, "", None),
    ("IF SHE BE DEFILED", "5:27", K3.pg_defiled, "", None),
    ("IF SHE BE CLEAN", "5:28", K3.pg_free, "", None),
    ("THE LAW OF JEALOUSY", "5:29-31", K3.pg_law_jealousy, "", None),
    ("THE VOW OF A NAZIRITE", "6:1-2", K3.pg_vow, SAY, "The Vow of a Nazirite"),
    ("NO WINE NOR STRONG DRINK", "6:3", K3.pg_no_wine, "", None),
    ("THE GRAPE-VINE", "6:4", K3.pg_kernels, "", None),
    ("NO RAZOR", "6:5", K3.pg_no_razor, "", None),
    ("NO DEAD BODY", "6:6-7", K3.pg_kin, "", None),
    ("HOLY UNTO JEHOVAH", "6:8", K3.pg_holy_naz, "", None),
    ("IF ANY MAN DIE SUDDENLY", "6:9", K3.pg_sudden, "", "If His Separation Be Defiled"),
    ("THE EIGHTH DAY", "6:10-11", K3.pg_doves8, "", None),
    ("THE FORMER DAYS VOID", "6:12", K3.pg_void, "", None),
    ("WHEN THE DAYS ARE FULFILLED", "6:13", K3.pg_fulfilled, "", "When the Days Are Fulfilled"),
    ("HIS OBLATION", "6:14-15", K3.pg_oblation, "", None),
    ("THE PRIEST SHALL PRESENT THEM", "6:16-17", K3.pg_present, "", None),
    ("THE HEAD OF HIS SEPARATION", "6:18", K3.pg_hair_fire, "", None),
    ("THE WAVE-OFFERING", "6:19-20", K3.pg_wave_naz, "", None),
    ("THE LAW OF THE NAZIRITE", "6:21", K3.pg_law_naz, "", None),
]
PG.extend(law_pages(LAWS, "NUM-C03-L", PG.next(), "If a Man Trespass", title_book="Numbers", carry=True))


@P("NUM-C03-P02-Bless", "On This Wise Ye Shall Bless")
def p02(n):
    t, h = rows(330, None)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), cap(v("6:22"), "left: 12px; top: 12px", size=11)
             + god(v("6:23"), "left: 12px; top: 50px", size=15, maxw=640)
             + god(v("6:24") + "<br>" + v("6:25") + "<br>" + v("6:26"), "left: 12px; top: 140px", size=24, maxw=680) + vref("NUM 6:22–26", "right: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #2A2458 0%, #5B2470 45%, #FFC14D 100%)", W1, h[1], K3.blessing("c3z", W1, h[1], 399),
             god(v("6:27"), "left: 12px; top: 12px", size=17, maxw=380) + vref("NUM 6:27", "right: 12px; top: 12px")
             + end_mark("NEXT · THE OFFERINGS OF THE PRINCES", "right: 10px; bottom: 10px"))
    return page("Numbers 6:22–27 — On This Wise Ye Shall Bless", t, r1 + r2, n)
