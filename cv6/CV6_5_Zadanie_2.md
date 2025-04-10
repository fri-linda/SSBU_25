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

    Použila som model RandomForestClassifier zo scikit-learn.
    Pre Grid Search som nastavila nasledovné hodnoty parametrov:

    n_estimators: [50, 100] – počet stromov v lese

    max_depth: [None, 10, 20] – maximálna hĺbka stromu

    min_samples_split: [2, 5] – minimálny počet vzoriek na rozdelenie vnútorného uzla

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

#TODO - Metrika

    Doplnila sa metrika precision

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

     def __apply_plot_labels(self, general_kwargs):
        """
        Applies labels and titles to a plot.

        Parameters:
        - general_kwargs: dict, containing title, xlabel, ylabel, and other label-related arguments.
        """
        if general_kwargs['title']:
            plt.title(general_kwargs['title'])
        if general_kwargs['xlabel']:
            plt.xlabel(general_kwargs['xlabel'])
        if general_kwargs['ylabel']:
            plt.ylabel(general_kwargs['ylabel'])
        if general_kwargs['xticks_rotation']:
            plt.xticks(rotation=general_kwargs['xticks_rotation'])
        if general_kwargs['xticks'] is not None:
            plt.xticks(ticks=general_kwargs['xticks'])
        if general_kwargs['yticks'] is not None and general_kwargs['yticklabels'] is not None:
            plt.yticks(ticks=general_kwargs['yticks'], labels=general_kwargs['yticklabels'])
        save_to_file = general_kwargs['save_to_file']
        if save_to_file:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(save_to_file), exist_ok=True)
            # Save the plot to the specified file
            plt.savefig(save_to_file)
            print(f"Plot saved to {save_to_file}")
### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

#TODO - Interpretácia

    Presnosť:
    logická regresia - lepšia ako pri random forest modely, na grafe hustoty je vidno normálne rozdelenie celkom fajne a tiež ako je regresia posunutá viac k jednotke
    a tiež je vidno ako je čiara hodnôt regresie vyššie na druhom grafe
    
    Precíznosť:
    To isté čo platilo pre presnoť vyšlo aj pre precíznsoť len trošku iné hodnoty ale správanie kvázy rovnaké
 
    F1 skóre to isté čo pri precíznosti a presnosti
 
    Pri ROC AUC mala síce logistická hodnota lepšie výsledky ale random forest model sa zadl pri 50 replikáciack mať viac ustálenejšie hodnoty

    Matice zámeny:
    čo sa týka regresie a random forest o grafy priemernej matice (posledné dva grafy) tak môžeme vydieť nulovú zmenu oproti 10 replikáciam a 50 replikáciam
    čo sa týka ako ich vzájomneho porovnanie môžeme povedať že regresia je presnejšia ako model random forest ale obi dva modely maly malí počet chýb zanedbateľný ich presnosťou

    Záver: Možeme povedať, že logická regresia je lepšia asi pre naše dáta ale nie zas o moc
**Odovzdávanie riešenia:** Ako súčasť riešenia zahrňte okrem odpovedí na otázky aj skripty s Vašou implementáciou, vygenerované logy a grafy (všetko môžete dať na Github).

----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
