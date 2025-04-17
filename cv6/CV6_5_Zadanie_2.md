## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

Použil som klasifikačný model K-nearest neighbors s nasledovnými parametrami:
    "n_neighbors": Počet najbližších susedov, ktoré sa zohľadnujú pri klasifikácií, teda koľko najbližších vzoriekzoberie aby vedel 
        terajšiu vzorku klasifikovať na základe metriky, ktorá je ďalším parametrom, použili sme hodnoty 3, 5, 7
    "weights": určuje váhy vybraných susedov, teda čím väčšia váha, tým bližšie, alebo pravdepodobnejšie sa klaasifikuje do triedy danej vzorky
        metódy sme vybrali unifrom, a distance, pri uniform majú všetci susedia tú istú váhu, a pri distance majú tým väčšiu váhu, čím sú bližšie k našej vzorke ktorú klasfikujeme
    "algorithm": určuje akým spôsobom sa vyhľadávajú najbližší susedia
        auto: automaticky vyberie najlepší algoritmus na základe vstupných dát
        ball_tree: používa hierarchickú štruktúru dát nazvanú ball_tree, ktorá organizuje vzorky do guľovtých oblastí na základe vzdialenosti. 
            Efektívne pre vysokodimenzionálne dáta
        kd_tree: hierarchická štruktúra, ktorá rozdeľuje pristeor do k-dimenzionálnych oblastí.
            Efektívne pre nízke a stredne dimenzionálne dáta
        brute: metóda "nasilu". Najjednoduchší, ale aj najpomalší prístup, pretože pre každú vzorku počíta vzdialenosť voči všetkým ostatným vzorkám
### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Rozhodol som sa doplniť metriku Recall
    Je to metrika, ktorá vyjadruje, aké percento skutočne pozitývnych prípadov bolo správne klasifikovaných

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

Model logistickej regresie dosahuje lepšie výsledky vo všetkých grafov než metóda K-najbližších susedov. 
Logistická regresia vykazovala vyššie priemerné hodnoty pri všetkých kľúčových metrikách.
Matice zámen potvrdili robí priemerne menej kalsifikačných chýb oboch typov.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
