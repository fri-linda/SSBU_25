from sklearn.model_selection import GridSearchCV
from sklearn.utils.validation import check_X_y


class ModelOptimizer:
    """A class for optimizing hyperparameters of machine learning models."""

    def __init__(self, model, param_grid):
        """
        Initialize the ModelOptimizer instance.

        Parameters:
        - model: scikit-learn model, the machine learning model for which hyperparameters are to be optimized.
        - param_grid: dict, the grid of hyperparameters to search over.
        """
        self.model = model
        self.param_grid = param_grid

    def grid_search(self, X_train, y_train, cv=5, scoring='accuracy'):
        """
        Perform grid search to find the best hyperparameters for the model.

        Parameters:
        - X_train: array-like, training features.
        - y_train: array-like, training labels.
        - cv: int, number of cross-validation folds.
        - scoring: str, scoring metric to optimize.

        Returns:
        - best_params: dict, the best hyperparameters found during grid search.
        """
        X_train, y_train = check_X_y(X_train, y_train, ensure_all_finite=True)
        grid_search = GridSearchCV(self.model, self.param_grid, cv=cv, scoring=scoring, n_jobs=-1)
        grid_search.fit(X_train, y_train)
        return grid_search.best_params_