## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

Pridal som dva nové modely - Random Forest a SVM. 
Pre Random Forest som nastavil parametre: n_estimators [50, 100, 200], max_depth [None, 5, 10], min_samples_split [2, 5, 10]. 
Pre SVM: C [0.1, 1, 10], kernel ['linear', 'rbf'], gamma ['scale', 'auto'].

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Doplnil som metriku precision (presnosť), ktorá meria podiel správne identifikovaných pozitívnych prípadov zo všetkých predpovedaných pozitívnych prípadov. 

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

Všetky grafy sa teraz ukladajú do priečinka "outputs/plots" ako PNG súbory. Vytvoril som ukladanie v novom súbore plot_saver.py a použil ju v main.py.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

Graf "metric_density_distribution.png": Distribúcia accuracy ukazuje, že Random Forest má najvyššiu a najstabilnejšiu presnosť. 
Graf "accuracy_over_replications.png": Krivky ukazujú, že Random Forest dosahuje konzistentne vysokú presnosť (modrá čiara) s malými výkyvmi medzi replikáciami.
Graf "precision_over_replications.png": Precision metrika potvrdzuje, že Random Forest najlepšie identifikuje skutočné pozitívne prípady. Logistická regresia vykazuje najnižšiu a najnestabilnejšiu precision.
Grafy confusion matrices: Random Forest má najnižší počet falošne negatívnych prípadov.
So zvyšujúcim sa počtom replikácií sa priemerné hodnoty metrík stabilizujú, čo potvrdzuje spoľahlivosť výsledkov.
Variabilita výsledkov medzi replikáciami je najnižšia pri Random Forest, čo z neho robí najspoľahlivejší model.
Random Forest sa ukazuje ako najvhodnejší model pre tento dataset, pretože kombinuje vysokú presnosť s nízkou variabilitou medzi replikáciami. 
SVM by mohol byť alternatívou v špecifických prípadoch, kde je kritická minimalizácia falošne pozitívnych výsledkov. 
Logistická regresia, hoci najrýchlejšia, nedosahuje dostatočnú presnosť pre túto úlohu.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
