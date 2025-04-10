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

def initialize_models_and_params():
    """
    Initializes models and their hyperparameter grids.

    Returns:
    - models: dict, dictionary of model instances.
    - param_grids: dict, dictionary of hyperparameter grids.
    """
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        "Random Forest": RandomForestClassifier()  # Pridávame nový model
    }

    param_grids = {
        "Logistic Regression": {"C": [0.1, 1, 10], "max_iter": [10000]},
        "Random Forest": {
            "n_estimators": [50, 100, 200],  
            "max_depth": [None, 10, 20],  
            "min_samples_split": [2, 5, 10],  
            "min_samples_leaf": [1, 2, 4]  
        }
    }

    return models, param_grids


Vybrala som model **RandomForestClassifier** s nasledujúcimi parametrami pre Grid Search:
    - **n_estimators**: [50, 100, 200] (Počet stromov v lese)
    - **max_depth**: [None, 10, 20] (Maximálna hĺbka stromu)
    - **min_samples_split**: [2, 5, 10] (Min. počet vzoriek na rozdelenie uzla)
    - **min_samples_leaf**: [1, 2, 4] (Min. počet vzoriek v listovom uzle)

    **RandomForestClassifier** 
    je silný model schopný spracovať veľké množstvo dát a zachytávať nelineárne vzťahy. 
    Okrem toho má zabudovanú ochranu pred overfittingom vďaka náhodnému výberu vzoriek a vlastností. 
    """

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

#TODO - Metrika
Recall

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

#TODO 
Logistic Regression:
Dosahoval veľmi konzistentné výsledky naprieč všetkými replikáciami.
Priemerná Accuracy aj F1 Score bola vysoká (okolo 0.975–0.98), pričom výkyvy boli minimálne.
Tiež mal stabilné Recall a ROC AUC, čo naznačuje dobrú schopnosť modelu detegovať pozitívne prípady bez veľkého počtu falošných negatívov.

Random Forest:

Pri niektorých replikáciách mal síce vyššie hodnoty ROC AUC (v niektorých prípadoch až 0.999), čo znamená silnú schopnosť rozlišovať triedy.
No zároveň sa ukázal ako menej stabilný – rozptyl vo výsledkoch (najmä Recall) bol väčší.
Výkon sa viac líšil v závislosti od náhodných inicializácií a nastavení parametrov (čo je vidno aj na rôznorodých hodnotách best parameters).

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
