# Estonian L2 learner GEC corpus
Estonian GEC test and development corpus that contains L2 learner texts error-annotated in the M2 format.


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
| M:LEX | Missing word | _See väga ilus linn_ -> _See on väga ilus linn_ |
| U:LEX | Unnecessary word | _auto välimus on punane_ -> _auto on punane_ |
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
