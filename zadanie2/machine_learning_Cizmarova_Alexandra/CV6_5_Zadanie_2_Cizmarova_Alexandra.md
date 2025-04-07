## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

Pridaný model je Random Forest Classifier.
Použité parametre a ich hodnoty pre Grid Search:
- `n_estimators`: [100, 200] – počet stromov v lese.
- `max_depth`: [3, 5, None] – maximálna hĺbka stromu bez obmedzenia.
- `min_samples_split`: [2, 5] – minimálny počet vzoriek potrebných na rozdelenie vnútorného uzla.
- `max_features`: ['sqrt', 'log2'] – počet vlastností vybraných pri hľadaní najlepšieho splitu.


### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Doplnená metrika je Precision (presnosť pozitívnych predikcií).
Precision udáva, aký podiel predikcií označených modelom ako pozitívne je skutočne správnych.  
Hodí sa použiť pri nevyvážených dátach.

Implementácia:
- Precision bola vypočítaná v `model_trainer.evaluate()`,
- pridaná do CSV logov v `experiment.__store_results()` a `experiment.__initialize_csv_file()`,
- zobrazená ako hustotný graf v `experiment_plotter.plot_metric_density()`,
- zobrazená ako priebehový graf v `experiment_plotter.plot_evaluation_metric_over_replications()`.


### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

Grafy sú automaticky ukladané pri ich vytvorení do adresára `outputs/` pomocou úpravy metódy `__generic_plot()` v súbore `base_plotter.py`.
Do tejto funkcie je pridaný voliteľný parameter `save_name`, ktorý umožňuje každý graf uložiť do súboru vo formáte `.png`. 
Následne sú všetky výstupné grafy (hustotné grafy, matice zámien, priebehy metrík) doplnené o názvy súborov, v ktorých sa ukladajú.


### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

Replikácie boli nastavené na 20, čiže experiment netrval dlho, výsledky modelov boli stabilnejšie a rozdiely medzi nimi sa prejavili výraznejšie.

Accuracy
- Logistic Regression dosiahla vyššiu priemernú presnosť 0.98, oproti Random Forest s 0.97.  
- Jej priebeh bol stabilnejší, s menšou variabilitou počas replikácií.
- 
Hustota metrík
- Logistic Regression mala posunuté hustoty vpravo pre všetky tri metriky – accuracy, F1 score aj ROC AUC – čo naznačuje jej vyššiu výkonnosť.  
- Random Forest mal síce ostrejšie rozloženie, ale menej výkonné.  

Confusion Matrix
- Logistic Regression: veľmi nízka chybovosť, takmer symetrická klasifikácia.  
- Random Forest: mierne vyšší počet false positives, čiže maligné boli predikované ako benigné.

Záver:
Na základe všetkých metrík (accuracy, F1, ROC AUC) a vizualizácií bola Logistic Regression mierne presnejšia, stabilnejšia a spoľahlivejšia ako Random Forest na tomto datasete.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
