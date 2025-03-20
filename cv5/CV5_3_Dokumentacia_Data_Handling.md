# Dokumentácia triedy Dataset

Trieda `Dataset` je navrhnutá na spracovanie, analýzu a vizualizáciu datasetu rakoviny prsníka. Nižšie je podrobný popis triedy a jej metód vrátane pseudokódu pre každú z nich.

---

## Trieda: `Dataset`

### Popis:
Táto trieda poskytuje funkcie na:
- Načítanie a čistenie datasetu rakoviny prsníka.
- Vykonávanie štatistickej analýzy.
- Rozdelenie datasetu na tréningovú a testovaciu množinu.
- Škálovanie dát pomocou štandardizácie alebo normalizácie.
- Vizualizáciu dát pomocou rôznych grafov.

---

### Metóda: `__init__()`

#### Popis:
Inicializuje triedu `Dataset` načítaním datasetu rakoviny prsníka a jeho čistením. Táto metóda načíta dáta, cieľové hodnoty, názvy atribútov a názvy cieľov z preddefinovaného datasetu. Po načítaní zavolá internú metódu na čistenie dát, aby zabezpečila, že dataset je pripravený na ďalšie spracovanie. Táto inicializácia je kľúčová pre správne fungovanie všetkých ostatných metód triedy.

```pseudo
load the breast cancer dataset
store the data, target, feature names, and target names
call the method to clean the data
```

---

### Metóda: `__load_and_clean_data()`

#### Popis:
Čistí dataset odstránením duplicitných riadkov a spracovaním chýbajúcich hodnôt. Táto metóda konvertuje načítané dáta na DataFrame pre jednoduchšiu manipuláciu. Následne odstráni duplicitné riadky a riadky s chýbajúcimi hodnotami, aby sa zabezpečila kvalita dát. Po vyčistení aktualizuje atribúty dát a cieľov, aby odrážali zmeny.

```pseudo
convert the data into a DataFrame
add the target column to the DataFrame
remove duplicate rows
remove rows with missing values
update the attributes for data and targets
```

---

### Metóda: `split_data(test_size=0.2, stratify=True, random_state=42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]`

#### Popis:
Rozdelí dataset na tréningovú a testovaciu množinu. Táto metóda umožňuje stratifikáciu, aby sa zabezpečilo, že rozdelenie tried v tréningovej a testovacej množine je rovnaké ako v pôvodnom datasete. Používa funkciu `train_test_split` z knižnice scikit-learn na rozdelenie dát a cieľov na tréningové a testovacie množiny. Výsledkom sú štyri výstupy: tréningové dáta, testovacie dáta, tréningové ciele a testovacie ciele.

```pseudo
if stratification is enabled, use the target for stratification
use `train_test_split` to split the data and targets
return the training and testing data and targets
```

---

### Metóda: `scale_data(X_train, X_test, scale_type='standard') -> Tuple[np.ndarray, np.ndarray]`

#### Popis:
Škáluje tréningové a testovacie dáta pomocou zvolenej metódy škálovania (štandardizácia alebo normalizácia). Táto metóda definuje slovník dostupných škálovačov, ako sú `StandardScaler` a `MinMaxScaler`. Na základe zvoleného typu škálovania vyberie vhodný škálovač, ktorý sa naučí na tréningových dátach a následne transformuje tréningové aj testovacie dáta. Ak je zadaný neplatný typ škálovania, vyhodí chybu `ValueError`.

```pseudo
define a dictionary of scalers (StandardScaler and MinMaxScaler)
retrieve the scaler based on the `scale_type`
if the scaler is invalid, raise a ValueError
fit the scaler on the training data and transform both training and testing data
return the scaled training and testing data
```

---

### Metóda: `__generic_plot(plot_func, *args, **kwargs)`

#### Popis:
Generická metóda na vykresľovanie grafov, ktorá redukuje redundanciu v metódach na vykresľovanie. Táto metóda extrahuje všeobecné vlastnosti grafu, ako sú názov a popisy osí, z argumentov `kwargs`. Vytvorí nový graf s určenou veľkosťou a zavolá poskytnutú funkciu na vykresľovanie s ostatnými argumentmi. Nakoniec nastaví názov, popisy osí a ďalšie vlastnosti grafu, ak sú poskytnuté, a zobrazí graf.

```pseudo
extract general plot properties (title, axis labels, etc.) from kwargs
create a new plot with the specified size
call the provided plotting function with the remaining arguments
set the title, axis labels, and other properties if provided
display the plot
```

---

### Metóda: `visualize_feature_distribution(feature_index, scaled_data=None, title_suffix="")`

#### Popis:
Vizualizuje distribúciu konkrétneho atribútu pred a po škálovaní pomocou boxplotov. Táto metóda overí, či je index atribútu platný, a získa názov atribútu a jeho pôvodné dáta. Následne vykreslí boxplot pre pôvodné dáta atribútu a, ak sú poskytnuté škálované dáta, vykreslí aj boxplot pre škálované dáta.

```pseudo
validate the feature index
retrieve the feature name and original feature data
plot the original feature using a boxplot
if scaled data is provided, plot the scaled feature using a boxplot
```

---

### Metóda: `plot_class_distribution()`

#### Popis:
Vykresľuje distribúciu tried v datasete. Táto metóda vytvorí DataFrame obsahujúci cieľové hodnoty a použije `countplot` na vizualizáciu počtu prípadov pre každú triedu. Výsledný graf poskytuje prehľad o rovnováhe tried v datasete.

```pseudo
create a DataFrame with the target column
use countplot to visualize the class distribution
```

---

### Metóda: `plot_correlation_matrix()`

#### Popis:
Vykresľuje korelačnú maticu atribútov v datasete. Táto metóda konvertuje dáta na DataFrame a vypočíta korelačnú maticu medzi atribútmi. Následne použije heatmap na vizualizáciu korelačných hodnôt, čo umožňuje identifikovať silné a slabé vzťahy medzi atribútmi.

```pseudo
convert the data into a DataFrame
calculate the correlation matrix
use heatmap to visualize the correlation matrix
```

---

### Metóda: `feature_importance()`

#### Popis:
Určuje dôležitosť každého atribútu pomocou Random Forest klasifikátora a vykresľuje výsledky. Táto metóda inicializuje model Random Forest, naučí ho na dátach a cieľoch a získa dôležitosti atribútov. Výsledky sú zoradené zostupne a vizualizované ako stĺpcový graf, ktorý ukazuje, ktoré atribúty najviac prispievajú k predikcii.

```pseudo
initialize a RandomForestClassifier
train the model on the data and targets
retrieve feature importances and sort them in descending order
plot the feature importances as a bar chart
```

---

### Metóda: `plot_feature_distributions()`

#### Popis:
Vykresľuje distribúciu pre každý atribút v datasete. Táto metóda konvertuje dáta na DataFrame a použije metódu `hist` na vykreslenie histogramov pre všetky atribúty. Výsledné grafy poskytujú prehľad o rozložení hodnôt jednotlivých atribútov.

```pseudo
convert the data into a DataFrame
use the `hist` method to plot histograms for all features
```

---

### Metóda: `plot_box_plots(scaled_data=None, target=None)`

#### Popis:
Vykresľuje boxploty pre každý atribút v datasete rozdelené podľa tried. Ak sú poskytnuté škálované dáta, použije ich na vykreslenie. Táto metóda overí, či dĺžky dát a cieľov sú rovnaké, a následne transformuje dáta na formát vhodný na vykreslenie boxplotov.

```pseudo
if scaled data is provided, use it; otherwise, use the original data
if a target is provided, use it; otherwise, use the original target
ensure the lengths of data and target match
convert the data into a DataFrame and add the target column
transform the DataFrame into a format suitable for plotting
use boxplot to visualize the data grouped by classes
```

---

### Metóda: `plot_pair_plot(features)`

#### Popis:
Vykresľuje párové grafy pre vybrané atribúty v datasete. Táto metóda konvertuje dáta na DataFrame, pridá cieľový stĺpec a použije `pairplot` na vizualizáciu vzťahov medzi vybranými atribútmi. Výsledné grafy ukazujú, ako sa jednotlivé atribúty vzájomne ovplyvňujú.

```pseudo
convert the data into a DataFrame
add the target column to the DataFrame
use `pairplot` to visualize relationships between selected features
```

---

### Metóda: `plot_all_features_before_after_scaling(X_train, X_train_scaled, scale_type)`

#### Popis:
Vizualizuje distribúciu všetkých atribútov pred a po škálovaní pomocou boxplotov. Táto metóda vykreslí boxploty pre pôvodné aj škálované tréningové dáta, pričom nastaví popisky osí na názvy atribútov. Výsledné grafy umožňujú porovnať efekt škálovania na distribúciu dát.

```pseudo
plot the original training data using boxplots
set the y-axis labels to feature names
plot the scaled training data using boxplots
set the y-axis labels to feature names
```

---

### Metóda: `plot_feature_before_after_scaling(X_train, X_train_scaled, feature_name)`

#### Popis:
Vizualizuje distribúciu konkrétneho atribútu pred a po škálovaní pomocou histogramov. Táto metóda overí názov atribútu, získa index a zodpovedajúce dáta a vykreslí histogramy pre pôvodné aj škálované dáta atribútu.

```pseudo
validate the feature name
retrieve the index and corresponding data for the feature
plot the original feature data using a histogram
plot the scaled feature data using a histogram
```

---

## Príklad použitia

```python
from data_handling_done import Dataset

# Inicializácia triedy Dataset
dataset = Dataset()

# Rozdelenie dát
X_train, X_test, y_train, y_test = dataset.split_data()

# Škálovanie dát
X_train_scaled, X_test_scaled = dataset.scale_data(X_train, X_test, scale_type='standard')

# Vykreslenie distribúcií atribútov
dataset.plot_feature_distributions()

# Vykreslenie boxplotov pre škálované dáta
dataset.plot_box_plots(scaled_data=X_train_scaled, target=y_train)
```