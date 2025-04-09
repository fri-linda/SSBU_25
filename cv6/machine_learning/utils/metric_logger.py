# utils/metric_logger.py

import csv
import os

def log_metrics_to_csv(run_id, model_name, accuracy, f1_score, roc_auc, file_path="outputs/model_accuracies.csv"):
    """
    Logs evaluation metrics to a CSV file.

    Parameters:
    - run_id: int, index replikácie
    - model_name: str, názov modelu
    - accuracy: float
    - f1_score: float
    - roc_auc: float
    - file_path: str, kam sa má CSV uložiť
    """
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["run_id", "model_name", "accuracy", "f1_score", "roc_auc"])
        writer.writerow([run_id, model_name, accuracy, f1_score, roc_auc])
