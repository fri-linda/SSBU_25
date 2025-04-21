## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

#TODO - Popis

Použitý model: RandomForestClassifier Hodnoty parametrov pre Grid Search:
 
n_estimators: [50, 100, 200]
max_depth: [None, 10, 20, 30]

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

#TODO - Metrika

Pridal som metriku "precision" do evaluácie modelov, ukladania výsledkov a vykresľovania grafov.

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

#TODO - Interpretácia

Analýza pri 20 replikáciach:
Based on these analyses, you can determine which model performs better in terms of accuracy, F1 score, ROC AUC, and precision. For example, if the Random Forest model consistently outperforms the Logistic Regression model across all metrics, it can be considered the better model for this particular dataset.
Graf precíznosti pri každej replikácii a priemernej precíznosti pre všetky replikácie ukazuje, že Random Forest model má vyššiu presnosť a javí sa ako stabilnejší model v porovnaní s Logistic Regression modelom, ktorý môže mať problém s konzistentnosťou.
Graf presnosti klasifikácie pri každej replikacii, plus priemer zobrazuje zase že random forest má väčšie výkyvy a nižší priemer, zatiaľ čo logická regresia má vyššiu stabilitu a vyšší výkon.
Average confusion matrix ukazuje že Random Forest model si vedie dobre, má vysoké hodnoty TP a TN, celkom nízke hodnoty FP a FN, model je vyvážený a funguje dobre na oboch triedach. Na druhej strane, Logistic Regression model má vyššie hodnoty FP a FN, čo naznačuje, že model môže mať problém s klasifikáciou niektorých prípadov správne.
Density plot accuracy vizualizuje distribúciu presnosti pre každý model. Random Forest model má širšiu distribúciu, čo naznačuje variabilitu v jeho výkone, zatiaľ čo Logistic Regression model má užšiu distribúciu, čo naznačuje stabilnejší výkon.
Density plot f1 score zobrazuje že Random Forest model má širšiu distribúciu a vyššie hodnoty F1 skóre, čo naznačuje lepší výkon v porovnaní s Logistic Regression modelom.
Desinity plot precision ukazuje že Random Forest model má širšiu distribúciu a vyššie hodnoty presnosti, čo naznačuje lepší výkon v porovnaní s Logistic Regression modelom.
Desinity plot roc_auc zobrazuje že Random Forest model má širšiu distribúciu a vyššie hodnoty ROC AUC, čo naznačuje lepší výkon v porovnaní s Logistic Regression modelom.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
