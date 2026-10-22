# CLAUDE.md — Bible Manga

The Bible as a full-colour manga in a 1980s cyberpunk-manga style (the general style only: never Akira's characters, logo,
red motorcycle, capsules, Neo-Tokyo or white-dome explosion), every word of scripture cut from the **ASV**. Python generates
every page (nothing is drawn by hand); the repo is the only source of truth. Served at **https://bible.apphaus.us**.

- **The manga** (`volumes/<id>/`): one volume per book of the Bible, in manga chapters of ~15–25 pages, ~140–160 words a page,
  story-complete: every verse full (lists as roll cells/charts, never dropped). Each volume has `coverage.md` (every verse
  full / partial / omitted), `volume.json` (chapters, blurbs) and `canvas.json` (page order and titles, read by the site).
- **Reference art** (`tools/full/reference/<series>/book-NN/`): 154 pages of the old digest whose drawings the early volumes lift
  (`reuse.panels()`, `<vol>.common.D(...)`); never published, never added to. New drawings go in `<pkg>/art.py`.

## Status

**Complete: the whole Old Testament, Genesis through Malachi (39 volumes, 4,478 pages, 23,145 verses).** Per-chapter detail is
in each `volumes/<id>/volume.json` and `coverage.md`. The New Testament waits on local branches: `wip/matthew`, `wip/mark`,
`wip/luke`, `wip/john`, `wip/acts` (first drafts; only Mark has a chapter). Next: those, then Romans–Revelation. The minor
prophets share `oba/minor.py` (`Kit`: page packing) and each other's art; Ezekiel's temple plans are `ezk.common.paged/plate`.

| # | Book | Package | Chapters | Pages | Verses |
|---|---|---|---|---|---|
| 1 | Genesis | `genesis` | 17 | 281 | 1,533: 1,512 full, 4 partial, 17 omitted (abridged retellings 24:38–47, 41:18–24, 42:31–34) |
| 2 | Exodus | `exo` | 12 | 219 | 1,213 full |
| 3 | Leviticus | `lev` | 9 | 128 | 859 full |
| 4 | Numbers | `num` | 16 | 230 | 1,288 full |
| 5 | Deuteronomy | `deu` | 15 | 169 | 959 full |
| 6 | Joshua | `jos` | 10 | 103 | 658 full |
| 7 | Judges | `jdg` | 10 | 137 | 618 full |
| 8 | Ruth | `rut` | 2 | 22 | 85 full |
| 9 | 1 Samuel | `sa1` | 14 | 193 | 810 full |
| 10 | 2 Samuel | `sa2` | 12 | 168 | 695 full |
| 11 | 1 Kings | `kg1` | 14 | 181 | 816 full |
| 12 | 2 Kings | `kg2` | 13 | 169 | 719 full |
| 13 | 1 Chronicles | `chr1` | 11 | 127 | 942 full |
| 14 | 2 Chronicles | `chr2` | 14 | 174 | 822 full |
| 15 | Ezra | `ezr` | 5 | 43 | 280 full |
| 16 | Nehemiah | `neh` | 7 | 77 | 406 full |
| 17 | Esther | `est` | 4 | 43 | 167 full |
| 18 | Job | `job` | 12 | 154 | 1,070 full |
| 19 | Psalms | `psa` | 17 | 428 | 2,461 full |
| 20 | Proverbs | `pro` | 11 | 136 | 915 full |
| 21 | Ecclesiastes | `ecc` | 4 | 54 | 222 full |
| 22 | Song of Solomon | `sng` | 3 | 33 | 117 full |
| 23 | Isaiah | `isa` | 18 | 282 | 1,292 full |
| 24 | Jeremiah | `jer` | 19 | 299 | 1,364 full |
| 25 | Lamentations | `lam` | 2 | 36 | 154 full |
| 26 | Ezekiel | `ezk` | 18 | 268 | 1,273 full |
| 27 | Daniel | `dan` | 6 | 78 | 357 full |
| 28 | Hosea | `hos` | 3 | 41 | 197 full |
| 29 | Joel | `jol` | 1 | 16 | 73 full |
| 30 | Amos | `amo` | 2 | 36 | 146 full |
| 31 | Obadiah | `oba` | 1 | 6 | 21 full |
| 32 | Jonah | `jon` | 2 | 15 | 48 full |
| 33 | Micah | `mic` | 2 | 26 | 105 full |
| 34 | Nahum | `nam` | 1 | 11 | 47 full |
| 35 | Habakkuk | `hab` | 1 | 12 | 56 full |
| 36 | Zephaniah | `zep` | 1 | 12 | 53 full |
| 37 | Haggai | `hag` | 1 | 9 | 38 full |
| 38 | Zechariah | `zec` | 4 | 49 | 211 full |
| 39 | Malachi | `mal` | 1 | 13 | 55 full |

Order numbers and ids for the rest: Matthew 40 "matthew", Mark 41, Luke 42, John 43, Acts 44,
Romans 45 … Revelation 66 ("Volume Forty" … "Volume Sixty-Six"). Book codes are the USFM ones in `ref/eng-asv` file names.

## Rules

- **Text:** ASV only, word for word, cut from `ref/eng-asv/*.usfm` with `asv.Book` — never typed, paraphrased or modernised
  ("Jehovah", "waste and void", "kine", "to-day"). Trim only with "…". Never quote a copyrighted translation (offer the ASV or WEB).
  Captions narrate, balloons carry speech, God's words always go in the Voice box. Non-scripture text (titles, credits, labels)
  carries `data-label` so the text check skips it.
- **Attribution: always just "ASV"** — never spelled out, never with a year, anywhere (`adr/0001-asv-attribution.md`).
- **God is never drawn**, not even a hand: light, storm, fire, an empty throne, the Voice box. Satan and demons are never drawn.
  Angels are figures of white light with a gold rim, no faces (wings only where the text gives them, e.g. seraphim, cherubim).
- **Restraint:** violence, death and sexual matters are told in words over landscapes, empty places, smoke, gates, shut doors,
  heaps of stones — nothing gory or explicit drawn. Each package's `__init__.py` lists its restraint decisions.
- **People:** realistic, well-proportioned figures (kit silhouettes via `mk.person()`, faces via `faces.face()`); never blobs or
  stick figures; serpents always `snake.py`. Keep each character's look consistent (see Cast).
- **Generated pages are never hand-edited:** fix the Python, rebuild, commit `tools/` and `volumes/` together.

## Building a chapter

1. Print the verses (`asv.Book("GEN").verses` is `{(c, v): text}`), group them ~140–160 words a page; lists become roll cells.
2. Write `tools/full/<pkg>/chNN.py`: `PG = Pages(start)` (`num/pages.py`; chapter 1 `Pages(1)`, later
   `Pages(_prev.START + len(_prev.PAGES) - 1)`), a title page `@P("<CODE>-C0N-00-Title", …, title=True)` + `fx.chapter_title`,
   then `PG.extend(discourse.pack(SEGS, prefix, PG.next(), …))` with segments `face([...], ref, FACE)` / `drawn([...], ref, art_fn, bg)`
   built from line helpers (`cp`/`caps` narration, `say`/`says` speech, `gd`/`gods` Voice box, `sg`/`sgs` poetry, `joined()`).
   Text only via `G.v(ref, frm=, to=, after=)` / `G.span("1:1-3")`. Last page: `end=end_mark("NEXT · …", …)`; last chapter of a book
   `end_mark("END OF <BOOK> · NEXT · <NEXT>", …, ch="完")`. Model packages: `chr2` (OT narrative), `jer`/`isa` (prophecy), `psa`/`job`.
3. Add it to `META["chapters"]` (module, dir, num, name, range, bible_chapters, blurb; `span` for a chapter starting mid-chapter).
4. `PYTHONUTF8=1 python tools/full/build_volume.py <pkg>` must end `0 not found, 0 lost` (every text block is ASV, every cut is on
   a page); `--check` writes nothing and fails on stale pages. Render with `node tools/site/shots.js <dir> volumes/<id>/pages/*.dc.html`
   and look at every page: captions over faces, clipped figures, lone panels, stamps over names, a caption repeated inside a
   balloon (a `say(..., frm=)` missing its `to=`).
5. Add the book's row above and commit.

A new volume: `tools/full/<pkg>/` with `__init__.py` (plan docstring + `META`: id, order, name, kanji, thumb `vol-<id>-`, book
code, title, volume, lede, chapters; `G = Book(code)`), `common.py` (line builders, cast faces), `cover.py`, `art.py`
(`from <prev>.art import *` to inherit drawings), `ch01.py`. Package names can't start with a digit (`kg1`, `chr2`) or shadow a kit
module (`exo`, not `exodus`).

## Code map

```
ref/<eBible id>/      Bible texts as USFM from eBible.org (see ref/README.md): eng-asv (the manga), spaRV1909, fraLSG
tools/full/           asv.py (Book: cuts, coverage; BIBLE_LANG), build_volume.py, fx.py (page(), chapter_title(), end_mark(), vref()),
                      discourse.py (pack: by_need, room, min_size, budget, default_head), speech.py (orate), rolls.py (roll_pages,
                      verse_cells), reuse.py (lift reference panels; fill()), picto.py, ntcast.py (New Testament cast),
                      <pkg>/ one package per book
tools/kit/            mk.py (page, panel, cap, god, balloon+tail, stamp, sfx, person(up=), defs, speed, stars), faces.py + faces_ex.py,
                      figures.json, snake.py, crowds.py, and per-book drawing kits: exodus*.py, numbers1, joshua1, judges1–2, ruth1,
                      samuel1–4, egypt, tower, ladder
tools/site/           build_site.py, rebuild_site.py, shots.js, assets/site.css + site.js
tools/book/           export_book.py + render.js (EPUB, print/reading PDF), downloads.py, asv_pdf.py (the ASV text as PDFs)
volumes/<id>/         generated pages (pages/*.dc.html), canvas.json, volume.json, coverage.md; volumes/<lang>/<id>/ for translations
```

Package notes (helpers worth reusing; each package's `__init__.py` has its plan and restraint notes):
- `genesis`: `art2.fit(base, top)` sizes standing figures; `art3` map helpers `grid_bg/node/route/label`; `art10.stage()` scene
  builder; `ch02.entry`/`rows`, `ch03.clan`/`hud`, `ch14.talk` dialogue panels.
- `exo`: `kit.talk/song/law`, `kit.law_pages(carry=)`, `kit.blueprints`, `art8` blueprint `bp/dim/tag`; `exodus_map`, `wonders`.
- `lev`/`num`: laws as `law_pages` cells with `lev/art` pictograms; `num/pages.py` (`Pages`); tally/clan/station cells; camp and
  march plans, spy, journeys, stations and borders maps.
- `deu`: `speech.orate` + `discourse.pack`, `deu.common.auto/law_chapter/sing/shade`. `jos`/`jdg`/`rut`/`sa1`/`sa2`: `common.face/drawn/
  over`, `D("A3", 0)` lifts reference panels, `jos.art.below()` sets a drawing under the words, battle maps; `sa1` packs with
  `by_need=True, room=0.92, min_size=12.5`; `asv.Book.v(..., after=)` for a phrase said twice in a verse.
- `kg1`/`kg2`: temple blueprints (`temple_plan`, `pillar_elev`, `molten_sea`, `base_laver`), `reign()` roll cells (Judah gold,
  Israel red), `joined()`, Elijah/Elisha figures, Assyria/exile maps; `rolls.roll_pages(..., end=)`.
- `chr1`/`chr2`: `lineage`/`branch` charts (staggered names), `cell/cells/roll`, `lot_grid`, `tally`, `porters_plan`, `month_wheel`;
  reuse 1–2 Kings cast and drawings; battle maps and fortification plans. `ezr`/`neh`: letter scrolls, return caravan, `wall_plan`,
  `plan_pages`. `est`: all new art (palace, king's gate, `inner_court`, `pur_wheel`, `adar_days`), `crowned(tok)`, no Voice box.
- `job`: `jdiscourse`/`jspeech` colour each speaker's song lines; `pf/pd/pf2/pd2/gpd`. `psa`: `psa.text` cuts superscriptions, book
  heads and line breaks from the USFM; `psa.common.psalm(n, "1 tree | 4 chaff", god=)` plans; ~120 scenes in `psa.art.SCENES`.
  `pro`: saying cells under emblems (`sayings`, `pick()`); Wisdom in white and gold. `ecc`/`sng`: `common.drawn`, `paged()`,
  `sng.art.plate` likeness cells.
- `isa`: `S("c:a-b", kind, looks)` alternates Isaiah's face and drawings; `art2.nations_map(hi=, arrows=)`. `jer`: `O`/`S`, `cut()`,
  `jer(age, mood)` faces, `near_east()`, `pagepack.py` merges lone panels. `lam`: `L(c, a, b, d=|t=)` one song box per verse.
- `dan`/`hos`/`jol`/`amo`: `dan/kit.py` `Lines(G, code, book, SPK)` (captions, Voice boxes, per-speaker speech), packed with
  `job.jdiscourse`; `dan.art.glow_fig` angels; beasts as heraldic plates.

## Visual style

80s airbrushed manga colouring: black ink over flat saturated fills and gradients, each panel its own background gradient; gutters,
captions and balloons cream/white. Paper `#F3EFE6`, ink `#0D0D0F`, red `#D7261E` (stamps, cover kanji), night `#0B0B2A→#1E1650→#5B2470`,
Voice box `#12113A` with a `#FFD23F` gold inner rule, light `#FFE680→#FFC14D→#FF6A2A`, sea `#8FD0E2`/`#0F4C68`/`#1F6F9A`, earth
`#4A2418`/`#C8682E`/`#C8A06A`, greens `#2E6B3A`/`#9CCB5E`, blood `#8A0E16`, Egypt gold `#E8B830` / blue `#1F5FAD`.
Fonts: Anton (Voice box, titles), IBM Plex Mono (captions, labels), Archivo Narrow 700 (balloons), Noto Sans JP 900 (SFX, kanji).
Page 760×1080, padding `28px 26px 30px`, grid rows with 12 px gaps, 3 px panel borders (full width 702, half 342); running foot:
verses left, `— NN —` centre, ASV right. Components: `cap()`, `god()`, `balloon()`+`tail()` (tail before the balloon, tip at the
mouth), `sfx()` (katakana + romaji), `stamp(n)` once per chapter, `ref()`. Covers: "THE BOOK OF" / "No. NN", the name in Anton
136–168 px, a vertical kanji block in the accent colour (創世記 SŌSEIKI …; NT: マタイによる福音書, マルコ…, ルカ…, ヨハネ…, 使徒行伝,
ローマ人への手紙, other letters katakana + 書/への手紙, ヨハネの黙示録), one short ASV caption, "ASV" and "Vol. N".

**Page format** (`.dc.html`, from the retired Claude Design canvases): keep `<script src="./support.js"></script>` in `<head>`;
markup inside `<x-dc>`; fonts from one Google Fonts `<link>` in `<helmet>`; closed elements, quoted attributes, inline styles;
inline SVG and CSS gradients only (no images, emoji, scripts or iframes); per-panel SVG id prefixes; `{{hole}}` is a plain lookup.

## Cast

Figures at a distance: `figures.json` silhouettes with a robe/tunic colour; women use WOMAN + a separate HAIR `<use>`; raised arms
`person(..., up=[…])` (needs `"ManUp"`/`"WomanUp"` in that panel's `defs()` or the figure renders headless); kneeling `exodus.kneel()`;
lying LIE_BODY + LIE_ARM (never rotate a standing figure). Close-ups: shaded profile faces (`face(tok, x, y, s, flip=)`). A warm
`scarf=` reads as long hair: use cool, dark or off-white headcloths, or a gold hem (`exo.art.HEM`).

- **Genesis:** Abram/Abraham grey hair and beard, slate-blue robe (white in old age); Sarai mulberry headscarf (grey-haired from 17);
  Lot maroon; Hagar cerulean, kohl; Melchizedek white with a gold band and crown; Noah's sons share one skin, robes blue/rust/green;
  Isaac brown curls → brown beard → blind white-haired; Rebekah green headscarf; Laban rust-red headcloth; Esau red curls and stubble,
  rust tunic; Jacob dark curls, slate-blue robe, black beard from 29:21, greying from 34; Rachel bareheaded, rose robe; Leah indigo
  headscarf; Joseph brown curls, coat of many colours (stripes) until 37:23, then a cream tunic, in Egypt collar and kohl (never a
  nemes); Judah off-white headcloth, black beard; Pharaoh of Joseph's day gold-and-blue nemes. Men in white at Mamre and Sodom: gold
  rim, no faces.
- **Exodus–Deuteronomy:** Moses off-white headcloth, black beard (young: Egyptian red-and-white headcloth, kohl); Aaron grey beard,
  blue headcloth (high priest: white mitre); Joshua young, black curls, rust tunic; the new Pharaoh black-and-gold nemes; Miriam
  brown hair (old: grey, pink scarf); Zipporah crimson scarf with gold hem; Jethro white beard, dark-teal headcloth; Caleb green
  headcloth; Balaam purple headcloth on a grey ass; the angel of Jehovah white, winged, sword drawn.
- **Joshua–Ruth:** Joshua rust-red headcloth, black beard (old: white); Rahab scarlet scarf; Deborah gold scarf; Barak slate-blue;
  Jael green scarf, silhouette only; Gideon tan headcloth; Samson seven braided locks, rust tunic (shaved: grey tunic; blind: a cloth
  band); Delilah black hair, gold band; Philistines white feathered head-dresses; Ruth rose scarf; Naomi purple scarf, grey hair;
  Boaz white headcloth, grey-brown beard.
- **Samuel–Kings–Chronicles:** Hannah teal; Eli white beard, blue headcloth with gold band; Samuel midnight blue; Saul crimson, a head
  taller (king: gold band and small crown); David auburn curls, sand tunic (king: purple headcloth with gold band, auburn beard;
  old: grey-auburn); Jonathan blue; Goliath brass helmet with red crest; Nathan olive green; Absalom heavy black hair, scarlet tunic,
  gold sash; Solomon, Elijah (hairy brown mantle, bareheaded), Elisha and the kings in `kg1`/`kg2` art; Ezra white beard, indigo
  headcloth with gold band; Nehemiah black beard, slate-blue headcloth with gold cord; Esther and the Persian court in `est.art`.
- **Wisdom and prophets:** Job white headcloth with gold band, then a sackcloth hood; Eliphaz teal, Bildad slate-purple, Zophar deep
  blue, Elihu young in green; Jeremiah dark blue-grey headcloth, beardless at his call, greying; Isaiah from `kg2.common.ISAIAH`;
  the servant and the anointed one of Isaiah are never drawn.
- **New Testament** (`tools/full/ntcast.py`, shared by every NT volume; never redraw these): Jesus is drawn as a man, always the same
  (the user's choice) — olive-brown skin, shoulder-length dark-brown hair, short dark-brown beard, undyed off-white robe, blue-grey
  mantle, soft gold glow, no halo; faces `JESUS`, `JESUS_TEACH`, `JESUS_STERN`, `JESUS_GRIEF`, `JESUS_PASSION`, `JESUS_RISEN`, figure
  `jesus_fig(p, x, y, s)`; his words are ordinary balloons. Also Peter, Andrew, James, John, Matthew, Thomas, Philip, Judas, Mary,
  Mary Magdalene, Martha, John the Baptist, a Pharisee, Caiaphas, Pilate, Herod, a centurion, Paul, with `ROBES`. The Father's voice:
  Voice box over light; the Spirit at the baptism: a dove of light. The passion: scourging and thorns as words over the empty court;
  the crucifixion only as three crosses on a hill against a darkened sky, from a distance, no wounds or blood; his death as words
  over the hill and the rent veil; the sealed tomb; the resurrection as the stone rolled away and the folded linen, then Jesus risen
  in white light. Parables drawn as their own scenes; the genealogies as lineage charts over roll cells.

## Languages

The site is in **ten languages**: English, Spanish (`es`), German (`de`), French (`fr`), Italian (`it`), Portuguese (`pt`), Russian
(`ru`), Chinese (`zh`, simplified), Japanese (`ja`) and Korean (`ko`), at bible.apphaus.us/<code>/. `ref/` holds the public-domain
texts (`ref/README.md` lists the ones in use and eBible's 64 public-domain whole Bibles): `eng-asv` (the manga), `spaRV1909`,
`deu1912`, `fraLSG`, `ita1927`, `porbrbsl`, `russyn`, `cmn-cu89s`, `jpnm`, `KorRV` (CrossWire, not eBible), and fallbacks for
verses a file lost (`spablm`, `deuelo`, `cmn-cu89t`). Spanish is the worked example below; every language works the same way.

- **Pages:** `BIBLE_LANG=es python tools/full/build_volume.py <pkg>` builds the same plans with the Spanish text into
  `volumes/es/<id>/` (generated in CI, git-ignored). `asv.Book` keeps `G.verses` in English (plans find their ASV words there) and
  hands out the translation: each cut is mapped onto the translated verse by its share of the letters, snapping to a break of the
  same kind (a speech break lands on the colon before the words spoken; cuts of one verse chain end to start); text a plan cuts
  again by an English phrase is a `Cut` that answers in ASV positions. The text check runs against the translation.
- **Verse numbering:** eBible's RV1909 keeps English verse numbers but shifts the words where its own numbering differs, leaving
  slots empty (and loses Job 39:28–40:5 and Numbers 30:16). `asv.align` re-pairs the chapters around any empty slot or any run of
  verses out of proportion (Gale–Church by length); the language's `versemap` spells out Job 38–41 and Numbers 29–30; lost verses
  come from its `fallback` (`spablm`, which says "Yahvé") and are listed in that volume's `coverage.md`. Psalm superscriptions: a
  text's own `\d` lines, else split off verse 1 by its `psalm_title` regex (RV1909: where the first word is in capitals); RV1909 has
  no poetic line breaks.
- **Labels** (titles, stamps, headings, map and chart labels, blurbs, ledes — not scripture): `tools/full/labels.py collect` lists
  every label of the English pages; `tools/full/i18n/es/*.json` maps each to Spanish (names in RV1909's spelling, quotations in
  RV1909's words); `labels.label()` translates a label whole or piece by piece (split at " · " and " — "), and verse references by
  rule (the language's `books` and `abbr`: "GEN 1:3" → "GN 1:3"). `python tools/full/labels.py missing es` lists what is still English;
  `leftover <lang>` lists English labels on built pages, but skips a node already partly translated, and page titles (canvas.json
  board titles, which go through the same tables) need their own comparison.
- **Site:** `rebuild_site.py --lang es` builds `_site-es/es/` (its own thumbnails, `_book/asv-es/` from `asv_pdf.py --text spaRV1909`,
  `_book/download/es/` from `downloads.py --lang es`). `build_site.py` takes its interface words from the language's `ui` and puts a
  **language dropdown** in every page's top bar (`lang_menu`: each language named in itself, linking to the page there whose verses
  start at or before this page's — page counts differ between languages — else that chapter, else that language's home).
- **Workers:** `bible` (`wrangler.jsonc`, `tools/site/workers/router.js`) owns bible.apphaus.us and serves nothing itself: `/es/…`
  goes to `bible-es` (`tools/site/workers/es.jsonc`, `_site-es/`), the rest to `bible-en` (`en.jsonc`, `_site/`), by service
  bindings. Each language Worker has its own 100,000-file limit (a language is ~18,000 files once the Bible is done).
- **A language is one file, `tools/lang/<code>.json`** (`tools/lang/langs.py` documents every key): its text, credit, fallback,
  versemap, psalm_title, `unspaced` (Chinese, Japanese: a cut may fall between any two characters, and the text check ignores
  line breaks), reference rules, the site's `ui`, the text PDF's `words`, the EPUB's `epub`, and `fonts` (Google Fonts families
  for a script the manga's fonts lack, set after each manga font in every font list of its pages, PDFs and EPUBs). Plus its text
  in `ref/<id>/`, its labels in `tools/full/i18n/<code>/`, a `tools/site/workers/<code>.jsonc` and a service binding in
  `wrangler.jsonc`; every tool and the workflow pick it up from there. Right-to-left scripts later.

## Website

Built by `.github/workflows/pages.yml` on every push to `master` (nothing generated is committed): `build_volume.py --check`
for every package, every translation's volumes (`BIBLE_LANG=<code>`, each `tools/lang/<code>.json`), the text PDFs by book
(cached), the downloads (every language, cached), `rebuild_site.py --thumbs` and `--lang <code>` (thumbnails cached), then deploys
`bible-en`, each `bible-<code>` and the
router `bible` to Cloudflare (`npx wrangler@4 deploy -c tools/site/workers/<lang>.jsonc`, then `npx wrangler@4 deploy`; Node 22),
and the English site alone to GitHub Pages (apphaus2.github.io/Bible, without the downloads: its 1 GB limit). Needs Actions secrets
`CLOUDFLARE_API_TOKEN` ("Edit Cloudflare Workers" template, zone apphaus.us) and `CLOUDFLARE_ACCOUNT_ID`, else the Cloudflare step
is skipped (not yet set). By hand from Windows: `npx wrangler login` once, build the sites, deploy the three Workers (account
apphaus@outlook.com).

- Pages: `index.html` (a section per volume with its downloads, "The Text", a table of contents), `<id>/chapter-NN/index.html`,
  `<id>/chapter-NN/NN-<slug>.html` (Prev/Next across books). All links relative.
- Reader (`site.js`): arrow keys; a swipe is a quick one-finger flick (¼ screen, ≥ 90 px, mostly sideways, < 0.6 s); a second
  finger cancels and blocks swipes for 0.6 s; nothing turns while zoomed or after a pan. Keep these rules: phones zoom to read.
- `asv/<BOOK>.pdf` (66 files, `asv/index.json`): the ASV by book; the "📖 p. N" button, "<range> in the ASV" and every footer
  credit open the book at the page's chapter. The whole-Bible PDF is built only to split it, never published.
- `download/en/`: each book as `<id>.epub` (fixed layout) and `<id>.pdf` (reading PDF at page size), split at chapter boundaries
  into `<id>-1.pdf` … under 24 MB (Cloudflare's 25 MiB file limit: Genesis is two parts). Links are absolute to bible.apphaus.us.
- `manifest.json` (every volume, chapter, page, thumbnail, text and download URL); `thumbs/` 380×540 JPGs, re-rendered by hash.

Local: `python tools/site/rebuild_site.py --thumbs` (Node + Playwright + Pillow) → `_site/`; `python tools/book/downloads.py` first
to include downloads. `export_book.py <id>` alone writes an EPUB and a 7 × 10 in print PDF with bleed (`--screen`: the reading PDF);
fonts are fetched from Google Fonts, subset and embedded. Before a print run: CMYK proof, preflight, epubcheck.

## Working notes for Claude

- Windows, in `C:\_GITHUB\apphaus2\Bible` or a worktree under `.claude/worktrees/`. Run Python as `PYTHONUTF8=1 python …`; Node +
  Playwright may live in a scratch folder (`NODE_PATH`). Renders use fallback fonts: if text fits there, it fits on the site.
- "continue" = build the next chapter. "commit" / "update github" = commit straight to `master` (from a worktree, commit there and
  fast-forward `master` in the main clone); the user runs `git push` (the SSH key has a passphrase). No CRLF-only commits.
- Git author Sky <sky75.morey@gmail.com>; commit messages end with the Co-Authored-By line.
- Parallel builders: one worktree per book from one brief; merge when a book is done (check `--check`, sample pages, add the row).
- Possible later: right-to-left reading order.
