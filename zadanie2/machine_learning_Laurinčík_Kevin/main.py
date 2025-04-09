import warnings
from plotting.plot_saver import PlotSaver
import matplotlib.pyplot as plt
import seaborn as sns

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
    experiment = Experiment(models, param_grids, n_replications=25, logger=logger)
    results = experiment.run(dataset.data, dataset.target)
    return experiment, results


def plot_results(experiment, results, logger):
    """
    Plots the results of the experiment.
    """
    logger.info("Generating plots for the experiment results...")
    plotter = ExperimentPlotter()

    # 1. Hustota rozdelenia pre všetky metriky
    density_metrics = ['accuracy', 'f1_score', 'precision']
    for metric in density_metrics:
        if metric in results.columns:
            plt.figure(figsize=(10, 6))
            sns.kdeplot(data=results, x=metric, hue='model', fill=True,
                        common_norm=False, alpha=0.5, palette='viridis')
            plt.title(f'Density Plot of {metric.capitalize()} Scores')
            plt.xlabel(metric.capitalize())
            plt.ylabel('Density')
            plt.tight_layout()
            PlotSaver.save_plot(f"density_{metric}")
            plt.close()

    # 2. Vývoj metrík počas replikácií
    replication_metrics = {
        'accuracy': 'Accuracy per Replication and Average Accuracy',
        'f1_score': 'F1 Score per Replication and Average F1 Score',
        'precision': 'Precision per Replication and Average Precision'
    }

    for metric, title in replication_metrics.items():
        if metric in results.columns:
            metric_results = results.groupby('model')[metric].apply(list).to_dict()

            plt.figure(figsize=(10, 5))
            colors = ['green', 'orange', 'blue']
            for i, (model_name, values) in enumerate(metric_results.items()):
                plt.plot(values, label=f"{model_name} per replication",
                         alpha=0.5, color=colors[i % len(colors)])
                avg_value = sum(values) / len(values)
                plt.axhline(y=avg_value, linestyle='--',
                            color=colors[i % len(colors)],
                            label=f"{model_name} average: {avg_value:.2f}")
            plt.title(title)
            plt.xlabel('Replication')
            plt.ylabel(metric.capitalize())
            plt.legend()
            plt.tight_layout()
            PlotSaver.save_plot(f"{metric}_over_replications")
            plt.close()

    # 3. Konfúzne matice
    plotter.plot_confusion_matrices(experiment.mean_conf_matrices)
    for model_name in experiment.mean_conf_matrices.keys():
        PlotSaver.save_plot(f"confusion_matrix_{model_name.lower().replace(' ', '_')}")

    logger.info("All required plots generated successfully.")

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
