import seaborn as sns
from matplotlib import pyplot as plt
from cv6.machine_learning_zilka_radoslav.plotting.base_plotter import BasePlotter
import os


class ExperimentPlotter(BasePlotter):
    """A class for plotting the results of machine learning experiments."""

    def plot_metric_density(self, results, metrics=('accuracy', 'f1_score', 'roc_auc')):
        """
        Plot density plots for specified metrics.

        Parameters:
        - results: DataFrame containing the results.
        - metrics: List of metrics to plot.
        """
        for metric in metrics:
            self._BasePlotter__generic_plot(
                sns.kdeplot,
                data=results,
                x=metric,
                hue="model",
                fill=True,
                common_norm=False,
                alpha=0.5,
                title=f'Density Plot of {metric.capitalize()}',
                xlabel=metric.capitalize(),
                ylabel='Density',
                figsize=(10, 6)
            )
            plots_dir = 'machine_learning/plots/metric'
            os.makedirs(plots_dir, exist_ok=True)
            plt.savefig(os.path.join(plots_dir, f'metric_density_{metric}.png'))
            plt.close()

    def plot_evaluation_metric_over_replications(self, all_metric_results, title, metric_name):
        """
        Plot accuracies for each model over all replications and display the average accuracy.

        Parameters:
        - all_metric_results: Dict containing accuracies for each model.
        - title: str, title of the plot.
        - metric_name: str, name of the metric to display on the y-axis.
        """

        def plot_func():
            colors = ['green', 'orange', 'blue']
            for i, (model_name, values) in enumerate(all_metric_results.items()):
                plt.plot(values, label=f"{model_name} per replication", alpha=0.5, color=colors[i % len(colors)])
                avg_accuracy = sum(values) / len(values)
                plt.axhline(y=avg_accuracy, linestyle='--', color=colors[i % len(colors)],
                            label=f"{model_name} average accuracy: {avg_accuracy:.2f}")
            plt.legend()

        self._BasePlotter__generic_plot(
            plot_func,
            title=title,
            xlabel='Replication',
            ylabel=metric_name,
            figsize=(10, 5)
        )
        plots_dir = 'machine_learning/plots/evaluation'
        os.makedirs(plots_dir, exist_ok=True)
        plt.savefig(os.path.join(plots_dir, 'accuracy_over_replications.png'))
        plt.close()

    def plot_confusion_matrices(self, confusion_matrices):
        """
        Plot the average confusion matrix for each model.

        Parameters:
        - confusion_matrices: Dict containing the average confusion matrix for each model.
        """
        for model_name, matrix in confusion_matrices.items():
            self._BasePlotter__generic_plot(
                sns.heatmap,
                matrix,
                annot=True,
                fmt='.2f',
                cmap='Blues',
                cbar=False,
                title=f'Average Confusion Matrix: {model_name}',
                xlabel='Predicted label',
                ylabel='True label',
                figsize=(6, 5)
            )
            plots_dir = 'machine_learning/plots/confusion_matrices'
            os.makedirs(plots_dir, exist_ok=True)
            plt.savefig(os.path.join(plots_dir, f'confusion_matrix_{model_name}.png'))
            plt.close()

    def print_best_parameters(self, results):
        """
        Print the most frequently chosen best parameters for each model.

        Parameters:
        - results: DataFrame containing the results.
        """
        for model_name in results['model'].unique():
            model_results = results[results['model'] == model_name]
            best_params_list = model_results['best_params'].value_counts().index[0]
            print(f"Most frequently chosen best parameters for {model_name}: {best_params_list}")

    def plot_recall_over_replications(self, recall_scores):
        """
        Plot recall scores over replications for each model.

        Parameters:
        - recall_scores: Dict containing recall scores for each model.
        """
        plt.figure(figsize=(10, 6))
        for model, scores in recall_scores.items():
            plt.plot(scores, marker='o', label=model)
        plt.title('Recall over Replications')
        plt.xlabel('Replication')
        plt.ylabel('Recall')
        plt.legend()
        plt.grid()

        plots_dir = 'machine_learning/plots/recall'
        os.makedirs(plots_dir, exist_ok=True)
        plt.savefig(os.path.join(plots_dir, 'recall_over_replications.png'))
        plt.close()