"""Joshua Book One — Jericho (Joshua 1–24). Writes the .dc.html pages into the given folder.
Usage: python3 joshua_book1.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus3 as Y, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
FX = J.tokens()
PAGES = {}
JOSHUA = dict(body="#12090A", cloth="#B5421E")
WAR = ("#8A3A1E", "#5A2A16", "#3A2214", "#5A6E8A")


def procession(p, x0, x1, y, s, seed, flip=False):
    """Men of war, then seven priests with trumpets, then the ark, marching to the right (or left when flipped)."""
    r = random.Random(seed); o = []; x = x0; step = 46 * s
    for i in range(6):
        o.append(person(p, round(x), y + r.randint(-3, 3), round(s, 3), body="#2A140C", cloth=r.choice(WAR), kind="Tunic", sw=4, flip=flip, extra=Z.SPEAR)); x += step
    for i in range(7):
        o.append(J.trumpeter(p, x, y + r.randint(-3, 3), s, flip=flip)); x += step
    o.append(J.ark_borne(p, x + 120 * s, y, s, f"pr{seed}", gap=110 * s, glow=False))
    return "".join(o)


# ───────────────────────── Cover ─────────────────────────
def cover():
    r = random.Random(7)
    horns = "".join(J.trumpeter("c1", x, y, sc, flip=fl) + J.blasts(x + (-60 if fl else 30) * sc, y - 200 * sc, sc * 1.2)
                    for x, y, sc, fl in [(90, 1000, 0.8, False), (200, 1018, 0.88, False), (580, 1018, 0.88, True), (690, 1000, 0.8, True)])
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c1", "Man", "ManUp", "Robe", "Tunic", "Hair")}
    {V.rays(380, 640, 40, 100, 900, color="#FFF4C2", op=0.2)}
    {J.jericho(-20, 140, 640, 820, 1, towers=1)}
    {J.jericho(620, 790, 660, 820, 2, towers=1)}
    {J.collapse(120, 640, 840, 420, 3)}
    <path d="M-10 830 C 200 820 500 836 770 826 L 770 1090 L -10 1090 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
    {crowd("c1", 30, -10, 770, 850, 900, 4, 0.18, 0.3, body=("#2A140C", "#3A2214"), cloth=WAR)}
    {J.ark_borne("c1", 380, 990, 0.72, "cva")}
    {horns}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 160px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">JOSHUA</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — Jericho</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 24</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>ヨ</span><span>シ</span><span>ュ</span><span>ア</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">YOSHUA-KI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">and the wall fell down flat, so that the people went up into the city, every man straight before him,</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #12113A 0%, #5A0E16 30%, #D7261E 55%, #FF8A3D 75%, #FFC14D 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Joshua Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover


# ───────────────────────── 01 · Be Strong (1:1–2, 1:9) ─────────────────────────
def p01():
    rod = '<path d="M520 230 L 528 70 C 528 50 550 48 554 64" fill="none" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path><path d="M520 230 L 528 70 C 528 50 550 48 554 64" fill="none" stroke="#8A5A30" stroke-width="5" stroke-linecap="round"></path>'
    s1 = f'''      {stars(50, 702, 200, 11)}
      <path d="M-10 304 L 300 200 C 420 160 560 170 712 220 L 712 304 Z" fill="#2A1A2E" stroke="#0D0D0F" stroke-width="2"></path>
      {rod}
      <path d="M470 236 C 500 222 560 222 590 236 L 590 244 L 470 244 Z" fill="#E2D8C4" stroke="#0D0D0F" stroke-width="2"></path>'''
    o1 = (cap("Now it came to pass after the death of Moses the servant of Jehovah, that Jehovah spake unto Joshua the son of Nun, Moses' minister, saying,", "left: 12px; top: 12px", maxw=380)
          + stamp(1, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 70%, #C2456A 100%)", 702, 294, s1, o1, "1 · After the death of Moses")

    s2 = f'''      {defs("b2", "Man", "Robe", "Tunic")}
      {hills(170, "#3F8A44", 12, 50)}
      <path d="M-10 230 C 200 210 500 250 712 220 L 712 270 C 500 290 200 260 -10 280 Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 270 C 200 260 500 290 712 266 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {N.camp(14, 20, 690, 300, 380, 13)}
      {person("b2", 600, 396, 0.9, stroke="#0D0D0F", **JOSHUA)}'''
    o2 = (god("Moses my servant is dead; now therefore arise, go over this Jordan, thou, and all this people, unto the land which I do give to them, even to the children of Israel.", "left: 12px; top: 12px", size=17, maxw=460)
          + ref("JOSH 1:2", "right: 12px; top: 12px", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 60%)", 702, 392, s2, o2, "2 · Go over this Jordan")

    s3 = f'''      {V.rays(160, 160, 30, 60, 600, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_JOSHUA_LEAD__"], -60, 10, 0.8)}'''
    o3 = (god("Have not I commanded thee? Be strong and of good courage; be not affrighted, neither be thou dismayed: for Jehovah thy God is with thee whithersoever thou goest.", "left: 280px; top: 30px", size=17, maxw=400)
          + ref("JOSH 1:9", "right: 12px; bottom: 9px"))
    P3 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 30px, #FF8A3D 200px, #5A0E16 460px)", 702, 294, s3, o3, "3 · Be strong and of good courage")
    body = P1 + P2 + P3
    return mk.page("Joshua 1:1–9 — Be Strong", "300px minmax(0, 1fr) 300px", body, 1)
PAGES["JO1-P01-Strong"] = p01


# ───────────────────────── 02 · Rahab (2:1–21) ─────────────────────────
def p02():
    s1 = f'''      {defs("r1", "Man", "Robe", "Tunic")}
      {J.jericho(-10, 712, 110, 250, 21, towers=3)}
      <path d="M300 250 L 300 170 C 300 140 400 140 400 170 L 400 250 Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("r1", 330, 270, 0.42, body="#12090A", cloth="#5A4A3E", kind="Robe", sw=4)}
      {person("r1", 370, 274, 0.44, body="#12090A", cloth="#3A2A3E", kind="Robe", sw=4)}'''
    o1 = (cap("And Joshua the son of Nun sent out of Shittim two men as spies secretly, saying, Go, view the land, and Jericho. And they went and came into the house of a harlot whose name was Rahab, and lay there.", "left: 12px; top: 12px", maxw=420)
          + stamp(2, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #2A1A5E 0%, #C2456A 60%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · Two men as spies")

    s2 = f'''      {defs("r2", "Man", "Woman", "Hair", "Robe")}
      {stars(30, 342, 160, 22)}
      <rect x="-10" y="200" width="362" height="110" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.4"></rect>
      {E.kneel(110, 196, 0.34, color="#3A2A3E")}
      {E.kneel(170, 196, 0.34, color="#5A4A3E")}
      {J.flax(60, 200, 170, 23)}
      {J.flax(80, 196, 140, 24)}
      {person("r2", 290, 200, 0.62, body="#3A1E14", cloth="#D7261E", woman=True, hair=True)}'''
    o2 = cap("But she had brought them up to the roof, and hid them with the stalks of flax, which she had laid in order upon the roof.", "left: 10px; top: 10px", size=10, maxw=320)
    P2a = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 100%)", 342, 294, s2, o2, "2a · Hid them with flax")
    s3 = f'''      {face(FX["__FACE_RAHAB__"], 412, 10, 0.78, flip=True)}'''
    o3 = ref("RAHAB", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P2b = panel("radial-gradient(circle at 70% 40%, #FFE680 0 20px, #FF8A3D 150px, #2A1A5E 330px)", 342, 294, s3, o3, "2b · Rahab")

    rope = '<path d="M300 150 L 304 360" stroke="#0D0D0F" stroke-width="5"></path><path d="M300 150 L 304 360" stroke="#C9A86A" stroke-width="3"></path>'
    s4 = f'''      {defs("r4", "Man", "ManUp", "Robe", "Tunic")}
      {stars(70, 702, 120, 25)}
      {J.jericho(-10, 712, 70, 400, 26, towers=2, window=(300, 130), cord=0)}
      {rope}
      {person("r4", 312, 300, 0.5, body="#12090A", cloth="#3A2A3E", kind="Robe", sw=4, up=[(-22, -158), (-14, -196), (-8, -228)])}
      {person("r4", 220, 398, 0.5, body="#12090A", cloth="#5A4A3E", kind="Robe", sw=4)}'''
    o4 = (cap("Then she let them down by a cord through the window: for her house was upon the side of the wall, and she dwelt upon the wall.", "left: 12px; top: 12px", maxw=250)
          + balloon("Behold, when we come into the land, thou shalt bind this line of scarlet thread in the window which thou didst let us down by: and thou shalt gather unto thee into the house thy father, and thy mother, and thy brethren, and all thy father's household.", "right: 14px; top: 12px", 340, size=11.5, pad="26px 34px")
          + cap("And she said, According unto your words, so be it. And she sent them away, and they departed: and she bound the scarlet line in the window.", "right: 12px; bottom: 12px", size=10.5, maxw=320))
    P3 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 392, s4, o4, "3 · The line of scarlet thread")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Joshua 2:1–21 — Rahab", "300px 300px minmax(0, 1fr)", body, 2)
PAGES["JO1-P02-Rahab"] = p02


# ───────────────────────── 03 · Crossing Jordan (3:15–17) ─────────────────────────
def p03():
    s1 = f'''      {defs("j1", "Man", "Robe", "Tunic")}
      {hills(260, "#3F8A44", 31, 40)}
      {J.heap(170, 380, 320, 260, "j1h")}
      <path d="M-10 380 C 200 370 500 386 712 376 L 712 604 L -10 604 Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></path>
      {J.riverbed(0, 712, 400, 600, 32)}
      <path d="M-10 470 C 120 480 300 520 712 520 L 712 604 L -10 604 Z" fill="#6A5A3A" opacity="0.5"></path>
      {J.ark_borne("j1", 430, 560, 1.1, "j1a")}'''
    o1 = (cap("… and when they that bare the ark were come unto the Jordan, and the feet of the priests that bare the ark were dipped in the brink of the water (for the Jordan overfloweth all its banks all the time of harvest),", "left: 12px; top: 12px", maxw=380)
          + cap("that the waters which came down from above stood, and rose up in one heap, a great way off, at Adam, the city that is beside Zarethan; and those that went down toward the sea of the Arabah, even the Salt Sea, were wholly cut off: and the people passed over right against Jericho.", "right: 12px; top: 150px", size=10.5, maxw=300)
          + sfx("ゴゴゴゴ", "GOGOGOGO", "left: 30px; top: 300px", size=40, fill="#8FD0E2", stroke="#0D0D0F", rot=-6, align="flex-start")
          + stamp(3, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 50%)", 702, 594, s1, o1, "1 · The waters stood in one heap")

    s2 = f'''      {defs("j2", "Man", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M-10 160 L 712 160 L 712 304 L -10 304 Z" fill="#8A7A5A"></path>
      {J.riverbed(0, 712, 170, 300, 33)}
      {J.ark_borne("j2", 600, 260, 0.6, "j2a", glow=True)}
      {crowd("j2", 40, -10, 480, 170, 290, 34, 0.2, 0.42)}'''
    o2 = (cap("And the priests that bare the ark of the covenant of Jehovah stood firm on dry ground in the midst of the Jordan; and all Israel passed over on dry ground, until all the nation were passed clean over the Jordan.", "left: 12px; top: 12px", maxw=460)
          + ref("JOSH 3:17", "right: 12px; top: 12px", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 702, 294, s2, o2, "2 · On dry ground")
    body = P1 + P2
    return mk.page("Joshua 3:15–17 — Crossing Jordan", "minmax(0, 1fr) 300px", body, 3)
PAGES["JO1-P03-Jordan"] = p03


# ───────────────────────── 04 · The Prince of the Host (5:13–15) ─────────────────────────
def p04():
    s1 = f'''      {defs("h1", "Man", "ManUp", "Robe", "Tunic", "Hair")}
      {J.jericho(-10, 300, 140, 240, 41, towers=1)}
      <path d="M-10 240 L 712 240 L 712 304 L -10 304 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("h1", 380, 290, 0.6, stroke="#0D0D0F", **JOSHUA)}
      {J.prince("h1", 560, 290, 0.66, flip=True)}'''
    o1 = (cap("And it came to pass, when Joshua was by Jericho, that he lifted up his eyes and looked, and, behold, there stood a man over against him with his sword drawn in his hand: and Joshua went unto him, and said unto him,", "left: 12px; top: 12px", maxw=330)
          + stamp(5, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 60%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · A man with his sword drawn")

    s2 = f'''      {defs("h2", "Man", "ManUp", "Robe", "Hair")}
      {V.rays(500, 160, 36, 60, 700, color="#FFFFFF", op=0.4)}
      <path d="M-10 330 L 712 330 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {J.prince("h2", 500, 380, 1.2, flip=True)}
      {N.prostrate(170, 376, 1.1, color="#B5421E", skin="#C98E66")}'''
    o2 = (balloon("Art thou for us, or for our adversaries?", "left: 12px; top: 12px", 240, size=15, pad="18px 26px")
          + god("Nay; but as prince of the host of Jehovah am I now come.", "right: 12px; top: 12px", size=19, maxw=260)
          + cap("And Joshua fell on his face to the earth, and did worship, and said unto him,", "left: 12px; top: 128px", size=10, maxw=250)
          + balloon("What saith my lord unto his servant?", "left: 30px; top: 200px", 200, size=14, pad="16px 20px"))
    P2 = panel("radial-gradient(circle at 70% 40%, #FFFFFF 0 60px, #FFF4C2 180px, #FFC14D 320px, #C2456A 520px)", 702, 392, s2, o2, "2 · Prince of the host of Jehovah")

    s3 = f'''      {V.rays(171, 160, 30, 40, 400, color="#FFF4C2", op=0.3)}'''
    o3 = (cap("And the prince of Jehovah's host said unto Joshua,", "left: 10px; top: 10px", size=10, maxw=300)
          + god("Put off thy shoe from off thy foot; for the place whereon thou standest is holy.", "left: 10px; top: 60px", size=18, maxw=300))
    P3a = panel("radial-gradient(circle at 50% 50%, #FFF4C2 0 30px, #FF8A3D 200px, #5A0E16 360px)", 342, 294, s3, o3, "3a · The place is holy")
    s4 = f'''      <path d="M-10 200 L 352 200 L 352 304 L -10 304 Z" fill="#C8A06A"></path>
      {E.sandal(120, 250, 1.4, -20)}
      {E.sandal(220, 256, 1.4, 70)}
      {V.rays(171, 240, 20, 30, 300, color="#FFF4C2", op=0.25)}'''
    o4 = cap("And Joshua did so.", "right: 10px; top: 10px", size=12) + ref("JOSH 5:15", "left: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6")
    P3b = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 342, 294, s4, o4, "3b · Joshua did so")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Joshua 5:13–15 — The Prince of the Host", "300px minmax(0, 1fr) 300px", body, 4)
PAGES["JO1-P04-Prince"] = p04


# ───────────────────────── 05 · Compass the City (6:2–4, 6:15–16) ─────────────────────────
def p05():
    s1 = f'''      {stars(40, 702, 120, 51)}
      {J.jericho(180, 712, 130, 304, 52, towers=3)}'''
    o1 = (cap("And Jehovah said unto Joshua,", "left: 12px; top: 12px", size=10)
          + god("See, I have given into thy hand Jericho, and the king thereof, and the mighty men of valor.", "left: 12px; top: 52px", size=19, maxw=360)
          + stamp(6, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 100%)", 702, 294, s1, o1, "1 · I have given into thy hand Jericho")

    s2 = f'''      {defs("m2", "Man", "ManUp", "Robe", "Tunic")}
      {J.jericho(-10, 712, 150, 290, 53, towers=4)}
      <path d="M-10 290 L 712 290 L 712 404 L -10 404 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {procession("m2", 10, 712, 390, 0.5, 54)}'''
    o2 = god("And ye shall compass the city, all the men of war, going about the city once. Thus shalt thou do six days. And seven priests shall bear seven trumpets of rams' horns before the ark: and the seventh day ye shall compass the city seven times, and the priests shall blow the trumpets.", "left: 12px; top: 12px", size=14, maxw=560)
    P2 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 392, s2, o2, "2 · Compass the city")

    s3 = f'''      {defs("m3", "Man", "ManUp", "Robe", "Tunic")}
      {J.sun(60, 200, 30)}
      {J.jericho(60, 300, 140, 240, 55, towers=1, houses=False)}
      <path d="M-10 240 L 352 240 L 352 304 L -10 304 Z" fill="#8A6A4A"></path>
      {"".join(person("m3", x, 280, 0.24, body="#12090A", cloth="#12090A", sw=2) for x in range(20, 340, 18))}'''
    o3 = (cap("And it came to pass on the seventh day, that they rose early at the dawning of the day, and compassed the city after the same manner seven times: only on that day they compassed the city seven times.", "left: 10px; top: 10px", size=9.5, maxw=320)
          + badge("七度", "right: 10px; bottom: 10px", size=18))
    P3a = panel("linear-gradient(180deg, #4A1D55 0%, #FF8A3D 60%, #FFC14D 100%)", 342, 294, s3, o3, "3a · Seven times")
    s4 = f'''      {speed(240, 160, 50, 80, 400, 56, color="#0D0D0F", sw=2, op=0.35)}
      {face(FX["__FACE_JOSHUA_LEAD__"], 412, 30, 0.72, flip=True)}'''
    o4 = (cap("And it came to pass at the seventh time, when the priests blew the trumpets, Joshua said unto the people,", "left: 10px; top: 10px", size=9.5, maxw=200)
          + tail(190, 210, "r")
          + balloon("Shout; for Jehovah hath given you the city.", "left: 8px; top: 140px", 190, size=16, pad="20px 18px"))
    P3b = panel("radial-gradient(circle at 70% 40%, #FFE680 0 20px, #FF6A2A 150px, #5A0E16 320px)", 342, 294, s4, o4, "3b · Shout")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Joshua 6:2–16 — Compass the City", "300px minmax(0, 1fr) 300px", body, 5)
PAGES["JO1-P05-Compass"] = p05


# ───────────────────────── 06 · The Wall Fell Down Flat (6:20) ─────────────────────────
def p06():
    shouters = "".join(person("w1", x, y, sc, body="#2A140C", cloth=c, kind="Tunic", sw=4, up=[(-22, -158), (-40, -206), (-30, -252)], extra=Z.SPEAR if k % 2 else "")
                       for k, (x, y, sc, c) in enumerate([(40, 690, 0.8, "#8A3A1E"), (130, 700, 0.9, "#5A2A16"), (560, 700, 0.9, "#5A6E8A"), (660, 690, 0.8, "#3A2214")]))
    s1 = f'''      {defs("w1", "Man", "ManUp", "Robe", "Tunic")}
      {V.rays(351, 360, 40, 80, 800, color="#FFF4C2", op=0.3)}
      {J.collapse(-10, 712, 540, 440, 61)}
      <path d="M-10 540 C 200 530 500 546 712 536 L 712 704 L -10 704 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("w1", 30, -10, 712, 550, 620, 62, 0.22, 0.4, cloth=WAR)}
      {J.trumpeter("w1", 250, 700, 0.95)}{J.blasts(280, 500, 1.3)}
      {J.trumpeter("w1", 450, 700, 0.95, flip=True)}{J.blasts(360, 500, 1.3)}
      {shouters}'''
    o1 = (cap("So the people shouted, and the priests blew the trumpets: and it came to pass, when the people heard the sound of the trumpet, that the people shouted with a great shout,", "left: 12px; top: 12px", maxw=330)
          + '    <div style="position: absolute; right: 14px; top: 110px; padding: 10px 16px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 3px #FFD23F; font-family: Anton, sans-serif; font-size: 34px; line-height: 1.05; text-transform: uppercase; max-width: 300px">and the wall fell down flat,</div>\n'
          + sfx("ドドドドッ", "DODODODO", "left: 20px; top: 300px", size=52, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start")
          + sfx("ワーッ", "WAAA!", "right: 20px; top: 260px", size=44, fill="#D7261E", stroke="#F3EFE6", rot=8, tagbg="#0D0D0F", tagfg="#F3EFE6"))
    P1 = panel("linear-gradient(180deg, #5A0E16 0%, #D7261E 40%, #FF8A3D 70%, #FFC14D 100%)", 702, 694, s1, o1, "1 · The wall fell down flat")

    s2 = f'''      {defs("w2", "Man", "Robe", "Tunic")}
      {J.collapse(-10, 712, 200, 80, 63)}
      <path d="M-10 200 L 712 200 L 712 254 L -10 254 Z" fill="#8A6A4A"></path>
      {"".join(person("w2", x, 160 + (x * 7) % 40, 0.32, body="#12090A", cloth=WAR[x % 4], kind="Tunic", sw=4, extra=Z.SPEAR) for x in range(20, 700, 40))}'''
    o2 = (cap("so that the people went up into the city, every man straight before him, and they took the city.", "left: 12px; top: 12px", maxw=420)
          + ref("JOSH 6:20", "right: 12px; bottom: 9px"))
    P2 = panel("linear-gradient(180deg, #2A1A2E 0%, #5A0E16 100%)", 702, 244, s2, o2, "2 · They took the city")
    body = P1 + P2
    return mk.page("Joshua 6:20 — The Wall Fell Down Flat", "minmax(0, 1fr) 250px", body, 6)
PAGES["JO1-P06-Wall"] = p06


# ───────────────────────── 07 · Sun, Stand Thou Still (10:12–14) ─────────────────────────
def p07():
    s1 = f'''      {speed(160, 150, 60, 100, 600, 71, color="#0D0D0F", sw=2, op=0.35)}
      {face(FX["__FACE_JOSHUA_LEAD__"], -60, 0, 0.82)}'''
    o1 = (cap("Then spake Joshua to Jehovah in the day when Jehovah delivered up the Amorites before the children of Israel; and he said in the sight of Israel,", "right: 12px; top: 12px", maxw=380)
          + tail(250, 196, "l")
          + balloon("Sun, stand thou still upon Gibeon; And thou, Moon, in the valley of Aijalon.", "left: 290px; top: 110px", 390, size=19, pad="22px 40px")
          + stamp(10, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFE680 0 30px, #FF6A2A 200px, #3A0E0E 460px)", 702, 294, s1, o1, "1 · Sun, stand thou still")

    s2 = f'''      {defs("s2", "Man", "Robe", "Tunic")}
      {J.sun(170, 90, 44)}
      {J.moon(560, 110, 32)}
      {J.city_hill(170, 260, 170, 110, 72)}
      <path d="M380 260 C 450 230 560 230 712 250 L 712 404 L 380 404 Z" fill="#3F8A44" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 250 C 200 240 500 260 712 250 L 712 404 L -10 404 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2" opacity="0.9"></path>
      {Z.warriors("s2", 18, 20, 360, 300, 390, 73, 0.3, 0.5)}
      {Z.warriors("s2", 14, 420, 700, 290, 360, 74, 0.2, 0.32, flip=True, body="#12090A", cloth=("#2A2A3A", "#3A3A4A"))}'''
    o2 = (cap("And the sun stood still, and the moon stayed, Until the nation had avenged themselves of their enemies. Is not this written in the book of Jashar? And the sun stayed in the midst of heaven, and hasted not to go down about a whole day.", "right: 12px; top: 160px", size=10.5, maxw=290)
          + badge("日よ、止まれ", "left: 12px; top: 12px", bg="#5A0E16", fg="#FFE680", size=17))
    P2 = panel("linear-gradient(180deg, #2C9DB8 0%, #8FD0E2 50%, #FFE3B8 100%)", 702, 392, s2, o2, "2 · The sun stood still")

    s3 = f'''      {V.rays(600, 40, 30, 40, 600, color="#FFF4C2", op=0.35)}
      {J.sun(600, 40, 30)}'''
    o3 = (cap("And there was no day like that before it or after it, that Jehovah hearkened unto the voice of a man: for Jehovah fought for Israel.", "left: 12px; top: 40px", size=14, maxw=470)
          + ref("JOSH 10:14", "left: 12px; bottom: 9px"))
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FF8A3D 60%, #C2456A 100%)", 702, 274, s3, o3, "3 · No day like that")
    body = P1 + P2 + P3
    return mk.page("Joshua 10:12–14 — Sun, Stand Thou Still", "300px minmax(0, 1fr) 280px", body, 7)
PAGES["JO1-P07-Sun"] = p07


# ───────────────────────── 08 · Choose You This Day (24:14–29) ─────────────────────────
def p08():
    s1 = f'''      {face(FX["__FACE_JOSHUA_OLD__"], -60, 0, 0.82)}'''
    o1 = (tail(250, 160, "l")
          + balloon("Now therefore fear Jehovah, and serve him in sincerity and in truth; and put away the gods which your fathers served beyond the River, and in Egypt; and serve ye Jehovah.", "left: 290px; top: 30px", 400, size=15, pad="24px 40px")
          + stamp(24, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 30px, #FFC14D 200px, #4A1D55 460px)", 702, 274, s1, o1, "1 · Fear Jehovah")

    s2 = f'''      {defs("c2", "Man", "ManUp", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M-10 280 C 200 270 500 286 712 276 L 712 434 L -10 434 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {J.oak(100, 300, 1.1, 81)}
      {person("c2", 180, 330, 0.95, body="#12090A", cloth="#B5421E", stroke="#FFF4C2", sw=3, up=[(-22, -158), (-46, -200), (-50, -246)])}
      {crowd("c2", 40, 280, 712, 290, 420, 82, 0.22, 0.5)}'''
    o2 = (balloon("And if it seem evil unto you to serve Jehovah, choose you this day whom ye will serve; whether the gods which your fathers served that were beyond the River, or the gods of the Amorites, in whose land ye dwell: but as for me and my house, we will serve Jehovah.", "right: 14px; top: 12px", 460, size=14.5, pad="26px 44px")
          + ref("JOSH 24:15", "left: 12px; top: 12px", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 702, 424, s2, o2, "2 · Choose you this day")

    s3 = f'''      {defs("c3", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      <path d="M-10 200 L 352 200 L 352 304 L -10 304 Z" fill="#C8A06A"></path>
      {"".join(person("c3", x, 290 - (i % 2) * 20, 0.42 - (i % 2) * 0.06, body="#2A140C", cloth=c, woman=i % 3 == 0, hair=i % 3 == 0, kind="Robe", sw=4, up=[(-22, -158), (-40, -206), (-30, -250)]) for i, (x, c) in enumerate([(30, "#C9A86A"), (80, "#5A6E8A"), (130, "#8A6A4A"), (180, "#C2456A"), (230, "#3F8A44"), (280, "#7A3BA8"), (330, "#C9A86A")]))}'''
    o3 = (cap("And the people said unto Joshua,", "left: 10px; top: 10px", size=10)
          + balloon("Jehovah our God will we serve, and unto his voice will we hearken.", "left: 30px; top: 46px", 280, size=14, pad="18px 30px"))
    P3a = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 342, 294, s3, o3, "3a · We will serve")
    s4 = f'''      {J.sun(250, 170, 40)}
      {hills(190, "#3A2A3E", 83, 40, 342)}'''
    o4 = (cap("And it came to pass after these things, that Joshua the son of Nun, the servant of Jehovah, died, being a hundred and ten years old.", "left: 10px; top: 10px", size=10, maxw=300)
          + '    <div style="position: absolute; left: 12px; bottom: 12px; display: flex; align-items: center; gap: 8px; padding: 4px 10px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 2px #FFD23F"><span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 20px">終</span><span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em">END OF JOSHUA</span></div>\n')
    P3b = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 50%, #FF8A3D 100%)", 342, 294, s4, o4, "3b · Joshua died")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Joshua 24:14–29 — Choose You This Day", "280px minmax(0, 1fr) 300px", body, 8)
PAGES["JO1-P08-Choose"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "joshua/project"))
