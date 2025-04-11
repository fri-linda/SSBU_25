## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0-Predpokladaný muž je biologickým otcom dievčaťa.
Matka a testovaný muž sú rodičmi dcéry.
Dvaja muži v datasete sú bratia testovaného muža, teda strýkovia dcéry.

HA-Predpokladaný muž nie je biologickým otcom dievčaťa.
Otcovstvo je pripísané neznámemu mužovi.
Testovaný muž a jeho bratia nie sú priamymi príbuznými dcéry.

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

H0-Dieťa je neterou dvoch strýkov, LR = 7 043 000, W = 99.999986%
HA-Dieťa nie je neterou dvoch strýkov, LR = 1, W = 0.000014%

Na základe výpočtu likelihood ratio (LR) a následnej pravdepodobnosti (W) je hypotéza H0 výrazne pravdepodobnejšia než alternatívna hypotéza HA. Aj keď genetická analýza nedáva absolútne potvrdenie (100%), môžeme s veľmi vysokou mierou istoty tvrdiť, že dieťa je neterou uvedených strýkov, a teda biologická väzba existuje. Hypotézu H0 prijímame.