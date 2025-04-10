import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

from cv6.machine_learning.plotting.base_plotter import BasePlotter


class DatasetPlotter(BasePlotter):
    """A class for visualizing dataset features."""

    def plot_class_distribution(self, df: pd.DataFrame):
        """
        Plots the distribution of classes in the dataset.

        Parameters:
        - df: DataFrame containing the dataset with a 'target' column.
        """
        self._BasePlotter__generic_plot(sns.countplot, x='target', data=df, title='Class Distribution')

    def plot_correlation_matrix(self, df: pd.DataFrame):
        """
        Plots the correlation matrix of the features in the dataset.

        Parameters:
        - df: DataFrame containing the dataset features.
        """
        self._BasePlotter__generic_plot(sns.heatmap, df.corr(), annot=True, fmt=".2f", cmap='coolwarm',
                                        figsize=(20, 15), title='Feature Correlation Matrix')

    def plot_feature_distributions(self, df: pd.DataFrame):
        """
        Plots the distribution for each feature in the dataset.

        Parameters:
        - df: DataFrame containing the dataset features.
        """
        df.hist(bins=20, figsize=(20, 15))
        plt.tight_layout()
        plt.show()

    def plot_box_plots(self, df: pd.DataFrame, target_col: str):
        """
        Plots box plots for each feature in the dataset split by target class.

        Parameters:
        - df: DataFrame containing the dataset features and target column.
        - target_col: Name of the target column.
        """
        df_melted = pd.melt(df, id_vars=[target_col], var_name="features", value_name="value")
        self._BasePlotter__generic_plot(sns.boxplot, x="features", y="value", hue=target_col, data=df_melted,
                                        xticks_rotation=90, figsize=(10, 6))

    def plot_pair_plot(self, df: pd.DataFrame, features: list, target_col: str):
        """
        Plots pair plots for the selected features in the dataset.

        Parameters:
        - df: DataFrame containing the dataset features and target column.
        - features: List of feature names to include in the pair plot.
        - target_col: Name of the target column.
        """
        plot = sns.pairplot(df, vars=features, hue=target_col, height=2.5)
        plot.fig.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()