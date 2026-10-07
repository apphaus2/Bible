"""Exodus Book Three — The Red Sea (Exodus 12–15). Writes the .dc.html pages into the given folder.
Usage: python3 exodus_book3.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus2 as X, exodus3 as Y, egypt
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
FX = Y.tokens()
PAGES = {}
NEMES = '<path d="M-17 -204 C -10 -214 10 -214 17 -204 L 24 -150 L 12 -156 L 10 -176 L -10 -176 L -12 -156 L -24 -150 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="3"></path><path d="M-19 -190 L 19 -190 M-21 -172 L 21 -172" stroke="#1F5FAD" stroke-width="4"></path>'
ROD_UP = '<path d="M-38 -276 L -24 -390" stroke="#0D0D0F" stroke-width="11" stroke-linecap="round"></path><path d="M-38 -276 L -24 -390" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>'
STAFF = '<path d="M30 -120 L 34 4" stroke="#3E2416" stroke-width="6" stroke-linecap="round"></path>'
ARM_OUT = [(-22, -158), (-62, -168), (-104, -180)]
ROD_OUT = '<path d="M-104 -180 L -230 -214" stroke="#0D0D0F" stroke-width="11" stroke-linecap="round"></path><path d="M-104 -180 L -230 -214" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>'

def crowd(p, n, x0, x1, y0, y1, seed, smin, smax, flock=0.0, body=("#2A140C", "#3A2214", "#4A2A1A"), cloth=("#C9A86A", "#B8A27A", "#8A6A4A", "#5A6E8A", "#C2456A")):
    r = random.Random(seed); items = []
    for _ in range(n):
        y = r.uniform(y0, y1); k = (y - y0) / max(1, y1 - y0)
        items.append((y, r.uniform(x0, x1), smin + (smax - smin) * k, r.random()))
    items.sort()
    out = []
    for y, x, s, q in items:
        if q < flock:
            out.append(E.sheep(x, y, s * 0.9, flip=r.random() < 0.5))
        else:
            out.append(person(p, f"{x:.0f}", f"{y:.0f}", f"{s:.2f}", body=r.choice(body), cloth=r.choice(cloth), kind=r.choice(["Robe", "Tunic"]), sw=4, woman=r.random() < 0.4))
    return "".join(out)

# ───────────────────────── Cover ─────────────────────────
def cover():
    walkers = crowd("c3", 40, 300, 460, 760, 1040, 3, 0.08, 0.36)
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c3", "Man", "Woman", "Robe", "Tunic")}
    {Y.sea_corridor(760, 1080, (380, 640), -60, 820, 9, uid="c3s")}
    {Y.pillar_fire(380, 640, 470, 46, 13)}
    {walkers}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 03</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 168px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; -webkit-text-stroke: 2px #0B2E4A">EXODUS</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Three — The Red Sea</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 12 – 15</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>出</span><span>エ</span><span>ジ</span><span>プ</span><span>ト</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHUTSU</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 260px; line-height: 1.45">And the waters were a wall unto them on their right hand, and on their left.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 3</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #2A1A5E 0%, #C2456A 35%, #FFC98A 58%, #FFF4C2 64%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Exodus Book Three — Cover", None, body, root_style=root)
PAGES["EX3-Cover"] = cover

# ───────────────────────── 01 · The Passover Lamb (12:1–11) ─────────────────────────
def p01():
    s1 = f'''      <circle cx="540" cy="170" r="150" fill="#FFF4C2" opacity="0.5"></circle>
      <path d="M-10 270 C 200 260 500 276 712 266 L 712 334 L -10 334 Z" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="2"></path>
      {Y.lamb(540, 300, 2.2)}'''
    o1 = (cap("And Jehovah spake unto Moses and Aaron in the land of Egypt, saying,", "left: 12px; top: 12px", maxw=380)
          + god("In the tenth day of this month they shall take to them every man a lamb, according to their fathers' houses, a lamb for a household: … Your lamb shall be without blemish, a male a year old.", "left: 12px; top: 70px", size=18, maxw=360)
          + stamp(12, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #FFE3B8 0%, #FFC98A 100%)", 702, 324, s1, o1, "1 · A lamb without blemish")

    s2 = f'''      <rect width="342" height="362" fill="#3A2214"></rect>
      <ellipse cx="171" cy="300" rx="150" ry="40" fill="#5A3A22"></ellipse>
      {Y.basin(171, 300, 160)}
      {Y.hyssop(190, 120, 1.5, rot=168)}'''
    o2 = cap("And ye shall take a bunch of hyssop, and dip it in the blood that is in the basin, and strike the lintel and the two side-posts with the blood that is in the basin;", "left: 10px; right: 10px; top: 10px", size=10)
    P2a = panel("#3A2214", 342, 362, s2, o2, "2a · Hyssop")
    s3 = f'''      <rect x="0" y="0" width="342" height="362" fill="#C8A06A"></rect>
      <g stroke="#8A6A4A" stroke-width="1.4"><path d="M0 60 L 342 60 M0 120 L 342 120 M0 180 L 342 180 M0 240 L 342 240 M0 300 L 342 300"></path></g>
      {Y.door(100, 110, 142, 252, light="#2A1A10")}'''
    o3 = cap("And they shall take of the blood, and put it on the two side-posts and on the lintel, upon the houses wherein they shall eat it.", "left: 10px; right: 10px; bottom: 10px", size=10) + ref("EX 12:7", "right: 10px; top: 8px", color="#0D0D0F", bg="#F3EFE6")
    P2b = panel("#C8A06A", 342, 362, s3, o3, "2b · The lintel and the side-posts")

    fam = "".join(person("e4", x, 284, s, body="#3A2214", cloth=c, woman=w, hair=w, extra=STAFF if st else "") for x, s, c, w, st in
                  [(90, 0.95, "#5A6E8A", False, True), (190, 0.82, "#C2456A", True, False), (270, 0.6, "#C9A86A", False, False), (450, 0.7, "#B8A27A", True, False), (560, 0.92, "#8A6A4A", False, True)])
    s4 = f'''      {defs("e4", "Man", "Woman", "Hair", "Robe")}
      <circle cx="350" cy="110" r="160" fill="#FFC14D" opacity="0.22"></circle>
      <path d="M346 96 C 340 84 346 74 350 66 C 354 76 360 86 354 96 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M334 96 L 366 96 C 364 106 336 106 334 96 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.4"></path>
      {fam}
      <rect x="250" y="200" width="200" height="22" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>
      <path d="M270 222 L 270 284 M430 222 L 430 284" stroke="#5A3A22" stroke-width="7"></path>
      <ellipse cx="350" cy="196" rx="40" ry="12" fill="#8A3A1E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>
      <ellipse cx="290" cy="198" rx="16" ry="6" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></ellipse><ellipse cx="410" cy="198" rx="16" ry="6" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'''
    o4 = god("And thus shall ye eat it: with your loins girded, your shoes on your feet, and your staff in your hand; and ye shall eat it in haste: it is Jehovah's passover.", "right: 12px; top: 12px", size=15, maxw=300)
    P3 = panel("linear-gradient(180deg, #2A1A10 0%, #5A3A22 100%)", 702, 294, s4, o4, "3 · In haste")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 12:1–11 — The Passover Lamb", "330px minmax(0, 1fr) 300px", body, 1)
PAGES["EX3-P01-Lamb"] = p01

# ───────────────────────── 02 · When I See the Blood (12:12–23) ─────────────────────────
def wind(n, x0, x1, y0, y1, seed, color="#05050A"):
    r = random.Random(seed); o = []
    for _ in range(n):
        y = r.uniform(y0, y1); xa = r.uniform(x0, x1 - 200); ln = r.uniform(160, 420)
        o.append(f'<path d="M{xa:.0f} {y:.0f} C {xa + ln*0.3:.0f} {y - r.uniform(20, 50):.0f} {xa + ln*0.7:.0f} {y + r.uniform(-30, 30):.0f} {xa + ln:.0f} {y - r.uniform(0, 30):.0f}" fill="none" stroke="{color}" stroke-width="{r.uniform(3, 10):.1f}" stroke-linecap="round" opacity="{r.uniform(0.5, 0.9):.2f}"></path>')
    return "".join(o)

def p02():
    obel = "".join(f'<path d="M{x} 294 L {x+6} {294-h} L {x+12} {294-h-10} L {x+18} {294-h} L {x+24} 294 Z" fill="#12040A" stroke="#3A0E1E" stroke-width="1.6"></path>' for x, h in [(470, 120), (540, 150), (620, 110)])
    s1 = f'''      {stars(140, 702, 294, 71)}
      {obel}
      {egypt.pyramid(660, 294, 180, 90, lit="#12040A", dark="#0B0206", line="#2A0A14", n=5)}'''
    o1 = god("For I will go through the land of Egypt in that night, and will smite all the first-born in the land of Egypt, both man and beast; and against all the gods of Egypt I will execute judgments: I am Jehovah.", "left: 12px; top: 12px", size=18, maxw=440)
    P1 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 294, s1, o1, "1 · That night")

    houses = "".join(f'<rect x="{x}" y="{200 - h}" width="{w}" height="{h + 200}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>' + Y.door(x + w / 2 - 22, 300, 44, 92, light="#FFC14D")
                     for x, w, h in [(10, 160, 40), (190, 150, 70), (360, 160, 30), (540, 160, 60)])
    s2 = f'''      {stars(80, 702, 160, 72)}
      <circle cx="600" cy="70" r="36" fill="#F3EFE6"></circle>
      {houses}
      <path d="M-10 392 L 712 392 L 712 402 L -10 402 Z" fill="#2A1A10"></path>
      {wind(26, -40, 760, 40, 220, 5)}
      {wind(10, -40, 760, 60, 200, 6, color="#5A0E16")}'''
    o2 = (god("And the blood shall be to you for a token upon the houses where ye are: and when I see the blood, I will pass over you,", "left: 12px; top: 12px", size=17, maxw=420)
          + sfx("ゴオオオ", "GOOOO", "right: 16px; top: 140px", size=44, fill="#12113A", stroke="#C8C2D6", rot=-6))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 70%, #3A2214 100%)", 702, 392, s2, o2, "2 · When I see the blood")

    kneelers = "".join(E.kneel(x, 270, s, color=c, rim="#0D0D0F", flip=fl) for x, s, c, fl in [(90, 0.9, "#5A6E8A", False), (190, 0.7, "#C2456A", True), (270, 0.55, "#C9A86A", True)])
    s3 = f'''      <rect width="342" height="294" fill="#3A2214"></rect>
      <circle cx="171" cy="120" r="150" fill="#FFC14D" opacity="0.25"></circle>
      <path d="M166 120 C 160 108 166 98 170 90 C 174 100 180 110 174 120 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M154 120 L 186 120 C 184 130 156 130 154 120 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.4"></path>
      {kneelers}'''
    o3 = cap("and none of you shall go out of the door of his house until the morning.", "left: 10px; right: 10px; top: 10px", size=10.5) + ref("EX 12:22", "right: 10px; bottom: 8px")
    P3a = panel("#3A2214", 342, 294, s3, o3, "3a · Until the morning")
    s4 = f'''      <rect width="342" height="294" fill="#12113A"></rect>
      <rect x="40" y="90" width="262" height="220" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>
      {Y.door(136, 170, 70, 130, light="#FFC14D")}
      {wind(14, -60, 400, 40, 140, 9)}'''
    o4 = cap("Jehovah will pass over the door, and will not suffer the destroyer to come in unto your houses to smite you.", "left: 10px; right: 10px; top: 10px", size=10.5) + ref("EX 12:23", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6")
    P3b = panel("#12113A", 342, 294, s4, o4, "3b · He will pass over")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 12:12–23 — When I See the Blood", "300px minmax(0, 1fr) 300px", body, 2)
PAGES["EX3-P02-Blood"] = p02

# ───────────────────────── 03 · A Great Cry (12:29–31) ─────────────────────────
def p03():
    sky = "".join(f'<rect x="{x}" y="{324 - h}" width="{w}" height="{h}" fill="#0B0206" stroke="#3A0E1E" stroke-width="1.6"></rect>' for x, w, h in [(-10, 90, 90), (80, 70, 130), (150, 110, 80), (260, 60, 150), (320, 120, 100), (440, 80, 70), (520, 90, 140), (610, 110, 90)])
    lit = "".join(f'<rect x="{x}" y="{y}" width="8" height="12" fill="#FFC14D"></rect>' for x, y in [(100, 220), (290, 200), (360, 240), (550, 210), (640, 250)])
    s1 = f'''      {stars(60, 702, 200, 81)}
      <circle cx="350" cy="120" r="80" fill="#D7261E"></circle><circle cx="350" cy="120" r="110" fill="#D7261E" opacity="0.2"></circle>
      {sky}{lit}'''
    o1 = cap("And it came to pass at midnight, that Jehovah smote all the first-born in the land of Egypt, from the first-born of Pharaoh that sat on his throne unto the first-born of the captive that was in the dungeon; and all the first-born of cattle.", "left: 12px; top: 12px", maxw=430)
    P1 = panel("linear-gradient(180deg, #05050A 0%, #3A0E1E 100%)", 702, 324, s1, o1, "1 · At midnight")

    s2 = f'''      {speed(500, 200, 70, 160, 800, 23, color="#0D0D0F", sw=2, op=0.5)}
      {face(FX["__FACE_PHARAOH_WEEP__"], 760, -14, 1.0, flip=True)}'''
    o2 = (cap("And Pharaoh rose up in the night, he, and all his servants, and all the Egyptians; and there was a great cry in Egypt, for there was not a house where there was not one dead.", "left: 12px; top: 12px", maxw=380)
          + sfx("ウワアア", "UWAAA", "left: 40px; top: 220px", size=58, fill="#F3EFE6", stroke="#5A0E16", rot=-6, align="flex-start"))
    P2 = panel("radial-gradient(circle at 75% 50%, #C2456A 0 30px, #5A0E16 260px, #12040A 480px)", 702, 372, s2, o2, "2 · A great cry")

    s3 = f'''      {defs("g3", "Man", "Robe")}
      <rect width="702" height="284" fill="#2A140C"></rect>
      {X.columns([20, 640], -10, 290, 40, color="#3A0E0E")}
      <circle cx="120" cy="90" r="90" fill="#FF8A3D" opacity="0.25"></circle>
      <path d="M116 120 L 116 60 M110 60 C 104 40 116 30 120 18 C 124 30 132 40 126 60 Z" stroke="#3E2416" stroke-width="4" fill="#FF8A3D"></path>
      {person("g3", 180, 284, 0.9, body="#12090A", cloth="#3A2A2E", stroke="#FF8A3D", sw=2.4)}
      {person("g3", 260, 288, 0.94, body="#12090A", cloth="#2A2A3E", stroke="#FF8A3D", sw=2.4)}'''
    o3 = (cap("And he called for Moses and Aaron by night, and said,", "right: 12px; top: 12px", maxw=330)
          + balloon("Rise up, get you forth from among my people, both ye and the children of Israel; and go, serve Jehovah, as ye have said.", "right: 24px; top: 72px", 360, size=15, pad="24px 36px")
          + ref("EX 12:31", "left: 12px; bottom: 9px"))
    P3 = panel("#2A140C", 702, 284, s3, o3, "3 · Get you forth")
    body = P1 + P2 + P3
    return mk.page("Exodus 12:29–31 — A Great Cry", "330px minmax(0, 1fr) 290px", body, 3)
PAGES["EX3-P03-Cry"] = p03

# ───────────────────────── 04 · Out of Egypt (12:37–13:21) ─────────────────────────
def p04():
    s1 = f'''      {defs("h1", "Man", "Woman", "Robe", "Tunic")}
      <circle cx="600" cy="160" r="60" fill="#FFF4C2"></circle>
      {egypt.pyramid(110, 210, 200, 110, n=7)}{egypt.pyramid(240, 214, 130, 70, n=5)}
      <path d="M-10 200 C 200 190 500 206 712 196 L 712 334 L -10 334 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("h1", 90, -20, 720, 200, 330, 41, 0.12, 0.5, flock=0.2)}'''
    o1 = cap("And the children of Israel journeyed from Rameses to Succoth, about six hundred thousand on foot that were men, besides children.", "left: 12px; top: 12px", maxw=420)
    P1 = panel("linear-gradient(180deg, #FF9A6B 0%, #FFC98A 50%, #FFE3B8 60%)", 702, 334, s1, o1, "1 · Six hundred thousand")

    s2 = f'''      {face(FX["__FACE_MOSES_CALM__"], -50, -10, 0.82)}'''
    o2 = (cap("And it came to pass at the end of four hundred and thirty years, even the selfsame day it came to pass, that all the hosts of Jehovah went out from the land of Egypt.", "right: 10px; bottom: 10px", size=10, maxw=200)
          + '    <div style="position: absolute; right: 12px; top: 14px; font-family: Anton, sans-serif; font-size: 40px; line-height: 1; color: #F3EFE6; -webkit-text-stroke: 1.5px #0D0D0F">430</div>\n')
    P2a = panel("linear-gradient(180deg, #FFC98A, #C2456A)", 342, 322, s2, o2, "2a · 430 years")
    bearers = "".join(person("h3", x, 284, 0.62, body="#3A2214", cloth=c) for x, c in [(70, "#5A6E8A"), (130, "#8A6A4A"), (230, "#B8A27A"), (290, "#C9A86A")])
    s3 = f'''      {defs("h3", "Man", "Robe")}
      <path d="M-10 250 C 100 244 240 254 352 246 L 352 332 L -10 332 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {bearers}
      <path d="M30 196 L 330 196" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>
      <path d="M90 196 L 90 150 C 90 120 250 120 250 150 L 250 196 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M100 160 L 240 160 M100 176 L 240 176" stroke="#1F5FAD" stroke-width="4"></path>
      <path d="M150 196 L 150 136 M190 196 L 190 136" stroke="#B5421E" stroke-width="3"></path>'''
    o3 = cap("And Moses took the bones of Joseph with him: for he had straitly sworn the children of Israel, saying, God will surely visit you; and ye shall carry up my bones away hence with you.", "left: 10px; right: 10px; top: 10px", size=9.5)
    P2b = panel("linear-gradient(180deg, #FFE3B8, #FFC98A)", 342, 322, s3, o3, "2b · The bones of Joseph")

    s4 = f'''      {defs("h4", "Man", "Woman", "Robe", "Tunic")}
      <path d="M-10 250 C 100 244 240 254 352 246 L 352 334 L -10 334 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {Y.pillar_cloud(220, 250, 30, 80, 5)}
      {crowd("h4", 30, -10, 200, 250, 320, 44, 0.12, 0.3)}'''
    o4 = cap("And Jehovah went before them by day in a pillar of cloud, to lead them the way,", "left: 10px; top: 10px", size=10, maxw=170)
    P3a = panel("linear-gradient(180deg, #8FD0E2, #E4F4EE)", 342, 324, s4, o4, "3a · Pillar of cloud")
    s5 = f'''      {defs("h5", "Man", "Woman", "Robe", "Tunic")}
      {stars(60, 342, 200, 91)}
      <path d="M-10 250 C 100 244 240 254 352 246 L 352 334 L -10 334 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
      {Y.pillar_fire(220, 254, 30, 70, 7)}
      {crowd("h5", 30, -10, 200, 250, 320, 45, 0.12, 0.3, body=("#12090A",), cloth=("#3A2214", "#2A1A2E", "#4A2A1A"))}'''
    o5 = cap("and by night in a pillar of fire, to give them light, that they might go by day and by night:", "left: 10px; top: 10px", size=10, maxw=170) + ref("EX 13:21", "right: 10px; bottom: 8px")
    P3b = panel("linear-gradient(180deg, #05050A, #2A1A5E)", 342, 324, s5, o5, "3b · Pillar of fire")
    body = P1 + cols(P2a, P2b) + cols(P3a, P3b)
    return mk.page("Exodus 12:37–13:21 — Out of Egypt", "340px minmax(0, 1fr) 330px", body, 4)
PAGES["EX3-P04-Exodus"] = p04

# ───────────────────────── 05 · Pharaoh Pursues (14:5–12) ─────────────────────────
def p05():
    s1 = f'''      {X.columns([300, 400], -10, 300, 46, color="#3A0E0E")}
      {face(FX["__FACE_PHARAOH_NEW__"], -50, -40, 0.92)}'''
    o1 = (cap("And it was told the king of Egypt that the people were fled: and the heart of Pharaoh and of his servants was changed towards the people, and they said,", "right: 12px; top: 12px", maxw=380)
          + tail(206, 176, "l")
          + balloon("What is this we have done, that we have let Israel go from serving us?", "left: 244px; top: 120px", 340, size=17, pad="22px 34px")
          + stamp(14, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 15% 50%, #FF6A4A 0 30px, #8A1A1A 220px, #2A0A0A 460px)", 702, 294, s1, o1, "1 · What is this we have done?")

    dust = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E8C88A" opacity="0.7"></circle>' for x, y, r in [(40, 340, 40), (100, 360, 50), (200, 330, 36), (300, 350, 44), (20, 300, 30), (420, 360, 40)])
    s2 = f'''      {speed(900, 260, 50, 100, 1000, 31, color="#F3EFE6", sw=2, op=0.5)}
      <path d="M-10 330 C 200 320 500 336 712 326 L 712 402 L -10 402 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {dust}
      {Y.chariot(260, 280, 0.62)}{Y.chariot(440, 300, 0.75)}{Y.chariot(120, 330, 0.85)}{Y.chariot(620, 360, 1.05)}{Y.chariot(370, 392, 1.2)}'''
    o2 = (cap("and he took six hundred chosen chariots, and all the chariots of Egypt, and captains over all of them.", "left: 12px; top: 12px", maxw=380)
          + sfx("ドドドド", "DODODODO", "right: 16px; top: 20px", size=46, fill="#D7261E", stroke="#F3EFE6", rot=6, tagbg="#0D0D0F", tagfg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #FF6A2A 0%, #FFC14D 70%)", 702, 392, s2, o2, "2 · Six hundred chosen chariots")

    s3 = f'''      {face(FX["__FACE_HEBREW_FEAR__"], -60, 4, 0.8)}'''
    o3 = cap("and, behold, the Egyptians were marching after them; and they were sore afraid:", "right: 10px; bottom: 10px", size=10.5, maxw=180) + ref("EX 14:10", "right: 10px; top: 8px")
    P3a = panel("radial-gradient(circle at 30% 40%, #FFE680 0 20px, #5A6E8A 200px, #12113A 360px)", 342, 294, s3, o3, "3a · Sore afraid")
    s4 = f'''      {defs("i4", "Man", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M-10 160 C 100 150 240 166 352 156 L 352 220 L -10 220 Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 214 C 100 206 240 220 352 210 L 352 304 L -10 304 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("i4", 26, -10, 352, 230, 300, 51, 0.16, 0.4)}'''
    o4 = (balloon("Because there were no graves in Egypt, hast thou taken us away to die in the wilderness?", "left: 10px; top: 10px", 250, size=13, pad="18px 24px")
          + tail(150, 116, "dr"))
    P3b = panel("linear-gradient(180deg, #5A6E8A, #C2456A)", 342, 294, s4, o4, "3b · No graves in Egypt")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 14:5–11 — Pharaoh Pursues", "300px minmax(0, 1fr) 300px", body, 5)
PAGES["EX3-P05-Pursuit"] = p05

# ───────────────────────── 06 · Stand Still (14:13–21) ─────────────────────────
def p06():
    s1 = f'''      {speed(160, 200, 60, 180, 800, 41, color="#FFF4C2", sw=1.4, op=0.5)}
      {face(FX["__FACE_MOSES_CALM__"], -60, -10, 1.0)}'''
    o1 = (cap("And Moses said unto the people,", "left: 12px; top: 12px")
          + tail(188, 222, "l")
          + balloon("Fear ye not, stand still, and see the salvation of Jehovah, which he will work for you to-day: for the Egyptians whom ye have seen to-day, ye shall see them again no more for ever. Jehovah will fight for you, and ye shall hold your peace.", "left: 226px; top: 50px", 460, size=15.5, pad="34px 50px"))
    P1 = panel("radial-gradient(circle at 20% 50%, #FFF4C2 0 40px, #FFC98A 200px, #2C9DB8 480px)", 702, 374, s1, o1, "1 · Stand still")

    s2 = f'''      {stars(80, 702, 140, 93)}
      <path d="M-10 160 L 712 160 L 712 304 L -10 304 Z" fill="#0B2E4A"></path>
      <g fill="none" stroke="#2C9DB8" stroke-width="2" opacity="0.7"><path d="M-10 190 C 100 180 200 196 300 186 C 400 176 500 192 712 182"></path><path d="M-10 230 C 120 220 240 236 360 226 C 480 216 600 232 712 222"></path><path d="M-10 270 C 120 260 240 276 360 266 C 480 256 600 272 712 262"></path></g>'''
    o2 = god("And lift thou up thy rod, and stretch out thy hand over the sea, and divide it: and the children of Israel shall go into the midst of the sea on dry ground.", "left: 12px; top: 12px", size=18, maxw=460)
    P2 = panel("linear-gradient(180deg, #05050A, #12113A)", 702, 294, s2, o2, "2 · Divide it")

    winds = "".join(f'<path d="M{x} {y} C {x+120} {y-20} {x+260} {y+16} {x+420} {y-6}" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.5"></path>' for x, y in [(160, 60), (260, 100), (200, 150), (320, 40)])
    s3 = f'''      {defs("j3", "Man", "ManUp", "Robe")}
      <path d="M-10 312 L -10 200 C 60 190 120 196 180 210 L 230 322 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M180 210 C 400 190 600 200 712 196 L 712 322 L 230 322 Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M420 200 L 470 322 L 520 322 L 470 198 Z" fill="#C8A06A" stroke="#E8F6FA" stroke-width="3"></path>
      <g fill="#E8F6FA">{"".join(f'<circle cx="{x}" cy="{y}" r="{r}"></circle>' for x, y, r in [(418, 196, 6), (474, 194, 6), (430, 230, 4), (466, 236, 4), (444, 270, 3), (486, 290, 4)])}</g>
      {winds}
      {person("j3", 120, 220, 0.62, body="#12090A", cloth="#2A1A2E", stroke="#FFE680", sw=2.4, flip=True, up=ARM_OUT, extra=ROD_OUT)}'''
    o3 = (cap("And Moses stretched out his hand over the sea; and Jehovah caused the sea to go back by a strong east wind all the night, and made the sea dry land, and the waters were divided.", "right: 12px; top: 12px", maxw=420)
          + sfx("ゴゴゴゴ", "GOGOGOGO", "right: 20px; bottom: 16px", size=44, fill="#F3EFE6", stroke="#0B2E4A", rot=-4))
    P3 = panel("linear-gradient(180deg, #12113A 0%, #2A1A5E 50%, #C2456A 100%)", 702, 312, s3, o3, "3 · A strong east wind")
    body = P1 + P2 + P3
    return mk.page("Exodus 14:13–21 — Stand Still", "380px 300px minmax(0, 1fr)", body, 6)
PAGES["EX3-P06-StandStill"] = p06

# ───────────────────────── 07 · Dry Ground (14:22–25) ─────────────────────────
def p07():
    s1 = f'''      {defs("k1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {Y.sea_corridor(702, 734, (351, 300), -40, 742, 21, uid="k1s")}
      <circle cx="351" cy="300" r="70" fill="#FFF4C2" opacity="0.5"></circle>
      {crowd("k1", 70, 230, 470, 340, 730, 61, 0.06, 0.55, flock=0.15)}'''
    o1 = (cap("And the children of Israel went into the midst of the sea upon the dry ground: and the waters were a wall unto them on their right hand, and on their left.", "left: 50%; top: 14px; transform: translateX(-50%)", size=12, center=True, maxw=420)
          + sfx("ザザーッ", "ZAZAA", "left: 24px; top: 300px", size=50, fill="#E8F6FA", stroke="#0B2E4A", rot=-8, align="flex-start")
          + ref("EX 14:22", "right: 14px; bottom: 12px"))
    P1 = panel("linear-gradient(180deg, #2A1A5E 0%, #C2456A 30%, #FFC98A 40%)", 702, 734, s1, o1, "1 · The midst of the sea")

    s2 = f'''      {Y.sea_corridor(342, 264, (171, 110), -20, 362, 22, uid="k2s")}
      {Y.chariot(150, 220, 0.42)}{Y.chariot(230, 250, 0.55)}'''
    o2 = cap("And the Egyptians pursued, and went in after them into the midst of the sea, all Pharaoh's horses, his chariots, and his horsemen.", "left: 10px; right: 10px; top: 10px", size=10)
    P2a = panel("#2A1A5E", 342, 264, s2, o2, "2a · They went in after them")
    s3 = f'''      <rect width="342" height="264" fill="#5A3A22"></rect>
      <path d="M-10 170 C 100 160 240 176 352 166 L 352 274 L -10 274 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
      <g transform="translate(110 190) rotate(-30)"><circle r="44" fill="none" stroke="#0D0D0F" stroke-width="9"></circle><circle r="44" fill="none" stroke="#8A5A30" stroke-width="5"></circle>
      <path d="M0 0 L 44 0 M0 0 L -22 38 M0 0 L -22 -38" stroke="#5A3A22" stroke-width="4"></path><circle r="8" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle></g>
      <path d="M40 220 C 80 210 140 214 180 226" fill="none" stroke="#2A140C" stroke-width="6"></path>'''
    o3 = (balloon("Let us flee from the face of Israel; for Jehovah fighteth for them against the Egyptians.", "right: 10px; top: 10px", 190, size=12.5, pad="18px 20px")
          + tail(250, 116, "dr")
          + ref("EX 14:25", "left: 10px; bottom: 8px"))
    P2b = panel("#5A3A22", 342, 264, s3, o3, "2b · Let us flee")
    body = P1 + cols(P2a, P2b)
    return mk.page("Exodus 14:22–25 — Dry Ground", "740px minmax(0, 1fr)", body, 7)
PAGES["EX3-P07-DryGround"] = p07

# ───────────────────────── 08 · The Horse and His Rider (14:27–15:21) ─────────────────────────
def p08():
    s1 = f'''      {Y.crash(702, 374, 31)}
      <g transform="rotate(-24 230 300)">{Y.chariot(260, 320, 0.8)}</g>
      <g transform="rotate(30 470 260)">{Y.chariot(430, 270, 0.65, flip=True)}</g>
      <g fill="#E8F6FA">{"".join(f'<circle cx="{x}" cy="{y}" r="{r}"></circle>' for x, y, r in [(150, 330, 14), (190, 344, 10), (260, 340, 16), (320, 330, 9), (420, 300, 12), (470, 286, 8), (520, 310, 14), (360, 350, 10)])}</g>
      <path d="M90 340 C 200 320 360 356 560 320" fill="none" stroke="#E8F6FA" stroke-width="6" stroke-linecap="round"></path>'''
    o1 = (cap("And Moses stretched forth his hand over the sea, and the sea returned to its strength when the morning appeared;", "left: 12px; top: 12px", maxw=300)
          + sfx("ザッバーン", "ZABBAAN", "left: 30px; top: 150px", size=50, fill="#E8F6FA", stroke="#0B2E4A", rot=-10, align="flex-start")
          + cap("And the waters returned, and covered the chariots, and the horsemen, even all the host of Pharaoh that went in after them into the sea; there remained not so much as one of them.", "right: 12px; bottom: 12px", maxw=380))
    P1 = panel("linear-gradient(180deg, #2A1A5E 0%, #FF8A3D 100%)", 702, 374, s1, o1, "1 · The sea returned")

    s2 = f'''      {defs("n2", "Man", "Woman", "Robe", "Tunic")}
      <circle cx="560" cy="120" r="50" fill="#FFF4C2"></circle>
      <path d="M-10 150 L 712 150 L 712 210 L -10 210 Z" fill="#2C9DB8"></path>
      <g fill="none" stroke="#8FE3EE" stroke-width="2"><path d="M40 170 C 140 162 240 176 340 168"></path><path d="M380 190 C 480 182 580 196 680 188"></path></g>
      <path d="M-10 204 C 200 196 500 210 712 200 L 712 284 L -10 284 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("n2", 60, -10, 712, 210, 280, 81, 0.14, 0.34, flock=0.1)}'''
    o2 = cap("And Israel saw the great work which Jehovah did upon the Egyptians, and the people feared Jehovah: and they believed in Jehovah, and in his servant Moses.", "left: 12px; top: 12px", maxw=440)
    P2 = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 50%)", 702, 284, s2, o2, "2 · They believed")

    s3 = f'''      {face(FX["__FACE_MIRIAM_OLD__"], -40, 10, 0.78)}
      {Y.timbrel(260, 120, 1.5, rot=-12)}'''
    o3 = (cap("And Miriam the prophetess, the sister of Aaron, took a timbrel in her hand; and all the women went out after her with timbrels and with dances.", "left: 10px; right: 10px; bottom: 10px", size=10)
          + stamp(15, "right: 12px; top: 12px"))
    P3a = panel("radial-gradient(circle at 70% 30%, #FFF4C2 0 30px, #FFC98A 160px, #C2456A 340px)", 342, 324, s3, o3, "3a · Miriam the prophetess")
    dancers = "".join(person("n4", x, 300, s, body="#5A3A22", cloth=c, woman=True, hair=True, up=[(-22, -158), (-46, -206), (-36, -250)], flip=fl,
                             extra=f'<g transform="translate(-36 -262)">{Y.timbrel(0, 0, 0.8)}</g>') for x, s, c, fl in [(70, 0.62, "#C2456A", False), (170, 0.7, "#E8B830", True), (270, 0.6, "#2C9DB8", False)])
    s4 = f'''      {defs("n4", "Woman", "WomanUp", "Hair", "Robe")}
      {speed(171, 160, 40, 100, 400, 5, color="#FFF4C2", sw=1.4, op=0.6)}
      <path d="M-10 290 L 352 290 L 352 334 L -10 334 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {dancers}'''
    o4 = (balloon("Sing ye to Jehovah, for he hath triumphed gloriously; The horse and his rider hath he thrown into the sea.", "left: 10px; top: 10px", 250, size=13, pad="18px 22px")
          + sfx("シャン", "SHAN", "right: 12px; top: 120px", size=30, fill="#E8B830", stroke="#0D0D0F", rot=8)
          + '    <span style="position: absolute; right: 10px; bottom: 7px; font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #0D0D0F">つづく · TO BE CONTINUED</span>\n')
    P3b = panel("linear-gradient(180deg, #FFE680, #FF8A3D)", 342, 324, s4, o4, "3b · The song of Miriam")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 14:27–15:21 — The Horse and His Rider", "380px minmax(0, 1fr) 330px", body, 8)
PAGES["EX3-P08-Song"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "exodus/project"))
