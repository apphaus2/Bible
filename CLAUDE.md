# CLAUDE.md — Bible Manga

Context for Claude (and humans) working in this repo. Read this first.

## What this is

A manga adaptation of the Bible, drawn as full-color vector pages in a 1980s cyberpunk-manga style
(general style only: never Akira's characters, logo or imagery), with every word of text taken from the
**ASV**. Everything is built in this repo with Claude Code (Python generates every
page; nothing is drawn by hand), and GitHub Actions builds and deploys the website to GitHub Pages on every push
to `master`; it is served at **https://bible.apphaus.us**. The repo is the only source of truth: review pages with `shots.js` renders or the website.

The manga (`volumes/`; "the full edition" in older notes and code): one volume per book of the Bible, split into
  manga chapters of roughly 15–25 pages. Target: every scene and every line of dialogue word for word
  ("story-complete"): narrative verses in full; genealogies and lists may become one illustrated page that
  quotes key lines; retellings and technical detail may be abridged, always marked with "…". Each volume
  has a `coverage.md` listing every verse as full / partial / omitted. About 140–160 words a page.

The first drafts (the "digest": short books of highlights, Genesis to 2 Samuel) are gone; the volumes replaced them.
The 154 digest pages whose drawings the volumes still lift are kept as reference art in `tools/full/reference/<series>/book-NN/`
(read by `reuse.panels()` and `<vol>.common.D(...)`, never published). Don't add to them: new drawings go in `<vol>/art.py`.

### Status

| Volume | Chapter | Bible chapters | Pages | Coverage | Folder |
|---|---|---|---|---|---|
| Genesis | 1 · In the Beginning (pilot) | 1–3 | cover + title + 16 | 80/80 verses full | `volumes/genesis/` |
| Genesis | 2 · Cain to the Flood | 4–9 | title + 24 (pp. 17–40) | 155/155 verses full | `volumes/genesis/` |
| Genesis | 3 · Babel to Abram's Covenant | 10–15 | title + 24 (pp. 41–64) | 147/147 verses full | `volumes/genesis/` |
| Genesis | 4 · The Cities of the Plain | 16–19 | title + 22 (pp. 65–86) | 114/114 verses full | `volumes/genesis/` |
| Genesis | 5 · The Son of Promise | 20–23 | title + 19 (pp. 87–105) | 96/96 verses full | `volumes/genesis/` |
| Genesis | 6 · A Wife for Isaac | 24:1–25:18 | title + 13 (pp. 106–118) | 75 full, 2 partial, 8 omitted (the retelling 24:38–47) | `volumes/genesis/` |
| Genesis | 7 · Jacob and Esau | 25:19–27:46 | title + 18 (pp. 119–136) | 97/97 verses full | `volumes/genesis/` |
| Genesis | 8 · The Ladder | 28–30 | title + 15 (pp. 137–151) | 100/100 verses full | `volumes/genesis/` |
| Genesis | 9 · Peniel | 31–33 | title + 18 (pp. 152–169) | 107/107 verses full | `volumes/genesis/` |
| Genesis | 10 · Bethel Again | 34–36 | title + 13 (pp. 170–182) | 103/103 verses full | `volumes/genesis/` |
| Genesis | 11 · The Dreamer | 37–38 | title + 14 (pp. 183–196) | 66/66 verses full | `volumes/genesis/` |
| Genesis | 12 · The Captain of the Guard | 39–40 | title + 9 (pp. 197–205) | 46/46 verses full | `volumes/genesis/` |
| Genesis | 13 · Pharaoh's Dreams | 41 | title + 10 (pp. 206–215) | 49 full, 2 partial, 6 omitted (the retelling 41:18–24) | `volumes/genesis/` |
| Genesis | 14 · The Brothers in Egypt | 42–43 | title + 13 (pp. 216–228) | 69 full, 1 partial, 3 omitted (the retelling 42:31–34) | `volumes/genesis/` |
| Genesis | 15 · I Am Joseph | 44–45 | title + 11 (pp. 229–239) | 62/62 verses full | `volumes/genesis/` |
| Genesis | 16 · Israel in Egypt | 46–47 | title + 11 (pp. 240–250) | 65/65 verses full | `volumes/genesis/` |
| Genesis | 17 · The Blessing of Jacob | 48–50 | title + 13 (pp. 251–263) | 81/81 verses full | `volumes/genesis/` |
| **Genesis** | **complete: cover + 17 chapters** | **1–50** | **281 pages (263 numbered)** | **1,533 verses: 1,512 full, 4 partial, 17 omitted (three abridged retellings)** | `volumes/genesis/` |
| Exodus | 1 · The Bush That Burned | 1–4 | cover + title + 20 (pp. 1–20) | 100/100 verses full | `volumes/exodus/` |
| Exodus | 2 · Let My People Go | 5–8 | title + 20 (pp. 21–40) | 110/110 verses full (6:14–25 as two scroll pages) | `volumes/exodus/` |
| Exodus | 3 · The Passover | 9–12 | title + 25 (pp. 41–65) | 125/125 verses full | `volumes/exodus/` |
| Exodus | 4 · The Red Sea | 13–15 | title + 16 (pp. 66–81) | 80/80 verses full (the Song of Moses in `kit.song` boxes) | `volumes/exodus/` |
| Exodus | 5 · Bread from Heaven | 16–18 | title + 18 (pp. 82–99) | 79/79 verses full | `volumes/exodus/` |
| Exodus | 6 · Sinai | 19–21 | title + 13 (pp. 100–112) | 87/87 verses full (the ordinances of ch. 21 as `kit.law` cells) | `volumes/exodus/` |
| Exodus | 7 · The Book of the Covenant | 22–24 | title + 10 (pp. 113–122) | 82/82 verses full (22:1–23:19 as five pages of law cells) | `volumes/exodus/` |
| Exodus | 8 · The Pattern of the Tabernacle | 25–27 | title + 13 (pp. 123–135) | 98/98 verses full (blueprint pages, `exo/art8.py`) | `volumes/exodus/` |
| Exodus | 9 · Holy to Jehovah | 28–31 | title + 20 (pp. 136–155) | 145/145 verses full (blueprints laid out by `ch09.pack()`) | `volumes/exodus/` |
| Exodus | 10 · The Golden Calf | 32–34 | title + 19 (pp. 156–174) | 93/93 verses full (32:27–28 caption-only over an empty gate) | `volumes/exodus/` |
| Exodus | 11 · The Willing Offering | 35–38 | title + 20 (pp. 175–194) | 133/133 verses full (the making set in full as blueprints) | `volumes/exodus/` |
| Exodus | 12 · The Glory | 39–40 | title + 12 (pp. 195–206) | 81/81 verses full | `volumes/exodus/` |
| **Exodus** | **complete: cover + 12 chapters** | **1–40** | **219 pages (206 numbered)** | **1,213 verses: all full** | `volumes/exodus/` |
| Leviticus | 1 · The Offerings | 1–5 | cover + title + 14 (pp. 1–14) | 104/104 verses full | `volumes/leviticus/` |
| Leviticus | 2 · The Consecration | 6–8 | title + 16 (pp. 15–30) | 104/104 verses full (ch. 8 as narrated blueprints) | `volumes/leviticus/` |
| Leviticus | 3 · Strange Fire | 9–11 | title + 14 (pp. 31–44) | 91/91 verses full (10:1–5 shown with restraint) | `volumes/leviticus/` |
| Leviticus | 4 · The Plague of Leprosy | 12–13 | title + 9 (pp. 45–53) | 67/67 verses full (skin signs as inspection-lens diagrams) | `volumes/leviticus/` |
| Leviticus | 5 · The Cleansing | 14–15 | title + 11 (pp. 54–64) | 90/90 verses full (issues drawn only as household things) | `volumes/leviticus/` |
| Leviticus | 6 · The Day of Atonement | 16–18 | title + 14 (pp. 65–78) | 80/80 verses full (ch. 18 as kinship charts only) | `volumes/leviticus/` |
| Leviticus | 7 · Holy unto Jehovah | 19–22 | title + 16 (pp. 79–94) | 121/121 verses full (ch. 20's penalties as charts under a red bar) | `volumes/leviticus/` |
| Leviticus | 8 · The Set Feasts | 23–25 | title + 15 (pp. 95–109) | 122/122 verses full (24:23 caption-only over a heap of stones) | `volumes/leviticus/` |
| Leviticus | 9 · Blessing and Curse | 26–27 | title + 9 (pp. 110–118) | 80/80 verses full | `volumes/leviticus/` |
| **Leviticus** | **complete: cover + 9 chapters** | **1–27** | **128 pages (118 numbered)** | **859 verses: all full** | `volumes/leviticus/` |
| Numbers | 1 · The Numbering | 1–2 | cover + title + 10 (pp. 1–10) | 88/88 verses full (census as tally cells, the camp as a blueprint plan) | `volumes/numbers/` |
| Numbers | 2 · The Charge of the Levites | 3–4 | title + 20 (pp. 11–30) | 100/100 verses full (the holy things wrapped, as blueprint plates) | `volumes/numbers/` |
| Numbers | 3 · Jehovah Bless Thee | 5–6 | title + 10 (pp. 31–40) | 58/58 verses full (jealousy and the Nazirite as law cells; 5:11–31 with restraint) | `volumes/numbers/` |
| Numbers | 4 · The Offerings of the Princes | 7–8 | title + 14 (pp. 41–54) | 115/115 verses full (one day a panel, each over a strip of the oblation) | `volumes/numbers/` |
| Numbers | 5 · The Cloud and the Trumpets | 9–10 | title + 12 (pp. 55–66) | 59/59 verses full (the order of march as a plan) | `volumes/numbers/` |
| Numbers | 6 · Graves of Lust | 11–12 | title + 16 (pp. 67–82) | 51/51 verses full (11:33 as the graves only) | `volumes/numbers/` |
| Numbers | 7 · The Twelve Spies | 13–14 | title + 17 (pp. 83–99) | 78/78 verses full (lifts eleven digest panels; 14:37, 14:45 as landscape) | `volumes/numbers/` |
| Numbers | 8 · Korah | 15–17 | title + 19 (pp. 100–118) | 104/104 verses full (16:31–35 as tents and censers; 15:36 as the heap) | `volumes/numbers/` |
| Numbers | 9 · The Water for Impurity | 18–19 | title + 8 (pp. 119–126) | 54/54 verses full (all law cells) | `volumes/numbers/` |
| Numbers | 10 · Meribah and the Serpent of Brass | 20–21 | title + 14 (pp. 127–140) | 64/64 verses full (lifts seven digest panels; the songs in song boxes) | `volumes/numbers/` |
| Numbers | 11 · Balaam | 22–24 | title + 19 (pp. 141–159) | 96/96 verses full (lifts eight digest panels; the parables in song boxes) | `volumes/numbers/` |
| Numbers | 12 · Phinehas | 25–26 | title + 9 (pp. 160–168) | 83/83 verses full (25:4–8 with restraint; the second census as tally cells) | `volumes/numbers/` |
| Numbers | 13 · The Daughters of Zelophehad | 27–29 | title + 13 (pp. 169–181) | 94/94 verses full (the feasts as law cells with the beasts counted) | `volumes/numbers/` |
| Numbers | 14 · Vows and the War with Midian | 30–31 | title + 9 (pp. 182–190) | 70/70 verses full (vows as law cells; the war told with restraint; the spoil as a chart) | `volumes/numbers/` |
| Numbers | 15 · The Journeys | 32–33 | title + 12 (pp. 191–202) | 98/98 verses full (the 42 stations as a lit route map over station cells) | `volumes/numbers/` |
| Numbers | 16 · The Borders of the Land | 34–36 | title + 11 (pp. 203–213) | 76/76 verses full (the borders as a map; refuge as law cells) | `volumes/numbers/` |
| **Numbers** | **complete: cover + 16 chapters** | **1–36** | **230 pages (213 numbered)** | **1,288 verses: all full** | `volumes/numbers/` |
| Deuteronomy | 1 · These Are the Words | 1–2 | cover + title + 15 (pp. 1–15) | 83/83 verses full (speech panels: `speech.orate`) | `volumes/deuteronomy/` |
| Deuteronomy | 2 · Take Heed to Thyself | 3–4 | title + 14 (pp. 16–29) | 78/78 verses full | `volumes/deuteronomy/` |
| Deuteronomy | 3 · Hear, O Israel | 5–6 | title + 10 (pp. 30–39) | 58/58 verses full (laid out by `discourse.pack`) | `volumes/deuteronomy/` |
| Deuteronomy | 4 · A People for His Own Possession | 7–8 | title + 8 (pp. 40–47) | 46/46 verses full | `volumes/deuteronomy/` |
| Deuteronomy | 5 · The Tables of Stone | 9–10 | title + 9 (pp. 48–56) | 51/51 verses full | `volumes/deuteronomy/` |
| Deuteronomy | 6 · The Place of His Name | 11–12 | title + 11 (pp. 57–67) | 64/64 verses full (the statutes as spoken law cells, `picto.pick`) | `volumes/deuteronomy/` |
| Deuteronomy | 7 · The Year of Release | 13–15 | title + 9 | 75/75 verses full (law cells) | `volumes/deuteronomy/` |
| Deuteronomy | 8 · Justice, Only Justice | 16–18 | title + 9 | 64/64 verses full (law cells) | `volumes/deuteronomy/` |
| Deuteronomy | 9 · When Thou Goest Forth to Battle | 19–21 | title + 9 | 64/64 verses full (law cells) | `volumes/deuteronomy/` |
| Deuteronomy | 10 · Thou Shalt Not | 22–23 | title + 8 | 55/55 verses full (law cells) | `volumes/deuteronomy/` |
| Deuteronomy | 11 · The Basket of First-fruits | 24–26 | title + 9 | 60/60 verses full (law cells) | `volumes/deuteronomy/` |
| Deuteronomy | 12 · The Blessings and the Curses | 27–28 | title + 14 | 94/94 verses full (the twelve curses as law cells; the siege words only) | `volumes/deuteronomy/` |
| Deuteronomy | 13 · Choose Life | 29–31 | title + 13 | 79/79 verses full | `volumes/deuteronomy/` |
| Deuteronomy | 14 · The Song of Moses | 32 | title + 10 | 52/52 verses full (the song in song boxes) | `volumes/deuteronomy/` |
| Deuteronomy | 15 · The Death of Moses | 33–34 | title + 11 | 41/41 verses full (the tribes as cells; Moses' death caption only, no grave drawn) | `volumes/deuteronomy/` |
| Joshua | 1 · Be Strong and of Good Courage | 1–2 | cover + title + 8 (pp. 1–8) | 42/42 verses full (lifts the digest's Jericho art: `reuse.fill`) | `volumes/joshua/` |
| Joshua | 2 · The Waters of the Jordan | 3–5 | title + 10 (pp. 9–18) | 56/56 verses full (5:2–8 as the flint knives and the camp only) | `volumes/joshua/` |
| Joshua | 3 · The Walls of Jericho | 6–7 | title + 10 (pp. 19–28) | 53/53 verses full (6:21 and 7:25 words only, over the dust and the heap) | `volumes/joshua/` |
| Joshua | 4 · Ai and the Gibeonites | 8–9 | title + 11 (pp. 29–39) | 62/62 verses full (the ambush as a map; 8:21–29 words over the smoke and the heap) | `volumes/joshua/` |
| Joshua | 5 · The Sun Stood Still | 10–11 | title + 11 (pp. 40–50) | 66/66 verses full (the southern campaign as a map; 10:24–27 words over the sealed cave) | `volumes/joshua/` |
| Joshua | 6 · The Land That Remaineth | 12–14 | title + 8 (pp. 51–58) | 72/72 verses full (the kings and the lands beyond the Jordan as roll pages: `rolls.py`) | `volumes/joshua/` |
| Joshua | 7 · The Lot of Judah | 15–17 | title + 8 (pp. 59–66) | 91/91 verses full (borders and cities as roll cells: `rolls.verse_cells`) | `volumes/joshua/` |
| Joshua | 8 · The Lots of the Seven Tribes | 18–19 | title + 7 (pp. 67–73) | 79/79 verses full (the seven lots as roll cells) | `volumes/joshua/` |
| Joshua | 9 · The Cities of Refuge | 20–22 | title + 11 (pp. 74–84) | 88/88 verses full (the Levites' cities as roll cells) | `volumes/joshua/` |
| Joshua | 10 · Choose You This Day | 23–24 | title + 8 (pp. 85–92) | 49/49 verses full (Joshua's death caption only, no grave drawn) | `volumes/joshua/` |
| Judges | 1 · After the Death of Joshua | 1–2 | cover + title + 11 (pp. 1–11) | 59/59 verses full (1:6–7 over an empty table; the round of the judges as a diagram) | `volumes/judges/` |
| Judges | 2 · Deborah | 3–5 | title + 16 (pp. 12–27) | 86/86 verses full (Eglon behind locked doors; the Song of Deborah in song boxes) | `volumes/judges/` |
| Judges | 3 · Gideon | 6–7 | title + 15 (pp. 28–42) | 65/65 verses full (the digest's Gideon panels; 7:25 words only) | `volumes/judges/` |
| Judges | 4 · Abimelech | 8–9 | title + 17 (pp. 43–59) | 92/92 verses full (9:5 and 9:53–54 words only; Jotham's fable over the four trees) | `volumes/judges/` |
| Judges | 5 · Jephthah | 10–12 | title + 15 (pp. 60–74) | 73/73 verses full (11:39 words over the mountains; Jephthah's message over the map of the way round) | `volumes/judges/` |
| Judges | 6 · Samson | 13–15 | title + 14 (pp. 75–88) | 65/65 verses full (the digest's Samson panels; 15:6 and the slaughters words only) | `volumes/judges/` |
| Judges | 7 · Delilah | 16 | title + 9 (pp. 89–97) | 31/31 verses full (16:1 and 16:21 words only; the digest's Delilah and pillars panels) | `volumes/judges/` |
| Judges | 8 · Micah and the Danites | 17–18 | title + 8 (pp. 98–105) | 44/44 verses full (18:27 words over the smoke) | `volumes/judges/` |
| Judges | 9 · Gibeah | 19 | title + 7 (pp. 106–112) | 30/30 verses full (19:22–30 words over a shut door, the dawn and a figure of twelve routes: no one drawn) | `volumes/judges/` |
| Judges | 10 · No King in Israel | 20–21 | title + 14 (pp. 113–126) | 73/73 verses full (the third day as a map; Jabesh-gilead words over smoke) | `volumes/judges/` |
| Ruth | 1 · Whither Thou Goest | 1–2 | cover + title + 10 (pp. 1–10) | 45/45 verses full (the digest's Ruth panels throughout) | `volumes/ruth/` |
| Ruth | 2 · The Near Kinsman | 3–4 | title + 9 (pp. 11–19) | 40/40 verses full (the generations of Perez as a roll page) | `volumes/ruth/` |
| 1 Samuel | 1 · Hannah | 1–2 | cover + title + 14 (pp. 1–14) | 64/64 verses full (Hannah's song in song boxes) | `volumes/1samuel/` |
| 1 Samuel | 2 · Speak, Jehovah | 3–5 | title + 14 (pp. 15–28) | 55/55 verses full (Eli's death as the empty gate; the ark's travels as a map) | `volumes/1samuel/` |
| 1 Samuel | 3 · Give Us a King | 6–8 | title + 11 (pp. 29–39) | 60/60 verses full (the digest's kine; 6:19 words only) | `volumes/1samuel/` |
| 1 Samuel | 4 · Saul Anointed | 9–10 | title + 14 (pp. 40–53) | 54/54 verses full | `volumes/1samuel/` |
| 1 Samuel | 5 · To Obey Is Better | 11–13 | title + 13 (pp. 54–66) | 63/63 verses full (11:2 and 11:7 words only) | `volumes/1samuel/` |
| 1 Samuel | 6 · Jonathan at Michmash | 14 | title + 13 (pp. 67–79) | 52/52 verses full (the crags as drawings; Saul's wars as a map) | `volumes/1samuel/` |
| 1 Samuel | 7 · Jehovah Looketh on the Heart | 15–16 | title + 14 (pp. 80–93) | 58/58 verses full (15:33 words only; the digest's anointing panels) | `volumes/1samuel/` |
| 1 Samuel | 8 · Goliath | 17 | title + 14 (pp. 94–107) | 58/58 verses full (the digest's David and Goliath book; 17:51, 17:54, 17:57 words only) | `volumes/1samuel/` |
| 1 Samuel | 9 · Saul Hath Slain His Thousands | 18–19 | title + 10 (pp. 108–117) | 54/54 verses full (18:25–27 and 19:24 words only) | `volumes/1samuel/` |
| 1 Samuel | 10 · Jonathan and David | 20–21 | title + 12 (pp. 118–129) | 57/57 verses full | `volumes/1samuel/` |
| 1 Samuel | 11 · The Cave | 22–24 | title + 15 (pp. 130–144) | 74/74 verses full (22:17–19 words over Nob's smoke) | `volumes/1samuel/` |
| 1 Samuel | 12 · Abigail | 25–26 | title + 14 (pp. 145–158) | 69/69 verses full (25:38 words only) | `volumes/1samuel/` |
| 1 Samuel | 13 · The Witch of En-dor | 27–29 | title + 11 (pp. 159–169) | 48/48 verses full (Samuel's shade a pale shape, no face; 27:9 and 27:11 words only) | `volumes/1samuel/` |
| 1 Samuel | 14 · Mount Gilboa | 30–31 | title + 9 (pp. 170–178) | 44/44 verses full (Saul's death over the crown and spear; 31:8–10 over smoke) | `volumes/1samuel/` |
| 2 Samuel | 1 · How Are the Mighty Fallen | 1–2 | cover + title + 13 (pp. 1–13) | 59/59 verses full (the song of the bow in song boxes; 1:15, 2:16 and 2:23 words only) | `volumes/2samuel/` |
| 2 Samuel | 2 · Abner | 3–4 | title + 11 (pp. 14–24) | 51/51 verses full (3:27, 4:5–7 and 4:12 words over the empty gate, the house at noon and the pool) | `volumes/2samuel/` |
| 2 Samuel | 3 · The City of David | 5–6 | title + 10 (pp. 25–34) | 48/48 verses full (the digest's anointing, ark and dancing panels; 6:7 words over the cart at Nacon) | `volumes/2samuel/` |
| 2 Samuel | 4 · For Ever | 7–8 | title + 9 (pp. 35–43) | 47/47 verses full (Nathan's oracle in the Voice box; David's wars as a map, 8:2 words only) | `volumes/2samuel/` |
| 2 Samuel | 5 · Mephibosheth | 9–10 | title + 9 (pp. 44–52) | 32/32 verses full (the digest's Mephibosheth page; Rabbah's gate as a map) | `volumes/2samuel/` |
| 2 Samuel | 6 · Thou Art the Man | 11–12 | title + 12 (pp. 53–64) | 58/58 verses full (11:2–4 over the digest's empty roof; Uriah's death as the distant wall; 12:31 words only) | `volumes/2samuel/` |
| 2 Samuel | 7 · Absalom | 13–14 | title + 17 (pp. 65–81) | 72/72 verses full (13:11–14 words over the chamber and the shut door; 13:28–29 over the empty feast) | `volumes/2samuel/` |
| 2 Samuel | 8 · The Mount of Olives | 15–16 | title + 15 (pp. 82–96) | 60/60 verses full (the digest's gate, Kidron and Olives panels; 16:22 words over a tent on the roof) | `volumes/2samuel/` |
| 2 Samuel | 9 · O My Son Absalom | 17–18 | title + 17 (pp. 97–113) | 62/62 verses full (the digest's oak and heap; 17:23 and 18:14–15 words only) | `volumes/2samuel/` |
| 2 Samuel | 10 · The King Returned | 19–20 | title + 16 (pp. 114–129) | 69/69 verses full (20:10–12 words over the empty highway; 20:22 over Abel's wall) | `volumes/2samuel/` |
| 2 Samuel | 11 · Jehovah Is My Rock | 21–22 | title + 15 (pp. 130–144) | 73/73 verses full (21:9 words over the mountain at harvest; David's song in song boxes) | `volumes/2samuel/` |
| 2 Samuel | 12 · Which Cost Me Nothing | 23–24 | title + 11 (pp. 145–155) | 64/64 verses full (the mighty men as roll cells; 24:15 words over the silent tents) | `volumes/2samuel/` |
| 1 Kings | 1 · Long Live King Solomon | 1 | cover + title + 11 (pp. 1–11) | 53/53 verses full (no digest book: all new drawings, `kg1/art.py`) | `volumes/1kings/` |
| 1 Kings | 2 · Show Thyself a Man | 2 | title + 10 (pp. 12–21) | 46/46 verses full (2:25, 2:34 and 2:46 words over the altar alone and the road) | `volumes/1kings/` |
| 1 Kings | 3 · An Understanding Heart | 3–4 | title + 11 (pp. 22–32) | 62/62 verses full (the officers as roll cells; the sword held, never used) | `volumes/1kings/` |
| 1 Kings | 4 · The House of Jehovah | 5–6 | title + 9 (pp. 33–41) | 56/56 verses full (the house as blueprint plates, `kg1.art.temple_plan` …) | `volumes/1kings/` |
| 1 Kings | 5 · The Pillars and the Sea | 7 | title + 9 (pp. 42–50) | 51/51 verses full (Solomon's houses, Jachin and Boaz, the sea and the bases as blueprint plates) | `volumes/1kings/` |
| 1 Kings | 6 · The Glory of Jehovah | 8 | title + 14 (pp. 51–64) | 66/66 verses full (Solomon's prayer as speech panels) | `volumes/1kings/` |
| 1 Kings | 7 · The Queen of Sheba | 9–10 | title + 10 (pp. 65–74) | 57/57 verses full (the levy's cities as a map; the throne of ivory as a blueprint) | `volumes/1kings/` |
| 1 Kings | 8 · His Heart Turned Away | 11 | title + 7 (pp. 75–81) | 43/43 verses full (Ahijah's twelve pieces; the rent kingdom as a map of the tribes) | `volumes/1kings/` |
| 1 Kings | 9 · To Your Tents, O Israel | 12–13 | title + 14 (pp. 82–95) | 67/67 verses full (12:18 and 13:24–28 words only: the ass and the lion standing, no body drawn) | `volumes/1kings/` |
| 1 Kings | 10 · Ahijah's Word | 14–15 | title + 8 (pp. 96–103) | 65/65 verses full (the reigns as roll cells, Judah gold and Israel red: `kg1.common.reign`) | `volumes/1kings/` |
| 1 Kings | 11 · Elijah | 16–17 | title + 10 (pp. 104–113) | 58/58 verses full (16:18 over Tirzah burning; Elijah in his hairy mantle, `kg1.art.elijah_fig`) | `volumes/1kings/` |
| 1 Kings | 12 · The Fire of Jehovah | 18 | title + 12 (pp. 114–125) | 46/46 verses full (18:28 over dark figures about the altar; 18:40 over the empty brook Kishon) | `volumes/1kings/` |
| 1 Kings | 13 · A Still Small Voice | 19–20 | title + 18 (pp. 126–143) | 64/64 verses full (Horeb: wind, earthquake, fire and the still small voice, God never drawn; Aphek as a map) | `volumes/1kings/` |
| 1 Kings | 14 · Naboth's Vineyard | 21–22 | title + 23 (pp. 144–166) | 82/82 verses full (21:13 and 22:34–38 words over the vineyard at dusk, the chariot at sunset and the empty pool) | `volumes/1kings/` |
| 2 Kings | 1 · The Chariot of Fire | 1–2 | cover + title + 14 (pp. 1–14) | 43/43 verses full (1:10–12 words over fire on the slope; 2:24 over the empty way) | `volumes/2kings/` |
| 2 Kings | 2 · The Pot of Oil | 3–4 | title + 19 (pp. 15–33) | 71/71 verses full (3:27 words over Kir-hareseth's wall and smoke) | `volumes/2kings/` |
| 2 Kings | 3 · Naaman | 5–6 | title + 18 (pp. 34–51) | 60/60 verses full (6:28–29 words over Samaria's wall, nothing drawn) | `volumes/2kings/` |
| 2 Kings | 4 · The Siege of Samaria | 7–8 | title + 10 (pp. 52–61) | 49/49 verses full (7:17–20 and 8:15 words only; `rolls.roll_pages(..., end=)` closes a chapter on a roll page) | `volumes/2kings/` |
| 2 Kings | 5 · Jehu | 9–10 | title + 17 (pp. 62–78) | 73/73 verses full (9:24–37, 10:7–8 and 10:25 words over the field, the empty window, the gate and the broken house) | `volumes/2kings/` |
| 2 Kings | 6 · Joash | 11–12 | title + 9 (pp. 79–87) | 42/42 verses full (11:16 and 12:20–21 words over the horses' entry and Millo, empty) | `volumes/2kings/` |
| 2 Kings | 7 · The Bones of Elisha | 13–14 | title + 9 (pp. 88–96) | 54/54 verses full (the reigns as roll cells; Jeroboam's border as a map) | `volumes/2kings/` |
| 2 Kings | 8 · Ahaz | 15–16 | title + 7 (pp. 97–103) | 58/58 verses full (ch. 15 as roll cells; Assyria as a map; the Damascus altar as a blueprint) | `volumes/2kings/` |
| 2 Kings | 9 · Carried Away into Assyria | 17 | title + 7 (pp. 104–110) | 41/41 verses full (the exile and the settlers as maps; 17:17 and 17:31 words only) | `volumes/2kings/` |
| 2 Kings | 10 · Hezekiah | 18–19 | title + 13 (pp. 111–123) | 74/74 verses full (19:35 over the silent camp, 19:37 over Nineveh; God never drawn) | `volumes/2kings/` |
| 2 Kings | 11 · The Shadow on the Dial | 20–21 | title + 8 (pp. 124–131) | 47/47 verses full (the dial of Ahaz; the line of Samaria as a blueprint; 21:16 words only) | `volumes/2kings/` |
| 2 Kings | 12 · Josiah | 22–23 | title + 14 (pp. 132–145) | 57/57 verses full (23:20 and 23:29 words only) | `volumes/2kings/` |
| 2 Kings | 13 · The Fall of Jerusalem | 24–25 | title + 10 (pp. 146–155) | 50/50 verses full (25:7, 25:21 and 25:25 words only; the city burning with no one drawn) | `volumes/2kings/` |
| 1 Chronicles | 1 · From Adam | 1–2 | cover + title + 9 (pp. 1–9) | 109/109 verses full (lineage charts, `chr1.art.lineage`/`branch`, over roll cells) | `volumes/1chronicles/` |
| 1 Chronicles | 2 · The Sons of David | 3–4 | title + 8 (pp. 10–17) | 67/67 verses full (Jabez as faces and a survey plan; 4:41 words over smoke) | `volumes/1chronicles/` |
| 1 Chronicles | 3 · The Sons of Levi | 5–6 | title + 10 (pp. 18–27) | 107/107 verses full (the Hagrites as a map; the high priests and the singers as lineage charts) | `volumes/1chronicles/` |
| 1 Chronicles | 4 · They That Dwelt in Jerusalem | 7–9 | title + 12 (pp. 27–38) | 124/124 verses full (7:21 words over the gate; the porters on four sides as a blueprint) | `volumes/1chronicles/` |
| 1 Chronicles | 5 · David King over Israel | 10–12 | title + 13 (pp. 38–50) | 101/101 verses full (the digest Gilboa and Hebron panels; 10:4–6 and 10:9–10 words over the crown, spear and burning city) | `volumes/1chronicles/` |
| 1 Chronicles | 6 · The Ark of God | 13–16 | title + 16 (pp. 51–66) | 103/103 verses full (13:10 words over the cart; the digest ark and dancing panels; the psalm of thanks in song boxes) | `volumes/1chronicles/` |
| 1 Chronicles | 7 · Thy Throne for Ever | 17–20 | title + 13 (pp. 66–78) | 71/71 verses full (Nathan's oracle in the Voice box; David's wars as maps; 20:3 words over Rabbah at dusk) | `volumes/1chronicles/` |
| 1 Chronicles | 8 · The Threshing-floor of Ornan | 21–22 | title + 9 (pp. 79–87) | 49/49 verses full (21:14 words over the silent tents; the answer by fire; the stores for the house) | `volumes/1chronicles/` |
| 1 Chronicles | 9 · The Courses | 23–25 | title + 9 (pp. 88–96) | 94/94 verses full (the Levites as a tally board; the twenty-four courses of priests and singers as boards of lots) | `volumes/1chronicles/` |
| 1 Chronicles | 10 · The Porters and the Captains | 26–27 | title + 8 (pp. 97–104) | 66/66 verses full (the gates as a plan with their wards; the twelve captains as a calendar wheel) | `volumes/1chronicles/` |
| 1 Chronicles | 11 · Thine Is the Kingdom | 28–29 | title + 11 (pp. 105–115) | 51/51 verses full (the pattern as 1 Kings' blueprints; David's death words only, over the crown laid down) | `volumes/1chronicles/` |
| **1 Chronicles** | **complete: cover + 11 chapters** | **1–29** | **127 pages (115 numbered)** | **942 verses: all full** | `volumes/1chronicles/` |
| 2 Chronicles | 1 · Wisdom and Knowledge | 1–4 | cover + title + 12 (pp. 1–12) | 74/74 verses full (the house as 1 Kings' blueprints) | `volumes/2chronicles/` |
| 2 Chronicles | 2 · The Glory Filled the House | 5–7 | title + 16 (pp. 13–28) | 78/78 verses full (Solomon's prayer in full as speech panels; God's answer in the Voice box) | `volumes/2chronicles/` |
| 2 Chronicles | 3 · The Queen of Sheba | 8–9 | title + 9 (pp. 29–37) | 49/49 verses full (the cities as a map; the throne of ivory as a blueprint) | `volumes/2chronicles/` |
| 2 Chronicles | 4 · Rehoboam | 10–12 | title + 11 (pp. 38–48) | 58/58 verses full (10:18 words only; the cities for defence as a map) | `volumes/2chronicles/` |
| 2 Chronicles | 5 · Abijah and Asa | 13–16 | title + 13 (pp. 49–61) | 70/70 verses full (Abijah's battle and Zerah's host as maps; 13:17 words only) | `volumes/2chronicles/` |
| 2 Chronicles | 6 · Jehoshaphat | 17–19 | title + 18 (pp. 62–79) | 64/64 verses full (Micaiah before the two kings; 18:33–34 words over the chariot at sunset) | `volumes/2chronicles/` |
| 2 Chronicles | 7 · The Battle Is Not Yours | 20–21 | title + 11 (pp. 79–89) | 57/57 verses full (20:22–25 words over the strewn valley; 21:4 and 21:18–19 words only) | `volumes/2chronicles/` |
| 2 Chronicles | 8 · Joash | 22–24 | title + 13 (pp. 90–102) | 60/60 verses full (23:15, 24:21 and 24:25 words over the horses' entry, the empty court and the city) | `volumes/2chronicles/` |
| 2 Chronicles | 9 · Amaziah and Uzziah | 25–27 | title + 11 (pp. 103–113) | 60/60 verses full (25:12 words over the empty rock; Uzziah's leprosy as his face in pale light) | `volumes/2chronicles/` |
| 2 Chronicles | 10 · Ahaz and Hezekiah | 28–29 | title + 12 (pp. 114–125) | 63/63 verses full (28:3 words only; the captives clothed and led to Jericho) | `volumes/2chronicles/` |
| 2 Chronicles | 11 · The Passover of Hezekiah | 30–31 | title + 8 (pp. 126–133) | 48/48 verses full (the posts with the letters as a map; the heaps of the tithes) | `volumes/2chronicles/` |
| 2 Chronicles | 12 · Sennacherib | 32 | title + 7 (pp. 134–140) | 33/33 verses full (the springs stopped and Gihon as plans; 32:21 words over the silent camp) | `volumes/2chronicles/` |
| 2 Chronicles | 13 · Manasseh and Josiah | 33–34 | title + 11 (pp. 141–151) | 58/58 verses full (33:6 and 33:24 words only; Manasseh in chains and humbled; the outer wall as a plan) | `volumes/2chronicles/` |
| 2 Chronicles | 14 · The Seventy Years | 35–36 | title + 8 (pp. 152–159) | 50/50 verses full (35:23–24 and 36:17–19 words over the chariot and the burning city; the decree of Cyrus) | `volumes/2chronicles/` |
| **2 Chronicles** | **complete: cover + 14 chapters** | **1–36** | **174 pages (159 numbered)** | **822 verses: all full** | `volumes/2chronicles/` |
| Ezra | 1 · The Decree of Cyrus | 1–2 | cover + title + 8 (pp. 1–8) | 81/81 verses full (the vessels and the assembly as tally boards; the families of the return as roll cells) | `volumes/ezra/` |
| Ezra | 2 · The Foundation of the House | 3–4 | title + 6 (pp. 9–14) | 37/37 verses full (the letters beyond the River as sealed scrolls, their words in speech boxes) | `volumes/ezra/` |
| Ezra | 3 · The House Finished | 5–6 | title + 6 (pp. 15–20) | 39/39 verses full (the roll at Achmetha and the measures of the house as a plan; 6:11 words only) | `volumes/ezra/` |
| Ezra | 4 · Ezra the Scribe | 7–8 | title + 9 (pp. 21–29) | 64/64 verses full (Ezra's line to Aaron as a chart; the silver and gold weighed on a great balance) | `volumes/ezra/` |
| Ezra | 5 · The Strange Wives | 9–10 | title + 8 (pp. 30–37) | 59/59 verses full (Ezra's prayer on his knees; the people trembling in the rain; the names as roll cells) | `volumes/ezra/` |
| **Ezra** | **complete: cover + 5 chapters** | **1–10** | **43 pages (37 numbered)** | **280 verses: all full** | `volumes/ezra/` |
| Nehemiah | 1 · The Wall of Jerusalem | 1–2 | cover + title + 8 (pp. 1–8) | 31/31 verses full (God's word to Moses in 1:8–9 in the Voice box; the night ride as a plan of the wall) | `volumes/nehemiah/` |
| Nehemiah | 2 · The Builders | 3–4 | title + 12 (pp. 9–20) | 55/55 verses full (ch. 3 as roll cells under the plan of the wall, its stretch lit page by page: `neh.common.plan_pages`) | `volumes/nehemiah/` |
| Nehemiah | 3 · The Work Finished | 5–6 | title + 8 (pp. 21–28) | 38/38 verses full (the plain of Ono as a map; the governor's table as a tally board) | `volumes/nehemiah/` |
| Nehemiah | 4 · The Genealogy of the Return | 7 | title + 8 (pp. 29–36) | 73/73 verses full (the register as bar charts and tally boards over roll cells) | `volumes/nehemiah/` |
| Nehemiah | 5 · The Book of the Law | 8–9 | title + 13 (pp. 37–49) | 56/56 verses full (Ezra on the pulpit of wood; the Levites' prayer drawn over the history it tells) | `volumes/nehemiah/` |
| Nehemiah | 6 · The Sealed Covenant | 10–11 | title + 8 (pp. 50–57) | 75/75 verses full (they that sealed and they that dwelt as roll cells; the villages as a map) | `volumes/nehemiah/` |
| Nehemiah | 7 · The Dedication of the Wall | 12–13 | title + 12 (pp. 58–69) | 78/78 verses full (the two companies on the plan of the wall; 13:25 words only over the shut gate) | `volumes/nehemiah/` |
| **Nehemiah** | **complete: cover + 7 chapters** | **1–13** | **77 pages (69 numbered)** | **406 verses: all full** | `volumes/nehemiah/` |
| Esther | 1 · Vashti and Esther | 1–2 | cover + title + 9 (pp. 1–9) | 45/45 verses full (all new drawings, `est/art.py`; 2:23 words over the threshold and the book of the chronicles) | `volumes/esther/` |
| Esther | 2 · For Such a Time as This | 3–4 | title + 7 (pp. 10–16) | 32/32 verses full (Pur as a wheel of the twelve months; Mordecai in sackcloth) | `volumes/esther/` |
| Esther | 3 · The King Could Not Sleep | 5–7 | title + 12 (pp. 17–28) | 38/38 verses full (the gallows only ever standing and empty; 7:10 words over the empty gallows far off at dusk) | `volumes/esther/` |
| Esther | 4 · The Days of Purim | 8–10 | title + 10 (pp. 29–38) | 52/52 verses full (9:1–16 words only, over the map of the provinces and Shushan at dusk; the days of Adar as a chart) | `volumes/esther/` |
| **Esther** | **complete: cover + 4 chapters** | **1–10** | **43 pages (38 numbered)** | **167 verses: all full** | `volumes/esther/` |
| Job | 1 · The Land of Uz | 1–3 | cover + title + 11 (pp. 1–11) | 61/61 verses full (Satan never drawn: words over the heavens, a dark streak at most; 1:15–19 words over the empty field; the boils as sackcloth, potsherd and ash heap) | `volumes/job/` |
| Job | 2 · The Vision of the Night | 4–7 | title + 12 (pp. 12–23) | 99/99 verses full (Eliphaz in teal song lines; the spirit a pale form with no face) | `volumes/job/` |
| Job | 3 · No Umpire Betwixt Us | 8–10 | title + 11 (pp. 24–34) | 79/79 verses full (the Bear, Orion and the Pleiades as a labelled night sky) | `volumes/job/` |
| Job | 4 · If a Man Die | 11–14 | title + 12 (pp. 35–46) | 95/95 verses full (the measures of the world as a technical section; the stump that sprouts again) | `volumes/job/` |
| Job | 5 · My Witness Is in Heaven | 15–17 | title + 9 (pp. 47–55) | 73/73 verses full (the mockers and archers with no blow drawn) | `volumes/job/` |
| Job | 6 · My Redeemer Liveth | 18–20 | title + 11 (pp. 56–66) | 79/79 verses full (19:25–27 over the dawn on the earth) | `volumes/job/` |
| Job | 7 · Where I Might Find Him | 21–24 | title + 13 (pp. 67–79) | 106/106 verses full (23:8–9 as a compass of four empty ways) | `volumes/job/` |
| Job | 8 · The Price of Wisdom | 25–28 | title + 10 (pp. 80–89) | 71/71 verses full (the mine in section; 28:25–26 as a blueprint plate) | `volumes/job/` |
| Job | 9 · The Months of Old | 29–31 | title + 13 (pp. 90–102) | 96/96 verses full (31:10 as the hand-mill alone) | `volumes/job/` |
| Job | 10 · Elihu | 32–37 | title + 21 (pp. 103–123) | 165/165 verses full (Elihu young in green; the storm of 36–37 ending in golden splendor) | `volumes/job/` |
| Job | 11 · Out of the Whirlwind | 38–39 | title + 8 (pp. 124–131) | 71/71 verses full (Jehovah in the Voice box over the whirlwind; the foundations as a blueprint; 39:30 words only) | `volumes/job/` |
| Job | 12 · Mine Eye Seeth Thee | 40–42 | title + 10 (pp. 132–141) | 75/75 verses full (behemoth as the river-horse, leviathan as the crocodile; the latter end as a tally board) | `volumes/job/` |
| **Job** | **complete: cover + 12 chapters** | **1–42** | **154 pages (141 numbered)** | **1,070 verses: all full** | `volumes/job/` |
| Psalms | 1 · Blessed Is the Man | 1–12 | cover + title + 21 (pp. 1–21) | 135/135 verses full (2:6–9 and 12:5 in the Voice box) | `volumes/psalms/` |
| Psalms | 2 · The Heavens Declare | 13–22 | title + 25 (pp. 22–46) | 161/161 verses full (Psalm 18's storm as cloud, hail and lightning) | `volumes/psalms/` |
| Psalms | 3 · Jehovah Is My Shepherd | 23–33 | title + 25 (pp. 47–71) | 153/153 verses full (Psalm 29's voice as storm, cedars and flood) | `volumes/psalms/` |
| Psalms | 4 · Wait for Jehovah | 34–41 | title + 26 (pp. 72–97) | 167/167 verses full | `volumes/psalms/` |
| Psalms | 5 · As the Hart Panteth | 42–50 | title + 22 (pp. 98–119) | 136/136 verses full (the sons of Korah as Levite singers) | `volumes/psalms/` |
| Psalms | 6 · A Clean Heart | 51–62 | title + 25 (pp. 120–144) | 148/148 verses full (60:6–8 in the Voice box over a map of the lands) | `volumes/psalms/` |
| Psalms | 7 · Let God Arise | 63–68 | title + 18 (pp. 145–162) | 96/96 verses full (68:21–23 words over the deep) | `volumes/psalms/` |
| Psalms | 8 · He Shall Have Dominion | 69–72 | title + 14 (pp. 163–176) | 85/85 verses full (Solomon for Psalm 72) | `volumes/psalms/` |
| Psalms | 9 · Whom Have I in Heaven | 73–78 | title + 27 (pp. 177–203) | 165/165 verses full (Asaph; Psalm 78's slain words over the empty camp) | `volumes/psalms/` |
| Psalms | 10 · How Amiable Are Thy Tabernacles | 79–89 | title + 32 (pp. 204–235) | 193/193 verses full (the confederate nations as a map; Heman and Ethan) | `volumes/psalms/` |
| Psalms | 11 · Our Dwelling-place | 90–100 | title + 23 (pp. 236–258) | 135/135 verses full (Moses' face for Psalm 90) | `volumes/psalms/` |
| Psalms | 12 · Bless Jehovah, O My Soul | 101–104 | title + 17 (pp. 259–275) | 93/93 verses full | `volumes/psalms/` |
| Psalms | 13 · He Remembered His Covenant | 105–106 | title + 17 (pp. 276–292) | 93/93 verses full (106:37–38 words over the idols and smoke) | `volumes/psalms/` |
| Psalms | 14 · They That Go Down to the Sea | 107–118 | title + 34 (pp. 293–326) | 199/199 verses full (110:1 and 110:4 in the Voice box) | `volumes/psalms/` |
| Psalms | 15 · Thy Word Is a Lamp | 119 | title + 27 (pp. 327–353) | 176/176 verses full (22 sections under their letter heads) | `volumes/psalms/` |
| Psalms | 16 · I Will Lift Up Mine Eyes | 120–137 | title + 28 (pp. 354–381) | 157/157 verses full (the Songs of Ascents; 137:7–9 words over the ruins) | `volumes/psalms/` |
| Psalms | 17 · Praise Ye Jehovah | 138–150 | title + 29 (pp. 382–410) | 169/169 verses full (Psalm 150 on its own last page) | `volumes/psalms/` |
| **Psalms** | **complete: cover + 17 chapters** | **1–150** | **428 pages (410 numbered)** | **2,461 verses: all full** | `volumes/psalms/` |
| Proverbs | 1 · The Beginning of Knowledge | 1–3 | cover + title + 12 (pp. 1–12) | 90/90 verses full (the father's words beside Solomon's face; Wisdom at the gate in white and gold light; the strange woman's house with no one drawn) | `volumes/proverbs/` |
| Proverbs | 2 · Get Wisdom | 4–6 | title + 12 (pp. 13–24) | 85/85 verses full (the strange woman never drawn, only a shut door at dusk; the ant; the six things, yea seven, as numbered signs) | `volumes/proverbs/` |
| Proverbs | 3 · Wisdom Hath Builded Her House | 7–9 | title + 12 (pp. 25–36) | 81/81 verses full (Proverbs 7 as the lattice, the street at twilight, a far veiled figure; the seven pillars) | `volumes/proverbs/` |
| Proverbs | 4 · A Wise Son | 10–12 | title + 12 (pp. 37–48) | 91/91 verses full (saying cells, one verse each under an emblem: `pro.common.sayings`) | `volumes/proverbs/` |
| Proverbs | 5 · A Tree of Life | 13–15 | title + 13 (pp. 49–61) | 93/93 verses full (saying cells; 13:12 a drawn cell) | `volumes/proverbs/` |
| Proverbs | 6 · The Lot Is Cast into the Lap | 16–18 | title + 11 (pp. 62–72) | 85/85 verses full (saying cells) | `volumes/proverbs/` |
| Proverbs | 7 · The King's Heart | 19–21 | title + 12 (pp. 73–84) | 90/90 verses full (saying cells; 21:1 the king among the watercourses) | `volumes/proverbs/` |
| Proverbs | 8 · The Words of the Wise | 22–24 | title + 11 (pp. 85–95) | 98/98 verses full (23:29–35 words over the red cup, no drunkard drawn; 24:30–34 the sluggard's field) | `volumes/proverbs/` |
| Proverbs | 9 · Apples of Gold | 25–27 | title + 10 (pp. 96–105) | 83/83 verses full (25:1 the men of Hezekiah at their scrolls) | `volumes/proverbs/` |
| Proverbs | 10 · Bold as a Lion | 28–29 | title + 8 (pp. 106–113) | 55/55 verses full (saying cells) | `volumes/proverbs/` |
| Proverbs | 11 · A Worthy Woman | 30–31 | title + 11 (pp. 114–124) | 64/64 verses full (Agur's numbered sayings as numbered signs; the worthy woman's household in song boxes) | `volumes/proverbs/` |
| **Proverbs** | **complete: cover + 11 chapters** | **1–31** | **136 pages (124 numbered)** | **915 verses: all full** | `volumes/proverbs/` |
| Ecclesiastes | 1 · Vanity of Vanities | 1–3 | cover + title + 15 (pp. 1–15) | 66/66 verses full (the sun's course, the wind's circuits and the rivers as diagrams; a time to every purpose as a ring of cells) | `volumes/ecclesiastes/` |
| Ecclesiastes | 2 · Two Are Better than One | 4–6 | title + 10 (pp. 16–25) | 48/48 verses full (the threefold cord as a blueprint) | `volumes/ecclesiastes/` |
| Ecclesiastes | 3 · A Good Name | 7–9 | title + 14 (pp. 26–39) | 64/64 verses full (one among a thousand as a grid of marks) | `volumes/ecclesiastes/` |
| Ecclesiastes | 4 · Remember Thy Creator | 10–12 | title + 10 (pp. 40–49) | 44/44 verses full (the silver cord and golden bowl as a plate of cells; 12:7 as dust and a light going up) | `volumes/ecclesiastes/` |
| **Ecclesiastes** | **complete: cover + 4 chapters** | **1–12** | **54 pages (49 numbered)** | **222 verses: all full** | `volumes/ecclesiastes/` |
| Song of Solomon | 1 · I Am a Rose of Sharon | 1–2 | cover + title + 8 (pp. 1–8) | 34/34 verses full (vineyards, the rose and the lily, roes, the winter past) | `volumes/songofsolomon/` |
| Song of Solomon | 2 · A Garden Shut Up | 3–5 | title + 12 (pp. 9–20) | 43/43 verses full (4:1–5 and 5:10–16 as plates of likeness cells only) | `volumes/songofsolomon/` |
| Song of Solomon | 3 · Love Is Strong as Death | 6–8 | title + 9 (pp. 21–29) | 40/40 verses full (7:1–9 as plates of cells only; 8:6–7 a flame over the floods) | `volumes/songofsolomon/` |
| **Song of Solomon** | **complete: cover + 3 chapters** | **1–8** | **33 pages (29 numbered)** | **117 verses: all full** | `volumes/songofsolomon/` |
| Isaiah | 1 · The Vineyard of Jehovah | 1–5 | cover + title + 20 (pp. 1–20) | 115/115 verses full (the vineyard, scarlet and snow, the ornaments of 3:18–23 as a plate) | `volumes/isaiah/` |
| Isaiah | 2 · Holy, Holy, Holy | 6–9 | title + 17 (pp. 21–37) | 81/81 verses full (the vision as light, smoke, an empty throne and six-winged seraphim, God never drawn) | `volumes/isaiah/` |
| Isaiah | 3 · The Root of Jesse | 10–12 | title + 10 (pp. 38–47) | 56/56 verses full (the march from Aiath to Nob as a map; the peaceable kingdom) | `volumes/isaiah/` |
| Isaiah | 4 · How Art Thou Fallen | 13–16 | title + 15 (pp. 48–62) | 77/77 verses full (13:15–16 and 14:19–21 words only; Moab as a map) | `volumes/isaiah/` |
| Isaiah | 5 · The Burden of Egypt | 17–20 | title + 12 (pp. 63–74) | 52/52 verses full (Isaiah's sign as sackcloth and sandals by the road) | `volumes/isaiah/` |
| Isaiah | 6 · Watchman, What of the Night? | 21–23 | title + 13 (pp. 75–87) | 60/60 verses full (the valley of vision as a plan; Tyre) | `volumes/isaiah/` |
| Isaiah | 7 · Thy Dead Shall Live | 24–27 | title + 13 (pp. 88–100) | 69/69 verses full (the feast on the mountain and the veil) | `volumes/isaiah/` |
| Isaiah | 8 · In Returning and Rest | 28–30 | title + 18 (pp. 101–118) | 86/86 verses full (the tried corner-stone and the threshing as plates) | `volumes/isaiah/` |
| Isaiah | 9 · The Desert Shall Blossom | 31–35 | title + 16 (pp. 119–134) | 80/80 verses full (34:2–7 words over Edom's mountains; the way of holiness) | `volumes/isaiah/` |
| Isaiah | 10 · On Whom Dost Thou Trust? | 36–39 | title + 19 (pp. 135–153) | 90/90 verses full (2 Kings' drawings and faces; 37:36–38 words over the silent camp) | `volumes/isaiah/` |
| Isaiah | 11 · Comfort Ye My People | 40–42 | title + 17 (pp. 154–170) | 85/85 verses full (the measures plate; one from the east as a map) | `volumes/isaiah/` |
| Isaiah | 12 · Ye Are My Witnesses | 43–45 | title + 14 (pp. 171–184) | 81/81 verses full (the idol's making as a plate; the doors of brass before Cyrus) | `volumes/isaiah/` |
| Isaiah | 13 · Go Ye Forth from Babylon | 46–48 | title + 10 (pp. 185–194) | 50/50 verses full (Bel and Nebo on the beasts) | `volumes/isaiah/` |
| Isaiah | 14 · A Light to the Gentiles | 49–51 | title + 15 (pp. 195–209) | 60/60 verses full (the servant never drawn) | `volumes/isaiah/` |
| Isaiah | 15 · A Man of Sorrows | 52–55 | title + 13 (pp. 210–222) | 57/57 verses full (52:13–53:12 words over a dry root, an empty road, stray sheep, a silent lamb; the servant never drawn) | `volumes/isaiah/` |
| Isaiah | 16 · The Fast That I Have Chosen | 56–59 | title + 15 (pp. 223–237) | 68/68 verses full (the armor laid out as a plate) | `volumes/isaiah/` |
| Isaiah | 17 · Arise, Shine | 60–62 | title + 9 (pp. 238–246) | 45/45 verses full (the anointed one never drawn: oil, scroll, opened prison) | `volumes/isaiah/` |
| Isaiah | 18 · New Heavens and a New Earth | 63–66 | title + 17 (pp. 247–263) | 80/80 verses full (63:1–6 over an empty winepress at sunset) | `volumes/isaiah/` |
| **Isaiah** | **complete: cover + 18 chapters** | **1–66** | **282 pages (263 numbered)** | **1,292 verses: all full** | `volumes/isaiah/` |
| Jeremiah | 1 · The Almond Rod | 1–3 | cover + title + 16 (pp. 1–16) | 81/81 verses full (his mouth touched as a shaft of light, the prophet kneeling; the almond rod and the caldron) | `volumes/jeremiah/` |
| Jeremiah | 2 · Evil from the North | 4–6 | title + 17 (pp. 17–33) | 92/92 verses full (waste and void as dark trembling hills) | `volumes/jeremiah/` |
| Jeremiah | 3 · The Temple of Jehovah | 7–9 | title + 17 (pp. 34–50) | 82/82 verses full (Topheth as altars and smoke, no one drawn) | `volumes/jeremiah/` |
| Jeremiah | 4 · The Broken Covenant | 10–12 | title + 13 (pp. 51–63) | 65/65 verses full | `volumes/jeremiah/` |
| Jeremiah | 5 · The Marred Girdle | 13–15 | title + 14 (pp. 64–77) | 70/70 verses full | `volumes/jeremiah/` |
| Jeremiah | 6 · The Potter's House | 16–18 | title + 16 (pp. 78–93) | 71/71 verses full | `volumes/jeremiah/` |
| Jeremiah | 7 · The Earthen Bottle | 19–22 | title + 16 (pp. 94–109) | 77/77 verses full (19:9 in words over the walls at night) | `volumes/jeremiah/` |
| Jeremiah | 8 · The Cup of the Wine of Wrath | 23–25 | title + 16 (pp. 110–125) | 88/88 verses full (the nations that drink the cup as lot boards and a map) | `volumes/jeremiah/` |
| Jeremiah | 9 · The Yoke | 26–28 | title + 14 (pp. 126–139) | 63/63 verses full (Uriah's death in words only) | `volumes/jeremiah/` |
| Jeremiah | 10 · A New Covenant | 29–31 | title + 18 (pp. 140–157) | 96/96 verses full (the measuring line of the city as a plan) | `volumes/jeremiah/` |
| Jeremiah | 11 · The Field at Anathoth | 32–33 | title + 15 (pp. 158–172) | 70/70 verses full | `volumes/jeremiah/` |
| Jeremiah | 12 · The Roll | 34–36 | title + 16 (pp. 173–188) | 73/73 verses full | `volumes/jeremiah/` |
| Jeremiah | 13 · The Dungeon | 37–39 | title + 15 (pp. 189–203) | 67/67 verses full (39:5–7 in words over the empty plain of Riblah) | `volumes/jeremiah/` |
| Jeremiah | 14 · Gedaliah | 40–42 | title + 13 (pp. 204–216) | 56/56 verses full (41:2–9 in words over the shut house and the pit's mouth) | `volumes/jeremiah/` |
| Jeremiah | 15 · Into Egypt | 43–45 | title + 11 (pp. 217–227) | 48/48 verses full | `volumes/jeremiah/` |
| Jeremiah | 16 · Against the Nations | 46–48 | title + 15 (pp. 228–242) | 82/82 verses full (Egypt, the Philistines and Moab as maps) | `volumes/jeremiah/` |
| Jeremiah | 17 · Babylon Is Taken | 49–50 | title + 17 (pp. 243–259) | 85/85 verses full | `volumes/jeremiah/` |
| Jeremiah | 18 · The Hammer of the Whole Earth | 51 | title + 13 (pp. 260–272) | 64/64 verses full (Seraiah's book sunk in the Euphrates) | `volumes/jeremiah/` |
| Jeremiah | 19 · The Fall of Jerusalem | 52 | title + 7 (pp. 273–279) | 34/34 verses full (2 Kings' drawings reused; Riblah in words only) | `volumes/jeremiah/` |
| **Jeremiah** | **complete: cover + 19 chapters** | **1–52** | **299 pages (279 numbered)** | **1,364 verses: all full** | `volumes/jeremiah/` |
| Lamentations | 1 · How Doth the City Sit Solitary | 1–2 | cover + title + 12 (pp. 1–12) | 44/44 verses full (one song box per verse; 2:11–12 and 2:20–21 in words over empty streets) | `volumes/lamentations/` |
| Lamentations | 2 · His Compassions Fail Not | 3–5 | title + 21 (pp. 13–33) | 110/110 verses full (4:4–10 and 5:9–12 in words over empty streets) | `volumes/lamentations/` |
| **Lamentations** | **complete: cover + 2 chapters** | **1–5** | **36 pages (33 numbered)** | **154 verses: all full** | `volumes/lamentations/` |
| Daniel | 1 · A Stone Cut Out Without Hands | 1–2 | cover + title + 13 (pp. 1–13) | 70/70 verses full (the image of gold, silver, brass, iron and clay as blueprint plates) | `volumes/daniel/` |
| Daniel | 2 · The Burning Fiery Furnace | 3–4 | title + 13 (pp. 14–26) | 67/67 verses full (3:22 words over the furnace mouth; the fourth in the fire a shape of light) | `volumes/daniel/` |
| Daniel | 3 · The Den of Lions | 5–6 | title + 13 (pp. 27–39) | 59/59 verses full (the writing a script of light, no hand drawn; 6:24 words only; the lions lying still) | `volumes/daniel/` |
| Daniel | 4 · The Ancient of Days | 7–8 | title + 12 (pp. 40–51) | 55/55 verses full (the beasts as heraldic emblems; the throne of fiery flames, no figure) | `volumes/daniel/` |
| Daniel | 5 · Seventy Weeks | 9–10 | title + 9 (pp. 52–60) | 48/48 verses full (Gabriel as a figure of light; the seventy weeks as a chart) | `volumes/daniel/` |
| Daniel | 6 · The Time of the End | 11–12 | title + 11 (pp. 61–71) | 58/58 verses full (the kings of the north and the south as a map) | `volumes/daniel/` |
| **Daniel** | **complete: cover + 6 chapters** | **1–12** | **78 pages (71 numbered)** | **357 verses: all full** | `volumes/daniel/` |
| Hosea | 1 · A Door of Hope | 1–3 | cover + title + 9 (pp. 1–9) | 39/39 verses full (Gomer only before the house; 2:2–13 words over an empty doorway) | `volumes/hosea/` |
| Hosea | 2 · The Cake Not Turned | 4–8 | title + 13 (pp. 10–22) | 75/75 verses full | `volumes/hosea/` |
| Hosea | 3 · I Will Be as the Dew | 9–14 | title + 15 (pp. 23–37) | 83/83 verses full (13:16 words over Samaria dark) | `volumes/hosea/` |
| **Hosea** | **complete: cover + 3 chapters** | **1–14** | **41 pages (37 numbered)** | **197 verses: all full** | `volumes/hosea/` |
| Joel | 1 · The Day of Jehovah | 1–3 | cover + title + 14 (pp. 1–14) | 73/73 verses full (the locusts as a plate and swarms; the Spirit poured out as light) | `volumes/joel/` |
| **Joel** | **complete: cover + 1 chapter** | **1–3** | **16 pages (14 numbered)** | **73 verses: all full** | `volumes/joel/` |
| Amos | 1 · For Three Transgressions | 1–4 | cover + title + 14 (pp. 1–14) | 59/59 verses full (the eight oracles over a map of the nations lit in turn) | `volumes/amos/` |
| Amos | 2 · The Plumb-line | 5–9 | title + 19 (pp. 15–33) | 87/87 verses full (the plumb-line as a blueprint, no hand drawn) | `volumes/amos/` |
| **Amos** | **complete: cover + 2 chapters** | **1–9** | **36 pages (33 numbered)** | **146 verses: all full** | `volumes/amos/` |

**Genesis through Lamentations, and Daniel through Amos (twenty-nine volumes), are complete.** Ezra is `tools/full/ezr/` (five chapters, plan in `ezr/__init__.py`; `ezr.art`
carries `chr2.art`; the Aramaic letters as sealed scrolls, `ezr.art.letter_scroll`, the return as `return_caravan`). Daniel, Hosea, Joel and Amos are `tools/full/dan/`, `hos/`, `jol/`, `amo/` (each art module builds on the one before; `dan.art` on
`est.art`): `dan/kit.py` `Lines(G, code, book, SPK)` builds captions, Voice boxes (`gls` keeps line breaks) and speech coloured and
tagged per speaker, panels `A`/`T`/`N`; packed with `job.jdiscourse`. Angels as `dan.art.glow_fig`; beasts as heraldic plates.
Isaiah is `tools/full/isa/` (18 chapters): prophecy by `isa.common.S("c:a-b", kind, looks, ...)`, which cuts a run of verses into panels
alternating Isaiah's face (`kg2.common.ISAIAH` + moods) with drawings `A(fn, bg, h=)`; `art2.nations_map(hi=, arrows=, show=)` serves every
burden of the nations; the servant and the anointed one are never drawn (a dry root, an empty road, a silent lamb).
Jeremiah is `tools/full/jer/` (19 chapters): prophecy by `jer.common.O`/`S` (whole verses in the Voice box beside Jeremiah's face or over a
drawing; `cut(ref, at)` splits "Jehovah said unto me,"), Jeremiah's face `jer.common.jer(age, mood)` (dark blue-grey headcloth, beardless
at his call, greying), `jer.art.near_east(...)` a map of the nations, `jer/pagepack.py` merges lone panels. Lamentations is
`tools/full/lam/`: `lam.common.L(c, a, b, d=… | t=…)` one song box per verse over a drawing or beside a mourner's face.
Psalms is `tools/full/psa/` (17 chapters by the five books): `psa.text` cuts what `asv.Book` drops — the superscriptions (`TITLES`), the
book heads (`BOOKS`), Psalm 119's first letter head and each verse's poetic line breaks — straight from `ref/asv`; they are `data-label`
heads, so the text check skips them. `psa.layout` copies `discourse.pack` with a red PSALM N head and song boxes one poetic line to a
row; a chapter is a list of `psa.common.psalm(n, "1 tree | 4 chaff | 10 DAVID_KING", god={...})` plans (scenes from `psa.art.SCENES`,
~120 drawings; faces from `FACES`).
Proverbs is `tools/full/pro/` (11 chapters): 1–9 and 30–31 by `discourse.pack` through `pro.common`; 10–29 as saying cells, two to a row
under an emblem (`pro.common.sayings`, `cellv`, `run`; ~117 emblems in `pro/emblems.py`, `pick()` chooses by the saying's words); Wisdom
in white with a gold band in gold light (`wisdom_fig`), the strange woman only far off and veiled. Ecclesiastes is `tools/full/ecc/` (the
Preacher is old Solomon) and the Song `tools/full/sng/` (the bride, the beloved and the daughters as faces; the likenesses only as the
things named, in cells: `sng.art.plate`); both have `common.drawn(refs, fn, bg)` (art sized under the song lines) and `paged()`.
Job is `tools/full/job/` (12 chapters, plan and restraint notes in `job/__init__.py`): its own copies of the packer and speech panels
(`job.jdiscourse`, `job.jspeech`) colour each speaker's song lines (`("song#D7261E", …)`), keep the poem's line breaks and name the
speaker on the panel (`seg(..., who=)`); `job.common` `pf`/`pd`/`pf2`/`pd2` set a speaker's verses beside a face or over a drawing, `gpd`
Jehovah's in Voice boxes; drawings in `job/art.py` … `art12.py` (`seated()`, `ostrich`, `hippo`, `croc`, `whirl` …). Cast: Job (white
headcloth with a gold band, then a sackcloth hood), Eliphaz in teal, Bildad slate-purple, Zophar deep blue, Elihu young in green.
Nehemiah is `tools/full/neh/` (7 chapters, plan in `neh/__init__.py`; `neh.art` has the wall and its gates as a plan,
`wall_plan(lit=, night=, companies=)`, the builders with a weapon in one hand, the pulpit of wood; `neh.common.plan_pages` sets one picture
above roll cells on every page of a list chapter). Nehemiah: black beard, slate-blue headcloth with a gold cord, greying in ch. 13; Ezra
(in Ezra and Nehemiah): white beard, indigo headcloth with a gold band. Esther is `tools/full/est/` (4 chapters, plan in `est/__init__.py`; every drawing new in
`est/art.py`: the palace of Shushan `hall()`, `kings_gate()` with winged bulls, the sceptre scene `inner_court(stage=)`, `empire_map`,
`pur_wheel`, `adar_days`; `est.common.crowned(tok)` puts a Persian crown on any face; no Voice box, the book never names God). Ezekiel and Obadiah–Malachi, and Matthew–Acts, are being built in parallel worktrees (packages `ezk`, `oba` … `mal`, `mat`, `mrk`, `luk`, `jhn`, `act`) from one brief, each merged when done. 2 Chronicles is `tools/full/chr2/` (fourteen chapters,
plan and restraint notes in `chr2/__init__.py`): Solomon's house reuses 1 Kings' blueprints, the kings of Judah 1–2 Kings' faces
and drawings (`chr2.common` takes the cast from `kg2.common`; `chr2.art` carries `chr1.art`, `kg2.art`, `kg1.art`), with new
battle maps (`battle_map`, `zerah_map`, `tekoa_map`, `posts_map`) and plans (`judah_forts`, `stopped_springs`, `outer_wall`). 1 Chronicles is `tools/full/chr1/` (a module
name cannot start with a digit; eleven chapters, plan in `chr1/__init__.py`): the genealogies of 1–9 as lineage charts
(`chr1.art.lineage`, `branch`, whose second row of names is staggered so no line crosses a name) over roll cells
(`chr1.common.cell`/`cells`/`roll`); David's story reuses 2 Samuel's cast and drawings (`sa2.common.over`/`D` for the reference
panels, `chr1.art.K2` = `sa2.art`); the courses of 23–27 as boards of lots (`chr1.art.lot_grid`), tally boards (`tally`), a plan
of the four gates (`porters_plan`) and a calendar wheel of the twelve captains (`month_wheel`). 2 Kings is `tools/full/kg2/` (13 chapters, plan and
restraint notes in `kg2/__init__.py`): it reuses 1 Kings' faces and drawings (`kg2.common` copies `kg1.common`; `kg2.art` re-exports
`kg1.art`), with Elisha (`kg2.art.elisha_fig`) and the exile maps (`assyria_map`, `exile_map`). `rolls.roll_pages(..., end=)` closes a
chapter on a roll page. Lists of reigns are `reign()` roll cells. 1 Kings is `tools/full/kg1/` (14 chapters, plan and
restraint notes in `kg1/__init__.py`). There is no digest book from here on, so every drawing is new (`kg1/art.py`): the temple and its
vessels are blueprint plates (`temple_plan`, `pillar_elev`, `molten_sea`, `base_laver`, from `exo.art8`'s `bp`/`dim`/`tag`); the reigns of
the kings are roll cells (`kg1.common.reign(name, refs, judah=)`, Judah gold, Israel red, `reign_pages`); Elijah is `kg1.art.elijah_fig`
(a hairy brown mantle, bareheaded). `kg1.common.joined(kind, ...)` builds one box from several cuts. 2 Samuel is `tools/full/sa2/` (12 chapters, plan and
restraint notes in `sa2/__init__.py`, the digest's two books lifted with `sa2.common.D("A5", 1)` / `D("B6", 0)`; `asv.Book.v(..., after=)`
finds a phrase said twice in one verse). 1 Samuel is `tools/full/sa1/` (14 chapters, plan and
restraint notes in `sa1/__init__.py`; the digest's two books lifted with `sa1.common.D("A3", 0)` / `D("B5", 2)`). It packs with
`discourse.pack(..., by_need=True, room=0.92, min_size=12.5)`: `min_size` splits any page on which a panel's words would
fall below that size, so long dialogue chapters stay readable. Ruth is `tools/full/rut/` (2 chapters, the digest's
Ruth book lifted with `rut.common.D(page, i, align)`; `reuse.fill(art, "xMidYMax")` keeps the figures when a half-width
panel is widened). Judges is `tools/full/jdg/`
(10 chapters, plan and restraint notes in `jdg/__init__.py`): like Joshua (`jdg.common` helpers, `D("A3", 0)` lifts the digest's
Deborah/Gideon book, `"B…"` the Samson book), packed with `by_need=True` so a page of short speeches keeps a readable size.
Judges 19 is drawn only as shut doors, dawn and a figure of twelve routes. `scratchpad`-style check worth repeating: a caption
whose words also sit inside a speech box on the same page means a `say(..., frm=)` is missing its `to=`. Joshua is `tools/full/jos/` (10
chapters, plan in `jos/__init__.py`): story chapters laid out by `discourse.pack` with `jos.common` line helpers (`face()`,
`drawn()`, `over()` for the digest's Jericho panels lifted with `reuse.fill`), battles as technical maps (`jos.art.ai_plan`,
`campaign`, `land_taken`) set under the words with `jos.art.below()`, and the lists of 12–21 as roll pages (`rolls.py`:
`roll_pages` packs cells, `verse_cells` groups a run of verses, two columns for the thirty and one kings). Restraint in Joshua:
6:21, 8:21–29, 10:24–28 and 11:11 are words over smoke, dust, a sealed cave or a heap; 7:25 over the heap of Achor.
`build_volume.py` also fails if any text cut from the ASV is on no page (it caught `discourse.pack` dropping pages).
Deuteronomy is `tools/full/deu/` (15
chapters, plan in `deu/__init__.py`): Moses' discourses as speech panels (`speech.orate`, packed by `discourse.pack`,
`deu.common.auto()` for long runs of his words), the statutes of 12–26 as spoken law cells (`deu.common.law_chapter`),
the songs as song boxes (`deu.common.sing`), the blessing of the tribes as `clan()` cells. Numbers is `tools/full/num/`
(16 chapters, plan in `num/__init__.py`). Its chapters number their pages with `num/pages.py` (`PG = Pages(start)`, `@PG.P(...)`,
`PG.extend(packed)`), so hand-drawn pages and pages packed by `exo.kit.law_pages` / `blueprints` mix in reading order; copy that
for new volumes. Lists are cells: `num.ch01.tally()` (a tribe and its number), `genesis.ch03.clan()`, `num.art15.station()`
(one encampment). Maps: `num/art.camp_plan()`, `art5.march_plan()`, `art7.spy_map()`, `art10.journeys()`, `art15.stations_map()`,
`art16.borders()`. Restraint in Numbers: 15:36 as the heap of stones; 16:31–35 as tents going down and censers; 25:4–8 as an empty
plain and a shut pavilion; 31 (the war with Midian) as distant smoke and the column of the prey, Moses' words over his face.
`exo.kit.law_pages(..., carry=True)` keeps the last page head on pages without one. Leviticus is
`tools/full/lev/` (9 chapters: 1 The Offerings 1–5 ·
2 The Consecration 6–8 · 3 Strange Fire 9–11 · 4 The Plague of Leprosy 12–13 · 5 The Cleansing 14–15 · 6 The Day of
Atonement 16–18 · 7 Holy unto Jehovah 19–22 · 8 The Set Feasts 23–25 · 9 Blessing and Curse 26–27). The laws are
`exo.kit.law_pages()`: items (heading, verses, pictogram, lead caption, page head) packed into pages of up to six
Voice-box cells, with pictograms from `lev/art.py` (an offering is the whole beast by the brass altar, then fire: no
carcasses). Each Leviticus chapter sets `START` from the previous chapter's page count, so numbering stays continuous.
Nadab and Abihu (10:1–5): the strange fire offered, then only their censers under the fire, then two wrapped shapes
carried far off. Aaron as high priest: `art9.high_priest()` at a distance, a grey-bearded face with a white mitre close up. Exodus lives in `tools/full/exo/` — the package is `exo` because `tools/kit/exodus.py` already owns
the name `exodus`; `python3 tools/full/build_volume.py exo` writes `volumes/exodus/` (the output folder is META's id). Planned Exodus
chapters (32,177 words): 1 The Bush That Burned (1–4) · 2 Let My People Go (5–8) · 3 The Passover (9–12) · 4 The Red Sea (13–15) ·
5 Bread from Heaven (16–18) · 6 Sinai (19–21) · 7 The Book of the Covenant (22–24) · 8 The Pattern of the Tabernacle (25–27) ·
9 Holy to Jehovah (28–31) · 10 The Golden Calf (32–34) · 11 The Willing Offering (35–38) · 12 The Glory (39–40). The making
repeats 25–31 almost word for word, but `kit.blueprints()` makes it cheap enough to keep every verse in full. Page numbers restart at 1 in each volume. 43:3–7 turned out short enough to keep in full. `ch14.talk()` builds
dialogue panels (a face plus a column of caption/balloon pieces, ovals deepened for long speeches).
Jacob's blessing (49:3–27) is two pages of cells, one per son; the volume ends with 完 "END OF GENESIS · NEXT · EXODUS". Joseph's story (37–50, ~11,500 words) is seven
chapters: 11 The Dreamer (37–38) · 12 The Captain of the Guard (39–40) · 13 Pharaoh's Dreams (41; 41:17–24 is a
retelling to abridge) · 14 The Brothers in Egypt (42–43) · 15 I Am Joseph (44–45) · 16 Israel in Egypt (46–47) ·
17 The Blessing of Jacob (48–50). `build_volume.py` now writes LF on every platform (no line-ending churn on Windows).
Genesis 28–36 is ~7,500 words, so Jacob's story is three chapters and the Genesis plan runs to twelve:
… 7 Jacob and Esau (25:19–27) · 8 The Ladder (28–30) · 9 Peniel (31–33) · 10 Bethel Again (34–36) ·
11 Joseph sold, Joseph raised up (37–41) · 12 Joseph and his brothers (42–50). Genesis 16–27 was too long for two chapters, so the
plan now runs to ten: 1 Creation and Eden (1–3) · 2 Cain to the Flood (4–9) · 3 Babel to Abram's covenant (10–15) ·
4 The Cities of the Plain (16–19) · 5 The Son of Promise (20–23) · 6 A Wife for Isaac (24:1–25:18) ·
7 Jacob and Esau (25:19–27) · 8 Jacob (28–36) · 9 Joseph sold, Joseph raised up (37–41) · 10 Joseph and his brothers (42–50).
A chapter may start or end inside a Bible chapter: give it `"span": ["24:1", "25:18"]` in META so coverage counts only
its verses. Genesis lists to treat as scroll pages: ch. 5, ch. 10, 11:10–32,
22:20–24, 25:1–4 and 12–18, ch. 36, 46:8–27 (166 verses). Retellings to abridge: 24:34–49, 41:17–24,
42:29–34, 43:3–7.


### Claude Design canvases (retired)

The pages used to be mirrored on private Claude Design canvases; that stopped after Genesis chapter 2. Pages
are generated, so edits made on a canvas could never flow back (the next build overwrites them and the
workflow's `--check` rejects them). Don't publish to the canvases or read them for content. The old artifacts
are left as they are (Genesis full edition, chapters 1–2: https://claude.ai/artifact/U99Xmh1RBdnVK7VynDna6L).
`canvas.json` files remain in the repo only because the website reads page order and titles from them.

## Repo layout

```
CLAUDE.md, README.md
adr/                  architecture decision records: one numbered file per decision (0001-asv-attribution.md, …)
.github/workflows/pages.yml   builds and deploys the website (see Website)
ref/asv/              the ASV as USFM from eBible.org (public domain): 02-GENeng-asv.usfm … — the text source
volumes/              THE FULL EDITION (generated by tools/full; never hand-edit)
  genesis/
    pages/            Main.dc.html (volume cover), GEN-C01-00-Title, GEN-C01-P01-… (chapter 1), …
    canvas.json       page index (order + titles) that the website reads; old Claude Design format
    volume.json       chapters for the website (dir, num, name, range, blurb, file prefixes)
    coverage.md       every verse of the chapters built so far: full / partial / omitted
_site/                the website, built locally for previews (git-ignored; Actions builds its own)
_book/                e-book and print exports (git-ignored; see Book export)
tools/
  full/               full-edition builder
    reference/        reference art: the old digest pages the volumes lift drawings from (<series>/book-NN/*.dc.html)
    asv.py            Book("GEN").v("1:3", frm=…, to=…) cuts exact text out of ref/asv and records coverage
    reuse.py          panels("reference/…/P05-Eden.dc.html") lifts a reference page's drawn panels for reuse
                      (a full-panel overlay div, e.g. rain streaks, comes along as an extra background layer)
    fx.py             page kit: use(art) / new(bg, w, h, svg) panels, vref() verse labels, day_stamp(),
                      chapter_title(), end_mark()
    build_volume.py   python3 tools/full/build_volume.py genesis  → writes volumes/genesis/ and checks the text
                      (--check writes nothing: fails if committed pages are out of date or any text isn't ASV)
    genesis/          __init__.py (META: chapters), cover.py, art.py (chapter 1 drawings), art2.py (chapter 2:
                      Cain's line, Noah and his house, the ark, the flood, the dove, the bow), art3.py (chapter 3: the
                      nations, Babel, Abram, Sarai and Lot, Egypt, the kings, Melchizedek, map-style panels), art4.py (chapter 4:
                      Hagar, Sarah, the men in white, the covenant, Sodom and the cave), art5.py (chapter 5: Abimelech, Isaac,
                      the wilderness of Beer-sheba, Moriah, Nahor's house, Machpelah), art6.py (chapter 6: Abraham's servant,
                      the well, Rebekah, Laban, camels couched and drinking), art7.py (chapter 7: Esau and Jacob, the pottage,
                      Gerar and the wells, the blind father, the kids of the goats), art8.py (chapter 8: Laban's house, Leah and
                      Rachel, the handmaids, the sons counter, the speckled flock and the rods), art9.py (chapter 9: the flight,
                      the teraphim, Gilead and Mizpah, the droves, the Jabbok, the meeting, Succoth), art10.py (chapter 10, and
                      `stage()`: a general scene builder — setting + cast placed by head height + props), art11.py (chapter 11: the
                      brethren, Dothan, the caravan, Judah and Tamar), art12.py (chapters 12–13: Potiphar's house, the prison,
                      the vine and the baskets, Pharaoh's court, the chariot, the storehouses), ch01.py … ch13.py
    exo/              the Exodus volume: __init__.py (META, id "exodus"), cover.py, kit.py (talk(): Genesis ch14's dialogue panel,
                      with short lines in balloons sized to their words; song(): a sung line; law(): a Voice-box cell for the
                      ordinances with a pictogram above, words auto-sized to the cell), art.py (the Exodus cast at a distance — moses(),
                      moses_prince(), aaron(), jethro(), zipporah(), pharaoh(), taskmaster(), princess(), elder(c, k), son(c, k),
                      hebrew(c), all usable in art10.stage()'s cast; faces; sons_row, bricks, households, milk_honey, peoples_map,
                      exodus_map() (Egypt → the wilderness → Canaan, as a technical map), burning() (the bush), black_tent(),
                      wonders(), horeb()), ch01.py …
  kit/                the shared drawing kit (mk.py, faces, figures, every art module; see below)
  site/               build_site.py, rebuild_site.py, shots.js, assets/site.css + site.js
  book/               export_book.py + render.js: a volume as a fixed-layout EPUB and a print PDF (see Book export);
                      asv_pdf.py: the whole ASV text as bible-asv.pdf, which the website links
```

Drawing kit reference (`tools/kit/`, and the website tools in `tools/site/`; the digest's book writers are gone, and
the crowd helpers the volumes used from them now live in `kit/crowds.py`):

```
  — shared kit —
  crowds.py           crowd(), procession() (men of war, trumpeters, the ark), midian_camp(), samson_both(), WAR colours
  figures.json        silhouettes: MAN, WOMAN, HAIR, LIE_BODY, LIE_ARM (feet at 0,0, ~200 units tall)
  faces.py            face(base="adam"|"eve", skin, shadow, hair, beard, scarf, egypt, collar, kohl,
                      false_beard, brow="scowl"|"sorrow", tear, sweat, stubble, light, …); faces/adam.svg, faces/eve.svg
  snake.py            snake(points, width, uid, head_scale): tapered, scaled serpent with a viper head
  egypt.py            pyramid(), granaries(), FAT/LEAN kine, SHEAF
  — Genesis —
  tower.py, ladder.py   Babel tower; Jacob's ladder with angels
  — Exodus —
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
  — Numbers and Joshua —
  numbers1.py         grapes(), fiery() (red-gold serpents), brass_serpent() (on its standard), ass()/ass_lying(),
                      mount() (a rider on an ass), angel() (white, winged, sword drawn), prostrate() (fallen on his face),
                      camp() (rows of tents), star(), SWORD_ARM/BLADE; Caleb, Balaam (angry, in awe), a frightened spy
  joshua1.py          jericho() (wall, towers, houses, Rahab's window and scarlet line), collapse() (the wall falling),
                      flax(), ark()/ark_borne() (the ark of the covenant on its staves), shofar()/trumpeter()/blasts(),
                      heap() + riverbed() (the Jordan standing in one heap), prince() (prince of Jehovah's host),
                      sun(), moon(), city_hill(), oak(); Joshua as leader, in awe and old, Rahab
  judges1.py          palm(), tabor(), tent_big(), rug_sleeper(), PIN/HAMMER, winepress(), wheat(), chaff(), fleece(), dew(),
                      bowl(), pitcher() (whole or broken, with its torch), torchbearer(), drinker_lap(), camel();
                      Deborah, Barak (afraid, bold), Jael, Gideon (afraid, bold, calm)
  judges2.py          samson() (figure with seven locks), lion(), fox() with firebrand, grain() (standing/burning), olive(),
                      jawbone(), philistines() (feathered head-dresses, round shields), gates() (doors, posts and bar), silver(),
                      mill(), fetters(), temple() (house of Dagon, lords on the roof, two middle pillars), cracks_on();
                      Samson (locks, asleep, blind and praying with a bandage), Delilah, Manoah's wife
  ruth1.py            sheaf(), field() (rows of ripe barley), reaper() with sickle, gleaner() (a stooping woman), graves(),
                      baby(), naomi_with_child(), heap() (heap of grain), sack(); Naomi, Mara (weeping), Naomi in joy,
                      Ruth (also weeping), Orpah, Boaz
  samuel1.py          lamp() (seven-branched lamp of God, lit or smoking), sanctuary() (veil and pillars inside the
                      tabernacle), shiloh() (tent of meeting in its linen court), mat_sleeper(), seat() (Eli's chair,
                      upright or fallen), eli_seated(), dagon(state 0 standing / 1 fallen / 2 stump only), head_alone(),
                      palm(), threshold(), cow()/calf() (milch kine), cart(), yoke(), team() (two kine and the cart with
                      the ark), vial() (horn of oil, pouring), drops(), boy() (child Samuel), eli(), hannah_with_child();
                      Hannah (weeping, joy), Eli (and in awe), child Samuel (day, night), Samuel old (and grieved), Saul
                      (and anointed)
  samuel2.py          david() (shepherd tunic, staff, bag; whirl=True spins the sling), sling(), goliath() (brass helmet,
                      coat of mail, greaves, great spear, shield), goliath_fallen(), helmet_alone(), stones(), brook(),
                      flying_stone(), harp() (kinnor), spear_in_wall(), crown(), cave() (bright ragged mouth),
                      skirt_piece(), knife(), gilboa(), spears_down(); David (also bold, grieved), Goliath, Jonathan,
                      Saul as king (also mad, weeping), Jesse
  samuel3.py          2 Samuel kit: dancer() (David in a linen ephod, both arms up, crowned), timbrel(), cymbals(),
                      musician() (timbrel / cymbals / harp), notes(), window() (arched palace window), cedar() (cedar
                      panelling), throne(), table() (the king's table), letter() (sealed scroll), roof() (palace roof
                      over Jerusalem's rooftops), lamb_held(); DAVID_K, NATHAN dicts; David as king (also joyful,
                      wrathful, grieving), David mourning, Nathan (also stern), Michal, Mephibosheth
  samuel4.py          absalom() (scarlet tunic, gold sash and band, heavy black hair behind), hanging() (caught in the oak,
                      arms up), great_oak() (thick trunk, long boughs; dark=True for silhouettes), bough_over(),
                      balance() (the hair weighed against shekels), gatehouse() (towers, gateway, chamber window, lit=),
                      runner(), stone_heap(), threshing_floor(), altar() (unhewn stones, fire and smoke); DAVID_OLD dict;
                      Absalom (also sly), David old (also alarmed, weeping), the Cushite, Gad
  — website and checking —
  build_site.py       writes the site from the volume folders
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
   Genesis 5 is two such pages, every verse in full). `ch03.py` adds `clan(...)` (a scroll cell without a lifespan bar, for
   the table of the nations) and `hud(...)` (a red counter tag); `art3.py` has map helpers (`grid_bg`, `node`, `route`)
   for technical-map panels. Size standing figures with `art2.fit(base, top)` (a
   figure is ~200 units tall at scale 1) so heads stay clear of the captions; figures are drawn front-on.
3. **Add the chapter to `META["chapters"]`** in `tools/full/<volume>/__init__.py`.
4. **Build and check:** `python3 tools/full/build_volume.py genesis` (stops on any text that isn't ASV), then
   `node tools/site/shots.js /tmp/png volumes/genesis/pages/GEN-C02-*.dc.html` and look at every page.
5. **Site and repo:** optionally preview with `python3 tools/site/rebuild_site.py --thumbs` (writes `_site/`);
   update the status table above and commit `volumes/` + `tools/` — the push deploys the site.

Starting a new volume: `tools/full/<id>/` with `__init__.py` (META with id, order, name, kanji, thumb
`vol-<id>-`, book code, chapters), `cover.py`, `art.py`, `ch01.py`.

## File format

Each page is a self-contained **Design Component** (`.dc.html`; the format comes from the retired Claude Design
canvases and the website reads it as is):

- Keep `<script src="./support.js"></script>` in `<head>` exactly as written.
- All markup sits inside `<x-dc>…</x-dc>`. Fonts come from one Google Fonts `<link>` in `<helmet>`.
- End with `<script type="text/x-dc" data-dc-script data-props='…'>` holding
  `class Component extends DCLogic { renderVals() {…} }`; `$preview` is `{"width":760,"height":1080}`.
  Covers declare an `accent` color prop and use `{{accent}}` on the kanji block.
- `{{hole}}` is a dotted lookup only, never an expression.
- Close every element, quote every attribute, use inline `style=""` (the editor edits it).
- Art is inline SVG plus CSS gradients: no images, emoji, DOM-building scripts or iframes.
- SVG `id`s get a per-panel prefix so `<defs>`/`<use>` never collide (the Exodus scripts pass one to `defs()`).
- Volume pages are **generated**: fix the script and re-run, never hand-edit the output.

`canvas.json` (written by `build_volume.py` for volumes): `v: 3`, `boards` keyed by file name (x, y, w 760, h 1080,
title), `order`, `notes`. The website uses `order` and each board's `title`.

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
出エジプト記 SHUTSU for Exodus, 民数記 MINSŪKI for Numbers, ヨシュア記 YOSHUA-KI for Joshua, 士師記 SHISHIKI for Judges, ルツ記 RUTSU-KI for Ruth, サムエル記上 SAMUERU-KI JŌ for 1 Samuel, エズラ記 EZURA-KI for Ezra, サムエル記下 SAMUERU-KI GE for 2 Samuel, 列王記上 RETSUŌKI JŌ for 1 Kings, 列王記下 RETSUŌKI GE for 2 Kings, 歴代志上 REKIDAISHI JŌ for 1 Chronicles, 歴代志下 REKIDAISHI GE for 2 Chronicles), one short ASV caption, "ASV" and "Vol. N" at the bottom (the digest covers predate this and
still spell it out; leave them).

**Recurring components** (all in `tools/kit/mk.py`):
- **Narration caption** `cap()`: paper box, 2 px ink border, mono 600 at 10–11 px, uppercase.
- **Voice of God** `god()`: indigo box with an inner gold rule, Anton, uppercase. God is never drawn.
- **Speech balloon** `balloon()` + `tail()`: white ellipse with a 2.5 px border; the SVG tail goes
  *before* the balloon in the DOM and its tip points at the speaker's mouth.
- **SFX** `sfx()`: katakana with a romanized tag (ゴオオ / GOOO, ドッ / DOH!).
- **Chapter stamp** `stamp(n)`: red-outlined rotated box, 第N章 over CHAPTER N, once per chapter.
- **Verse ref** `ref()`: tiny mono `EX 14:22` in a corner when no caption names the verse.
- **Speed lines** `speed()`, starfields `stars()`.
- **Running foot** (full edition, `fx.page()`): verses at the left, `— NN —` in the centre, `ASV` at the right,
  9 px grey mono, so every page names its translation. Chapter title pages end the credit line with "· ASV"
  the credit.

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
  - Pharaoh's daughter: black hair, gold band, collar, kohl. Zipporah: crimson headscarf with a woven gold hem along its
    front edge (`art.HEM`; without it a warm scarf reads as long red hair); a crimson robe at a distance.
  - Jethro (Reuel), priest of Midian: white hair and beard, dark-teal headcloth with a gold band; teal robe.
  - Joshua in Exodus 17: the young captain, black curly hair, bareheaded, a rust tunic at a distance (`art5.joshua`).
  - The midwives: Shiphrah (teal headscarf), Puah (slate-violet headscarf). Moses' father: black beard, bareheaded;
    Jochebed: slate-blue headscarf. Elders of Israel: grey beards, headcloths of six colours (`art.elder(c, k)`).
  - God is never drawn, not even a hand: "I will put forth my hand" is storm and lightning over Egypt (`art.wonders`).
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
- **Character guide (Genesis 10–15, full edition, `art3.py`):**
  - Abram: grey hair and beard, bareheaded; a slate-blue robe at a distance. Sarai: mulberry headscarf, dark hair; a
    mulberry robe at a distance. Lot: maroon headcloth with a dark cord, brown beard; a maroon robe.
  - Terah: white hair and beard. Nimrod: black hair and beard, gold band. Pharaoh of Abram's day: red-and-gold nemes.
    Melchizedek: white headcloth with a gold band, white beard, white robe and a small gold crown. The king of Sodom:
    plum headcloth with a gold band, black beard, scowl. Kings at a distance: a small gold crown on a robed figure.
  - Noah's three sons share one skin tone and differ only by robe colour (Shem blue, Ham rust, Japheth green); the
    table of the nations uses the same three colours.
  - The covenant pieces (15:10, 15:17) are drawn as covered offerings on stones: no carcasses shown.
- **Character guide (Genesis 16–19, `art4.py`):**
  - Abraham keeps Abram's look (grey hair and beard, slate-blue robe); Sarah from Genesis 17 is grey-haired under the
    mulberry headscarf. Hagar: Egyptian, black hair, kohl, cerulean headscarf and robe. Lot's wife: slate-grey robe;
    his two daughters: rose and ochre robes, seen only at a distance. The men of Sodom: black silhouettes with torches.
  - The angel of Jehovah with Hagar is a tall shape of white light (no face, no wings) and speaks in the Voice box, as
    does Jehovah at Mamre. The three men at Mamre and the two at Sodom are men in white with a gold rim and a soft
    glow, no wings and no faces drawn; at Sodom they speak in balloons.
  - Close-ups use `fc()` in `ch04.py`, which sizes a face to its panel so the eyes stay clear of the captions.
  - Restraint: Genesis 17 is drawn as covenant rings, renamed names and the household gathered; Genesis 19:4–9 as the
    crowd outside a shut door; 19:30–36 as the cave mouth from outside, a wine jar, a fire. Every word is on the page.
  - No seven-branched lamp before the tabernacle: Lot's house has a clay oil lamp (`art4.clay_lamp()`).
- **Character guide (Genesis 20–23, `art5.py`):**
  - Abimelech king of Gerar: blue headcloth with a gold band, black beard; a royal-blue robe and a small gold crown at a
    distance (also afraid with sweat, stern with red light). Phicol: slate-blue tunic and a spear.
  - Isaac as a child: cream tunic; as a lad (Genesis 22): brown curls, the digest's Isaac face. Ishmael: olive tunic.
  - Ephron the Hittite: rust headcloth with a dark cord, brown beard; the children of Heth sit in earth-toned robes at
    the city gate.
  - Moriah (22:9–10): Abraham as a black silhouette on the summit, Isaac a dark shape on the wood, then the digest's raised
    hand against the sky; no blade on a body. The angel of Jehovah speaks from heaven in the Voice box.
- **Character guide (Genesis 24–25:18, `art6.py`):**
  - Abraham in old age: white hair and beard. His servant, the elder of his house: tan headcloth with a dark cord, grey
    beard, tan robe. Rebekah: green headscarf, dark hair, green robe, pitcher on her shoulder; veiled in white (24:65).
  - Laban: rust-red headcloth with a cord, black beard, rust robe. Bethuel: white hair and beard, plum headcloth.
    Isaac grown: brown hair and beard, cream robe. Ishmael old: olive headcloth, white beard.
  - The retelling (24:34–49) is one page: 24:34–37 and 24:48–49 in full, the repeated middle as one balloon cut with "…",
    tagged "AS HE TOLD IT · GEN 24:37–47 ABRIDGED".
- **Character guide (Genesis 25:19–27, `art7.py`):**
  - Esau: red curly hair and red stubble, a rust-red tunic with fur marks, bow and quiver at a distance (faint, weeping
    and hating variants). Jacob: dark curly hair, beardless, slate-blue robe; in Esau's garments and the goat skins he
    wears Esau's rust tunic with dark gloves and collar. Both from the digest's Book Four faces.
  - Isaac in old age: white hair and beard, blind (pale eye), lamp-lit inside the tent; trembling in violet light.
  - Rebekah older: grey-brown hair under the green headscarf; urgent with a scowl and red light.
  - God's words to Rebekah, and to Isaac at Gerar and Beer-sheba, use the Voice box; Isaac's blessings are balloons.
- **Character guide (Genesis 28–30, `art8.py`):**
  - Jacob grows a black beard while serving Laban (from 29:21); slate-blue robe and staff at a distance.
  - Laban older: grey beard under the rust-red headcloth. Rachel: bareheaded, long black hair, rose robe.
    Leah: indigo headscarf (a warm scarf read as blonde hair), auburn hair, indigo robe; veiled in white at the
    wedding. Bilhah: teal robe; Zilpah: lavender robe (both only at a distance).
  - Jacob's children are counted on a strip of twelve nodes (`art8.sons_ring()`), the newest lit red, above scroll cells
    for each birth (`ch08.son()`), coloured by mother. 30:3–4, 9 and 14–16 are in full; drawn as faces, the tent door,
    the mandrake plant.
- **Character guide (Genesis 31–33, `art9.py`):**
  - Esau grown: red curls and a full red beard, rust robe (weeping at the meeting). The teraphim: three small clay
    household figures. The angels at Mahanaim are figures of light like the angel at the fountain; the man who wrestles
    at the Jabbok is the digest's paired silhouette, and his words are in the Voice box.
  - Rachel's words in 31:35 are in full; drawn as her face and the camel's saddle.
- Chapter title pages: the credit line is "Genesis · Volume One · ASV" (no edition name).
- **Character guide (Genesis 34–36, `art10.py`):**
  - Hamor: white beard, teal headcloth with a gold band. Shechem: teal headcloth with the band, stubble. Simeon and Levi:
    scowling, red light. Jacob greying from here (grey-black beard). Dinah: rose-pink robe, seen only at a distance.
  - Restraint: 34:2 is a caption over the city; the sword at Shechem is two figures at the gate under smoke; 35:22 is a
    caption over the tower of Eder. Rachel's death is her face and the midwife's, then the pillar by the road.
- **Character guide (Genesis 37–38, `art11.py`):**
  - Joseph young: brown curls, beardless; the coat of many colours as vertical stripes on his figure. Israel: grey-white
    hair and beard. Reuben: dark beard, sorrowful. Judah: off-white headcloth with a dark cord, black beard. The
    brethren: black stubble, scowl, red light. Tamar: dark-grey widow's scarf; violet veil at Enaim.
  - Faces' `scarf=` covers the hair, so warm reds and tans read as long hair: use off-white, dark or cool colours.
  - Genesis 38 is in full; drawn as faces, the gate of Enaim, the pledge, and the twins with the scarlet thread.
- **Character guide (Genesis 39–41, `art12.py`):**
  - Joseph has no coat of many colours after 37:23: a plain cream tunic (`stage()` cast "joseph_plain"). In Egypt, from
    41:14, he keeps his brown curls with an Egyptian collar and kohl (never a nemes, so he never looks like Pharaoh;
    the digest's nemes Joseph panels are not reused from 45:1 on). Judah's plea (44:18–34) is kept in full.
  - Pharaoh of Joseph's day: gold-and-blue nemes, false beard. Potiphar: white-and-blue headcloth, collar, kohl.
    Potiphar's wife: black hair, gold band, collar, kohl. The butler: white-and-red headcloth; the baker: tan.
  - 39:7–18 is in full; drawn as faces, an empty doorway and the garment in her hand.
- **Genesis faces:** Adam, Eve, Cain, Noah, Abraham, Sarah, Isaac, Jacob, Esau, Rachel, Joseph (also in
  Egyptian dress, weeping), Pharaoh of Joseph's day (gold-and-blue nemes), old Jacob — all in `faces.py`.
- **Character guide (New Testament, `tools/full/ntcast.py`, shared by every New Testament volume):**
  - Jesus is drawn as a man, always the same (the user chose this): a first-century Galilean, olive-brown skin, shoulder-length
    dark-brown hair, a short dark-brown beard, an undyed off-white robe and a blue-grey mantle over one shoulder, a soft gold glow, no
    halo. Faces `JESUS`, `JESUS_TEACH`, `JESUS_STERN`, `JESUS_GRIEF`, `JESUS_PASSION`, `JESUS_RISEN`; at a distance `jesus_fig(p, x, y, s)`.
    His words are ordinary speech balloons. The Father is never drawn (the voice from heaven in the Voice box over light); the Spirit
    at the baptism is a dove of light; angels are white light with a gold rim, no faces.
  - The recurring cast is in `ntcast` too (Peter, Andrew, James, John, Matthew, Thomas, Philip, Judas, Mary, Mary Magdalene, Martha,
    John the Baptist, a Pharisee, Caiaphas, Pilate, Herod, a centurion, Paul) with `ROBES` colours at a distance; never redraw them.
  - The passion with restraint: scourging and the crown of thorns words over the empty court; the crucifixion as three crosses on the
    hill against a darkened sky, from a distance only, no wounds or blood; his death words over the hill and the rent veil; the sealed
    tomb; the resurrection as the stone rolled away and the folded linen, then Jesus risen in white light. Demons are never drawn.
- **Serpents:** always `snake.py` (tapered body, belly scutes, blotches, viper head). The magicians'
  serpents are the brown recolor `exodus2.serpent(..., brown=True)`.

## Text rules

- **ASV** only, word for word. Trim with `…`; never paraphrase or
  modernize. Keep ASV wording: "Jehovah", "Jehovah God", "waste and void", "great sea-monsters",
  "kine", "murrain", "to-day", "the Cherubim".
- **Source: `ref/asv/*.usfm`** (eBible.org, public domain; Strong's tags and footnotes are stripped by `asv.py`).
  The full edition cuts every word out of it with `asv.Book`, and `build_volume.py` re-checks every caption,
  balloon and Voice box against it. Poetry (the Song of Deborah, David's lament, Jacob's blessing) is in the
  file too — no more fetch-tool refusals. For the digest, the old source was `https://ebible.org/asv/<BOOK><NN>.htm`.
- **Don't** quote the NASB, NAB or any other copyrighted translation. If asked for one, offer the ASV or the
  World English Bible (also public domain).
- **Attribution: always "ASV"** — never spelled out, never with the year, on pages, the website, the e-book or the
  docs (see `adr/0001-asv-attribution.md`).
- Captions carry narration, balloons carry dialogue, God's words always use the Voice box.
- Text that is not scripture (chapter titles, credits) carries `data-label` so the text check skips it.

## Website (built by GitHub Actions)

A static site built from `volumes/`, served at https://bible.apphaus.us. Nothing generated is committed: on every push to `master`,
`.github/workflows/pages.yml` checks each volume (`build_volume.py <vol> --check`), runs
`rebuild_site.py --thumbs --out _site` (Python + Pillow, Node + Playwright Chromium) and deploys `_site/`
twice: to GitHub Pages (https://apphaus2.github.io/Bible/) and, with `npx wrangler@4 deploy`, to Cloudflare as the Worker
`bible` (`wrangler.jsonc`: static assets from `_site/`, custom domain bible.apphaus.us; Cloudflare adds the DNS record), like the
other apphaus.us apps. Thumbnails are cached between runs (actions/cache on `_site/thumbs`), so a push only re-renders pages whose
source changed. One-time settings: repo Settings › Pages › Source: **GitHub Actions** (leave its custom domain empty: the domain
belongs to Cloudflare), and two Actions secrets, `CLOUDFLARE_API_TOKEN` (the "Edit Cloudflare Workers" token template, with
apphaus.us as its zone) and `CLOUDFLARE_ACCOUNT_ID`; without them the Cloudflare step is skipped. By hand from Windows (Node 22+):
`npx wrangler login` once, build `_site/` with `rebuild_site.py --thumbs`, then `npx wrangler deploy`. All links are
relative, so the site works at the domain root and at apphaus2.github.io/Bible/ alike. Runs: the repo's Actions tab (or "Run workflow" by hand).

- `index.html`: "The Books" (one section per volume, a card per chapter), "The Text", then a table of contents.
- `<volume>/chapter-NN/index.html` and `<volume>/chapter-NN/NN-<slug>.html` (page labels use the printed page
  number). Prev/Next chain through every chapter, across books.
- Reader controls (`tools/site/assets/site.js`): arrow keys, and swipe to turn the page. A swipe is only a quick
  one-finger flick (a quarter of the screen, at least 90 px, mostly sideways, under 0.6 s). A second finger (pinch)
  cancels it and blocks swipes for 0.6 s; nothing turns while the page is zoomed (`visualViewport.scale` > 1) or if the
  viewport panned during the gesture. Keep these rules if the reader changes; phones zoom to read the captions.
- `asv/GEN.pdf` …: the ASV split into one small PDF per book (66 files, the largest about 540 KB), like the HistoryX reader's
  book: every reader page has a top-right "📖 p. N" button that opens its book's PDF at the page where the page's chapter starts
  (`asv/2SA.pdf#page=18`; N is the printed page of the whole Bible). `asv/index.json` (chapter → page in the book file and in
  the whole PDF) is written by `asv_pdf.py` (`--split-only` redoes it from an existing `bible-asv.pdf`); the footer "ASV" credit
  opens the same place.
- `bible-asv.pdf`: the whole ASV text (see Book export). The workflow builds it with `tools/book/asv_pdf.py` and caches
  it (key: `ref/asv`, `asv_pdf.py`, `render.js`); `rebuild_site.py` copies `_book/bible-asv.pdf` in when it exists, and
  only then does `build_site.py` link it: a "Whole Bible · PDF" button and a "The Text" section on the home page, a
  "<range> in the ASV" button on every chapter/book page, and the "ASV" credit in every footer, which opens the PDF at
  that page's chapter (`#nameddest=GEN.24`, from the page's verse ref).
- `manifest.json`: every series/volume, book/chapter and page (title, verse ref, URL, thumbnail, source), plus `text`
  (the PDF's URL).
- `thumbs/`: 380×540 JPGs — `vol-<volume>-chapter-NN-<slug>.jpg`.
  `thumbs/.sources.json` keeps a hash of each thumbnail's source page; changed pages are re-rendered and
  unused thumbnails deleted automatically.

Local preview (same command the workflow runs; output in git-ignored `_site/`):
```
python3 tools/site/rebuild_site.py --thumbs   # needs node + playwright + Pillow; open _site/index.html
```
Volumes come from `volumes/*/volume.json` (written by `build_volume.py`). Always run `build_volume.py` and commit its output after changing a
volume's sources, or the workflow's `--check` step fails the deploy.

## Book export (e-reader and print)

`python3 tools/book/export_book.py genesis` writes `_book/genesis.epub` and `_book/genesis-print.pdf` from the same
pages the website uses. It needs Node + Playwright, like `shots.js`.
- **EPUB:** fixed-layout EPUB 3 (the comics standard), one XHTML page per manga page with vector art and live text,
  a cover image, contents by chapter and a page list with the printed numbers. Pages are converted to XHTML
  (SVG namespaces, `xlink:href`, `data-label=""`, `<br/>`), and each one is checked for well-formedness.
- **PDF:** 7 × 10 in trim (the page's own 0.704 ratio) plus 0.125 in bleed, vector. Story pages are fitted to the
  trim width with the panels 1/4 in inside the trim. Full-bleed pages (cover, chapter titles) are scaled to fill the
  bleed box. Keep text on full-bleed pages at least 40 px from the edge.
- **Fonts:** downloaded from the Google Fonts API, subset to the characters the volume uses, cached in
  `_book/fonts/` and embedded in both outputs (all four fonts are SIL Open Font License). `--no-fonts` skips this,
  and readers then substitute their own fonts (Anton's wide fallback breaks the title layouts).
- Still to do before a real print run: a CMYK proof of the reds and golds, a printer's preflight, and an epubcheck run.

**The ASV text as a PDF:** `python3 tools/book/asv_pdf.py` sets the whole Bible from `ref/asv` as `_book/bible-asv.pdf`
(about 1,175 pages, 8 MB, ~30 s): 7 × 10 in, two columns of Source Serif 4, red verse numbers, Anton chapter numerals
(on their own line where a chapter opens in poetry), a running head with the book name and the manga's running foot
(`— NN —`, ASV). Title page and testament dividers in the night/gold palette with 聖書; a contents page linking every
book and chapter; supplied words in italics; psalm titles, BOOK I–V, Psalm 119's letters and the 16 NT footnotes kept;
front matter and preface left out (ADR 0001). Every book, chapter and testament is a named destination, so
`bible-asv.pdf#nameddest=GEN.24` opens at Genesis 24 (`OT`, `NT`, `GEN`, `PSA.119` …). Needs Playwright ≥ 1.49
(Chromium 131 draws the running heads with CSS page-margin boxes) and `pypdf`, which writes the bookmarks: Chromium
only makes bookmarks in a tagged PDF, three times the size. `--books GEN,PSA` builds a quick proof.

## Checking pages

`node tools/site/shots.js <out_dir> page.dc.html …` renders PNGs with Playwright. The sandbox has no
Anton/Archivo/Plex fonts, so renders use wider fallbacks: if text fits there, it fits on the website.
Look at people, faces, balloon tails, overlaps and cut-off art before publishing. A lifted panel keeps its
original viewBox and is cropped (`slice`) to the new panel, so give it a row of similar proportions.

## Working notes for Claude

- **Where Claude works:** Claude Code on the user's Windows machine, in `C:\_GITHUB\apphaus2\Bible` (sometimes a
  worktree under `.claude/worktrees/`). Run Python as `PYTHONUTF8=1 python …` (the default code page breaks the
  UTF-8 sources). Node + Playwright for `shots.js` may need installing in a scratch folder (`NODE_PATH`).
- **"continue"** from the user means: build the next full-edition chapter.
- **"commit" / "update github"** means: commit straight to `master` (from a worktree, commit there and fast-forward
  `master` in the main clone), then give the push command; the user runs `git push`. The push deploys the site.
  Don't fuss over Windows line endings, but don't commit files whose only change is CRLF.
- Commit messages end with the Co-Authored-By line; the git author is Sky <sky75.morey@gmail.com>.

## Roadmap

- On through the Bible, book by book (Ezekiel through Malachi in progress; then the New Testament).
- `mk.person(..., up=…)` needs `"ManUp"`/`"WomanUp"` in that panel's `defs()`, or the figure renders headless.
- Possible option: right-to-left reading order.
