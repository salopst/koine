---
title: "Koine Greek Vocab--Mounce flash cards"
author: salopst
date: 2022-06-28T16:44:28+0100
lastmod: 2022-07-02T07:10:36+0100
filename: ~/Projects/koine/koine-greek-vocab-mounce-cards.md
filetags:
  - "koine"
  - "greek"
  - "vocab"
  - "mounce"
  - "cards"
  - "New Testament"
refs: 
- https://doxa.billmounce.com/MBG_Numbering.pdf
- https://blueletterbible.org/
- https://biblehub.com/
- https://wiktionary.org
- https://www.lexilogos.com/keyboard/greek_ancient.htm
---
# Koine Greek Vocab — Mounce flash cards

## Methodology

- of the 1000 cards, 1-325 (inclusive) are ordered from their appearance in Mounce's Basics of Biblical Greek Grammar.
- Cards 326-1000 are ordered by frequency of occurrence in the New Testament. In this case 49 down to 10.
- 10 cards a day, *most cursorily*, in the morning.
- Type them out here.
- Make an effort to find a gloss for each of the previous 10 cards.
- ~~At the end of each set of five, add the Strong's number and the review the gloss.~~ randomly add glosses for $n$ cards. Presence of a Strong's No. in the below lists should be *some* indication that the word has been studied.
- It is hoped that repition will make some of these stick.
- bit-by-bit, parse the below tables-of-twenty and jam into Anki. Obvs this will happen after adding all glosses, POS etc. So maybe revisit the *random* finding of Strong's numbers, and get back to regularity?****

- Current iteration (2022-07-18) of the db is:

```python
koineSchema ={
  'name': 'koine-words',
  'fields': [
    # typesense cannot index integer fields, so strongs=string
    { 'name': 'strongs', 'type': 'string' },
    { 'name': 'mounce', 'type': 'int32' },
    { 'name': 'frequency', 'type': 'int32' },
    { 'name': 'lexeme', 'type': 'string' },
    { 'name': 'genitive', 'type': 'string' },
    { 'name': 'article', 'type': 'string' },
    { 'name': 'pos', 'type': 'string' },
    { 'name': 'gloss_en', 'type': 'string' }
    # { 'name': 'derived', 'type': 'string' }
    # { 'name': 'mnemonic', 'type': 'string' }

  ],
  'default_sorting_field': 'frequency'
}
```

### TODO

-[x] create master dataset
    - firebase
    - in progress
-[x] Offer own database/API?
    - typesense
    - localhost only

- Do I need to specify the stem type? έλπιδο*θέλεματ* -- s3fcd (dental)
- Anki cards
- Beg Rhinospike for modern Greek pronunciation
- Record own pronunciation
- Redo koine Greek word of the day-- python/go/node?
- Look into spoken koine communities... Discord/Discourse/Reddit
- Quotation snippet, chapter/verse "model". If yes, hand-select or generate?
- English words derived from this greek word field?
- Aide-mémoires/mnemonics field?
- glosses in Latin, Old English, Spanish??

**POS** Parts of Speech

- [x] TODO: dig deeper into morphological classification. Now in ./data/DictRMAC.json, but not in the tables below.s
- [x] somewhat *ad hoc* system used principally 'cause I might want to parse some of these later.
πνεῦμα|πνεύμαtos|τό -- s3nc -- noun/3rd/neuter/changing-stem
| n | πνεῦμα    →  πνεύματα    |
| a | πνεῦμα    →  πνεύματα    |
| g | πνεύματος →  πνεύμων     |
| d | πνεύματι  →  πνεύμαςι(ν) |

ἐγώ -- p1ns -- pronoun/1st person/[nom|acc|gen|dat]/singular

### Card stock

- <https://www.ehow.com/how_7280259_measure-thickness-cardstock.html>

- Caliper is a measurement of paper thickness expressed in thousandths of an inch
  
- often get asked how do you measure the thickness of paper of card or card and the answer is simple – in microns using a micrometer. A micrometer is a tool for measuring very fine thicknesses.

-You get 1000 microns in every millimeter, which gives you one million microns per meter!

### Audio files

- `*.ogg` files on *wiktionary.org

- <https://upload.wikimedia.org/wikipedia/commons/transcoded/a/a8/Grc-%CF%88%CF%85%CF%87%CE%AE.ogg/Grc-%CF%88%CF%85%CF%87%CE%AE.ogg.mp3>
- 💡 `Grc-` langcode prefix.

```html
<td class="unicode audiolink" style="padding-right:5px; padding-left: 0;">Audio (Classical Attic)</td><td class="audiofile"><audio id="mwe_player_0" controls="" preload="none" width="175" style="width:175px;" data-durationhint="2" data-mwtitle="Grc-ψυχή.ogg" data-mwprovider="wikimediacommons"><source src="//upload.wikimedia.org/wikipedia/commons/a/a8/Grc-%CF%88%CF%85%CF%87%CE%AE.ogg" type="audio/ogg; codecs=&quot;vorbis&quot;" data-title="Original Ogg file (132 kbps)" data-shorttitle="Ogg source" data-width="0" data-height="0" data-bandwidth="131816" /><source src="//upload.wikimedia.org/wikipedia/commons/transcoded/a/a8/Grc-%CF%88%CF%85%CF%87%CE%AE.ogg/Grc-%CF%88%CF%85%CF%87%CE%AE.ogg.mp3" type="audio/mpeg" data-title="MP3" data-shorttitle="MP3" data-transcodekey="mp3" data-width="0" data-height="0" data-bandwidth="156232" /></audio></td><td class="audiometa" style="font-size: 80%;">(<a href="/wiki/File:Grc-%CF%88%CF%85%CF%87%CE%AE.ogg" title="File:Grc-ψυχή.ogg">file</a>)</td>
```

### Table editing

- org-mode, of course: <https://orgmode.org/worg/org-tutorials/tables.html>

- on the web: <https://tableconvert.com>
  
**Visual Studio Code**:  

- <https://marketplace.visualstudio.com/items?itemName=TakumiI.markdowntable>
`Ctrl + P` >> `ext install TakumiI.markdowntable`
- `Shift + Alt + F` : format all tables
- `Shift + Alt + T` : tab-seperated-values (TSV) to table

## 2022-06-28 Koine Greek Vocab--Mounce cards 1-20

| strongs | mounce | Freq. | lexeme    | genitive | article | pos | gloss_en                      |
| ------- | ------ | ----- | --------- | -------- | ------- | --- | ----------------------------- |
| 11      | 01     | 73    | Ἀβραάμ    | --       | ὁ       | s0m | Abraham                       |
| 32      | 02     | 75    | ἄγγελος   | ου       | ὁ       | s2m | angel, messenger              |
| 281     | 03     | 129   | ἀμήν      | --       | --      | adv | amen, truly, so be it         |
| 444     | 04     | 550   | ἄνθρωπος  | ου       | ὁ       | s2m | man, mankind f. == slave      |
| 652     | 05     | 80    | ἀπόστολος | ου       | ὁ       | s2m | apostle, envoy                |
| 1056    | 06     | 61    | Γαλιλαία  | ας       | ἡ       | s1f | Gallilee                      |
| 1124    | 07     | 50    | γραφή     | ῆς       | ἡ       | s1f | writing, drawing              |
| 1138    | 08     | 59    | Δαβίδ     | --       | ὁ       | s0m | David                         |
| 1391    | 09     | 166   | δόξα      | ης       | ἡ       | sub | glory, majesty, fame, opinion |
| 1473    | 10     | 1725  | ἐγώ       | --       | --      | pns | I am                          |
| 2078    | 11     | 52    | ἔσχατος   | η        | ον      | adj | last/first, end, extreme      |
| 2222    | 12     | 135   | ζωή       | ῆς       | ἡ       | s1f | life, life-force              |
| 2316    | 13     | 1317  | θεός      | οῦ       | ὁ       | s2m | God, the Lord, a god          |
| 2532    | 14     | 9153  | καί       | --       | --      | con | and, even, also, namely       |
| 2588    | 15     | 156   | καρδία    | ας       | ἡ       | s1f | heart, life, spirit           |
| 2889    | 16     | 186   | κόσμος    | ου       | ὁ       | s2m | order, world, mode, ruler     |
| 3056    | 17     | 330   | λόγος     | ου       | ὁ       | s2m | word, statement, message      |
| 3972    | 18     | 158   | Παῦλος    | ου       | ὁ       | s2m | Paul                          |
| 4074    | 19     | 156   | Πέτρος    | ου       | ὁ       | s2m | Peter, rock, stone            |
| 4091    | 20     | 55    | Πιλᾶτος   | ου       | ὁ       | sub | Pilate                        |

## 2022-06-29 Koine Greek Vocab--Mounce cards 21-40

| strongs | mounce | Freq. | lexeme   | genitive | article | pos  | gloss_en                      |
| ------- | ------ | ----- | -------- | -------- | ------- | ---- | ----------------------------- |
| 4151    | 21     | 379   | πνεῦμα   | ματος    | τό      | s3nc | air, spirit, breath           |
| 4396    | 22     | 114   | προφήτης | ου       | ὁ       | s1m  | prophet, seer                 |
| 4521    | 23     | 68    | σάββατον | ου       | τό      | s2n  | sabbath, week                 |
| 4396    | 24     | 75    | Σίμων    | ωνος     | ὁ       | s3m  | Simon                         |
| 5456    | 25     | 139   | φωνή     | ῆς       | ἡ       | s1f  | sound, noise, voice           |
| 5547    | 26     | 529   | Χριστός  | ου       | ὁ       | s2m  | Mesiah, Christ                |
| 26      | 27     | 116   | ἀγάπη    | ης       | ἡ       | s1f  | love, amistad, goodwill       |
| 243     | 28     | 115   | ἄλλος    | ή        | ὁ       | adj  | other, another                |
| 846     | 29     | 5597  | αὐτός    | ή        | ὁ       | adj  | he, she, it... them etc.      |
| 932     | 30     | 162   | βασιλεία | ας       | ἡ       | s1f  | kingdom, royal rule           |
| 1161    | 31     | 2792  | δέ       | --       | --      | con  | but, and, then rather         |
| 1722    | 32     | 2752  | ἐν       | --       | --      | con  | in, on, amongst, within       |
| 2041    | 33     | 169   | ἔργον    | ου       | τό      | s2n  | work, deed, business          |
| 2540    | 34     | 85    | καιρός   | οῦ       | ὁ       | s1m  | (appointed) time, season      |
| 3568    | 35     | 147   | νῦν      | --       | --      | adv  | now, at (the) present         |
| 3588    | 36     | 19870 | ὁ        | ἡ        | τό      | art  | the, he/she, it, that         |
| 3754    | 37     | 1296  | ὅτι      | --       | --      | con  | that, since, because          |
| 3756    | 38     | 1606  | οὐ       | οὐκ      | οὐχ     | adv  | not, no, never                |
| 5610    | 39     | 106   | ὥρα      | ας       | ἡ       | s1f  | hour, occasion, moment        |
| 266     | 40     | 173   | ἁμαρτία  | ας       | ἡ       | s1f  | sin, sinfulness, fault, error |

## 2022-06-30 Koine Greek Vocab--Mounce cards 41-60

| strongs | mounce | Freq. | lexeme     | genitive | article | pos       | gloss_en                                                               |
| ------- | ------ | ----- | ---------- | -------- | ------- | --------- | ---------------------------------------------------------------------- |
| 716     | 41     | 55    | ἀρχή       | ῆς       | ἡ       | s1f       | beginning, first, authority, ruler                                     |
| 1041    | 42     | 1041  | γάρ        | --       | --      | con       | (postpositive) for, indeed, because                                    |
| 0000    | 43     | 708   | εἶπεν      | --       | __      | vaia3s    | he said (from εἶπον with movable nu.)                                  |
| 1519    | 44     | 1768  | εἰς        | --       | --      | p+acc     | into                                                                   |
| 1849    | 45     | 102   | ἐξουσία    | ας       | ἡ       | s1f       | authority, power, jurisdiction                                         |
| 2098    | 46     | 76    | εὐαγγέλιον | ου       | τό      | s2n       | gospell, good news                                                     |
| 2424    | 47     | 47    | Ἰηςοῦς     | ου       | ὁ       | s2m       | Jesus, Joshua                                                          |
| 2962    | 48     | 717   | κύριος     | ου       | ὁ       | s12m      | lord, master, saviour, guardian,owner                                  |
| 3361    | 49     | 1042  | μή         | --       | --      | part      | not, lest                                                              |
| 3772    | 50     | 273   | οὐρανος    | ου       | ὁ       | s2m       | sky, heaven                                                            |
| 3778    | 51     | 1338  | οὗτος      | αὗτη     | τοῦτο   | dpro      | this/these; he/ they                                                   |
| 4771    | 52     | 1069  | σύ         | --       | --      | ppro      | you 1ns (first person nominative singular)                             |
| 5207    | 53     | 377   | υἱός       | οῦ       | ὁ       | s2m       | son, descendant                                                        |
| 5620    | 54     | 83    | ὥστε       | --       | --      | conj      | so that, therefore (crasis of ὡς (5613) and τέ (5037))                 |
| 235     | 55     | 638   | ἀλλά       | --       | --      | conj      | but, instead, yet, except                                              |
| 517     | 56     | 646   | ἀπό        | --       | --      | p+gen     | (away) from +gen                                                       |
| 1223    | 57     | 668   | διά        | --       | --      | P+gen/acc | through, by means of +gen; because of, for the sake of, therefore +acc |
| 0000    | 58     | 2460  | εἶμι       | --       | --      | vpia1ns   | I am, exist (Mounce); I come/go (everywhere else)                      |
| 1537    | 59     | 914   | ἐκ, ἐξ     | --       | --      | p+gen     | from, out of +gen                                                      |
| 2250    | 60     | 389   | ἡμέρα      | ας       | ἡ       | s1f       | day, time of the day, time, indefinite period of time                  |

## 🇨🇦🇨🇦 2022-07-01 Koine Greek Vocab--Mounce cards 61-80

| strongs | mounce | Freq. | lexeme   | genitive | article | pos      | gloss_en                                                 |
| ------- | ------ | ----- | -------- | -------- | ------- | -------- | -------------------------------------------------------- |
| 2258    | 61     | 315   | ἦν       | --       | --      | vpia3ns  | he was : εἶμι (pres ind act  3rd personalsing)           |
| 2281    | 62     | 91    | θάλασσα  | ης       | ἡ       | s1f      | sea, Mediterranean, salt water                           |
| 2288    | 63     | 120   | θάνατος  | ου       | ὁ       | s2m      | death, corpse                                            |
| 2443    | 64     | 663   | ἵνα      | --       | --      | conj     | in order that, so that, so (inroduces clause)            |
| 2491    | 65     | 135   | Ἰωάννης  | ου       | ὁ       | s1m      | John                                                     |
| 3004    | 66     | 2354  | λέγω     | --       | --      | verb     | I say, speak, reckon                                     |
| 3326    | 67     | 469   | μετά     | --       | --      | prep+g+a | with + gen ; after +acc                                  |
| 3614    | 68     | 93    | οἰκία    | ας       | ἡ       | s1f      | house, home; family                                      |
| 3624    | 69     | 114   | οἶκος    | ου       | ὁ       | s2f      | house, home, temple, lineage                             |
| 3793    | 70     | 175   | ὅχλος    | ου       | ὁ       | s2m      | crowd, populace, mob, riot                               |
| 3844    | 71     | 194   | παρά     | --       | --      | prep+g+d | from+gen ; beside, in presence of + dat ; alongside +acc |
| 3850    | 72     | 50    | παραβολή | ῆς       | ἡ       | s1f      | juxtaposition, illustration, parable, analogy            |
| 4314    | 73     | 700   | πρός     | --       | --      | prep+a   | to, towards, with                                        |
| 5259    | 74     | 22    | ὑπό      | --       | --      | prep+g+a | by +gen ; under/below of +acc                            |
| 18      | 75     | 102   | ἀγαθός   | ή        | όν      | adj      | good, profitable, generous, upright, virtuous            |
| 27      | 76     | 61    | ἀγαπητός | ή        | όν      | adj      | beloved, dear; worthy of love                            |
| 166     | 77     | 71    | αἰώνιος  | --       | ον      | adj      | eternal, long ago                                        |
| 240     | 78     | 100   | ἀλλήλων  | --       | --      | pro3gp   | one another   (reflexive 3gp)                            |
| 611     | 79     | 82    | ἀπεκρίθη | --       | --      | V-ADI-3S | he answered (Aorist/Middle Deponent Indicative)  3rd PS) |
| 1400    | 80     | 124   | δοῦλος   | ου       | ὁ       | s2m      | servant, slave                                           |

## 🏳️‍🌈🏳️‍🌈 2022-07-02 Koine Greek Vocab--Mounce cards 81-100

| strongs | mounce | Freq. | lexeme  | genitive | article | pos      | gloss_en                                                                |
| ------- | ------ | ----- | ------- | -------- | ------- | -------- | ----------------------------------------------------------------------- |
| 1437    | 81     | 351   | ἐάν     | --       | --      | conj     | if, except, unless; (marker for the subjunctive)                        |
| 1699    | 82     | 76    | ἐμός    | ἐμή      | ἐμόν    | adj      | my, mine                                                                |
| 1785    | 83     | 67    | ἐντολή  | ῆς       | ἡ       | s1m      | an injunction, order, command, behest                                   |
| 2531    | 84     | 182   | καθώς   | --       | --      | adj      | how, as, when, even as                                                  |
| 2556    | 85     | 50    | κακός   | ή        | όν      | adj      | bad, low-born, mean, evil, base, corrupt, affliction                    |
| 1473    | 86     | 564   | μου     | --       | --      | pro-1g6  | my  (1gs of ἐγώ (1ns))                                                  |
| 3738    | 87     | 128   | νεκρός  | νεκρά    | νεκρόν  | adj      | dead, lifeless, mortal                                                  |
| 4103    | 88     | 67    | πιστός  | ή        | όν      | adj      | faithful,  believing, trustworthy                                       |
| 4190    | 89     | 78    | πονηρός | ή        | όν      | adj      | bad, malaevolent, indolent, wicked                                      |
| 4413    | 90     | 155   | πρῶτος  | η        | ον      | adj      | first, earlier                                                          |
| 5154    | 91     | 56    | τρίτος  | η        | ον      | adj      | third                                                                   |
| 39      | 92     | 233   | ἅγιος   | ἄγιη     | ἅγιον   | adj      | holy, moral,consecrated                                                 |
| 1509    | 93     | 503   | εἰ      | --       | --      | conj     | if                                                                      |
| 1509    | 94     | 86    | εἰ μή   | --       | --      | conj     | if not                                                                  |
| 1519    | 95     | 344   | εἷς     | μία      | ἕν      | num-ord  | one                                                                     |
| 2235    | 96     | 61    | ἤδη     | --       | --      | adv      | now, already, by this time,                                             |
| 3686    | 97     | 231   | ὄνομα   | ματος    | τό      | s3n      | name, fame, reputation                                                  |
| 3762    | 98     | 234   | οὐδείς  | οὐδεμί   | οὐδέν   | pro      | none, nothing, no one                                                   |
| 3956    | 99     | 1244  | πᾶς     | πᾶσα     | πᾶν     | adjy     | each, every , all                                                       |
| 4012    | 100    | 333   | περί    | --       | --      | prep+g+a | (gen.) concerning, with regard to, about; (acc.) nearby, around, about, |

## 2022-07-03 Koine Greek Vocab--Mounce cards 101-120

| strongs | mounce | Freq. | lexeme   | genitive | article | pos   | gloss_en                                     |
| ------- | ------ | ----- | -------- | -------- | ------- | ----- | -------------------------------------------- |
| 4561    | 101    | 147   | σάρξ     | σάρκος   | ἠ       | s3n   | flesh, the natural order                     |
| 4862    | 102    | 128   | σύν      | --       | --      | p+dat | with, beside                                 |
| 4983    | 103    | 103   | σῶμα     | ςῶματος  | τό      | s3n   | body, the entirety of a thing                |
| 5048    | 104    | 99    | τέκνον   | ου       | τό      | s2n   | child, descendant                            |
| 5100    | 105    | 525   | τις      | τι       | --      | adj   | one, anyone, something                       |
| 5101    | 106    | 555   | τίς      | τί       | --      | int   | who? what? which? why?                       |
| 80      | 107    | 341   | ἀδελφός  | οῦ       | ὁ       | s2m   | bother, countryman                           |
| 302     | 108    | 167   | ἄν       | ἄν       | --      | part  | (indicates conditionality)                   |
| 120     | 109    | 216   | ἀνήρ     | ἀνδρός   | ὁ       | s3mcd | man, husband, human                          |
| 1711    | 110    | 114   | ἐκκλησία | ας       | ἡ       | s1f   | church, assembly, congregation               |
| 1680    | 111    | 53    | ἐλπίς    | ἐλπίδος  | ἡ       | s3fcd | hope, expectation:= Elpis Vresley            |
| 1854    | 112    | 63    | ἔξω      | ἐξωτέρω  | ἐξωτάτω | adv   | out, outside                                 |
| 1909    | 113    | 890   | ἐπί      | --       | --      | pgda  | g on, over; d: on, at, while; a: across, for |
| 2249    | 114    | 864   | ἡμεῖς    | --       | --      | pp1p  | we, us, our                                  |
| 2307    | 115    | 62    | θέλημα   | ματος    | τό      | s3ncd | will, desire:= Thelma and Loiuse             |
| 2396    | 116    | 34    | ἴδε      | --       | --      | int   | see!, look!; here, there                     |
| 2400    | 117    | 200   | ἰδου     | --       | --      | int   | behold!, suddenly, now                       |
| 2566    | 118    | 100   | καλός    | ή        | όν      | adj   | good, right; beautiful; excellent            |
| 3384    | 119    | 83    | μήτηρ    | μητρός   | ἡ       | s3fc  | mother                                       |
| 3761    | 120    | 143   | οὐδέ     | --       | --      |       | and not, nor, neither, not even              |

## 🇱🇷🇱🇷 2022-07-04 Koine Greek Vocab--Mounce cards 121-140

| strongs | mounce | Freq. | lexeme     | genitive | article | pos  | gloss_en                                         |
| ------- | ------ | ----- | ---------- | -------- | ------- | ---- | ------------------------------------------------ |
| 3962    | 121    | 413   | πατήρ      | πατρός   | ὁ       | s3m  | father, ancestor                                 |
| 4102    | 122    | 243   | πίστις     | πίστεως  | ή       | s3f  | faith, belief, trust, faithfulness               |
| 5204    | 123    | 76    | ὑδωρ       | ὑδατος   | τό      | s3n  | water, rain, sweat, time (waterclocks)           |
| 5210    | 124    | 1840  | ὑμεῖς      | --       | --      | pnsp | you (pl)                                         |
| 5457    | 125    | 73    | φῶς        | φωτός    | τό      | s3n  | light, daylight, firelight                       |
| 5485    | 126    | 155   | χάρις      | χάριτος  | ἡ       | s3f  | grace, favour, kindness, charm, thanks           |
| 5602    | 127    | 61    | ὧδε        | --       | --      | adv  | here, thus, in this manner                       |
| 265     | 128    | 122   | αἰώνος     | αἰῶνος   | ὁ       | s3m  | age, etenity,lifetime                            |
| 1320    | 129    | 59    | διδάσκαλος | ου       | ὁ       | s2m  | teacher, master                                  |
| 2117    | 130    | 51    | εὐθύς      | --       | --      | adv  | immediately (of time); directly,straight (place) |
| 2193    | 131    | 146   | ἕως        | --       | --      | cap  | (conj, adv, prep+gen)  until, so far as          |
| 3101    | 132    | 261   | μαθητής    | οῦ       | ὁ       | s3f  | disciple, pupil, seeker, student                 |
| 3303    | 133    | 179   | μέν        | --       | --      | part | "on the one hand", whereas                       |
| 3367    | 134    | 90    | μηδείς     | μηδεμία  | μηδέν   | pro  | nothing, no one                                  |
| 3441    | 135    | 114   | μόνος      | η        | ον      | adj  | alone, only, forsaken, solitary                  |
| 3704    | 136    | 53    | ὅπως       | --       | --      | con  | how, that, in order that                         |
| 3745    | 137    | 110   | ὅσος       | η        | ον      | adj  | as gret as, so many as; often                    |
| 3767    | 138    | 499   | οὖν        | --       | --      | part | therefore, then, accordingly                     |
| 3788    | 139    | 100   | ὀφθαλμός   | οῦ       | ὁ       | s2m  | eye, sight, vision                               |
| 3825    | 140    | 141   | πάλιν      | --       | --      | adv  | again (of time); back, backwards (of place)      |

## 2022-07-05 Koine Greek Vocab--Mouncecards 141-160

| strongs | mounce | Freq. | lexeme     | genitive | article | pos      | gloss_en                                  |
| ------- | ------ | ----- | ---------- | -------- | ------- | -------- | ----------------------------------------- |
| 4228    | 141    | 93    | πούς       | ποδός    | ό       | s3m      | foot                                      |
| 5228    | 142    | 150   | ὑπέρ       | --       | --      | pga      | +gen in behalf of; +acc above             |
| 1135    | 143    | 215   | γυνή       | γυναικός | ἡ       | s3fc     | (irreg)                                   |
| 1343    | 144    | 92    | δικαιοσύνη | ης       | ἡ       | s1f      | righteosness, justice                     |
| 1427    | 145    | 75    | δώδεκα     | --       | --      | num      | twelve                                    |
| 1438    | 146    | 319   | ἑαυτοῦ     | ῆς       |         | pp3g     | of himself, of themseleves                |
| 1565    | 147    | 265   | ἐκεῖνος    | η        | ο       | pro      | that, those                               |
| 0000    | 148    | 343   | ἥ          | --       | --      | part     | or, either, than                          |
| 2504    | 149    | 84    | κἀγώ       | --       | --      | conj     | and I (crasis of καὶ (kaì) and ἐγώ (egṓ)) |
| 3107    | 150    | 50    | μακάριος   | ια       | ιον     | adj      | blessed, happy, fortunate                 |
| 3173    | 151    | 243   | μέγας      | μεγάλη   | μέγα    | adj      | large, great, loud, awesome               |
| 4172    | 152    | 162   | πόλις      | εως      | ἡ       | s3f      | city, town, village                       |
| 4118    | 153    | 416   | πολύς      | πολλή    | πολύ    | adj/adv  | many, great, large; often (adv.)          |
| 4459    | 154    | 103   | πῶς        | --       | --      | part     | how? how many?                            |
| 4592    | 155    | 77    | σημεῖον    | ου       | τό      | s2n      | sign, signal, mark                        |
| 225     | 156    | 109   | ἀλήθεια    | ας       | ἡ       | s1f      | truth, sincerity, divine truth            |
| 1515    | 157    | 92    | εἰρήνη     | ης       | ἡ       | s1f      | peace, harmony, safety, welfare, health   |
| 1799    | 158    | 94    | ἐνώπιον    | --       | --      | prep+gen | before, in the presence of                |
| 1860    | 159    | 52    | ἐπαγγελία  | ας       | ἡ       | s1f      | promise, annunciation                     |
| 2033    | 160    | 88    | ἑπτά       | --       | --      | num      | seven                                     |
  
## 2022-07-06 Koine Greek Vocab--Mouncecards 161-180

| strongs | mounce | Freq. | lexeme      | genitive | article | pos      | gloss_en                             |
| ------- | ------ | ----- | ----------- | -------- | ------- | -------- | ------------------------------------ |
| 2362    | 161    | 62    | θρόνος      | ου       | ὁ       | s2m      | throne, seat of power                |
| 2419    | 162    | 177   | 'Ιερουσαλήμ | --       | ή       | s1f      | Jerusalem                            |
| 2596    | 163    | 473   | κάτα        | --       | --      | prep+g+a | against (gen.) ; according to (acc.) |
| 2776    | 164    | 75    | κεφαλή      | ῆς       | ἡ       | s1f      | head, top, origin                    |
| 3598    | 165    | 101   | ὁδός        | οῦ       | ἡ       | s2f      | road, path, journey                  |
| 3739    | 166    | 1365  | ὅς          | ἥ        | ὅ       | dem pro  | who, whom, that which                |
| 3753    | 167    | 103   | ὅτε         | --       | --      | adv      | when, wheras                         |
| 3779    | 168    | 208   | οὕτως       | --       | --      | adv         | thus, so, in this manner    |
| 4143    | 169    | 68    | πλοῖον      | ου       | τό      | s2n         |  boat, ship                 |
| 4834    | 170    | 68    | ῥῆμα        | ατος     | τό      | s3n         |  word, saying; matter, thing    |
| 5037    | 171    | 215   | τε          | --       | --      | conj         |  and, so; τε...τε both...and |
| 5495        | 172    | 177   | χείρ        | χειρός   | ἡ       |  s3f        | hand , arm, finger, paw                  |
| 5590        | 173    | 103   | ψυχή        | ῆς       | ἡ       |   s3       | soul, life, self, vital spirit |
| 191         | 174    | 428   | ἀκούω       | --       | --      |  verb       | I hear, learn, obey, understand   |
| 991        | 175    | 133   | βλέπω       | --       | --      |   verb       |  I look at, see, consider                           |
| 2192        | 176    | 708   | ἔχω         | --       | --      |  verb        |  I have, hold; I am (intrans.)                  |
|  3089       | 177    | 42    | λύω         | --       | --      | verb         |   I untie, loose, set free, destroy    |
|  3551       | 178    | 194   | νόμος       | ου       | ὁ       |  s2m        |  usage, custom; law, principle     |
|  3699       | 179    | 82    | ὅπου        | --       | --      |  adv        |  where                                     |
|  4100       | 180    | 241   | πιστεύω     | --       | --      |  verb        |  to believe, have faith in     |

## 2022-07-07 Koine Greek Vocab--Mouncecards 181-200

| strongs | mounce | Freq. | lexeme      | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ----------- | -------- | ------- | --- | -------- |
| 4383        | 181    | 76    | πρόσωπον    | ου       | τό      | s2n    | face, appearance, presence         |
| 5119        | 182    | 160   | τότε        | --       | --      | adv    | then, when, at that time   |
| 5185        | 183    | 50    | τυφλός      | ἡ        | όν      |  adj   | blind, unseen, dark, closed         |
| 5479        | 184    | 59    | χαρά        | χαρᾶς    | ἡ       |  s1f   | joy, delight, exultation         |
|  25         | 185    | 143   | ἀγαπάω      | --       | --      | verb   |  I love, cherish, I brotherly love (agape)        |
| 1140        | 186    | 63    | δαιμόνιου   | ου       | τό      | s2n    |  demon, (pagan) god, evil spirit        |
| 2212        | 187    | 117   | ζητέω       | --       | --      | verb   |  to seek, to inquire, to strive          |
| 2564        | 188    | 148   | καλέω       | --       | --      | verb    |  I call, name; invite, summon        |
| 2980        | 189    | 296   | λαλέω       | --       | --      |  verb   |          |
|         | 190    | 318   | οἶδα        | --       | --      |     |          |
|         | 191    | 123   | ὅταν        | --       | --      |     |          |
|         | 192    | 55    | πλείων      | --       | --      |     |          |
|         | 193    | 86    | πληρόω      | --       | --      |     |          |
|         | 194    | 568   | ποιέω       | --       | --      |     |          |
|         | 195    | 70    | τηρέω       | --       | --      |     |          |
|         | 196    | 231   | ἀποκρίνομαι | --       | --      |     |          |
|         | 197    | 101   | δεῖ         | --       | --      |     |          |
|         | 198    | 210   | δύναμαι     | --       | --      |     |          |
|         | 199    | 634   | ἔρχομαι     | --       | --      |     |          |
|         | 200    | 61    | νύξ         | νυκτός   | ἡ       |     |          |

## 2022-07-08 Koine Greek Vocab--Mouncecards 201-220

| strongs | mounce | Freq. | lexeme    | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | --------- | -------- | ------- | --- | -------- |
|         | 201    | 153   | ὄστις     | ἤτις     | ὄτι     |     |          |
|         | 202    | 153   | πορεύομαι | --       | --      |     |          |
|         | 203    | 59    | συνάγω    | --       | --      |     |          |
|         | 204    | 94    | τόπος     | ου       | ὁ       |     |          |
|         | 205    | 504   | ὡς        | --       | --      |     |          |
|         | 206    | 115   | βασιλεύς  | έως      | ὁ       |     |          |
|         | 207    | 97    | γεννάω    | --       | --      |     |          |
|         | 208    | 140   | ζάω       | --       | --      |     |          |
|         | 209    | 43    | 'Ιουδάια  | ας       | ἡ       |     |          |
|         | 210    | 195   | 'Ιουδαῖος | αία      | αῖον    |     |          |
|         | 211    | 68    | 'Ισραήλ   | ὁ        | --      |     |          |
|         | 212    | 66    | καρπός    | οῦ       | ὁ       |     |          |
|         | 213    | 48    | μείζων    | --       | --      |     |          |
|         | 214    | 109   | ὁλος      | η        | ον      |     |          |
|         | 215    | 60    | προσκυνέω | --       | --      |     |          |
|         | 216    | 101   | αἴρω      | --       | --      |     |          |
|         | 217    | 74    | αποκτείνω | --       | --      |     |          |
|         | 218    | 132   | ἀποστέλλω | --       | --      |     |          |
|         | 219    | 77    | βαπτίζω   | --       | --      |     |          |
|         | 220    | 222   | γινώσκω   | --       | --      |     |          |

## 2022-07-09 Koine Greek Vocab--Mouncecards 221-240

| strongs | mounce | Freq. | lexeme    | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | --------- | -------- | ------- | --- | -------- |
|         | 221    | 50    | γλῶςςα    | ης       | ἡ       |     |          |
|         | 222    | 144   | ἐγείρω    | --       | --      |     |          |
|         | 223    | 81    | ἐκβάλλω   | --       | --      |     |          |
|         | 224    | 105   | ἐκεῖ      | --       | --      |     |          |
|         | 225    | 114   | κρίνω     | --       | --      |     |          |
|         | 226    | 142   | λαός      | οῦ       | ὁ       |     |          |
|         | 227    | 118   | μένω      | --       | --      |     |          |
|         | 228    | 454   | ὁραω      | --       | --      |     |          |
|         | 229    | 51    | σοπία     | ας       | ἡ       |     |          |
|         | 230    | 78    | στόμα     | ατος     | τό      |     |          |
|         | 231    | 106   | σῴζω      | --       | --      |     |          |
|         | 232    | 90    | ἀκολουτέω | --       | --      |     |          |
|         | 233    | 97    | διδάσκω   | --       | --      |     |          |
|         | 234    | 56    | ἐπερωτάω  | --       | --      |     |          |
|         | 235    | 63    | ἐρωτάω    | --       | --      |     |          |
|         | 236    | 208   | θέλω      | --       | --      |     |          |
|         | 237    | 95    | περιπατέω | --       | --      |     |          |
|         | 238    | 56    | συναγωγή  | ῆς       | ἡ       |     |          |
|         | 239    | 98    | φαρισαῖος | ου       | ὁ       |     |          |
|         | 240    | 54    | χρόνος    | ου       | ὁ       |     |          |

## 2022-07-10 Koine Greek Vocab--Mouncecards 241-260

| strongs | mounce | Freq. | lexeme      | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ----------- | -------- | ------- | --- | -------- |
|         | 241    | 111   | ἀποθνῄσκω   | --       | --      |     |          |
|         | 242    | 97    | ἄρτος       | ου       | ὁ       |     |          |
|         | 243    | 122   | βάλλω       | --       | --      |     |          |
|         | 244    | 250   | γῆ          | γῆς      | ἡ       |     |          |
|         | 245    | 669   | γίνομαι     | --       | --      |     |          |
|         | 246    | 194   | εἰσέρχομαι  | --       | --      |     |          |
|         | 247    | 218   | ἐξέρχομαι   | --       | --      |     |          |
|         | 248    | 93    | ἔτι         | --       | --      |     |          |
|         | 249    | 176   | εὑρίσκω     | --       | --      |     |          |
|         | 250    | 258   | λαμβάνω     | --       | --      |     |          |
|         | 251    | 87    | οὔτε        | --       | --      |     |          |
|         | 252    | 86    | προσέρχομαι | --       | --      |     |          |
|         | 253    | 85    | προσεύχομαι | --       | --      |     |          |
|         | 254    | 71    | πῦρ         | -ός      | τό      |     |          |
|         | 256    | 117   | ἄρχω        | --       | --      |     |          |
|         | 255    | 86    | ἀπέρχομαι   | --       | --      |     |          |
|         | 257    | 191   | γράφω       | --       | --      |     |          |
|         | 258    | 53    | διό         | --       | --      |     |          |
|         | 259    | 61    | δοξάζω      | --       | --      |     |          |
|         | 260    | 119   | δύναμις     | εως      | ἡ       |     |          |

## 2022-07-11 Koine Greek Vocab--Mouncecards 261-280

| strongs | mounce | Freq. | lexeme     | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ---------- | -------- | ------- | --- | -------- |
|         | 261    | 61    | χηρύσσω    | --       | --      |     |          |
|         | 262    | 73    | πίνω       | --       | --      |     |          |
|         | 263    | 67    | ἀγω        | --       | --      |     |          |
|         | 264    | 97    | αἷμα       | ματος    | τό      |     |          |
|         | 265    | 82    | ἕκαστος    | η        | ον      |     |          |
|         | 266    | 60    | ἱμάτιον    | ου       | τό      |     |          |
|         | 267    | 63    | ὄρος       | ὄρους    | τό      |     |          |
|         | 268    | 79    | ὑπάγω      | --       | --      |     |          |
|         | 269    | 95    | φοβέομαι   | --       | --      |     |          |
|         | 270    | 74    | χαίρω      | --       | --      |     |          |
|         | 271    | 70    | αἰτέω      | --       | --      |     |          |
|         | 272    | 81    | μᾶλλον     | --       | --      |     |          |
|         | 273    | 76    | μαρτυρέω   | --       | --      |     |          |
|         | 274    | 82    | ἀναβαίνω   | --       | --      |     |          |
|         | 275    | 122   | ἀρχιερεύς  | έως      | ὁ       |     |          |
|         | 276    | 54    | δεξιός     | ιά       | ιόν     |     |          |
|         | 277    | 135   | δύο        | --       | --      |     |          |
|         | 278    | 99    | ἕτερος     | α        | ον      |     |          |
|         | 279    | 54    | εὐαγγελίζω | --       | --      |     |          |
|         | 280    | 58    | θεωρέω     | --       | --      |     |          |

## 🧡🚶🚶🥁 2022-07-12 Koine Greek Vocab--Mouncecards 281-300

| strongs | mounce | Freq. | lexeme     | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ---------- | -------- | ------- | --- | -------- |
|         | 281    | 62    | Ἱεροσόλυμα | τά       | ή       |     |          |
|         | 282    | 91    | κάθημαι    | --       | --      |     |          |
|         | 283    | 81    | καταβαίνω  | --       | --      |     |          |
|         | 284    | 24    | οὗ         | --       | --      |     |          |
|         | 285    | 109   | παρακαλέω  | --       | --      |     |          |
|         | 286    | 52    | πείθω      | --       | --      |     |          |
|         | 287    | 68    | τρεῖς      | τρία     | --      |     |          |
|         | 288    | 59    | ἀσπάζομαι  | --       | --      |     |          |
|         | 289    | 63    | γραμματεύς | έως      | ὁ       |     |          |
|         | 290    | 43    | έφή        | --       | --      |     |          |
|         | 291    | 71    | ἱερόν      | οῦ       | τό      |     |          |
|         | 292    | 56    | κράζω      | --       | --      |     |          |
|         | 293    | 54    | οὐχί       | --       | --      |     |          |
|         | 294    | 52    | παιδίον    | ου       | τό      |     |          |
|         | 295    | 52    | σπείρω     | --       | --      |     |          |
|         | 296    | 56    | δέξομαι    | --       | --      |     |          |
|         | 297    | 62    | δοκέω      | --       | --      |     |          |
|         | 298    | 158   | ἐσθίω      | --       | --      |     |          |
|         | 299    | 79    | πέμπω      | --       | --      |     |          |
|         | 300    | 66    | φέρω       | --       | --      |     |          |

## 2022-07-13 Koine Greek Vocab--Mouncecards 301-320

| strongs | mounce | Freq. | lexeme      | genitive | article  | pos | gloss_en |
| ------- | ------ | ----- | ----------- | -------- | -------- | --- | -------- |
|         | 301    | 56    | μηδέ        | --       | --       |     |          |
|         | 302    | 66    | πρεσβύτερος | α        | ον       |     |          |
|         | 303    | 59    | λίθος       | ου       | ὁ        |     |          |
|         | 304    | 57    | τοιοῦτος    | αύτη     | ούτον    |     |          |
|         | 305    | 79    | δίκαιος     | αία      | αιον     |     |          |
|         | 306    | 109   | μέλλω       | --       | --       |     |          |
|         | 307    | 90    | ἀπόλλυμι    | --       | --       |     |          |
|         | 308    | 66    | ἀπολύω      | --       | --       |     |          |
|         | 309    | 65    | εἴτε        | --       | --       |     |          |
|         | 310    | 415   | δίδωμι      | --       | --       |     |          |
|         | 311    | 162   | ἔθνος       | ους      | τό       |     |          |
|         | 312    | 55    | λοιπός      | ή        | όν       |     |          |
|         | 313    | 80    | Μωϋσῆς      | έως      | ὁ        |     |          |
|         | 314    | 119   | παραδίδωμι  | --       | --       |     |          |
|         | 315    | 90    | πίπτω       | --       | --       |     |          |
|         | 316    | 60    | ὑπάχω       | --       | --       |     |          |
|         | 317    | 108   | ἀνίστημι    | --       | --       |     |          |
|         | 318    | 77    | ἀνοίγω      | --       | --       |     |          |
|         | 319    | 143   | ἀφίημι      | --       | --       |     |          |
|         | 320    | 33    | δεικνύω     | --       | δείκνυμι |     |          |

## 🇫🇷🇫🇷 2022-07-14 Koine Greek Vocab--Mouncecards 321-340

| strongs | mounce | Freq. | lexeme      | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ----------- | -------- | ------- | --- | -------- |
|         | 321    | 114   | ἴδιος       | α        | ον      |     |          |
|         | 322    | 154   | ἵστημι      | --       | --      |     |          |
|         | 323    | 58    | μέσος       | η        | ον      |     |          |
|         | 324    | 100   | τίθημι      | --       | --      |     |          |
|         | 325    | 66    | φημί        | --       | --      |     |          |
|         | 326    | 49    | ἀρα         | --       | --      |     |          |
|         | 327    | 49    | ἄχρι        | ἄχρις    | --      |     |          |
|         | 328    | 49    | ἔτος        | ους      | τό      |     |          |
|         | 329    | 49    | παραλαμβάνω | --       | --      |     |          |
|         | 330    | 49    | φανερόω     | --       | --      |     |          |
|         | 331    | 49    | χρεία       | ας       | ἡ       |     |          |
|         | 332    | 48    | ἀποδίδωμι   | --       | --      |     |          |
|         | 333    | 48    | ἔμπροσθεν   | --       | --      |     |          |
|         | 334    | 48    | ἔρημος      | ον       | --      |     |          |
|         | 335    | 48    | ποῦ         | --       | --      |     |          |
|         | 336    | 47    | ἀμρτωλός    | ον       | ??      |     |          |
|         | 337    | 47    | κρατέω      | --       | --      |     |          |
|         | 338    | 47    | κρίσις      | εως      | ἡ       |     |          |
|         | 339    | 47    | οὐκέτι      | --       | --      |     |          |
|         | 340    | 47    | πρό         | --       | --      |     |          |

## 2022-07-15 Koine Greek Vocab--Mouncecards 341-360|

| strongs | mounce | Freq. | lexeme     | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ---------- | -------- | ------- | --- | -------- |
|         | 341    | 47    | προσφέρω   | --       | --      |     |          |
|         | 342    | 47    | φόβος      | ου       | ὁ       |     |          |
|         | 343    | 47    | φυλακή     | ῆς       | ἡ       |     |          |
|         | 344    | 46    | θηρίον     | ου       | τό      |     |          |
|         | 345    | 46    | καθίζω     | --       | --      |     |          |
|         | 346    | 46    | μικρός     | ά        | όν      |     |          |
|         | 347    | 46    | οὐναί      | --       | --      |     |          |
|         | 348    | 46    | σταυρόω    | --       | --      |     |          |
|         | 349    | 46    | σωτηρία    | ας       | ἡ       |     |          |
|         | 350    | 45    | ἀπαγγέλλω  | --       | --      |     |          |
|         | 351    | 45    | διώκω      | --       | --      |     |          |
|         | 352    | 45    | θλῖψις     | εως      | ἡ       |     |          |
|         | 353    | 45    | ναός       | οῦ       | ὁ       |     |          |
|         | 354    | 45    | ὅμοιος     | οία      | οιον    |     |          |
|         | 355    | 44    | ἐπιγινώσκω | --       | --      |     |          |
|         | 356    | 44    | Ἰούδας     | α        | ὁ       |     |          |
|         | 357    | 44    | κατοικέω   | --       | --      |     |          |
|         | 358    | 43    | ἀμαρτάνω   | --       | --      |     |          |
|         | 359    | 43    | γενεά      | ᾶς       | ᾶ       | ης  |          |
|         | 360    | 43    | δεύτερος   | α        | ον      |     |          |

## 2022-07-16 Koine Greek Vocab--Mouncecards 361-380

| strongs | mounce | Freq. | lexeme    | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | --------- | -------- | ------- | --- | -------- |
|         | 361    | 43    | δέω       | --       | --      |     |          |
|         | 362    | 43    | διέρχομαι | --       | --      |     |          |
|         | 363    | 43    | 'Ηρῴδης   | ου       | ὁ       |     |          |
|         | 364    | 43    | θαυμάζω   | --       | --      |     |          |
|         | 365    | 43    | θεραπεύω  | --       | --      |     |          |
|         | 366    | 43    | σεαυτοῦ   | --       | --      |     |          |
|         | 367    | 43    | σπέρμα    | ατος     | τό      |     |          |
|         | 368    | 43    | φωνέω     | --       | --      |     |          |
|         | 369    | 42    | ἀνάστασις | --       | --      |     |          |
|         | 370    | 42    | ἐγγίζω    | --       | --      |     |          |
|         | 371    | 42    | Ἰάκωβος   | ου       | ὁ       |     |          |
|         | 372    | 42    | καινός    | ή        | όν      |     |          |
|         | 373    | 42    | μέπος     | ους      | τό      |     |          |
|         | 374    | 42    | πάσχω     | --       | --      |     |          |
|         | 375    | 41    | ἄξιος     | α        | ον      |     |          |
|         | 376    | 41    | ἐργάζομαι | --       | --      |     |          |
|         | 377    | 41    | εὐλογέω   | --       | --      |     |          |
|         | 378    | 41    | πάντοτε   | --       | --      |     |          |
|         | 379    | 41    | παρίστημι | --       | --      |     |          |
|         | 380    | 41    | σήμερον   | --       | --      |     |          |

## 2022-07-17 Koine Greek Vocab--Mouncecards 381-400

| strongs | mounce | Freq. | lexeme     | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ---------- | -------- | ------- | --- | -------- |
|         | 381    | 41    | τέσσερες   | α        | --      |     |          |
|         | 382    | 41    | τιμή       | ῆς       | ἡ       |     |          |
|         | 383    | 41    | χωρίς      | --       | --      |     |          |
|         | 384    | 40    | ἑτοιμάζω   | --       | --      |     |          |
|         | 385    | 40    | κλαίω      | --       | --      |     |          |
|         | 386    | 40    | λογίζομαι  | --       | --      |     |          |
|         | 387    | 40    | μισέω      | --       | --      |     |          |
|         | 388    | 40    | μνημεῖον   | ου       | τό      |     |          |
|         | 389    | 40    | οἰκοδομέω  | --       | --      |     |          |
|         | 390    | 40    | ὀλίγος     | η        | ον      |     |          |
|         | 391    | 40    | τέλος      | ους      | τό      |     |          |
|         | 392    | 39    | ἅπτω       | --       | --      |     |          |
|         | 393    | 39    | δικαιόω    | --       | --      |     |          |
|         | 394    | 39    | ἐπιτίθημι  | --       | --      |     |          |
|         | 395    | 39    | θύρα       | ας       | ἡ       |     |          |
|         | 396    | 39    | ἱκανός     | ή        | όν      |     |          |
|         | 397    | 39    | περισστεύω | --       | --      |     |          |
|         | 398    | 39    | πλανάω     | --       | --      |     |          |
|         | 399    | 39    | πράσσω     | --       | --      |     |          |
|         | 400    | 39    | πρόβατον   | ου       | τό      |     |          |

## 2022-07-18 Koine Greek Vocab--Mouncecards 401-420

| strongs | mounce | Freq. | lexeme      | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | ----------- | -------- | ------- | --- | -------- |
|         | 401    | 38    | ἐπιθυμία    | ας       | ἡ       |     |          |
|         | 402    | 38    | εὐχαριστέω  | --       | --      |     |          |
|         | 403    | 38    | πειράζω     | --       | --      |     |          |
|         | 404    | 38    | πέντε       | --       | --      |     |          |
|         | 405    | 38    | ὑποτάσσω    | --       | --      |     |          |
|         | 406    | 37    | ἄρχων       | οντος    | ὁ       |     |          |
|         | 407    | 37    | βούλομαι    | --       | --      |     |          |
|         | 408    | 37    | διάβολος    | ον       | --      |     |          |
|         | 409    | 37    | διακονέω    | --       | --      |     |          |
|         | 410    | 37    | ἐκεῖθεν     | --       | --      |     |          |
|         | 411    | 37    | ἐμαυτον     | ῆς       | --      |     |          |
|         | 412    | 37    | καλῶ        | --       | --      |     |          |
|         | 413    | 37    | καυχάομαι   | --       | --      |     |          |
|         | 414    | 37    | μαρτυρία    | ας       | ἡ       |     |          |
|         | 415    | 37    | παραγίνομαι | --       | --      |     |          |
|         | 416    | 37    | ἀγρός       | οῦ       | ὁ       |     |          |
|         | 417    | 36    | ἅρτι        | --       | --      |     |          |
|         | 418    | 36    | ἐπιστρέφω   | --       | --      |     |          |
|         | 419    | 36    | εὑθέως      | --       | --      |     |          |
|         | 420    | 36    | ὀργή        | ῆς       | ἡ       |     |          |

## 🌞40.3°C🔥 2022-07-19 Koine Greek Vocab--Mouncecards 421-440

| strongs | mounce | Freq. | lexeme    | genitive | article | pos | gloss_en |
| ------- | ------ | ----- | --------- | -------- | ------- | --- | -------- |
|         | 421    | 36    | οὖς       | ὠτός     | τό      |     |          |
|         | 422    | 36    | περιτομή  | ῆς       | η       |     |          |
|         | 423    | 36    | προσευκξή | ῆς       | ἡ       |     |          |
|         | 424    | 36    | σατανᾶς   | ᾶ        | ὁ       |     |          |
|         | 425    | 36    | πίλιππος  | ου       | ὁ       |     |          |
|         | 426    | 36    | ὥστερ     | --       | --      |     |          |
|         | 427    | 35    | Ἰωσή      | --       | ὁ       |     |          |
|         | 428    | 35    | μάρτυς    | μάρτυρος | ὁ       |     |          |
|         | 429    | 35    | ὀπίσω     | --       | --      |     |          |
|         | 430    | 35    | ὀφείλω    | --       | --      |     |          |
|         | 431    | 35    | ὑποστρέφω | --       | --      |     |          |
|         | 432    | 34    | ἁπας      | ασα      | αν      |     |          |
|         | 433    | 34    | βιβλίον   | ου       | τό      |     |          |
|         | 434    | 34    | βλασφημέω | --       | --      |     |          |
|         | 435    | 34    | διακονία  | ας       | ἡ       |     |          |
|         | 436    | 34    | μέλος     | ους      | τό      |     |          |
|         | 437    | 34    | μετανοέω  | --       | --      |     |          |
|         | 438    | 34    | μήτε      | --       | --      |     |          |
|         | 439    | 34    | οἶνος     | ου       | ὁ       |     |          |
|         | 440    | 34    | πτωχός    | ή        | όν      |     |          |

## 2022-07-20 Koine Greek Vocab--Mouncecards 441-460

| strongs | mounce | Freq.       | lexeme | genitive | article | pos | gloss_en |
| ------- | ------ | ----------- | ------ | -------- | ------- | --- | -------- |
| 441     | 33     | ἀρνέομαι    | --     | --       |         |     |          |
| 442     | 33     | ἀσθενέω     | --     | --       |         |     |          |
| 443     | 33     | διαθήκη     | ης     | ἡ        |         |     |          |
| 444     | 33     | ἐκπορεύομαι | --     | --       |         |     |          |
| 445     | 33     | ναί         | --     | --       |         |     |          |
| 446     | 33     | ποῖος       | --     | --       |         |     |          |
| 447     | 33     | ἀκάθαρτος   | --     | ον       |         |     |          |
| 448     | 32     | ἀναγινώςκω  | --     | --       |         |     |          |
| 449     | 32     | δυνατός     | ή      | όν       |         |     |          |
| 450     | 32     | ἐχθός       | ά      | όν       |         |     |          |
| 451     | 32     | ἕλιος       | ου     | ὁ        |         |     |          |
| 452     | 32     | παρανγγέλλω | --     | --       |         |     |          |
| 453     | 32     | ὑπομονή     | ῆς     | ἡ        |         |     |          |
| 454     | 31     | ἄνεμος      | ου     | ὁ        |         |     |          |
| 455     | 31     | ἐγγύς       | --     | --       |         |     |          |
| 456     | 31     | ἐλπίζω      | --     | --       |         |     |          |
| 457     | 31     | ἔξεστιν     | --     | --       |         |     |          |
| 458     | 31     | ἰερεύς      | έως    | ὁ        |         |     |          |
| 459     | 31     | καθαρίζω    | --     | --       |         |     |          |
| 460     | 31     | ναρρησία    | ας     | ἡ        |         |     |          |

## 2022-07-21 Koine Greek Vocab--Mouncecards 461-480

| strongs | mounce | Freq.      | lexeme | genitive | article | pos | gloss_en |
| ------- | ------ | ---------- | ------ | -------- | ------- | --- | -------- |
|         | 461    | πλῆθος     | ους    | τό       |         |     |          |
|         | 463    | ποτήριον   | ου     | τό       |         |     |          |
|         | 462    | πλήν       | --     | --       |         |     |          |
|         | 464    | σκότος     | ους    | τό       |         |     |          |
|         | 465    | φαίνω      | --     | --       |         |     |          |
|         | 466    | φυλάσσω    | --     | --       |         |     |          |
|         | 467    | φυλή       | ῆς     | ή        |         |     |          |
|         | 468    | ἀγοράζω    | --     | --       |         |     |          |
|         | 469    | ἀρνίον     | ου     | τό       |         |     |          |
|         | 470    | διδαχή     | ῆς ἡ   |          |         |     |          |
|         | 471    | ἐπικαλέω   | --     | --       |         |     |          |
|         | 472    | ὁμοίως     | --     | --       |         |     |          |
|         | 473    | συνείδησις | εως    | ἡ        |         |     |          |
|         | 474    | συνέρχομαι | --     | --       |         |     |          |
|         | 475    | γνῶσις     | εως    | ἡ        |         |     |          |
|         | 476    | διάκονος   | ου     | ὁ;ἡ      |         |     |          |
|         | 477    | ἐπιτιμάω   | --     | --       |         |     |          |
|         | 478    | Ἠλίας      | ου     | ὁ        |         |     |          |
|         | 479    | ἰσχυρός    | ά      | όν       |         |     |          |
|         | 480    | Καῖσαρ     | ος     | ὁ        |         |     |          |

## 2022-07-22 Koine Greek Vocab--Mouncecards 481-500

| strongs | mounce | Freq.      | lexeme | genitive | article | pos | gloss_en |
| ------- | ------ | ---------- | ------ | -------- | ------- | --- | -------- |
|         | 481    | μάχαιρα    | ης     | ἡ        |         |     |          |
|         | 482    | μισθός     | οῦ     | ὁ        |         |     |          |
|         | 483    | παράκλησις | εως    | ἡ        |         |     |          |
|         | 484    | παρέρχομαι | --     | --       |         |     |          |
|         | 485    | πάσχα      | --     | τό       |         |     |          |
|         | 486    | πόθεν      | --     | --       |         |     |          |
|         | 487    | ποτέ       | --     | --       |         |     |          |
|         | 488    | προσκαλέω  | --     | --       |         |     |          |
|         | 489    | σκανδαλίζω | --     | --       |         |     |          |
|         | 490    | φεύγω      | --     | --       |         |     |          |
|         | 491    | φίλος      | η      | ον       |         |     |          |
|         | 492    | ἁγιάζω     | --     | --       |         |     |          |
|         | 493    | ἀδικέω     | --     | --       |         |     |          |
|         | 494    | ἀληθινός   | ή      | όν       |         |     |          |
|         | 495    | βαρναβᾶς   | ᾶ      | ὁ        |         |     |          |
|         | 496    | γαμέω      | --     | --       |         |     |          |
|         | 497    | ἐλεέω      | --     | --       |         |     |          |
|         | 498    | ἡγέομαι    | --     | --       |         |     |          |
|         | 499    | θυγάτηρ    | τρος   | ἡ        |         |     |          |
|         | 500    | θυσία      | ας     | ἡ        |         |     |          |

**εἰ** `σ/ς` `έρ`  χομαι, εἰσέρχῃ (εἰσέρχει), εἰσέρχεται || εἰσερχόμεθᾰ, εἰσέρχεσθε, εἰσέρχονται

ομαι, ῃ(ει), εται || όμεθᾰ,εσθε, ονται

[s5038] τὸ τεῖχος, τεχους-- mound, wall, fortification
