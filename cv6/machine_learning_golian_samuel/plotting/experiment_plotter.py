import seaborn as sns
from matplotlib import pyplot as plt
from plotting.base_plotter import BasePlotter
import os

class ExperimentPlotter(BasePlotter):
    """A class for plotting the results of machine learning experiments."""

    def __init__(self):
        super().__init__()
        os.makedirs("machine_learning/plots", exist_ok=True)

    def save_plot(self, filename):
        """Save the current plot to a file."""
        plt.savefig(f"machine_learning/plots/{filename}", bbox_inches='tight')
        plt.show()  # Display the plot in PyCharm
        plt.close()  # Close the plot after displaying and saving

    def plot_metric_density(self, results, metrics=('accuracy', 'f1_score', 'roc_auc', 'precision')):
        """
        Plot density plots for specified metrics.

        Parameters:
        - results: DataFrame containing the results.
        - metrics: List of metrics to plot.
        """
        for metric in metrics:
            plt.figure(figsize=(10, 6))
            sns.kdeplot(data=results, x=metric, hue="model", fill=True, common_norm=False, alpha=0.5)
            plt.title(f'Density Plot of {metric.capitalize()}')
            plt.xlabel(metric.capitalize())
            plt.ylabel('Density')
            plt.legend(title='Model')  # Ensure legend is displayed
            plt.tight_layout()  # Adjust layout to prevent labels from being cut off
            self.save_plot(f'density_plot_{metric}.png')

    def plot_evaluation_metric_over_replications(self, all_metric_results, title, metric_name):
        """
        Plot accuracies for each model over all replications and display the average accuracy.

        Parameters:
        - all_metric_results: Dict containing accuracies for each model.
        - title: str, title of the plot.
        - metric_name: str, name of the metric to display on the y-axis.
        """
        plt.figure(figsize=(10, 5))
        colors = ['green', 'orange', 'blue']
        for i, (model_name, values) in enumerate(all_metric_results.items()):
            plt.plot(values, label=f"{model_name} per replication", alpha=0.5, color=colors[i % len(colors)])
            avg_accuracy = sum(values) / len(values)
            plt.axhline(y=avg_accuracy, linestyle='--', color=colors[i % len(colors)],
                        label=f"{model_name} average {metric_name.lower()}: {avg_accuracy:.2f}")
        plt.title(title)
        plt.xlabel('Replication')
        plt.ylabel(metric_name)
        plt.legend()
        plt.tight_layout()  # Adjust layout to prevent labels from being cut off
        self.save_plot(f'{metric_name.lower()}_over_replications.png')

    def plot_confusion_matrices(self, confusion_matrices):
        """
        Plot the average confusion matrix for each model.

        Parameters:
        - confusion_matrices: Dict containing the average confusion matrix for each model.
        """
        for model_name, matrix in confusion_matrices.items():
            plt.figure(figsize=(6, 5))
            sns.heatmap(matrix, annot=True, fmt='.2f', cmap='Blues', cbar=False)
            plt.title(f'Average Confusion Matrix: {model_name}')
            plt.xlabel('Predicted label')
            plt.ylabel('True label')
            plt.tight_layout()  # Adjust layout to prevent labels from being cut off
            self.save_plot(f'confusion_matrix_{model_name}.png')

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