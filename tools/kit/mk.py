"""Page-building helpers shared by the Exodus books. Each helper returns an HTML string in the house style."""
import json, pathlib, random
B = pathlib.Path(__file__).parent
FIG = json.loads((B / "figures.json").read_text())
TUNIC = "M-25 -164 C -31 -150 -33 -120 -28 -58 L -18 -62 L -8 -55 L 2 -62 L 12 -55 L 22 -62 L 28 -58 C 33 -120 31 -150 25 -164 C 14 -170 -14 -170 -25 -164 Z"
ROBE = "M-26 -166 C -36 -150 -40 -110 -40 -60 C -40 -30 -36 -10 -30 0 L 30 0 C 36 -10 40 -30 40 -60 C 40 -110 36 -150 26 -166 C 14 -172 -14 -172 -26 -166 Z"
BOW = "M-46 0 C -46 -26 -28 -46 0 -48 C 22 -50 40 -38 46 -20 L 56 -10 C 62 -6 64 -2 58 0 Z M38 -24 A 11 11 0 1 0 60 -24 A 11 11 0 1 0 38 -24 Z"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Archivo+Narrow:wght@600;700&amp;family=IBM+Plex+Mono:wght@500;600&amp;family=Noto+Sans+JP:wght@900&amp;display=swap" rel="stylesheet">'

MAN_UP = FIG["MAN"].replace("C -28 -159 -29 -152 -29 -146 L -31 -122 L -32 -98 C -33 -90 -31 -84 -28 -84 C -25 -84 -24 -90 -25 -98 L -24 -122 L -22 -142 L -19 -139", "C -26 -158 -22 -150 -20 -140 L -19 -139")
WOMAN_UP = FIG["WOMAN"].replace("C -24 -159 -25 -152 -25 -146 L -27 -122 L -28 -98 C -29 -90 -27 -84 -24 -84 C -21 -84 -20 -90 -21 -98 L -20 -122 L -19 -141 L -16 -138", "C -22 -158 -19 -150 -17 -140 L -16 -138")
assert MAN_UP != FIG["MAN"] and WOMAN_UP != FIG["WOMAN"]
def arm(pts, color, w=10):
    """A free arm in figure-local units, from the shoulder (-22,-158) through elbow to hand. Use with ManUp/WomanUp."""
    d = "M" + " L ".join(f"{x} {y}" for x, y in pts)
    return (f'<path d="{d}" fill="none" stroke="#0D0D0F" stroke-width="{w+4}" stroke-linecap="round" stroke-linejoin="round"></path>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"></path>')
def defs(p, *names):
    m = {"Man": FIG["MAN"], "Woman": FIG["WOMAN"], "Hair": FIG["HAIR"], "Tunic": TUNIC, "Robe": ROBE, "Bow": BOW,
         "LieB": FIG["LIE_BODY"], "LieA": FIG["LIE_ARM"], "ManUp": MAN_UP, "WomanUp": WOMAN_UP}
    return "<defs>" + "".join(f'<path id="{p}{n}" d="{m[n]}"></path>' for n in names) + "</defs>"

def person(p, x, y, s, body="#2A1A10", cloth=None, kind="Robe", woman=False, hair=False, stroke="#0D0D0F", sw=3, flip=False, extra="", up=None, pre=""):
    """up: list of arm points (local) for a raised/free left arm; the figure's own left arm is removed."""
    sx = -s if flip else s
    fig = ("Woman" if woman else "Man") + ("Up" if up else "")
    o = f'<g transform="translate({x} {y}) scale({sx} {s})" fill="{body}">{pre}<use href="#{p}{fig}"></use>'
    if hair: o += f'<use href="#{p}Hair"' + (f' fill="{hair}"' if isinstance(hair, str) else '') + '></use>'
    if cloth: o += f'<use href="#{p}{kind}" fill="{cloth}" stroke="{stroke}" stroke-width="{sw}"></use>'
    if up: o += arm(up, body, 10)
    return o + extra + "</g>"

def page(title, rows, body, num=None, root_style=None):
    st = root_style or f"position: relative; width: 760px; height: 1080px; box-sizing: border-box; padding: 28px 26px 30px; background: #F3EFE6; color: #0D0D0F; font-family: 'IBM Plex Mono', monospace; display: grid; grid-template-rows: {rows}; gap: 12px"
    foot = f'\n  <span style="position: absolute; left: 0; right: 0; bottom: 9px; text-align: center; font-size: 9px; letter-spacing: 0.3em; color: #6B6862">— {num:02d} —</span>' if num is not None else ""
    props = '{"accent":{"editor":"color","default":"#D7261E","options":["#D7261E","#E8A317","#1F5FAD"]},"$preview":{"width":760,"height":1080}}' if root_style else '{"$preview":{"width":760,"height":1080}}'
    rv = "return { accent: this.props.accent ?? '#D7261E' };" if root_style else "return {};"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
</style>
</helmet>
<div style="{st}">
{body}{foot}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props}'>
class Component extends DCLogic {{
  renderVals() {{
    {rv}
  }}
}}
</script>
</body>
</html>
'''

def panel(bg, w, h, svg, over="", comment=""):
    c = f"\n  <!-- {comment} -->" if comment else ""
    return (f'{c}\n  <div style="position: relative; overflow: hidden; border: 3px solid #0D0D0F; background: {bg}">\n'
            f'    <svg viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; width: 100%; height: 100%; display: block">\n{svg}\n    </svg>\n{over}  </div>')

def cols(*panels, tmpl=None):
    t = tmpl or f"repeat({len(panels)}, minmax(0, 1fr))"
    return f'\n  <div style="display: grid; grid-template-columns: {t}; gap: 12px; min-height: 0">' + "".join(p.replace("\n  ", "\n    ") for p in panels) + "\n  </div>"

def cap(text, pos, size=11, center=False, maxw=None):
    mw = f" max-width: {maxw}px;" if maxw else ""
    ta = " text-align: center;" if center else ""
    return (f'    <div style="position: absolute; {pos};{mw} padding: 7px 10px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; '
            f'font-size: {size}px; font-weight: 600; line-height: 1.45; letter-spacing: 0.03em; text-transform: uppercase;{ta}">{text}</div>\n')

def god(text, pos, size=20, maxw=None):
    mw = f" max-width: {maxw}px;" if maxw else ""
    return (f'    <div style="position: absolute; {pos};{mw} padding: 13px 17px; background: #12113A; color: #F3EFE6; box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px #FFD23F; '
            f'font-family: Anton, sans-serif; font-size: {size}px; line-height: 1.14; letter-spacing: 0.04em; text-transform: uppercase">{text}</div>\n')

TAILS = {"dl": "M6 0 L 4 36 L 26 0", "dr": "M18 0 L 40 36 L 38 0", "ul": "M6 40 L 4 4 L 26 40", "ur": "M18 40 L 40 4 L 38 40",
         "l": "M44 6 L 2 20 L 44 30", "r": "M0 6 L 42 20 L 0 30"}
def tail(left, top, d="dl"):
    return (f'    <svg width="44" height="40" viewBox="0 0 44 40" style="position: absolute; left: {left}px; top: {top}px; display: block">'
            f'<path d="{TAILS[d]}" fill="#ffffff" stroke="#0D0D0F" stroke-width="2.5" stroke-linejoin="round"></path></svg>\n')

def balloon(text, pos, width, size=16, pad="14px 22px"):
    return (f'    <div style="position: absolute; {pos}; width: {width}px; box-sizing: border-box; padding: {pad}; background: #ffffff; color: #0D0D0F; border: 2.5px solid #0D0D0F; border-radius: 50%; '
            f"font-family: 'Archivo Narrow', sans-serif; font-weight: 700; font-size: {size}px; line-height: 1.15; text-transform: uppercase; text-align: center\">{text}</div>\n")

KANJI = "〇一二三四五六七八九"
def kanji_num(n):
    if n < 10: return KANJI[n]
    t, u = divmod(n, 10)
    return ("" if t == 1 else KANJI[t]) + "十" + (KANJI[u] if u else "")

def stamp(ch, pos, rot=4):
    return (f'    <div style="position: absolute; {pos}; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 5px 10px 4px; border: 2.5px solid #D7261E; color: #D7261E; background: #F3EFE6; transform: rotate({rot}deg)">\n'
            f'      <span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 18px; line-height: 1">第{kanji_num(ch)}章</span>\n'
            f'      <span style="font-size: 8px; font-weight: 600; letter-spacing: 0.16em">CHAPTER {ch}</span>\n    </div>\n')

def sfx(jp, roman, pos, size=46, fill="#0D0D0F", stroke="#F3EFE6", rot=-6, tagbg=None, tagfg=None, align="flex-end"):
    tb = tagbg or fill; tf = tagfg or stroke
    return (f'    <div style="position: absolute; {pos}; display: flex; flex-direction: column; align-items: {align}; transform: rotate({rot}deg)">\n'
            f'      <span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: {size}px; line-height: 1; color: {fill}; -webkit-text-stroke: 4px {stroke}; paint-order: stroke fill">{jp}</span>\n'
            f'      <span style="margin-top: 1px; padding: 1px 4px; background: {tb}; color: {tf}; font-size: 9px; font-weight: 600; letter-spacing: 0.24em">{roman}</span>\n    </div>\n')

def ref(text, pos, color="#F3EFE6", bg=None):
    b = f" padding: 1px 5px; background: {bg};" if bg else ""
    return f'    <span style="position: absolute; {pos};{b} color: {color}; font-size: 9px; font-weight: 600; letter-spacing: 0.18em">{text}</span>\n'

def speed(cx, cy, n, r0, r1, seed, color="#ffffff", sw=1.4, op=0.6):
    import math
    r = random.Random(seed); o = []
    for i in range(n):
        a = r.uniform(0, 6.283); ra = r.uniform(r0, r0 * 1.6)
        o.append(f'<path d="M{cx + math.cos(a)*ra:.0f} {cy + math.sin(a)*ra:.0f} L {cx + math.cos(a)*r1:.0f} {cy + math.sin(a)*r1:.0f}"></path>')
    return f'<g stroke="{color}" stroke-width="{sw}" opacity="{op}">' + "".join(o) + "</g>"

def stars(n, w, h, seed, color="#F3EFE6"):
    r = random.Random(seed)
    return f'<g fill="{color}">' + "".join(f'<circle cx="{r.uniform(0,w):.0f}" cy="{r.uniform(0,h):.0f}" r="{r.choice([0.6,0.8,1,1.2,1.6])}"></circle>' for _ in range(n)) + "</g>"

def face(tok, x, y, s, flip=False):
    sx = -s if flip else s
    return f'<g transform="translate({x} {y}) scale({sx} {s})">{tok}</g>'
