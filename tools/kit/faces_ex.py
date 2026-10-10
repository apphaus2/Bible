import faces
BAND = '\n<path d="M238 104 C 206 98 160 94 100 108" fill="none" stroke="#0D0D0F" stroke-width="7.5" stroke-linecap="round"></path><path d="M238 104 C 206 98 160 94 100 108" fill="none" stroke="#E8B830" stroke-width="5" stroke-linecap="round"></path><circle cx="230" cy="102" r="5" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1.4"></circle>'
CORD = '\n<path d="M238 100 C 206 92 160 88 98 104" fill="none" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path><path d="M238 100 C 206 92 160 88 98 104" fill="none" stroke="#3A2214" stroke-width="6" stroke-linecap="round"></path>'
def F(*a, band=False, cord=False, **k):
    s = faces.face(*a, **k)
    return s + (BAND if band else "") + (CORD if cord else "")
def tokens():
    t = {}
    t["__FACE_MOSES__"] = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True)
    t["__FACE_MOSES_FIRE__"] = F("adam", skin="#E8A06A", shadow="#8A3A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, brow="sorrow", light="#FFD23F")
    t["__FACE_MOSES_AFRAID__"] = F("adam", skin="#E8A06A", shadow="#8A3A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, brow="sorrow", sweat=True, light="#FF8A3D")
    t["__FACE_MOSES_PRINCE__"] = F("adam", skin="#D9A27A", shadow="#9A6A4A", egypt=("#F3EFE6", "#D7261E"), collar=True, kohl=True)
    t["__FACE_MOSES_ANGRY__"] = F("adam", skin="#C47A5A", shadow="#5A1A16", egypt=("#F3EFE6", "#D7261E"), collar=True, kohl=True, brow="scowl", light="#FF6A4A")
    t["__FACE_PRINCESS__"] = F("eve", skin="#D9A27A", shadow="#9A6A4A", hair="#0D0D0F", collar=True, kohl=True, band=True)
    t["__FACE_MIRIAM__"] = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22")
    t["__FACE_JOCHEBED__"] = F("eve", skin="#DDA684", shadow="#A87050", hair="#2A1A10", scarf="#5A6E8A", brow="sorrow")
    t["__FACE_ZIPPORAH__"] = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#1A1210", scarf="#B5421E")
    t["__FACE_PHARAOH_NEW__"] = F("adam", skin="#B9785A", shadow="#5A2A1E", egypt=("#0D0D0F", "#E8B830"), collar=True, kohl=True, false_beard=True, brow="scowl", light="#FF6A4A")
    t["__FACE_TASKMASTER__"] = F("adam", skin="#B9785A", shadow="#6A3A2A", egypt=("#E8E2D6", "#A89E86"), brow="scowl", kohl=True)
    t["__FACE_SLAVE__"] = F("adam", skin="#B98A6E", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", brow="sorrow", sweat=True, stubble="#2A1A10")
    t["__FACE_HEBREW_ANGRY__"] = F("adam", skin="#B98A6E", shadow="#5E3A2A", hair="#1A1210", hl="#4A3A2E", brow="scowl", stubble="#2A1A10")
    return t
