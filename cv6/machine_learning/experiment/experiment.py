from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold, train_test_split
import os
from sklearn.base import clone

from cv6.machine_learning.data.data_handling_refactored import DatasetRefactored
from cv6.machine_learning.models.model_optimizer import ModelOptimizer
from cv6.machine_learning.models.model_trainer import ModelTrainer


class Experiment:
    """Trieda na spracovanie celého experimentu trénovania a vyhodnocovania modelov."""

    def __init__(self, models, models_params, n_replications=10, logger=None):
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
        with open(self.accuracies_file, 'w') as file:
            file.write("Model,Replication,Accuracy,F1 Score,ROC AUC,Precision,Best Parameters\n")

    def run(self, X, y):
        self.replication_conf_matrices = {model_name: [] for model_name in self.models_params.keys()}
        for replication in range(self.n_replications):
            self.__run_single_replication(replication, X, y)
        self.mean_conf_matrices = self.__calculate_mean_conf_matrices()
        return self.results

    def __run_single_replication(self, replication, X, y):
        if self.logger:
            self.logger.info("Spúšťam replikáciu " + str(replication + 1) + '/' + str(self.n_replications))
        else:
            print(f"Spúšťam replikáciu {replication + 1}/{self.n_replications}.")
        X_resampled, y_resampled = self.__balance_dataset(X, y)
        for model_name in self.models_params.keys():
            self.__train_and_evaluate_model(model_name, X_resampled, y_resampled, replication)

    def __balance_dataset(self, X, y):
        smote = SMOTE()
        return smote.fit_resample(X, y)

    def __train_and_evaluate_model(self, model_name, X_resampled, y_resampled, replication):
        # Vytvorenie kópie modelu, aby každá replikácia začínala čistou inštanciou
        model_instance = clone(self.models[model_name])

        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
        optimizer = ModelOptimizer(model_instance, self.models_params[model_name])
        best_params = optimizer.grid_search(X_resampled, y_resampled, cv=skf)

        trainer = ModelTrainer(model_instance, best_params)
        X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.4)
        X_train, X_test = self.datascaler.scale_data(X_train, X_test, scale_type='normalize')

        trainer.train(X_train, y_train)
        accuracy, f1, roc_auc, precision, predictions = trainer.evaluate(X_test, y_test)

        self.__store_results(model_name, replication, accuracy, f1, roc_auc, precision, best_params)
        self.replication_conf_matrices[model_name].append(confusion_matrix(y_test, predictions))

    def __store_results(self, model_name, replication, accuracy, f1, roc_auc, precision, best_params):
        new_row = pd.DataFrame({
            'model': [model_name],
            'replication': [replication + 1],
            'accuracy': [accuracy],
            'f1_score': [f1],
            'roc_auc': [roc_auc],
            'precision': [precision],
            'best_params': [best_params]
        })
        self.results = pd.concat([self.results, new_row], ignore_index=True)
        with open(self.accuracies_file, 'a') as file:
            file.write(
                f"{model_name},{replication + 1},{accuracy:.4f},{f1:.4f},{roc_auc:.4f},{precision:.4f},\"{best_params}\"\n")

    def __calculate_mean_conf_matrices(self):
        return {model_name: np.mean(np.array(matrices), axis=0)
                for model_name, matrices in self.replication_conf_matrices.items()}
