# CV6: Rozšírená dokumentácia pre machine_learning projekt 

Dokumentácia popisuje implementáciu pipeline pre strojové učenie, ktorá zahŕňa trénovanie, hodnotenie a vizualizáciu modelov. Obsahuje triedy na spracovanie dát, optimalizáciu hyperparametrov, vizualizáciu výsledkov a ďalšie.

---

### Trieda: `ModelTrainer`

Trieda `ModelTrainer` je navrhnutá na trénovanie a hodnotenie modelov strojového učenia. Obsahuje metódy na inicializáciu modelu s jeho hyperparametrami, trénovanie modelu na trénovacích údajoch a vyhodnotenie modelu na testovacích údajoch. Táto trieda umožňuje jednoduchú integráciu rôznych modelov z knižnice scikit-learn a poskytuje metriky, ako sú presnosť, F1 skóre a ROC AUC.

---

**Metóda:** `__init__(self, model, parameters)`

Inicializuje inštanciu `ModelTrainer` uložením modelu a jeho hyperparametrov. Táto metóda pripraví model na ďalšie operácie, ako je trénovanie a hodnotenie.

```pseudo
INPUT: model (scikit-learn model), parameters (dict of hyperparameters)
STORE the model instance in self.model
STORE the hyperparameters in self.parameters
```

---

**Metóda:** `train(self, X_train, y_train)`

Trénuje model na trénovacích údajoch. Validuje vstupné dáta a cieľové hodnoty, nastaví hyperparametre modelu a následne model natrénuje na poskytnutých údajoch.

```pseudo
INPUT: X_train (array-like training features), y_train (array-like training labels)
VALIDATE X_train and y_train using check_X_y to ensure they are in the correct format
SET the model's hyperparameters using self.parameters
FIT the model on X_train and y_train
```

---

**Metóda:** `evaluate(self, X_test, y_test)`

Vyhodnotí model na testovacích údajoch. Validuje vstupné dáta a cieľové hodnoty, predikuje štítky pre testovacie dáta a vypočíta metriky, ako sú presnosť, F1 skóre a ROC AUC. Táto metóda vracia hodnoty metrík spolu s predikovanými štítkami.

```pseudo
INPUT: X_test (array-like test features), y_test (array-like test labels)
VALIDATE X_test and y_test using check_array to ensure they are in the correct format
PREDICT labels for X_test using the model's predict method
IF the model supports predict_proba:
    CALCULATE probabilities for X_test
ELSE:
    SET probabilities to zeros
CALCULATE accuracy, F1 score, and ROC AUC using the predictions and y_test
RETURN accuracy, F1 score, ROC AUC, and predictions
```

---

### Trieda: `ModelOptimizer`

Trieda `ModelOptimizer` je navrhnutá na optimalizáciu hyperparametrov modelov strojového učenia. Používa metódu grid search na prehľadávanie mriežky hyperparametrov a výber najlepších hodnôt. Táto trieda umožňuje efektívne vylepšiť výkon modelov pomocou optimalizácie.

---

**Metóda:** `__init__(self, model, param_grid)`

Inicializuje inštanciu `ModelOptimizer` uložením modelu a mriežky hyperparametrov. Táto metóda pripraví model na optimalizáciu hyperparametrov.

```pseudo
INPUT: model (scikit-learn model), param_grid (dict of hyperparameters)
STORE the model instance in self.model
STORE the hyperparameter grid in self.param_grid
```

---

**Metóda:** `grid_search(self, X_train, y_train, cv=5, scoring='accuracy')`

Vykoná grid search na nájdenie najlepších hyperparametrov pre model. Validuje vstupné dáta a cieľové hodnoty, použije krížovú validáciu na hodnotenie modelu a vráti najlepšie hyperparametre. Táto metóda je kľúčová pre optimalizáciu modelov.

```pseudo
INPUT: X_train (array-like training features), y_train (array-like training labels), cv (int, number of folds), scoring (str, metric to optimize)
VALIDATE X_train and y_train using check_X_y to ensure they are in the correct format
INITIALIZE GridSearchCV with self.model, self.param_grid, cv, and scoring
FIT the grid search on X_train and y_train
RETURN the best parameters found by the grid search
```

---

### Trieda: `Experiment`

Trieda `Experiment` spracováva celý proces experimentu trénovania a hodnotenia modelov. Obsahuje metódy na spustenie experimentu cez viacero replikácií, vyváženie datasetu pomocou SMOTE, trénovanie a hodnotenie modelov a ukladanie výsledkov. Táto trieda umožňuje jednoduché porovnanie viacerých modelov a ich výkonu.

---

**Metóda:** `__init__(self, models, models_params, n_replications=100, logger=None)`

Inicializuje experiment s modelmi, ich parametrami a počtom replikácií. Ukladá modely, ich hyperparametre a inicializuje prázdny DataFrame na ukladanie výsledkov. Ak je poskytnutý logger, používa ho na logovanie.

```pseudo
INPUT: models (dict of model instances), models_params (dict of hyperparameters), n_replications (int, number of replications), logger (Logger instance)
STORE the models in self.models
STORE the hyperparameters in self.models_params
STORE the number of replications in self.n_replications
INITIALIZE an empty DataFrame in self.results to store results
IF logger is provided:
    STORE the logger in self.logger
ELSE:
    SET self.logger to None
```

---

**Metóda:** `run(self, X, y)`

Spustí experiment cez viacero replikácií. Pre každú replikáciu vyváži dataset, natrénuje a vyhodnotí každý model a vypočíta priemerné matice zámien. Táto metóda vracia výsledky experimentu.

```pseudo
INPUT: X (array-like features), y (array-like labels)
INITIALIZE a dictionary to store confusion matrices for each model
FOR each replication in range(self.n_replications):
    CALL __run_single_replication with the current replication, X, and y
CALCULATE mean confusion matrices for each model
RETURN self.results
```

---

**Metóda:** `__run_single_replication(self, replication, X, y)`

Spustí jednu replikáciu trénovania a hodnotenia modelov. Vyváži dataset a pre každý model ho natrénuje a vyhodnotí.

```pseudo
INPUT: replication (int, current replication number), X (array-like features), y (array-like labels)
PRINT the current replication number
BALANCE the dataset using __balance_dataset
FOR each model in self.models_params:
    CALL __train_and_evaluate_model with the model name, balanced data, and replication number
```

---

**Metóda:** `__balance_dataset(self, X, y)`

Vyváži dataset pomocou SMOTE. Táto metóda zabezpečuje, že dataset má rovnaký počet prípadov pre každú triedu, čo zlepšuje výkon modelov na nevyvážených dátach.

```pseudo
INPUT: X (array-like features), y (array-like labels)
INITIALIZE SMOTE
RETURN the resampled data and labels
```

---

**Metóda:** `__train_and_evaluate_model(self, model_name, X_resampled, y_resampled, replication)`

Trénuje a hodnotí jeden model. Používa grid search na optimalizáciu hyperparametrov, rozdelí dáta na tréningovú a testovaciu množinu, škáluje dáta, natrénuje model a vyhodnotí jeho výkon.

```pseudo
INPUT: model_name (str), X_resampled (array-like features), y_resampled (array-like labels), replication (int)
INITIALIZE StratifiedKFold for cross-validation
INITIALIZE ModelOptimizer with the model and its hyperparameters
PERFORM grid search to find the best hyperparameters
SPLIT the resampled data into training and test sets
SCALE the training and test data
TRAIN the model using ModelTrainer
EVALUATE the model and calculate metrics
STORE the results using __store_results
APPEND the confusion matrix to the model's confusion matrices
```

---

**Metóda:** `__store_results(self, model_name, replication, accuracy, f1, roc_auc, best_params)`

Uloží výsledky jednej evaluácie. Táto metóda pridá nový riadok s výsledkami modelu do DataFrame a zaznamená výsledky do logu.

```pseudo
INPUT: model_name (str), replication (int), accuracy (float), f1 (float), roc_auc (float), best_params (dict)
CREATE a new row with the model's results
APPEND the row to self.results
LOG the results
```

---

### Trieda: `ExperimentPlotter`

Trieda `ExperimentPlotter` je navrhnutá na vizualizáciu výsledkov experimentov strojového učenia. Obsahuje metódy na vykresľovanie hustotných grafov, grafov presnosti, matíc zámien a ďalších vizualizácií. Táto trieda umožňuje jednoduché pochopenie výkonu modelov.

---

**Metóda:** `plot_metric_density(self, results, metrics=('accuracy', 'f1_score', 'roc_auc'))`

Vykreslí hustotné grafy pre špecifikované metriky. Táto metóda umožňuje vizualizovať rozloženie hodnôt metrík pre rôzne modely.

```pseudo
INPUT: results (DataFrame containing experiment results), metrics (tuple of metric names)
FOR each metric in metrics:
    EXTRACT the column corresponding to the metric from results
    GROUP the data by model and calculate density for the metric
    PLOT the density plot with the metric on the x-axis and density on the y-axis
    SET the title, x-axis label, and y-axis label
DISPLAY the plot
```

---

**Metóda:** `plot_evaluation_metric_over_replications(self, all_metric_results, title, metric_name)`

Vykreslí hodnoty metriky pre každý model počas všetkých replikácií a zobrazí priemernú hodnotu metriky.

```pseudo
INPUT: all_metric_results (dict of metric values for each model), title (str), metric_name (str)
INITIALIZE a color palette for the models
FOR each model in all_metric_results:
    PLOT the metric values for each replication as a line plot
    CALCULATE the average metric value for the model
    ADD a dashed line to represent the average metric value
SET the title, x-axis label ('Replication'), and y-axis label (metric_name)
DISPLAY the plot
```

---

**Metóda:** `plot_confusion_matrices(self, confusion_matrices)`

Vykreslí priemernú maticu zámien pre každý model. Táto metóda umožňuje vizualizovať, ako dobre modely klasifikujú jednotlivé triedy.

```pseudo
INPUT: confusion_matrices (dict of confusion matrices for each model)
FOR each model in confusion_matrices:
    CALCULATE the average confusion matrix for the model
    PLOT the confusion matrix as a heatmap
    SET the title ('Average Confusion Matrix: <model_name>'), x-axis label ('Predicted label'), and y-axis label ('True label')
DISPLAY the plot
```

---

**Metóda:** `print_best_parameters(self, results)`

Vytlačí najčastejšie vybrané najlepšie parametre pre každý model. Táto metóda poskytuje prehľad o optimalizovaných hyperparametroch.

```pseudo
INPUT: results (DataFrame containing experiment results)
FOR each unique model in results:
    FILTER the rows corresponding to the model
    EXTRACT the 'best_params' column
    FIND the most frequently occurring parameter set
    PRINT the model name and the most frequent parameter set
```

---

### Trieda: `BasePlotter`

Trieda `BasePlotter` je abstraktná trieda, ktorá poskytuje spoločné funkcie na vykresľovanie grafov. Obsahuje generickú metódu na vykresľovanie, ktorá redukuje redundanciu v špecializovaných metódach na vykresľovanie.

---

**Metóda:** `__generic_plot(self, plot_func, *args, **kwargs)`

Generická metóda na vykresľovanie grafov. Táto metóda vytvára nový graf, zavolá poskytnutú funkciu na vykresľovanie a nastaví vlastnosti grafu, ako sú názov a popisy osí.

```pseudo
INPUT: plot_func (Callable), *args, **kwargs
EXTRACT general plot properties (title, axis labels, etc.) from kwargs
CREATE a new plot with the specified size
CALL the provided plotting function with the remaining arguments
SET the title, axis labels, and other properties if provided
DISPLAY the plot
```

---

**Metóda:** `__apply_plot_labels(self, general_kwargs)`

Aplikuje názvy a popisy na graf. Táto metóda nastaví názov grafu, popisy osí a ďalšie vlastnosti na základe poskytnutých argumentov.

```pseudo
INPUT: general_kwargs (dict containing title, xlabel, ylabel, etc.)
SET the title, xlabel, ylabel, and other properties if provided
```

---

### Trieda: `DatasetPlotter`

Trieda `DatasetPlotter` je navrhnutá na vizualizáciu vlastností datasetu. Obsahuje metódy na vykresľovanie distribúcie tried, korelačných matíc, distribúcií atribútov a ďalších grafov.

---

**Metóda:** `plot_class_distribution(self, df)`

Vykresľuje distribúciu tried v datasete.

```pseudo
INPUT: df (DataFrame containing the dataset with a 'target' column)
USE countplot to visualize the class distribution
```

---

**Metóda:** `plot_correlation_matrix(self, df)`

Vykresľuje korelačnú maticu atribútov v datasete.

```pseudo
INPUT: df (DataFrame containing the dataset features)
CALCULATE the correlation matrix
USE heatmap to visualize the correlation matrix
```

---

**Metóda:** `plot_feature_distributions(self, df)`

Vykresľuje distribúciu pre každý atribút v datasete.

```pseudo
INPUT: df (DataFrame containing the dataset features)
USE hist to plot histograms for all features
```

---

**Metóda:** `plot_box_plots(self, df, target_col)`

Vykresľuje boxploty pre každý atribút v datasete rozdelené podľa tried.

```pseudo
INPUT: df (DataFrame containing the dataset features and target column), target_col (str)
MELT the DataFrame to prepare it for boxplotting
USE boxplot to visualize the data grouped by classes
```

---

**Metóda:** `plot_pair_plot(self, df, features, target_col)`

Vykresľuje párové grafy pre vybrané atribúty v datasete.

```pseudo
INPUT: df (DataFrame containing the dataset features and target column), features (list of feature names), target_col (str)
USE pairplot to visualize relationships between selected features
```

---

### Trieda: `DatasetRefactored`

Trieda `DatasetRefactored` spracováva načítanie, čistenie a analýzu datasetu rakoviny prsníka. Obsahuje metódy na rozdelenie dát, škálovanie a konverziu na DataFrame.

---

**Metóda:** `__init__(self)`

Inicializuje triedu `DatasetRefactored` načítaním a čistením dát.

```pseudo
LOAD the breast cancer dataset
STORE the data, target, feature names, and target names
CALL the method to clean the data
```

---

**Metóda:** `__load_and_clean_data(self)`

Čistí dataset odstránením duplicitných riadkov a spracovaním chýbajúcich hodnôt.

```pseudo
CONVERT the data into a DataFrame
ADD the target column to the DataFrame
REMOVE duplicate rows
REMOVE rows with missing values
UPDATE the attributes for data and targets
```

---

**Metóda:** `to_dataframe(self)`

Konvertuje dataset na pandas DataFrame.

```pseudo
RETURN a DataFrame containing the features and target
```

---

**Metóda:** `split_data(self, test_size, stratify, random_state)`

Rozdelí dataset na tréningovú a testovaciu množinu.

```pseudo
INPUT: test_size (float), stratify (bool), random_state (int)
USE train_test_split to split the data and targets
RETURN the training and testing data and targets
```

---

**Metóda:** `scale_data(self, X_train, X_test, scale_type)`

Škáluje tréningové a testovacie dáta pomocou zvolenej metódy škálovania.

```pseudo
INPUT: X_train (array-like), X_test (array-like), scale_type (str)
SELECT the scaler based on the scale_type
FIT the scaler on the training data and transform both training and testing data
RETURN the scaled training and testing data
```

---

### Trieda: `Logger`

Trieda `Logger` spravuje logovanie správ a výsledkov do konzoly a súborov. Umožňuje jednoduché sledovanie priebehu aplikácie.

---

**Metóda:** `__init__(self, log_file, log_level)`

Inicializuje inštanciu `Logger` nastavením konzolového a súborového logovania.

```pseudo
INPUT: log_file (str), log_level (int)
CREATE a console handler and set its level
IF log_file is provided:
    CREATE a file handler and set its level
ADD the handlers to the logger
```

---

**Metóda:** `info(self, message)`

Zaznamená informačnú správu.

```pseudo
INPUT: message (str)
LOG the message with INFO level
```

---

**Metóda:** `debug(self, message)`

Zaznamená debugovaciu správu.

```pseudo
INPUT: message (str)
LOG the message with DEBUG level
```

---

**Metóda:** `warning(self, message)`

Zaznamená varovnú správu.

```pseudo
INPUT: message (str)
LOG the message with WARNING level
```

---

**Metóda:** `error(self, message)`

Zaznamená chybovú správu.

```pseudo
INPUT: message (str)
LOG the message with ERROR level
```

---

**Metóda:** `critical(self, message)`

Zaznamená kritickú správu.

```pseudo
INPUT: message (str)
LOG the message with CRITICAL level
```

---

### Príklad použitia

```python
from data.data_handling_refactored import DatasetRefactored
from experiment.experiment import Experiment
from plotting.experiment_plotter import ExperimentPlotter
from utils.logger import Logger

# Inicializácia datasetu
dataset = DatasetRefactored()

# Inicializácia loggera
logger = Logger(log_file="outputs/application.log")

# Rozdelenie dát
X_train, X_test, y_train, y_test = dataset.split_data()

# Inicializácia modelov a parametrov
models = {"Logistic Regression": LogisticRegression(solver='liblinear')}
param_grids = {"Logistic Regression": {"C": [0.1, 1, 10], "max_iter": [10000]}}

# Spustenie experimentu
experiment = Experiment(models, param_grids, n_replications=10, logger=logger)
results = experiment.run(X_train, y_train)

# Vykreslenie výsledkov
plotter = ExperimentPlotter()
plotter.plot_metric_density(results)
plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
```
