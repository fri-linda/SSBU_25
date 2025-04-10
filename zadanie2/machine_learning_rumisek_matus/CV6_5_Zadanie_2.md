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

SVM (Support Vector Machine) zo scikit-learn (trieda SVC) s voľbou probability=True, aby sme mohli počítať metriky ako napr. ROC AUC.

Parametre a ich hodnoty pre Grid Search: 

C: [0.1, 1, 10]

Ide o regulačný parameter, ktorý ovplyvňuje, aká veľká chyba je tolerovaná. Čím vyššia hodnota C, tým menší dôraz na regularizáciu.

kernel: ["linear", "rbf"] 

linear používa lineárnu separačnú hranicu.

rbf (radiálna báza) vie modelovať nelineárne vzťahy v dátach, čo môže zlepšiť presnosť pri zložitejších úlohách.

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

#TODO - Metrika

Precision meria, aký podiel z prípadov, ktoré model označil za pozitívne, je skutočne pozitívnych.

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

#TODO - Interpretácia

Tu je skrátená verzia interpretácie:

Precision: Graf zobrazuje vývoj hodnoty precision cez replikácie. Ak SVM má vyššiu a stabilnejšiu precision, znamená to lepšie rozpoznávanie pozitívnych prípadov a menej falošných poplachov oproti Logistic Regression, ktorá môže byť variabilnejšia.

Accuracy: Oba modely dosahujú vysokú accuracy, no ak Logistic Regression vykazuje menšiu variabilitu, je jej výkon stabilnejší.

Density Plots: Hustotné grafy ukazujú, či výsledky metrík (accuracy, F1, ROC AUC) sú sústredené okolo vysokých hodnôt, čo svedčí o dobrej výkonnosti. Ak SVM dosahuje hustejšie rozdelenie v ROC AUC, naznačuje lepšiu diskriminačnú schopnosť.

Confusion Matrix: Priemerné matice zmätenia odhaľujú, že SVM môže mať nižší počet falošne pozitívnych a negatívnych predikcií, čo znamená lepšie oddelenie tried.

Celková interpretácia:

SVM: Vhodný tam, kde je kritické minimalizovať falošné poplachy (vyššia precision a ROC AUC), ale môže byť citlivejší na rozdelenie dát.

Logistic Regression: Poskytuje konzistentnejšie a stabilnejšie výsledky, čo je výhodné v prípadoch, kde je dôležitá predvídateľnosť, hoci metriky precision/ROC AUC môžu byť o niečo nižšie.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
