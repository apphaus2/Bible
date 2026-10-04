import pathlib, re, json
B = pathlib.Path(__file__).parent
FIG = json.loads((B/"figures.json").read_text())
TUNIC = "M-25 -164 C -31 -150 -33 -120 -28 -58 L -18 -62 L -8 -55 L 2 -62 L 12 -55 L 22 -62 L 28 -58 C 33 -120 31 -150 25 -164 C 14 -170 -14 -170 -25 -164 Z"
def _inner(p):
    s = (B/p).read_text()
    return re.sub(r'^<g id="[A-Z]+">\n', '', s).rsplit('</g>', 1)[0]
def face(base="adam", skin=None, shadow=None, hair=None, hl=None, brow=None, beard=False, sigil=False, light=None, scarf=None, laugh=False, beard_color=None, blind=False, tear=False, sweat=False, stubble=None, egypt=None, collar=False, kohl=False, false_beard=False):
    s = _inner(f"faces/{base}.svg")
    d_skin, d_sh = ("#D9A27A", "#A8684A") if base == "adam" else ("#E3B08A", "#B97A58")
    if skin: s = s.replace(d_skin, skin)
    if shadow: s = s.replace(d_sh, shadow)
    if hair and base == "eve": s = s.replace('fill="#3A1E14" stroke="#0D0D0F" stroke-width="2"', f'fill="{hair}" stroke="#0D0D0F" stroke-width="2"').replace('stroke="#3A1E14" stroke-width="2.4"', f'stroke="{hair}" stroke-width="2.4"')
    if hair: s = s.replace('fill="#1A1210" stroke="#0D0D0F" stroke-width="2"', f'fill="{hair}" stroke="#0D0D0F" stroke-width="2"').replace('stroke="#1A1210" stroke-width="4.5"', f'stroke="{hair}" stroke-width="4.5"')
    if hl: s = s.replace('stroke="#5A4A3E"', f'stroke="{hl}"')
    if brow == "scowl":
        s = s.replace('M198 154 C 212 147 226 148 237 155', 'M198 148 C 212 151 226 157 238 163')
        s = s.replace('M206 168 C 214 162 224 161 231 170', 'M206 167 C 214 164 224 164 231 170')
    if brow == "sorrow":
        s = s.replace('M198 154 C 212 147 226 148 237 155', 'M198 158 C 210 150 222 146 234 152')
    if beard:
        s += ('\n<path d="M166 246 C 178 280 198 304 222 316 C 240 318 252 304 250 284 C 248 270 244 262 240 260 C 236 262 238 270 232 274 C 226 286 214 292 200 290 C 186 286 174 270 166 246 Z" fill="%s" stroke="#0D0D0F" stroke-width="1.8" stroke-linejoin="round"></path>'
              '\n<path d="M212 238 C 222 231 238 231 245 238 C 246 244 240 248 234 246 C 228 249 220 248 212 244 Z" fill="%s" stroke="#0D0D0F" stroke-width="1.4"></path>'
              '\n<g fill="none" stroke="#8A867E" stroke-width="1.2" stroke-linecap="round"><path d="M190 272 C 196 286 206 298 216 306"></path><path d="M206 270 C 212 286 222 298 232 306"></path><path d="M180 262 C 186 278 196 292 206 302"></path></g>'
              '\n<g fill="none" stroke="#7A5038" stroke-width="1.2" opacity="0.7"><path d="M200 186 C 206 192 212 194 218 194"></path><path d="M206 132 C 214 130 222 130 230 132"></path><path d="M204 140 C 212 138 222 138 230 140"></path></g>') % (hair or "#E8E2D6", hair or "#E8E2D6")
    if blind:
        s = s.replace('<ellipse cx="224" cy="170.5" rx="3" ry="4" fill="#2A1A10"></ellipse>', '<ellipse cx="224" cy="170.5" rx="3" ry="4" fill="#C8D0D6"></ellipse>')
        s = s.replace('<circle cx="225" cy="169" r="0.9" fill="#ffffff"></circle>', '')
    if tear:
        s += '\n<path d="M226 176 C 228 186 224 196 226 206 C 228 212 222 214 220 208 C 218 200 222 190 226 176 Z" fill="#CFEFFF" stroke="#2C7DA0" stroke-width="1"></path>'
    if sweat:
        s += '\n<g fill="#CFEFFF" stroke="#2C7DA0" stroke-width="1"><path d="M210 112 C 214 120 214 126 210 128 C 206 126 206 120 210 112 Z"></path><path d="M244 196 C 247 202 247 206 244 208 C 241 206 241 202 244 196 Z"></path></g>'
    if stubble:
        s += ('\n<path d="M168 246 C 180 274 200 296 222 306 C 238 306 244 296 242 284 C 238 276 236 270 232 272 C 226 284 214 290 200 288 C 186 284 176 268 168 246 Z" fill="%s" opacity="0.75"></path>' % stubble)
    if kohl:
        s += '\n<path d="M206 170 C 214 165 224 164 233 168 L 246 164" fill="none" stroke="#0D0D0F" stroke-width="2.6" stroke-linecap="round"></path><path d="M210 174 C 218 177 226 176 232 172" fill="none" stroke="#0D0D0F" stroke-width="1.4"></path>'
    if egypt:
        import re as _re2
        s = _re2.sub(r'<path d="M234 106 C 240 96.*?</path>\n  <g fill="none" stroke="#[0-9A-Fa-f]{6}" stroke-width="1.5" stroke-linecap="round">.*?</g>\n', '', s, flags=_re2.S)
        a, b = egypt
        s += ('\n<defs><pattern id="nemes%s" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(8)"><rect width="12" height="12" fill="%s"></rect><rect width="12" height="5" fill="%s"></rect></pattern></defs>'
              '\n<path d="M236 108 C 240 84 222 44 172 38 C 120 34 90 70 86 114 C 84 150 92 190 96 230 C 100 290 108 340 112 392 L 162 392 C 156 330 148 270 150 240 C 150 210 148 190 152 176 C 156 150 168 132 186 122 C 204 114 222 110 236 108 Z" fill="url(#nemes%s)" stroke="#0D0D0F" stroke-width="2.2" stroke-linejoin="round"></path>'
              '\n<path d="M236 108 C 210 112 186 120 172 132" fill="none" stroke="#0D0D0F" stroke-width="5"></path><path d="M236 108 C 210 112 186 120 172 132" fill="none" stroke="#E8B830" stroke-width="3"></path>') % (a[1:]+b[1:], a, b, a[1:]+b[1:])
    if collar:
        s += ('\n<path d="M140 380 C 150 340 180 320 216 330 C 240 336 256 352 262 380 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
              '\n<g fill="none" stroke="#1F5FAD" stroke-width="4"><path d="M150 370 C 162 344 188 334 214 340 C 236 344 248 358 254 376"></path></g><path d="M156 378 C 168 356 190 348 212 352 C 232 356 242 366 246 380" fill="none" stroke="#D7261E" stroke-width="3"></path>')
    if false_beard:
        s += '\n<path d="M226 300 L 222 350 L 238 350 L 240 300 Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.6"></path><g stroke="#E8B830" stroke-width="2"><path d="M223 314 L 239 314 M223 328 L 239 328 M222 342 L 238 342"></path></g>'
    if laugh:
        import re as _re
        s = _re.sub(r'<path d="M209 171 C 215 165.*?</path>\n  <ellipse cx="224".*?</ellipse>\n  <circle cx="225" cy="169".*?</circle>\n', '<path d="M209 171 C 215 175 223 175 229 170" fill="none" stroke="#0D0D0F" stroke-width="2.4" stroke-linecap="round"></path>\n', s, flags=_re.S)
        s += '\n<path d="M226 252 C 230 256 236 256 240 250" fill="none" stroke="#0D0D0F" stroke-width="2" stroke-linecap="round"></path><path d="M196 240 C 204 236 210 238 214 244" fill="none" stroke="#B97A58" stroke-width="1.6" stroke-linecap="round"></path>'
    if scarf and base == "adam":
        import re as _re3
        s = _re3.sub(r'<path d="M234 106 C 240 96.*?</path>\n  <g fill="none" stroke="#[0-9A-Fa-f]{6}" stroke-width="1.5" stroke-linecap="round">.*?</g>\n', '', s, flags=_re3.S)
    if scarf:
        s += ('\n<path d="M238 106 C 242 80 222 38 170 32 C 118 28 84 70 82 122 C 80 182 90 262 92 392 L 158 392 C 152 300 146 214 150 182 C 154 152 166 132 184 122 C 202 112 220 108 238 106 Z" fill="%s" stroke="#0D0D0F" stroke-width="2.2" stroke-linejoin="round"></path>'
              '\n<g fill="none" stroke="#0D0D0F" stroke-width="1.2" opacity="0.45"><path d="M228 70 C 200 50 150 48 110 80"></path><path d="M110 120 C 106 200 110 290 112 390"></path><path d="M132 140 C 128 220 130 300 134 390"></path></g>'
              '\n<path d="M232 76 C 206 56 160 52 120 76" fill="none" stroke="#F3EFE6" stroke-width="3" opacity="0.5"></path>') % scarf
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
    t["__FACE_ABRAM__"] = face("adam", skin="#C98E66", shadow="#8A5A3E", hair="#B8B2A6", hl="#8A867E", beard=True, light="#FFE680")
    t["__FACE_ABRAM_STARS__"] = face("adam", skin="#9A7A8A", shadow="#4A3A6E", hair="#C8C2D6", hl="#8A86A6", beard=True, light="#CFE0FF")
    t["__FACE_SARAH__"] = face("eve", skin="#DDA684", shadow="#A87050", hair="#C8C2B6", scarf="#C9A86A", laugh=True)
    t["__FACE_ISAAC__"] = face("adam", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22", hl="#8A6A4A")
    t["__FACE_JACOB__"] = face("adam", skin="#D9A27A", shadow="#A8684A", hair="#2A1A10", hl="#5A4A3E")
    t["__FACE_JACOB_STRAIN__"] = face("adam", skin="#C98E66", shadow="#5A3A4A", hair="#2A1A10", hl="#5A4A3E", brow="scowl", sweat=True, light="#FFC98A")
    t["__FACE_JACOB_AWE__"] = face("adam", skin="#B9A6B8", shadow="#4A3A6E", hair="#1A1210", hl="#6A5A7E", brow="sorrow", light="#FFF4C2")
    t["__FACE_ESAU__"] = face("adam", skin="#C47A5A", shadow="#8A4A32", hair="#B5421E", hl="#E06A3A", stubble="#B5421E")
    t["__FACE_ESAU_CRY__"] = face("adam", skin="#C47A5A", shadow="#6A3A3A", hair="#B5421E", hl="#E06A3A", stubble="#B5421E", brow="sorrow", tear=True)
    t["__FACE_ISAAC_OLD__"] = face("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, blind=True)
    t["__FACE_RACHEL__"] = face("eve", skin="#E3B08A", shadow="#B97A58", hair="#1A1210")
    t["__FACE_JOSEPH__"] = face("adam", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22", hl="#8A6A4A")
    t["__FACE_JOSEPH_EGYPT__"] = face("adam", skin="#D9A27A", shadow="#9A6A4A", egypt=("#1F5FAD", "#E8B830"), collar=True, kohl=True)
    t["__FACE_JOSEPH_WEEP__"] = face("adam", skin="#D9A27A", shadow="#8A5A5A", egypt=("#1F5FAD", "#E8B830"), collar=True, kohl=True, brow="sorrow", tear=True)
    t["__FACE_PHARAOH__"] = face("adam", skin="#C98E66", shadow="#8A5A3E", egypt=("#E8B830", "#1F5FAD"), collar=True, kohl=True, false_beard=True, light="#FFE680")
    t["__FACE_JACOB_OLD_WEEP__"] = face("adam", skin="#C98E66", shadow="#6A4A5A", hair="#C8C2B6", hl="#8A867E", beard=True, brow="sorrow", tear=True)
    return t
def build(paths):
    t = tokens()
    for p in paths:
        s = pathlib.Path(p).read_text()
        for k, v in t.items(): s = s.replace(k, v)
        left = re.findall(r"__[A-Z_]+__", s)
        assert not left, (p, left)
        pathlib.Path(p).write_text(s)
