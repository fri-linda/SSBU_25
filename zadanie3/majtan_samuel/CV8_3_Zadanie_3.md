## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0:
- muz zo vzorky je biologickym otcom dcery

H1:
- muz zo vzorky nie je biologickym otcom dcery

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

H0 (pedigree 1):
- muz je biologickym otcom dietata
- LR (likelihood ratio): 7 043 000
- Pravdepodobnost (W): 0.99999986 (≈ 99.999986 %)

H1 (pedigree 2):
- muz nie je biologickym otcom dietata
Pravdepodobnost (W): 0.000000142 (≈ 0.0000142 %)

Takze mozme povedat na zaver, ze podla LR = 7 043 000 a pravdepodobnosti W = 99.999986% je s vysokou pravdepodobnostou muz biologickym otcom dietata. Alternativnu hypotezu H1 zamietame, kedze je extremne nepravdepodobna.