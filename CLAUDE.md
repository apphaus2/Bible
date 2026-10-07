# CLAUDE.md — Bible Manga

Context for Claude (and humans) working in this repo. Read this first.

## What this is

A manga adaptation of the Bible, book by book, drawn as full-color vector pages in a
1980s cyberpunk-manga style, with the text taken word for word from the
**American Standard Version (1901)**. Each "book" of the manga is a cover plus 7–8 pages.
The pages are edited on private Claude Design canvases and published as a static
website from `docs/` (GitHub Pages).

### Status

| Series | Manga book | Chapters | Story | Folder | Text checked |
|---|---|---|---|---|---|
| Genesis | One — The Beginning | 1–3 | Creation → Eden → the Fall | `manga/genesis/book-01/` | yes |
| Genesis | Two — The Flood | 4–9 | Cain and Abel → the Flood → the rainbow | `manga/genesis/book-02/` | yes |
| Genesis | Three — The Promise | 11–22 | Babel → Abram's call → Sodom → Moriah | `manga/genesis/book-03/` | yes |
| Genesis | Four — The Ladder | 25–33 | Jacob and Esau → Bethel → Peniel → reunion | `manga/genesis/book-04/` | yes |
| Genesis | Five — The Dreamer | 37–50 | Joseph: coat → pit → Pharaoh → reunion | `manga/genesis/book-05/` | yes |
| Exodus | One — The Bush That Burned | 1–4 | bondage → bulrushes → Midian → the burning bush → I AM → the rod | `manga/exodus/book-01/` | yes |
| Exodus | Two — The Plagues | 5–11 | let my people go → rod against rod → the plagues → the midnight warning | `manga/exodus/book-02/` | yes |
| Exodus | Three — The Red Sea | 12–15 | the passover → the great cry → the pillars → the sea divided → Miriam's song | `manga/exodus/book-03/` | **no — see below** |

**Genesis is complete.** Exodus Books One to Three are done.

**Open item:** Exodus Book Three's quotations were written from the ASV but not yet checked
against the source (the ebible.org fetch wasn't approved at the time). Check every quoted line
in `tools/exodus_book3.py` against `https://ebible.org/asv/EXO12.htm` … `EXO15.htm`
(12:1–41, 13:19–21, 14:5–31, 15:20–21), fix any word that differs, re-run the script, republish,
and mark it checked in the table.

### The live canvases (private Claude Design artifacts)

- Genesis: https://claude.ai/artifact/UGXs4gFgPqfSp92tykHmT3
- Exodus: https://claude.ai/artifact/GkjFPGxsPf2iJtfVooXJNa

The canvas and the repo hold the same `.dc.html` files. The canvas can be edited by hand in the
browser, so **read a canvas's `project/canvas.json` (and any page you'll change) before
publishing to it**, and merge rather than overwrite. Publishing a page only sends that file;
send `canvas.json` only when boards, notes or order change.

## Repo layout

```
CLAUDE.md
index.html            redirect to docs/
docs/                 the website (generated — never edit by hand; see Website)
manga/
  genesis/
    canvas.json       Genesis canvas index (all books)
    book-01/          Main.dc.html (cover), P01…P07, canvas.json (this book only)
    book-02/ … book-05/   B2-…B5- Cover, P01…P08, canvas.json
  exodus/
    canvas.json       Exodus canvas index (all books)
    book-01/          Main.dc.html (cover), EX1-P01…EX1-P08, canvas.json
    book-02/          EX2-Cover, EX2-P01…EX2-P08, canvas.json
    book-03/          EX3-Cover, EX3-P01…EX3-P08, canvas.json
tools/
  — shared kit —
  figures.json        silhouettes: MAN, WOMAN, HAIR, LIE_BODY, LIE_ARM (feet at 0,0, ~200 units tall)
  faces.py            face(base="adam"|"eve", skin, shadow, hair, beard, scarf, egypt, collar, kohl,
                      false_beard, brow="scowl"|"sorrow", tear, sweat, stubble, light, …); faces/adam.svg, faces/eve.svg
  snake.py            snake(points, width, uid, head_scale): tapered, scaled serpent with a viper head
  egypt.py            pyramid(), granaries(), FAT/LEAN kine, SHEAF
  — Genesis only (token pipeline) —
  tower.py, ladder.py   Babel tower; Jacob's ladder with angels
  build3.py, build4.py, build5.py   swap __TOKEN__ placeholders in Genesis Book 3/4/5 pages
  — Exodus (one script per book) —
  mk.py               page helpers: page(), panel(), cols(), cap(), god(), balloon()+tail(), stamp(), sfx(),
                      ref(), person() (up=[shoulder, elbow, hand] for a raised arm), defs(), face(), speed(), stars()
  faces_ex.py         Moses (shepherd, fire-lit, afraid; Egyptian prince, angry), Pharaoh's daughter, Miriam,
                      Jochebed, Zipporah, the new Pharaoh, a taskmaster, Hebrew slaves
  exodus.py           reeds, the ark of bulrushes, flame()/blaze(), bush() (burning, not consumed), sheep(), hand(),
                      kneel(), sandal()
  exodus2.py          frogs, flies/swarm, lice, locusts, fish, hail, bolt(), columns(), brown serpents, kine_dead();
                      Aaron, the magicians (afraid, with boils), Pharaoh afraid, stern Moses
  exodus3.py          door() with blood, hyssop(), basin(), lamb(), horse(), chariot(), pillar_cloud(), pillar_fire(),
                      sea_corridor() (the parted sea in perspective), crash() (breaking wave), timbrel();
                      Pharaoh weeping, old Miriam, a frightened Hebrew, calm Moses
  exodus_book1.py … exodus_book3.py   each writes one whole book: python3 tools/exodus_bookN.py <out_dir>
  — website and checking —
  build_site.py       builds docs/ from flat page folders (SERIES config lists every series and book)
  rebuild_site.py     one step: python3 tools/rebuild_site.py [--thumbs]
  site/site.css, site/site.js   reader styles and keys/swipe navigation (copied into docs/assets/)
  shot.js, shots.js   Playwright renders: node tools/shots.js <out_dir> page.dc.html …
  thumbs.js           older thumbnail batch renderer (jobs file)
```

## How to add the next book

1. **Get the text first.** Fetch the ASV chapters from `https://ebible.org/asv/<BOOK><NN>.htm`
   (e.g. `EXO16.htm`). Plan a cover + 8 pages, 2–4 panels each, and pick the verses for each panel.
   Every caption, balloon and Voice box must be an exact ASV substring (trim with `…` only).
2. **Write `tools/<series>_bookN.py`** on the pattern of `exodus_book3.py`: one function per page
   returning `mk.page(...)`, new art in a `<series>N.py` generator module, new faces via
   `faces_ex.F(...)` in that module's `tokens()`.
   File stems: `EX4-Cover`, `EX4-P01-…`; titles `B4 · 00 · Cover`, `B4 · 01 · …`.
3. **Render and look:** `python3 tools/exodus_book4.py /tmp/ex && node tools/shots.js /tmp/png /tmp/ex/*.dc.html`.
   Check faces, figures, balloon tails pointing at the speaker's mouth, text inside balloons,
   captions not covering faces, and nothing important cut off. Fix the script and re-run.
4. **Publish to the canvas:** read `project/canvas.json`, add the boards (rows of 5 then 4, x = col × 840,
   rows 1200 apart, each book starting 2800 below the last: 0, 2800, 5600, 8400, …) and a
   `title1` note 300 above the first row, then send the new pages plus the index.
5. **Repo:** copy the pages to `manga/<series>/book-NN/` with a book-only `canvas.json`, update
   `manga/<series>/canvas.json`, add the book to `SERIES` in `tools/build_site.py`, run
   `python3 tools/rebuild_site.py --thumbs`, update this file's status table, commit.

## File format

Each page is a self-contained **Design Component** (`.dc.html`) for the Claude Design canvas:

- Keep `<script src="./support.js"></script>` in `<head>` exactly as written.
- All markup sits inside `<x-dc>…</x-dc>`. Fonts come from one Google Fonts `<link>` in `<helmet>`.
- End with `<script type="text/x-dc" data-dc-script data-props='…'>` holding
  `class Component extends DCLogic { renderVals() {…} }`; `$preview` is `{"width":760,"height":1080}`.
  Covers declare an `accent` color prop and use `{{accent}}` on the kanji block.
- `{{hole}}` is a dotted lookup only, never an expression.
- Close every element, quote every attribute, use inline `style=""` (the editor edits it).
- Art is inline SVG plus CSS gradients: no images, emoji, DOM-building scripts or iframes.
- SVG `id`s get a per-panel prefix so `<defs>`/`<use>` never collide (the Exodus scripts pass one to `defs()`).
- Genesis pages were written by hand with `__TOKEN__` placeholders filled by `build3/4/5.py`.
  Exodus pages are **generated**: fix the script and re-run, never hand-edit the output.

`canvas.json`: `v: 3`, `boards` keyed by file name (x, y, w 760, h 1080, title), `order`, `notes`
(`kind: "title1"`, `maxW: 4120` for book titles). Keep `createdOnFiles` and every key you aren't changing.

## Visual style guide

**Influences:** 1980s Japanese cyberpunk manga in general — precise linework, technical labels,
flying debris, radial speed lines, screentone, big cinematic splash panels.
**Never** use Akira's characters, logo or title treatment, the red motorcycle, pill or capsule
imagery, Neo-Tokyo, or the white-dome explosion: the general style only, not a recreation.

**Full color**, 80s airbrushed manga coloring: black ink linework over flat, saturated fills and
smooth gradients. Gutters, captions and balloons stay cream and white so the text reads.

| Token | Value | Use |
|---|---|---|
| Paper | `#F3EFE6` | page gutter, captions |
| Ink | `#0D0D0F` | linework, borders, speed lines |
| Red | `#D7261E` | chapter stamps, accents, cover kanji block |
| Night | `#0B0B2A` → `#1E1650` → `#5B2470` | void, cosmos, God's-voice panels |
| Voice box | `#12113A` fill, `#FFD23F` gold inner rule | all of God's words |
| Light | `#FFE680` → `#FFC14D` → `#FF6A2A` | light, sun, glow, fire |
| Sea | `#8FD0E2` sky, `#0F4C68`/`#1F6F9A` water, `#E8F6FA` foam | waters, the Red Sea |
| Earth | `#4A2418` rock, `#C8682E` lit rock, `#C8A06A`/`#E8C88A` sand | land, desert |
| Life | `#2E6B3A` / `#1F4A34` greens, `#9CCB5E` grass | plants, Eden |
| Blood | `#8A0E16` river, `#B5121B` doorposts | the Nile, the passover |
| Egypt | gold `#E8B830`, blue `#1F5FAD`, Pharaoh's nemes black-and-gold | court, palace |

Each panel gets its own background gradient. Keep black lines on top of fills.

**Fonts:** Anton (God's voice, titles), IBM Plex Mono (captions, labels), Archivo Narrow 700
(speech balloons), Noto Sans JP 900 (sound effects, kanji).

**Page:** 760×1080, padding `28px 26px 30px`, CSS grid with explicit `grid-template-rows` and 12 px
gaps, panels with a 3 px ink border and `overflow:hidden`, page number centered at the bottom as `— NN —`.
Usable panel widths: full 702, half 342; heights are the row height minus 6.

**Covers:** "THE BOOK OF" / "No. NN", the series title in Anton 168 px, "Book N — Name",
"Chapters a – b", a vertical kanji block in the accent color (創世記 SŌSEIKI for Genesis,
出エジプト記 SHUTSU for Exodus), one short ASV caption, "Adapted from the American Standard
Version (1901)" and "Vol. N" at the bottom.

**Recurring components** (all in `tools/mk.py`):
- **Narration caption** `cap()`: paper box, 2 px ink border, mono 600 at 10–11 px, uppercase.
- **Voice of God** `god()`: indigo box with an inner gold rule, Anton, uppercase. God is never drawn.
- **Speech balloon** `balloon()` + `tail()`: white ellipse with a 2.5 px border; the SVG tail goes
  *before* the balloon in the DOM and its tip points at the speaker's mouth.
- **SFX** `sfx()`: katakana with a romanized tag (ゴオオ / GOOO, ドッ / DOH!).
- **Chapter stamp** `stamp(n)`: red-outlined rotated box, 第N章 over CHAPTER N, once per chapter.
- **Verse ref** `ref()`: tiny mono `EX 14:22` in a corner when no caption names the verse.
- **Speed lines** `speed()`, starfields `stars()`.

## People and creatures

The user asked for **realistic, well-proportioned people** and a **serpent that looks like a snake**.
Never fall back to blobs or stick figures.

- **Distant figures:** `figures.json` silhouettes via `mk.person()`, with a `Robe` or `Tunic` over them.
  Women use WOMAN plus a separate HAIR `<use>` (never merge subpaths — they render hollow).
  Raised or reaching arms: `person(..., up=[(-22,-158), elbow, hand])` (removes that hanging arm).
  Kneeling, cowering or bowed figures: `exodus.kneel()`. Lying figures: LIE_BODY + LIE_ARM.
  Never rotate a standing figure to make it lie down.
- **Close-ups:** every key emotional beat gets a shaded profile face from `faces.face()`.
  Flip with `face(tok, x, y, s, flip=True)` (x is then the right edge).
- **Character guide (Exodus):**
  - Moses grown: off-white shepherd's headcloth with a dark cord, black beard. Young Moses: Egyptian
    red-and-white headcloth, collar, kohl. Moods: calm (gold rim light), fire-lit, afraid (sweat), stern (scowl, red light).
  - Aaron: grey beard, blue headcloth with cord.
  - The new Pharaoh (from Exodus 1): black-and-gold nemes, false beard, kohl; afraid and weeping variants.
  - Pharaoh's magicians: black-and-white headcloth, kohl, purple rim light.
  - Miriam: brown hair when young; old Miriam has grey hair and a pink headscarf, with a timbrel.
  - Pharaoh's daughter: black hair, gold band, collar, kohl. Zipporah: red headscarf.
- **Genesis faces:** Adam, Eve, Cain, Noah, Abraham, Sarah, Isaac, Jacob, Esau, Rachel, Joseph (also in
  Egyptian dress, weeping), Pharaoh of Joseph's day (gold-and-blue nemes), old Jacob — all in `faces.py`.
- **Serpents:** always `snake.py` (tapered body, belly scutes, blotches, viper head). The magicians'
  serpents are the brown recolor `exodus2.serpent(..., brown=True)`.

## Text rules

- **American Standard Version (1901)** only, word for word. Trim with `…`; never paraphrase or
  modernize. Keep ASV wording: "Jehovah", "Jehovah God", "waste and void", "great sea-monsters",
  "kine", "murrain", "to-day", "the Cherubim".
- Source: `https://ebible.org/asv/<BOOK><NN>.htm` (GEN01…, EXO01…). Check every line against it.
- **Don't** quote the NASB, NAB (the Vatican site's translation) or any other copyrighted
  translation. If asked for one, offer the ASV or the World English Bible (also public domain).
- Captions carry narration, balloons carry dialogue, God's words always use the Voice box.
- Proofread captions: one past typo ("caled" for "called") was caught by the user.

## Website (`docs/`)

A static site built from the pages, served by GitHub Pages from `main` › `/docs`
(the root `index.html` redirects there).

- `docs/index.html`: landing page with a section per series, book cards, and a full table of contents.
- `docs/<series>/book-NN/index.html`: each book's index with page thumbnails.
- `docs/<series>/book-NN/NN-<slug>.html`: one URL per manga page, with breadcrumbs
  (Bible Manga / series / book / page), Prev/Next (arrow keys and swipe too) and `<link rel=prev/next>`.
  Books chain into each other, and the end of Genesis continues into Exodus.
- `docs/manifest.json`: every series, book and page (title, verse ref, URL, thumbnail) for linking.
- `docs/thumbs/`: 380×540 JPGs — `book-NN-<slug>.jpg` for Genesis, `exodus-book-NN-<slug>.jpg` for Exodus.

Rebuild after any page change:
```
python3 tools/rebuild_site.py --thumbs   # --thumbs renders only missing thumbnails
```
To refresh a changed page's thumbnail, delete its JPG first. New book: add it to that series'
`books` in `SERIES` in `tools/build_site.py`; a new series is a new `SERIES` entry with `id`,
`name`, `kanji`, `thumb` prefix and `lede`.

## Checking pages

`node tools/shots.js <out_dir> page.dc.html …` renders PNGs with Playwright. The sandbox has no
Anton/Archivo/Plex fonts, so renders use wider fallbacks: if text fits there, it fits on the canvas.
Look at people, faces, balloon tails, overlaps and cut-off art before publishing.

## Working notes for Claude

- **Pushing:** Claude can't push to GitHub from its cloud session. It writes the changed files into
  the user's clone at `~/_GITHUB/apphaus2/Bible` (when the Mac is connected) and gives the user the
  command: `cd ~/_GITHUB/apphaus2/Bible && git add -A && git commit -m "…" && git push`.
- **"continue"** from the user means: build the next manga book.
- **"commit" / "update github"** means: write the latest repo files to the Mac clone and give the push command.
- Commit messages end with the Co-Authored-By and Claude-Session lines; the git author is Sky.

## Roadmap

- Check Exodus Book Three's text against the ASV (see Status).
- Exodus Book Four — Exodus 16–20: manna and quails, water from the rock, Sinai, the ten commandments.
- Exodus Book Five — Exodus 24, 32–34, 40: the tables of stone, the golden calf, the glory filling the tabernacle.
- Then Leviticus/Numbers highlights or straight on to Joshua — the user's call.
- Possible option: right-to-left reading order.
