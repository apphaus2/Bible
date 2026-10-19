import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, samuel2 as S2, exodus as E
from num.art import ALL
from genesis.art2 import hills, fit
from psa import G
from psa import art as K

def cover():
    """David the shepherd with his harp on the hillside under the night sky, his flock about him (full-bleed)."""
    w, h = 760, 820
    art = (mk.defs("cv", *ALL) + K.sky(w, h, "#05051A", "#3A2A6A") + mk.stars(260, w, h * 0.7, 19) + K.moon(w * 0.8, h * 0.3, 26)
           + f'<path d="M-10 {h * 0.5} C {w * 0.3} {h * 0.2} {w * 0.6} {h * 0.3} {w + 10} {h * 0.05}" stroke="#8A8AC8" stroke-width="{h * 0.12}" fill="none" opacity="0.16"></path>'
           + hills(w, h, h * 0.66, 19, color="#1A1A3A", amp=14)
           + f'<path d="M-10 {h + 10} L -10 {h * 0.78} C {w * 0.3} {h * 0.7} {w * 0.6} {h * 0.72} {w + 10} {h * 0.8} L {w + 10} {h + 10} Z" fill="#2A2A4A" stroke="#0D0D0F" stroke-width="2"></path>'
           + "".join(E.sheep(w * x, h * y, 0.9, flip=i % 2 == 1, wool="#C8C8D8") for i, (x, y) in enumerate(((0.56, 0.86), (0.66, 0.9), (0.76, 0.87), (0.86, 0.92), (0.62, 0.96))))
           + K.shepherd("cv", w * 0.3, h * 0.9, fit(h * 0.9, h * 0.56)) + S2.harp(w * 0.3 + 46, h * 0.72, 0.8))
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">'
           f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 260)">{art}</g></svg>'
           '<div style="position: absolute; left: 0; right: 0; top: 0; height: 420px; background: linear-gradient(180deg, rgba(5,5,26,1) 0%, rgba(5,5,26,0.8) 60%, rgba(5,5,26,0) 100%)"></div>')
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Book of</span>
  </div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 160px; line-height: 1.0; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">PSALMS</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Nineteen</span>
    <span style="font-weight: 500; opacity: 0.85">Psalms 1 – 150</span>
  </div>
  <div style="position: absolute; top: 226px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 44px; line-height: 1.02; color: #F3EFE6"><span>詩</span><span>篇</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">SHIHEN</span>
  </div>
  <div style="position: absolute; left: 38px; top: 320px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("150:6", to="praise Jehovah.")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 19</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #05051A; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Psalms — Volume Nineteen", None, body, root_style=root)
