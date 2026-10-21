"""ref/KorRV/*.usfm from CrossWire's SWORD module KorRV (Korean Revised Version 1952/1961, 개역; TextSource=Wikisource,
DistributionLicense=Public Domain; korrv.conf beside this file). eBible.org's Korean text ("kor") is the same translation,
but its file loses 74 Old Testament verses and renumbers the chapters around them, so the manga uses this one.

    python ref/KorRV/sword2usfm.py <unzipped KorRV.zip>/modules/texts/ztext/korrv ref/KorRV

The module's verse index (NRSV versification) is walked with the ASV's chapter and verse counts, which are the same in the
Old Testament; in the New, NRSV has a 3 John 1:15 and a Revelation 12:18. Psalm superscriptions become \\d lines. A verse
the module joins to the one before it is left empty (its editors' notes "(앞절과 동일)", "상동", "8절과 같음", "(없음)"
dropped): asv.Book cuts the joined verse back into its slots ("merged" in tools/lang/ko.json)."""
import sys, pathlib, struct, zlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "full"))
import asv
NAMES = [n.replace("_", " ") for n in (
    "창세기 출애굽기 레위기 민수기 신명기 여호수아 사사기 룻기 사무엘상 사무엘하 열왕기상 열왕기하 역대상 역대하 에스라 느헤미야 "
    "에스더 욥기 시편 잠언 전도서 아가 이사야 예레미야 예레미야_애가 에스겔 다니엘 호세아 요엘 아모스 오바댜 요나 미가 나훔 하박국 "
    "스바냐 학개 스가랴 말라기 마태복음 마가복음 누가복음 요한복음 사도행전 로마서 고린도전서 고린도후서 갈라디아서 에베소서 빌립보서 "
    "골로새서 데살로니가전서 데살로니가후서 디모데전서 디모데후서 디도서 빌레몬서 히브리서 야고보서 베드로전서 베드로후서 요한일서 "
    "요한이서 요한삼서 유다서 요한계시록").split()]
FILES = [(c, f) for c, f in asv.FILES.items() if c not in ("FRT", "INT")]
assert len(FILES) == 66 == len(NAMES)
ADJ = {("3JN", 1): 15, ("REV", 12): 18}
# the module's copying slips, each checked against eBible's transcription of the same text (ebible.org/kor): Proverbs 13:10
# carries all of 13:11 again at its end; Isaiah 45:22 그리하며 for 그리하면; Song of Solomon 6:13 lacks its first half
# (eBible's 6:13); and 어호와 for 여호와 (seven times)
FIX = {("PRO", 13, 10): (" 망령되이 얻은 재물은 줄어가고 손으로 모은 것은 늘어가느니라", ""),
       ("ISA", 45, 22): ("그리하며 구원을", "그리하면 구원을"),
       ("SNG", 6, 13): ("", "돌아오고 돌아오라 술람미 여자야 돌아오고 돌아오라 우리로 너를 보게 하라 ")}
NOTE = re.compile(r"\(?(?:앞절과 |\d+절과 )?(?:상동|같음|동일|없음)\)?")

def reader(mod, t):
    bzs, bzv, bzz = ((mod / f"{t}.{x}").read_bytes() for x in ("bzs", "bzv", "bzz"))
    blocks = [struct.unpack_from("<III", bzs, i) for i in range(0, len(bzs), 12)]
    cache = {}
    def entry(i):
        b, off, size = struct.unpack_from("<IIH", bzv, i * 10)
        if size == 0: return ""
        if b not in cache:
            o, s, _ = blocks[b]; cache[b] = zlib.decompress(bzz[o:o + s])
        return cache[b][off:off + size].decode("utf-8")
    return entry, len(bzv) // 10

def one(t): return re.sub(r"\s+", " ", t).strip()

def main(mod, out):
    out.mkdir(parents=True, exist_ok=True)
    for t, books in (("ot", FILES[:39]), ("nt", FILES[39:])):
        entry, n = reader(mod, t)
        i = 2                                                    # the module and testament headings
        for code, fname in books:
            src = asv.parse(ROOT / "ref" / "eng-asv" / fname)
            name = NAMES[[c for c, _ in FILES].index(code)]
            lines = [f"\\id {code} Korean Revised Version (KorRV), CrossWire SWORD module 2.0.1, public domain",
                     "\\rem Converted by ref/KorRV/sword2usfm.py from the SWORD zText module KorRV (TextSource=Wikisource).",
                     f"\\h {name}", f"\\toc1 {name}", f"\\toc2 {name}", f"\\mt1 {name}"]
            i += 1                                               # the book heading
            for c in sorted({c for c, v in src}):
                i += 1                                           # the chapter heading
                lines.append(f"\\c {c}")
                for v in range(1, ADJ.get((code, c), max(v for cc, v in src if cc == c)) + 1):
                    raw = entry(i); i += 1
                    title = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S)
                    body = one(re.sub(r"<[^>]+>", "", re.sub(r"<title[^>]*>.*?</title>", "", raw, flags=re.S)))
                    if (code, c, v) in FIX:
                        old, new = FIX[(code, c, v)]
                        if not old: body = new + body
                        else: assert body.count(old) == 1, (code, c, v); body = body.replace(old, new)
                    body = body.replace("어호와", "여호와")
                    if NOTE.fullmatch(body): body = ""
                    if title: lines.append(f"\\d {one(re.sub(r'<[^>]+>', '', title.group(1)))}")
                    if v == 1 or title: lines.append("\\p")
                    lines.append(f"\\v {v} {body}" if body else f"\\v {v}")
            (out / fname.replace("eng-asv", "KorRV")).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        assert i == n, (t, i, n)
        print(t, i, "index entries")

if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
