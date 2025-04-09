import warnings
from plotting.plot_saver import PlotSaver

# Suppress specific FutureWarnings from scikit-learn
warnings.filterwarnings("ignore", category=FutureWarning)

from sklearn.linear_model import LogisticRegression
from data.data_handling_refactored import DatasetRefactored
from experiment.experiment import Experiment
from plotting.experiment_plotter import ExperimentPlotter
from utils.logger import Logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def initialize_models_and_params():
    """
    Initializes models and their hyperparameter grids.
    """
    models = {
        "Logistic Regression": LogisticRegression(solver='liblinear'),
        "Random Forest": RandomForestClassifier(),
        "SVM": SVC(probability=True)
    }
    param_grids = {
        "Logistic Regression": {"C": [0.1, 1, 10], "max_iter": [10000]},
        "Random Forest": {
            "n_estimators": [50, 100, 200],
            "max_depth": [None, 5, 10],
            "min_samples_split": [2, 5, 10]
        },
        "SVM": {
            "C": [0.1, 1, 10],
            "kernel": ['linear', 'rbf'],
            "gamma": ['scale', 'auto']
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
    """Run the experiment with increased replications."""
    experiment = Experiment(models, param_grids, n_replications=30, logger=logger)
    results = experiment.run(dataset.data, dataset.target)
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

    # 1. Plot metric density and save
    plotter.plot_metric_density(results)
    PlotSaver.save_plot("metric_density_distribution")

    # 2. Plot accuracy over replications and save
    accuracy_results = experiment.results.groupby('model')['accuracy'].apply(list).to_dict()
    plotter.plot_evaluation_metric_over_replications(
        accuracy_results,
        'Accuracy per Replication and Average Accuracy',
        'Accuracy'
    )
    PlotSaver.save_plot("accuracy_over_replications")

    # 3. Plot precision over replications (new metric from Task 2) and save
    if 'precision' in experiment.results.columns:
        precision_results = experiment.results.groupby('model')['precision'].apply(list).to_dict()
        plotter.plot_evaluation_metric_over_replications(
            precision_results,
            'Precision per Replication and Average Precision',
            'Precision'
        )
        PlotSaver.save_plot("precision_over_replications")

    # 4. Plot confusion matrices and save
    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    for model_name in experiment.mean_conf_matrices.keys():
        PlotSaver.save_plot(f"confusion_matrix_{model_name.lower().replace(' ', '_')}")

    plotter.print_best_parameters(results)

    logger.info("Plots generated and saved successfully.")


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


if __name__ == "__main__":
    main()
