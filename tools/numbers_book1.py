"""Numbers Book One — In the Wilderness (Numbers 13–24). Writes the .dc.html pages into the given folder.
Usage: python3 numbers_book1.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus2 as X, exodus3 as Y, exodus4 as Z, exodus5 as V, numbers1 as N
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd, ROD_UP
FX = N.tokens()
PAGES = {}
MOSES = dict(body="#12090A", cloth="#E2D8C4")
AARON = dict(body="#12090A", cloth="#4A6A9A")
ARMS_OUT_L = [(-22, -158), (-56, -150), (-84, -124)]
ARMS_OUT_R = [(22, -158), (56, -150), (84, -124)]
STAFF_UP = '<path d="M-40 -238 L -6 -330" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M-40 -238 L -6 -330" stroke="#8A5A30" stroke-width="6" stroke-linecap="round"></path>'
SMITE_ARM = [(-22, -158), (-40, -200), (-42, -238)]


def badge(text, pos, bg="#12113A", fg="#FFD23F", size=15):
    return (f'    <div style="position: absolute; {pos}; padding: 2px 8px; background: {bg}; color: {fg}; font-family: \'Noto Sans JP\', sans-serif; '
            f'font-weight: 900; font-size: {size}px; letter-spacing: 0.2em">{text}</div>\n')


def carriers(p, x, y, s, seed=1, body="#2A140C", c1="#8A6A4A", c2="#5A6E8A"):
    """Two men bearing one cluster of grapes upon a staff between them; (x, y) is the ground under the cluster."""
    gap = 170 * s; sh = y - 150 * s
    return (person(p, round(x - gap), y, round(s, 3), body=body, cloth=c1, kind="Tunic", sw=4)
            + person(p, round(x + gap), y, round(s, 3), body=body, cloth=c2, kind="Tunic", sw=4)
            + f'<path d="M{x - gap - 40*s:.0f} {sh:.0f} L {x + gap + 40*s:.0f} {sh:.0f}" stroke="#0D0D0F" stroke-width="{9*s:.1f}" stroke-linecap="round"></path>'
            + f'<path d="M{x - gap - 40*s:.0f} {sh:.0f} L {x + gap + 40*s:.0f} {sh:.0f}" stroke="#8A5A30" stroke-width="{5*s:.1f}" stroke-linecap="round"></path>'
            + N.grapes(x, sh, 0.92 * s, seed))


def fruit(x, y, seed):
    """A heap of pomegranates and figs."""
    r = random.Random(seed); o = []
    for _ in range(9):
        cx, cy = x + r.uniform(-50, 50), y - r.uniform(0, 26)
        if r.random() < 0.55:
            o.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="15" fill="#C2261E" stroke="#0D0D0F" stroke-width="2"></circle>'
                     f'<path d="M{cx-5:.0f} {cy-13:.0f} L {cx-3:.0f} {cy-20:.0f} L {cx:.0f} {cy-15:.0f} L {cx+3:.0f} {cy-20:.0f} L {cx+5:.0f} {cy-13:.0f}" fill="#8A1A16" stroke="#0D0D0F" stroke-width="1.6"></path>'
                     f'<circle cx="{cx-5:.0f}" cy="{cy-4:.0f}" r="4" fill="#FF8A7A" opacity="0.7"></circle>')
        else:
            o.append(f'<path d="M{cx:.0f} {cy-18:.0f} C {cx+14:.0f} {cy-6:.0f} {cx+14:.0f} {cy+10:.0f} {cx:.0f} {cy+10:.0f} C {cx-14:.0f} {cy+10:.0f} {cx-14:.0f} {cy-6:.0f} {cx:.0f} {cy-18:.0f} Z" fill="#5A3A5A" stroke="#0D0D0F" stroke-width="2"></path>'
                     f'<path d="M{cx:.0f} {cy-18:.0f} L {cx:.0f} {cy-24:.0f}" stroke="#3E5A22" stroke-width="3"></path>')
    return "".join(o)


def hills(y, color, seed, amp=40, w=712):
    r = random.Random(seed); pts = [(-10, y)]
    x = -10
    while x < w + 10:
        x += r.uniform(60, 140); pts.append((x, y - r.uniform(0, amp)))
    d = "M-10 " + str(y + 400) + " L " + " L ".join(f"{px:.0f} {py:.0f}" for px, py in pts) + f" L {w + 10} {y + 400} Z"
    return f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'


def cracks(x0, x1, y0, y1, seed):
    r = random.Random(seed); o = []
    for _ in range(14):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1); d = f"M{x:.0f} {y:.0f}"
        for _ in range(3):
            x += r.uniform(-40, 40); y += r.uniform(-6, 10); d += f" L {x:.0f} {y:.0f}"
        o.append(f'<path d="{d}" fill="none" stroke="#5A3A22" stroke-width="2"></path>')
    return "".join(o)


def fiery_at(x, y, s, uid, flip=False, seed=1):
    """A short fiery serpent slithering at (x, y), head toward +x (or -x when flipped)."""
    r = random.Random(seed); k = -1 if flip else 1
    P = [(x - k * 120 * s, y + r.uniform(-4, 4)), (x - k * 80 * s, y - 14 * s), (x - k * 40 * s, y + 10 * s), (x, y - 6 * s), (x + k * 26 * s, y - 34 * s), (x + k * 44 * s, y - 40 * s)]
    return N.fiery(P, 9 * s, uid, 0.9 * s)


# ───────────────────────── Cover ─────────────────────────
def cover():
    lookers = "".join(person("c1", x, y, sc, body="#12090A", cloth=c, kind="Robe", sw=4, woman=w, hair=w, flip=x > 380,
                             up=[(-22, -158), (-46, -196), (-54, -236)] if u else None)
                      for x, y, sc, c, w, u in [(70, 1030, 0.62, "#C9A86A", False, True), (170, 1050, 0.7, "#5A6E8A", True, False),
                                                (590, 1050, 0.7, "#8A6A4A", False, True), (690, 1030, 0.6, "#C2456A", True, True)])
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c1", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
    {V.rays(400, 470, 36, 90, 900, color="#FFF4C2", op=0.22)}
    <path d="M-10 860 L 120 800 L 260 830 L 420 780 L 600 820 L 770 790 L 770 1090 L -10 1090 Z" fill="#4A2A3E" stroke="#0D0D0F" stroke-width="2"></path>
    <path d="M-10 900 C 200 890 500 906 770 896 L 770 1090 L -10 1090 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
    {N.camp(14, 10, 750, 880, 930, 5)}
    {N.brass_serpent(380, 420, 600, "cvb")}
    {fiery_at(250, 1000, 1.1, "cvf1", seed=2)}
    {fiery_at(520, 1010, 1.0, "cvf2", flip=True, seed=3)}
    {lookers}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 136px; line-height: 1.16; letter-spacing: -1px; color: #F3EFE6">NUMBERS</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — In the Wilderness</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 13 – 24</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>民</span><span>数</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">MINSŪKI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 320px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 230px; line-height: 1.45">when he looked unto the serpent of brass, he lived.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #12113A 0%, #4A1D55 32%, #C2456A 58%, #FF8A3D 78%, #FFC14D 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Numbers Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover


# ───────────────────────── 01 · The Twelve Spies (13:1–2, 13:23) ─────────────────────────
def p01():
    s1 = f'''      {stars(80, 702, 294, 101)}
      {V.rays(600, 40, 24, 40, 500, color="#FFE680", op=0.2)}
      <path d="M-10 250 C 200 240 500 256 712 246 L 712 304 L -10 304 Z" fill="#2A1A2E"></path>
      {N.camp(10, 20, 690, 246, 270, 102, color=("#2A1A2E", "#3A2A3E", "#1A1020"))}'''
    o1 = (cap("And Jehovah spake unto Moses, saying,", "left: 12px; top: 12px")
          + god("Send thou men, that they may spy out the land of Canaan, which I give unto the children of Israel: of every tribe of their fathers shall ye send a man, every one a prince among them.", "left: 12px; top: 58px", size=18, maxw=520)
          + stamp(13, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 100%)", 702, 294, s1, o1, "1 · Send thou men")

    vines = "".join(f'<path d="M{x} 300 C {x+10} 260 {x-10} 240 {x+6} 210" fill="none" stroke="#3E5A22" stroke-width="5"></path>'
                    f'<ellipse cx="{x+6}" cy="214" rx="26" ry="14" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for x in range(20, 712, 70))
    s2 = f'''      {defs("e2", "Man", "Robe", "Tunic")}
      {hills(220, "#5E8F26", 103, 50)}
      {vines}
      {hills(320, "#8A7A3A", 104, 14)}
      {carriers("e2", 330, 380, 0.88, 105)}
      {fruit(620, 384, 106)}'''
    o2 = (cap("And they came unto the valley of Eshcol, and cut down from thence a branch with one cluster of grapes, and they bare it upon a staff between two; they brought also of the pomegranates, and of the figs.", "left: 12px; top: 12px", maxw=430)
          + ref("NUM 13:23", "right: 12px; top: 12px", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 70%)", 702, 392, s2, o2, "2 · The valley of Eshcol")

    s3 = f'''      {defs("e3", "Man", "Robe", "Tunic")}
      <path d="M-10 230 C 80 200 200 196 352 214 L 352 304 L -10 304 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(person("e3", 30 + i * 26, 222 + (i % 3) * 3, 0.3, body="#12090A", cloth="#12090A", kind="Tunic", sw=2) for i in range(12))}'''
    o3 = badge("十二人", "left: 12px; top: 12px") + ref("NUM 13:2", "right: 10px; top: 10px", color="#0D0D0F", bg="#F3EFE6")
    P3a = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 60%, #FFF4C2 100%)", 342, 294, s3, o3, "3a · Twelve men")
    s4 = f'''      {face(FX["__FACE_CALEB__"], 412, 10, 0.78, flip=True)}'''
    o4 = ref("CALEB · JUDAH", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P3b = panel("radial-gradient(circle at 70% 40%, #FFF4C2 0 20px, #FFC14D 150px, #3F8A44 330px)", 342, 294, s4, o4, "3b · Caleb")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Numbers 13:1–23 — The Twelve Spies", "300px minmax(0, 1fr) 300px", body, 1)
PAGES["NU1-P01-Spies"] = p01


# ───────────────────────── 02 · The Evil Report (13:27–33) ─────────────────────────
def p02():
    s1 = f'''      {defs("r1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("r1", 26, 380, 712, 236, 296, 201, 0.2, 0.42)}
      {person("r1", 70, 290, 0.66, stroke="#0D0D0F", **MOSES)}
      {carriers("r1", 230, 296, 0.5, 202)}'''
    o1 = (cap("And they told him, and said,", "left: 12px; top: 12px")
          + tail(400, 120, "dl")
          + balloon("We came unto the land whither thou sentest us; and surely it floweth with milk and honey; and this is the fruit of it.", "left: 340px; top: 12px", 350, size=13, pad="18px 34px"))
    P1 = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 60%)", 702, 294, s1, o1, "1 · Milk and honey")

    s2 = f'''      {face(FX["__FACE_SPY__"], -70, 10, 0.74)}'''
    o2 = (tail(118, 170, "l")
          + balloon("Howbeit the people that dwell in the land are strong, and the cities are fortified, and very great: and moreover we saw the children of Anak there.", "left: 150px; top: 46px", 186, size=11.5, pad="22px 18px")
          + ref("NUM 13:28", "left: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P2a = panel("radial-gradient(circle at 30% 40%, #E8C8A0 0 20px, #8A6A6A 160px, #2A1A2E 330px)", 342, 294, s2, o2, "2a · The children of Anak")
    s3 = f'''      {face(FX["__FACE_CALEB__"], 412, 10, 0.74, flip=True)}'''
    o3 = (cap("And Caleb stilled the people before Moses, and said,", "left: 10px; top: 10px", size=10, maxw=200)
          + tail(196, 186, "r")
          + balloon("Let us go up at once, and possess it; for we are well able to overcome it.", "left: 10px; top: 120px", 194, size=13, pad="20px 18px"))
    P2b = panel("radial-gradient(circle at 70% 40%, #FFF4C2 0 20px, #FFC14D 150px, #3F8A44 330px)", 342, 294, s3, o3, "2b · Caleb stilled the people")

    giant = person("r3", 540, 410, 2.0, body="#2A140C", cloth="#5A2A16", kind="Tunic", stroke="#FF6A2A", sw=2.5, extra=Z.SPEAR + Z.SHIELD)
    s4 = f'''      {defs("r3", "Man", "Robe", "Tunic")}
      {hills(330, "#5A3A3E", 203, 30)}
      {giant}
      <path d="M-10 380 L 712 380 L 712 410 L -10 410 Z" fill="#3A2214"></path>
      {"".join(person("r3", x, 384, 0.17, body="#12090A", cloth="#C9A86A", kind="Tunic", sw=6) for x in (250, 272, 296))}
      {X.locust(210, 376, 0.5, rot=0, flip=True)}'''
    o4 = (cap("But the men that went up with him said,", "left: 12px; top: 12px", maxw=260)
          + balloon("We are not able to go up against the people; for they are stronger than we.", "left: 12px; top: 64px", 280, size=13.5, pad="20px 30px")
          + cap("And there we saw the Nephilim, the sons of Anak, who come of the Nephilim: and we were in our own sight as grasshoppers, and so we were in their sight.", "left: 12px; bottom: 44px", size=10.5, maxw=260)
          + sfx("ズシン", "ZUSHIN", "right: 14px; bottom: 30px", size=42, fill="#F3EFE6", stroke="#0D0D0F", rot=6))
    P3 = panel("linear-gradient(180deg, #5A0E16 0%, #C2456A 60%, #FF8A3D 100%)", 702, 398, s4, o4, "3 · As grasshoppers")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Numbers 13:27–33 — The Evil Report", "300px 300px minmax(0, 1fr)", body, 2)
PAGES["NU1-P02-Report"] = p02


# ───────────────────────── 03 · The People Wept (14:1–9) ─────────────────────────
def p03():
    r = random.Random(301)
    weepers = "".join(E.kneel(x, 270 + r.uniform(0, 20), r.uniform(0.32, 0.42), color=r.choice(["#2A140C", "#3A2214", "#4A2A1A"]), flip=r.random() < 0.5)
                      for x in range(30, 700, 48))
    s1 = f'''      {stars(70, 702, 220, 302)}
      <path d="M-10 214 C 200 204 500 220 712 210 L 712 304 L -10 304 Z" fill="#1A1020"></path>
      {N.camp(9, 10, 700, 200, 222, 303, color=("#2A1A2E", "#3A2A3E", "#1A1020"))}
      {weepers}'''
    o1 = (cap("And all the congregation lifted up their voice, and cried; and the people wept that night.", "left: 12px; top: 12px", maxw=300)
          + cap("… and the whole congregation said unto them,", "left: 12px; top: 92px", size=10, maxw=300)
          + balloon("Would that we had died in the land of Egypt! or would that we had died in this wilderness!", "right: 14px; top: 14px", 330, size=14, pad="20px 34px")
          + sfx("ウウウ…", "UUU…", "right: 30px; bottom: 26px", size=34, fill="#8FD0E2", stroke="#0D0D0F", rot=-4)
          + stamp(14, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 274, s1, o1, "1 · The people wept")

    tear = '<path d="M-6 -150 L 4 -138 L -4 -126 L 6 -112 L -2 -100" fill="none" stroke="#F3EFE6" stroke-width="3"></path>'
    s2 = f'''      {speed(171, 120, 50, 60, 400, 304, color="#FFF4C2", sw=2, op=0.4)}
      <path d="M-10 250 L 352 250 L 352 304 L -10 304 Z" fill="#8A6A4A"></path>
      {Z.figure_both(110, 262, 0.9, "#12090A", "#C9A86A", ARMS_OUT_L, ARMS_OUT_R, "w2a", stroke="#0D0D0F").replace("</g>", tear + "</g>", 1)}
      {Z.figure_both(240, 262, 0.9, "#12090A", "#3F8A44", ARMS_OUT_L, ARMS_OUT_R, "w2b", stroke="#0D0D0F").replace("</g>", tear + "</g>", 1)}'''
    o2 = cap("And Joshua the son of Nun and Caleb the son of Jephunneh, who were of them that spied out the land, rent their clothes:", "left: 10px; top: 10px", size=10, maxw=320)
    P2a = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 100%)", 342, 294, s2, o2, "2a · They rent their clothes")
    s3 = f'''      {face(FX["__FACE_JOSHUA__"], 412, 20, 0.72, flip=True)}'''
    o3 = (cap("and they spake unto all the congregation of the children of Israel, saying,", "left: 10px; top: 10px", size=10, maxw=190)
          + tail(194, 196, "r")
          + balloon("The land, which we passed through to spy it out, is an exceeding good land.", "left: 10px; top: 126px", 196, size=13, pad="20px 18px"))
    P2b = panel("radial-gradient(circle at 70% 40%, #FFF4C2 0 20px, #E8A35A 150px, #4A1D55 330px)", 342, 294, s3, o3, "2b · An exceeding good land")

    s4 = f'''      {V.rays(160, 200, 30, 60, 600, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_CALEB__"], -60, 20, 0.88)}'''
    o4 = (tail(250, 200, "l")
          + balloon("If Jehovah delight in us, then he will bring us into this land, and give it unto us; a land which floweth with milk and honey.", "left: 290px; top: 14px", 400, size=15, pad="22px 40px")
          + balloon("Only rebel not against Jehovah, neither fear ye the people of the land; for they are bread for us: their defence is removed from over them, and Jehovah is with us: fear them not.", "left: 290px; top: 176px", 400, size=14, pad="26px 40px")
          + ref("NUM 14:8–9", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 30px, #FFC14D 200px, #3F8A44 460px)", 702, 418, s4, o4, "3 · Jehovah is with us")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Numbers 14:1–9 — The People Wept", "280px 300px minmax(0, 1fr)", body, 3)
PAGES["NU1-P03-Wept"] = p03


# ───────────────────────── 04 · Forty Years; No Water (14:33–34, 20:2, 20:8) ─────────────────────────
def p04():
    s1 = f'''      {defs("f1", "Man", "Woman", "Robe", "Tunic")}
      {hills(250, "#E8A35A", 401, 60)}
      {hills(290, "#C8803A", 402, 30)}
      {"".join(person("f1", 420 + i * 22, 300 - i * 4, round(0.24 - i * 0.012, 3), body="#12090A", cloth="#12090A", sw=2, woman=i % 3 == 1) for i in range(10))}'''
    o1 = (god("And your children shall be wanderers in the wilderness forty years, and shall bear your whoredoms, until your dead bodies be consumed in the wilderness.", "left: 12px; top: 12px", size=16, maxw=470)
          + god("After the number of the days in which ye spied out the land, even forty days, for every day a year, shall ye bear your iniquities, even forty years, and ye shall know my alienation.", "left: 12px; top: 128px", size=14, maxw=400)
          + badge("四十年", "right: 14px; top: 14px", size=20))
    P1 = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 60%, #FFE3B8 100%)", 702, 324, s1, o1, "1 · Forty years")

    s2 = f'''      {defs("f2", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      <path d="M-10 250 L 712 250 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {cracks(0, 712, 260, 380, 403)}
      {Z.tent(110, 300, 150, 110, color="#5A3A22")}
      {person("f2", 70, 360, 0.72, stroke="#0D0D0F", **MOSES)}
      {person("f2", 150, 366, 0.7, stroke="#0D0D0F", **AARON)}
      {"".join(person("f2", x, y, s, body="#2A140C", cloth=c, kind="Tunic", sw=4, flip=True, up=[(-22, -158), (-40, -206), (-30, -250)]) for x, y, s, c in [(330, 330, 0.5, "#8A6A4A"), (430, 360, 0.66, "#5A6E8A"), (540, 340, 0.56, "#C9A86A"), (640, 376, 0.78, "#8A3A1E")])}
      {crowd("f2", 26, 260, 712, 262, 330, 404, 0.2, 0.4)}'''
    o2 = (cap("And there was no water for the congregation: and they assembled themselves together against Moses and against Aaron.", "left: 12px; top: 12px", maxw=330)
          + sfx("ザワザワ", "ZAWA ZAWA", "right: 18px; top: 18px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=6, tagbg="#0D0D0F", tagfg="#F3EFE6")
          + stamp(20, "right: 20px; bottom: 14px"))
    P2 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 394, s2, o2, "2 · No water")

    s3 = f'''      {stars(40, 702, 280, 405)}
      {Z.rock(470, 300, 220, 200)}'''
    o3 = (god("Take the rod, and assemble the congregation, thou, and Aaron thy brother, and speak ye unto the rock before their eyes, that it give forth its water; and thou shalt bring forth to them water out of the rock; so thou shalt give the congregation and their cattle drink.", "left: 12px; top: 12px", size=15, maxw=430)
          + ref("NUM 20:8", "right: 12px; top: 10px"))
    P3 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 100%)", 702, 284, s3, o3, "3 · Speak ye unto the rock")
    body = P1 + P2 + P3
    return mk.page("Numbers 14:33–20:8 — Forty Years", "330px minmax(0, 1fr) 290px", body, 4)
PAGES["NU1-P04-Forty"] = p04


# ───────────────────────── 05 · He Smote the Rock Twice (20:10–12) ─────────────────────────
def p05():
    s1 = f'''      {face(FX["__FACE_MOSES_STERN__"], -60, 0, 0.82)}'''
    o1 = (cap("And Moses and Aaron gathered the assembly together before the rock, and he said unto them,", "right: 12px; top: 12px", maxw=330)
          + tail(250, 200, "l")
          + balloon("Hear now, ye rebels; shall we bring you forth water out of this rock?", "left: 290px; top: 110px", 380, size=21, pad="24px 40px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFE680 0 30px, #FF6A2A 200px, #3A0E0E 460px)", 702, 294, s1, o1, "1 · Hear now, ye rebels")

    s2 = f'''      {defs("m2", "Man", "ManUp", "Robe", "Tunic")}
      {speed(470, 180, 70, 120, 800, 501, color="#FFF4C2", sw=2, op=0.45)}
      <path d="M-10 330 L 712 330 L 712 444 L -10 444 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {Z.rock(380, 360, 330, 290)}
      {Z.gush(470, 220, 502, 1.2)}
      {person("m2", 280, 400, 1.15, body="#12090A", cloth="#E2D8C4", stroke="#FFF4C2", sw=3, flip=True, up=[(-22, -158), (-40, -206), (-38, -270)], extra=ROD_UP)}
      {person("m2", 120, 410, 0.9, stroke="#0D0D0F", **AARON)}'''
    o2 = (cap("And Moses lifted up his hand, and smote the rock with his rod twice: and water came forth abundantly, and the congregation drank, and their cattle.", "left: 12px; top: 12px", maxw=300)
          + sfx("ガン！", "GAN!", "left: 340px; top: 40px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start")
          + sfx("ガン！", "GAN!", "left: 420px; top: 110px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=6, align="flex-start")
          + sfx("ドドドッ", "DODODO", "right: 18px; bottom: 24px", size=40, fill="#8FD0E2", stroke="#0D0D0F", rot=-4))
    P2 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 50%, #FF8A3D 100%)", 702, 434, s2, o2, "2 · He smote the rock twice")

    s3 = f'''      {defs("m3", "Man", "Robe")}
      {hills(220, "#3F8A44", 503, 40)}
      <path d="M-10 230 L 712 230 L 712 284 L -10 284 Z" fill="#3A2214"></path>
      {person("m3", 560, 236, 0.4, body="#12090A", cloth="#12090A", sw=2)}
      {person("m3", 600, 238, 0.38, body="#12090A", cloth="#12090A", sw=2)}'''
    o3 = (cap("And Jehovah said unto Moses and Aaron,", "left: 12px; top: 12px", size=10)
          + god("Because ye believed not in me, to sanctify me in the eyes of the children of Israel, therefore ye shall not bring this assembly into the land which I have given them.", "left: 12px; top: 52px", size=15, maxw=430)
          + ref("NUM 20:12", "right: 12px; bottom: 9px"))
    P3 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 60%, #C2456A 100%)", 702, 274, s3, o3, "3 · Ye shall not bring this assembly")
    body = P1 + P2 + P3
    return mk.page("Numbers 20:10–12 — He Smote the Rock Twice", "300px minmax(0, 1fr) 280px", body, 5)
PAGES["NU1-P05-Rock"] = p05


# ───────────────────────── 06 · Fiery Serpents (21:5–9) ─────────────────────────
def p06():
    s1 = f'''      {defs("s1", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      <path d="M-10 190 L 712 190 L 712 264 L -10 264 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {N.camp(6, 10, 700, 186, 200, 601)}
      {"".join(person("s1", x, y, s, body="#2A140C", cloth=c, kind="Tunic", sw=4, up=[(-22, -158), (-40, -206), (-30, -250)]) for x, y, s, c in [(60, 250, 0.46, "#8A6A4A"), (150, 256, 0.5, "#5A6E8A"), (230, 246, 0.42, "#C9A86A")])}
      {crowd("s1", 14, -10, 300, 210, 250, 602, 0.18, 0.32)}'''
    o1 = (cap("And the people spake against God, and against Moses,", "left: 12px; top: 12px", maxw=300)
          + balloon("Wherefore have ye brought us up out of Egypt to die in the wilderness? for there is no bread, and there is no water; and our soul loatheth this light bread.", "right: 14px; top: 12px", 380, size=13, pad="18px 38px")
          + stamp(21, "left: 16px; top: 64px", rot=-4))
    P1 = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 100%)", 702, 254, s1, o1, "1 · This light bread")

    s2 = f'''      <path d="M-10 160 L 352 160 L 352 284 L -10 284 Z" fill="#C8803A"></path>
      {E.kneel(90, 250, 0.6, color="#3A2214", flip=True)}
      {N.prostrate(250, 270, 0.7, color="#5A2A16", flip=True)}
      {fiery_at(150, 262, 0.9, "s2a", seed=603)}
      {fiery_at(300, 236, 0.7, "s2b", flip=True, seed=604)}
      {fiery_at(40, 200, 0.6, "s2c", seed=605)}'''
    o2 = (cap("And Jehovah sent fiery serpents among the people, and they bit the people; and much people of Israel died.", "left: 10px; top: 10px", size=10, maxw=320)
          + sfx("シャーッ", "SHAAA", "right: 12px; top: 92px", size=32, fill="#D7261E", stroke="#FFF4C2", rot=8))
    P2a = panel("linear-gradient(180deg, #5A0E16 0%, #FF6A2A 100%)", 342, 274, s2, o2, "2a · Fiery serpents")
    s3 = f'''      {defs("s3", "Man", "Robe")}
      <path d="M-10 220 L 352 220 L 352 284 L -10 284 Z" fill="#8A6A4A"></path>
      {person("s3", 300, 270, 0.62, stroke="#0D0D0F", flip=True, **MOSES)}
      {E.kneel(170, 262, 0.42, color="#3A2214")}
      {E.kneel(100, 266, 0.46, color="#4A2A1A")}
      {E.kneel(36, 262, 0.4, color="#2A140C")}'''
    o3 = (cap("And the people came to Moses, and said,", "left: 10px; top: 8px", size=9.5)
          + balloon("We have sinned, because we have spoken against Jehovah, and against thee; pray unto Jehovah, that he take away the serpents from us.", "left: 8px; top: 40px", 250, size=10.5, pad="16px 24px")
          + cap("And Moses prayed for the people.", "right: 8px; bottom: 8px", size=9.5))
    P2b = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 342, 274, s3, o3, "2b · We have sinned")

    r = random.Random(606)
    lookers = "".join(person("s4", x, 470 + (i % 2) * 10, round(r.uniform(0.42, 0.56), 2), body="#12090A", cloth=r.choice(["#C9A86A", "#5A6E8A", "#8A6A4A", "#C2456A"]),
                             kind="Robe", sw=4, woman=i % 3 == 0, hair=i % 3 == 0, flip=x > 351, up=[(-22, -158), (-46, -196), (-54, -236)] if i % 2 == 0 else None)
                      for i, x in enumerate([40, 120, 200, 500, 580, 660]))
    s4 = f'''      {defs("s4", "Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")}
      {V.rays(380, 130, 32, 40, 600, color="#FFF4C2", op=0.3)}
      <path d="M-10 420 C 200 410 500 426 712 416 L 712 474 L -10 474 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {N.brass_serpent(351, 110, 350, "s4b")}
      {E.kneel(270, 450, 0.5, color="#3A2214", skin="#C98E66")}
      {lookers}
      {fiery_at(150, 466, 0.7, "s4f", seed=607)}'''
    o4 = (cap("And Jehovah said unto Moses,", "left: 12px; top: 12px", size=10)
          + god("Make thee a fiery serpent, and set it upon a standard: and it shall come to pass, that every one that is bitten, when he seeth it, shall live.", "left: 12px; top: 50px", size=15, maxw=250)
          + cap("And Moses made a serpent of brass, and set it upon the standard: and it came to pass, that if a serpent had bitten any man, when he looked unto the serpent of brass, he lived.", "right: 12px; top: 12px", size=10.5, maxw=230))
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 45%, #FFC14D 100%)", 702, 464, s4, o4, "3 · The serpent of brass")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Numbers 21:5–9 — The Serpent of Brass", "260px 280px minmax(0, 1fr)", body, 6)
PAGES["NU1-P06-Serpent"] = p06


# ───────────────────────── 07 · Balaam's Ass (22:22–28) ─────────────────────────
def p07():
    s1 = f'''      {defs("b1", "Man", "ManUp", "Robe", "Tunic")}
      {hills(200, "#7A3BA8", 701, 60)}
      {hills(240, "#C2456A", 702, 30)}
      <path d="M-10 270 C 200 260 500 276 712 266 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {N.mount(330, 284, 0.9, p="b1", rider_body="#3A1E14", rider_cloth="#7A3BA8")}
      {person("b1", 200, 290, 0.48, body="#2A140C", cloth="#8A6A4A", kind="Tunic", sw=4)}
      {person("b1", 140, 286, 0.44, body="#2A140C", cloth="#5A6E8A", kind="Tunic", sw=4)}
      <g opacity="0.35">{N.angel("b1", 620, 286, 0.5, glow=True)}</g>'''
    o1 = (cap("And God's anger was kindled because he went; and the angel of Jehovah placed himself in the way for an adversary against him. Now he was riding upon his ass, and his two servants were with him.", "left: 12px; top: 12px", maxw=420)
          + stamp(22, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #2A1A5E 0%, #C2456A 60%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · An adversary in the way")

    s2 = f'''      {defs("b2", "Man", "ManUp", "Robe", "Tunic")}
      <path d="M-10 250 L 712 250 L 712 404 L -10 404 Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M380 404 C 420 330 470 290 520 250 L 600 250 C 560 290 520 340 500 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {N.angel("b2", 560, 330, 0.95)}
      {speed(220, 300, 40, 90, 400, 703, color="#0D0D0F", sw=2, op=0.35)}
      {N.mount(220, 380, 1.3, flip=True, p="b2", rider_body="#3A1E14", rider_cloth="#7A3BA8", up=SMITE_ARM, extra=STAFF_UP)}'''
    o2 = (cap("And the ass saw the angel of Jehovah standing in the way, with his sword drawn in his hand; and the ass turned aside out of the way, and went into the field: and Balaam smote the ass, to turn her into the way.", "left: 12px; top: 12px", maxw=330)
          + sfx("バシッ", "BASHI!", "left: 40px; bottom: 30px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start"))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 702, 394, s2, o2, "2 · The ass turned aside")

    s3 = f'''      {defs("b3", "Man", "ManUp", "Robe")}
      <path d="M-10 230 L 352 230 L 352 304 L -10 304 Z" fill="#8A6A4A"></path>
      {N.ass_lying(170, 270, 1.0)}
      {person("b3", 120, 276, 0.66, body="#3A1E14", cloth="#7A3BA8", flip=False, up=SMITE_ARM, extra=STAFF_UP)}'''
    o3 = cap("And the ass saw the angel of Jehovah, and she lay down under Balaam: and Balaam's anger was kindled, and he smote the ass with his staff.", "left: 10px; top: 10px", size=10, maxw=320)
    P3a = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 100%)", 342, 294, s3, o3, "3a · She lay down")
    s4 = f'''      {V.rays(240, 200, 24, 40, 400, color="#FFF4C2", op=0.4)}
      {N.ass_lying(90, 330, 2.2)}'''
    o4 = (cap("And Jehovah opened the mouth of the ass, and she said unto Balaam,", "left: 10px; top: 10px", size=10, maxw=320)
          + balloon("What have I done unto thee, that thou hast smitten me these three times?", "left: 10px; top: 72px", 210, size=13, pad="18px 22px")
          + tail(150, 160, "dr"))
    P3b = panel("radial-gradient(circle at 70% 60%, #FFF4C2 0 30px, #FFC14D 160px, #C2456A 330px)", 342, 294, s4, o4, "3b · The mouth of the ass")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Numbers 22:22–28 — Balaam's Ass", "300px minmax(0, 1fr) 300px", body, 7)
PAGES["NU1-P07-Ass"] = p07


# ───────────────────────── 08 · Eyes Opened (22:29–31, 24:5, 24:17) ─────────────────────────
def p08():
    s1 = f'''      {speed(160, 140, 50, 100, 500, 801, color="#0D0D0F", sw=2, op=0.35)}
      {face(FX["__FACE_BALAAM__"], -60, 0, 0.8)}'''
    o1 = (cap("And Balaam said unto the ass,", "left: 12px; top: 12px")
          + tail(250, 170, "l")
          + balloon("Because thou hast mocked me: I would there were a sword in my hand, for now I had killed thee.", "left: 290px; top: 70px", 380, size=17, pad="22px 40px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFE680 0 30px, #C2456A 200px, #2A1A5E 460px)", 702, 254, s1, o1, "1 · Because thou hast mocked me")

    s2 = f'''      {defs("o2", "Man", "ManUp", "Robe", "Hair")}
      {V.rays(470, 160, 40, 60, 700, color="#FFFFFF", op=0.45)}
      <path d="M-10 360 L 712 360 L 712 444 L -10 444 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {N.angel("o2", 470, 400, 1.3)}
      {N.prostrate(180, 404, 1.3, color="#7A3BA8", skin="#B9785A")}
      {N.ass(60, 400, 0.9, color="#8A8478")}'''
    o2 = (cap("Then Jehovah opened the eyes of Balaam, and he saw the angel of Jehovah standing in the way, with his sword drawn in his hand; and he bowed his head, and fell on his face.", "left: 12px; top: 12px", maxw=300)
          + sfx("ハッ", "HA!", "right: 24px; top: 24px", size=44, fill="#FFF4C2", stroke="#0D0D0F", rot=6))
    P2 = panel("radial-gradient(circle at 67% 40%, #FFFFFF 0 60px, #FFF4C2 180px, #FFC14D 320px, #C2456A 520px)", 702, 434, s2, o2, "2 · He fell on his face")

    s3 = f'''      {stars(30, 342, 120, 802)}
      <path d="M-10 120 L 352 120 L 352 304 L -10 304 Z" fill="#8A5A30"></path>
      {N.camp(26, -10, 352, 130, 290, 803, color=("#F3EFE6", "#C9A86A", "#5A3A22", "#8A3A1E"))}'''
    o3 = (cap("How goodly are thy tents, O Jacob,<br>Thy tabernacles, O Israel!", "left: 10px; top: 10px", size=11)
          + ref("NUM 24:5", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P3a = panel("linear-gradient(180deg, #2A1A5E 0%, #C2456A 100%)", 342, 294, s3, o3, "3a · How goodly are thy tents")
    s4 = f'''      {stars(60, 342, 294, 804)}
      {V.rays(250, 110, 24, 20, 300, color="#FFF4C2", op=0.3)}
      {N.star(250, 110, 60)}'''
    o4 = (cap("I see him, but not now; I behold him, but not nigh: There shall come forth a star out of Jacob, And a sceptre shall rise out of Israel, And shall smite through the corners of Moab, And break down all the sons of tumult.", "left: 10px; bottom: 50px", size=9.5, maxw=230)
          + '    <div style="position: absolute; left: 12px; bottom: 10px; display: flex; align-items: center; gap: 8px; padding: 4px 10px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 2px #FFD23F"><span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 20px">終</span><span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em">END OF NUMBERS</span></div>\n'
          + stamp(24, "right: 12px; bottom: 10px"))
    P3b = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 342, 294, s4, o4, "3b · A star out of Jacob")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Numbers 22:29–24:17 — A Star out of Jacob", "260px minmax(0, 1fr) 300px", body, 8)
PAGES["NU1-P08-Star"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "numbers/project"))
