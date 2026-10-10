"""Judges Book Two — Samson (Judges 13–16). Writes the .dc.html pages into the given folder.
Usage: python3 judges_book2.py <out_dir>"""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, pathlib, random
import mk, exodus as E, exodus3 as Y, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J, judges1 as G, judges2 as S
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
FX = S.tokens()
PAGES = {}
ARMS_WIDE_L = [(-22, -158), (-58, -164), (-94, -170)]
ARMS_WIDE_R = [(22, -158), (58, -164), (94, -170)]
LORDS = ("#1F5FAD", "#B5121B", "#E8B830", "#7A3BA8")


def samson_both(x, y, s, left, right, uid, locks=True, stroke="#0D0D0F", cloth="#8A3A1E"):
    """Samson with both arms free (wrestling, pushing the pillars)."""
    return (Z.figure_both(x, y, s, "#3A1E14", cloth, left, right, uid, stroke=stroke)
            .replace("</g>", (f'<g>{S.LOCKS_FIG}</g>' if locks else "") + "</g>", 1)
            .replace(f'fill="{cloth}" stroke="{stroke}" stroke-width="3"', f'fill="{cloth}" stroke="{stroke}" stroke-width="3"'))


def end_mark(text, pos, ch="終"):
    return (f'    <div style="position: absolute; {pos}; display: flex; align-items: center; gap: 8px; padding: 4px 10px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 2px #FFD23F">'
            f'<span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 20px">{ch}</span><span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em">{text}</span></div>\n')


# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c2", "Man", "ManUp", "Robe", "Tunic")}
    {V.rays(380, 720, 40, 80, 900, color="#FFF4C2", op=0.25)}
    <g transform="translate(-10 400)">{S.temple(780, 690, 70, (250, 530), uid="c2", seed=21)}</g>
    {S.cracks_on(240, 510, 1080, 22)}{S.cracks_on(520, 510, 1080, 23)}
    {J.collapse(-10, 770, 470, 120, 24)}
    {samson_both(380, 1040, 1.5, [(-22, -158), (-60, -168), (-92, -180)], [(22, -158), (60, -168), (92, -180)], "c2s", stroke="#FFD23F")}
    {speed(380, 800, 60, 120, 600, 25, color="#FFF4C2", sw=2, op=0.4)}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 02</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 160px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">JUDGES</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Two — Samson</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 13 – 16</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>士</span><span>師</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHISHIKI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">O Lord Jehovah, remember me, I pray thee, and strengthen me, I pray thee, only this once, O God,</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 2</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #2A0A1E 0%, #7A1A2A 35%, #D7261E 60%, #FF8A3D 85%, #FFC14D 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Judges Book Two — Cover", None, body, root_style=root)
PAGES["JG2-Cover"] = cover


# ───────────────────────── 01 · A Nazirite unto God (13:3–24) ─────────────────────────
def p01():
    s1 = f'''      {defs("n1", "Man", "Woman", "Hair", "Robe")}
      <path d="M-10 220 C 200 210 500 226 712 216 L 712 304 L -10 304 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2"></path>
      {S.grain(-10, 712, 250, 30, 101)}
      {N.angel("n1", 470, 280, 0.66, sword=False)}
      {person("n1", 260, 284, 0.6, body="#3A1E14", cloth="#5A6E8A", woman=True, hair=True)}'''
    o1 = (cap("And the angel of Jehovah appeared unto the woman, and said unto her,", "left: 12px; top: 12px", maxw=300)
          + stamp(13, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 70%)", 702, 294, s1, o1, "1 · The angel and the woman")

    s2 = f'''      {V.rays(560, 160, 30, 40, 500, color="#FFFFFF", op=0.4)}
      {face(FX["__FACE_MANOAH_WIFE__"], -60, 20, 0.86)}'''
    o2 = (god("Behold now, thou art barren, and bearest not; but thou shalt conceive, and bear a son.", "right: 12px; top: 12px", size=17, maxw=380)
          + god("… for, lo, thou shalt conceive, and bear a son; and no razor shall come upon his head; for the child shall be a Nazirite unto God from the womb: and he shall begin to save Israel out of the hand of the Philistines.", "right: 12px; top: 120px", size=15, maxw=380)
          + ref("JDG 13:3, 5", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("radial-gradient(circle at 30% 50%, #FFF4C2 0 30px, #FFC14D 200px, #C2456A 460px)", 702, 392, s2, o2, "2 · No razor shall come upon his head")

    s3 = f'''      {defs("n3", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {J.sun(600, 70, 34)}
      {hills(190, "#3F8A44", 102, 40)}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 304 L -10 304 Z" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="2"></path>
      {person("n3", 340, 286, 0.7, body="#3A1E14", cloth="#5A6E8A", woman=True, hair=True)}
      {S.samson("n3", 400, 290, 0.38, cloth="#C9A86A")}'''
    o3 = (cap("And the woman bare a son, and called his name Samson: and the child grew, and Jehovah blessed him.", "left: 12px; top: 12px", maxw=300)
          + ref("SAMSON", "right: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s3, o3, "3 · The child grew")
    body = P1 + P2 + P3
    return mk.page("Judges 13:3–24 — A Nazirite unto God", "300px minmax(0, 1fr) 300px", body, 1)
PAGES["JG2-P01-Nazirite"] = p01


# ───────────────────────── 02 · The Young Lion (14:5–6) ─────────────────────────
def p02():
    vines = "".join(f'<path d="M{x} 250 L {x} 200" stroke="#5A3A22" stroke-width="4"></path><ellipse cx="{x}" cy="196" rx="22" ry="12" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1.6"></ellipse><circle cx="{x - 6}" cy="208" r="4" fill="#5A1A6E"></circle>' for x in range(20, 712, 50))
    s1 = f'''      {defs("l1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {hills(170, "#8A6A4A", 201, 40)}
      {vines}
      <path d="M-10 250 C 200 240 500 256 712 246 L 712 294 L -10 294 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {S.samson("l1", 520, 280, 0.6)}
      {person("l1", 300, 276, 0.5, body="#2A140C", cloth="#8A6A4A", sw=4)}
      {person("l1", 250, 278, 0.48, body="#3A1E14", cloth="#5A6E8A", woman=True, hair=True, sw=4)}'''
    o1 = (cap("Then went Samson down, and his father and his mother, to Timnah, and came to the vineyards of Timnah:", "left: 12px; top: 12px", maxw=320)
          + stamp(14, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 284, s1, o1, "1 · The vineyards of Timnah")

    s2 = f'''      {speed(470, 200, 70, 100, 700, 202, color="#0D0D0F", sw=2, op=0.35)}
      <path d="M-10 330 L 712 330 L 712 404 L -10 404 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {S.lion(380, 350, 2.2)}'''
    o2 = (cap("and, behold, a young lion roared against him.", "left: 12px; top: 12px", size=12)
          + sfx("ガオオオッ", "GAOOO!", "right: 16px; top: 24px", size=50, fill="#FFD23F", stroke="#0D0D0F", rot=8))
    P2 = panel("radial-gradient(circle at 70% 40%, #FFE680 0 30px, #FF6A2A 200px, #5A0E16 480px)", 702, 394, s2, o2, "2 · A young lion roared")

    s3 = f'''      {defs("l3", "Man", "Robe", "Tunic")}
      {V.rays(351, 160, 36, 40, 600, color="#FFF4C2", op=0.35)}
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#8A6A4A"></path>
      <g transform="rotate(-24 420 220)">{S.lion(460, 260, 1.1, flip=True)}</g>
      {samson_both(300, 290, 0.95, [(-22, -158), (10, -150), (50, -150)], [(22, -158), (70, -176), (110, -186)], "l3s", stroke="#FFF4C2")}'''
    o3 = (cap("And the Spirit of Jehovah came mightily upon him, and he rent him as he would have rent a kid; and he had nothing in his hand: but he told not his father or his mother what he had done.", "right: 12px; top: 12px", size=10.5, maxw=290)
          + ref("JDG 14:6", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 60%, #FF8A3D 100%)", 702, 294, s3, o3, "3 · Nothing in his hand")
    body = P1 + P2 + P3
    return mk.page("Judges 14:5–6 — The Young Lion", "290px minmax(0, 1fr) 300px", body, 2)
PAGES["JG2-P02-Lion"] = p02


# ───────────────────────── 03 · Three Hundred Foxes (15:4–5) ─────────────────────────
def p03():
    pairs = "".join(S.fox(x, y, 0.9, flip=True, brand=False) + S.fox(x + 96, y, 0.9, brand=True) for x, y in [(80, 250), (340, 270), (560, 246)])
    s1 = f'''      {defs("x1", "Man", "ManUp", "Robe", "Tunic")}
      {stars(60, 702, 200, 301)}
      <path d="M-10 230 L 712 230 L 712 304 L -10 304 Z" fill="#2A1A2E"></path>
      {pairs}'''
    o1 = (cap("And Samson went and caught three hundred foxes, and took firebrands, and turned tail to tail, and put a firebrand in the midst between every two tails.", "left: 12px; top: 12px", maxw=420)
          + stamp(15, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 294, s1, o1, "1 · Tail to tail")

    r = random.Random(302)
    runners = "".join(S.fox(x, 600 + r.uniform(-20, 30), r.uniform(0.7, 1.0), flip=r.random() < 0.3, seed=i) for i, x in enumerate(range(60, 700, 110)))
    s2 = f'''      {stars(40, 702, 200, 303)}
      <path d="M-10 420 C 200 410 500 426 712 416 L 712 704 L -10 704 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(S.olive(x, 420, 0.9, burning=x % 2 == 0, seed=x) for x in (60, 170, 600, 680))}
      {S.grain(-10, 712, 540, 50, 304, burning=True)}
      {S.grain(-10, 712, 640, 40, 305)}
      {runners}'''
    o2 = (cap("And when he had set the brands on fire, he let them go into the standing grain of the Philistines, and burnt up both the shocks and the standing grain, and also the oliveyards.", "left: 12px; top: 12px", maxw=420)
          + sfx("ゴオオオ", "GOOOO", "right: 16px; top: 160px", size=52, fill="#FFD23F", stroke="#0D0D0F", rot=6))
    P2 = panel("linear-gradient(180deg, #2A0A1E 0%, #7A1A2A 40%, #D7261E 70%, #FF8A3D 100%)", 702, 694, s2, o2, "2 · The standing grain burnt up")
    body = P1 + P2
    return mk.page("Judges 15:4–5 — Three Hundred Foxes", "300px minmax(0, 1fr)", body, 3)
PAGES["JG2-P03-Foxes"] = p03


# ───────────────────────── 04 · The Jawbone (15:14–16) ─────────────────────────
def p04():
    ropes = "".join(f'<path d="M{x} {y} l 14 -6" stroke="#C9A86A" stroke-width="4" stroke-linecap="round"></path>' for x, y in [(330, 150), (370, 140), (300, 170), (400, 160), (350, 120)])
    s1 = f'''      {defs("w1", "Man", "ManUp", "Robe", "Tunic")}
      {V.rays(351, 160, 36, 40, 500, color="#FFF4C2", op=0.35)}
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#8A6A4A"></path>
      {samson_both(351, 290, 0.8, ARMS_WIDE_L, ARMS_WIDE_R, "w1s", stroke="#FFF4C2")}
      {ropes}
      {S.philistines("w1", 10, 480, 712, 250, 300, 401, 0.3, 0.46, flip=True)}
      {S.philistines("w1", 6, -10, 200, 250, 300, 402, 0.3, 0.46)}'''
    o1 = (cap("When he came unto Lehi, the Philistines shouted as they met him: and the Spirit of Jehovah came mightily upon him, and the ropes that were upon his arms became as flax that was burnt with fire, and his bands dropped from off his hands.", "left: 12px; top: 12px", size=10, maxw=320)
          + sfx("ブチッ", "BUCHI!", "right: 16px; top: 20px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=6))
    P1 = panel("linear-gradient(180deg, #5A0E16 0%, #C2456A 60%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · The ropes became as flax")

    s2 = f'''      {defs("w2", "Man", "ManUp", "Robe", "Tunic")}
      {speed(260, 160, 70, 100, 800, 403, color="#FFF4C2", sw=2, op=0.4)}
      <path d="M-10 330 L 712 330 L 712 404 L -10 404 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {S.philistines("w2", 9, 380, 712, 300, 390, 404, 0.4, 0.7, flip=True)}
      {"".join(N.prostrate(x, 392, 0.7, color=c, flip=True) for x, c in [(420, "#1F5FAD"), (560, "#B5121B")])}
      {S.samson("w2", 240, 396, 1.15, up=[(-22, -158), (-46, -206), (-30, -260)], extra=S.jawbone(-36, -262, 0.7, rot=-40), stroke="#FFF4C2")}'''
    o2 = (cap("And he found a fresh jawbone of an ass, and put forth his hand, and took it, and smote a thousand men therewith.", "left: 12px; top: 12px", size=12, maxw=320)
          + sfx("ドカッ", "DOKA!", "left: 380px; top: 80px", size=50, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start"))
    P2 = panel("radial-gradient(circle at 35% 40%, #FFF4C2 0 30px, #FF8A3D 200px, #5A0E16 480px)", 702, 394, s2, o2, "2 · A fresh jawbone")

    s3 = f'''      {face(FX["__FACE_SAMSON__"], -50, 0, 0.82)}
      {S.jawbone(560, 200, 1.1, rot=-20)}'''
    o3 = (cap("And Samson said,", "left: 280px; top: 12px", size=10)
          + tail(250, 160, "l")
          + balloon("With the jawbone of an ass, heaps upon heaps,<br>With the jawbone of an ass have I smitten a thousand men.", "left: 290px; top: 50px", 330, size=16, pad="22px 34px")
          + badge("千人", "right: 14px; bottom: 14px", size=26))
    P3 = panel("radial-gradient(circle at 25% 45%, #FFE680 0 30px, #FF6A2A 200px, #3A0E0E 460px)", 702, 294, s3, o3, "3 · Heaps upon heaps")
    body = P1 + P2 + P3
    return mk.page("Judges 15:14–16 — The Jawbone", "300px minmax(0, 1fr) 300px", body, 4)
PAGES["JG2-P04-Jawbone"] = p04


# ───────────────────────── 05 · The Gates of Gaza (16:3–4) ─────────────────────────
def p05():
    s1 = f'''      {stars(60, 702, 160, 501)}
      {J.moon(600, 60, 26)}
      {J.jericho(-10, 712, 120, 304, 502, color="#8A7A6A", towers=2)}
      <rect x="290" y="150" width="120" height="154" fill="#12090A"></rect>
      <g transform="translate(350 304)">{S.gates(0, 0, 0.7).replace('translate(0.0 0.0)', 'translate(0 0)')}</g>'''
    o1 = (cap("And Samson lay till midnight, and arose at midnight, and laid hold of the doors of the gate of the city, and the two posts, and plucked them up, bar and all,", "left: 12px; top: 12px", maxw=380)
          + stamp(16, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 294, s1, o1, "1 · At midnight")

    s2 = f'''      {defs("g2", "Man", "Robe", "Tunic")}
      {J.sun(620, 80, 36)}
      <path d="M-10 404 L 120 360 C 300 280 480 180 712 120 L 712 404 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>
      {S.samson("g2", 380, 300, 1.0, extra=S.gates(0, -150, 0.7, rot=-14), stroke="#FFF4C2")}'''
    o2 = (cap("and put them upon his shoulders, and carried them up to the top of the mountain that is before Hebron.", "left: 12px; top: 12px", size=12, maxw=320)
          + sfx("ズシッ", "ZUSHI", "left: 30px; bottom: 30px", size=44, fill="#F3EFE6", stroke="#0D0D0F", rot=-6, align="flex-start"))
    P2 = panel("linear-gradient(180deg, #4A1D55 0%, #FF8A3D 60%, #FFC14D 100%)", 702, 394, s2, o2, "2 · The top of the mountain")

    s3 = f'''      {face(FX["__FACE_DELILAH__"], 760, 10, 0.82, flip=True)}'''
    o3 = (cap("And it came to pass afterward, that he loved a woman in the valley of Sorek, whose name was Delilah.", "left: 12px; top: 12px", size=12, maxw=320)
          + ref("DELILAH", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("radial-gradient(circle at 75% 45%, #FFE680 0 30px, #C2456A 200px, #2A0A1E 460px)", 702, 294, s3, o3, "3 · Delilah")
    body = P1 + P2 + P3
    return mk.page("Judges 16:3–4 — The Gates of Gaza", "300px minmax(0, 1fr) 300px", body, 5)
PAGES["JG2-P05-Gaza"] = p05


# ───────────────────────── 06 · Wherein Thy Great Strength Lieth (16:5–17) ─────────────────────────
def p06():
    s1 = f'''      {defs("d1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      <rect width="702" height="304" fill="#3A1E2A"></rect>
      <path d="M-10 240 L 712 240 L 712 304 L -10 304 Z" fill="#5A3A3A"></path>
      {person("d1", 100, 280, 0.66, body="#3A1E14", cloth="#7A3BA8", woman=True, hair=True)}
      {"".join(person("d1", x, 284, 0.6, body="#5A2A16", cloth=c, kind="Tunic", sw=4, flip=True, extra=S.FEATHERS + S.FEATHER_BAND) for x, c in zip((480, 550, 620, 690), LORDS))}
      {S.silver(250, 280, 30, 601, 60)}'''
    o1 = (cap("And the lords of the Philistines came up unto her, and said unto her,", "left: 12px; top: 12px", size=10, maxw=300)
          + balloon("Entice him, and see wherein his great strength lieth, and by what means we may prevail against him, that we may bind him to afflict him: and we will give thee every one of us eleven hundred pieces of silver.", "right: 14px; top: 12px", 390, size=12.5, pad="22px 40px"))
    P1 = panel("linear-gradient(180deg, #3A1E2A 0%, #7A1A2A 100%)", 702, 294, s1, o1, "1 · The lords of the Philistines")

    s2 = f'''      {face(FX["__FACE_DELILAH__"], 760, 10, 0.8, flip=True)}'''
    o2 = (cap("And she said unto him,", "left: 12px; top: 12px", size=10)
          + tail(420, 150, "r")
          + balloon("How canst thou say, I love thee, when thy heart is not with me? thou hast mocked me these three times, and hast not told me wherein thy great strength lieth.", "left: 12px; top: 50px", 410, size=14, pad="22px 40px"))
    P2 = panel("radial-gradient(circle at 75% 45%, #FFE680 0 30px, #C2456A 200px, #2A0A1E 460px)", 702, 294, s2, o2, "2 · How canst thou say, I love thee")

    s3 = f'''      {face(FX["__FACE_SAMSON__"], -50, 10, 0.82)}'''
    o3 = (cap("And he told her all his heart, and said unto her,", "left: 290px; top: 12px", size=10)
          + tail(250, 190, "l")
          + balloon("There hath not come a razor upon my head; for I have been a Nazirite unto God from my mother's womb: if I be shaven, then my strength will go from me, and I shall become weak, and be like any other man.", "left: 290px; top: 52px", 400, size=14, pad="26px 40px"))
    P3 = panel("radial-gradient(circle at 25% 45%, #FFE680 0 30px, #B5421E 200px, #2A0A1E 460px)", 702, 392, s3, o3, "3 · All his heart")
    body = P1 + P2 + P3
    return mk.page("Judges 16:5–17 — Wherein Thy Great Strength Lieth", "300px 300px minmax(0, 1fr)", body, 6)
PAGES["JG2-P06-Delilah"] = p06


# ───────────────────────── 07 · The Philistines Are upon Thee (16:19–21) ─────────────────────────
def p07():
    r = random.Random(701)
    falling = "".join(f'<path d="M{f} {y} c 10 10 -6 20 4 34" fill="none" stroke="#1A1210" stroke-width="4" stroke-linecap="round" transform="rotate({r.uniform(-40, 40):.0f} {f} {y})"></path>' for f, y in [(250, 196), (270, 214), (290, 186), (305, 224), (230, 222), (320, 200), (262, 236)])
    s1 = f'''      {defs("v1", "Man", "ManUp", "Woman", "Hair", "Robe", "Tunic")}
      <rect width="702" height="304" fill="#B5652E"></rect>
      <ellipse cx="340" cy="150" rx="300" ry="160" fill="#FFC14D" opacity="0.5"></ellipse>
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#5A3A3A"></path>
      {E.kneel(240, 262, 0.7, color="#7A3BA8", flip=True, skin="#D9A27A")}
      {N.prostrate(330, 266, 1.0, color="#8A3A1E", skin="#3A1E14", flip=True)}
      {person("v1", 370, 262, 0.62, body="#3A1E14", cloth="#3A3A4A", kind="Tunic", sw=4, flip=False, up=[(-22, -158), (-50, -130), (-76, -112)], extra='<path d="M-76 -112 L -96 -104 L -94 -98 L -74 -106 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>')}
      {falling}'''
    o1 = (cap("And she made him sleep upon her knees; and she called for a man, and shaved off the seven locks of his head; and she began to afflict him, and his strength went from him.", "left: 12px; top: 12px", maxw=380)
          + badge("七房", "right: 14px; top: 14px", bg="#5A0E16", fg="#FFE680", size=20))
    P1 = panel("#B5652E", 702, 294, s1, o1, "1 · The seven locks")

    s2 = f'''      {face(FX["__FACE_DELILAH__"], -60, 20, 0.7)}'''
    o2 = (cap("And she said,", "left: 10px; top: 10px", size=10)
          + tail(126, 168, "l")
          + balloon("The Philistines are upon thee, Samson.", "left: 160px; top: 110px", 170, size=16, pad="20px 16px"))
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #C2456A 150px, #2A0A1E 330px)", 342, 294, s2, o2, "2a · Upon thee, Samson")
    s3 = f'''      {face(FX["__FACE_SAMSON_SLEEP__"], 412, 20, 0.7, flip=True)}'''
    o3 = (cap("And he awoke out of his sleep, and said,", "left: 10px; top: 10px", size=10, maxw=200)
          + tail(196, 178, "r")
          + balloon("I will go out as at other times, and shake myself free.", "left: 8px; top: 110px", 196, size=13.5, pad="20px 18px"))
    P2b = panel("radial-gradient(circle at 70% 50%, #E8C8A0 0 20px, #7A3BA8 160px, #12113A 330px)", 342, 294, s3, o3, "2b · Shake myself free")

    s4 = f'''      {defs("v4", "Man", "ManUp", "Robe", "Tunic")}
      <rect width="702" height="404" fill="#12090A"></rect>
      <path d="M420 -10 L 470 -10 L 560 404 L 380 404 Z" fill="#FFE680" opacity="0.12"></path>
      <path d="M-10 330 L 712 330 L 712 404 L -10 404 Z" fill="#2A1A1A"></path>
      {S.mill(260, 320, 0.9)}
      {S.samson("v4", 470, 380, 0.95, locks=False, cloth="#5A4A3E", up=[(-22, -158), (-50, -166), (-80, -176)], stroke="#8A7A6A")}
      {S.fetters(440, 376, 1.0)}'''
    o4 = (cap("But he knew not that Jehovah was departed from him.", "left: 12px; top: 12px", size=12, maxw=300)
          + cap("And the Philistines laid hold on him, and put out his eyes; and they brought him down to Gaza, and bound him with fetters of brass; and he did grind in the prison-house.", "right: 12px; top: 12px", size=10.5, maxw=280)
          + sfx("ゴリ…ゴリ…", "GORI… GORI…", "left: 30px; bottom: 30px", size=30, fill="#8A7A6A", stroke="#0D0D0F", rot=-4, align="flex-start"))
    P3 = panel("#12090A", 702, 394, s4, o4, "3 · He did grind in the prison-house")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Judges 16:19–21 — The Philistines Are upon Thee", "300px 300px minmax(0, 1fr)", body, 7)
PAGES["JG2-P07-Shaven"] = p07


# ───────────────────────── 08 · The Pillars (16:22, 16:28–30) ─────────────────────────
def p08():
    s1 = f'''      {face(FX["__FACE_SAMSON_PRAY__"], -50, 0, 0.8)}'''
    o1 = (cap("Howbeit the hair of his head began to grow again after he was shaven.", "right: 12px; top: 12px", size=10, maxw=360)
          + cap("And Samson called unto Jehovah, and said,", "left: 290px; top: 70px", size=10)
          + tail(250, 170, "l")
          + balloon("O Lord Jehovah, remember me, I pray thee, and strengthen me, I pray thee, only this once, O God, that I may be at once avenged of the Philistines for my two eyes.", "left: 290px; top: 106px", 400, size=13.5, pad="22px 40px"))
    P1 = panel("radial-gradient(circle at 25% 40%, #FFF4C2 0 30px, #FFC14D 160px, #4A1D55 420px)", 702, 274, s1, o1, "1 · Remember me")

    s2 = f'''      {defs("p2", "Man", "Robe")}
      {V.rays(351, 380, 40, 60, 700, color="#FFF4C2", op=0.3)}
      {S.temple(702, 494, 60, (250, 452), uid="p2", seed=801)}
      {S.cracks_on(250, 110, 494, 802)}{S.cracks_on(452, 110, 494, 803)}
      {samson_both(351, 480, 1.25, [(-22, -158), (-56, -168), (-80, -176)], [(22, -158), (56, -168), (80, -176)], "p2s", locks=True, stroke="#FFD23F", cloth="#5A4A3E")}
      {speed(351, 300, 50, 160, 500, 804, color="#FFF4C2", sw=2, op=0.35)}'''
    o2 = (cap("And Samson took hold of the two middle pillars upon which the house rested, and leaned upon them, the one with his right hand, and the other with his left.", "left: 12px; top: 120px", size=10, maxw=210)
          + cap("And Samson said,", "right: 12px; top: 120px", size=10)
          + balloon("Let me die with the Philistines.", "right: 12px; top: 160px", 200, size=17, pad="20px 20px")
          + cap("And he bowed himself with all his might;", "right: 12px; bottom: 14px", size=11)
          + sfx("ミシミシッ", "MISHI MISHI", "left: 20px; bottom: 30px", size=38, fill="#F3EFE6", stroke="#0D0D0F", rot=-6, align="flex-start"))
    P2 = panel("linear-gradient(180deg, #4A1D55 0%, #7A1A2A 50%, #2A0A1E 100%)", 702, 494, s2, o2, "2 · The two middle pillars")

    s3 = f'''      {J.collapse(-10, 712, 230, 220, 805)}
      <path d="M-10 230 L 712 230 L 712 254 L -10 254 Z" fill="#3A2214"></path>'''
    o3 = (cap("and the house fell upon the lords, and upon all the people that were therein. So the dead that he slew at his death were more than they that he slew in his life.", "left: 12px; top: 12px", size=11, maxw=420)
          + sfx("ドドドドッ", "DODODODO", "right: 16px; top: 18px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=6)
          + end_mark("END OF JUDGES", "right: 14px; bottom: 12px"))
    P3 = panel("linear-gradient(180deg, #D7261E 0%, #FF8A3D 60%, #FFC14D 100%)", 702, 244, s3, o3, "3 · The house fell")
    body = P1 + P2 + P3
    return mk.page("Judges 16:22–30 — The Pillars", "280px minmax(0, 1fr) 250px", body, 8)
PAGES["JG2-P08-Pillars"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "judges/project"))
