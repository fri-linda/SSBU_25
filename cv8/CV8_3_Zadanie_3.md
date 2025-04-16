## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

Hypotéza H0 (príbuzenská hypotéza):
Testované osoby sú biologicky príbuzné dieťaťu, sú to jeho strýkovia.
Hypotéza HA (nepríbuzenská hypotéza):
Testované osoby nie sú biologicky príbuzné dieťaťu, nie sú to jeho strýkovia.

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

LR = 7042640
W = 7042640 / 7042641 = 0.999999858

Hypotéza H0 – že testované osoby sú biologickými strýkami dieťaťa – je silne podporená genetickými údajmi, 
pričom vypočítané LR (v poriadku miliónov) a následná pravdepodobnosť blížiaca sa 100 % dokazujú jej správnosť.

Hypotéza HA – že medzi osobami neexistuje biologický príbuzenský vzťah – je na základe týchto výsledkov vyvrátená.