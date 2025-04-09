import warnings

# Potlačenie niektorých FutureWarning správ zo scikit-learn
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from data.data_handling_refactored import DatasetRefactored
from experiment.experiment import Experiment
from plotting.experiment_plotter import ExperimentPlotter
from utils.logger import Logger


def initialize_models_and_params():
    """
    Inicializácia modelov a hyperparameter gridov.

    Vrátené hodnoty:
    - models: dictionary inštancií modelov.
    - param_grids: dictionary s hyperparameter gridmi pre jednotlivé modely.
    """
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        "Random Forest": RandomForestClassifier(random_state=42)
    }
    param_grids = {
        "Logistic Regression": {"C": [0.1, 1, 10], "max_iter": [10000]},
        "Random Forest": {
            "n_estimators": [50, 100, 200],
            "max_depth": [None, 5, 10],
            "min_samples_split": [2, 5],
            "min_samples_leaf": [1, 2],
            "bootstrap": [True, False]
        }
    }
    return models, param_grids


def run_experiment(dataset, models, param_grids, logger):
    """
    Spustenie experimentu s daným datasetom, modelmi a hyperparameter gridmi.

    Pridali sme parameter 'replications', ktorý nastavujeme na 50 –
    čo znamená, že počas behu experimentu sa vykoná 50 replikácií.

    Argumenty:
    - dataset: inštancia Dataset, ktorá obsahuje dáta a target.
    - models: dictionary inštancií modelov.
    - param_grids: dictionary hyperparameter gridov.
    - logger: inštancia Logger na zaznamenávanie hlásení.

    Vrátené hodnoty:
    - experiment: objekt experimentu.
    - results: DataFrame s výsledkami experimentu.
    """
    logger.info("Spúšťam experiment...")
    replications = 20  # Zvýšený počet replikácií pre robustnejšiu evaluáciu
    experiment = Experiment(models, param_grids, logger=logger, replications=replications)
    results = experiment.run(dataset.data, dataset.target)
    logger.info("Experiment prebehol úspešne.")
    return experiment, results


def plot_results(experiment, results, logger):
    """
    Vykreslenie výsledkov experimentu.

    Argumenty:
    - experiment: inštancia experimentu.
    - results: DataFrame s výsledkami experimentu.
    - logger: inštancia Logger na zaznamenávanie hlásení.
    """
    logger.info("Generujem grafy výsledkov experimentu...")
    plotter = ExperimentPlotter()
    plotter.plot_metric_density(results)
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['accuracy'].apply(list).to_dict(),
        'Accuracy per Replication and Average Accuracy', 'Accuracy')
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['f1_score'].apply(list).to_dict(),
        'F1 Score per Replication and Average F1 Score', 'F1 Score')
    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    plotter.print_best_parameters(results)
    logger.info("Grafy boli úspešne vygenerované a uložené.")


def main():
    """
    Hlavná funkcia spúšťajúca tréning a evaluáciu modelov.

    Funkcia inicializuje dataset, definuje modely a hyperparametre,
    nastavuje vyšší počet replikácií a spúšťa experiment.
    Po behu aplikácie si preštudujte vygenerované grafy.

    Po analýze grafov (napr. hustota Accuracy, evolúcia metrik a confusion matrix)
    môžeme pozorovať, že:

    - **Density Plots (hustota metrik)**: U grafov hustoty môžete zistiť, ako sú hodnoty Accuracy, F1 Score a ROC AUC rozdelené pre jednotlivé modely.
      Napríklad, ak má Random Forest hustotu s menším rozptýlením a vyššími hodnotami, naznačuje to, že model je konzistentnejší.

    - **Evolúcia metrik počas replikácií**: Grafy evolúcie metrik počas 50 replikácií ukážu, ako sa jednotlivé metriky (napr. Accuracy a F1 Score) menia naprieč behmi.
      Ak sa pre Random Forest hodnoty konvergujú rýchlejšie a s menšou variabilitou, môže to znamenať stabilnejší výkon.

    - **Confusion Matrices (maticie zámien)**: Z grafov s confusion matrix získate prehľad, koľko prípadov bolo nesprávne klasifikovaných (False Positives / False Negatives) pre jednotlivé modely.
      Ak Random Forest vykazuje menej chýb, je považovaný za výhodnejší najmä v citlivých aplikáciách, ako je diagnostika rakoviny.

    Tieto vizualizácie vám pomôžu lepšie porovnať a zhodnotiť výkonnosť jednotlivých modelov.
    """
    logger = Logger(log_file="outputs/application.log")
    logger.info("Aplikácia spustená.")

    dataset = DatasetRefactored()
    models, param_grids = initialize_models_and_params()
    experiment, results = run_experiment(dataset, models, param_grids, logger)
    plot_results(experiment, results, logger)

    logger.info("Aplikácia skončila úspešne.")


if __name__ == "__main__":
    main()
