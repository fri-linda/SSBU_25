## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html


Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**


Do experimentu bol pridaný nový model strojového učenia: KNeighborsClassifier (k-najbližších susedov).
Tento model je založený na hľadaní najbližších susedov v trénovacej množine a klasifikácii podľa väčšiny.
Pre tento model boli do Grid Search definované nasledujúce hyperparametre:
   - n_neighbors: [3, 5, 7] – počet susedov, ktorí sa berú do úvahy pri rozhodovaní o triede.
   - weights: ['uniform', 'distance'] – spôsob váženia susedov (rovnaká váha alebo váha podľa vzdialenosti).
   - metric: ['euclidean', 'manhattan'] – metrika použitá na výpočet vzdialenosti medzi bodmi.



### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**


Pridal som metriku precision a to nasledovne:

Výpočet precision: Najprv som použil funkciu precision_score zo scikit-learn, aby som vypočítal precision pre každý model počas testovania. Táto metrika vyjadruje presnosť predikcie pozitívnej triedy, teda pomer správne predikovaných pozitívnych prípadov k celkovému počtu predikovaných pozitívnych prípadov.

Uloženie do výsledkov experimentu: Následne som pridal hodnotu precision do slovníka s výsledkami experimentu pre každý model. Týmto spôsobom sa precision uložila pre každú repeticiu, čím bola pripravená na ďalšie spracovanie.

Zobrazenie v grafoch: Aby sa precision zobrazila v grafickej forme, zavolal som funkciu plot_evaluation_metric_over_replications, ktorá vykreslí priebeh precision počas jednotlivých repeticie. Tento graf zobrazuje hodnoty precision pre každý model a umožňuje vizualizáciu, ako sa presnosť modelov pri predikcii pozitívnej triedy mení počas repeticie.

Týmto spôsobom som pridal precision do experimentu a zabezpečil, aby bola správne vizualizovaná v grafoch a uložená v logoch.

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

POPIS:

V tejto úprave som implementoval funkciu, ktorá ukladá všetky generované grafy do samostatných priečinkov so špecifickým názvom, aby sa grafy pri opakovaných spusteniach programu neprepisovali. Každý priečinok bude obsahovať timestamp, ktorý jednoznačne identifikuje čas, kedy bol program spustený. Týmto spôsobom sa zabezpečí, že grafy budú správne usporiadané a nebudú sa prekrývať.

Popis zmien:
Pridanie timestampu:

Pre každý graf sa vytvorí jedinečný názov podadresára založený na aktuálnom čase. Použili sme funkciu datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), ktorá generuje časový údaj vo formáte YYYY-MM-DD_HH-MM-SS. Tento timestamp sa následne pripojí k názvu podadresára, čo umožňuje rozlíšiť grafy pri viacerých spusteniach programu.

Vytvorenie priečinka pre každý beh programu:

Pred uložením grafov sa skontroluje, či existuje priečinok s názvom na základe timestampu. Ak nie, vytvorí sa nový priečinok, ktorý bude obsahovať všetky grafy z daného behu programu.
Taktiez sa do nazvu priecinku zapisuje aj pocet replikacii pri ktorych bol beh spusteny.

Jedinečné názvy pre grafy:

Pre každý graf sa generuje názov súbor[cv7](../../cv7)u podľa typu grafu (napr. accuracy_density_plot). Ak súbor s rovnakým názvom už existuje, automaticky sa pridá index, aby sa názov stal jedinečným a zabránilo sa prepisovaniu súborov.

Ukladanie a zatváranie grafov:

Po vykreslení grafu sa uloží do príslušného priečinka a následne sa graf zatvorí, aby sa zabránilo jeho zobrazeniu a ďalšiemu zbytočnému vykresľovaniu.
### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)



### Porovnanie modelov: Logistic Regression vs. K-Nearest Neighbors

Presnosť (Accuracy):

Po vykonaní 100 replikácií sa ukázalo, že Logistic Regression dosahuje vyššiu a stabilnejšiu presnosť v rozmedzí 0.975 – 0.985. Jeho výsledky mali menší rozptyl, čo naznačuje konzistentný výkon naprieč rôznymi dátovými vzorkami.
Model K-Nearest Neighbors (KNN) dosahoval presnosť v rozmedzí 0.955 – 0.975, no s väčšou variabilitou. Po zvýšení počtu replikácií na 1000 sa rozdiely medzi modelmi síce zmenšili, no Logistic Regression si udržala výhodu v stabilite aj spoľahlivosti.

F1-skóre:

Logistická regresia dosahovala vyššie hodnoty F1-skóre, so sústredenou distribúciou medzi 0.96 – 1.00, čo znamená dobrú rovnováhu medzi presnosťou a úplnosťou (precision a recall).
KNN mal F1-skóre nižšie a rozptýlenejšie (okolo 0.94 – 0.98), čo naznačuje menšiu konzistenciu pri správnom zachytení pozitívnych prípadov.

ROC AUC:

Oba modely dosiahli vysoké hodnoty ROC AUC nad 0.97, čo svedčí o dobrej schopnosti rozlišovať medzi triedami.
Logistic Regression však mala rozloženie viac sústredené okolo 0.99 – 1.00, čo poukazuje na vyššiu a stabilnejšiu výkonnosť v tejto metrike. KNN mal mierne nižšie hodnoty, so širším rozptylom.

Precision (presnosť pozitívnych predikcií):

Logistická regresia preukázala najvyššiu konzistenciu, s hodnotami presnosti v rozmedzí 0.98 – 1.02.
KNN dosahovala nižšiu a variabilnejšiu presnosť (0.94 – 0.98), čo poukazuje na väčší výskyt falošne pozitívnych prípadov.

Porovnanie vývoja metrik počas replikácií:

Accuracy a Precision per Replication: Oba modely dosiahli identickú priemernú hodnotu 0.97, čo naznačuje, že z hľadiska dlhodobého priemeru sú výkonnostne podobné. Rozdiel sa však prejavuje v rozptyle a stabilite jednotlivých opakovaní, kde Logistic Regression jasne vedie.

Analýza priemerných konfúznych matíc

Logistic Regression:
Správne klasifikovala približne 278.85 z 286 prípadov (~97.5 %).
Falošne pozitívne (FP) = 4.29, falošne negatívne (FN) = 2.86.
Výsledky svedčia o vysokej presnosti a spoľahlivosti pri binárnej klasifikácii.

K-Nearest Neighbors:
Správne klasifikovala 277 z 287 prípadov (~96.6 %).
FP = 4.61, FN = 4.16.
Hoci model je výkonný, výsledky naznačujú nižšiu stabilitu oproti logistickej regresii.

Záver:

Na základe analýzy viacerých metrík možno povedať, že Logistic Regression vykazuje lepšie výsledky tak z hľadiska presnosti, ako aj stability.
Aj keď KNN dosahuje podobné priemerné hodnoty, jeho výkonnosť je viac ovplyvnená dátami a variabilitou. Logistická regresia je preto vhodnejšou voľbou pre úlohy, kde je potrebná vysoká konzistencia, presnosť a predvídateľnosť modelu.

**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
