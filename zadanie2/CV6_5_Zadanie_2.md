## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

**Použitý model:**  
- **Random Forest** z knižnice *scikit-learn*

**Hyperparametre pre Random Forest:**
- **n_estimators:** `[100, 150, 300]` – počet stromov v lese.
- **max_depth:** `[5, 15, None]` – maximálna hĺbka stromu (kde `None` znamená, že strom nie je obmedzený).

**Zmeny aj pre Logistic Regression:**  
- **C:** `[0.05, 0.5, 5]` – inverzný parameter regularizácie.
- **max_iter:** `[5000]` – maximálny počet iterácií.

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

**Doplnená metrika:**  
- **Precision (presnosť):**  
  - Vyjadruje pomer správne identifikovaných pozitívnych prípadov ku všetkým prípadom, ktoré boli klasifikované ako pozitívne.

**Implementácia:**
- V triede `ModelTrainer` sme do metódy `evaluate` pridali výpočet `precision` pomocou funkcie `precision_score` zo `sklearn.metrics`.
- Hodnoty metriky sa ukladajú do CSV súboru `outputs/model_accuracies.csv` a zobrazujú sa v hustotných grafoch aj v grafe priebehu počas replikácií.


### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.


Grafy sú automaticky ukladané pri ich vytvorení do adresára `graphs/`.
 

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

**Počet replikácií:**
- Počet replikácií bol nastavený na **20**, čo zabezpečuje robustnejšie štatistické výsledky a lepšiu validáciu modelov.

**Interpretácia výsledkov:**
- **Grafy hustoty metrik (accuracy, f1_score, roc_auc, precision):**  
  - Z grafov je zrejmé, že **Random Forest** vykazuje konzistentnejšie a často lepšie výsledky s menšou variabilitou oproti **Logistic Regression**.
  
- **Grafy priebehu metrik cez replikácie:**  
  - Tieto grafy demonštrujú stabilitu modelu – Random Forest má nižšiu variabilitu výsledkov počas replikácií, čo naznačuje robustnejší výkon voči rôznym rozdeleniam dát.
  
- **Priemerné matice zámien:**  
  - Ukazujú, že Random Forest robí menej chýb pri klasifikácii, čo potvrdzuje jeho lepšiu schopnosť správne identifikovať triedy.


**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
