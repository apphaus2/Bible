"""Shared page kit for the full edition: panels from lifted or new art, verse labels, day stamps, chapter title pages.
Text always comes from asv.Book (never typed by hand); this module only places it."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "kit"))
import mk
from mk import cols, cap, god, tail, balloon, sfx, kanji_num

def use(art, extra="", over="", comment=""):
    """A panel built from lifted digest art (reuse.Art), with optional extra SVG on top."""
    return mk.panel(art.bg, art.w, art.h, art.svg + extra, over, comment)

def new(bg, w, h, svg, over="", comment=""):
    return mk.panel(bg, w, h, svg, over, comment)

def vref(text, pos="right: 8px; bottom: 7px"):
    """A small verse label, e.g. 'GEN 1:1–2'."""
    return mk.ref(text, pos, color="#0D0D0F", bg="#F3EFE6")

def day_stamp(n, pos, rot=-4):
    words = ["", "FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH"]
    return (f'    <div style="position: absolute; {pos}; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 5px 10px 4px; border: 2.5px solid #D7261E; color: #D7261E; background: #F3EFE6; transform: rotate({rot}deg)">\n'
            f'      <span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 18px; line-height: 1">第{kanji_num(n)}日</span>\n'
            f'      <span style="font-size: 8px; font-weight: 600; letter-spacing: 0.16em">THE {words[n]} DAY</span>\n    </div>\n')

def page(title, rows, body, num):
    return mk.page(title, rows, body, num)

def chapter_title(num, kanji_ep, title, rng, art_svg, bg, quote_text, credit):
    """A chapter opener: full-bleed art, the episode number (第一話), the title, the verse range and one quoted line."""
    body = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; display: block">{art_svg}</svg>
  <div style="position: absolute; left: 38px; top: 40px; display: flex; align-items: center; gap: 14px">
    <span style="padding: 10px 12px; background: #D7261E; color: #F3EFE6; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 30px; line-height: 1">{kanji_ep}</span>
    <span style="font-size: 12px; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: #F3EFE6">Chapter {num}</span>
  </div>
  <h1 data-label style="position: absolute; left: 34px; top: 100px; margin: 0; max-width: 680px; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 96px; line-height: 1.0; letter-spacing: -0.5px; color: #F3EFE6; text-transform: uppercase; text-shadow: 4px 4px 0 #0D0D0F">{title}</h1>
  <div data-label style="position: absolute; left: 38px; top: 330px; font-size: 13px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">{rng}</div>
  <div style="position: absolute; left: 38px; bottom: 70px; max-width: 420px; padding: 9px 13px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 14px; font-weight: 600; line-height: 1.45; letter-spacing: 0.04em; text-transform: uppercase">{quote_text}</div>
  <div data-label style="position: absolute; left: 38px; right: 38px; bottom: 30px; font-size: 10px; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.85">{credit}</div>'''
    root = f"position: relative; width: 760px; height: 1080px; overflow: hidden; background: {bg}; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page(f"{rng} — Chapter {num}: {title}", None, body, root_style=root)

def end_mark(text, pos, ch="つづく"):
    return (f'    <div style="position: absolute; {pos}; display: flex; align-items: center; gap: 8px; padding: 4px 10px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 2px #FFD23F">'
            f'<span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 20px">{ch}</span><span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em">{text}</span></div>\n')
