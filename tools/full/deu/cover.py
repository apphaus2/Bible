import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus5 as V
from deu import G, art as K

def cover():
    """Moses on the rise in the plains of Moab, his hand raised over all Israel at dusk; the Jordan and Jericho beyond."""
    w, h = 760, 1080
    svg = (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; display: block">'
           + V.rays(120, 640, 40, 40, 1100, color="#FFC14D", op=0.12) + f'<g transform="translate(0 300)">{K.address("cv", w, 780, 501, raise_hand=True, dusk=True)}</g>' + '</svg>')
    svg += '<div style="position: absolute; left: 0; right: 0; top: 0; height: 440px; background: linear-gradient(180deg, rgba(42,26,58,1) 0%, rgba(42,26,58,0.85) 60%, rgba(42,26,58,0) 100%)"></div>'
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Fifth Book of Moses</span>
  </div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 96px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">DEUTERONOMY</h1>
  <div style="position: absolute; top: 250px; left: 38px; width: 300px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 266px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Five</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 34</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; margin-top: 30px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>申</span><span>命</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHINMEIKI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 340px; padding: 8px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 14px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 340px; line-height: 1.45">{G.v("6:4")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 5</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #2A1A3A; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Deuteronomy — Volume Five", None, body, root_style=root)
