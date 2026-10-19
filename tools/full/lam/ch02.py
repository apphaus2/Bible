"""Lamentations volume, Chapter 2 — His Compassions Fail Not (Lamentations 3–5), the last chapter of Lamentations. Every verse,
word for word from ref/asv, each verse its own song line. The third lament: I am the man that hath seen affliction — dark places,
the heavy chain, the ways walled up with hewn stone, the bear and the lion, the mark for the arrow; yet this I recall: his
compassions fail not, they are new every morning (the dawn over the broken city); let him sit alone and keep silence; let us lift
up our heart with our hands; the cloud that no prayer can pass through; chased like a bird; out of the lowest dungeon (the pit
and its stone, no one drawn). The fourth: how is the gold become dim!; the sons of Zion as earthen pitchers; the famine and the
slain (4:4–10) words over empty streets and a cold hearth; the wanderers; the pursuers swifter than eagles; the cup to Edom. The
fifth: remember, O Jehovah; water bought for money; the elders ceased from the gate; the crown is fallen from our head; the foxes
walk upon Mount Zion; thy throne is from generation to generation; turn thou us unto thee, O Jehovah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from lam import G, art as K
from lam.common import pack, L, ZION, ZION_PLEA, MOURNER, MOURNER_HOPE, ELDER, GOLDEN, COLD, RED
from lam import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
M, MH, E, Z, ZP = (MOURNER, COLD), (MOURNER_HOPE, GOLDEN), (ELDER, COLD), (ZION, COLD), (ZION_PLEA, GOLDEN)
DAWN = "#2A2A6A"


@P("LAM-C02-00-Title", "Chapter 2 · His Compassions Fail Not", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.new_morning(760, 780, 201)}</g><rect x="0" y="0" width="760" height="302" fill="#2A2A6A"></rect>')
    return chapter_title(2, "第二話", "His Compassions Fail Not", "Lamentations 3 – 5", svg, DAWN, v("3:23"), "Lamentations · Volume Twenty-Five")


SEGS = [L(3, 1, 6, d=("#0E0C10", lambda w, h: K.dark_places(w, h, 202)), head="I Am the Man That Hath Seen Affliction", stamp=3),
        L(3, 7, 9, d=("#5A5A6A", lambda w, h: K.hewn_wall(w, h, 203))),
        L(3, 10, 11, d=("#3A3A2A", lambda w, h: K.bear_lion(w, h, 204)), k=0.4),
        L(3, 12, 13, d=("#5A4A4A", lambda w, h: K.mark_arrow(w, h, 205)), k=0.36),
        L(3, 14, 18, t=M),
        L(3, 19, 21, t=MH),
        L(3, 22, 24, d=(DAWN, lambda w, h: K.new_morning(w, h, 206)), head="His Compassions Fail Not"),
        L(3, 25, 27, t=MH),
        L(3, 28, 30, d=("#3A3A6A", lambda w, h: K.sit_alone("sa2", w, h, 207))),
        L(3, 31, 33, t=MH),
        L(3, 34, 36, d=("#1E1A1E", lambda w, h: K.prisoners(w, h, 208))),
        L(3, 37, 39, t=M),
        L(3, 40, 42, d=("#2A2A5A", lambda w, h: K.lift_hands("lh2", w, h, 209)), head="Let Us Search and Try Our Ways"),
        L(3, 43, 45, d=("#1A1A24", lambda w, h: K.thick_cloud(w, h, 210))),
        L(3, 46, 48, t=M),
        L(3, 49, 51, d=("#14122A", lambda w, h: K.tears(w, h, 211))),
        L(3, 52, d=("#8A8AA0", lambda w, h: K.bird_chased(w, h, 212)), k=0.3),
        L(3, 53, 55, d=("#2A2A3A", lambda w, h: K.pit_stone(w, h, 213)), head="Out of the Lowest Dungeon"),
        L(3, 56, 58, t=MH),
        L(3, 59, 63, t=M),
        L(3, 64, 66, d=("#2A2A3A", lambda w, h: K.cursed_day(w, h, 214))),
        L(4, 1, d=("#3A2A4A", lambda w, h: K.dim_gold(w, h, 215)), k=0.3, head="How Is the Gold Become Dim!", stamp=4),
        L(4, 2, d=("#3A2A22", lambda w, h: K.pitchers_row(w, h, 216)), k=0.3),
        L(4, 3, d=("#E8A060", lambda w, h: K.ostriches(w, h, 217)), k=0.3),
        L(4, 4, 5, d=("#3A2A4A", lambda w, h: K.empty_streets(w, h, 218))),
        L(4, 6, d=("#2A2A3A", lambda w, h: K.cursed_day(w, h, 219)), k=0.3),
        L(4, 7, 8, t=E),
        L(4, 9, 10, d=("#2A2420", lambda w, h: K.cold_hearth(w, h, 220))),
        L(4, 11, 12, d=("#2A0A0A", lambda w, h: K.burning_city(w, h, 221)), head="He Hath Kindled a Fire in Zion"),
        L(4, 13, 15, d=("#5A4A5A", lambda w, h: K.wanderers("wa2", w, h, 222))),
        L(4, 16, 17, t=E),
        L(4, 18, 19, d=("#5A6A8A", lambda w, h: K.eagle(w, h, 223))),
        L(4, 20, d=("#E8A060", lambda w, h: K.empty_pit(w, h, 224)), k=0.3),
        L(4, 21, 22, d=("#2A0E14", lambda w, h: K.cup(w, h, 225))),
        L(5, 1, 3, t=E, head="Remember, O Jehovah", stamp=5),
        L(5, 4, 5, d=("#8A7A6A", lambda w, h: K.water_money(w, h, 226)), k=0.36),
        L(5, 6, 8, d=("#1A1820", lambda w, h: K.yoke_iron(w, h, 227))),
        L(5, 9, 12, d=("#3A2A4A", lambda w, h: K.empty_streets(w, h, 228))),
        L(5, 13, d=("#5A5A6A", lambda w, h: K.mill_wood(w, h, 229)), k=0.3),
        L(5, 14, d=("#6A6A7A", lambda w, h: K.gate_empty(w, h, 230)), k=0.3),
        L(5, 15, 16, d=("#3A3040", lambda w, h: K.crown_fallen(w, h, 231)), k=0.4, head="The Crown Is Fallen from Our Head"),
        L(5, 17, 18, d=("#3A3A6A", lambda w, h: K.foxes_zion(w, h, 232)), k=0.4),
        L(5, 19, 20, d=("#0F0E2A", lambda w, h: K.throne_ever(w, h, 233)), k=0.4, head="Thou, O Jehovah, Abidest for Ever"),
        L(5, 21, 22, t=ZP)]
PG.extend(pack(SEGS, "LAM-C02-D", PG.next(), end=end_mark("END OF LAMENTATIONS · NEXT · EZEKIEL", "right: 10px; bottom: 34px", ch="完")))
