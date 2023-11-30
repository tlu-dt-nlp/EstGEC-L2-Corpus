# Estonian L2 Grammatical Error Correction Corpus (EstGEC-L2)
### The subset of Estonian Grammatical Error Correction Corpus (EstGEC) that contains L2 learner writings error-annotated in the M2 format.

This subcorpus currently consists of 263 texts and 3,790 sentences retrieved from the [Estonian Interlanguage Corpus](https://elle.tlu.ee/tools) compiled at the Tallinn University. The texts include narrative/descriptive and argumentative writings as well as informal and formal letters representing various proficiency levels. EstGEC-L2 material has been divided into a test and development set that can be used for evaluating and improving Estonian automated correction tools. The test set comprises 2,029 and the dev set 1,761 sentences, distributed between the proficiency levels as follows:
* A2 – 937 (495 in test set);
* B1 – 963 (504 in test set);
* B2 – 1,091 (534 in test set);
* C1 – 796 (495 in test set).

Previously, the texts had been manually error-tagged in the CoNLL-U format,indicating the error type, scope, and correction in the field for miscellaneous token attributes. The annotation has been converted to the M2 format (the conversion script can be found [here](https://github.com/tlu-dt-nlp/m2-preprocessing)) using an adapted version of the [ERRANT](https://github.com/chrisjbryant/errant) tagset. Whereas the previous format was limited to one error annotation per sentence, up to two new annotation versions have been added. Considering the two-phase annotation, each text has been reviewed by three expert annotators.

There are 12 main and 18 combined error types in the error classification (see tables 1 and 2). The prefix indicates whether a word, phrase or punctuation mark should be replaced ('R:'), is missing ('M:') or unnecessary ('U:'). In our tagset, we do not distinguish the part of speech (POS) of the replaced, added or deleted word. For example, all word choice errors are indicated by the tag 'R:LEX'. This has helped to reduce the complexity of the error categorization, while allowing us to classify all errors and avoid the 'OTHER' tag. Since the edit types often overlap (e.g., spelling errors co-occur with inflectional form and word choice errors), there are numerous edit and POS combinations, and the POS of the original and correct word can differ. We differentiate between nominal (noun, adjective, pronoun and numeral) and verb form errors, including case, number, agreement, tense and mood errors.

Another important difference to the English M2 annotation is that we allow overlapping error scope if a token-level error occurs within a word order error, e.g., one of the words contains a spelling error. Therefore, it is possible to detect token-level corrections even if word order has not been corrected. Furthermore, orthography errors have been divided into capitalization and whitespace errors, 

**Table 1.** Main error types
| Error tag | Meaning | Example |
|:--------------|:-------------|:--------------|
| R:SPELL | Spelling error | _soobib_ -> _sobib_ |
| R:CASE | Capitalization error | _Juuli_ -> _juuli_ |
| R:WS | Whitespace error | _igalpool_ -> _igal pool_ |
| R:NOM:FORM | Nominal form error | _kallis_ -> _kallid_ (Sing -> Plur) |
| R:VERB:FORM | Verb form error | _tegeleb_ -> _tegeles_ (Pres -> Past) |
| R:LEX | Word choice error | _ilusasti_ -> _ilus_ (ADV -> ADJ) |
| R:PUNCT | Punctuation choice error | _Kohtumiseni._ -> _Kohtumiseni!_ |
| R:WO | Word order error | _üldse polnud_ -> _polnud üldse_ |
| M:LEX | Missing word(s) | _See väga ilus linn_ -> _See on väga ilus linn_ |
| U:LEX | Unnecessary word(s) | _auto välimus on punane_ -> _auto on punane_ |
| U:PUNCT | Unnecessary punctuation | _laupäeval, kell 10_ -> _laupäeval kell 10_ |

**Table 2.** Combined error types
| Error tag | Meaning | Example |
|:--------------|:-------------|:--------------|
| R:SPELL:CASE | Spelling and capitalization error | _Vannalinnas_ -> _vanalinnas_ |
| R:WS:SPELL | Whitespace and spelling error | _liimik koht_ -> _lemmikkoht_ |
| R:WS:CASE | Whitespace and capitalization<br />error | _Kontserdi majas_ -> _kontserdimajas_ |
| R:WS:NOM:FORM | Whitespace and nominal form<br />error | _kogupäev_ -> _kogu päeva_ (Nom -> Gen) |
| R:WS:NOM:FORM:SPELL | Whitespace, nominal form and<br />spelling error | _politika uudiseid_ -> _poliitikauudised_<br />(Par -> Nom) |
| R:WS:NOM:FORM:CASE | Whitespace, nominal form and<br />capitalization error | _cv online_ -> _CV-Online’i_ (Nom -> Gen) |
| R:NOM:FORM:SPELL| Nominal form and spelling error | _ekskursioni_ ~ _ekskursiooni_ -><br />_ekskursioonile_ (Gen/Par -> All)|
| R:NOM:FORM:CASE | Nominal form and capitalization<br />error | _tartu_ -> _Tartut_ (Nom -> Par) |
| R:NOM:FORM:SPELL:CASE | Nominal form, spelling and<br />capitalization error | _Sobrad_ ~ _Sõbrad_ -> _sõpradega_<br />(Nom -> Com) |
| R:VERB:FORM:SPELL | Verb form and spelling error | _kaisin_ ~ _käisin_ -> _käin_ (Past -> Pres) |
| R:VERB:FORM:SPELL:CASE | Verb form, spelling and<br />capitalization error | _jstume_ ~ _istume_ -> _Istusime_<br />(Pres -> Past) |
| R:LEX:SPELL | Word choice and spelling error | _laksin_ ~ _läksin_ -> _käisin_ |
| R:LEX:CASE | Word choice and capitalization<br />error | _võimalikult_ -> _Võimalik_ (ADV -> ADJ) |
| R:LEX:NOM:FORM | Word choice and nominal form<br />error | _muusikaid_ -> _muusikastiilid_<br />(Par -> Nom) |
| R:LEX:VERB:FORM | Word choice and verb form<br />error | _(mina) oli_ -> _(mina) käisin_<br />(3rd person -> 1st person) |
| R:LEX:WO | Word choice error affects<br />word order | _läbi interneti_ -> _interneti kaudu_ |
| R:LEX:WS | Word choice and whitespace<br />error | _oma teist_ -> _teineteist_ |
| R:WO:NOM:FORM | Word order error affects the<br />choice of nominal form | _pealinn Islandil_ -> _Islandi pealinn_<br />(Ade -> Gen) |

## References

* The dataset has been used to evaluate the [GEC](https://koodivaramu.eesti.ee/tartunlp/corrector) toolkit developed in collaboration by the language technology groups of the University of Tartu and the Tallinn University. The L1 subset of the corpus is being annotated at the University of Tartu.
* The M2 Scorer adapted for the EstGEC corpus can be found [here](https://github.com/TartuNLP/estgec/tree/c3e7bba56f9b20c80f4a63d0e1d5abc17f96aaf9/M2_scorer_est).
* Conference presentations:
  * [8th Estonian Digital Humanities Conference, October 5-7, 2022, Tallinn](https://dh.org.ee/wp-content/uploads/sites/3/2022/10/Allkivi_Metsoja_et_al_slides_DH2022.pdf)
  * [20th Annual Conference of Applied Linguistics, April 27-28, 2023, Tallinn](https://www.rakenduslingvistika.ee/wp-content/uploads/2023/05/02_Allkivi-Metsoja_jt_Veamargendusega_korpus_grammatikakontrollija.pdf) (in Estonian)
