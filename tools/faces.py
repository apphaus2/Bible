import pathlib, re, json
B = pathlib.Path(__file__).parent
FIG = json.loads((B/"figures.json").read_text())
TUNIC = "M-25 -164 C -31 -150 -33 -120 -28 -58 L -18 -62 L -8 -55 L 2 -62 L 12 -55 L 22 -62 L 28 -58 C 33 -120 31 -150 25 -164 C 14 -170 -14 -170 -25 -164 Z"
def _inner(p):
    s = (B/p).read_text()
    return re.sub(r'^<g id="[A-Z]+">\n', '', s).rsplit('</g>', 1)[0]
def face(base="adam", skin=None, shadow=None, hair=None, hl=None, brow=None, beard=False, sigil=False, light=None):
    s = _inner(f"faces/{base}.svg")
    d_skin, d_sh = ("#D9A27A", "#A8684A") if base == "adam" else ("#E3B08A", "#B97A58")
    if skin: s = s.replace(d_skin, skin)
    if shadow: s = s.replace(d_sh, shadow)
    if hair: s = s.replace('fill="#1A1210" stroke="#0D0D0F" stroke-width="2"', f'fill="{hair}" stroke="#0D0D0F" stroke-width="2"').replace('stroke="#1A1210" stroke-width="4.5"', f'stroke="{hair}" stroke-width="4.5"')
    if hl: s = s.replace('stroke="#5A4A3E"', f'stroke="{hl}"')
    if brow == "scowl":
        s = s.replace('M198 154 C 212 147 226 148 237 155', 'M198 148 C 212 151 226 157 238 163')
        s = s.replace('M206 168 C 214 162 224 161 231 170', 'M206 167 C 214 164 224 164 231 170')
    if brow == "sorrow":
        s = s.replace('M198 154 C 212 147 226 148 237 155', 'M198 158 C 210 150 222 146 234 152')
    if beard:
        s += ('\n<path d="M166 246 C 178 280 198 304 222 316 C 240 318 252 304 250 284 C 248 270 244 262 240 260 C 236 262 238 270 232 274 C 226 286 214 292 200 290 C 186 286 174 270 166 246 Z" fill="%s" stroke="#0D0D0F" stroke-width="1.8" stroke-linejoin="round"></path>'
              '\n<path d="M226 240 C 234 238 244 240 248 246 C 242 248 234 248 226 246 Z" fill="%s" stroke="#0D0D0F" stroke-width="1.4"></path>'
              '\n<g fill="none" stroke="#8A867E" stroke-width="1.2" stroke-linecap="round"><path d="M190 272 C 196 286 206 298 216 306"></path><path d="M206 270 C 212 286 222 298 232 306"></path><path d="M180 262 C 186 278 196 292 206 302"></path></g>'
              '\n<g fill="none" stroke="#7A5038" stroke-width="1.2" opacity="0.7"><path d="M200 186 C 206 192 212 194 218 194"></path><path d="M206 132 C 214 130 222 130 230 132"></path><path d="M204 140 C 212 138 222 138 230 140"></path></g>') % (hair or "#E8E2D6", hair or "#E8E2D6")
    if sigil:
        s += ('\n<g transform="translate(222 124)"><circle r="16" fill="#FFD23F" opacity="0.25"></circle><circle r="9" fill="none" stroke="#FFD23F" stroke-width="2.2"></circle>'
              '<path d="M0 -13 L 0 13 M-13 0 L 13 0" stroke="#FFD23F" stroke-width="1.8"></path><circle r="2.4" fill="#ffffff"></circle></g>')
    if light:
        s += f'\n<path d="M230 110 C 234 130 236 145 236 158 C 236 164 232 168 231 172 C 240 188 252 204 262 218" fill="none" stroke="{light}" stroke-width="3" stroke-linecap="round" opacity="0.9"></path>'
    return s
TOKENS = {
  "__MAN__": FIG["MAN"], "__WOMAN__": FIG["WOMAN"], "__HAIR__": FIG["HAIR"], "__TUNIC__": TUNIC,
  "__LIEB__": FIG["LIE_BODY"], "__LIEA__": FIG["LIE_ARM"],
}
def tokens():
    t = dict(TOKENS)
    t["__FACE_CAIN_ANGRY__"] = face("adam", skin="#C47A5A", shadow="#5A1A16", brow="scowl", light="#FF6A4A")
    t["__FACE_CAIN__"] = face("adam", skin="#B98A6E", shadow="#5E4A5A", brow="scowl")
    t["__FACE_CAIN_MARK__"] = face("adam", skin="#B98A6E", shadow="#4A3A5E", brow="sorrow", sigil=True, light="#FFD23F")
    t["__FACE_NOAH__"] = face("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#E8E2D6", hl="#B8B2A6", brow="sorrow", beard=True, light="#FFF4C2")
    return t
def build(paths):
    t = tokens()
    for p in paths:
        s = pathlib.Path(p).read_text()
        for k, v in t.items(): s = s.replace(k, v)
        left = re.findall(r"__[A-Z_]+__", s)
        assert not left, (p, left)
        pathlib.Path(p).write_text(s)
