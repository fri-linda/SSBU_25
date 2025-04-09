import seaborn as sns
from matplotlib import pyplot as plt
from plotting.base_plotter import BasePlotter


class ExperimentPlotter(BasePlotter):
    """A class for plotting the results of machine learning experiments."""

    def plot_metric_density(self, results):
        """
        Plots the density distribution of evaluation metrics for each model.

        Parameters:
        - results: DataFrame containing model evaluation results.
        """
        metrics = ['accuracy', 'f1_score', 'roc_auc', 'precision']
        for metric in metrics:
            if metric not in results.columns:
                continue
            plt.figure(figsize=(10, 6))
            for model in results['model'].unique():
                sns.kdeplot(results[results['model'] == model][metric], label=model, fill=True)
            plt.title(f'Distribution of {metric.capitalize()} across replications')
            plt.xlabel(metric.capitalize())
            plt.ylabel('Density')
            plt.legend()
            plt.grid(True)
            plt.savefig(f"outputs/{metric}_density_plot.png")
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
            plt.savefig(f"outputs/{model_name}_over_time.png") 

        self._BasePlotter__generic_plot(
            plot_func,
            title=title,
            xlabel='Replication',
            ylabel=metric_name,
            figsize=(10, 5)
        )

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

    def print_best_model(self, results, metric='f1_score'):
        """
        Prints the best model based on the average value of a selected metric.

        Parameters:
        - results: DataFrame, the experiment results.
        - metric: str, the metric used for evaluation.
        """
        if metric not in results.columns:
            print(f"Metrika '{metric}' sa nenašla vo výsledkoch.")
            return

        avg_scores = results.groupby('model')[metric].mean()
        best_model = avg_scores.idxmax()
        best_score = avg_scores.max()
        print(f"\nNajlepší model podľa metriky {metric} je: {best_model}")
        print(f"Priemerné {metric}: {best_score:.4f}")