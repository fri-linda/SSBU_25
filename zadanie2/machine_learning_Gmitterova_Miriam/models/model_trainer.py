from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.utils.validation import check_X_y, check_array
from sklearn.metrics import precision_score


class ModelTrainer:
    """A class for training and evaluating machine learning models."""

    def __init__(self, model, parameters):
        """
        Initialize the ModelTrainer instance.

        Parameters:
        - model: scikit-learn model, the machine learning model to be trained.
        - parameters: dict, hyperparameters for the model.
        """
        self.model = model
        self.parameters = parameters


    def train(self, X_train, y_train):
        """
        Train the model on the training data.

        Parameters:
        - X_train: array-like, training features.
        - y_train: array-like, training labels.
        """
        #X_train, y_train = check_X_y(X_train, y_train, ensure_all_finite=True)
        X_train, y_train = check_X_y(X_train, y_train)

        self.model.set_params(**self.parameters)
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """
        Evaluate the model on the test data.

        Parameters:
        - X_test: array-like, test features.
        - y_test: array-like, test labels.

        Returns:
        - accuracy: float, accuracy of the model on the test data.
        - f1: float, F1 score of the model on the test data.
        - roc_auc: float, ROC AUC of the model on the test data.
        - predictions: array, predicted labels for the test data.
        """
        #X_test = check_array(X_test, ensure_all_finite=True)
        X_test = check_array(X_test)

        #y_test = check_array(y_test, ensure_2d=False, ensure_all_finite=True)
        y_test = check_array(y_test, ensure_2d=False)

        predictions = self.model.predict(X_test)
        prob_predictions = self.model.predict_proba(X_test)[:, 1] if hasattr(self.model, "predict_proba") else [0] * len(
            y_test)

        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)
        roc_auc = roc_auc_score(y_test, prob_predictions)

        precision = precision_score(y_test, predictions)

        return accuracy, f1, roc_auc, precision, predictions