"""Leviticus volume, Chapter 4 — The Plague of Leprosy (Leviticus 12–13). Every verse, word for word from ref/asv.
All law cells: the purifying after childbirth, and the priest's inspection of the skin, the head and the garment, drawn
as clinical sample diagrams (lev/art4.py)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from exo import art8 as B8
from exo.kit import law_pages, set_book
from lev import G, art4 as K
from lev import ch03 as _prev

v, sp = G.v, G.span
set_book(G)
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"
SAY2 = "And Jehovah spake unto Moses and unto Aaron, saying,"


@P("LEV-C04-00-Title", "Chapter 4 · The Plague of Leprosy")
def title():
    svg = (B8.bp(760, 1080) + f'<g transform="translate(380 560) scale(4) translate(-160 -50)">{K.lens(160, 50, 40, spot="white", hair="white", deep=True)}</g>'
           + K.label(380, 900, "THE PRIEST SHALL LOOK ON THE PLAGUE", B8.CY, 14))
    return chapter_title(4, "第四話", "The Plague of Leprosy", "Leviticus 12 – 13", svg, B8.INK, v("13:46", frm="he shall dwell alone;"), "Leviticus · Volume Three")


LAWS = [
    ("IF A WOMAN BEAR A MAN-CHILD", "12:1-2", K.pg_birth, SAY, "The Days of Her Purifying"),
    ("THE EIGHTH DAY", "12:3", K.pg_eighth, "", None),
    ("THREE AND THIRTY DAYS", "12:4", K.pg_33, "", None),
    ("A MAID-CHILD", "12:5", K.pg_maid, "", None),
    ("WHEN THE DAYS ARE FULFILLED", "12:6-7", K.pg_lamb_dove, "", None),
    ("IF HER MEANS SUFFICE NOT", "12:8", K.pg_poor, "", None),
    ("A RISING, A SCAB, A BRIGHT SPOT", "13:1-2", K.pg_brought, SAY2, "The Plague in the Skin"),
    ("THE HAIR TURNED WHITE", "13:3", K.pg_white_hair, "", None),
    ("SHUT UP SEVEN DAYS", "13:4", K.pg_shut7, "", None),
    ("AT A STAY", "13:5", K.pg_stay, "", None),
    ("THE PLAGUE BE DIM", "13:6", K.pg_dim, "", None),
    ("IF THE SCAB SPREAD", "13:7-8", K.pg_spread, "", None),
    ("A WHITE RISING", "13:9-11", K.pg_old, "", "An Old Leprosy"),
    ("COVERED ALL HIS FLESH", "13:12-13", K.pg_all_white, "", None),
    ("RAW FLESH", "13:14-15", K.pg_raw, "", None),
    ("CHANGED UNTO WHITE", "13:16-17", K.pg_raw_white, "", None),
    ("A BOIL", "13:18-20", K.pg_boil, "", "The Boil and the Burning"),
    ("NO WHITE HAIRS", "13:21-22", K.pg_shut7, "", None),
    ("THE SCAR OF THE BOIL", "13:23", K.pg_boil_scar, "", None),
    ("A BURNING BY FIRE", "13:24-25", K.pg_burn, "", None),
    ("NO WHITE HAIR IN THE BRIGHT SPOT", "13:26-27", K.pg_burn_white, "", None),
    ("THE SCAR OF THE BURNING", "13:28", K.pg_burn_scar, "", None),
    ("UPON THE HEAD OR THE BEARD", "13:29-30", K.pg_scall, "", "The Scall"),
    ("NO BLACK HAIR", "13:31-32", K.pg_scall_shut, "", None),
    ("HE SHALL BE SHAVEN", "13:33-34", K.pg_shaven, "", None),
    ("IF THE SCALL SPREAD", "13:35-36", K.pg_spread, "", None),
    ("BLACK HAIR GROWN UP", "13:37", K.pg_scall_healed, "", None),
    ("WHITE BRIGHT SPOTS", "13:38-39", K.pg_tetter, "", "Bald, Yet Clean"),
    ("BALD", "13:40-41", K.pg_bald, "", None),
    ("A REDDISH-WHITE PLAGUE", "13:42-44", K.pg_bald_plague, "", None),
    ("UNCLEAN, UNCLEAN", "13:45", K.pg_leper, "", "He Shall Dwell Alone"),
    ("WITHOUT THE CAMP", "13:46", K.pg_alone, "", None),
    ("WOOLLEN OR LINEN", "13:47-48", K.pg_garments, "", "The Plague in a Garment"),
    ("GREENISH OR REDDISH", "13:49-50", K.pg_greenish, "", None),
    ("A FRETTING LEPROSY", "13:51-52", K.pg_g_burn, "", None),
    ("WASH THE THING", "13:53-54", K.pg_g_wash, "", None),
    ("IF IT HAVE NOT CHANGED ITS COLOR", "13:55", K.pg_g_burn, "", None),
    ("DIM AFTER THE WASHING", "13:56-57", K.pg_g_rend, "", None),
    ("WASHED THE SECOND TIME", "13:58", K.pg_g_clean, "", None),
    ("THE LAW OF THE PLAGUE", "13:59", K.pg_g_law, "", None),
]
PAGES += law_pages(LAWS, "LEV-C04-L", START, "The Plague of Leprosy", end=end_mark("NEXT · THE CLEANSING", "right: 10px; top: 10px"))
