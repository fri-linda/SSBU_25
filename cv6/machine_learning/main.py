import warnings
import matplotlib.pyplot as plt
import os

from sklearn.neighbors import KNeighborsClassifier

# Suppress specific FutureWarnings from scikit-learn
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.linear_model import LogisticRegression
from data.data_handling_refactored import DatasetRefactored
from experiment.experiment import Experiment
from cv6.machine_learning.plotting.experiment_plotter import ExperimentPlotter
from utils.logger import Logger


def initialize_models_and_params():
    """
    Initializes models and their hyperparameter grids.

    Returns:
    - models: dict, dictionary of model instances.
    - param_grids: dict, dictionary of hyperparameter grids.
    """
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        "K-Nearest Neighbors": KNeighborsClassifier(),
    }
    param_grids = {
        "Logistic Regression": {"C": [0.1, 1, 10], "max_iter": [10000]},
        "K-Nearest Neighbors": {
            "n_neighbors": [3, 5, 7],
            "weights": ['uniform', 'distance'],
            "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
        }
    }
    return models, param_grids


def run_experiment(dataset, models, param_grids, logger):
    """
    Runs the experiment with the given dataset, models, and hyperparameter grids.

    Parameters:
    - dataset: Dataset instance, the dataset to use.
    - models: dict, dictionary of model instances.
    - param_grids: dict, dictionary of hyperparameter grids.
    - logger: Logger instance, for logging messages.

    Returns:
    - experiment: Experiment instance, the experiment object.
    - results: DataFrame, the results of the experiment.
    """
    logger.info("Starting the experiment...")
    # Set the number of replications to a higher value
    n_replications = 120      # You can adjust this number as needed
    experiment = Experiment(models, param_grids, n_replications=n_replications, logger=logger)
    results = experiment.run(dataset.data, dataset.target)
    logger.info("Experiment completed successfully.")
    return experiment, results


def plot_results(experiment, results, logger):
    """
    Plots the results of the experiment.

    Parameters:
    - experiment: Experiment instance, the experiment object.
    - results: DataFrame, the results of the experiment.
    - logger: Logger instance, for logging messages.
    """
    logger.info("Generating plots for the experiment results...")
    plotter = ExperimentPlotter()
    plotter.plot_metric_density(results)
    save_plot('accuracy_density_plot.png')
    plotter.plot_evaluation_metric_over_replications(
        experiment.results.groupby('model')['accuracy'].apply(list).to_dict(),
        'Accuracy per Replication and Average Accuracy', 'Accuracy')
    save_plot('accuracy_over_replications.png')
    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    save_plot('confusion_matrices.png')
    plotter.print_best_parameters(results)
    save_plot('best_parameters.png')
    plotter.plot_recall_over_replications(
        experiment.results.groupby('model')['recall'].apply(list).to_dict()
    )
    save_plot('recall_over_replications.png')
    logger.info("Plots generated successfully.")


def main():
    """
    Main function to execute the model training and evaluation pipeline.

    Initializes the dataset, defines models and their parameter grids,
    and invokes the replication of model training and evaluation.
    """
    logger = Logger(log_file="outputs/application.log")
    logger.info("Application started.")

    dataset = DatasetRefactored()
    models, param_grids = initialize_models_and_params()
    experiment, results = run_experiment(dataset, models, param_grids, logger)
    plot_results(experiment, results, logger)

    logger.info("Application finished successfully.")





def save_plot(filename):
    plots_dir = 'machine_learning/plots'
    os.makedirs(plots_dir, exist_ok=True)
    plt.savefig(os.path.join(plots_dir, filename))
    plt.close()

if __name__ == "__main__":
    main()