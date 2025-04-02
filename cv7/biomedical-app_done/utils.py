import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import data_init as data

def update_patient_data(patient_data_dict, file_info):
    # Autogenerate patient ID
    last_id = max(int(pid.split(" ")[1]) for pid in data.patient_ids)
    new_patient_id = f"Patient {last_id + 1}"

    if file_info:
        try:
            # Read the CSV file and set the 'Date' column as the index
            new_data = pd.read_csv(file_info[0]["datapath"], parse_dates=["Date"], index_col="Date")
            data.patient_ids.append(new_patient_id)
            patient_data_dict[new_patient_id] = new_data
            return f"Patient Data for {new_patient_id} read from CSV successfully"
        except Exception as e:
            return f"Error reading CSV file: {str(e)}"
    else:
        return "Error: No file provided."

def generate_data_for_patient(patient_data_dict, patient_id):
    if patient_id not in patient_data_dict:
        return f"Error: Patient ID '{patient_id}' does not exist."

    latest_date = patient_data_dict[patient_id].index.max() + pd.DateOffset(months=1)
    new_data = {
        "Cholesterol": [np.random.normal(200, 30)],  # Cholesterol: 170-230 mg/dL
        "Blood Pressure": [np.random.normal(120, 15)],  # Blood Pressure: 90-150 mmHg
        "Glucose": [np.random.normal(100, 20)],  # Glucose: 80-140 mg/dL
    }
    new_row = pd.DataFrame(new_data, index=[latest_date])
    patient_data_dict[patient_id] = pd.concat([patient_data_dict[patient_id], new_row])
    return f"Data for {patient_id} updated successfully."

def generate_statistical_summary(patient_id, stats, filtered_data):
    summary_str = ""
    for measurement in stats:
        measurement_data = filtered_data[measurement]  # Access the measurement directly from the DataFrame
        desc = measurement_data.describe()
        stats_lines = [
            f"| Count: {desc['count']:>10.0f} |",
            f"Mean: {desc['mean']:>10.2f} |",
            f"Std: {desc['std']:>10.2f} |",
            f"Min: {desc['min']:>10.2f} |",
            f"25%: {desc['25%']:>10.2f} |",
            f"50%: {desc['50%']:>10.2f} |",
            f"75%: {desc['75%']:>10.2f} |",
            f"Max: {desc['max']:>10.2f} |",
        ]
        measurement_summary = f"{measurement} Summary:\n" + "\n".join(stats_lines) + "\n\n"
        summary_str += measurement_summary
    return summary_str

def create_plot(patient_id, measurement_type, filtered_data, graph_type):
    fig, ax = plt.subplots()

    if graph_type == "Line Plot":
        ax.plot(filtered_data.index, filtered_data)
    elif graph_type == "Histogram":
        ax.hist(filtered_data, bins=15)

    ax.grid(True, which='both')
    ax.set_title(f"{measurement_type} for {patient_id}")
    ax.set_xlabel("Date" if graph_type == "Line Plot" else "Value Range")
    ax.set_ylabel(measurement_type)
    plt.tight_layout()
    return fig
