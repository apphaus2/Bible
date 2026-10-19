"""Jeremiah volume, Chapter 8 — The Cup of the Wine of Wrath (Jeremiah 23–25). Every verse, word for word from ref/asv.
Woe unto the shepherds that scatter the sheep; the remnant gathered again to their folds; a righteous Branch unto David —
Jehovah our righteousness; concerning the prophets — my heart within me is broken; the whirling tempest; I have dreamed, I have
dreamed; is not my word like fire, and like a hammer that breaketh the rock?; the burden of Jehovah; the two baskets of figs
before the temple; three and twenty years; the millstones and the lamp; seventy years; then the cup of the wine of wrath, and
all the nations made to drink it, as a map lit kingdom by kingdom; the shepherds wail; the lion hath left his covert."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art8 as K, art5 as K5, art7 as K7
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, GOLDEN, COLD, RED, NIGHT
from jer import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W1, G1, S1, C1, A1 = (jer(1, "word"), GOLDEN), (jer(1, "grief"), COLD), (jer(1, "stern"), RED), (jer(1, "calm"), GOLDEN), (jer(1, "afraid"), COLD)
MAP = "#0B1A2E"
WRATH = "#2A0E14"
def nations(places, hi, box=(29.5, 49.6, 25.6, 37.6)):
    return (MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM",) + places, hi=hi, box=box))


@P("JER-C08-00-Title", "Chapter 8 · The Cup of the Wine of Wrath", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.cup(760, 780, 801)}</g><rect x="0" y="0" width="760" height="302" fill="#2A0E14"></rect>')
    return chapter_title(8, "第八話", "The Cup of the Wine of Wrath", "Jeremiah 23 – 25", svg, WRATH, v("25:15", frm="Take this cup", to="at my hand,"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("23:1-2", t=S1, head="Woe unto the Shepherds", stamp=23),
        O("23:3-4", a=("#8FB0C8", lambda w, h: K.flock(w, h, 802, fold=True))),
        O("23:5-6", a=("#3A3A7A", lambda w, h: K.branch(w, h, 803)), head="A Righteous Branch"),
        O("23:7-8", a=(MAP, lambda w, h: K.return_map(w, h)), k=0.42),
        O("23:9-10", kind="say", t=G1, head="Concerning the Prophets"),
        O("23:11-12", t=S1),
        O("23:13-14", a=("#2A2A3A", lambda w, h: K7.cursed_day(w, h, 804))),
        O("23:15", a=("#3A3A3A", lambda w, h: K.wormwood(w, h, 805)), k=0.3),
        O("23:16-17", t=W1, head="Hearken Not unto the Prophets"),
        O("23:18-20", a=("#1A1A2A", lambda w, h: K.tempest(w, h, 806))),
        O("23:21-24", t=S1),
        O("23:25-27", a=("#1A1430", lambda w, h: K.dreamer(w, h, 807)), head="I Have Dreamed, I Have Dreamed"),
        O("23:28-29", a=("#1A1012", lambda w, h: K.hammer_rock(w, h, 808)), k=0.36),
        O("23:30-32", t=S1),
        O("23:33-34", t=W1, head="The Burden of Jehovah"),
        O("23:35-37", t=S1),
        O("23:38-40", a=("#3A2A4A", lambda w, h: K.empty_city(w, h, 809, dusk=True))),
        O("24:1-2", kind="cap", a=("#8FB0C8", lambda w, h: K.figs(w, h, 810)), k=0.34, head="Two Baskets of Figs", stamp=24),
        S([cp("24:3", to="Then said Jehovah unto me,"), gd("24:3", frm="What seest", to="Jeremiah?"), cp("24:3", frm="And I said,", to="And I said,"), say("24:3", frm="Figs;"),
           cp("24:4"), gd("24:5")], "24:3-5", t=W1),
        O("24:6-7", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "BABYLON", "CHALDEA"), hi=("BABYLON",), arrows=[("BABYLON", "JERUSALEM")], lit="#FFD23F")), k=0.44),
        O("24:8", a=("#8FB0C8", lambda w, h: K.figs(w, h, 811, bad=True)), k=0.3),
        O("24:9-10", t=S1),
        O("25:1-2", kind="cap", a=("#8FB0C8", lambda w, h: K.temple_gate("tg8", w, h, 812)), k=0.3, head="Three and Twenty Years", stamp=25),
        O("25:3-4", kind="say", t=W1),
        O("25:5-7", kind="say", t=S1),
        O("25:8-9", a=("#4A3A4A", lambda w, h: K.north_host("nh8", w, h, 813))),
        O("25:10-11", a=("#2A2220", lambda w, h: K.millstones_lamp(w, h, 814))),
        O("25:12", a=("#1A1430", lambda w, h: K.seventy(w, h, 815)), k=0.36, head="Seventy Years"),
        O("25:13-14", t=S1),
        S([*cut("25:15", "unto me:"), gd("25:16")], "25:15-16", a=(WRATH, lambda w, h: K.cup(w, h, 816)), k=0.3, head="The Cup of the Wine of Wrath"),
        O("25:17-20", kind="cap", a=("#1A1430", lambda w, h: K.lot_grid(w, h * 0.86, ["JERUSALEM", "CITIES OF JUDAH", "PHARAOH", "MINGLED PEOPLE", "UZ", "PHILISTINES", "ASHKELON",
                                                                                "GAZA", "EKRON", "ASHDOD"], cols=5, color="#FF8A6A")), k=0.46),
        O("25:21-24", kind="cap", a=("#1A1430", lambda w, h: K.lot_grid(w, h * 0.86, ["EDOM", "MOAB", "AMMON", "TYRE", "SIDON", "THE ISLE", "DEDAN", "TEMA", "BUZ", "ARABIA"],
                                                                                cols=5, color="#FF8A6A")), k=0.42),
        O("25:25-26", kind="cap", a=nations(("ELAM", "THE MEDES", "ASSYRIA", "BABYLON"), ("ELAM", "THE MEDES", "ASSYRIA", "BABYLON"), box=(33.0, 50.6, 27.0, 38.6)), k=0.4),
        O("25:27", a=(WRATH, lambda w, h: K.cup(w, h, 817)), k=0.3),
        O("25:28-29", t=S1),
        O("25:30-31", a=("#2A0A1A", lambda w, h: K.grape_tread(w, h, 818)), head="Jehovah Will Roar from on High"),
        O("25:32-33", a=("#1A1A2A", lambda w, h: K.tempest(w, h, 819))),
        O("25:34-36", a=("#3A3A4A", lambda w, h: K.shepherds_wail("sw8", w, h, 820)), head="Wail, Ye Shepherds"),
        O("25:37-38", a=("#C8703A", lambda w, h: K.lion_thicket(w, h, 821)), k=0.34)]
PG.extend(pack(SEGS, "JER-C08-D", PG.next(), end=end_mark("NEXT · THE YOKE", "right: 10px; bottom: 34px")))
