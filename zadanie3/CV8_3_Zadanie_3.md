## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="../cv8/data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0 - Muž je otcom dcéry - strýkovia sú jej príbuzní.
HA - Muž nie je otcom dcéry - strýkovia nie sú jej príbuzní.

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**Presná metóda (Exact LR):

Logaritmická pravdepodobnosť H₀: -84.9882

Logaritmická pravdepodobnosť H₁: -100.7557

Likelihood Ratio (LR): 7.043 × 10⁶

Posteriorná pravdepodobnosť W(H₀): 0.99999986

Metóda klastrov (Cluster approach):

Logaritmická pravdepodobnosť H₀: -84.8410

Logaritmická pravdepodobnosť H₁: -100.7068

Likelihood Ratio (LR): 7.77 × 10⁶

Posteriorná pravdepodobnosť W(H₀): 0.99999986

Na základe výsledkov analýzy môžeme s vysokou istotou potvrdiť, že hypotéza H₀ (muž je otcom dcéry) je veľmi silne podporená genetickými údajmi.
Hodnota LR presahuje 7 miliónov a posteriorná pravdepodobnosť otcovstva je takmer 100%, čo znamená, že genetické údaje sú extrémne presvedčivé v prospech H₀.