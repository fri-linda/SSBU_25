# main.py

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC  # <-- Pridávame nový model: SVM


from data.data_handling_refactored import DatasetRefactored
from experiment.experiment import Experiment
from plotting.  experiment_plotter import ExperimentPlotter
from utils.logger import Logger

def initialize_models_and_params():
    """
    Initializes models and their hyperparameter grids.

    V rámci Úlohy 1 (1b) sme pridali ďalší model strojového učenia (SVM)
    a definovali jeho parametre a hodnoty pre Grid Search.
    """
    # Pôvodný model
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        # Nový model - SVM
        "SVM": SVC(probability=True)
    }

    # Hyperparametre pre jednotlivé modely
    param_grids = {
        "Logistic Regression": {
            "C": [0.1, 1, 10],
            "max_iter": [10000]
        },
        # Parametre a hodnoty pre Grid Search pre SVM
        "SVM": {
            "C": [0.1, 1, 10],
            "kernel": ["linear", "rbf"]
        }
    }

    return models, param_grids


def run_experiment(dataset, models, param_grids, logger):
    """
    Runs the experiment with the given dataset, models, and hyperparameter grids.
    """
    logger.info("Starting the experiment...")
    experiment = Experiment(models, param_grids, logger=logger)
    results = experiment.run(dataset.data, dataset.target)
    logger.info("Experiment completed successfully.")
    return experiment, results


def plot_results(experiment, results, logger):
    """
    Plots the results of the experiment.
    """
    logger.info("Generating plots for the experiment results...")
    plotter = ExperimentPlotter()
    plotter.plot_metric_density(results)
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['accuracy'].apply(list).to_dict(),
        'Accuracy per Replication and Average Accuracy',
        'Accuracy'
    )
    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    plotter.print_best_parameters(results)
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['precision'].apply(list).to_dict(),
        'Precision per Replication and Average Precision',
        'Precision'
    )
    logger.info("Plots generated successfully.")


def main():
    logger = Logger(log_file="outputs/application.log")
    logger.info("Application started.")

    dataset = DatasetRefactored()
    models, param_grids = initialize_models_and_params()
    experiment, results = run_experiment(dataset, models, param_grids, logger)
    plot_results(experiment, results, logger)

    logger.info("Application finished successfully.")


if __name__ == "__main__":
    main()
