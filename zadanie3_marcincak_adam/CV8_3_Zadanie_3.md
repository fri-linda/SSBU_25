## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H(0) - strykovia sú príbuzní dieťaťu
H(1) - strýkovia nie sú príbuzní dieťaťu

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

LR[H(0)] => 7 042 640
W[H(0)] = 0.99999

LR[H(1)] => 1.419922e-007 -> 0.0000001419922
W[H(1)] = 1.41992179838218e-7

Dieta je príbuzné strýkom. H(0) nezamietam => otec je s veľkou pravdepodobnosťou autorom dieťaťa.

