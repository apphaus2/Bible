"""The Job volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The prologue (1–2) is told as story; the speeches of Job, Eliphaz, Bildad, Zophar and Elihu are song lines (one box a verse,
the poem's lines kept, the rule in the speaker's colour) beside their faces or over drawings of the images in the poetry,
each panel tagged with the speaker's name (job.jdiscourse, job.jspeech: copies of discourse.py and speech.py). Jehovah's
speeches out of the whirlwind (38–41) are in the Voice box over storm and creation; God is never drawn. Satan is never drawn
either: his words are set over the heavens. Restraint: the servants slain and the house fallen on the young men (1:15–19)
words over the empty field, the burnt pasture, the dust of the bands and the fallen house; the boils (2:7) as sackcloth, a
potsherd and the ash heap; behemoth and leviathan drawn as the natural river-horse and crocodile.

Plan (18,263 words, twelve chapters): 1 The Land of Uz (1–3) · 2 The Vision of the Night (4–7) · 3 No Umpire Betwixt Us
(8–10) · 4 If a Man Die (11–14) · 5 My Witness Is in Heaven (15–17) · 6 My Redeemer Liveth (18–20) · 7 Where I Might Find
Him (21–24) · 8 Where Shall Wisdom Be Found? (25–28) · 9 The Months of Old (29–31) · 10 Elihu (32–37) · 11 Out of the
Whirlwind (38–39) · 12 Mine Eye Seeth Thee (40–42)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JOB")

META = {
  "id": "job", "order": 18, "name": "Job", "kanji": "ヨブ記", "thumb": "vol-job-", "book": "JOB",
  "title": "Job Volume", "volume": "Volume Eighteen",
  "lede": "The eighteenth book of the Bible, in full: a man in the land of Uz, perfect and upright, stripped of all he had; his three friends and their counsel; Elihu; Jehovah answering out of the whirlwind; and the latter end of Job blessed more than his beginning, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Land of Uz", "range": "Job 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "A man in the land of Uz, perfect and upright, with seven sons and three daughters and the greatest substance of the children of the east; Satan before Jehovah — doth Job fear God for nought?; four messengers, each escaped alone to tell thee; Jehovah gave, and Jehovah hath taken away; the boils, the potsherd and the ashes; three friends sitting silent seven days; then Job opened his mouth: let the day perish wherein I was born."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Vision of the Night", "range": "Job 4–7", "bible_chapters": [4, 5, 6, 7],
     "blurb": "Eliphaz the Temanite: who ever perished, being innocent?; a spirit passed before my face — shall mortal man be more just than God?; man is born unto trouble, as the sparks fly upward; happy is the man whom God correcteth. Job answers: oh that my vexation were but weighed; my brethren have dealt deceitfully as a brook; my days are swifter than a weaver's shuttle; what is man, that thou shouldest magnify him?"},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "No Umpire Betwixt Us", "range": "Job 8–10", "bible_chapters": [8, 9, 10],
     "blurb": "Bildad the Shuhite: doth God pervert justice?; inquire of the former age; can the rush grow up without mire?; whose trust is a spider's web. Job answers: how can man be just with God? — he maketh the Bear, Orion, and the Pleiades; he goeth by me, and I see him not; there is no umpire betwixt us; thou hast fashioned me as clay; the land of darkness and of the shadow of death."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "If a Man Die", "range": "Job 11–14", "bible_chapters": [11, 12, 13, 14],
     "blurb": "Zophar the Naamathite: canst thou by searching find out God? — it is high as heaven, deeper than Sheol. Job answers: no doubt but ye are the people; ask now the beasts, and they shall teach thee; behold, he will slay me, nevertheless I will maintain my ways; man, that is born of a woman, is of few days, and full of trouble; there is hope of a tree; if a man die, shall he live again?"},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "My Witness Is in Heaven", "range": "Job 15–17", "bible_chapters": [15, 16, 17],
     "blurb": "Eliphaz again: should a wise man fill himself with the east wind?; art thou the first man that was born?; the wicked man travaileth with pain all his days. Job answers: miserable comforters are ye all; his archers compass me round about; O earth, cover not thou my blood — even now, behold, my witness is in heaven; who is there that will strike hands with me?; the bars of Sheol."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "My Redeemer Liveth", "range": "Job 18–20", "bible_chapters": [18, 19, 20],
     "blurb": "Bildad again: the light of the wicked shall be put out; a gin shall take him by the heel. Job answers: he hath walled up my way; my kinsfolk have failed; have pity upon me, O ye my friends; oh that my words were graven in the rock for ever! — but as for me I know that my Redeemer liveth. Zophar again: the triumphing of the wicked is short; the viper's tongue; the bow of brass."},
  ],
}
