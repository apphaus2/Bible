"""Ruth Book One — Whither Thou Goest (Ruth 1–4). Writes the .dc.html pages into the given folder.
Usage: python3 ruth_book1.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus3 as Y, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J, judges1 as G, judges2 as S, ruth1 as R
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
from judges_book2 import end_mark
FX = R.tokens()
PAGES = {}
NAOMI = dict(body="#3A1E14", cloth="#4A3A6A", woman=True, hair="#B8B2A6")
RUTH = dict(body="#3A1E14", cloth="#C2456A", woman=True, hair=True)
ORPAH = dict(body="#3A1E14", cloth="#E8A317", woman=True, hair=True)
BOAZ = dict(body="#2A140C", cloth="#F3EFE6")
MOAB = "#7A3BA8"


def bethlehem(cx, base, w, h, seed):
    return J.city_hill(cx, base, w, h, seed)


# ───────────────────────── Cover ─────────────────────────
def cover():
    r = random.Random(11)
    reapers = "".join(R.reaper("c1", x, 830 + r.uniform(-8, 8), 0.42, flip=x > 500, cloth=r.choice(["#8A6A4A", "#5A6E8A", "#C9A86A"])) for x in (90, 180, 560, 660))
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c1", "Man", "ManUp", "Robe", "Tunic", "Woman", "Hair")}
    {J.sun(560, 640, 70)}
    {V.rays(560, 640, 36, 90, 800, color="#FFF4C2", op=0.2)}
    {bethlehem(560, 760, 200, 120, 12)}
    <path d="M-10 770 C 200 750 500 780 770 760 L 770 1090 L -10 1090 Z" fill="#E8A35A" stroke="#0D0D0F" stroke-width="2"></path>
    {R.field(-10, 770, 800, 30, 13, rows=2)}
    {reapers}
    {"".join(R.sheaf(x, 900, 1.0) for x in (60, 140, 640, 720))}
    {R.field(-10, 770, 1000, 50, 14, rows=2)}
    {R.gleaner(320, 1000, 2.4)}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 168px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">RUTH</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — Whither Thou Goest</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 4</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>ル</span><span>ツ</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">RUTSU-KI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">for whither thou goest, I will go; and where thou lodgest, I will lodge;</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #2A1A5E 0%, #7A3BA8 25%, #C2456A 45%, #FF8A3D 65%, #FFC14D 80%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Ruth Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover


# ───────────────────────── 01 · When the Judges Judged (1:1–5) ─────────────────────────
def p01():
    s1 = f'''      {defs("a1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {J.sun(600, 70, 40)}
      {hills(170, MOAB, 101, 40)}
      <path d="M-10 200 L 712 200 L 712 294 L -10 294 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(f'<path d="M{x} {y} l 30 4 l 10 -6" fill="none" stroke="#8A5A30" stroke-width="2"></path>' for x, y in [(40, 250), (120, 270), (220, 240), (520, 260), (620, 280)])}
      {person("a1", 340, 272, 0.56, body="#2A140C", cloth="#8A6A4A", sw=4)}
      {person("a1", 390, 274, 0.54, **NAOMI, sw=4)}
      {person("a1", 440, 276, 0.42, body="#2A140C", cloth="#5A6E8A", kind="Tunic", sw=4)}
      {person("a1", 480, 276, 0.4, body="#2A140C", cloth="#3F8A44", kind="Tunic", sw=4)}'''
    o1 = (cap("And it came to pass in the days when the judges judged, that there was a famine in the land. And a certain man of Beth-lehem-judah went to sojourn in the country of Moab, he, and his wife, and his two sons.", "left: 12px; top: 12px", maxw=380)
          + stamp(1, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 60%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · A famine in the land")

    s2 = f'''      {defs("a2", "Man", "Woman", "Hair", "Robe")}
      {hills(200, MOAB, 102, 40, 342)}
      <path d="M-10 230 L 352 230 L 352 304 L -10 304 Z" fill="#8A6A4A"></path>
      {R.graves(120, 260, 1, 1.2)}
      {E.kneel(240, 270, 0.5, color="#4A3A6A", flip=True)}'''
    o2 = cap("And Elimelech, Naomi's husband, died; and she was left, and her two sons.", "left: 10px; top: 10px", size=10.5, maxw=320)
    P2a = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 100%)", 342, 294, s2, o2, "2a · Elimelech died")
    s3 = f'''      {defs("a3", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {hills(200, MOAB, 103, 40, 342)}
      <path d="M-10 230 L 352 230 L 352 304 L -10 304 Z" fill="#C8A06A"></path>
      {person("a3", 60, 286, 0.5, body="#2A140C", cloth="#5A6E8A", kind="Tunic", sw=4)}
      {person("a3", 110, 286, 0.46, **ORPAH, sw=4)}
      {person("a3", 220, 286, 0.5, body="#2A140C", cloth="#3F8A44", kind="Tunic", sw=4)}
      {person("a3", 270, 286, 0.46, **RUTH, sw=4)}'''
    o3 = cap("And they took them wives of the women of Moab; the name of the one was Orpah, and the name of the other Ruth: and they dwelt there about ten years.", "left: 10px; top: 10px", size=10, maxw=320)
    P2b = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 342, 294, s3, o3, "2b · Orpah and Ruth")

    s4 = f'''      {stars(40, 702, 200, 104)}
      {hills(240, "#3A1E4A", 105, 40)}
      <path d="M-10 280 L 712 280 L 712 404 L -10 404 Z" fill="#3A2A2E" stroke="#0D0D0F" stroke-width="2"></path>
      {R.graves(400, 330, 3, 1.2)}
      {E.kneel(160, 360, 0.6, color="#4A3A6A", flip=False)}
      {E.kneel(230, 364, 0.56, color="#E8A317")}
      {E.kneel(290, 364, 0.56, color="#C2456A")}'''
    o4 = (cap("And Mahlon and Chilion died both of them; and the woman was left of her two children and of her husband.", "left: 12px; top: 12px", maxw=380)
          + ref("RUTH 1:5", "right: 12px; bottom: 9px"))
    P3 = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 100%)", 702, 394, s4, o4, "3 · The woman was left")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Ruth 1:1–5 — When the Judges Judged", "300px 300px minmax(0, 1fr)", body, 1)
PAGES["RU1-P01-Moab"] = p01


# ───────────────────────── 02 · Return, Each of You (1:8, 1:14) ─────────────────────────
def p02():
    s1 = f'''      {defs("b1", "Woman", "Hair", "Robe")}
      {hills(190, MOAB, 201, 40)}
      <path d="M-10 230 L 712 230 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M200 304 C 300 270 420 250 712 236 L 712 254 C 430 266 320 284 250 304 Z" fill="#E8C88A"></path>
      {person("b1", 120, 288, 0.66, **NAOMI)}
      {person("b1", 210, 290, 0.62, **ORPAH, flip=True)}
      {person("b1", 270, 290, 0.62, **RUTH, flip=True)}'''
    o1 = (cap("And Naomi said unto her two daughters-in-law,", "left: 12px; top: 12px", size=10)
          + tail(330, 140, "dl")
          + balloon("Go, return each of you to her mother's house: Jehovah deal kindly with you, as ye have dealt with the dead, and with me.", "left: 300px; top: 14px", 390, size=14, pad="20px 40px"))
    P1 = panel("linear-gradient(180deg, #C2456A 0%, #FFC14D 100%)", 702, 294, s1, o1, "1 · Return each of you")

    s2 = f'''      {face(FX["__FACE_ORPAH__"], -50, 20, 0.74)}'''
    o2 = cap("And they lifted up their voice, and wept again:", "left: 160px; top: 10px", size=10, maxw=170) + ref("ORPAH", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #E8A35A 150px, #5A1A3E 330px)", 342, 294, s2, o2, "2a · Orpah wept")
    s3 = f'''      {face(FX["__FACE_RUTH_WEEP__"], 412, 20, 0.74, flip=True)}'''
    o3 = sfx("ううっ", "UUH…", "left: 20px; top: 40px", size=36, fill="#8FD0E2", stroke="#0D0D0F", rot=-6, align="flex-start") + ref("RUTH", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P2b = panel("radial-gradient(circle at 70% 50%, #FFE680 0 20px, #C2456A 150px, #2A1A5E 330px)", 342, 294, s3, o3, "2b · Ruth wept")

    hug = [(-22, -158), (8, -150), (30, -150)]
    s4 = f'''      {defs("b4", "Woman", "WomanUp", "Hair", "Robe")}
      {J.sun(110, 120, 40)}
      {hills(220, MOAB, 202, 40)}
      <path d="M-10 270 L 712 270 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("b4", 130, 290, 0.3, **ORPAH, flip=True)}
      {person("b4", 470, 396, 1.0, **NAOMI)}
      {person("b4", 420, 398, 0.94, **RUTH, up=hug)}'''
    o4 = (cap("and Orpah kissed her mother-in-law, but Ruth clave unto her.", "right: 12px; top: 12px", size=13, maxw=300)
          + ref("RUTH 1:14", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 50%, #FFC14D 100%)", 702, 394, s4, o4, "3 · Ruth clave unto her")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Ruth 1:8–14 — Return, Each of You", "300px 300px minmax(0, 1fr)", body, 2)
PAGES["RU1-P02-Return"] = p02


# ───────────────────────── 03 · Whither Thou Goest (1:16–19) ─────────────────────────
def p03():
    s1 = f'''      {V.rays(160, 260, 36, 60, 800, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_RUTH__"], -40, 120, 1.15)}'''
    o1 = (cap("And Ruth said,", "right: 12px; top: 12px", size=11)
          + tail(320, 330, "l")
          + balloon("Entreat me not to leave thee, and to return from following after thee, for whither thou goest, I will go; and where thou lodgest, I will lodge; thy people shall be my people, and thy God my God; where thou diest, will I die, and there will I be buried: Jehovah do so to me, and more also, if aught but death part thee and me.", "left: 360px; top: 60px", 330, size=15.5, pad="40px 36px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 40px, #FFC14D 220px, #C2456A 460px, #4A1D55 640px)", 702, 694, s1, o1, "1 · Whither thou goest")

    s2 = f'''      {defs("c2", "Woman", "Hair", "Robe")}
      {J.sun(560, 140, 44)}
      {bethlehem(560, 200, 120, 70, 301)}
      <path d="M-10 190 C 200 180 500 196 712 186 L 712 254 L -10 254 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M60 254 C 200 230 380 210 520 196 L 540 198 C 400 216 240 236 120 254 Z" fill="#E8C88A"></path>
      {person("c2", 250, 226, 0.4, **NAOMI)}
      {person("c2", 290, 224, 0.4, **RUTH)}'''
    o2 = cap("So they two went until they came to Beth-lehem.", "left: 12px; top: 12px", size=12)
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 244, s2, o2, "2 · They two went")
    body = P1 + P2
    return mk.page("Ruth 1:16–19 — Whither Thou Goest", "minmax(0, 1fr) 250px", body, 3)
PAGES["RU1-P03-Whither"] = p03


# ───────────────────────── 04 · Call Me Mara (1:19–22) ─────────────────────────
def p04():
    s1 = f'''      {defs("d1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {J.jericho(-10, 712, 110, 230, 401, color="#E8C88A", towers=2)}
      <path d="M300 230 L 300 160 C 300 130 400 130 400 160 L 400 230 Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 230 L 712 230 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("d1", 330, 260, 0.5, **NAOMI)}{person("d1", 370, 262, 0.5, **RUTH)}
      {crowd("d1", 20, 420, 712, 240, 300, 402, 0.24, 0.42, cloth=("#C9A86A", "#E8C88A", "#8A6A4A", "#5A6E8A", "#C2456A", "#3F8A44"))}
      {crowd("d1", 12, -10, 270, 240, 300, 403, 0.24, 0.42)}'''
    o1 = (cap("And it came to pass, when they were come to Beth-lehem, that all the city was moved about them, and the women said,", "left: 12px; top: 12px", maxw=330)
          + balloon("Is this Naomi?", "right: 16px; top: 16px", 200, size=18, pad="18px 20px")
          + sfx("ザワ…", "ZAWA…", "right: 30px; bottom: 30px", size=34, fill="#F3EFE6", stroke="#0D0D0F", rot=6))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · Is this Naomi?")

    s2 = f'''      {face(FX["__FACE_MARA__"], -50, 10, 0.86)}'''
    o2 = (cap("And she said unto them,", "right: 12px; top: 12px", size=10)
          + tail(270, 200, "l")
          + balloon("Call me not Naomi, call me Mara; for the Almighty hath dealt very bitterly with me.", "left: 310px; top: 90px", 360, size=19, pad="26px 36px")
          + badge("苦", "right: 14px; bottom: 14px", bg="#2A2A3E", fg="#E8F0F6", size=34))
    P2 = panel("radial-gradient(circle at 25% 45%, #C8D0DE 0 30px, #5A6E8A 200px, #12113A 460px)", 702, 394, s2, o2, "2 · Call me Mara")

    s3 = f'''      {defs("d3", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {bethlehem(560, 170, 150, 80, 404)}
      <path d="M-10 160 C 200 150 500 166 712 156 L 712 304 L -10 304 Z" fill="#E8A35A" stroke="#0D0D0F" stroke-width="2"></path>
      {R.field(-10, 712, 200, 26, 405, rows=3)}
      {person("d3", 120, 290, 0.6, **NAOMI)}{person("d3", 180, 292, 0.6, **RUTH)}'''
    o3 = cap("So Naomi returned, and Ruth the Moabitess, her daughter-in-law, with her, who returned out of the country of Moab: and they came to Beth-lehem in the beginning of barley harvest.", "right: 12px; top: 12px", size=10.5, maxw=380)
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 294, s3, o3, "3 · The beginning of barley harvest")
    body = P1 + P2 + P3
    return mk.page("Ruth 1:19–22 — Call Me Mara", "300px minmax(0, 1fr) 300px", body, 4)
PAGES["RU1-P04-Mara"] = p04


# ───────────────────────── 05 · The Field of Boaz (2:2–5) ─────────────────────────
def p05():
    s1 = f'''      {defs("e1", "Woman", "Hair", "Robe")}
      <rect width="702" height="304" fill="#8A5A30"></rect>
      <rect x="440" y="40" width="120" height="100" fill="#FFE680" stroke="#0D0D0F" stroke-width="3"></rect>
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#5A3A22"></path>
      {person("e1", 160, 292, 0.68, **RUTH)}
      {person("e1", 260, 290, 0.7, **NAOMI, flip=True)}'''
    o1 = (cap("And Ruth the Moabitess said unto Naomi,", "left: 12px; top: 12px", size=10)
          + balloon("Let me now go to the field, and glean among the ears of grain after him in whose sight I shall find favor.", "left: 12px; top: 44px", 300, size=12.5, pad="18px 30px")
          + cap("And she said unto her,", "left: 340px; top: 12px", size=10)
          + balloon("Go, my daughter.", "left: 360px; top: 50px", 170, size=14, pad="14px 16px")
          + stamp(2, "right: 16px; bottom: 14px"))
    P1 = panel("#8A5A30", 702, 294, s1, o1, "1 · Let me now go to the field")

    r = random.Random(501)
    s2 = f'''      {defs("e2", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      {J.sun(620, 70, 40)}
      {bethlehem(140, 170, 120, 70, 502)}
      <path d="M-10 160 C 200 150 500 166 712 156 L 712 404 L -10 404 Z" fill="#E8A35A" stroke="#0D0D0F" stroke-width="2"></path>
      {R.field(-10, 712, 190, 26, 503, rows=2)}
      {"".join(R.reaper("e2", x, 270 + r.uniform(-6, 6), 0.6, cloth=r.choice(["#8A6A4A", "#5A6E8A", "#C9A86A"]), woman=i % 3 == 2) for i, x in enumerate((340, 420, 500, 580, 660)))}
      {"".join(R.sheaf(x, 300, 0.9) for x in (380, 460, 540, 620))}
      {R.field(-10, 712, 380, 40, 504, rows=1)}
      {R.gleaner(160, 380, 1.4)}'''
    o2 = cap("And she went, and came and gleaned in the field after the reapers: and her hap was to light on the portion of the field belonging unto Boaz, who was of the family of Elimelech.", "left: 12px; top: 12px", maxw=380)
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 702, 394, s2, o2, "2 · The field of Boaz")

    s3 = f'''      {face(FX["__FACE_BOAZ__"], -60, 20, 0.72)}'''
    o3 = (cap("And, behold, Boaz came from Beth-lehem, and said unto the reapers,", "left: 140px; top: 8px", size=9.5, maxw=190)
          + tail(118, 186, "l")
          + balloon("Jehovah be with you.", "left: 152px; top: 150px", 170, size=14, pad="16px 14px")
          + cap("And they answered him, Jehovah bless thee.", "left: 10px; bottom: 10px", size=9.5))
    P3a = panel("radial-gradient(circle at 30% 50%, #FFF4C2 0 20px, #FFC14D 150px, #8A5A30 330px)", 342, 294, s3, o3, "3a · Jehovah be with you")
    s4 = f'''      {defs("e4", "Man", "ManUp", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M-10 170 L 352 170 L 352 304 L -10 304 Z" fill="#E8A35A"></path>
      {R.field(-10, 352, 200, 26, 505, rows=2)}
      {person("e4", 70, 290, 0.66, **BOAZ, up=[(-22, -158), (-50, -164), (-80, -170)], flip=True)}
      {person("e4", 140, 292, 0.6, body="#2A140C", cloth="#8A6A4A", kind="Tunic", sw=4, flip=True)}
      {R.gleaner(290, 270, 0.7)}'''
    o4 = (cap("Then said Boaz unto his servant that was set over the reapers,", "left: 10px; top: 8px", size=9.5, maxw=320)
          + balloon("Whose damsel is this?", "left: 30px; top: 66px", 190, size=15, pad="16px 16px"))
    P3b = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 342, 294, s4, o4, "3b · Whose damsel is this?")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Ruth 2:2–5 — The Field of Boaz", "300px minmax(0, 1fr) 300px", body, 5)
PAGES["RU1-P05-Field"] = p05


# ───────────────────────── 06 · Under Whose Wings (2:8–17) ─────────────────────────
def p06():
    s1 = f'''      {face(FX["__FACE_BOAZ__"], -50, 10, 0.8)}'''
    o1 = (cap("Then said Boaz unto Ruth,", "right: 12px; top: 12px", size=10)
          + tail(250, 170, "l")
          + balloon("Hearest thou not, my daughter? Go not to glean in another field, neither pass from hence, but abide here fast by my maidens.", "left: 290px; top: 60px", 390, size=15, pad="22px 40px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 30px, #FFC14D 200px, #8A5A30 460px)", 702, 274, s1, o1, "1 · Hearest thou not, my daughter?")

    s2 = f'''      {defs("f2", "Man", "Robe")}
      <path d="M-10 200 L 352 200 L 352 304 L -10 304 Z" fill="#E8A35A"></path>
      {R.field(-10, 352, 220, 20, 601, rows=1)}
      {person("f2", 260, 280, 0.72, **BOAZ, flip=True)}
      {N.prostrate(110, 284, 0.9, color="#C2456A", skin="#3A1E14")}'''
    o2 = cap("Then she fell on her face, and bowed herself to the ground, and said unto him,", "left: 10px; top: 10px", size=10, maxw=320)
    P2a = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 342, 294, s2, o2, "2a · She fell on her face")
    s3 = f'''      {face(FX["__FACE_RUTH__"], 412, 30, 0.72, flip=True)}'''
    o3 = (tail(194, 196, "r")
          + balloon("Why have I found favor in thy sight, that thou shouldest take knowledge of me, seeing I am a foreigner?", "left: 8px; top: 60px", 196, size=12.5, pad="22px 18px"))
    P2b = panel("radial-gradient(circle at 70% 50%, #FFF4C2 0 20px, #C2456A 150px, #4A1D55 330px)", 342, 294, s3, o3, "2b · Seeing I am a foreigner")

    wings = (f'<g transform="translate(240 400) scale(1.6)"><path d="{N.ladder.WING}" fill="#FFF4C2" stroke="#E8B830" stroke-width="2"></path>'
             f'<path d="{N.ladder.WING}" transform="scale(-1 1)" fill="#FFF4C2" stroke="#E8B830" stroke-width="2"></path></g>')
    s4 = f'''      {defs("f4", "Woman", "Hair", "Robe")}
      {V.rays(240, 120, 36, 40, 600, color="#FFF4C2", op=0.35)}
      {wings}
      <path d="M-10 330 L 712 330 L 712 414 L -10 414 Z" fill="#8A5A30"></path>
      {person("f4", 240, 330, 0.62, **RUTH)}
      {R.sack(560, 392, 1.3)}
      {R.sheaf(620, 396, 1.1)}{R.sheaf(660, 400, 1.0)}'''
    o4 = (tail(420, 160, "l")
          + balloon("Jehovah recompense thy work, and a full reward be given thee of Jehovah, the God of Israel, under whose wings thou art come to take refuge.", "left: 450px; top: 14px", 240, size=13, pad="22px 24px")
          + cap("So she gleaned in the field until even; and she beat out that which she had gleaned, and it was about an ephah of barley.", "left: 12px; bottom: 12px", size=10.5, maxw=330)
          + ref("RUTH 2:12, 17", "right: 12px; bottom: 9px"))
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 50%, #FFC14D 100%)", 702, 404, s4, o4, "3 · Under whose wings")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Ruth 2:8–17 — Under Whose Wings", "280px 300px minmax(0, 1fr)", body, 6)
PAGES["RU1-P06-Wings"] = p06


# ───────────────────────── 07 · The Threshing-floor (3:2–11) ─────────────────────────
def p07():
    s1 = f'''      {face(FX["__FACE_NAOMI__"], -50, 10, 0.8)}'''
    o1 = (tail(250, 160, "l")
          + balloon("And now is not Boaz our kinsman, with whose maidens thou wast? Behold, he winnoweth barley to-night in the threshing-floor.", "left: 290px; top: 40px", 390, size=15, pad="22px 40px")
          + stamp(3, "right: 16px; bottom: 14px") + ref("NAOMI", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFE680 0 30px, #8A5A30 200px, #2A1A2E 460px)", 702, 274, s1, o1, "1 · The threshing-floor")

    s2 = f'''      {stars(90, 702, 260, 701)}
      {J.moon(600, 70, 30)}
      <path d="M-10 300 L 712 300 L 712 434 L -10 434 Z" fill="#3A2A2E" stroke="#0D0D0F" stroke-width="2"></path>
      <ellipse cx="351" cy="330" rx="330" ry="40" fill="#5A4A3E" stroke="#0D0D0F" stroke-width="2"></ellipse>
      {R.heap(200, 330, 260, 110)}
      {G.rug_sleeper(420, 344, 1.0, color="#5A6E8A", flip=False)}
      {N.prostrate(300, 352, 0.5, color="#C2456A", skin="#3A1E14", flip=True)}'''
    o2 = (cap("And when Boaz had eaten and drunk, and his heart was merry, he went to lie down at the end of the heap of grain: and she came softly, and uncovered his feet, and laid her down.", "left: 12px; top: 12px", maxw=360)
          + cap("And it came to pass at midnight, that the man was afraid, and turned himself; and, behold, a woman lay at his feet.", "right: 12px; bottom: 12px", size=10.5, maxw=330))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 424, s2, o2, "2 · At midnight")

    s3 = f'''      {face(FX["__FACE_RUTH__"], -70, 30, 0.7)}'''
    o3 = (cap("And he said, Who art thou? And she answered,", "left: 10px; top: 8px", size=9.5, maxw=320)
          + tail(116, 196, "l")
          + balloon("I am Ruth thy handmaid: spread therefore thy skirt over thy handmaid; for thou art a near kinsman.", "left: 150px; top: 70px", 186, size=12, pad="22px 16px"))
    P3a = panel("radial-gradient(circle at 30% 55%, #E8C8A0 0 20px, #4A3A6A 160px, #05050A 330px)", 342, 294, s3, o3, "3a · I am Ruth thy handmaid")
    s4 = f'''      {face(FX["__FACE_BOAZ__"], 412, 30, 0.7, flip=True)}'''
    o4 = (tail(196, 200, "r")
          + balloon("And now, my daughter, fear not; I will do to thee all that thou sayest; for all the city of my people doth know that thou art a worthy woman.", "left: 8px; top: 30px", 196, size=11.5, pad="24px 18px"))
    P3b = panel("radial-gradient(circle at 70% 55%, #E8C8A0 0 20px, #5A6E8A 160px, #05050A 330px)", 342, 294, s4, o4, "3b · A worthy woman")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Ruth 3:2–11 — The Threshing-floor", "280px minmax(0, 1fr) 300px", body, 7)
PAGES["RU1-P07-Threshing"] = p07


# ───────────────────────── 08 · Obed (4:9–17) ─────────────────────────
def p08():
    s1 = f'''      {defs("g1", "Man", "ManUp", "Robe", "Tunic")}
      {J.jericho(-10, 712, 100, 250, 801, color="#E8C88A", towers=2, houses=True)}
      <path d="M280 250 L 280 160 C 280 120 420 120 420 160 L 420 250 Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("g1", 350, 296, 0.66, **BOAZ, up=[(-22, -158), (-50, -190), (-60, -224)])}
      {"".join(E.kneel(x, 290, 0.44, color=c, flip=x > 350) for x, c in [(120, "#5A6E8A"), (180, "#8A6A4A"), (240, "#C9A86A"), (470, "#8A6A4A"), (530, "#5A6E8A"), (590, "#4A3A6A")])}'''
    o1 = (cap("And Boaz said unto the elders, and unto all the people,", "left: 12px; top: 12px", size=10, maxw=240)
          + balloon("Ye are witnesses this day, that I have bought all that was Elimelech's, and all that was Chilion's and Mahlon's, of the hand of Naomi.", "right: 14px; top: 12px", 380, size=12.5, pad="20px 40px")
          + stamp(4, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · Ye are witnesses this day")

    s2 = f'''      {defs("g2", "Man", "Woman", "WomanUp", "Hair", "Robe")}
      {J.sun(171, 100, 40)}
      <path d="M-10 230 L 352 230 L 352 304 L -10 304 Z" fill="#C8A06A"></path>
      {person("g2", 120, 290, 0.66, **BOAZ)}
      {person("g2", 200, 292, 0.62, **RUTH)}'''
    o2 = cap("So Boaz took Ruth, and she became his wife; and he went in unto her, and Jehovah gave her conception, and she bare a son.", "left: 10px; top: 8px", size=9.5, maxw=320)
    P2a = panel("linear-gradient(180deg, #C2456A 0%, #FFC14D 100%)", 342, 294, s2, o2, "2a · Boaz took Ruth")
    s3 = f'''      {defs("g3", "Woman", "WomanUp", "Hair", "Robe")}
      {V.rays(171, 170, 30, 30, 400, color="#FFF4C2", op=0.4)}
      <path d="M-10 250 L 352 250 L 352 304 L -10 304 Z" fill="#8A5A30"></path>
      {R.naomi_with_child("g3", 171, 300, 0.9)}'''
    o3 = cap("And Naomi took the child, and laid it in her bosom, and became nurse unto it.", "left: 10px; top: 8px", size=9.5, maxw=320)
    P2b = panel("radial-gradient(circle at 50% 55%, #FFF4C2 0 30px, #FFC14D 150px, #C2456A 330px)", 342, 294, s3, o3, "2b · Naomi took the child")

    s4 = f'''      {V.rays(160, 200, 30, 60, 600, color="#FFF4C2", op=0.35)}
      {face(FX["__FACE_NAOMI_JOY__"], -50, 10, 0.8)}'''
    o4 = (cap("And the women her neighbors gave it a name, saying, There is a son born to Naomi; and they called his name Obed: he is the father of Jesse, the father of David.", "left: 290px; top: 20px", size=12, maxw=390)
          + '    <div style="position: absolute; left: 290px; top: 170px; display: flex; align-items: center; gap: 10px; font-family: Anton, \'Archivo Narrow\', sans-serif; font-size: 30px; color: #12113A; letter-spacing: 0.04em">OBED <span style="color: #C2456A">›</span> JESSE <span style="color: #C2456A">›</span> DAVID</div>\n'
          + end_mark("END OF RUTH", "right: 14px; bottom: 12px"))
    P3 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 30px, #FFE680 200px, #FFC14D 460px)", 702, 394, s4, o4, "3 · The father of David")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Ruth 4:9–17 — Obed", "300px 300px minmax(0, 1fr)", body, 8)
PAGES["RU1-P08-Obed"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "ruth/project"))
