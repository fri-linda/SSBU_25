## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

Hypotéza H₁:
Muž, ktorého bratia (strýkovia) boli testovaní, je biologickým otcom dcéry.
Hypotéza H₂:
Tento muž nie je biologickým otcom dcéry a skutočným otcom je niekto iný, nepríbuzný muž.

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

LR vysoko nad 1: Výsledky ukazujú, že je omnoho pravdepodobnejšie, že DNA profily boli získané podľa hypotézy H₁, teda že muž je otcom.
Ak pred testom predpokladáme rovnakú pravdepodobnosť oboch hypotéz (tj. 50 %), výsledná (posteriorná = W) pravdepodobnosť otcovstva, po vypočítaní bude prakticky 100 %.
Napríklad pre LR ≈ 7.04 × 10⁶ a p=0.5:
W = (7 040 000 * 0,5) / (7 040 000 * 0,5 + 0,5) == 99,99%

Na základe vysokých hodnôt LR a následného výpočtu veľmi vysokej posteriornej pravdepodobnosti (prakticky 100 %) môžeme jednoznačne konštatovať:
Hypotéza H₁ („testovaný muž je biologickým otcom dcéry“) je jednoznačne podporená.
Hypotéza H₂ („testovaný muž nie je otcom“) je vyvrátená.
Rozhodnutie:
Nepriamy test otcovstva cez analýzu DNA strýkov jasne potvrdzuje, že daný muž je biologickým otcom dcéry.