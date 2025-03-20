import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from typing import Tuple, List, Optional, Callable

class Dataset:
    """
    This class handles loading, preprocessing, analyzing, and visualizing the breast cancer dataset.
    """

    def __init__(self):
        """
        Initializes the Dataset class by loading and cleaning the data.
        """
        data = load_breast_cancer()
        self.data, self.target = data.data, data.target
        self.feature_names = data.feature_names
        self.target_names = data.target_names
        self.__load_and_clean_data()

    def __load_and_clean_data(self):
        """
        Cleans the data by removing duplicates and handling missing values.
        """
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df['target'] = self.target
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        self.target = df['target'].values
        self.data = df.drop('target', axis=1).values

    def __generic_plot(self, plot_func: Callable, *args, **kwargs):
        """
        A generic plotting function to reduce redundancy in plotting methods.
        """
        general_kwargs = {key: kwargs.pop(key, None) for key in ['title', 'xlabel', 'ylabel', 'xticks_rotation', 'yticks', 'yticklabels', 'xticks']}
        plt.figure(figsize=kwargs.pop('figsize', (10, 6)))
        plot_func(*args, **kwargs)  # Capture the plot object for functions like sns.pairplot
        if general_kwargs['title']:
            plt.title(general_kwargs['title'])
        if general_kwargs['xlabel']:
            plt.xlabel(general_kwargs['xlabel'])
        if general_kwargs['ylabel']:
            plt.ylabel(general_kwargs['ylabel'])
        if general_kwargs['xticks_rotation']:
            plt.xticks(rotation=general_kwargs['xticks_rotation'])
        if general_kwargs['xticks'] is not None:
            plt.xticks(ticks=general_kwargs['xticks'])
        if general_kwargs['yticks'] is not None and general_kwargs['yticklabels'] is not None:
            plt.yticks(ticks=general_kwargs['yticks'], labels=general_kwargs['yticklabels'])
        plt.tight_layout()
        plt.show()

    def split_data(self, test_size: float = 0.2, stratify: bool = True, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Splits the dataset into training and testing sets.
        """
        stratify_param = self.target if stratify else None
        return train_test_split(self.data, self.target, test_size=test_size, stratify=stratify_param, random_state=random_state)

    def scale_data(self, X_train: np.ndarray, X_test: np.ndarray, scale_type: str = 'standard') -> Tuple[np.ndarray, np.ndarray]:
        """
        Scales the training and test datasets using the specified scaling method.
        """
        scalers = {
            'standard': StandardScaler(),
            'normalize': MinMaxScaler()
        }
        scaler = scalers.get(scale_type)
        if not scaler:
            raise ValueError("Invalid scale_type. Choose 'standard' or 'normalize'.")
        return scaler.fit_transform(X_train), scaler.transform(X_test)

    def visualize_feature_distribution(self, feature_index: int, scaled_data: Optional[np.ndarray] = None, title_suffix: str = ""):
        """
        Visualizes the distribution of a specific feature before and after scaling using boxplots.
        """
        if feature_index < 0 or feature_index >= len(self.feature_names):
            raise IndexError("Invalid feature index. Please provide a valid index.")

        feature_name = self.feature_names[feature_index]
        original_feature = self.data[:, feature_index]

        self.__generic_plot(sns.boxplot, data=original_feature, color='blue', width=0.3,
                            title=f"Boxplot of Feature: {feature_name} {title_suffix}", xlabel=feature_name, ylabel="Value")

        if scaled_data is not None:
            scaled_feature = scaled_data[:, feature_index]
            self.__generic_plot(sns.boxplot, data=scaled_feature, color='orange', width=0.3,
                                title=f"Boxplot of Scaled Feature: {feature_name} {title_suffix}", xlabel=feature_name, ylabel="Value")

    def plot_class_distribution(self):
        """
        Plots the distribution of classes in the dataset.
        """
        df = pd.DataFrame({'target': self.target})
        self.__generic_plot(sns.countplot, x='target', data=df, title='Class Distribution')

    def plot_correlation_matrix(self):
        """
        Plots the correlation matrix of the features in the dataset.
        """
        df = pd.DataFrame(self.data, columns=self.feature_names)
        self.__generic_plot(sns.heatmap, df.corr(), annot=True, fmt=".2f", cmap='coolwarm',
                            figsize=(20, 15), title='Feature Correlation Matrix')

    def feature_importance(self):
        """
        Determines the importance of each feature using a random forest classifier and plots the results.
        """
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(self.data, self.target)
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]

        self.__generic_plot(plt.bar, range(self.data.shape[1]), importances[indices], align='center',
                            title='Feature Importances', xlabel='Features', ylabel='Importance',
                            xticks=range(self.data.shape[1]), xticks_rotation=90,
                            figsize=(10, 6))

    def plot_feature_distributions(self):
        """
        Plots the distribution for each feature in the dataset.
        """
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df.hist(bins=20, figsize=(20, 15))  # Directly call the DataFrame's hist method
        plt.tight_layout()  # Ensure proper layout
        plt.show()  # Display the figure

    def plot_box_plots(self, scaled_data: Optional[np.ndarray] = None, target: Optional[np.ndarray] = None):
        """
        Plots box plots for each feature in the dataset split by target class.
        If scaled_data is provided, it uses the scaled data for plotting.
        The target parameter must match the length of the provided data.
        """
        data_to_plot = scaled_data if scaled_data is not None else self.data
        target_to_plot = target if target is not None else self.target

        if len(data_to_plot) != len(target_to_plot):
            raise ValueError("Length of data and target must match.")

        df = pd.DataFrame(data_to_plot, columns=self.feature_names)
        df['target'] = target_to_plot
        df_melted = pd.melt(df, id_vars=["target"], var_name="features", value_name="value")
        self.__generic_plot(sns.boxplot, x="features", y="value", hue="target", data=df_melted,
                            xticks_rotation=90, figsize=(10, 6))

    def plot_pair_plot(self, features: List[str]):
        """
        Plots pair plots for the selected features in the dataset.
        """
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df['target'] = self.target
        plot = sns.pairplot(df, vars=features, hue="target", height=2.5)  # Directly create the pair plot
        plot.fig.suptitle("Pair Plot of Selected Features", y=1.02)  # Add a title with proper spacing
        plt.show()  # Ensure the plot is displayed

    def plot_all_features_before_after_scaling(self, X_train: np.ndarray, X_train_scaled: np.ndarray, scale_type: str):
        """
        Visualizes the distribution of all features before and after scaling using boxplots.
        """
        # plot the original data
        self.__generic_plot(sns.boxplot, data=X_train, orient='h',
                            title=f'Before {scale_type}', ylabel="Features", xlabel="Values",
                            yticks=range(len(self.feature_names)), yticklabels=self.feature_names,
                            figsize=(16, 6))

        # plot the scaled data
        self.__generic_plot(sns.boxplot, data=X_train_scaled, orient='h',
                            title=f'After {scale_type}', ylabel="Features", xlabel="Values",
                            yticks=range(len(self.feature_names)), yticklabels=self.feature_names,
                            figsize=(16, 6))

    def plot_feature_before_after_scaling(self, X_train: np.ndarray, X_train_scaled: np.ndarray, feature_name: str):
        """
        Visualizes the distribution of a specific feature before and after scaling using histograms.
        """
        if feature_name not in self.feature_names:
            raise ValueError(f"Feature '{feature_name}' not found in feature names.")

        feature_index = list(self.feature_names).index(feature_name)
        original_feature = X_train[:, feature_index]
        scaled_feature = X_train_scaled[:, feature_index]

        # plot histogram for original feature
        self.__generic_plot(plt.hist, original_feature, bins=20, color='blue', alpha=0.7,
                            title=f"Before Scaling: {feature_name}", xlabel=feature_name, ylabel="Frequency",
                            figsize=(12, 6))

        # plot histogram for scaled feature
        self.__generic_plot(plt.hist, scaled_feature, bins=20, color='orange', alpha=0.7,
                            title=f"After Scaling: {feature_name}", xlabel=feature_name, ylabel="Frequency",
                            figsize=(12, 6))
