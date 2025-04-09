## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

Vyuzila som nahodny les (random forest) s parametrami:
            n_estimators: [50, 100, 200],
            max_depth: [None, 5, 10],
            min_samples_split: [2, 5],
            min_samples_leaf: [1, 2],
            bootstrap: [True, False].

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

F1 skore

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

Počet replikácií:

Počet replikácií bol nastavený na 20, čo umožňuje získať robustnejší a štatisticky spoľahlivejší odhad výkonnosti modelov. Vyšší počet replikácií minimalizuje vplyv náhodných odchýlok pri delení dát a zároveň potvrdzuje stabilitu metrík.

Interpretácia výsledkov:

Grafy hustoty metrik (accuracy, f1_score, roc_auc):

Z grafov hustoty vyplýva, že hodnoty metrik pre jednotlivé modely sú zoskupené okolo stredných hodnôt. Napríklad, ak Random Forest vykazuje užšie a posunuté rozdelenie smerom k vyšším hodnotám accuracy a F1 skóre, znamená to, že tento model má konzistentnejší a lepší výkon v porovnaní s Logistic Regression.

Grafy priebehu metrik počas replikácií:

Čiarové grafy, ktoré zobrazujú vývoj metrik počas 50 replikácií, demonštrujú stabilitu modelov. Ak sa pre Random Forest krivka hodnôt stabilizuje rýchlejšie a vykazuje menšiu variabilitu oproti Logistic Regression, naznačuje to, že Random Forest poskytuje robustnejšie a spoľahlivejšie výsledky v rôznych rozdeleniach dát.

Priemerné matice zámien:

Agregované confusion matrices pre jednotlivé modely poskytujú prehľad o klasifikačných chybách. Ak Random Forest vykazuje menej chybne klasifikovaných prípadov (nižší počet FP a FN) v porovnaní s Logistic Regression, potvrdzuje to jeho lepšiu schopnosť správne rozpoznávať jednotlivé triedy (napr. benigné vs. maligné prípady).

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
