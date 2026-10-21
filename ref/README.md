# ref/ — the Bible texts

Each folder is one translation as USFM from eBible.org, named by its eBible id: the part of each file name after the
book code (`02-GENspaRV1909.usfm` is `spaRV1909`). The zip is `https://ebible.org/Scriptures/<id>_usfm.zip`; unzip its
`.usfm` files (and `copr.htm`, the licence) into `ref/<id>/`. Only public-domain texts are used.

| Folder | Text | Used for |
|---|---|---|
| `eng-asv/` | American Standard Version (1901), English | the manga: every word is cut from it (`tools/full/asv.py`) |
| `spaRV1909/` | Reina-Valera 1909, Spanish | `BIBLE_LANG=es` builds |
| `spablm/` | Biblia Libre para el Mundo, Spanish | the verses `spaRV1909`'s file lost |
| `fraLSG/` | Louis Segond 1910, French | `BIBLE_LANG=fr` builds |
| `deu1912/` | Luther 1912, German | `BIBLE_LANG=de` builds |
| `deuelo/` | Unrevised Elberfelder, German | the verses `deu1912`'s file lost |
| `ita1927/` | Riveduta 1927, Italian | `BIBLE_LANG=it` builds |
| `russyn/` | Russian Synodal | `BIBLE_LANG=ru` builds |
| `jpnm/` | Japanese Freedom Bible (an eBible draft) | `BIBLE_LANG=ja` builds |
| `cmn-cu89s/` | Chinese Union Version, simplified | `BIBLE_LANG=zh` builds |
| `cmn-cu89t/` | Chinese Union Version, traditional | characters `cmn-cu89s`'s file lost (`holes`) |
| `KorRV/` | 개역 Korean Revised Version (1952/61), from CrossWire's SWORD module (`korrv.conf`), not eBible | `BIBLE_LANG=ko` builds |

## Public-domain whole Bibles on eBible.org (64 of 248 whole Bibles; list of October 2026)

From `https://ebible.org/Scriptures/translations.csv`: downloadable, all 39 OT and 27 NT books, "public domain" in the
copyright line. DC = deuterocanonical books included (not used by the manga). Check `copr.htm` in the zip before using one.

| eBible id | Language | Title | DC |
|---|---|---|---|
| `arb-vd` | Arabic | Arabic Van Dyck Bible |  |
| `mya` | Burmese | Burmese Common Language Bible |  |
| `myajvb` | Burmese | Judson Burmese Bible |  |
| `cekak` | Chin, Eastern Khumi | Asang Khongca Bible |  |
| `hlt` | Chin, Matu | Matupi Chin Standard Bible w/ Strongs |  |
| `hltmcsb` | Chin, Matu | Matupi Chin Standard Bible 2019 | 17 |
| `cmn-cu89s` | Chinese | Chinese Union Version (simplified) |  |
| `cmn-cu89t` | Chinese | Chinese Union Version (traditional) |  |
| `cmnswcb` | Chinese, Mandarin | World Chinese Bible |  |
| `ces1613` | Czech | Czech Kralická Bible 1613 |  |
| `nld` | Dutch | Dutch Bible 1917 |  |
| `eng-asv` (in `ref/`) | English | American Standard Version (1901) |  |
| `eng-kjv` | English | King James Version + Apocrypha | 14 |
| `eng-kjv2006` | English | King James Version |  |
| `eng-rv` | English | Revised Version | 14 |
| `eng-web` | English | World English Bible Classic | 15 |
| `eng-webbe` | English | World English Bible British Edition with Deuterocanon | 15 |
| `engBBE` | English | Bible in Basic English |  |
| `engDBY` | English | Darby Translation |  |
| `engDRA` | English | Douay-Rheims 1899 | 7 |
| `engasvbt` | English | ASV Byzantine Text | 18 |
| `engbsb` | English | English Berean Standard Bible |  |
| `enggnv` | English | Geneva Bible 1599 |  |
| `engkjvcpb` | English | KJV Cambridge Paragraph | 14 |
| `engmsb` | English | Majority Standard BIble |  |
| `engwebp` | English | World English Bible |  |
| `engwebpb` | English | World English Bible British Edition |  |
| `engwebster` | English | Webster Bible |  |
| `engwebu` | English | World English Bible Updated | 15 |
| `engwmb` | English | World Messianic Bible |  |
| `engwmbb` | English | World Messianic Bible British Edition |  |
| `engylt` | English | Young's Literal Translation |  |
| `epo` | Esperanto | Esperanto Bible |  |
| `fraLSG` (in `ref/`) | French | French Louis Segond 1910 Bible |  |
| `fra_fob` | French | French Ostervald Bible |  |
| `frajnd` | French | French: Bible J.N. Darby |  |
| `frasbl` | French | French Free Holy Bible for the World | 15 |
| `deu1912` | German, Standard | German Luther Bible 1912 |  |
| `deuelo` | German, Standard | German Unrevised Elberfelder Bible |  |
| `deutkw` | German, Standard | German Textbibel |  |
| `hat` | Haitian | Haitian Creole Bible 1985 |  |
| `haw1868` | Hawaiian | Hawaiian Bible 1868 |  |
| `heb` | Hebrew | Modern Hebrew Bible |  |
| `ita1885` | Italian | Italian Diodati Bible |  |
| `ita1927` | Italian | Italian Riveduta Bible |  |
| `jpnm` | Japanese | Japanese Freedom Bible |  |
| `kor` | Korean | Korean Bible 1910 |  |
| `kos` | Kosraean | Kosraean Bible |  |
| `latVUC` | Latin | Clementine Vulgate 1598 | 7 |
| `pesOPV` | Persian | Old Persion Version Bible |  |
| `porbrbsl` | Portuguese | World Portuguese Bible | 15 |
| `ron1924` | Romanian | Romanian Bible (Cyrillic) |  |
| `russyn` | Russian | Russian Synodal Bible |  |
| `srp1865` | Serbian | Serbian DK Bible (Latin) |  |
| `srp1868` | Serbian | Serbian DK Bible (Cyrillic) |  |
| `spaRV1909` (in `ref/`) | Spanish | Reina Valera 1909 |  |
| `spabes` | Spanish | La Biblia en Español Sencillo |  |
| `spabll` | Spanish | Spanish BLL | 16 |
| `spablm` | Spanish | Spanish Free Bible for the World | 15 |
| `thafb` | Thai | Thai Freedom Bible |  |
| `ton` | Tongan | Revised West Version |  |
| `ukr1871` | Ukrainian | Ukrainian Bible by P. Kulish |  |
| `ukrfb` | Ukrainian | Ukrainian Freedom Bible |  |
| `vie1934` | Vietnamese | Vietnamese Bible 1923 |  |
