"""2 Kings volume, Chapter 2 — The Pot of Oil (2 Kings 3–4). Every verse, word for word from ref/asv.
Jehoram and Mesha's rebellion; three kings in the wilderness of Edom without water; bring me a minstrel — make this valley
full of trenches; the water red as blood in the morning sun; Kir-hareseth (3:27 words over the wall and its smoke). Then the
widow's pot of oil and the borrowed vessels; the great woman of Shunem and the little chamber on the wall; thou shalt embrace
a son; my head, my head; the ride to Carmel — it is well; Gehazi's staff; the child sneezed seven times; death in the pot;
and twenty loaves of barley for a hundred men."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, ELISHA, ELISHA_STERN, JEHORAM, JEHOSHAPHAT, WIDOW, SHUNAMMITE, SHUNAMMITE_GRIEF, GEHAZI,
                        SONS_PROPHETS, MESSENGER, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"
CHAMBER = lambda seed: below(lambda w, h: K.upper_chamber("uc%d" % seed, w, h, seed), 0.4)


@P("2KI-C02-00-Title", "Chapter 2 · The Pot of Oil", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#C8A878"></rect><g transform="translate(0 340)">{K.oil_vessels("t2", 760, 740, 201)}</g>')
    return chapter_title(2, "第二話", "The Pot of Oil", "2 Kings 3 – 4", svg, "#8A6A3A", v("4:6", frm="And the oil stayed."), "2 Kings · Volume Twelve")


SEGS = [face([caps("3:1-3")], "2KGS 3:1–3", JEHORAM, head="Mesha King of Moab", stamp=3),
        drawn([caps("3:4-6"), cp("3:7", to="saying,"), say("3:7", frm="The king of Moab", to="against Moab to battle?"), cp("3:7", frm="And he said,", to="And he said,"), say("3:7", frm="I will go up:")],
              "2KGS 3:4–7", below(lambda w, h: K.three_kings("tk2", w, h, 202), 0.36), "#FFE6A0"),
        face([cp("3:8", to="And he said,"), say("3:8", frm="Which way", to="go up?"), cp("3:8", frm="And he answered,", to="And he answered,"), say("3:8", frm="The way of the wilderness"), caps("3:9"),
              cp("3:10", to="And the king of Israel said,"), say("3:10", frm="Alas!")], "2KGS 3:8–10", JEHORAM, bg=COLD),
        face([cp("3:11", to="But Jehoshaphat said,"), say("3:11", frm="Is there not", to="by him?"), cp("3:11", frm="And one of the king", to="answered and said,"), say("3:11", frm="Elisha the son"),
              cp("3:12", to="And Jehoshaphat said,"), say("3:12", frm="The word of Jehovah", to="is with him."), cp("3:12", frm="So the king of Israel")], "2KGS 3:11–12", JEHOSHAPHAT),
        face([cp("3:13", to="unto the king of Israel,"), say("3:13", frm="What have I", to="thy mother."), cp("3:13", frm="And the king of Israel said unto him,", to="said unto him,"), say("3:13", frm="Nay;"),
              cp("3:14", to="And Elisha said,"), say("3:14", frm="As Jehovah of hosts"), say("3:15", to="But now bring me a minstrel."), cp("3:15", frm="And it came to pass,")], "2KGS 3:13–15",
             ELISHA_STERN, bg=RED, head="Bring Me a Minstrel"),
        drawn([cp("3:16", to="And he said,"), say("3:16", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("3:16", frm="Make this valley"), say("3:17", to="For thus saith Jehovah,"),
               gd("3:17", frm="Ye shall not see"), gods("3:18-19")], "2KGS 3:16–19", below(lambda w, h: K.trenches("tr2", w, h, 203), 0.5), "#8FD0E2"),
        drawn([caps("3:20-22")], "2KGS 3:20–22", below(lambda w, h: K.trenches("tr2b", w, h, 204, red=True), 0.34), "#FFB04A", head="As Red as Blood"),
        drawn([cp("3:23", to="and they said,"), say("3:23", frm="This is blood;"), caps("3:24-25")], "2KGS 3:23–25", below(lambda w, h: K.ramah("rm2", w, h, 205), 0.4), "#8FD0E2"),
        drawn([caps("3:26-27")], "2KGS 3:26–27", lambda w, h: K.kir_wall(w, h, 206), "#3A1A1A"),
        face([cp("4:1", to="saying,"), say("4:1", frm="Thy servant my husband")], "2KGS 4:1", WIDOW, bg=COLD, head="A Pot of Oil", stamp=4),
        face([cp("4:2", to="said unto her,"), say("4:2", frm="What shall I do", to="in the house?"), cp("4:2", frm="And she said,", to="And she said,"), say("4:2", frm="Thy handmaid"),
              cp("4:3", to="Then he said,"), joined("say", ("4:3", "Go, borrow"), "4:4")], "2KGS 4:2–4", ELISHA),
        drawn([caps("4:5"), cp("4:6", to="unto her son,"), say("4:6", frm="Bring me", to="a vessel."), cp("4:6", frm="And he said unto her,", to="said unto her,"), say("4:6", frm="There is not", to="a vessel more."),
               cp("4:6", frm="And the oil stayed.")], "2KGS 4:5–6", below(lambda w, h: K.oil_vessels("ov2", w, h, 207), 0.32), "#C8A878"),
        face([cp("4:7", to="And he said,"), say("4:7", frm="Go, sell")], "2KGS 4:7", ELISHA),
        drawn([caps("4:8"), cp("4:9", to="unto her husband,"), joined("say", ("4:9", "Behold now,"), "4:10")], "2KGS 4:8–10", below(lambda w, h: K.shunem_house("sh2", w, h, 208), 0.4), "#8FD0E2",
              head="The Great Woman of Shunem"),
        face([caps("4:11"), cp("4:12", to="to Gehazi his servant,"), say("4:12", frm="Call this Shunammite.", to="Call this Shunammite."), cp("4:12", frm="And when he had called her,"),
              cp("4:13", to="And he said unto him,"), say("4:13", frm="Say now", to="captain of the host?"), cp("4:13", frm="And she answered,", to="And she answered,"), say("4:13", frm="I dwell")],
             "2KGS 4:11–13", ELISHA),
        face([cp("4:14", to="And he said,"), say("4:14", frm="What then", to="for her?"), cp("4:14", frm="And Gehazi answered,", to="And Gehazi answered,"), say("4:14", frm="Verily"),
              cp("4:15", to="And he said,"), say("4:15", frm="Call her.", to="Call her."), cp("4:15", frm="And when he had called her,")], "2KGS 4:14–15", GEHAZI),
        face([cp("4:16", to="And he said,"), say("4:16", frm="At this season,", to="embrace a son."), cp("4:16", frm="And she said,", to="And she said,"), say("4:16", frm="Nay, my lord,"), caps("4:17")],
             "2KGS 4:16–17", SHUNAMMITE, head="Thou Shalt Embrace a Son"),
        drawn([caps("4:18"), cp("4:19", to="unto his father,"), say("4:19", frm="My head,", to="my head."), cp("4:19", frm="And he said to his servant,", to="to his servant,"), say("4:19", frm="Carry him"),
               caps("4:20-21")], "2KGS 4:18–21", below(lambda w, h: K.reapers("rp2", w, h, 209), 0.44), "#FFE6A0"),
        face([cp("4:22", to="and said,"), say("4:22", frm="Send me,"), cp("4:23", to="And he said,"), say("4:23", frm="Wherefore", to="nor sabbath."), cp("4:23", frm="And she said,", to="And she said,"),
              say("4:23", frm="It shall be well."), cp("4:24", to="and said to her servant,"), say("4:24", frm="Drive,")], "2KGS 4:22–24", SHUNAMMITE_GRIEF, bg=COLD),
        drawn([cp("4:25", to="to Gehazi his servant,"), say("4:25", frm="Behold, yonder"), say("4:26", to="is it well with the child?"),
               cp("4:26", frm="And she answered,", to="And she answered,"), say("4:26", frm="It is well.")], "2KGS 4:25–26", below(lambda w, h: K.ride_carmel("rc2", w, h, 210), 0.4), "#8FD0E2",
              head="It Is Well"),
        face([cp("4:27", to="but the man of God said,"), say("4:27", frm="Let her alone:"), cp("4:28", to="Then she said,"), say("4:28", frm="Did I desire")], "2KGS 4:27–28", SHUNAMMITE_GRIEF, bg=COLD),
        face([cp("4:29", to="Then he said to Gehazi,"), say("4:29", frm="Gird up"), cp("4:30", to="And the mother of the child said,"), say("4:30", frm="As Jehovah liveth,", to="leave thee."),
              cp("4:30", frm="And he arose,")], "2KGS 4:29–30", ELISHA_STERN),
        face([cp("4:31", to="saying,"), say("4:31", frm="The child is not awaked."), caps("4:32-33")], "2KGS 4:31–33", GEHAZI, bg=COLD),
        drawn([caps("4:34-35")], "2KGS 4:34–35", CHAMBER(211), "#D8B88A"),
        drawn([cp("4:36", to="and said,"), say("4:36", frm="Call this Shunammite.", to="Call this Shunammite."), cp("4:36", frm="So he called her.", to="he said,"), say("4:36", frm="Take up thy son."), caps("4:37")],
              "2KGS 4:36–37", below(lambda w, h: K.upper_chamber("uc2c", w, h, 212, down=True), 0.36), "#D8B88A"),
        drawn([cp("4:38", to="and he said unto his servant,"), say("4:38", frm="Set on"), caps("4:39"), cp("4:40", to="and said,"), say("4:40", frm="O man of God,", to="in the pot."),
               cp("4:40", frm="And they could not eat")], "2KGS 4:38–40", below(lambda w, h: K.pottage("pt2", w, h, 213), 0.44), "#E8C8A0", head="Death in the Pot"),
        face([cp("4:41", to="But he said,"), say("4:41", frm="Then bring meal.", to="Then bring meal."), cp("4:41", frm="And he cast it", to="and he said,"), say("4:41", frm="Pour out", to="that they may eat."),
              cp("4:41", frm="And there was no harm")], "2KGS 4:41", ELISHA),
        drawn([cp("4:42", to="And he said,"), say("4:42", frm="Give unto the people,"), cp("4:43", to="And his servant said,"), say("4:43", frm="What,", to="a hundred men?"), cp("4:43", frm="But he said,", to="But he said,"),
               say("4:43", frm="Give the people,", to="for thus saith Jehovah,"), gd("4:43", frm="They shall eat,"), caps("4:44")], "2KGS 4:42–44", below(lambda w, h: K.loaves(w, h, 214), 0.5), "#5A3A22")]
PG.extend(pack(SEGS, "2KI-C02-D", PG.next(), end=end_mark("NEXT · NAAMAN", "right: 10px; bottom: 34px")))
