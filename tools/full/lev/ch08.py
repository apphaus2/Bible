"""Leviticus volume, Chapter 8 — The Set Feasts (Leviticus 23–25). Every verse, word for word from ref/eng-asv.
The feasts (23), the lamp and the showbread (24:1–9) and the jubilee (25) as law cells; the blasphemer (24:10–23) as a story
page. The stoning (24:23) is caption-only over a heap of stones without the camp."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cap, god
from exo import art as A, art8 as B8
from exo.kit import law_pages, set_book, talk
from lev import G, art8 as K
from lev import ch07 as _prev
from genesis.ch02 import rows, W1, NIGHT
from genesis.ch03 import SAND
from genesis.ch07 import RED

v, sp = G.v, G.span
set_book(G)
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"
DUSK = "linear-gradient(180deg, #2A1A3E 0%, #6A2A4A 60%, #C8682E 100%)"


@P("LEV-C08-00-Title", "Chapter 8 · The Set Feasts")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2458"></rect>' + f'<g transform="translate(0 480) scale(2.375)">{K.pg_dwell("t8")}</g>'
    return chapter_title(8, "第八話", "The Set Feasts", "Leviticus 23 – 25", svg, "#2A2458", v("25:10", frm="proclaim liberty", to="inhabitants thereof:").rstrip(":"), "Leviticus · Volume Three")


FEASTS = [
    ("THE SET FEASTS OF JEHOVAH", "23:1-2", K.pg_proclaim, SAY, "The Set Feasts of Jehovah"),
    ("THE SABBATH", "23:3", K.pg_sabbath, "", None),
    ("THE PASSOVER", "23:4-5", K.pg_passover, "", None),
    ("UNLEAVENED BREAD", "23:6-8", K.pg_unleavened, "", None),
    ("THE SHEAF OF THE FIRST-FRUITS", "23:9-11", K.pg_sheaf, SAY, "The Sheaf of the First-fruits"),
    ("A HE-LAMB", "23:12-13", K.pg_he_lamb, "", None),
    ("UNTIL THIS SELFSAME DAY", "23:14", K.pg_no_bread, "", None),
    ("FIFTY DAYS", "23:15-16", K.pg_fifty, "", "Seven Sabbaths Complete"),
    ("TWO WAVE-LOAVES", "23:17", K.pg_loaves, "", None),
    ("SEVEN LAMBS", "23:18-19", K.pg_seven_lambs, "", None),
    ("HOLY TO JEHOVAH FOR THE PRIEST", "23:20-21", K.pg_wave_bread, "", None),
    ("THE CORNERS OF THY FIELD", "23:22", K.pg_corners, "", None),
    ("A MEMORIAL OF BLOWING OF TRUMPETS", "23:23-25", K.pg_trumpets, SAY, "The Seventh Month"),
    ("THE DAY OF ATONEMENT", "23:26-28", K.pg_atonement, SAY, None),
    ("AFFLICTED IN THAT SAME DAY", "23:29-31", K.pg_afflict, "", None),
    ("FROM EVEN UNTO EVEN", "23:32", K.pg_ninth, "", None),
    ("THE FEAST OF TABERNACLES", "23:33-36", K.pg_booths, SAY, "Ye Shall Dwell in Booths"),
    ("THESE ARE THE SET FEASTS", "23:37-38", K.pg_feasts_all, "", None),
    ("THE FRUITS OF THE LAND", "23:39-40", K.pg_branches, "", None),
    ("IN BOOTHS SEVEN DAYS", "23:41-43", K.pg_dwell, "", None),
    ("MOSES DECLARED", "23:44", K.pg_declared, "", None),
    ("PURE OLIVE OIL", "24:1-2", K.pg_oil, SAY, "The Lamp and the Showbread"),
    ("FROM EVENING TO MORNING", "24:3-4", K.pg_lamps, "", None),
    ("TWELVE CAKES", "24:5-6", K.pg_twelve, "", None),
    ("EVERY SABBATH DAY", "24:7-9", K.pg_frankincense, "", None),
]
PAGES += law_pages(FEASTS, "LEV-C08-L", START, "The Set Feasts")
NEXT = START + len(PAGES) - 1


@P("LEV-C08-S1-Blasphemer", f"{NEXT} · He Blasphemed the Name")
def blasphemer():
    t, h = rows(260, 250, None)
    r1 = new(SAND, W1, h[0], K.strife("k8a", W1, h[0], 811), cap(v("24:10"), "left: 12px; top: 12px", size=11, maxw=440) + vref("LEV 24:10", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.ward("k8b", W1, h[1], 812), cap(v("24:11") + " " + v("24:12"), "left: 12px; top: 12px", size=11, maxw=460) + vref("LEV 24:11–12", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], A.X_COSMIC(W1, h[2]), cap(v("24:13"), "left: 12px; top: 12px", size=11) + god(v("24:14") + " " + v("24:15") + " " + v("24:16"), "left: 12px; top: 48px", size=15, maxw=640) + vref("LEV 24:13–16", "right: 12px; bottom: 12px"))
    return page("Leviticus 24:10–16 — He Blasphemed the Name", t, r1 + r2 + r3, NEXT)

@P("LEV-C08-S2-Stoned", f"{START + len(PAGES) - 1} · Life for Life")
def stoned():
    t, h = rows(200, 260, None)
    n = START + [x[0] for x in PAGES].index("LEV-C08-S2-Stoned") - 1
    scales = lambda w, hh: f'<g transform="translate({w * 0.62:.1f} {hh * 0.08:.1f}) scale({hh / 110:.3f})">{K.pg_life("s2")[len(K.GND):]}</g>'
    r1 = new(NIGHT, W1, h[0], A.X_COSMIC(W1, h[0]) + scales(W1, h[0]), god(v("24:17") + " " + v("24:18"), "left: 12px; top: 12px", size=17, maxw=380) + vref("LEV 24:17–18", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], A.X_COSMIC(W1, h[1]), god(v("24:19") + " " + v("24:20") + " " + v("24:21") + " " + v("24:22"), "left: 12px; top: 12px", size=16, maxw=640) + vref("LEV 24:19–22", "right: 12px; bottom: 12px"))
    r3 = new(DUSK, W1, h[2], K.heap_without("k8c", W1, h[2], 821), cap(v("24:23"), "left: 12px; top: 12px", size=12, maxw=460) + vref("LEV 24:23", "right: 12px; bottom: 12px"))
    return page("Leviticus 24:17–23 — Life for Life", t, r1 + r2 + r3, n)

JUBILEE = [
    ("A SABBATH UNTO JEHOVAH", "25:1-4", K.pg_land_sabbath, "And Jehovah spake unto Moses in mount Sinai, saying,", "A Sabbath for the Land"),
    ("THAT WHICH GROWETH OF ITSELF", "25:5", K.pg_of_itself, "", None),
    ("FOOD FOR YOU", "25:6-7", K.pg_food_all, "", None),
    ("SEVEN TIMES SEVEN YEARS", "25:8", K.pg_49, "", "The Jubilee"),
    ("THE LOUD TRUMPET", "25:9-10", K.pg_jubilee_horn, "", None),
    ("A JUBILEE", "25:11-13", K.pg_jubilee, "", None),
    ("YE SHALL NOT WRONG ONE ANOTHER", "25:14-17", K.pg_price, "", None),
    ("IN SAFETY", "25:18-19", K.pg_safety, "", None),
    ("WHAT SHALL WE EAT?", "25:20-22", K.pg_sixth, "", None),
    ("THE LAND IS MINE", "25:23-24", K.pg_mine, "", "The Redemption of the Land"),
    ("HIS KINSMAN THAT IS NEXT", "25:25-28", K.pg_kinsman, "", None),
    ("A HOUSE IN A WALLED CITY", "25:29-30", K.pg_walled, "", None),
    ("THE VILLAGES", "25:31", K.pg_villages, "", None),
    ("THE CITIES OF THE LEVITES", "25:32-34", K.pg_levites, "", None),
    ("THOU SHALT UPHOLD HIM", "25:35-38", K.pg_uphold, "", "If Thy Brother Be Waxed Poor"),
    ("AS A HIRED SERVANT", "25:39-41", K.pg_go_out, "", None),
    ("THEY ARE MY SERVANTS", "25:42-43", K.pg_my_servants, "", None),
    ("OF THE NATIONS", "25:44-46", K.pg_nations, "", None),
    ("ONE OF HIS BRETHREN MAY REDEEM HIM", "25:47-49", K.pg_redeem, "", None),
    ("RECKON WITH HIM", "25:50-53", K.pg_reckon, "", None),
    ("IN THE YEAR OF JUBILEE", "25:54-55", K.pg_go_out_jubilee, "", None),
]
PAGES += law_pages(JUBILEE, "LEV-C08-N", START + len(PAGES) - 1, "The Jubilee", end=end_mark("NEXT · BLESSING AND CURSE", "right: 10px; top: 10px"))
