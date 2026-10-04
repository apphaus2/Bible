# CLAUDE.md — Bible Manga

Context for Claude (and humans) working in this repo.

## What this is

A manga adaptation of the Bible, book by book, drawn as full-color vector pages in a
1980s cyberpunk-manga style. Genesis is complete; Exodus is under way.

- **Book One — Genesis 1–3** (Creation → Eden → the Fall): done, `manga/genesis/book-01/`
- **Book Two — Genesis 4–9** (Cain and Abel → the Flood → the rainbow): done, `manga/genesis/book-02/`
- **Book Three — Genesis 11–22** (Babel → Abram's call → Sodom → Moriah): done, `manga/genesis/book-03/`
- **Book Four — Genesis 25–33** (Jacob and Esau → Bethel → Peniel → reunion): done, `manga/genesis/book-04/`
- **Book Five — Genesis 37–50** (Joseph: coat → pit → Egypt → Pharaoh → reunion): done, `manga/genesis/book-05/`
- **Genesis is complete.**
- Genesis live canvas (private Claude Design artifact): https://claude.ai/artifact/UGXs4gFgPqfSp92tykHmT3

**Exodus**

- **Book One — Exodus 1–4** (bondage → the ark of bulrushes → Midian → the burning bush → I AM → the rod): done, `manga/exodus/book-01/`
- Exodus live canvas (its own private Claude Design artifact): https://claude.ai/artifact/GkjFPGxsPf2iJtfVooXJNa

## Repo layout

```
manga/
  genesis/
    canvas.json       the live canvas index (all books; Book Two rows start at y = 2800, Book Three at 5600, Book Four at 8400, Book Five at 11200)
    book-01/          Genesis 1–3: Main.dc.html (cover), P01…P07, canvas.json (this book only)
    book-02/          Genesis 4–9: B2-Cover, B2-P01…B2-P08, canvas.json (this book only)
    book-03/          Genesis 11–22: B3-Cover, B3-P01…B3-P08, canvas.json (this book only)
    book-04/          Genesis 25–33: B4-Cover, B4-P01…B4-P08, canvas.json (this book only)
    book-05/          Genesis 37–50: B5-Cover, B5-P01…B5-P08, canvas.json (this book only)
  exodus/
    canvas.json       the Exodus canvas index (Book One rows at y = 0 and 1200; Book Two will start at 2800)
    book-01/          Exodus 1–4: Main.dc.html (cover), EX1-P01…EX1-P08, canvas.json (this book only)
tools/
  faces.py            figure/face kit: build(paths) swaps __MAN__, __WOMAN__, __HAIR__,
                      __TUNIC__, __LIEB__/__LIEA__, __FACE_*__ tokens in page files
  faces/adam.svg, faces/eve.svg   shaded profile close-ups (base art for face variants)
  figures.json        silhouette paths (man, woman, hair, reclining body/arm)
  snake.py            generates a tapered, scaled serpent from a centerline
  tower.py            generates the stepped brick Tower of Babel (tiers, ramps, scaffolding, crane)
  build3.py           Book Three build: faces.tokens() + __ROBE__, __TOWER_*__, __STARS_*__ tokens
  ladder.py           generates Jacob's ladder in perspective with winged angels
  build4.py           Book Four build: build3 tokens + __LADDER_*__, __BOW__ (bowing figure), Esau/Jacob faces
  egypt.py            pyramids, granary rows, fat/lean kine, sheaf paths
  build5.py           Book Five build: build4 tokens + __PYRAMIDS_*__, __GRANARIES_*__, __FAT__/__LEAN__/__RIBS__, __SHEAF__
  shot.js             Playwright render of a .dc.html to PNG, for checking a page
  shots.js            the same for many pages: node tools/shots.js <out_dir> a.dc.html b.dc.html …
  mk.py               page-building helpers for Exodus on: page(), panel(), cols(), cap(), god(), balloon()+tail(),
                      stamp(), sfx(), ref(), person() (with ManUp/WomanUp + arm points for a raised arm), speed(), stars()
  faces_ex.py         Exodus faces: Moses (shepherd headcloth + cord, beard; fire-lit; afraid), Moses as an Egyptian
                      prince (angry variant), Pharaoh's daughter, Miriam, Jochebed, Zipporah, the new Pharaoh,
                      a taskmaster, Hebrew slaves
  exodus.py           reeds/bulrushes, the ark of bulrushes, flame/blaze, the burning bush (not consumed), sheep,
                      an open hand (leprous variant), kneeling figure, sandals
  exodus_book1.py     writes all of Exodus Book One: python3 tools/exodus_book1.py <out_dir>
```

New books go in `manga/<book>/book-NN/` and keep the same file conventions.
File stems must be unique across the whole canvas, so Book Two pages are prefixed `B2-` (Book Three: `B3-`).
Exodus has its own canvas: its pages are prefixed `EX1-` (Book Two: `EX2-`), and its first cover is `Main.dc.html`.

Genesis pages were written by hand with `__TOKEN__` placeholders and filled by `build3/4/5.py`. From Exodus on,
each book is one Python script (`exodus_book1.py`) that composes every page from the `mk.py` helpers and the
generators, so a fix is an edit to the script and a re-run, never a hand edit of the generated `.dc.html`.

## File format

Each page is a self-contained **Design Component** (`.dc.html`) for the Claude
Design canvas:

- Keep `<script src="./support.js"></script>` in `<head>` exactly as written.
- All markup sits inside `<x-dc>…</x-dc>`. Fonts come from one Google Fonts
  `<link>` in `<helmet>`.
- End each file with a `<script type="text/x-dc" data-dc-script data-props='…'>`
  block containing `class Component extends DCLogic { renderVals() {…} }`.
  `$preview` is `{"width":760,"height":1080}`.
- `{{hole}}` only does a dotted lookup, never an expression.
- Close every element and quote every attribute. Use inline `style=""`, since
  that's what the editor edits.
- Art is inline SVG plus CSS gradients. Don't use images, emoji, scripts that
  build the DOM, or iframes.
- Give SVG `id`s a page prefix (`dk`, `fm`, `ld`, `lf`, `ed`, `sv`, `ex`, …) so
  `<defs>`/`<use>` never collide.

`canvas.json`: pages are 760×1080, in rows of 4 or 5. Frames are 80 px apart in a row
and 120 px apart between rows (y = 0, 1200, 2400…). Every page needs a `boards`
entry and an `order` slot. Keep `createdOnFiles` unchanged.

## Visual style guide

**Influences:** 1980s Japanese cyberpunk manga in general. That means precise
linework, technical annotation labels, flying debris, radial speed lines,
screentone, and big cinematic splash panels.
**Never** use Akira's characters, logo or title treatment, the red motorcycle,
pill or capsule imagery, Neo-Tokyo, or the white-dome explosion. Use the
general style only, not a recreation of that work.

**Full color**, in the style of 80s airbrushed manga coloring: black ink linework
over flat, saturated fills and smooth gradients. Gutters, captions and speech
balloons stay cream and white so the text reads cleanly.

| Token | Value | Use |
|---|---|---|
| Paper | `#F3EFE6` | page gutter, captions |
| Ink | `#0D0D0F` | linework, borders, speed lines |
| Red | `#D7261E` | day stamps, forbidden fruit, serpent eye, flaming sword |
| Night | `#0B0B2A` → `#1E1650` → `#5B2470` | void, cosmos, God's-voice panels |
| Voice box | `#12113A` fill, `#FFD23F` gold inner rule | all of God's words |
| Light | `#FFE680` → `#FFC14D` → `#FF6A2A` | creation light, sun, glow |
| Sea | `#8FD0E2` sky, `#0F4C68` water, `#6FD3E0` crests | waters, firmament |
| Earth | `#4A2418` rock, `#C8682E` lit rock, `#F2733F` dust sky | land rising |
| Life | `#2E6B3A` / `#1F4A34` greens, `#9CCB5E` tree of knowledge | plants, Eden |
| Serpent | `#1B3A12` body, `#C9E265` bands and outline, `#0B2A1E` jungle | serpent pages |
| Skin/people | `#3A2230` silhouettes and hands, `#F4C9A0` skin close-ups | humans |
| Exile | `#1A0F3A` → `#4A1D55` sky, gold `#FFD23F` rim light | cherubim, gate |

Each panel gets its own background gradient (an inline `background:`). Use
SVG fills for shapes and keep black lines on top. A gradient goes last in a
layered `background`, under any conic speed lines.

**Fonts:** Anton (God's voice, titles), IBM Plex Mono (narration captions, labels),
Archivo Narrow 700 (speech balloons), Noto Sans JP 900 (sound effects).

**Page:** 760×1080. Padding `28px 26px 30px`. The CSS grid has explicit
`grid-template-rows` and 12 px gaps. Panels have a 3 px ink border and
`overflow:hidden`. The page number goes centered at the bottom as `— NN —`.

**Recurring components** (copy the inline styles from existing pages):
- **Narration caption:** a paper box with a 2 px ink border, mono 600 at 11 px,
  uppercase.
- **Voice of God:** an indigo `#12113A` box with an inner gold rule
  (`box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px #FFD23F`), Anton,
  uppercase. No speaker is ever drawn.
- **Speech balloon:** a white ellipse (`border-radius:50%`) with a 2.5 px border
  and an SVG triangle tail placed *before* the balloon in the DOM. The serpent
  gets a black balloon with a double paper outline.
- **SFX:** Japanese katakana with a romanized tag underneath, e.g. ドン / DOOOM,
  ゴゴゴ / GOGOGO.
- **Day / chapter stamp:** a red-outlined rotated box with kanji over English
  (第一日 / THE FIRST DAY in Book One, 第四章 / CHAPTER 4 from Book Two on).
- **Verse ref:** tiny mono `GEN 1:3` in a corner.
- **Speed lines:** layered `repeating-conic-gradient` (focus) or thin tapered
  SVG wedges (horizontal). Screentone is a `radial-gradient` dot grid.
- **People.** The goal is realistic, well-proportioned figures, not cut-outs.
  - **Distant figures:** the silhouettes in `tools/figures.json` (feet at 0,0,
    about 200 units tall, legs about half the height, gaps between arms and
    body). Use the separate WOMAN body for women, and the HAIR path as its own
    `<use>`, never merged into the body path (merged subpaths render hollow).
    From Genesis 3:21 on, people wear the `__TUNIC__` coat of skins. Use the
    LIE_BODY + LIE_ARM side view for lying figures; never rotate a standing one.
  - **Close-ups:** use shaded profile faces (`tools/faces/*.svg` via
    `faces.face()`): skin with a shadow side, a highlight line, a real eye,
    ear and hair. Variants so far: Adam, Eve, Cain (angry, marked), and Noah
    (white hair and beard), Abraham (grey beard; star-lit variant), Sarah
    (headscarf, laughing), Isaac, blind old Isaac, Jacob (calm, straining,
    awed), Esau (red hair and stubble; weeping; angry), and Rachel. Give every
    key emotional beat a face close-up. Book Five adds Joseph, Joseph in
    Egyptian dress (`egypt=` striped headcloth with the hair hidden, gold
    collar, kohl), weeping Joseph, Pharaoh (false beard), and grieving old Jacob.
    Exodus adds the faces in `tools/faces_ex.py`. Grown Moses always wears an off-white
    shepherd's headcloth with a dark cord and a black beard (a `scarf=` on the male face
    now hides the hair under it); young Moses is in Egyptian dress, red-and-white.
  - **Poses:** `person(..., up=[shoulder, elbow, hand])` draws a raised or reaching arm
    and removes that side's hanging arm. Kneeling or cowering people use
    `exodus.kneel()` (arm across the face), not the old `__BOW__` blob.
  - The burning bush is `exodus.bush()`: one merged blaze outline with hotter cores,
    dark thorny branches, and green leaves still on them (the bush is not consumed).
  - Joseph's coat of many colors is a 6-band stripe `<pattern>` (red, gold,
    teal, purple, green, orange) on the TUNIC or ROBE.
  - Patriarchs and travellers wear the full-length `__ROBE__`; younger people
    wear the `__TUNIC__`.
- **Serpent:** generated by `tools/snake.py` (tapered body, pale belly with
  scutes, dorsal blotches, scales, a viper head with slit pupil and forked
  tongue). Clip the branch over the body where the coils pass behind it.

## Text rules

- Use the **American Standard Version (1901)** (public domain) only. Trim with
  `…`; don't paraphrase. Keep ASV specifics: "Jehovah God", "waste and void",
  "great sea-monsters", "as God", Pishon, "the Cherubim".
- **Don't** quote the NASB, NAB (the Vatican site's translation) or any other
  copyrighted translation. If someone asks for one, offer the ASV or the World
  English Bible (also public domain) instead.
- Captions carry narration and balloons carry dialogue. God's words always use
  the Voice box.

## Website (`docs/`)

A static site built from the pages, served by GitHub Pages from `main` › `/docs`.

- `docs/index.html` is the landing page: every book plus a full table of contents.
- `docs/<series>/book-NN/index.html` is each book's index, with page thumbnails
  (`<series>` is `genesis` or `exodus`).
- `docs/<series>/book-NN/NN-<slug>.html` is one URL per manga page, with
  breadcrumbs (Bible Manga / series / book / page), Prev/Next (arrow keys and swipe work too)
  and `<link rel=prev/next>`. The last page of a book continues into the next book, and the
  end of Genesis continues into Exodus.
- `docs/manifest.json` lists every series, book and page (title, verse ref, URL,
  thumbnail) for linking from another website.
- `docs/thumbs/*.jpg` are 380×540 page previews: `book-NN-<slug>.jpg` for Genesis,
  `exodus-book-NN-<slug>.jpg` for Exodus.

Rebuild after any page change (each series' pages flat in one folder with its canvas.json):
```
python3 tools/build_site.py docs genesis=<genesis pages dir> exodus=<exodus pages dir>
cp tools/site/* docs/assets/
node tools/shots.js <png_dir> <pages…>   # then resize each PNG to a 380×540 JPG in docs/thumbs/
```
When adding a book, add it to that series' `books` in `SERIES` in `tools/build_site.py`
(a new series is a new `SERIES` entry).

## Checking pages

Render with `node tools/shot.js page.dc.html out.png` (Playwright; the fonts may
fall back locally) and look at people, the serpent and text overlaps before
publishing.

## Roadmap

- Exodus Book Two — Exodus 5–11: Moses and Aaron before Pharaoh, the rods and serpents, the ten plagues
- Exodus Book Three — Exodus 12–15: the passover, the departure, the Red Sea, the song of Moses
- Exodus Book Four — Exodus 16–20, 32–34: manna, Sinai, the ten commandments, the golden calf
- Possible option: right-to-left reading order
