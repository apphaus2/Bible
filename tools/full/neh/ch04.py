"""Nehemiah volume, Chapter 4 — The Genealogy of the Return (Nehemiah 7). Every verse, word for word from ref/asv.
The doors set up and the porters, singers and Levites appointed; Hanani and Hananiah given charge — let not the gates of
Jerusalem be opened until the sun be hot; the city wide and large, but the people few; the book of the genealogy of them
that came up at the first: the leaders with Zerubbabel (a board of names), the men of the people of Israel by their
fathers' houses and by their cities (bar charts over roll cells, every verse in full), the priests, the Levites, the
singers and the porters (a tally board), the Nethinim and the children of Solomon's servants; those who could not show
their fathers' houses, till there stood up a priest with Urim and Thummim; the whole assembly and their beasts, the gifts
to the work; and all Israel in their cities when the seventh month was come."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from exo.art9 import urim
from neh import G, art as K
from neh.common import pack, cp, say, caps, drawn, face, NEHEMIAH, COLD, GOLDEN, RED, plan_pages
from neh import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD, SKY = "#0B1A2E", "#1A1430", "#8FD0E2"
GOLD_C, CYAN_C, ROSE_C, LILAC = "#FFD23F", "#8FD0E2", "#FF8A6A", "#C8A0E8"
LEADERS = ["ZERUBBABEL", "JESHUA", "NEHEMIAH", "AZARIAH", "RAAMIAH", "NAHAMANI", "MORDECAI", "BILSHAN", "MISPERETH", "BIGVAI", "NEHUM", "BAANAH"]
PEOPLE_N = [("PAROSH", 2172), ("SHEPHATIAH", 372), ("ARAH", 652), ("PAHATH-MOAB", 2818), ("ELAM", 1254), ("ZATTU", 845), ("ZACCAI", 760), ("BINNUI", 648),
            ("BEBAI", 628), ("AZGAD", 2322), ("ADONIKAM", 667), ("BIGVAI", 2067), ("ADIN", 655), ("ATER", 98), ("HASHUM", 328), ("BEZAI", 324), ("HARIPH", 112), ("GIBEON", 95)]
CITIES_N = [("BETH-LEHEM, NETOPHAH", 188), ("ANATHOTH", 128), ("BETH-AZMAVETH", 42), ("KIRIATH-JEARIM …", 743), ("RAMAH AND GEBA", 621), ("MICHMAS", 122),
            ("BETH-EL AND AI", 123), ("THE OTHER NEBO", 52), ("THE OTHER ELAM", 1254), ("HARIM", 320), ("JERICHO", 345), ("LOD, HADID, ONO", 721), ("SENAAH", 3930)]


@P("NEH-C04-00-Title", "Chapter 4 · The Genealogy of the Return", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.genealogy_book(760, 640, 401)}</g><rect x="0" y="0" width="760" height="332" fill="#2A1A2A"></rect>'
                '<rect x="0" y="968" width="760" height="120" fill="#2A1A2A"></rect>')
    return chapter_title(4, "第四話", "The Genealogy of the Return", "Nehemiah 7", svg, "#2A1A2A", v("7:5", frm="And I found the book"), "Nehemiah · Volume Sixteen")


SEGS = [drawn([caps("7:1-2")], "NEH 7:1–2", below(lambda w, h: K.wall_done("wd4", w, h, 402), 0.3), "#FFC890", head="The Doors Set Up", stamp=7),
        face([cp("7:3", to="And I said unto them,"), say("7:3", frm="Let not the gates")], "NEH 7:3", NEHEMIAH),
        drawn([caps("7:4")], "NEH 7:4", below(lambda w, h: K.empty_city(w, h, 403), 0.16), SKY),
        drawn([caps("7:5")], "NEH 7:5", below(lambda w, h: K.genealogy_book(w, h, 404), 0.3), "#2A1A2A", head="The Book of the Genealogy"),
        drawn([caps("7:6-7")], "NEH 7:6–7", below(lambda w, h: K.names_board(w, h, LEADERS, "WHO CAME WITH ZERUBBABEL"), 0.4), BOARD)]
PG.extend(pack(SEGS, "NEH-C04-D", PG.next()))
ROLL = [("The Men of the People", lambda w, h: K.bars(w, h, PEOPLE_N, "THE CHILDREN OF … · NEHEMIAH 7:8–25"), 330,
         [("By Their Fathers' Houses", "7:8-16", GOLD_C), ("By Their Fathers' Houses", "7:17-25", CYAN_C)]),
        ("The Men of the Cities", lambda w, h: K.bars(w, h, CITIES_N, "THE MEN OF … · NEHEMIAH 7:26–38", hi=("SENAAH",)), 330,
         [("By Their Cities", "7:26-33", GOLD_C), ("By Their Cities", "7:34-38", CYAN_C)]),
        ("The Priests and the Levites", lambda w, h: K.tally_grid(w, h, [("JEDAIAH", "973", GOLD_C), ("IMMER", "1,052", GOLD_C), ("PASHHUR", "1,247", GOLD_C), ("HARIM", "1,017", GOLD_C),
                                                                          ("THE LEVITES", "74", CYAN_C), ("THE SINGERS", "148", ROSE_C), ("THE PORTERS", "138", LILAC)], 4,
                                                                         "THE PRIESTS · THE LEVITES · THE SINGERS · THE PORTERS"), 330,
         [("The Priests", "7:39-42", GOLD_C), ("The Levites, the Singers, the Porters", "7:43-45", CYAN_C)]),
        ("The Nethinim", lambda w, h: K.altar_service("as4", w, h, 405), 280,
         [("The Nethinim", "7:46-56", GOLD_C), ("The Children of Solomon's Servants", "7:57-60", CYAN_C)])]
PG.extend(plan_pages(ROLL, "NEH-C04-E", PG.next(), tag="THE GENEALOGY · NEHEMIAH 7"))
SEGS2 = [drawn([caps("7:61-64")], "NEH 7:61–64", below(lambda w, h: K.genealogy_book(w, h, 406, gaps=True), 0.4), "#2A1A2A", head="Their Register Was Not Found"),
         drawn([caps("7:65")], "NEH 7:65", below(lambda w, h: urim(w, h), 0.16), MAP),
         drawn([caps("7:66-69")], "NEH 7:66–69", below(lambda w, h: K.tally_grid(w, h, [("THE WHOLE ASSEMBLY", "42,360", GOLD_C), ("SERVANTS", "7,337", CYAN_C), ("SINGING MEN AND WOMEN", "245", ROSE_C),
                                                                                       ("HORSES", "736", LILAC), ("MULES", "245", LILAC), ("CAMELS", "435", LILAC), ("ASSES", "6,720", LILAC)], 4), 0.46),
               BOARD, head="The Whole Assembly Together"),
         drawn([caps("7:70-72")], "NEH 7:70–72", below(lambda w, h: K.tally_grid(w, h, [("THE GOVERNOR · GOLD", "1,000 DARICS", GOLD_C), ("BASINS", "50", GOLD_C), ("GARMENTS", "530", GOLD_C),
                                                                                       ("THE HEADS · GOLD", "20,000 DARICS", CYAN_C), ("THE HEADS · SILVER", "2,200 POUNDS", CYAN_C),
                                                                                       ("THE PEOPLE · GOLD", "20,000 DARICS", ROSE_C), ("THE PEOPLE · SILVER", "2,000 POUNDS", ROSE_C), ("GARMENTS", "67", ROSE_C)], 4,
                                                                                      "GIVEN UNTO THE WORK"), 0.46), BOARD),
         drawn([caps("7:73")], "NEH 7:73", below(lambda w, h: K.villages("vl4", w, h, 407), 0.24), "#FFC890")]
PG.extend(pack(SEGS2, "NEH-C04-F", PG.next(), end=end_mark("NEXT · THE BOOK OF THE LAW", "right: 10px; bottom: 34px")))
