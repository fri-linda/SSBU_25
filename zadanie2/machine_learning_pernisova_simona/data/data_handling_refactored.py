import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from typing import Tuple


class DatasetRefactored:
    """
    This class handles loading, preprocessing, and analyzing the breast cancer dataset.
    """

    def __init__(self):
        """
        Initializes the DatasetRefactored class by loading and cleaning the data.
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
        df = self.to_dataframe()
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        self.target = df['target'].values
        self.data = df.drop('target', axis=1).values

    def to_dataframe(self) -> pd.DataFrame:
        """
        Converts the dataset into a pandas DataFrame.

        Returns:
        - DataFrame containing the features and target.
        """
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df['target'] = self.target
        return df

    def split_data(self, test_size: float = 0.2, stratify: bool = True, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Splits the dataset into training and testing sets.

        Parameters:
        - test_size: float, proportion of the dataset to include in the test split.
        - stratify: bool, whether to stratify the split based on the target.
        - random_state: int, random seed for reproducibility.

        Returns:
        - X_train: array-like, training features.
        - X_test: array-like, testing features.
        - y_train: array-like, training labels.
        - y_test: array-like, testing labels.
        """
        stratify_param = self.target if stratify else None
        return train_test_split(self.data, self.target, test_size=test_size, stratify=stratify_param, random_state=random_state)

    def scale_data(self, X_train: np.ndarray, X_test: np.ndarray, scale_type: str = 'standard') -> Tuple[np.ndarray, np.ndarray]:
        """
        Scales the training and test datasets using the specified scaling method.

        Parameters:
        - X_train: array-like, training features.
        - X_test: array-like, testing features.
        - scale_type: str, type of scaling ('standard' or 'normalize').

        Returns:
        - X_train_scaled: array-like, scaled training features.
        - X_test_scaled: array-like, scaled testing features.
        """
        scalers = {
            'standard': StandardScaler(),
            'normalize': MinMaxScaler()
        }
        scaler = scalers.get(scale_type)
        if not scaler:
            raise ValueError("Invalid scale_type. Choose 'standard' or 'normalize'.")
        return scaler.fit_transform(X_train), scaler.transform(X_test)