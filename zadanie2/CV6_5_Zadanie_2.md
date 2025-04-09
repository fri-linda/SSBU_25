## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

Použil som model **RandomForestClassifier** zo scikit-learn. Pre tento model som definoval nasledovný hyperparameter grid pre Grid Search:  
- **n_estimators:** `[50, 100, 200]`  
- **max_depth:** `[None, 10, 20]`  


### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Ako ďalšiu metriku som implementoval **precision** (presnosť), ktorá udáva pomer správne identifikovaných pozitívnych prípadov k celkovému počtu prípadov, ktoré boli klasifikované ako pozitívne 🎯.  
Implementácia zahŕňa:  
- Úpravu triedy `ModelTrainer` na výpočet precision pomocou funkcie `precision_score` zo sklearn.  
- Uloženie hodnoty precision do CSV súboru (`model_accuracies.csv`).  
- Pridanie precision do grafov hustoty rozdelenia a vytvorenie samostatného grafu, ktorý zobrazuje priebeh precision počas replikácií.


### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

- **Počet replikácií:** V skripte `main.py` som nastavil počet replikácií na **20**. Tento vyšší počet replikácií poskytuje robustnejšie a štatisticky významnejšie výsledky.
- **Interpretácia vygenerovaných grafov:**  
  - **Hustotné grafy metrik (accuracy, f1, roc_auc, precision):**  
    - Grafy ukazujú, že model **Random Forest** dosahuje konzistentnejšie a často aj lepšie výsledky v porovnaní s **Logistic Regression**.  
  - **Grafy priebehu metrik počas replikácií:**  
    - Tieto grafy odhaľujú, že variabilita výsledkov pre Random Forest je nižšia, čo naznačuje stabilnejší výkon naprieč rôznymi behmi.  
  - **Priemerné matice zámien:**  
    - Matice potvrdzujú, že Random Forest robí menej chýb pri klasifikácii, čo je dôležité najmä pri riešení nevyvážených datasetov 📊.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
