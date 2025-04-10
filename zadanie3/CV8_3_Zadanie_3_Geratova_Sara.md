## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H(0) = predpokladame, ze muz je otcom dietata a brat oboch stykov je otcom dietata
H(A) = predpokladame, ze muz nie je otcom dietata a brat oboch stykov nie je otcom dietata

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

- LR pre H(0) = 7.04264e+006
- LR pre H(A) = 7.76989e+006
-
- W = P(H0|údaje) = LR/(LR+1)
- W pre H(0) = 0.99901
- W pre H(A) = 0.00099

Zaver analýzy: 
- S pravdepodobnostou 99,901% je muz otcom dietata a brat oboch stykov je otcom dietata
- S pravdepodobnostou 0,00099% nie je muz otcom dietata a brat oboch stykov nie je otcom dietata