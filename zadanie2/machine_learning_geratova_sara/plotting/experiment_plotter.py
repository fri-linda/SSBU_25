import seaborn as sns
from matplotlib import pyplot as plt
from plotting.base_plotter import BasePlotter
import os


class ExperimentPlotter(BasePlotter):
    """A class for plotting the results of machine learning experiments."""

    def __init__(self):
        # Zabezpečíme, že adresár 'machine_learning_geratova_sara' existuje pre ukladanie grafov.
        os.makedirs("machine_learning_geratova_sara", exist_ok=True)

    def plot_metric_density(self, results, metrics=('accuracy', 'f1_score', 'roc_auc')):
        """
        Vykreslí hustotu rozdelenia (density plot) pre zadané metriky pre každý model.

        Grafy budú uložené do adresára machine_learning_geratova_sara pod názvami:
        density_accuracy.png, density_f1_score.png, density_roc_auc.png.
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
                figsize=(10, 6),
                save_path=f"machine_learning_geratova_sara/density_{metric}.png"
            )

    def plot_evaluation_metric_over_replications(self, all_metric_results, title, metric_name):
        """
        Vykreslí priebeh zvolenej metriky (napr. Accuracy alebo F1 score) počas replikácií pre jednotlivé modely.

        Graf sa uloží do súboru v adresári machine_learning_geratova_sara s názvom:
        <metric_name_lowercase>_over_replications.png
        """

        def plot_func():
            colors = ['green', 'orange', 'blue']
            for i, (model_name, values) in enumerate(all_metric_results.items()):
                plt.plot(values, label=f"{model_name} per replication", alpha=0.5, color=colors[i % len(colors)])
                avg = sum(values) / len(values)
                plt.axhline(y=avg, linestyle='--', color=colors[i % len(colors)],
                            label=f"{model_name} average {metric_name.lower()}: {avg:.2f}")
            plt.legend()

        self._BasePlotter__generic_plot(
            plot_func,
            title=title,
            xlabel='Replication',
            ylabel=metric_name,
            figsize=(10, 5),
            save_path=f"machine_learning_geratova_sara/{metric_name.lower()}_over_replications.png"
        )

    def plot_confusion_matrices(self, confusion_matrices):
        """
        Vykreslí a uloží priemernú confusion matrix pre každý model.
        Súbory budú uložené do adresára machine_learning_geratova_sara s názvom:
        conf_matrix_<model_nazov>.png
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
                figsize=(6, 5),
                save_path=f"machine_learning_geratova_sara/conf_matrix_{model_name.replace(' ', '_')}.png"
            )

    def print_best_parameters(self, results):
        """
        Vypíše najčastejšie zvolené optimálne parametre pre každý model.

        Výpis prebehne do konzoly.
        """
        for model_name in results['model'].unique():
            model_results = results[results['model'] == model_name]
            best_params_list = model_results['best_params'].value_counts().index[0]
            print(f"Most frequently chosen best parameters for {model_name}: {best_params_list}")
