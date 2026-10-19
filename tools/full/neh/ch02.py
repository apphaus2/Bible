"""Nehemiah volume, Chapter 2 — The Builders (Nehemiah 3–4). Every verse, word for word from ref/asv.
The builders of the wall, portion by portion, round from the sheep gate and back to it again: each run of verses over the
plan of the wall with its stretch and its gates lit (neh.art.wall_plan), with drawings of the priests building the sheep
gate, the fish gate's doors and bars, and Shallum with his daughters; then Sanballat's mockery — if a fox go up, he shall
break down their stone wall; Nehemiah's prayer; the adversaries conspiring on every side (a map); the people set behind the
wall with swords, spears and bows — remember the Lord, who is great and terrible; and the builders with one hand in the
work and with the other holding his weapon, the trumpet by Nehemiah, none putting off their clothes."""
import sys, pathlib, math
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from neh import G, art as K
from neh.common import (pack, cp, say, gd, says, caps, drawn, face, joined, NEHEMIAH, NEHEMIAH_PRAY, NEHEMIAH_STERN, SANBALLAT, TOBIAH, GESHEM,
                        JUDAH_MAN, PEOPLE, COLD, GOLDEN, RED, plan_pages)
from neh import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, SKY = "#0B1A2E", "#8FD0E2"


@P("NEH-C02-00-Title", "Chapter 2 · The Builders", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.gate_build("t2", 760, 600, 201)}</g><rect x="0" y="0" width="760" height="332" fill="#8FD0E2"></rect>'
                '<rect x="0" y="928" width="760" height="160" fill="#C8B88A"></rect>')
    return chapter_title(2, "第二話", "The Builders", "Nehemiah 3 – 4", svg, "#3A5A7A", v("4:6", frm="for the people had a mind to work."), "Nehemiah · Volume Sixteen")


def plan(*lit):
    return lambda w, h: K.wall_plan(w, h, lit=lit)

GOLD_C, CYAN_C, ROSE_C = "#FFD23F", "#8FD0E2", "#FF8A6A"
WALL = [("The Sheep Gate", lambda w, h: K.gate_build("gb2", w, h, 202, priests=True), 300,
         [("The Sheep Gate", "3:1-2", GOLD_C), ("The Fish Gate", "3:3-5", CYAN_C)]),
        ("The Old Gate", plan("SHEEP GATE", "TOWER OF HAMMEAH", "TOWER OF HANANEL", "FISH GATE", "OLD GATE", "GATE OF EPHRAIM", "BROAD WALL", "TOWER OF THE FURNACES"), 330,
         [("The Old Gate", "3:6-7", GOLD_C), ("Unto the Broad Wall", "3:8-11", CYAN_C)]),
        ("He and His Daughters", lambda w, h: K.daughters("dt2", w, h, 204), 290,
         [("Shallum and His Daughters", "3:12", ROSE_C), ("The Valley Gate", "3:13", GOLD_C), ("The Dung Gate", "3:14", CYAN_C)]),
        ("The Fountain Gate", plan("TOWER OF THE FURNACES", "VALLEY GATE", "DUNG GATE", "FOUNTAIN GATE", "POOL OF SHELAH", "SEPULCHRES OF DAVID", "THE ARMORY"), 330,
         [("The Fountain Gate", "3:15", GOLD_C), ("Unto the Sepulchres of David", "3:16-19", CYAN_C)]),
        ("Earnestly Repaired", lambda w, h: K.builders("bd2", w, h, 205, trumpet=False, top=0.66), 290,
         [("Earnestly Repaired", "3:20-21", GOLD_C), ("Unto the Turning of the Wall", "3:22-25", CYAN_C)]),
        ("The Water Gate", plan("HOUSE OF ELIASHIB", "WATER GATE", "TOWER THAT STANDETH OUT", "HORSE GATE", "EAST GATE", "GATE OF HAMMIPHKAD", "SHEEP GATE"), 330,
         [("Ophel and the Water Gate", "3:26-27", GOLD_C), ("The Horse Gate", "3:28-30", CYAN_C), ("Unto the Sheep Gate", "3:31-32", ROSE_C)])]
PG.extend(plan_pages(WALL, "NEH-C02-D", PG.next(), tag="THE BUILDERS OF THE WALL · NEHEMIAH 3", stamp=3))
SEGS2 = [face([caps("4:1"), cp("4:2", to="and said,"), say("4:2", frm="What are these")], "NEH 4:1–2", SANBALLAT, bg=RED, head="If a Fox Go Up", stamp=4),
         face([cp("4:3", to="and he said,"), say("4:3", frm="Even that which")], "NEH 4:3", TOBIAH, bg=RED),
         face([says("4:4-5")], "NEH 4:4–5", NEHEMIAH_PRAY, bg=COLD),
         drawn([caps("4:6")], "NEH 4:6", below(lambda w, h: K.builders("bd2b", w, h, 206, trumpet=False, top=0.64), 0.3), SKY, head="A Mind to Work"),
         drawn([caps("4:7-8")], "NEH 4:7–8", below(lambda w, h: K.foes_map(w, h), 0.3), MAP, head="They Conspired All of Them Together"),
         drawn([caps("4:9")], "NEH 4:9", below(lambda w, h: K.watch_night("wn2", w, h, 207), 0.3), "#0B0B2A"),
         face([cp("4:10", to="And Judah said,"), say("4:10", frm="The strength")], "NEH 4:10", JUDAH_MAN, bg=COLD),
         face([cp("4:11", to="And our adversaries said,"), say("4:11", frm="They shall not know")], "NEH 4:11", GESHEM, bg=RED),
         face([cp("4:12", to="ten times from all places,"), say("4:12", frm="Ye must return")], "NEH 4:12", PEOPLE, bg=COLD),
         drawn([caps("4:13")], "NEH 4:13", below(lambda w, h: K.families_armed("fa2", w, h, 208), 0.26), "#8A7A8A", head="Remember the Lord"),
         face([cp("4:14", to="and to the rest of the people,"), say("4:14", frm="Be not ye afraid")], "NEH 4:14", NEHEMIAH_STERN, bg=RED),
         drawn([caps("4:15")], "NEH 4:15", below(lambda w, h: K.builders("bd2c", w, h, 209, trumpet=False, top=0.62), 0.24), SKY),
         drawn([caps("4:16-18")], "NEH 4:16–18", below(lambda w, h: K.builders("bd2d", w, h, 210, top=0.62), 0.4), SKY, head="With the Other Held His Weapon"),
         face([cp("4:19", to="and to the rest of the people,"), joined("say", ("4:19", "The work is great"), "4:20")], "NEH 4:19–20", NEHEMIAH),
         drawn([caps("4:21")], "NEH 4:21", below(lambda w, h: K.builders("bd2e", w, h, 211, dusk=True, top=0.62), 0.32), "#5A3A6A"),
         face([cp("4:22", to="said I unto the people,"), say("4:22", frm="Let every one")], "NEH 4:22", NEHEMIAH),
         drawn([caps("4:23")], "NEH 4:23", below(lambda w, h: K.watch_night("wn2b", w, h, 212, water=True), 0.2), "#0B0B2A")]
PG.extend(pack(SEGS2, "NEH-C02-E", PG.next(), end=end_mark("NEXT · THE WORK FINISHED", "right: 10px; bottom: 34px")))
