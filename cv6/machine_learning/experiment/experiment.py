from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold, train_test_split
import os


from data.data_handling_refactored import DatasetRefactored
from models.model_optimizer import ModelOptimizer
from models.model_trainer import ModelTrainer

class Experiment:
    """A class to handle the entire experiment of training and evaluating models."""

    def __init__(self, models, models_params, n_replications=10, logger=None):
        """
        Initialize the Experiment with models, their parameters, and number of replications.

        Parameters:
        - models: dict, a dictionary of machine learning model instances.
        - models_params: dict, a dictionary of hyperparameters for the models.
        - n_replications: int, the number of training/evaluation cycles to perform.
        - logger: Logger instance, for logging messages.
        """
        self.models = models
        self.models_params = models_params
        self.n_replications = n_replications
        self.results = pd.DataFrame()
        self.datascaler = DatasetRefactored()
        self.accuracies_file = "outputs/model_accuracies.csv"
        self.logger = logger
        os.makedirs("outputs", exist_ok=True)
        self.__initialize_csv_file()

    def __initialize_csv_file(self):
        """Initialize the CSV file with headers."""
        with open(self.accuracies_file, 'w') as file:
            file.write("Model,Replication,Accuracy,F1 Score,ROC AUC,Best Parameters\n")

    def run(self, X, y):
        """Run the experiment over multiple replications."""
        self.replication_conf_matrices = {model_name: [] for model_name in self.models_params.keys()}

        for replication in range(self.n_replications):
            self.__run_single_replication(replication, X, y)

        self.mean_conf_matrices = self.__calculate_mean_conf_matrices()
        return self.results

    def __run_single_replication(self, replication, X, y):
        """Run a single replication of training and evaluating the models."""
        if self.logger:
            self.logger.info("Starting replication " + str(replication + 1) + '/' + str(self.n_replications))
        else:
            print(f"Starting replication {replication + 1}/{self.n_replications}.")
        X_resampled, y_resampled = self.__balance_dataset(X, y)
        
        for model_name in self.models_params.keys():
            self.__train_and_evaluate_model(model_name, X_resampled, y_resampled, replication)

    def __balance_dataset(self, X, y):
        """Balance the dataset using SMOTE."""
        smote = SMOTE()
        return smote.fit_resample(X, y)

    def __train_and_evaluate_model(self, model_name, X_resampled, y_resampled, replication):
        """Train and evaluate a single model."""
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
        optimizer = ModelOptimizer(self.models[model_name], self.models_params[model_name])

        best_params = optimizer.grid_search(X_resampled, y_resampled, cv=skf)

        # train the model with the best parameters
        trainer = ModelTrainer(self.models[model_name], best_params)

        # split the resampled data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.4)

        # scale the data using the DataScaler class
        X_train, X_test = self.datascaler.scale_data(X_train, X_test, scale_type='normalize')

        # train and evaluate the model
        trainer.train(X_train, y_train)
        accuracy, f1, roc_auc, predictions = trainer.evaluate(X_test, y_test)

        self.__store_results(model_name, replication, accuracy, f1, roc_auc, best_params)
        self.replication_conf_matrices[model_name].append(confusion_matrix(y_test, predictions))

    def __store_results(self, model_name, replication, accuracy, f1, roc_auc, best_params):
        """Store the results of a single evaluation."""
        new_row = pd.DataFrame({
            'model': model_name,
            'replication': replication + 1,
            'accuracy': accuracy,
            'f1_score': f1,
            'roc_auc': roc_auc,
            'best_params': [best_params]
        })
        self.results = pd.concat([self.results, new_row], ignore_index=True)

        # append the results to the CSV file
        with open(self.accuracies_file, 'a') as file:
            file.write(f"{model_name},{replication + 1},{accuracy:.4f},{f1:.4f},{roc_auc:.4f},\"{best_params}\"\n")

    def __calculate_mean_conf_matrices(self):
        """Calculate the mean confusion matrisx for each model."""
        return {model_name: np.mean(np.array(matrices), axis=0)
                for model_name, matrices in self.replication_conf_matrices.items()}