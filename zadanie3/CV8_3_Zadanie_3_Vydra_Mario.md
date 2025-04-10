## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0 - muž je biologickým otcom dcéry (dieťa so strýkami sú príbuzní)

HA - muž nie je biologickým otcom dcéry (dieťa so strýkami nie sú príbuzní)

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

LR (H0) = 7042640

W(H0 | údaje) = 7042640 / (7042640 + 1) = 0.99999986 -> 99.999986%

W(HA | údaje) = 1 - 0.99999986 = 0.00000014 -> 0.000014%

Záver: Prijímame prvú hypotézu H0. Môžeme povedať, že s 99.999986% pravdepodobnosťou, daný muž je biologickým otcom dcéry (dieťa so strýkami sú príbuzní).