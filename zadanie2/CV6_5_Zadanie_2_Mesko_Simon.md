## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

Pridaný model: KNeighborsClassifier (KNN)

Použité parametre pre Grid Search:
- n_neighbors: [3, 5, 7] — počet susedov, ktorí sa berú do úvahy pri klasifikácii
- weights: ['uniform', 'distance'] — určenie váh susedom; uniform = rovnaká váha, distance = bližší susedia majú väčšiu váhu
- metric: ['euclidean', 'manhattan'] — metriky vzdialenosti; euklidovská a manhattanská vzdialenosť

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Pridaná metrika: Precision

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

Porovnanie modelov (Logistic Regression vs KNN)

Accuracy
Pri 10 replikáciách sa priemerná presnosť oboch modelov pohybovala okolo 0.98, s veľmi malými rozdielmi.
Pri 20 replikáciách má mierne vyššiu priemernú presnosť stále Logistic Regression (~0.98), zatiaľ čo KNN klesol mierne pod 0.97.
Záver: Logistic Regression robí menej chýb celkovo a je stabilnejší, keď sa experiment opakuje viackrát.

F1 skóre
Pri 10 replikáciách boli hodnoty F1-score pre oba modely veľmi blízko pri sebe.
Pri 20 replikáciách má však Logistic Regression viditeľne vyšší a stabilnejší F1-score než KNN, ktorého výsledky sú rozptýlenejšie.
Záver: Logistic Regression dosahuje lepšiu rovnováhu medzi presnosťou a úplnosťou predikcie.

Precision
Pri 10 replikáciách malo KNN jemne vyššie priemerné precision ako Logistic Regression.
Pri 20 replikáciách sa rozdiely vyrovnali, pričom Logistic Regression vykazuje rovnomernejšiu distribúciu a menej extrémne hodnoty.
Záver: Aj keď má KNN v niektorých prípadoch vyššiu presnosť pozitívnych predikcií, Logistická regresia je z pohľadu konzistentnosti spoľahlivejšia.

ROC AUC
Pri 10 replikáciách aj pri 20 replikáciách má Logistic Regression výrazne užší a vyšší vrchol hustoty, čo naznačuje konzistentne vysoké hodnoty. KNN má širšiu distribúciu s nižšími hodnotami.
Záver: Z hľadiska schopnosti oddeľovať triedy je Logistic Regression jednoznačne efektívnejší. Vyššie ROC AUC znamená lepšie rozpoznávanie medzi pozitívnymi a negatívnymi triedami.

Confusion Matrices
Logistic Regression má menej chýb – teda menej FP aj FN.
KNN spravil viac nesprávnych predikcií pri 20 replikáciách.
Záver: Logistic Regression sa menej mýli – najmä v prípade, keď ide o dôležité rozhodnutia (napr. neoznačí chorého ako zdravého).

Celkové zhrnutie
Logistic Regression je viac konzistentná, spoľahlivá a presná v takmer všetkom.
KNN je menej konzistentný pri vyššom počte replikácií (je viac citlivý na dáta a parametre).
Pri oboch modeloch sú rozdiely malé, ale Logistic Regression je spoľahlivejšia vo väčšine metrikách.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
