import seaborn as sns
from matplotlib import pyplot as plt
import os
from cv6.machine_learning.plotting.base_plotter import BasePlotter

class ExperimentPlotter(BasePlotter):
    """Trieda pre vizualizáciu výsledkov experimentov."""
    def __init__(self):
        # Vytvorenie adresára pre ukladanie grafov
        os.makedirs("machine_learning/graphs", exist_ok=True)

    def plot_metric_density(self, results, metrics=('accuracy', 'f1_score', 'roc_auc', 'precision')):
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
            filename = f"machine_learning/graphs/density_{metric}.png"
            plt.savefig(filename)
            plt.close()

    def plot_evaluation_metric_over_replications(self, all_metric_results, title, metric_name):
        def plot_func():
            colors = ['green', 'orange', 'blue']
            for i, (model_name, values) in enumerate(all_metric_results.items()):
                plt.plot(values, label=f"{model_name} per replication", alpha=0.5, color=colors[i % len(colors)])
                avg_metric = sum(values) / len(values)
                plt.axhline(y=avg_metric, linestyle='--', color=colors[i % len(colors)],
                            label=f"{model_name} average {metric_name.lower()}: {avg_metric:.2f}")
            plt.legend()
        self._BasePlotter__generic_plot(
            plot_func,
            title=title,
            xlabel='Replication',
            ylabel=metric_name,
            figsize=(10, 5)
        )
        filename = f"machine_learning/graphs/evaluation_{metric_name.lower()}.png"
        plt.savefig(filename)
        plt.close()

    def plot_confusion_matrices(self, confusion_matrices):
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
            filename = f"machine_learning/graphs/confusion_matrix_{model_name.replace(' ', '_')}.png"
            plt.savefig(filename)
            plt.close()

    def print_best_parameters(self, results):
        for model_name in results['model'].unique():
            model_results = results[results['model'] == model_name]
            best_params_list = model_results['best_params'].value_counts().index[0]
            print(f"Najčastejšie zvolené najlepšie parametre pre {model_name}: {best_params_list}")
