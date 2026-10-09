"""1 Samuel Book Two — The Battle Is Jehovah's (1 Samuel 16–31). Writes the .dc.html pages into the given folder.
Usage: python3 samuel_book2.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus4 as Z, exodus5 as V, joshua1 as J, judges2 as S, samuel1 as A, samuel2 as B
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
from judges_book1 import shout
from judges_book2 import end_mark
from samuel_book1 import D, SAMUEL, philistine, fleeing, shouting
FX = B.tokens()
PAGES = {}
SAUL = dict(body="#2A140C", cloth="#8A1E2E", kind="Tunic", sw=4)
JONATHAN = dict(body="#3A1E14", cloth="#1F5FAD", kind="Tunic", sw=4)
KING = B.crown(0, -194, 0.42)
SEPIA = "#E8C890"


def brothers(p, xs, y, s, seed):
    r = random.Random(seed)
    return "".join(person(p, x, y, round(s * r.uniform(0.92, 1.0), 3), body="#3A1E14", cloth=r.choice(["#5A6E8A", "#8A6A4A", "#3F8A44", "#C9A86A", "#4A3A6A", "#B5652E"]), kind="Tunic", sw=4) for x in xs)


def army(p, n, x0, x1, y0, y1, seed, smin, smax):
    """Israel's army: men in tunics with spears."""
    r = random.Random(seed); o = []
    for y, x in sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)):
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        o.append(person(p, round(x), round(y), round(s, 3), body="#2A140C", cloth=r.choice(["#8A6A4A", "#5A6E8A", "#C9A86A", "#3F8A44"]), kind="Tunic", sw=4, extra=Z.SPEAR))
    return "".join(o)


# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {D("c1")}
    {J.sun(560, 520, 90)}
    {V.rays(560, 520, 40, 100, 900, color="#FFF4C2", op=0.18)}
    {hills(760, "#7A3A2A", 1101, 60, 760)}
    <path d="M-10 900 C 200 880 500 900 770 890 L 770 1090 L -10 1090 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
    {B.goliath("c1", 520, 1010, 3.0)}
    {B.david("c1", 170, 1040, 1.5, whirl=True)}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The First Book of</span>
    <span>No. 02</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 124px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6">SAMUEL</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Two — The Battle Is Jehovah's</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 16 – 31</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.04; color: #F3EFE6"><span>サ</span><span>ム</span><span>エ</span><span>ル</span><span>記</span><span>上</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">SAMUERU-KI JŌ</span>
  </div>
  <div style="position: absolute; left: 38px; top: 322px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">for the battle is Jehovah's,</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 2</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #2A0A1A 0%, #8A1E2E 30%, #D7261E 55%, #FF8A3D 80%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("1 Samuel Book Two — Cover", None, body, root_style=root)
PAGES["SA2-Cover"] = cover


# ───────────────────────── 01 · The Youngest (16:1–11) ─────────────────────────
def p01():
    s1 = f'''      {D("a1")}
      {hills(170, "#8A9A5A", 1201, 30)}
      <path d="M-10 190 L 712 190 L 712 254 L -10 254 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("a1", 90, 232, 0.66, **SAMUEL, up=[(-22, -158), (-14, -128), (6, -124)], extra=A.vial(8, -118, 0.7, rot=10))}'''
    o1 = (cap("And Jehovah said unto Samuel,", "left: 160px; top: 12px", size=10)
          + god("fill thy horn with oil, and go: I will send thee to Jesse the Beth-lehemite; for I have provided me a king among his sons.", "left: 160px; top: 48px", size=16, maxw=400)
          + stamp(16, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 244, s1, o1, "1 · Fill thy horn with oil")

    s2 = f'''      {D("a2")}
      {J.city_hill(560, 150, 200, 80, 1202)}
      <path d="M-10 150 L 712 150 L 712 474 L -10 474 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {brothers("a2", [330, 380, 430, 480, 530, 580], 330, 0.62, 1203)}
      {person("a2", 250, 446, 1.15, body="#3A1E14", cloth="#5A6E8A", kind="Tunic", sw=4)}
      {person("a2", 90, 450, 0.92, **SAMUEL)}'''
    o2 = (cap("And it came to pass, when they were come, that he looked on Eliab, and said, Surely Jehovah's anointed is before him.", "left: 12px; top: 12px", size=10.5, maxw=300)
          + cap("But Jehovah said unto Samuel,", "right: 12px; top: 120px", size=10)
          + god("Look not on his countenance, or on the height of his stature; because I have rejected him: for Jehovah seeth not as man seeth; for man looketh on the outward appearance, but Jehovah looketh on the heart.", "right: 12px; top: 156px", size=17, maxw=360)
          + ref("ELIAB", "left: 222px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 464, s2, o2, "2 · Jehovah looketh on the heart")

    s3 = f'''      {face(FX["__FACE_JESSE__"], -50, 20, 0.74)}'''
    o3 = (cap("And Samuel said unto Jesse, Are here all thy children? And he said,", "right: 10px; top: 10px", size=9.5, maxw=170)
          + balloon("There remaineth yet the youngest, and, behold, he is keeping the sheep.", "right: 10px; bottom: 16px", 180, size=12.5, pad="20px 18px"))
    P3a = panel("radial-gradient(circle at 30% 50%, #FFE3B8 0 20px, #C9A86A 150px, #5A3A22 330px)", 342, 294, s3, o3, "3a · The youngest")
    r = random.Random(4)
    s4 = f'''      {D("a4")}
      {J.sun(260, 120, 40)}
      {hills(170, "#6A8A4A", 1204, 40, 342)}
      <path d="M-10 220 L 352 220 L 352 304 L -10 304 Z" fill="#8A9A5A"></path>
      {"".join(E.sheep(r.uniform(20, 320), r.uniform(230, 290), 0.36, flip=r.random() < 0.5) for _ in range(9))}
      {B.david("a4", 120, 276, 0.6)}'''
    o4 = ref("DAVID", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P3b = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 60%, #FFE3B8 100%)", 342, 294, s4, o4, "3b · Keeping the sheep")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("1 Samuel 16:1–11 — The Youngest", "250px minmax(0, 1fr) 300px", body, 1)
PAGES["SA2-P01-Youngest"] = p01


# ───────────────────────── 02 · Arise, Anoint Him (16:12–23) ─────────────────────────
def p02():
    s1 = f'''      {V.rays(160, 160, 36, 40, 700, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_DAVID__"], -40, 0, 0.86)}'''
    o1 = (cap("And he sent, and brought him in. Now he was ruddy, and withal of a beautiful countenance, and goodly to look upon.", "right: 12px; top: 12px", size=11, maxw=330)
          + cap("And Jehovah said,", "right: 12px; top: 130px", size=10)
          + god("Arise, anoint him; for this is he.", "right: 12px; top: 166px", size=24, maxw=300))
    P1 = panel("radial-gradient(circle at 25% 50%, #FFF4C2 0 30px, #FFC14D 200px, #C2456A 460px)", 702, 324, s1, o1, "1 · This is he")

    s2 = f'''      {D("b2")}
      {V.rays(330, -40, 40, 40, 800, color="#FFF4C2", op=0.35)}
      <path d="M-10 330 L 712 330 L 712 414 L -10 414 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {brothers("b2", [60, 120, 180, 540, 600, 660], 380, 0.66, 1205)}
      {B.david("b2", 320, 390, 0.95, staff=False, bag=False)}
      {person("b2", 430, 392, 1.0, **SAMUEL, up=[(-22, -158), (-50, -200), (-80, -228)])}
      {A.vial(342, 172, 1.2, rot=-140, pour=24)}
      {A.drops(322, 196, 8, 1206, spread=14)}'''
    o2 = cap("Then Samuel took the horn of oil, and anointed him in the midst of his brethren: and the Spirit of Jehovah came mightily upon David from that day forward.", "left: 12px; top: 12px", size=11, maxw=420)
    P2 = panel("radial-gradient(circle at 47% 30%, #FFF4C2 0 40px, #FFD23F 200px, #B5652E 460px)", 702, 404, s2, o2, "2 · In the midst of his brethren")

    s3 = f'''      {D("b3")}
      <path d="M-10 -10 L 712 -10 L 712 264 L -10 264 Z" fill="#4A1D55"></path>
      {face(FX["__FACE_SAUL_MAD__"], -40, -50, 0.62)}
      <path d="M-10 240 L 712 240 L 712 264 L -10 264 Z" fill="#2A1A2E"></path>
      {B.david("b3", 560, 246, 0.9, staff=False, up=[(-22, -158), (-30, -128), (-6, -118)], extra=B.harp(2, -96, 0.6))}
      {"".join(f'<path d="M{x} {y} c 10 -10 20 10 30 0" fill="none" stroke="#FFD23F" stroke-width="2.4"></path>' for x, y in [(450, 90), (420, 130), (470, 160)])}'''
    o3 = cap("And it came to pass, when the evil spirit from God was upon Saul, that David took the harp, and played with his hand: so Saul was refreshed, and was well, and the evil spirit departed from him.", "left: 240px; top: 12px", size=10, maxw=230)
    P3 = panel("#4A1D55", 702, 254, s3, o3, "3 · David took the harp")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 16:12–23 — Arise, Anoint Him", "330px minmax(0, 1fr) 260px", body, 2)
PAGES["SA2-P02-Anoint"] = p02


# ───────────────────────── 03 · Goliath of Gath (17:4–11) ─────────────────────────
def p03():
    s1 = f'''      {D("c1")}
      {hills(230, "#7A3A2A", 1301, 40)}
      {S.philistines("c1", 16, 400, 712, 230, 270, 1302, 0.18, 0.26)}
      <path d="M-10 270 L 712 270 L 712 504 L -10 504 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {B.goliath("c1", 470, 488, 2.0)}'''
    o1 = (cap("And there went out a champion out of the camp of the Philistines, named Goliath, of Gath, whose height was six cubits and a span.", "left: 12px; top: 12px", size=12, maxw=300)
          + cap("And he had a helmet of brass upon his head, and he was clad with a coat of mail; and the weight of the coat was five thousand shekels of brass.", "left: 12px; top: 150px", size=10.5, maxw=260)
          + stamp(17, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #5A1A16 0%, #D7261E 45%, #FF8A3D 100%)", 702, 494, s1, o1, "1 · A champion")

    s2 = f'''      {mk.speed(520, 140, 50, 140, 600, 1303, color="#FFD23F", op=0.4)}
      {face(FX["__FACE_GOLIATH__"], 760, -30, 0.7, flip=True)}'''
    o2 = (cap("And the Philistine said,", "left: 12px; top: 12px", size=10)
          + tail(380, 120, "r")
          + balloon("I defy the armies of Israel this day; give me a man, that we may fight together.", "left: 20px; top: 48px", 360, size=19, pad="26px 38px")
          + sfx("ウオォ", "UOOH", "left: 30px; bottom: 16px", size=34, fill="#FFD23F", stroke="#0D0D0F", rot=-6, align="flex-start"))
    P2 = panel("radial-gradient(circle at 75% 50%, #FFD23F 0 30px, #D7261E 200px, #2A0A0A 460px)", 702, 274, s2, o2, "2 · I defy the armies of Israel")

    s3 = f'''      {D("c3")}
      {hills(110, "#6A8A4A", 1304, 40)}
      <path d="M-10 150 L 712 150 L 712 224 L -10 224 Z" fill="#8A9A5A" stroke="#0D0D0F" stroke-width="2"></path>
      {army("c3", 18, 240, 712, 150, 200, 1305, 0.28, 0.4)}
      {person("c3", 140, 206, 0.5, **SAUL, extra=KING)}'''
    o3 = cap("And when Saul and all Israel heard those words of the Philistine, they were dismayed, and greatly afraid.", "left: 12px; top: 12px", size=10.5, maxw=330)
    P3 = panel("linear-gradient(180deg, #5A6E8A 0%, #C8D0DE 100%)", 702, 214, s3, o3, "3 · Dismayed")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 17:4–11 — Goliath of Gath", "minmax(0, 1fr) 280px 220px", body, 3)
PAGES["SA2-P03-Goliath"] = p03


# ───────────────────────── 04 · The Living God (17:26–37) ─────────────────────────
def p04():
    s1 = f'''      {D("d1")}
      {hills(150, "#6A8A4A", 1401, 30)}
      <path d="M-10 180 L 712 180 L 712 254 L -10 254 Z" fill="#8A9A5A" stroke="#0D0D0F" stroke-width="2"></path>
      {army("d1", 6, 480, 700, 220, 240, 1402, 0.42, 0.5)}
      {B.david("d1", 410, 240, 0.56)}'''
    o1 = (cap("And David spake to the men that stood by him, saying,", "left: 12px; top: 12px", size=10, maxw=220)
          + balloon("What shall be done to the man that killeth this Philistine, and taketh away the reproach from Israel? for who is this uncircumcised Philistine, that he should defy the armies of the living God?", "left: 12px; top: 58px", 360, size=12.5, pad="20px 38px")
          + tail(370, 120, "r"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 244, s1, o1, "1 · The living God")

    s2 = f'''      {face(FX["__FACE_DAVID_BOLD__"], -50, 20, 0.74)}'''
    o2 = (cap("And David said to Saul,", "right: 10px; top: 10px", size=10)
          + balloon("Let no man's heart fail because of him; thy servant will go and fight with this Philistine.", "right: 8px; bottom: 14px", 180, size=12.5, pad="20px 18px"))
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #FF8A3D 150px, #8A1E2E 330px)", 342, 294, s2, o2, "2a · Thy servant will go")
    s3 = f'''      {face(FX["__FACE_SAUL_KING__"], 392, 20, 0.74, flip=True)}'''
    o3 = (cap("And Saul said to David,", "left: 10px; top: 10px", size=10)
          + balloon("Thou art not able to go against this Philistine to fight with him; for thou art but a youth, and he a man of war from his youth.", "left: 8px; bottom: 12px", 190, size=11.5, pad="22px 20px"))
    P2b = panel("radial-gradient(circle at 70% 50%, #C8D0DE 0 20px, #5A6E8A 150px, #12113A 330px)", 342, 294, s3, o3, "2b · But a youth")

    r = random.Random(9)
    s4 = f'''      {D("d4")}
      <path d="M-10 190 L 712 190 L 712 264 L -10 264 Z" fill="#B59A6A" stroke="#5A3A22" stroke-width="2"></path>
      {"".join(E.sheep(r.uniform(20, 200), r.uniform(200, 240), 0.4, flip=True) for _ in range(5))}
      {S.lion(400, 236, 0.9, flip=True)}
      {E.sheep(330, 220, 0.34)}
      {B.david("d4", 560, 244, 0.86, staff=False, up=[(-22, -158), (-60, -150), (-96, -140)])}
      <rect x="-10" y="-10" width="722" height="284" fill="#8A5A30" opacity="0.18"></rect>'''
    o4 = cap("Thy servant was keeping his father's sheep; and when there came a lion, or a bear, and took a lamb out of the flock, I went out after him, and smote him, and delivered it out of his mouth;", "left: 12px; top: 12px", size=10.5, maxw=430)
    P3 = panel(f"linear-gradient(180deg, {SEPIA} 0%, #F3E0B8 100%)", 702, 254, s4, o4, "3 · The lion")

    s5 = f'''      {V.rays(560, 80, 30, 30, 500, color="#FFF4C2", op=0.3)}'''
    o5 = (balloon("Jehovah that delivered me out of the paw of the lion, and out of the paw of the bear, he will deliver me out of the hand of this Philistine.", "left: 12px; top: 10px", 380, size=12.5, pad="18px 34px")
          + cap("And Saul said unto David,", "right: 12px; top: 12px", size=10)
          + shout("Go, and Jehovah shall be with thee.", "right: 12px; top: 48px", size=20, maxw=270))
    P4 = panel("linear-gradient(90deg, #FFC14D 0%, #4A1D55 100%)", 702, 184, s5, o5, "4 · Go")
    body = P1 + cols(P2a, P2b) + P3 + P4
    return mk.page("1 Samuel 17:26–37 — The Living God", "250px 300px 260px minmax(0, 1fr)", body, 4)
PAGES["SA2-P04-LivingGod"] = p04


# ───────────────────────── 05 · Five Smooth Stones (17:38–40) ─────────────────────────
def p05():
    s1 = f'''      {D("e1")}
      {A.sanctuary(702, 294, 250, seed=15, glow=False)}
      {person("e1", 520, 286, 0.92, **SAUL, extra=KING)}
      {person("e1", 300, 288, 0.74, body="#5A2A16", cloth="#B08A3A", kind="Robe", sw=3, extra=B.MAIL + '<g transform="translate(0 -14) scale(1.25) translate(0 14)">' + B.HELMET + '</g>' + '<path d="M26 -110 L 40 -20" stroke="#8A8A9A" stroke-width="5"></path>')}'''
    o1 = (cap("And Saul clad David with his apparel, and he put a helmet of brass upon his head, and he clad him with a coat of mail.", "left: 12px; top: 12px", size=10, maxw=250)
          + balloon("I cannot go with these; for I have not proved them.", "right: 12px; top: 14px", 220, size=14, pad="18px 22px")
          + cap("And David put them off him.", "right: 12px; bottom: 12px", size=10)
          + sfx("ガチャ", "GACHA", "left: 330px; top: 30px", size=28, fill="#F3EFE6", stroke="#0D0D0F", rot=8))
    P1 = panel("#3A2214", 702, 294, s1, o1, "1 · I cannot go with these")

    s2 = f'''      {D("e2")}
      {hills(80, "#6A8A4A", 1501, 30)}
      <path d="M-10 110 L 712 110 L 712 264 L -10 264 Z" fill="#C8A06A"></path>
      {B.brook(-10, 712, 150, 70, 1502)}
      {E.kneel(130, 166, 0.66, color="#C9A86A", skin="#5A2A16")}
      {B.stones(300, 176, 5, 2.4, seed=1503)}'''
    o2 = (cap("and chose him five smooth stones out of the brook,", "left: 12px; top: 12px", size=12)
          + badge("五", "right: 14px; top: 14px", size=30))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 254, s2, o2, "2 · Five smooth stones")

    s3 = f'''      {D("e3")}
      {J.sun(560, 90, 40)}
      {hills(170, "#8A3A2A", 1504, 40)}
      {S.philistines("e3", 10, 420, 712, 190, 210, 1505, 0.14, 0.18)}
      {B.goliath("e3", 560, 250, 0.42)}
      <path d="M-10 230 C 200 260 500 240 712 236 L 712 434 L -10 434 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {B.david("e3", 180, 410, 1.1)}'''
    o3 = (cap("And he took his staff in his hand, and chose him five smooth stones out of the brook, and put them in the shepherd's bag which he had, even in his wallet; and his sling was in his hand: and he drew near to the Philistine.", "right: 12px; top: 270px", size=11, maxw=380))
    P3 = panel("linear-gradient(180deg, #8A1E2E 0%, #FF8A3D 60%, #FFC14D 100%)", 702, 424, s3, o3, "3 · He drew near")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 17:38–40 — Five Smooth Stones", "300px 260px minmax(0, 1fr)", body, 5)
PAGES["SA2-P05-Stones"] = p05


# ───────────────────────── 06 · In the Name of Jehovah (17:42–47) ─────────────────────────
def p06():
    s1 = f'''      {D("f1")}
      <path d="M-10 250 L 712 250 L 712 294 L -10 294 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {B.goliath("f1", 560, 300, 1.5)}
      {B.david("f1", 120, 280, 0.6)}'''
    o1 = (cap("And when the Philistine looked about, and saw David, he disdained him; for he was but a youth, and ruddy, and withal of a fair countenance.", "left: 12px; top: 12px", size=10, maxw=290)
          + cap("And the Philistine said unto David,", "left: 190px; top: 140px", size=9.5)
          + balloon("Am I a dog, that thou comest to me with staves?", "left: 200px; top: 176px", 220, size=13.5, pad="16px 22px")
          + tail(420, 186, "r"))
    P1 = panel("linear-gradient(180deg, #2A0A0A 0%, #8A1E2E 60%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · Am I a dog")

    s2 = f'''      {V.rays(160, 170, 36, 40, 700, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_DAVID_BOLD__"], -40, 10, 0.86)}'''
    o2 = (cap("Then said David to the Philistine,", "right: 12px; top: 12px", size=10)
          + tail(320, 200, "l")
          + balloon("Thou comest to me with a sword, and with a spear, and with a javelin: but I come to thee in the name of Jehovah of hosts, the God of the armies of Israel, whom thou hast defied.", "left: 360px; top: 46px", 330, size=15, pad="30px 34px"))
    P2 = panel("radial-gradient(circle at 25% 50%, #FFF4C2 0 40px, #FFC14D 200px, #D7261E 460px)", 702, 324, s2, o2, "2 · In the name of Jehovah")

    s3 = f'''      {D("f3")}
      {J.sun(351, 200, 70)}
      {V.rays(351, 200, 40, 70, 800, color="#FFF4C2", op=0.25)}
      {hills(230, "#5A2A1E", 1601, 40)}
      <path d="M-10 270 C 200 300 500 300 712 270 L 712 394 L -10 394 Z" fill="#8A4A22" stroke="#0D0D0F" stroke-width="2"></path>
      {army("f3", 10, -10, 160, 250, 280, 1602, 0.16, 0.22)}
      {S.philistines("f3", 10, 560, 712, 250, 280, 1603, 0.16, 0.22)}
      {B.david("f3", 280, 340, 0.36)}
      {B.goliath("f3", 440, 344, 0.62)}'''
    o3 = (cap("and that all this assembly may know that Jehovah saveth not with sword and spear:", "left: 12px; top: 12px", size=10.5, maxw=330)
          + shout("for the battle is Jehovah's,", "right: 14px; top: 14px", size=28, maxw=300)
          + cap("and he will give you into our hand.", "right: 12px; bottom: 12px", size=10))
    P3 = panel("linear-gradient(180deg, #2A0A1A 0%, #D7261E 50%, #FFC14D 100%)", 702, 394, s3, o3, "3 · The battle is Jehovah's")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 17:42–47 — In the Name of Jehovah", "300px 330px minmax(0, 1fr)", body, 6)
PAGES["SA2-P06-Name"] = p06


# ───────────────────────── 07 · A Sling and a Stone (17:48–51) ─────────────────────────
def p07():
    s1 = f'''      {D("g1")}
      {mk.speed(351, 130, 60, 160, 600, 1701, color="#F3EFE6", op=0.5)}
      <path d="M-10 220 L 712 220 L 712 264 L -10 264 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(f'<ellipse cx="{x}" cy="230" rx="{18 + i * 6}" ry="8" fill="#E8C88A" opacity="0.6"></ellipse>' for i, x in enumerate([200, 160, 120]))}
      {B.david("g1", 300, 246, 0.9, whirl=True)}'''
    o1 = (cap("that David hastened, and ran toward the army to meet the Philistine.", "right: 12px; top: 12px", size=11, maxw=300)
          + sfx("ヒュン", "HYUN HYUN", "left: 40px; top: 40px", size=36, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start"))
    P1 = panel("linear-gradient(90deg, #FFC14D 0%, #D7261E 100%)", 702, 254, s1, o1, "1 · David hastened")

    s2 = f'''      {mk.speed(560, 120, 70, 60, 700, 1702, color="#FFD23F", op=0.5)}
      {B.flying_stone(500, 120, 2.6)}'''
    o2 = (cap("And David put his hand in his bag, and took thence a stone, and slang it, and smote the Philistine in his forehead;", "left: 12px; top: 12px", size=10.5, maxw=330)
          + sfx("ガッ", "GAKK", "right: 30px; bottom: 30px", size=56, fill="#FFD23F", stroke="#0D0D0F", rot=6))
    P2 = panel("radial-gradient(circle at 75% 50%, #FFF4C2 0 30px, #D7261E 200px, #12113A 460px)", 702, 244, s2, o2, "2 · The stone")

    s3 = f'''      {hills(150, "#5A2A1E", 1703, 30)}
      <path d="M-10 180 L 712 180 L 712 274 L -10 274 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#E8C88A" opacity="0.55"></ellipse>' for x, y, rx, ry in [(250, 230, 150, 30), (420, 236, 140, 26), (340, 210, 100, 24)])}
      {B.goliath_fallen(340, 246, 1.3)}'''
    o3 = (cap("and the stone sank into his forehead, and he fell upon his face to the earth.", "left: 12px; top: 12px", size=12, maxw=420)
          + sfx("ズゥン", "ZUUN", "right: 30px; top: 24px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=-4))
    P3 = panel("linear-gradient(180deg, #8A1E2E 0%, #FF8A3D 100%)", 702, 264, s3, o3, "3 · He fell upon his face")

    s4 = f'''      {D("g4")}
      {hills(120, "#5A2A1E", 1704, 30)}
      <path d="M-10 150 L 712 150 L 712 224 L -10 224 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {S.philistines("g4", 14, 340, 712, 150, 200, 1705, 0.24, 0.34, flip=True, spear=False)}'''
    o4 = (cap("So David prevailed over the Philistine with a sling and with a stone,", "left: 12px; top: 12px", size=11, maxw=300)
          + cap("And when the Philistines saw that their champion was dead, they fled.", "left: 12px; bottom: 12px", size=10, maxw=300))
    P4 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 224, s4, o4, "4 · They fled")
    body = P1 + P2 + P3 + P4
    return mk.page("1 Samuel 17:48–51 — A Sling and a Stone", "260px 250px 270px minmax(0, 1fr)", body, 7)
PAGES["SA2-P07-Stone"] = p07


# ───────────────────────── 08 · Jonathan; Saul's Spear (18:1–11) ─────────────────────────
def p08():
    drape = '<path d="M-74 -150 L -96 -150 L -100 -70 L -80 -64 L -70 -80 Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></path><path d="M-94 -140 L -96 -76" stroke="#E8B830" stroke-width="2"></path>'
    s1 = f'''      {D("h1")}
      {V.rays(351, 80, 30, 40, 600, color="#FFF4C2", op=0.3)}
      <path d="M-10 230 L 712 230 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {B.david("h1", 280, 290, 0.92, staff=False, bag=False)}
      {person("h1", 440, 292, 0.96, **JONATHAN, up=[(-22, -158), (-50, -152), (-74, -150)], extra=drape)}'''
    o1 = (cap("that the soul of Jonathan was knit with the soul of David, and Jonathan loved him as his own soul.", "left: 12px; top: 12px", size=11, maxw=300)
          + stamp(18, "right: 16px; top: 14px")
          + ref("JONATHAN", "right: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · Knit with the soul of David")

    s2 = f'''      {face(FX["__FACE_JONATHAN__"], -50, 10, 0.74)}'''
    o2 = cap("Then Jonathan and David made a covenant, because he loved him as his own soul.", "right: 10px; top: 10px", size=10, maxw=160)
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #2C9DB8 150px, #12113A 330px)", 342, 274, s2, o2, "2a · A covenant")
    s3 = f'''      <path d="M40 200 L 300 200 L 290 250 L 50 250 Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M60 214 L 280 214" stroke="#E8B830" stroke-width="3"></path>
      <path d="M70 180 L 270 150" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path><path d="M70 180 L 270 150" stroke="#C8C2D6" stroke-width="5" stroke-linecap="round"></path>
      <path d="M60 182 L 90 178 M74 170 L 78 192" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>
      <path d="M90 110 C 170 60 250 70 300 130" fill="none" stroke="#0D0D0F" stroke-width="8"></path><path d="M90 110 C 170 60 250 70 300 130" fill="none" stroke="#8A5A30" stroke-width="5"></path>
      <path d="M90 110 L 300 130" stroke="#F3EFE6" stroke-width="1.6"></path>
      <path d="M30 260 C 120 240 220 270 320 250" fill="none" stroke="#0D0D0F" stroke-width="10"></path><path d="M30 260 C 120 240 220 270 320 250" fill="none" stroke="#E8B830" stroke-width="6"></path>'''
    o3 = cap("And Jonathan stripped himself of the robe that was upon him, and gave it to David, and his apparel, even to his sword, and to his bow, and to his girdle.", "left: 10px; top: 10px", size=9.5, maxw=322)
    P2b = panel("linear-gradient(180deg, #F3E0B8 0%, #C9A86A 100%)", 342, 274, s3, o3, "2b · Robe, sword, bow and girdle")

    s4 = f'''      {D("h4")}
      <path d="M-10 -10 L 712 -10 L 712 414 L -10 414 Z" fill="#6A4A3A"></path>
      {"".join(f'<path d="M-10 {y} L 712 {y}" stroke="#4A3428" stroke-width="2"></path>' for y in range(30, 340, 40))}
      <path d="M-10 340 L 712 340 L 712 414 L -10 414 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
      {person("h4", 150, 396, 1.0, **SAUL, up=[(-22, -158), (-46, -196), (-30, -236)], extra=KING)}
      {mk.speed(150, 200, 20, 60, 200, 1801, color="#F3EFE6", op=0.4)}
      {B.spear_in_wall(560, 180, 1.0, rot=-6)}
      {E.kneel(560, 384, 0.7, color="#C9A86A", skin="#5A2A16", flip=True)}
      {B.harp(620, 384, 0.5, rot=30)}'''
    o4 = (cap("And Saul had his spear in his hand; and Saul cast the spear; for he said,", "left: 220px; top: 12px", size=10.5, maxw=280)
          + balloon("I will smite David even to the wall.", "left: 220px; top: 80px", 220, size=15, pad="18px 22px")
          + sfx("ドスッ", "DOSU", "right: 30px; top: 50px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=8)
          + cap("And David avoided out of his presence twice.", "right: 12px; bottom: 12px", size=10.5))
    P3 = panel("#6A4A3A", 702, 404, s4, o4, "3 · Saul cast the spear")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("1 Samuel 18:1–11 — Jonathan", "300px 280px minmax(0, 1fr)", body, 8)
PAGES["SA2-P08-Jonathan"] = p08


# ───────────────────────── 09 · The Cave (24:3–17) ─────────────────────────
def p09():
    s1 = f'''      {D("i1")}
      {B.cave(702, 464, 420, 230, 400, seed=1901)}
      {person("i1", 530, 398, 0.92, body="#1A1210", cloth="#5A1A22", kind="Robe", sw=3, extra=KING)}
      {E.kneel(330, 398, 0.62, color="#5A4A3A", skin="#3A1E14")}
      {B.knife(356, 336, 0.9, rot=-20)}
      {B.skirt_piece(460, 372, 1.2, color="#5A1A22")}
      {"".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#F3EFE6"></circle><circle cx="{x + 9}" cy="{y}" r="2.4" fill="#F3EFE6"></circle>' for x, y in [(60, 300), (130, 330), (200, 290), (90, 380), (250, 360)])}'''
    o1 = (cap("And he came to the sheepcotes by the way, where was a cave; and Saul went in to cover his feet. Now David and his men were abiding in the innermost parts of the cave.", "left: 12px; top: 12px", size=10.5, maxw=380)
          + cap("Then David arose, and cut off the skirt of Saul's robe privily.", "left: 12px; bottom: 12px", size=11, maxw=300)
          + stamp(24, "right: 16px; top: 14px"))
    P1 = panel("#1A1412", 702, 464, s1, o1, "1 · The skirt of Saul's robe")

    s2 = f'''      {face(FX["__FACE_DAVID_GRIEVED__"], -40, -30, 0.7)}'''
    o2 = (cap("And he said unto his men,", "left: 300px; top: 12px", size=10)
          + tail(270, 110, "l")
          + balloon("Jehovah forbid that I should do this thing unto my lord, Jehovah's anointed, to put forth my hand against him, seeing he is Jehovah's anointed.", "left: 310px; top: 44px", 370, size=14, pad="22px 38px"))
    P2 = panel("radial-gradient(circle at 25% 50%, #8FD0E2 0 30px, #2A3A6A 200px, #05050A 460px)", 702, 254, s2, o2, "2 · Jehovah forbid")

    s3 = f'''      {face(FX["__FACE_SAUL_WEEP__"], -50, 10, 0.74)}'''
    o3 = (cap("Is this thy voice, my son David? And Saul lifted up his voice, and wept.", "right: 10px; top: 10px", size=10, maxw=160))
    P3a = panel("radial-gradient(circle at 30% 50%, #C8D0DE 0 20px, #5A6E8A 150px, #12113A 330px)", 342, 274, s3, o3, "3a · Saul wept")
    s4 = f'''      {D("i4")}
      {hills(170, "#8A7A6A", 1902, 40, 342)}
      <path d="M-10 210 L 352 210 L 352 284 L -10 284 Z" fill="#A89A86"></path>
      {E.kneel(80, 260, 0.5, color="#C9A86A", skin="#5A2A16")}
      {person("i4", 270, 262, 0.62, **SAUL, extra=KING)}'''
    o4 = (cap("And he said to David,", "left: 10px; top: 10px", size=10)
          + balloon("Thou art more righteous than I; for thou hast rendered unto me good, whereas I have rendered unto thee evil.", "left: 10px; top: 42px", 230, size=12, pad="18px 24px"))
    P3b = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 342, 274, s4, o4, "3b · More righteous than I")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("1 Samuel 24:3–17 — The Cave", "minmax(0, 1fr) 260px 280px", body, 9)
PAGES["SA2-P09-Cave"] = p09


# ───────────────────────── 10 · Mount Gilboa (31:1–6) ─────────────────────────
def p10():
    s1 = f'''      {J.sun(560, 120, 50)}
      {B.gilboa(702, 294, 160, 2001, color="#2A1A2E")}
      {B.spears_down(range(30, 700, 26), 230, 2002)}
      {mk.speed(351, 150, 40, 200, 700, 2003, color="#FFD23F", op=0.25)}'''
    o1 = (cap("Now the Philistines fought against Israel: and the men of Israel fled from before the Philistines, and fell down slain in mount Gilboa.", "left: 12px; top: 12px", size=11, maxw=380)
          + stamp(31, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #2A0A1A 0%, #8A1E2E 50%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · Mount Gilboa")

    s2 = f'''      {J.sun(351, 330, 110)}
      {V.rays(351, 330, 40, 110, 900, color="#FFF4C2", op=0.15)}
      {B.gilboa(702, 600, 200, 2004, color="#3A1E2A")}
      <path d="M-10 560 C 200 540 500 560 712 548 L 712 714 L -10 714 Z" fill="#2A1A1E" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M470 600 L 430 380" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path><path d="M470 600 L 430 380" stroke="#6B4A2A" stroke-width="5" stroke-linecap="round"></path>
      <path d="M430 380 L 420 352 L 438 376 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="2"></path>
      {B.crown(300, 602, 1.6, 14)}'''
    o2 = (cap("So Saul died, and his three sons, and his armorbearer, and all his men, that same day together.", "left: 50%; top: 40px; transform: translateX(-50%)", size=16, maxw=480, center=True)
          + end_mark("END OF 1 SAMUEL", "right: 14px; bottom: 12px"))
    P2 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 40%, #D7261E 75%, #FF8A3D 100%)", 702, 704, s2, o2, "2 · That same day together")
    body = P1 + P2
    return mk.page("1 Samuel 31:1–6 — Mount Gilboa", "300px minmax(0, 1fr)", body, 10)
PAGES["SA2-P10-Gilboa"] = p10


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "1samuel/project"))
