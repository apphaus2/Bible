"""Numbers volume, Chapter 9 — The Water for Impurity (Numbers 18–19). Every verse, word for word from ref/eng-asv.
All law cells (exo.kit.law_pages, pictograms in num/art9.py): the charge of the priests and the Levites, the priests'
portions and the covenant of salt, the tithe and the tithe of the tithe, and the red heifer and the water for impurity."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import chapter_title, end_mark
from exo.kit import law_pages, set_book
from num import G, art9 as K9
from num.pages import Pages
from lev.art import altar
from num import ch08 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SAY = "And Jehovah spake unto Moses, saying,"
SAY2 = "And Jehovah spake unto Moses and unto Aaron, saying,"


@P("NUM-C09-00-Title", "Chapter 9 · The Water for Impurity", title=True)
def title(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A2E"></rect>' + V.rays(380, 760, 40, 30, 1100, color="#FF8A3D", op=0.18)
           + f'<g transform="translate(0 500) scale(2.375)">{mk.defs("t9", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic") + K9.pg_cedar("t9")}</g>')
    return chapter_title(9, "第九話", "The Water for Impurity", "Numbers 18 – 19", svg, "#2A1A2E", v("18:20", frm="I am thy portion"), "Numbers · Volume Four")


LAWS = [
    ("THE INIQUITY OF THE SANCTUARY", "18:1", K9.pg_bear, "", "The Charge of the Priests and the Levites"),
    ("JOINED UNTO THEE", "18:2", K9.pg_joined, "", None),
    ("THAT THEY DIE NOT", "18:3-4", K9.pg_not_nigh, "", None),
    ("THE CHARGE OF THE ALTAR", "18:5", K9.pg_charge, "", None),
    ("A GIFT", "18:6", K9.pg_gift, "", None),
    ("WITHIN THE VEIL", "18:7", K9.pg_within_veil, "", None),
    ("MY HEAVE-OFFERINGS", "18:8", K9.pg_heave, "", "The Portion of the Priests"),
    ("THE MOST HOLY THINGS", "18:9", K9.pg_most_holy, "", None),
    ("EVERY MALE", "18:10", K9.pg_males, "", None),
    ("THE WAVE-OFFERINGS", "18:11", K9.pg_wave, "", None),
    ("THE BEST OF THE OIL", "18:12", K9.pg_best, "", None),
    ("THE FIRST-RIPE FRUITS", "18:13-14", K9.pg_first_ripe, "", None),
    ("THAT OPENETH THE WOMB", "18:15-16", K9.pg_firstborn, "", None),
    ("THE FIRSTLING", "18:17-18", K9.pg_firstling, "", None),
    ("A COVENANT OF SALT", "18:19", K9.pg_salt, "", None),
    ("I AM THY PORTION", "18:20", K9.pg_portion, "", "The Tithe"),
    ("ALL THE TITHE", "18:21", K9.pg_tithe, "", None),
    ("LEST THEY BEAR SIN", "18:22-23", K9.pg_no_nigh, "", None),
    ("NO INHERITANCE", "18:24", K9.pg_no_inherit, "", None),
    ("A TITHE OF THE TITHE", "18:25-26", K9.pg_tithe_tithe, SAY, None),
    ("AS THE THRESHING-FLOOR", "18:27-28", K9.pg_floor, "", None),
    ("THE BEST THEREOF", "18:29-30", K9.pg_best_heave, "", None),
    ("YOUR REWARD", "18:31-32", K9.pg_reward, "", None),
    ("A RED HEIFER", "19:1-2", K9.pg_heifer, SAY2, "The Red Heifer"),
    ("WITHOUT THE CAMP", "19:3", K9.pg_eleazar, "", None),
    ("SEVEN TIMES", "19:4", K9.pg_seven_toward, "", None),
    ("IN HIS SIGHT", "19:5", K9.pg_burn, "", None),
    ("CEDAR · HYSSOP · SCARLET", "19:6", K9.pg_cedar, "", None),
    ("UNTIL THE EVEN", "19:7-8", K9.pg_wash_even, "", None),
    ("THE ASHES OF THE HEIFER", "19:9", K9.pg_ashes, "", None),
    ("A STATUTE FOR EVER", "19:10", K9.pg_gatherer, "", None),
    ("THE DEAD BODY OF ANY MAN", "19:11-12", K9.pg_touch_dead, "", "He That Toucheth the Dead"),
    ("HE DEFILETH THE TABERNACLE", "19:13", K9.pg_defileth, "", None),
    ("WHEN A MAN DIETH IN A TENT", "19:14-15", K9.pg_tent_dead, "", None),
    ("IN THE OPEN FIELD", "19:16", K9.pg_field, "", None),
    ("THE ASHES AND RUNNING WATER", "19:17", K9.pg_running, "", "The Water for Impurity"),
    ("A CLEAN PERSON SHALL TAKE HYSSOP", "19:18", K9.pg_sprinkle, "", None),
    ("ON THE THIRD DAY AND ON THE SEVENTH", "19:19", K9.pg_third_seventh, "", None),
    ("THAT SOUL SHALL BE CUT OFF", "19:20", K9.pg_not_purify, "", None),
    ("A PERPETUAL STATUTE", "19:21-22", K9.pg_toucheth, "", None),
]
PG.extend(law_pages(LAWS, "NUM-C09-L", PG.next(), "The Charge of the Priests and the Levites", title_book="Numbers", carry=True,
                    end=end_mark("NEXT · MERIBAH", "right: 10px; top: 10px")))
