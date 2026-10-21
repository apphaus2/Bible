import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from ezk import G
from ezk import art as K
from num.art import ALL

def cover():
    """The visions of God: the throne of sapphire above the firmament, fire and brightness and the bow round about it (no
    figure), and under the crystal the four living creatures with their wheels (full-bleed)."""
    p = "cv"
    art = (K.throne(760, 1080, 2601) + mk.defs(p, *ALL)
           + "".join(K.wheel(x, 1010, 40, 2602 + i, tilt=t) for i, (x, t) in enumerate(((90, -8), (290, 6), (470, -6), (670, 8))))
           + "".join(K.creature(p, x, 1000, 0.82, 2610 + i, spread="level") for i, x in enumerate((150, 300, 460, 610)))
           + K.vgrad("cvb", [(0, "rgba(5,5,26,0)"), (1, "rgba(5,5,26,0.95)")]) + '<rect x="0" y="960" width="760" height="120" fill="url(#cvb)"></rect>')
    svg = f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">{art}</svg>'
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Book of</span><span>No. 26</span>
  </div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 136px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">EZEKIEL</h1>
  <div style="position: absolute; top: 222px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 238px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Twenty-Six</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 48</span>
  </div>
  <div style="position: absolute; top: 226px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 38px; line-height: 1.02; color: #F3EFE6"><span>エ</span><span>ゼ</span><span>キ</span><span>エ</span><span>ル</span><span>書</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.1em; color: #F3EFE6">EZEKIERU-SHO</span>
  </div>
  <div style="position: absolute; left: 38px; top: 306px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("1:1", frm="the heavens were opened")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 26</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #05051A; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Ezekiel — Volume Twenty-Six", None, body, root_style=root)
