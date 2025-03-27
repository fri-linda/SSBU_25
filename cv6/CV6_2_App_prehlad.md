# CV6: Prehľad aplikácie (machine_learning) 

Aplikácia v priečinku `machine_learning` demonštruje použitie strojového učenia na datasete UCI ML Breast Cancer Wisconsin (Diagnostic) z knižnice scikit-learn [1].

Aplikáciu otvorte v programe PyCharm. Pri otváraní aplikácie zvoľte možnosť vytvorenia **nového virtuálneho prostredia**. Ak je potrebná konfigurácia **Python interpretra**, postup nájdete v súbore `CV6_1_Vitrtualne_prostredie.md`.

V hlavnom adresári sa nachádza súbor `requirements.txt`, ktorý obsahuje zoznam knižníc, ktoré je potrebné nainštalovať pred spustením aplikácie.

Adresár **machine_learning** obsahuje hlavný skript `main.py`, ktorý spúšťa analýzu datasetu pomocou strojového učenia. Ďalšie skripty implementujú logiku pre beh experimentov, spracovanie dát, optimalizáciu modelov, vizualizáciu výsledkov a ďalšie.

---

## Prehľad implementovaných tried

### Triedy a ich zodpovednosti:
1. **`DatasetRefactored`**:
   - Načítava a čistí dataset rakoviny prsníka.
   - Rozdeľuje dáta na tréningovú a testovaciu množinu.
   - Škáluje dáta pomocou štandardizácie alebo normalizácie.

2. **`ModelTrainer`**:
   - Trénuje modely strojového učenia na poskytnutých dátach.
   - Vyhodnocuje modely pomocou metrík, ako sú presnosť, F1 skóre a ROC AUC.

3. **`ModelOptimizer`**:
   - Optimalizuje hyperparametre modelov pomocou grid search.

4. **`Experiment`**:
   - Spracováva celý experiment trénovania a hodnotenia modelov.
   - Používa SMOTE na vyváženie datasetu.
   - Ukladá výsledky experimentov a počíta priemerné matice zámien.

5. **`ExperimentPlotter`**:
   - Vizualizuje výsledky experimentov pomocou hustotných grafov, matíc zámien a ďalších vizualizácií.

6. **`Logger`**:
   - Spravuje logovanie správ a výsledkov do konzoly a súborov.

---

## Diagramy aplikácie

### Class Diagram

```plantuml
@startuml
class BasePlotter {
    +__generic_plot(plot_func: Callable, *args, **kwargs)
    +__apply_plot_labels(general_kwargs: dict)
}

class DatasetPlotter {
    +plot_class_distribution(df: pd.DataFrame)
    +plot_correlation_matrix(df: pd.DataFrame)
    +plot_feature_distributions(df: pd.DataFrame)
    +plot_box_plots(df: pd.DataFrame, target_col: str)
    +plot_pair_plot(df: pd.DataFrame, features: list, target_col: str)
}

class ExperimentPlotter {
    +plot_metric_density(results: pd.DataFrame, metrics: tuple)
    +plot_evaluation_metric_over_replications(all_metric_results: dict, title: str, metric_name: str)
    +plot_confusion_matrices(confusion_matrices: dict)
    +print_best_parameters(results: pd.DataFrame)
}

class Logger #wheat {
    +__init__(log_file: Optional[str], log_level: int)
    +info(message: str)
    +debug(message: str)
    +warning(message: str)
    +error(message: str)
    +critical(message: str)
}

class DatasetRefactored {
    +__init__()
    +__load_and_clean_data()
    +to_dataframe() : pd.DataFrame
    +split_data(test_size: float, stratify: bool, random_state: int) : Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]
    +scale_data(X_train: np.ndarray, X_test: np.ndarray, scale_type: str) : Tuple[np.ndarray, np.ndarray]
}

class ModelTrainer {
    +__init__(model: object, parameters: dict)
    +train(X_train: np.ndarray, y_train: np.ndarray)
    +evaluate(X_test: np.ndarray, y_test: np.ndarray) : Tuple[float, float, float, np.ndarray]
}

class ModelOptimizer {
    +__init__(model: object, param_grid: dict)
    +grid_search(X_train: np.ndarray, y_train: np.ndarray, cv: int, scoring: str) : dict
}

class Experiment {
    +__init__(models: dict, models_params: dict, n_replications: int, logger: Logger)
    +run(X: np.ndarray, y: np.ndarray) : pd.DataFrame
    -__initialize_csv_file()
    -__run_single_replication(replication: int, X: np.ndarray, y: np.ndarray)
    -__balance_dataset(X: np.ndarray, y: np.ndarray) : Tuple[np.ndarray, np.ndarray]
    -__train_and_evaluate_model(model_name: str, X_resampled: np.ndarray, y_resampled: np.ndarray, replication: int)
    -__store_results(model_name: str, replication: int, accuracy: float, f1: float, roc_auc: float, best_params: dict)
    -__calculate_mean_conf_matrices() : dict
}

DatasetRefactored --> Experiment
Experiment --> ModelTrainer
Experiment --> ModelOptimizer
Experiment --> ExperimentPlotter
Experiment --> Logger
ExperimentPlotter --|> BasePlotter
DatasetPlotter --|> BasePlotter
@enduml
```

---

### Call Sequence Diagram

```plantuml
@startuml
actor User
participant "main.py" as Main
participant "DatasetRefactored" as Dataset
participant "Experiment" as Experiment
participant "ModelTrainer" as Trainer
participant "ModelOptimizer" as Optimizer
participant "ExperimentPlotter" as Plotter
participant "Logger" as Logger #wheat

User -> Main: Run main.py
Main [#peru]--> Logger: Initialize Logger
Main -> Dataset: Initialize DatasetRefactored
Main -> Dataset: Split data
Main -> Experiment: Initialize Experiment
Main -> Experiment: Run experiment
Experiment -> Dataset: Balance dataset (SMOTE)
Experiment -> Optimizer: Perform grid search
Experiment -> Trainer: Train model
Experiment -> Trainer: Evaluate model
Experiment [#peru]--> Logger: Log results
Experiment -> Plotter: Generate plots
Plotter -> Main: Display plots
Main--> User: Read and Interpret plots
@enduml

```

---

## Výstupy aplikácie

Do adresára **outputs** sa ukladajú:
- Logy aplikácie (napr. `application.log`).
- Výsledky experimentov (napr. `model_accuracies.csv`).
- Vizualizácie (napr. grafy hustoty, matice zámien, grafy pre metriky).

---

#### Referencie

[1] https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html