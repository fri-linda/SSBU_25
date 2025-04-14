## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="../cv8/data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0: Otcom dcéry je muž a dcéra je príbuzná so strýkami.

H1: Otcom dcéry nie je muž, z toho dôvodu nie je dcéra príbuzná so strýkami.

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

W = P(H0|údaje) = LR/(LR+1) (LR z výpočtu FamLinkX)
LR: 7.043e+006 (0.99999986)
W≈0.99999986 
P(H0) = 99,999%
P(H1) = 0.001%
Hypotéza H0 je výrazne pravdepodobnejšia (takmer 100%), preto môžeme prijať hypotézu H0 a aj 
keď nepotvrdzuje otcovstvo na 100%, môžeme tvrdiť, že dcéra je s vysokou pravdepodobnosťou potomkom muža, a teda neterou 2 stýkov.