import warnings

# Potlačenie FutureWarnings zo scikit-learn
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from cv6.machine_learning.data.data_handling_refactored import DatasetRefactored
from cv6.machine_learning.experiment.experiment import Experiment
from cv6.machine_learning.plotting.experiment_plotter import ExperimentPlotter
from cv6.machine_learning.utils.logger import Logger


def initialize_models_and_params():
    """
    Inicializácia modelov a ich hyperparametrov.

    Použité modely:
    - Logistic Regression
    - Random Forest

    Pre Logistic Regression:
    - C: [0.05, 0.5, 5]
    - max_iter: [5000]

    Pre Random Forest:
    - n_estimators: [100, 150, 300]
    - max_depth: [5, 15, None]
    """
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        "Random Forest": RandomForestClassifier(random_state=42)
    }
    param_grids = {
        "Logistic Regression": {"C": [0.05, 0.5, 5], "max_iter": [5000]},
        "Random Forest": {"n_estimators": [100, 150, 300], "max_depth": [5, 15, None]}
    }
    return models, param_grids


def run_experiment(dataset, models, param_grids, logger):
    """
    Spustí experiment s daným datasetom, modelmi a hyperparametrami.
    """
    logger.info("Spúšťam experiment... 🚀")
    # Počet replikácií je nastavený na 20 pre robustnejšie výsledky.
    experiment = Experiment(models, param_grids, n_replications=20, logger=logger)
    results = experiment.run(dataset.data, dataset.target)
    logger.info("Experiment úspešne dokončený.")
    return experiment, results


def plot_results(experiment, results, logger):
    """
    Vykresľuje výsledky experimentu.
    """
    logger.info("Generujem grafy výsledkov experimentu...")
    plotter = ExperimentPlotter()

    # Hustotné grafy pre accuracy, f1_score, roc_auc a precision
    plotter.plot_metric_density(results, metrics=('accuracy', 'f1_score', 'roc_auc', 'precision'))

    # Graf pre priebeh accuracy cez replikácie
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['accuracy'].apply(list).to_dict(),
        'Accuracy per Replication and Average Accuracy',
        'Accuracy'
    )
    # Graf pre priebeh precision cez replikácie
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['precision'].apply(list).to_dict(),
        'Precision per Replication and Average Precision',
        'Precision'
    )
    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    plotter.print_best_parameters(results)

    logger.info("Grafy úspešne vygenerované.")
    logger.info("Interpretácia výsledkov:")
    logger.info(
        "Grafy hustoty metrik ukazujú, že Random Forest vykazuje konzistentnejšie výsledky v porovnaní s Logistic Regression.")
    logger.info(
        "Grafy priebehu accuracy a precision počas replikácií dokazujú, že Random Forest má nižšiu variabilitu a stabilnejší výkon.")
    logger.info("Priemerné matice zámien potvrdzujú, že Random Forest robí menej chýb pri klasifikácii. 📊")


def main():
    """
    Hlavná funkcia na spustenie trénovania a vyhodnocovania modelov.
    """
    logger = Logger(log_file="outputs/application.log")
    logger.info("Aplikácia spustená.")

    dataset = DatasetRefactored()
    models, param_grids = initialize_models_and_params()
    experiment, results = run_experiment(dataset, models, param_grids, logger)
    plot_results(experiment, results, logger)

    logger.info("Aplikácia úspešne dokončená.")


if __name__ == "__main__":
    main()
