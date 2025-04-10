## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

#TODO

- H0 - muž je otcom dcéry a strýkovia sú príbuzné
- HA - muž nie je otcom dcéry a preto strýkovia nie sú príbuzné

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

#TODO

- LR - 7.04264e+006
- W - 7.04264e+006 / (7.04264e+006 + 1) ~ 0.999999871
- H0 = 99.9999871 %
- HA = 100 - H0 = 0.0000129 %

- prijímame H0, pretože pravdepodobnosť je takmer 100%. Muž je otcom dcéry.