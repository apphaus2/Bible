"""Matthew volume, Chapter 2 — The Sermon on the Mount (Matthew 5–7). Every verse, word for word from ref/eng-asv.
Jesus seated on the mountain, the disciples on the grass before him and the multitudes coming up the hill; the beatitudes
beside his face and over the listening hillside; then each saying drawn as its own small scene, his words in speech boxes
over it, between panels of his face: the salt trodden under foot; the city on a hill and the lamp on the stand; the scroll
of the law, every jot lit; the gift left before the altar; the prison door and the last farthing; the heavens a blaze of
light (no form in it), the earth and Jerusalem; the second mile beside the milestone; the sun and the rain on one field;
the trumpet in the street and the shut door of the inner chamber; the prayer in song boxes over the field of bread at
sunrise; moth and rust and the broken wall; the lamp of the body; the birds of the heaven and the lilies of the field;
pearls in the mire; the opened door; a loaf and a stone, a fish and a serpent; the two gates; the wolf among the sheep;
the trees and their fruits; the houses on the rock and on the sand. The words of 5:27–30 stand beside his face only."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art2 as A, ch01 as _prev
from mat.common import K, Pages, drawn, cp, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C02-00-Title", "Chapter 2 · The Sermon on the Mount", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.mount_teach("t2", 760, 780, 501)}</g>'
    return title(2, "The Sermon on the Mount", "Matthew 5 – 7", svg, "#2A3A5A", v("5:3"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **k)
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b, c=None):
    """His words, verses a–b of chapter c (or of the chapter in a), one speech box a verse."""
    ch, x = a.split(":"); y = int(b)
    return [sy(f"{ch}:{k}") for k in range(int(x), y + 1)]

SEGS = [D([cp("5:1"), cp("5:2")], lambda w, h: A.mount_teach("mt1", w, h, 502), "#8FD0E2", head="The Sermon on the Mount", stamp=5, h=440),
        F(S("5:3", 6), head="Blessed"),
        D(S("5:7", 10), lambda w, h: A.hillside("hs1", w, h, 503), "#8FD0E2"),
        F(S("5:11", 12), JESUS),
        D(S("5:13", 13), lambda w, h: A.salt("sl1", w, h, 504), "#C8D8E2", head="The Salt of the Earth"),
        D(S("5:14", 16), lambda w, h: A.city_light("cl1", w, h, 505), NIGHT, head="The Light of the World"),
        D(S("5:17", 18), lambda w, h: A.law_scroll("ls1", w, h, 506), "#1A1630", head="Not to Destroy, but to Fulfil"),
        F(S("5:19", 20)),
        F(S("5:21", 22), JESUS_STERN, bg=RED, head="But I Say unto You"),
        D(S("5:23", 24), lambda w, h: A.altar_gift("ag1", w, h, 507), "#E8D8B8"),
        D(S("5:25", 26), lambda w, h: A.prison_door("pd1", w, h, 508), "#5A5048"),
        F(S("5:27", 30), JESUS_STERN, bg=RED),
        F(S("5:31", 32)),
        D(S("5:33", 37), lambda w, h: A.oaths("oa1", w, h, 509), "#FFE680", head="Swear Not at All"),
        F(S("5:38", 40), JESUS),
        D(S("5:41", 42), lambda w, h: A.two_miles("tm1", w, h, 510), "#8FD0E2"),
        F(S("5:43", 44), head="Love Your Enemies"),
        D(S("5:45", 45), lambda w, h: A.sun_rain("sn1", w, h, 511), "#FFC890"),
        F(S("5:46", 48), JESUS),
        # Matthew 6
        F(S("6:1", 1), head="In Secret", stamp=6),
        D(S("6:2", 4), lambda w, h: A.trumpet_street("ts1", w, h, 601), "#8FD0E2"),
        D(S("6:5", 6), lambda w, h: A.inner_chamber("ic1", w, h, 602), "#6A5048"),
        F(S("6:7", 8), JESUS),
        D([sy("6:9", to="pray ye:"), sg("6:9", frm="Our Father"), sg("6:10"), sg("6:11"), sg("6:12"), sg("6:13")], lambda w, h: A.prayer_field("pf1", w, h, 603), "#3A3A7A",
          head="Our Father Who Art in Heaven"),
        F(S("6:14", 15)),
        F(S("6:16", 18), JESUS),
        D(S("6:19", 21), lambda w, h: A.treasures("tr1", w, h, 604), "#4A3A30", head="Treasures in Heaven"),
        D(S("6:22", 23), lambda w, h: A.eye_lamp("el1", w, h, 605), "#05050E"),
        F(S("6:24", 24), JESUS_STERN, bg=RED),
        F(S("6:25", 25), JESUS),
        D(S("6:26", 27), lambda w, h: A.birds_heaven("bh1", w, h, 606), "#5AB0D8"),
        D(S("6:28", 30), lambda w, h: A.lilies_field("lf1", w, h, 607), "#8FD0E2"),
        F(S("6:31", 34)),
        # Matthew 7
        F(S("7:1", 3), head="Judge Not", stamp=7),
        F(S("7:4", 5), JESUS_STERN, bg=RED),
        D(S("7:6", 6), lambda w, h: A.pearls("pr1", w, h, 701), "#A8A08A"),
        D(S("7:7", 8), lambda w, h: A.door_knock("dk1", w, h, 702), "#2A2050"),
        D(S("7:9", 10), lambda w, h: A.loaf_stone("lo1", w, h, 703), "#3A2A2A"),
        F(S("7:11", 12), JESUS),
        D(S("7:13", 14), lambda w, h: A.two_gates("tg1", w, h, 704), "#3A1A2A", head="The Narrow Gate"),
        D(S("7:15", 15), lambda w, h: A.wolves("wv1", w, h, 705), "#2A1A3A"),
        D(S("7:16", 20), lambda w, h: A.fruit_trees("ft1", w, h, 706), "#8FD0E2", head="By Their Fruits"),
        F(S("7:21", 23), JESUS_STERN, bg=RED),
        D(S("7:24", 25), lambda w, h: A.house_storm("hr1", w, h, 707), "#14141E", head="Upon the Rock"),
        D(S("7:26", 27), lambda w, h: A.house_storm("hr2", w, h, 708, rock=False), "#14141E"),
        D([cp("7:28"), cp("7:29")], lambda w, h: A.mount_teach("mt2", w, h, 709, astonished=True), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MAT-C02-D", PG.next(), end=nxt("NEXT · THE HARVEST IS PLENTEOUS")))
