from sklearn.model_selection import GridSearchCV
from sklearn.utils.validation import check_X_y

class ModelOptimizer:
    """Trieda pre optimalizáciu hyperparametrov modelov strojového učenia."""
    def __init__(self, model, param_grid):
        self.model = model
        self.param_grid = param_grid

    def grid_search(self, X_train, y_train, cv=5, scoring='accuracy'):
        X_train, y_train = check_X_y(X_train, y_train, ensure_all_finite=True)
        grid_search = GridSearchCV(self.model, self.param_grid, cv=cv, scoring=scoring, n_jobs=-1)
        grid_search.fit(X_train, y_train)
        return grid_search.best_params_
