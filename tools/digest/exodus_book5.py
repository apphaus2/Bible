"""Exodus Book Five — The Glory (Exodus 24–40). Writes the .dc.html pages into the given folder.
Usage: python3 exodus_book5.py <out_dir>"""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, pathlib, random
import mk, exodus as E, exodus2 as X, exodus3 as Y, exodus4 as Z, exodus5 as V, egypt
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd
FX = V.tokens()
PAGES = {}
TABLETS_ARM = [(-22, -158), (-40, -200), (-20, -228)]

def dancers(p, n, x0, x1, y0, y1, seed, smin, smax):
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1), r.random()) for _ in range(n)); out = []
    for y, x, q in items:
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0); w = q < 0.5
        out.append(person(p, round(x), round(y), round(s, 2), body="#3A1E14", cloth=r.choice(["#C2456A", "#E8B830", "#2C9DB8", "#7A3BA8", "#FF8A3D", "#3F8A44"]),
                          woman=w, hair=w, flip=r.random() < 0.5, up=[(-22, -158), (-46, -206), (-36, -250)]))
    return "".join(out)

# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c5", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
    {V.rays(380, 560, 36, 120, 900, color="#FFF4C2", op=0.25)}
    <path d="M-10 820 L 200 600 L 330 680 L 470 520 L 620 640 L 770 560 L 770 1090 L -10 1090 Z" fill="#3A2A3E" stroke="#0D0D0F" stroke-width="2.4"></path>
    <path d="M-10 960 C 200 950 500 966 770 956 L 770 1090 L -10 1090 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
    {V.calf(600, 1000, 0.55, "c5c")}
    {dancers("c5", 10, 470, 740, 980, 1040, 3, 0.16, 0.24)}
    {V.tables(380, 668, 1.05, "c5t")}
    {Z.figure_both(380, 960, 1.15, "#12090A", "#E2D8C4", [(-22, -158), (-50, -220), (-46, -262)], [(22, -158), (50, -220), (46, -262)], "c5m", stroke="#FFF4C2")}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 05</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 168px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">EXODUS</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Five — The Glory</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 24 – 40</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>出</span><span>エ</span><span>ジ</span><span>プ</span><span>ト</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHUTSU</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">the two tables of the testimony, tables of stone, written with the finger of God.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 5</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #12113A 0%, #4A1D55 35%, #C2456A 60%, #FFC14D 80%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Exodus Book Five — Cover", None, body, root_style=root)
PAGES["EX5-Cover"] = cover

# ───────────────────────── 01 · Come Up to Me (24:12–18) ─────────────────────────
def glory_mount(cx, base, w, h, seed):
    """Sinai under the cloud of glory: the summit hidden in white cloud lit like devouring fire."""
    m = Z.sinai(cx, base, w, h, seed, fire=False)
    return m + Y.pillar_cloud(cx, base - h * 0.75, base - h * 1.25, w * 0.7, seed + 1).replace('fill="#C8C2D6"', 'fill="#FFC14D"') + E.blaze(cx, base - h * 0.85, w * 0.3, h * 0.3, seed + 2, n=7)

def p01():
    s1 = f'''      {V.rays(560, 150, 24, 40, 500, color="#FFE680", op=0.25)}'''
    o1 = (cap("And Jehovah said unto Moses,", "left: 12px; top: 12px")
          + god("Come up to me into the mount, and be there: and I will give thee the tables of stone, and the law and the commandment, which I have written, that thou mayest teach them.", "left: 12px; top: 58px", size=19, maxw=500)
          + stamp(24, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 100%)", 702, 294, s1, o1, "1 · Come up to me")

    s2 = f'''      {defs("g2", "Man", "Woman", "Robe", "Tunic")}
      {glory_mount(470, 390, 460, 300, 11)}
      <path d="M-10 360 C 200 350 500 366 712 356 L 712 402 L -10 402 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("g2", 30, -10, 260, 350, 396, 12, 0.12, 0.24)}'''
    o2 = (cap("And the glory of Jehovah abode upon mount Sinai, and the cloud covered it six days: and the seventh day he called unto Moses out of the midst of the cloud.", "left: 12px; top: 12px", maxw=300)
          + cap("And the appearance of the glory of Jehovah was like devouring fire on the top of the mount in the eyes of the children of Israel.", "left: 12px; bottom: 60px", maxw=260))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 60%, #7A2A5A 100%)", 702, 392, s2, o2, "2 · Devouring fire")

    s3 = f'''      {defs("g3", "Man", "Robe")}
      {Y.pillar_cloud(500, 300, -60, 360, 13).replace('fill="#C8C2D6"', 'fill="#FFE680"')}
      <path d="M-10 304 L 260 120 L 340 160 L 420 60 L 712 -10 L 712 304 Z" fill="#3A2A3E" stroke="#0D0D0F" stroke-width="2.4" opacity="0.9"></path>
      {Y.pillar_cloud(470, 220, 20, 300, 14)}
      {person("g3", 300, 214, 0.36, body="#12090A", cloth="#E2D8C4", stroke="#FFE680", sw=6)}'''
    o3 = (cap("And Moses entered into the midst of the cloud, and went up into the mount: and Moses was in the mount forty days and forty nights.", "left: 12px; top: 12px", maxw=300)
          + '    <div style="position: absolute; left: 14px; bottom: 12px; padding: 2px 8px; background: #12113A; color: #FFD23F; font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 15px; letter-spacing: 0.2em">四十日四十夜</div>\n')
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 100%)", 702, 294, s3, o3, "3 · Forty days and forty nights")
    body = P1 + P2 + P3
    return mk.page("Exodus 24:12–18 — Come Up to Me", "300px minmax(0, 1fr) 300px", body, 1)
PAGES["EX5-P01-ComeUp"] = p01

# ───────────────────────── 02 · The Finger of God (31:18–32:1) ─────────────────────────
def p02():
    s1 = f'''      {V.rays(351, 360, 40, 120, 800, color="#FFF4C2", op=0.35)}
      {E.blaze(351, 640, 640, 380, 21, n=11)}
      {V.tables(351, 560, 1.9, "f1t")}'''
    o1 = (cap("And he gave unto Moses, when he had made an end of communing with him upon mount Sinai,", "left: 12px; top: 12px", maxw=420)
          + cap("the two tables of the testimony, tables of stone, written with the finger of God.", "right: 12px; bottom: 12px", size=13, maxw=420)
          + stamp(31, "right: 16px; top: 14px"))
    P1 = panel("radial-gradient(circle at 50% 50%, #FFFFFF 0 60px, #FFE680 180px, #FF8A3D 360px, #5A1A3E 520px)", 702, 704, s1, o1, "1 · Tables of stone")

    s2 = f'''      {face(FX["__FACE_MOSES_SHINE__"], -60, 0, 0.82)}'''
    o2 = ref("EX 31:18", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6")
    P2a = panel("radial-gradient(circle at 70% 40%, #FFFFFF 0 30px, #FFE680 160px, #FF8A3D 340px)", 342, 294, s2, o2, "2a · Moses on the mount")
    s3 = f'''      {defs("f3", "Man", "Woman", "Robe", "Tunic")}
      {stars(60, 342, 160, 23)}
      <path d="M-10 200 L 352 200 L 352 304 L -10 304 Z" fill="#3A2214"></path>
      {"".join(Z.tent(x, 204, w, h, color="#5A3A22") for x, w, h in [(40, 70, 50), (300, 80, 56)])}
      {crowd("f3", 24, 80, 260, 200, 290, 24, 0.16, 0.34)}'''
    o3 = cap("And when the people saw that Moses delayed to come down from the mount,", "left: 10px; right: 10px; top: 10px", size=10.5)
    P2b = panel("linear-gradient(180deg, #05050A, #2A1A5E)", 342, 294, s3, o3, "2b · Moses delayed")
    body = P1 + cols(P2a, P2b)
    return mk.page("Exodus 31:18–32:1 — The Finger of God", "minmax(0, 1fr) 300px", body, 2)
PAGES["EX5-P02-Tables"] = p02

# ───────────────────────── 03 · Make Us Gods (32:1–4) ─────────────────────────
def p03():
    s1 = f'''      {defs("k1", "Man", "ManUp", "Woman", "Robe", "Tunic")}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 334 L -10 334 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("k1", 620, 300, 0.9, body="#3A1E14", cloth="#4A6A9A", stroke="#0D0D0F")}
      {"".join(person("k1", x, 300 + (i % 2) * 14, 0.5 + (i % 3) * 0.06, body="#2A140C", cloth=c, kind="Tunic", sw=4, up=[(-22, -158), (-36, -214), (-24, -262)]) for i, (x, c) in enumerate([(240, "#8A6A4A"), (330, "#5A6E8A"), (420, "#C9A86A"), (500, "#8A3A1E")]))}
      {crowd("k1", 30, -10, 520, 240, 330, 31, 0.2, 0.5)}'''
    o1 = (cap("the people gathered themselves together unto Aaron, and said unto him,", "left: 12px; top: 12px", maxw=300)
          + balloon("Up, make us gods, which shall go before us; for as for this Moses, the man that brought us up out of the land of Egypt, we know not what is become of him.", "right: 14px; top: 12px", 380, size=13.5, pad="20px 36px")
          + stamp(32, "left: 16px; bottom: 14px", rot=-4) + ref("AARON", "right: 60px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P1 = panel("linear-gradient(180deg, #4A1D55 0%, #FF8A3D 100%)", 702, 324, s1, o1, "1 · Make us gods")

    s2 = f'''      {face(FX["__FACE_AARON_FEAR__"], -60, 10, 0.8)}'''
    o2 = (cap("And Aaron said unto them,", "left: 10px; top: 10px", size=10)
          + tail(118, 200, "l")
          + balloon("Break off the golden rings, which are in the ears of your wives, of your sons, and of your daughters, and bring them unto me.", "left: 156px; top: 100px", 180, size=12.5, pad="22px 18px"))
    P2a = panel("radial-gradient(circle at 30% 40%, #FFE680 0 20px, #E8A35A 160px, #5A1A3E 340px)", 342, 352, s2, o2, "2a · The golden rings")
    s3 = f'''      <rect width="342" height="352" fill="#2A140C"></rect>
      {E.blaze(171, 340, 260, 160, 33, n=8)}
      <path d="M86 250 C 86 310 256 310 256 250 Z" fill="#5A5650" stroke="#0D0D0F" stroke-width="3"></path>
      <ellipse cx="171" cy="250" rx="85" ry="16" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2.4"></ellipse>
      <ellipse cx="171" cy="250" rx="60" ry="9" fill="#FFF4C2"></ellipse>
      {V.rings(171, 140, 26, 34, 70)}'''
    o3 = cap("And he received it at their hand, and fashioned it with a graving tool,", "left: 10px; right: 10px; top: 10px", size=10.5) + ref("EX 32:4", "right: 10px; bottom: 8px")
    P2b = panel("#2A140C", 342, 352, s3, o3, "2b · Fashioned with a graving tool")

    s4 = f'''      {V.rays(351, 220, 28, 60, 500, color="#FFE680", op=0.35)}
      <path d="M-10 290 L 712 290 L 712 334 L -10 334 Z" fill="#3A2214"></path>
      {V.calf(351, 300, 1.4, "k4c")}'''
    o4 = (cap("and made it a molten calf: and they said, These are thy gods, O Israel, which brought thee up out of the land of Egypt.", "left: 12px; top: 12px", maxw=340)
          + sfx("キラッ", "KIRA!", "right: 20px; top: 30px", size=46, fill="#FFD23F", stroke="#0D0D0F", rot=8))
    P3 = panel("radial-gradient(circle at 50% 60%, #FFF4C2 0 40px, #E8A317 200px, #5A1A16 460px)", 702, 324, s4, o4, "3 · A molten calf")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 32:1–4 — Make Us Gods", "330px minmax(0, 1fr) 330px", body, 3)
PAGES["EX5-P03-MakeUsGods"] = p03

# ───────────────────────── 04 · They Rose Up to Play (32:6–8) ─────────────────────────
def p04():
    s1 = f'''      {defs("d1", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      <path d="M-10 280 C 200 270 500 286 712 276 L 712 384 L -10 384 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      <rect x="120" y="230" width="70" height="50" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></rect>
      {E.blaze(155, 232, 70, 90, 41, n=5)}
      {V.calf(400, 300, 0.9, "d1c")}
      {dancers("d1", 26, -10, 712, 290, 380, 42, 0.26, 0.6)}'''
    o1 = (cap("And they rose up early on the morrow, and offered burnt-offerings, and brought peace-offerings; and the people sat down to eat and to drink, and rose up to play.", "left: 12px; top: 12px", maxw=420)
          + sfx("ドンドン", "DON DON", "right: 18px; top: 24px", size=44, fill="#D7261E", stroke="#F3EFE6", rot=6, tagbg="#0D0D0F", tagfg="#F3EFE6"))
    P1 = panel("linear-gradient(180deg, #7A2A5A 0%, #FF8A3D 60%, #FFC14D 100%)", 702, 374, s1, o1, "1 · Rose up to play")

    s2 = f'''      {stars(60, 702, 294, 43)}
      {E.blaze(600, 300, 200, 220, 44, n=8)}'''
    o2 = (cap("And Jehovah spake unto Moses,", "left: 12px; top: 12px")
          + god("Go, get thee down; for thy people, that thou broughtest up out of the land of Egypt, have corrupted themselves:", "left: 12px; top: 58px", size=22, maxw=470))
    P2 = panel("linear-gradient(180deg, #05050A, #4A1D55)", 702, 294, s2, o2, "2 · Get thee down")
    s3 = f'''      <rect width="702" height="312" fill="#12040A"></rect>
      {V.calf(560, 290, 0.9, "d3c").replace('url(#d3cG)', '#3A2214')}'''
    o3 = (god("they have turned aside quickly out of the way which I commanded them: they have made them a molten calf, and have worshipped it, and have sacrificed unto it, and said, These are thy gods, O Israel, which brought thee up out of the land of Egypt.", "left: 12px; top: 12px", size=17, maxw=440)
          + ref("EX 32:7–8", "right: 12px; bottom: 9px"))
    P3 = panel("#12040A", 702, 312, s3, o3, "3 · They have turned aside quickly")
    body = P1 + P2 + P3
    return mk.page("Exodus 32:6–8 — They Rose Up to Play", "380px 300px minmax(0, 1fr)", body, 4)
PAGES["EX5-P04-Play"] = p04

# ───────────────────────── 05 · He Brake Them (32:15–19) ─────────────────────────
def p05():
    tab = f'<g transform="translate(-20 -250) scale(0.32)">{V.tables(0, 0, 1.0, "b1t", glow=False)}</g>'
    s1 = f'''      {defs("b1", "Man", "ManUp", "Robe", "Tunic")}
      <path d="M-10 294 L 300 60 L 420 120 L 560 -10 L 712 -10 L 712 294 Z" fill="#3A2A3E" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M260 290 C 320 220 380 160 460 100" fill="none" stroke="#5A4A6E" stroke-width="3" stroke-dasharray="6 8"></path>
      {person("b1", 400, 190, 0.5, body="#12090A", cloth="#E2D8C4", stroke="#FFE680", sw=5, up=TABLETS_ARM, extra=tab)}
      {person("b1", 340, 230, 0.44, body="#12090A", cloth="#8A3A1E", stroke="#FFE680", sw=5)}'''
    o1 = (cap("And Moses turned, and went down from the mount, with the two tables of the testimony in his hand; … And the tables were the work of God, and the writing was the writing of God, graven upon the tables.", "left: 12px; top: 12px", maxw=320))
    P1 = panel("linear-gradient(180deg, #4A1D55 0%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · Down from the mount")

    s2 = f'''      {face(FX["__FACE_JOSHUA__"], -70, 10, 0.72)}'''
    o2 = (cap("he said unto Moses,", "left: 10px; top: 10px", size=10)
          + tail(108, 182, "l")
          + balloon("There is a noise of war in the camp.", "left: 146px; top: 140px", 188, size=15, pad="18px 18px"))
    P2a = panel("radial-gradient(circle at 30% 40%, #FFE680 0 20px, #FF6A2A 150px, #5A0E16 320px)", 342, 274, s2, o2, "2a · A noise of war")
    s3 = f'''      {face(FX["__FACE_MOSES_STERN__"], 412, 10, 0.72, flip=True)}'''
    o3 = (tail(198, 172, "r")
          + balloon("It is not the voice of them that shout for mastery, neither is it the voice of them that cry for being overcome; but the noise of them that sing do I hear.", "left: 8px; top: 30px", 200, size=11.5, pad="24px 20px"))
    P2b = panel("radial-gradient(circle at 70% 40%, #FFE680 0 20px, #B5421E 150px, #2A0A0A 320px)", 342, 274, s3, o3, "2b · Them that sing")

    s4 = f'''      {defs("b4", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      {speed(260, 180, 70, 120, 800, 45, color="#FFF4C2", sw=2, op=0.5)}
      <path d="M-10 360 L 712 360 L 712 444 L -10 444 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {V.calf(560, 368, 0.6, "b4c")}
      {dancers("b4", 12, 430, 712, 360, 420, 46, 0.2, 0.3)}
      {Z.figure_both(200, 360, 0.95, "#12090A", "#E2D8C4", [(-22, -158), (-40, -230), (-20, -290)], [(22, -158), (40, -230), (20, -290)], "b4m", stroke="#FF6A4A")}
      {V.tables(200, 100, 0.55, "b4t", glow=False, rot=-8)}
      {V.shards(330, 360, 0.9, 47)}'''
    o4 = (cap("And it came to pass, as soon as he came nigh unto the camp, that he saw the calf and the dancing: and Moses' anger waxed hot,", "right: 12px; top: 12px", maxw=330)
          + sfx("ガシャーン", "GASHAAN", "left: 280px; top: 210px", size=48, fill="#F3EFE6", stroke="#0D0D0F", rot=-6, align="flex-start")
          + cap("and he cast the tables out of his hands, and brake them beneath the mount.", "right: 12px; bottom: 12px", size=12, maxw=300))
    P3 = panel("radial-gradient(circle at 30% 40%, #FFE680 0 30px, #FF6A2A 200px, #5A0E16 480px)", 702, 434, s4, o4, "3 · He brake them")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 32:15–19 — He Brake Them", "300px 280px minmax(0, 1fr)", body, 5)
PAGES["EX5-P05-Broken"] = p05

# ───────────────────────── 06 · Who Is on Jehovah's Side? (32:20–26) ─────────────────────────
def p06():
    dust = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFD23F" opacity="0.8"></circle>' for x, y, r in [(470, 250, 3), (500, 240, 2), (530, 256, 3), (560, 246, 2), (590, 260, 2.5), (520, 270, 2), (610, 250, 2)])
    s1 = f'''      <path d="M-10 270 L 712 270 L 712 324 L -10 324 Z" fill="#3A2214"></path>
      {E.blaze(200, 290, 300, 260, 51, n=9)}
      {V.calf(200, 280, 0.9, "w1c").replace('stop-color="#FFF4C2"', 'stop-color="#FFE680"').replace('stop-color="#8A5A10"', 'stop-color="#5A0E16"')}
      {E.blaze(200, 296, 220, 80, 52, n=8)}
      <path d="M400 290 C 500 280 600 296 712 286 L 712 324 L 400 324 Z" fill="#2C9DB8"></path>
      {dust}'''
    o1 = (cap("And he took the calf which they had made, and burnt it with fire, and ground it to powder, and strewed it upon the water, and made the children of Israel drink of it.", "right: 12px; top: 12px", maxw=340)
          + ref("EX 32:20", "left: 12px; bottom: 9px"))
    P1 = panel("linear-gradient(180deg, #5A0E16 0%, #FF6A2A 100%)", 702, 324, s1, o1, "1 · Burnt with fire")

    s2 = f'''      {speed(170, 200, 60, 160, 800, 52, color="#0D0D0F", sw=2, op=0.4)}
      {face(FX["__FACE_MOSES_STERN__"], -60, 0, 0.95)}'''
    o2 = (cap("then Moses stood in the gate of the camp, and said,", "left: 12px; top: 12px")
          + tail(168, 220, "l")
          + balloon("Whoso is on Jehovah's side, let him come unto me.", "left: 208px; top: 120px", 440, size=24, pad="30px 40px"))
    P2 = panel("radial-gradient(circle at 25% 50%, #FFE680 0 30px, #FF6A2A 200px, #3A0E0E 460px)", 702, 352, s2, o2, "2 · Whoso is on Jehovah's side")

    s3 = f'''      {defs("w3", "Man", "Robe", "Tunic")}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M560 300 L 560 150 L 590 150 L 590 300 Z M660 300 L 660 150 L 690 150 L 690 300 Z M550 140 L 700 140 L 700 160 L 550 160 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {person("w3", 625, 294, 0.6, body="#12090A", cloth="#E2D8C4", stroke="#0D0D0F")}
      {crowd("w3", 30, 160, 540, 236, 300, 53, 0.18, 0.44, cloth=("#4A6A9A", "#5A6E8A", "#2C9DB8"))}'''
    o3 = cap("And all the sons of Levi gathered themselves together unto him.", "left: 12px; top: 12px", maxw=300) + ref("EX 32:26", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P3 = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 60%)", 702, 294, s3, o3, "3 · The sons of Levi")
    body = P1 + P2 + P3
    return mk.page("Exodus 32:20–26 — Who Is on Jehovah's Side?", "330px minmax(0, 1fr) 300px", body, 6)
PAGES["EX5-P06-Side"] = p06

# ───────────────────────── 07 · Show Me Thy Glory (33:18–23) ─────────────────────────
def p07():
    s1 = f'''      {V.rays(640, 40, 24, 40, 600, color="#FFF4C2", op=0.35)}
      {face(FX["__FACE_MOSES_CALM__"], -60, 0, 0.8)}'''
    o1 = (cap("And he said,", "left: 12px; top: 12px")
          + tail(152, 186, "l")
          + balloon("Show me, I pray thee, thy glory.", "left: 190px; top: 120px", 300, size=22, pad="24px 30px")
          + stamp(33, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(135deg, #2A1A5E 0%, #C2456A 70%, #FFE680 100%)", 702, 294, s1, o1, "1 · Show me thy glory")

    s2 = f'''      {V.rays(351, 196, 40, 60, 600, color="#FFFFFF", op=0.45)}'''
    o2 = (god("I will make all my goodness pass before thee, and will proclaim the name of Jehovah before thee; and I will be gracious to whom I will be gracious, and will show mercy on whom I will show mercy.", "left: 12px; top: 12px", size=17, maxw=430)
          + god("Thou canst not see my face; for man shall not see me and live.", "right: 12px; bottom: 12px", size=22, maxw=360))
    P2 = panel("radial-gradient(circle at 50% 50%, #FFFFFF 0 60px, #FFF4C2 160px, #FFC14D 300px, #FF8A3D 460px)", 702, 392, s2, o2, "2 · Man shall not see me and live")

    s3 = f'''      {defs("y3", "Man", "Robe")}
      <rect width="702" height="294" fill="#FFF4C2"></rect>
      {V.rays(470, 140, 30, 40, 600, color="#FFFFFF", op=0.8)}
      <path d="M-10 304 L -10 -10 L 230 -10 C 250 80 240 160 260 304 Z" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="3"></path>
      <path d="M150 304 C 160 220 170 140 160 60 L 200 60 C 210 140 220 220 230 304 Z" fill="#1A1220" stroke="#0D0D0F" stroke-width="2"></path>
      {person("y3", 186, 240, 0.4, body="#12090A", cloth="#E2D8C4", stroke="#FFE680", sw=5)}
      <path d="M200 -10 C 300 20 340 80 300 140 C 270 180 230 150 240 110 C 250 70 230 30 200 -10 Z" fill="#FFFFFF" opacity="0.85"></path>'''
    o3 = god("… while my glory passeth by, that I will put thee in a cleft of the rock, and will cover thee with my hand until I have passed by: and I will take away my hand, and thou shalt see my back; but my face shall not be seen.", "right: 12px; top: 12px", size=15, maxw=400)
    P3 = panel("#FFF4C2", 702, 294, s3, o3, "3 · A cleft of the rock")
    body = P1 + P2 + P3
    return mk.page("Exodus 33:18–23 — Show Me Thy Glory", "300px minmax(0, 1fr) 300px", body, 7)
PAGES["EX5-P07-Glory"] = p07

# ───────────────────────── 08 · The Glory Filled the Tabernacle (34:29–40:38) ─────────────────────────
def p08():
    tab = f'<g transform="translate(-20 -250) scale(0.32)">{V.tables(0, 0, 1.0, "z1t", glow=False)}</g>'
    s1 = f'''      {defs("z1", "Man", "ManUp", "Robe")}
      <path d="M-10 324 L 300 60 L 420 120 L 560 -10 L 712 -10 L 712 324 Z" fill="#3A2A3E" stroke="#0D0D0F" stroke-width="2.4"></path>
      {V.rays(420, 160, 30, 30, 400, color="#FFF4C2", op=0.6)}
      {person("z1", 420, 300, 0.7, body="#12090A", cloth="#F3EFE6", stroke="#FFF4C2", sw=4, up=TABLETS_ARM, extra=tab)}'''
    o1 = (cap("And it came to pass, when Moses came down from mount Sinai with the two tables of the testimony in Moses' hand, … that Moses knew not that the skin of his face shone by reason of his speaking with him.", "left: 12px; top: 12px", maxw=300)
          + stamp(34, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #2A1A5E 0%, #FFC14D 100%)", 702, 324, s1, o1, "1 · His face shone")

    s2 = f'''      {V.rays(171, 160, 30, 60, 400, color="#FFFFFF", op=0.7)}
      {face(FX["__FACE_MOSES_SHINE__"], -40, 0, 0.82)}'''
    P2a = panel("radial-gradient(circle at 50% 45%, #FFFFFF 0 60px, #FFF4C2 160px, #FFC14D 320px)", 342, 312, s2, ref("EX 34:29", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"), "2a · The skin of his face shone")
    s3 = f'''      {face(FX["__FACE_AARON_FEAR__"], 412, 0, 0.8, flip=True)}'''
    o3 = cap("And when Aaron and all the children of Israel saw Moses, behold, the skin of his face shone; and they were afraid to come nigh him.", "left: 10px; bottom: 10px", size=10, maxw=190)
    P2b = panel("linear-gradient(180deg, #8FD0E2, #4A6A9A)", 342, 312, s3, o3, "2b · Afraid to come nigh him")

    s4 = f'''      {stars(50, 702, 120, 81)}
      {Y.pillar_cloud(420, 150, -40, 220, 82)}
      {Y.pillar_fire(420, 160, 30, 50, 83)}
      {V.rays(420, 160, 26, 60, 500, color="#FFE680", op=0.25)}
      <path d="M-10 270 C 200 260 500 276 712 266 L 712 334 L -10 334 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {V.tabernacle(380, 286, 420, "z4")}'''
    o4 = (cap("Then the cloud covered the tent of meeting, and the glory of Jehovah filled the tabernacle.", "left: 12px; top: 12px", size=12, maxw=260)
          + cap("For the cloud of Jehovah was upon the tabernacle by day, and there was fire therein by night, in the sight of all the house of Israel, throughout all their journeys.", "right: 12px; top: 12px", maxw=220)
          + '    <div style="position: absolute; left: 14px; bottom: 12px; display: flex; align-items: center; gap: 8px; padding: 4px 10px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 2px #FFD23F"><span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 22px">終</span><span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em">END OF EXODUS</span></div>\n')
    P3 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 50%, #C2456A 100%)", 702, 324, s4, o4, "3 · The glory filled the tabernacle")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 34:29–40:38 — The Glory Filled the Tabernacle", "330px minmax(0, 1fr) 330px", body, 8)
PAGES["EX5-P08-Tabernacle"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "exodus/project"))
