## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

#TODO
H0 (Pedigree 1): Tretí brat (neprítomný muž) je biologickým otcom dieťaťa.
H1 (Pedigree 2): Tretí brat nie je otcom dieťaťa.



### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**
Pedigree	lnLikelihood	LR versus pedigree 2 (W)
Pedigree 1	-84.9882	7.043e+006 (0.99999986)
Pedigree 2	-100.7557	1 (1.419922e-007)
Z výsledkov analýzy vyplýva, že hypotéza H₀ (Pedigree 1), podľa ktorej je muž biologickým otcom dieťaťa, je viac ako 7 miliónkrát pravdepodobnejšia ako alternatívna hypotéza H₁ (Pedigree 2), ktorá otcovstvo vylučuje.

Na základe výpočtu:
W = LR / (LR + 1) = 7.043 × 10⁶ / (7.043 × 10⁶ + 1) ≈ 0.99999986

To znamená, že posteriorná pravdepodobnosť hypotézy H₀ je približne 99.999986%, čo predstavuje extrémne silný dôkaz v prospech otcovstva.
Aj keď sa v genetických analýzach nikdy nepotvrdzuje vzťah na absolútnych 100%, môžeme na základe týchto výsledkov s veľmi vysokou pravdepodobnosťou potvrdiť, že muž je otcom dieťaťa, a teda dievča je neterou oboch strýkov.