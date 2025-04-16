## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

Nulová hypotéza (H₀):
Muž, ktorého bratia boli testovaní, je biologickým otcom dcéry.
Z toho dôvodu je dcéra geneticky príbuzná s bratmi tohto muža (strýkami).

Alternatívna hypotéza (H₁):
Muž, ktorého bratia boli testovaní, nie je biologickým otcom dcéry.
Preto dcéra nie je geneticky príbuzná so strýkami.

### Úloha 2 (4b)

Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

Výpočty boli vykonané pomocou softvéru **FamLinkX**, ktorý umožňuje testovanie nepriamych príbuzenských vzťahov na základe pravdepodobnostných modelov.

- **Získaný Likelihood Ratio (LR):**  
  **LR = 7.043 × 10⁶**

Toto číslo udáva, že je približne **7 miliónov krát pravdepodobnejšie**, že DNA profily boli získané za predpokladu platnosti hypotézy **H₀**, než za predpokladu **H₁**.

### Výpočet posteriornej pravdepodobnosti (Bayesova pravdepodobnosť):

Za predpokladu rovnakej predbežnej pravdepodobnosti oboch hypotéz (P(H₀) = P(H₁) = 0.5), vypočítame pravdepodobnosť po zohľadnení dôkazov takto:

W = (LR × P(H₀)) / [(LR × P(H₀)) + (P(H₁))] W = (7_043_000 × 0.5) / [(7_043_000 × 0.5) + 0.5] W ≈ 0.99999986 → 99.999986 %


##  Interpretácia

- Hodnota LR vysoko nad 1 silno podporuje platnosť hypotézy **H₀**.
- Výsledná posteriorná pravdepodobnosť **W ≈ 99.999986 %** predstavuje v genetickej forenznej praxi **extrémne silný dôkaz v prospech otcovstva**.
- Aj keď genetická analýza nikdy nevylučuje alternatívu úplne, výsledky sú **prakticky jednoznačné**.


##  Záver

Na základe analýzy DNA medzi dcérou a dvoma bratmi podozrivého muža (strýkmi), ako aj vypočítanej vysokej pravdepodobnosti otcovstva, môžeme **jednoznačne prijať hypotézu H₀**:

- Testovaný muž je **s extrémne vysokou pravdepodobnosťou biologickým otcom dcéry**.
- Dcéra je geneticky príbuzná so strýkami, čo nepriamo potvrdzuje otcovstvo.

 Tieto výsledky predstavujú **veľmi silný dôkaz** v prospech biologického otcovstva testovaného muža.