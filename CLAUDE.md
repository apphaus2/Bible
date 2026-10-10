# CLAUDE.md — Bible Manga

Context for Claude (and humans) working in this repo. Read this first.

## What this is

A manga adaptation of the Bible, drawn as full-color vector pages in a 1980s cyberpunk-manga style
(general style only: never Akira's characters, logo or imagery), with every word of text taken from the
**American Standard Version (1901)**. Pages are edited on private Claude Design canvases and published as a
static website that GitHub Actions builds and deploys to GitHub Pages on every push to `main`.

There are two editions:

- **The full edition (primary, in progress)** — `volumes/`. One volume per book of the Bible, split into
  manga chapters of roughly 15–25 pages. Target: every scene and every line of dialogue word for word
  ("story-complete"): narrative verses in full; genealogies and lists may become one illustrated page that
  quotes key lines; retellings and technical detail may be abridged, always marked with "…". Each volume
  has a `coverage.md` listing every verse as full / partial / omitted. About 140–160 words a page.
- **The digest edition (legacy)** — `digest/`. The first drafts: 9–11-page books of highlights from Genesis to
  2 Samuel (175 pages, about 8% of the text). Kept for now as second-class (a smaller section lower on the
  home page); expected to be deleted once the full edition overtakes it. Don't extend it.

### Status — full edition

| Volume | Chapter | Bible chapters | Pages | Coverage | Folder |
|---|---|---|---|---|---|
| Genesis | 1 · In the Beginning (pilot) | 1–3 | cover + title + 16 | 80/80 verses full | `volumes/genesis/` |
| Genesis | 2 · Cain to the Flood | 4–9 | title + 24 (pp. 17–40) | 155/155 verses full | `volumes/genesis/` |

Next: Genesis chapter 3 (Genesis 10–15; ch. 10 and 11:10–32 are lists → scroll pages like Genesis 5). Planned Genesis chapters:
1 Creation and Eden (1–3) · 2 Cain to the Flood (4–9) · 3 Babel to Abram's covenant (10–15) ·
4 Abraham (16–23) · 5 Isaac and Rebekah (24–27) · 6 Jacob (28–36) · 7 Joseph sold, Joseph raised up (37–41) ·
8 Joseph and his brothers (42–50). Genesis lists to treat as scroll pages: ch. 5, ch. 10, 11:10–32,
22:20–24, 25:1–4 and 12–18, ch. 36, 46:8–27 (166 verses). Retellings to abridge: 24:34–49, 41:17–24,
42:29–34, 43:3–7.

### Status — digest edition (legacy)

| Series | Manga book | Chapters | Story | Folder | Text checked |
|---|---|---|---|---|---|
| Genesis | One — The Beginning | 1–3 | Creation → Eden → the Fall | `digest/genesis/book-01/` | yes |
| Genesis | Two — The Flood | 4–9 | Cain and Abel → the Flood → the rainbow | `digest/genesis/book-02/` | yes |
| Genesis | Three — The Promise | 11–22 | Babel → Abram's call → Sodom → Moriah | `digest/genesis/book-03/` | yes |
| Genesis | Four — The Ladder | 25–33 | Jacob and Esau → Bethel → Peniel → reunion | `digest/genesis/book-04/` | yes |
| Genesis | Five — The Dreamer | 37–50 | Joseph: coat → pit → Pharaoh → reunion | `digest/genesis/book-05/` | yes |
| Exodus | One — The Bush That Burned | 1–4 | bondage → bulrushes → Midian → the burning bush → I AM → the rod | `digest/exodus/book-01/` | yes |
| Exodus | Two — The Plagues | 5–11 | let my people go → rod against rod → the plagues → the midnight warning | `digest/exodus/book-02/` | yes |
| Exodus | Three — The Red Sea | 12–15 | the passover → the great cry → the pillars → the sea divided → Miriam's song | `digest/exodus/book-03/` | yes |
| Exodus | Four — Sinai | 16–20 | manna and quails → water from the rock → Amalek → the mountain on fire → the ten commandments | `digest/exodus/book-04/` | yes |
| Exodus | Five — The Glory | 24–40 | the tables of stone → the golden calf → the tables broken → the cleft of the rock → the shining face → the tabernacle | `digest/exodus/book-05/` | yes |
| Numbers | One — In the Wilderness | 13–24 | the twelve spies → the evil report → forty years → the rock smitten twice → the serpent of brass → Balaam's ass → a star out of Jacob | `digest/numbers/book-01/` | yes |
| Joshua | One — Jericho | 1–24 | be strong → Rahab → crossing Jordan → the prince of the host → the walls of Jericho → the sun stands still → choose you this day | `digest/joshua/book-01/` | yes |
| Judges | One — The Sword of Gideon | 4–8 | Deborah → Mount Tabor → Jael's tent → Gideon in the winepress → the fleece → the three hundred → trumpets, pitchers and torches | `digest/judges/book-01/` | yes |
| Judges | Two — Samson | 13–16 | the Nazirite → the young lion → the foxes → the jawbone → the gates of Gaza → Delilah → the seven locks → the pillars | `digest/judges/book-02/` | yes |
| Ruth | One — Whither Thou Goest | 1–4 | Moab → Orpah and Ruth → whither thou goest → call me Mara → the field of Boaz → the threshing-floor → Obed | `digest/ruth/book-01/` | yes |
| 1 Samuel | One — Thy Servant Heareth | 1–10 | Hannah's vow → the child given → here am I → speak; for thy servant heareth → the ark taken → Dagon fallen → the kine → give us a king → Saul anointed | `digest/1samuel/book-01/` | yes |
| 1 Samuel | Two — The Battle Is Jehovah's | 16–31 | the youngest → David anointed → Goliath of Gath → the living God → five smooth stones → in the name of Jehovah → a sling and a stone → Jonathan and Saul's spear → the cave → mount Gilboa | `digest/1samuel/book-02/` | yes |
| 2 Samuel | One — Thou Art the Man | 1–12 | mourning for Saul and Jonathan → king over all Israel → the ark comes up → dancing before Jehovah → for ever → Mephibosheth → the letter → the ewe lamb → thou art the man | `digest/2samuel/book-01/` | yes |
| 2 Samuel | Two — O My Son Absalom | 14–24 | no blemish in him → he stole the hearts → Absalom is king in Hebron → the mount of Olives → deal gently → between heaven and earth → tidings → O my son → which cost me nothing | `digest/2samuel/book-02/` | yes |

Every digest quotation from Exodus to 2 Samuel matches `ref/asv` exactly (657 segments). The Genesis digest
predates the checks: 12 of its 180 segments have small slips (6 punctuation, 6 trimmed wording).

### The live canvases (private Claude Design artifacts)

- **Genesis — Full Edition: https://claude.ai/artifact/U99Xmh1RBdnVK7VynDna6L**
- Digest canvases:
  - Genesis: https://claude.ai/artifact/UGXs4gFgPqfSp92tykHmT3
  - Exodus: https://claude.ai/artifact/GkjFPGxsPf2iJtfVooXJNa
  - Numbers: https://claude.ai/artifact/5XBpW6avLboeS41ixSmFp3
  - Joshua: https://claude.ai/artifact/5R9PTFZzptHXrwfqyee8mW
  - Judges: https://claude.ai/artifact/9HMcH2CtBEqKHE5aBtG8JP
  - Ruth: https://claude.ai/artifact/S4ogKfD3AAzMEAJTP7gFBi
  - 1 Samuel: https://claude.ai/artifact/PpQmFPRcmsqZZ7dbBjyJgA
  - 2 Samuel: https://claude.ai/artifact/6LsxVZxmaSSTzH5aCpDGLw

The canvas and the repo hold the same `.dc.html` files. The canvas can be edited by hand in the
browser, so **read a canvas's `project/canvas.json` (and any page you'll change) before
publishing to it**, and merge rather than overwrite. Publishing a page only sends that file;
send `canvas.json` only when boards, notes or order change.

## Repo layout

```
CLAUDE.md, README.md
.github/workflows/pages.yml   builds and deploys the website (see Website)
ref/asv/              the ASV as USFM from eBible.org (public domain): 02-GENeng-asv.usfm … — the text source
volumes/              THE FULL EDITION (generated by tools/full; never hand-edit)
  genesis/
    pages/            Main.dc.html (volume cover), GEN-C01-00-Title, GEN-C01-P01-… (chapter 1), …
    canvas.json       canvas index (one block of rows per chapter)
    volume.json       chapters for the website (dir, num, name, range, blurb, file prefixes)
    coverage.md       every verse of the chapters built so far: full / partial / omitted
digest/               THE DIGEST EDITION (legacy, was manga/): <series>/canvas.json, <series>/book-NN/*.dc.html
_site/                the website, built locally for previews (git-ignored; Actions builds its own)
tools/
  full/               full-edition builder
    asv.py            Book("GEN").v("1:3", frm=…, to=…) cuts exact text out of ref/asv and records coverage
    reuse.py          panels("digest/…/P05-Eden.dc.html") lifts a digest page's drawn panels for reuse
                      (a full-panel overlay div, e.g. rain streaks, comes along as an extra background layer)
    fx.py             page kit: use(art) / new(bg, w, h, svg) panels, vref() verse labels, day_stamp(),
                      chapter_title(), end_mark()
    build_volume.py   python3 tools/full/build_volume.py genesis  → writes volumes/genesis/ and checks the text
                      (--check writes nothing: fails if committed pages are out of date or any text isn't ASV)
    genesis/          __init__.py (META: chapters), cover.py, art.py (chapter 1 drawings), art2.py (chapter 2:
                      Cain's line, Noah and his house, the ark, the flood, the dove, the bow), ch01.py, ch02.py, …
  kit/                the shared drawing kit (mk.py, faces, figures, every art module; see below)
  digest/             the digest book writers (exodus_book1.py … samuel4_book2.py, build3–5.py)
  site/               build_site.py, rebuild_site.py, shots.js, assets/site.css + site.js
```

Drawing kit reference (`tools/kit/`, except the `*_book*.py` and `build3–5.py` writers in `tools/digest/`
and the website tools in `tools/site/`):

```
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
  exodus4.py          quail(), manna(), tent(), basket(), rock() and gush() (water from the rock), figure_both() (both arms
                      raised), warriors() with spears and shields, sinai() (the mountain on fire with its smoke
                      column), numeral() (big kanji 一…十 for the ten commandments); Joshua, an Israelite woman
  exodus5.py          tables() (the two tables of stone), calf() (the golden calf on a pedestal), rings(), shards() (the
                      broken tables), rays() (glory), tabernacle() (tent and court); Aaron afraid, Moses' shining face
  exodus_book1.py … exodus_book5.py   each writes one whole book: python3 tools/exodus_bookN.py <out_dir>
  — Numbers and Joshua —
  numbers1.py         grapes(), fiery() (red-gold serpents), brass_serpent() (on its standard), ass()/ass_lying(),
                      mount() (a rider on an ass), angel() (white, winged, sword drawn), prostrate() (fallen on his face),
                      camp() (rows of tents), star(), SWORD_ARM/BLADE; Caleb, Balaam (angry, in awe), a frightened spy
  numbers_book1.py    writes Numbers Book One (also has badge(), hills(), carriers() for the grape-bearers)
  joshua1.py          jericho() (wall, towers, houses, Rahab's window and scarlet line), collapse() (the wall falling),
                      flax(), ark()/ark_borne() (the ark of the covenant on its staves), shofar()/trumpeter()/blasts(),
                      heap() + riverbed() (the Jordan standing in one heap), prince() (prince of Jehovah's host),
                      sun(), moon(), city_hill(), oak(); Joshua as leader, in awe and old, Rahab
  joshua_book1.py     writes Joshua Book One (procession() = men of war, seven trumpeters, the ark)
  judges1.py          palm(), tabor(), tent_big(), rug_sleeper(), PIN/HAMMER, winepress(), wheat(), chaff(), fleece(), dew(),
                      bowl(), pitcher() (whole or broken, with its torch), torchbearer(), drinker_lap(), camel();
                      Deborah, Barak (afraid, bold), Jael, Gideon (afraid, bold, calm)
  judges_book1.py     writes Judges Book One (shout() = a big gold-ruled battle cry, midian_camp() = tents and camels)
  judges2.py          samson() (figure with seven locks), lion(), fox() with firebrand, grain() (standing/burning), olive(),
                      jawbone(), philistines() (feathered head-dresses, round shields), gates() (doors, posts and bar), silver(),
                      mill(), fetters(), temple() (house of Dagon, lords on the roof, two middle pillars), cracks_on();
                      Samson (locks, asleep, blind and praying with a bandage), Delilah, Manoah's wife
  judges_book2.py     writes Judges Book Two (samson_both() = Samson with both arms free, end_mark())
  ruth1.py            sheaf(), field() (rows of ripe barley), reaper() with sickle, gleaner() (a stooping woman), graves(),
                      baby(), naomi_with_child(), heap() (heap of grain), sack(); Naomi, Mara (weeping), Naomi in joy,
                      Ruth (also weeping), Orpah, Boaz
  ruth_book1.py       writes Ruth Book One
  samuel1.py          lamp() (seven-branched lamp of God, lit or smoking), sanctuary() (veil and pillars inside the
                      tabernacle), shiloh() (tent of meeting in its linen court), mat_sleeper(), seat() (Eli's chair,
                      upright or fallen), eli_seated(), dagon(state 0 standing / 1 fallen / 2 stump only), head_alone(),
                      palm(), threshold(), cow()/calf() (milch kine), cart(), yoke(), team() (two kine and the cart with
                      the ark), vial() (horn of oil, pouring), drops(), boy() (child Samuel), eli(), hannah_with_child();
                      Hannah (weeping, joy), Eli (and in awe), child Samuel (day, night), Samuel old (and grieved), Saul
                      (and anointed)
  samuel_book1.py     writes 1 Samuel Book One (philistine(), ark_seized(), fleeing(), shouting() crowd, dagon_house())
  samuel2.py          david() (shepherd tunic, staff, bag; whirl=True spins the sling), sling(), goliath() (brass helmet,
                      coat of mail, greaves, great spear, shield), goliath_fallen(), helmet_alone(), stones(), brook(),
                      flying_stone(), harp() (kinnor), spear_in_wall(), crown(), cave() (bright ragged mouth),
                      skirt_piece(), knife(), gilboa(), spears_down(); David (also bold, grieved), Goliath, Jonathan,
                      Saul as king (also mad, weeping), Jesse
  samuel_book2.py     writes 1 Samuel Book Two (brothers(), army(); KING = crown on a figure's head)
  samuel3.py          2 Samuel kit: dancer() (David in a linen ephod, both arms up, crowned), timbrel(), cymbals(),
                      musician() (timbrel / cymbals / harp), notes(), window() (arched palace window), cedar() (cedar
                      panelling), throne(), table() (the king's table), letter() (sealed scroll), roof() (palace roof
                      over Jerusalem's rooftops), lamb_held(); DAVID_K, NATHAN dicts; David as king (also joyful,
                      wrathful, grieving), David mourning, Nathan (also stern), Michal, Mephibosheth
  samuel3_book1.py    writes 2 Samuel Book One (elders())
  samuel4.py          absalom() (scarlet tunic, gold sash and band, heavy black hair behind), hanging() (caught in the oak,
                      arms up), great_oak() (thick trunk, long boughs; dark=True for silhouettes), bough_over(),
                      balance() (the hair weighed against shekels), gatehouse() (towers, gateway, chamber window, lit=),
                      runner(), stone_heap(), threshing_floor(), altar() (unhewn stones, fire and smoke); DAVID_OLD dict;
                      Absalom (also sly), David old (also alarmed, weeping), the Cushite, Gad
  samuel4_book2.py    writes 2 Samuel Book Two (forest(), mourners() with covered heads, fleeing())
  — website and checking —
  build_site.py       writes the site from volume folders + flat digest folders (DIGEST lists the digest books)
  rebuild_site.py     one step: python3 tools/site/rebuild_site.py [--thumbs] [--out _site]
  assets/site.css, assets/site.js   reader styles and keys/swipe navigation (copied into _site/assets/)
  shots.js            Playwright renders: node tools/site/shots.js <out_dir> page.dc.html …
```

## How to build the next full-edition chapter

1. **Plan from the text.** Print the chapter's verses from `ref/asv` (`asv.Book`) with word counts and group
   them into pages of about 140–160 words. Decide what is full, what (if anything) is a list page or an
   abridged retelling. Every verse of the chapters must end up full, partial (with "…") or knowingly omitted.
2. **Write `tools/full/<volume>/chNN.py`** like `ch01.py`: one function per page registered with `@P(name, title)`;
   text only through `G.v(ref, frm=, to=)` / `G.span(refs)` — never typed by hand. Narration in `cap()`,
   dialogue in `balloon()`, God's words in `god()`; a `vref("GEN 1:3–4")` label on each panel; day/chapter
   stamps. Reuse digest art with `reuse.panels()` where it fits; new drawings go in `<volume>/art.py`.
   Number pages continuously through the volume (chapter 2 starts after chapter 1's last page).
   `ch02.py` adds two helpers worth copying: `rows(...)` (row template + the real panel heights, so each
   viewBox matches its panel) and `entry(...)` (a "scroll" cell for genealogies: name, lifespan bar, verses —
   Genesis 5 is two such pages, every verse in full). Size standing figures with `art2.fit(base, top)` (a
   figure is ~200 units tall at scale 1) so heads stay clear of the captions; figures are drawn front-on.
3. **Add the chapter to `META["chapters"]`** in `tools/full/<volume>/__init__.py`.
4. **Build and check:** `python3 tools/full/build_volume.py genesis` (stops on any text that isn't ASV), then
   `node tools/site/shots.js /tmp/png volumes/genesis/pages/GEN-C02-*.dc.html` and look at every page.
5. **Publish** the new pages plus `canvas.json` to the volume's canvas (read its `project/canvas.json` first).
6. **Site and repo:** optionally preview with `python3 tools/site/rebuild_site.py --thumbs` (writes `_site/`);
   update the status table above and commit `volumes/` + `tools/` — the push deploys the site.

Starting a new volume: `tools/full/<id>/` with `__init__.py` (META with id, order, name, kanji, thumb
`vol-<id>-`, book code, chapters), `cover.py`, `art.py`, `ch01.py`; a new canvas from the Design type.

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

**Covers:** "THE BOOK OF" / "No. NN", the series title in Anton 136–168 px (shrink longer names), "Book N — Name",
"Chapters a – b", a vertical kanji block in the accent color (創世記 SŌSEIKI for Genesis,
出エジプト記 SHUTSU for Exodus, 民数記 MINSŪKI for Numbers, ヨシュア記 YOSHUA-KI for Joshua, 士師記 SHISHIKI for Judges, ルツ記 RUTSU-KI for Ruth, サムエル記上 SAMUERU-KI JŌ for 1 Samuel), one short ASV caption, "Adapted from the American Standard
Version (1901)" and "Vol. N" at the bottom.

**Recurring components** (all in `tools/kit/mk.py`):
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
  - Aaron: grey beard, blue headcloth with cord. Hur appears only as a silhouette (brown robe).
  - Joshua: young, black hair, stubble, scowl, fire-orange rim light.
  - The new Pharaoh (from Exodus 1): black-and-gold nemes, false beard, kohl; afraid and weeping variants.
  - Pharaoh's magicians: black-and-white headcloth, kohl, purple rim light.
  - Miriam: brown hair when young; old Miriam has grey hair and a pink headscarf, with a timbrel.
  - Pharaoh's daughter: black hair, gold band, collar, kohl. Zipporah: red headscarf.
- **Character guide (Numbers, Joshua):**
  - Caleb: green headcloth with cord, brown beard, gold rim light. The spies: bareheaded, stubble, sweat.
  - Balaam: purple headcloth, grey-black beard, scowl (awe variant with sweat); rides a grey ass.
  - The angel of Jehovah: white robe, gold rim, wings, sword drawn. The prince of Jehovah's host: crimson robe,
    gold breastplate and rim light, sword drawn, no wings.
  - Joshua as leader (Joshua book): rust-red headcloth with cord, black beard, scowl; old Joshua: white hair and beard.
  - Rahab: scarlet headscarf, black hair.
- **Character guide (Judges):**
  - Deborah: gold headscarf, black hair, light rim; a yellow robe at a distance. Barak: slate-blue headcloth, black beard.
  - Jael: green headscarf, scowl; shown only in silhouette at the tent-pin (keep it restrained, no gore).
  - Gideon: tan headcloth with cord, stubble (afraid with sweat, bold with fire light); calm and bearded at the end.
  - Midian: camels with red saddle-cloths, dark tents.
  - Samson: dark curly hair with seven long braided locks, black beard, rust-red tunic at a distance; after the
    shaving no locks and a grey tunic; blind Samson wears a cloth band over the eyes (no wounds shown).
  - Delilah: black hair with a gold band. Manoah's wife: slate-blue headscarf. Philistines: white feathered
    head-dresses on a blue band, round bronze shields; their lords in tunics of blue, red, gold and purple.
- **Character guide (Ruth):**
  - Ruth: rose-pink headscarf, dark hair (rose robe at a distance). Orpah: saffron headscarf.
  - Naomi: purple headscarf with grey hair; Mara is the same face weeping in cold blue light; joyful at the end.
  - Boaz: white headcloth with a dark cord, grey-brown beard, white robe at a distance.
- **Character guide (1 Samuel):**
  - Hannah: teal headscarf and teal robe. Peninnah: red robe, with her children.
  - Eli: white hair and beard, blue headcloth with a gold band, blue robe. Child Samuel: dark curls, white linen tunic.
  - Samuel grown: grey beard, midnight-blue headcloth and robe. Saul: black hair, stubble, crimson headcloth and tunic,
    drawn a head taller than everyone. Dagon: gilded torso, green fish-scale lower body, fish-head crown.
  - Eli's death is caption-only (an overturned chair by the gate).
  - David: ruddy, auburn curls, no beard; sand tunic with staff, shepherd's bag and sling.
  - Goliath: brass helmet with a red crest, scale coat of mail, brass greaves, a spear taller than he is.
  - Jonathan: blue headcloth and tunic, stubble. Saul as king: black beard, crimson headcloth with a gold band,
    crimson tunic, small gold crown on his figure. Jesse: grey beard, brown headcloth.
  - Goliath's death stops at "he fell upon his face" (17:46 and 17:51's beheading are not shown); Saul's death on
    Gilboa is 31:1 and 31:6 only, drawn as his crown and spear on the mountain.
- **Character guide (2 Samuel):**
  - David as king: auburn hair and beard, purple headcloth with a gold band; purple tunic with a small gold crown;
    a white linen ephod when he dances before the ark.
  - Nathan: grey beard, olive-green headcloth and tunic. Michal: crimson headcloth with a gold band (Saul's colour).
    Mephibosheth: blue headcloth and tunic like his father Jonathan. Bath-sheba appears only as a mother with Solomon.
  - 11:2 is caption-only (David alone on the roof); Uriah's death is a distant silhouette.
  - David's lament (1:19–27) is poetry the fetch tool won't quote; Book One uses 1:11–12 and 1:17 instead.
  - Absalom: heavy black hair to the shoulders, gold band, scarlet tunic with a gold sash, stubble. David old:
    grey-auburn hair, pale beard, purple headcloth with the gold band. The Cushite: white headcloth.
  - Absalom's death (18:14–15) is not shown: 18:9 (caught in the oak) then 18:17 (the heap of stones).
- **Genesis faces:** Adam, Eve, Cain, Noah, Abraham, Sarah, Isaac, Jacob, Esau, Rachel, Joseph (also in
  Egyptian dress, weeping), Pharaoh of Joseph's day (gold-and-blue nemes), old Jacob — all in `faces.py`.
- **Serpents:** always `snake.py` (tapered body, belly scutes, blotches, viper head). The magicians'
  serpents are the brown recolor `exodus2.serpent(..., brown=True)`.

## Text rules

- **American Standard Version (1901)** only, word for word. Trim with `…`; never paraphrase or
  modernize. Keep ASV wording: "Jehovah", "Jehovah God", "waste and void", "great sea-monsters",
  "kine", "murrain", "to-day", "the Cherubim".
- **Source: `ref/asv/*.usfm`** (eBible.org, public domain; Strong's tags and footnotes are stripped by `asv.py`).
  The full edition cuts every word out of it with `asv.Book`, and `build_volume.py` re-checks every caption,
  balloon and Voice box against it. Poetry (the Song of Deborah, David's lament, Jacob's blessing) is in the
  file too — no more fetch-tool refusals. For the digest, the old source was `https://ebible.org/asv/<BOOK><NN>.htm`.
- **Don't** quote the NASB, NAB or any other copyrighted translation. If asked for one, offer the ASV or the
  World English Bible (also public domain).
- Captions carry narration, balloons carry dialogue, God's words always use the Voice box.
- Text that is not scripture (chapter titles, credits) carries `data-label` so the text check skips it.

## Website (built by GitHub Actions)

A static site built from both editions. Nothing generated is committed: on every push to `main`,
`.github/workflows/pages.yml` checks each volume (`build_volume.py <vol> --check`), runs
`rebuild_site.py --thumbs --out _site` (Python + Pillow, Node + Playwright Chromium) and deploys `_site/`
as a GitHub Pages artifact. Thumbnails are cached between runs (actions/cache on `_site/thumbs`), so a
push only re-renders pages whose source changed; a cold build of all ~190 thumbnails takes about 2 minutes.
One-time setting: repo Settings › Pages › Source: **GitHub Actions**. Runs: the repo's Actions tab
(it can also be started by hand with "Run workflow").

- `index.html`: "The Full Edition" first (one section per volume, a card per chapter), then
  "Digest Editions" (smaller cards, with a note), then a table of contents.
- Full edition: `<volume>/chapter-NN/index.html` and `<volume>/chapter-NN/NN-<slug>.html`
  (page labels use the printed page number). Digests: `digest-<series>/book-NN/…`.
  Prev/Next chains within each edition, across books.
- `manifest.json`: every series/volume, book/chapter and page (title, verse ref, URL, thumbnail, source).
- `thumbs/`: 380×540 JPGs — `vol-<volume>-chapter-NN-<slug>.jpg` for the full edition; the digest
  keeps its old names (`book-NN-…` for Genesis, `<series>-book-NN-…` for the others).
  `thumbs/.sources.json` keeps a hash of each thumbnail's source page; changed pages are re-rendered and
  unused thumbnails deleted automatically.

Local preview (same command the workflow runs; output in git-ignored `_site/`):
```
python3 tools/site/rebuild_site.py --thumbs   # needs node + playwright + Pillow; open _site/index.html
```
Volumes come from `volumes/*/volume.json` (written by `build_volume.py`); digest books are listed in
`DIGEST` in `tools/site/build_site.py`. Always run `build_volume.py` and commit its output after changing a
volume's sources, or the workflow's `--check` step fails the deploy.

## Checking pages

`node tools/site/shots.js <out_dir> page.dc.html …` renders PNGs with Playwright. The sandbox has no
Anton/Archivo/Plex fonts, so renders use wider fallbacks: if text fits there, it fits on the canvas.
Look at people, faces, balloon tails, overlaps and cut-off art before publishing. A lifted panel keeps its
original viewBox and is cropped (`slice`) to the new panel, so give it a row of similar proportions.

## Working notes for Claude

- **Pushing:** Claude can't push to GitHub from its cloud session (GitHub is blocked from both the cloud
  and the Mac's sandbox). It commits in its own copy, writes the files into the user's clone at
  `~/_GITHUB/apphaus2/Bible` and commits there; the user runs `git push`.
- **"continue"** from the user means: build the next full-edition chapter.
- **"commit" / "update github"** means: write the latest repo files to the Mac clone, commit, and give the push
  command. The push deploys the site; there is no generated site folder to commit.
- Commit messages end with the Co-Authored-By and Claude-Session lines; the git author is Sky.

## Roadmap

- Full edition: finish Genesis (chapters 2–8), then Exodus, then on through the digest's books and beyond
  (1 Kings next after 2 Samuel). Delete the digest once the full edition covers its books.
- `mk.person(..., up=…)` needs `"ManUp"`/`"WomanUp"` in that panel's `defs()`, or the figure renders headless.
- Possible option: right-to-left reading order.
