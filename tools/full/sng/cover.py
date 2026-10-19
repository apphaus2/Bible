import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from sng import G
from sng import art as K

def scene(w, h, seed=7):
    """The cover's landscape: evening over the hills, a young hart leaping on the far mountain, vineyards on the slopes and
    lilies and roses in the foreground."""
    r = random.Random(seed)
    o = [K.sky(w, h, "#3A1A4A", "#F3A07A"), K.sun(w * 0.7, h * 0.56, 40, color="#FFD8A0", op=0.35),
         K.hills(w, h, h * 0.58, seed, color="#5A3A5A", amp=34, step=80), K.roe(w * 0.28, h * 0.56, 0.9, hart=True, pose="leap", color="#2A1A2A"),
         K.hills(w, h, h * 0.66, seed + 1, color="#6A5A4A", amp=16, step=90), K.vine_rows(w, h, h * 0.72, h * 0.86, seed, rows=3, blossom=True)]
    for _ in range(9):
        o.append(K.flower(r.uniform(20, w - 20), r.uniform(h * 0.95, h * 1.02), r.uniform(1.1, 1.6), r.choice(["lily", "lily", "rose"]), r.randint(1, 99)))
    return "".join(o)

def cover():
    """Evening over the hills of the Song: a young hart leaping on the mountain, vineyards in blossom, lilies (full-bleed)."""
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">{scene(760, 1080)}</svg>'
           '<div style="position: absolute; left: 0; right: 0; top: 0; height: 470px; background: linear-gradient(180deg, rgba(58,26,74,1) 0%, rgba(58,26,74,0.8) 64%, rgba(58,26,74,0) 100%)"></div>')
    body = svg + f'''
  <h1 style="position: absolute; top: 34px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; line-height: 1.0; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F"><span style="display: block; font-size: 64px; letter-spacing: 0">THE SONG OF</span><span style="display: block; font-size: 136px">SOLOMON</span></h1>
  <div style="position: absolute; top: 254px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 270px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Twenty-Two</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 8</span>
  </div>
  <div style="position: absolute; top: 250px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.02; color: #F3EFE6"><span>雅</span><span>歌</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">GAKA</span>
  </div>
  <div style="position: absolute; left: 38px; top: 340px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("2:1")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 22</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #3A1A4A; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Song of Solomon — Volume Twenty-Two", None, body, root_style=root)
