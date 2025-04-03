import numpy as np
import pandas as pd
from shiny import ui

np.random.seed(42)
patient_ids = [f"Patient {i}" for i in range(1, 11)]
dates = pd.date_range(start="2023-01-01", periods=12, freq="ME")
measurements = ["Cholesterol", "Blood Pressure", "Glucose"]
views = {"graph": "Visualization", "summary": "Statistical Summary", "table": "Patient Data Table"}

# Store each patient's data in a dictionary of DataFrames with realistic ranges
data = {
    patient: pd.DataFrame(
        {
            "Cholesterol": np.random.normal(200, 30, len(dates)),  # Cholesterol: 170-230 mg/dL
            "Blood Pressure": np.random.normal(120, 15, len(dates)),  # Blood Pressure: 90-150 mmHg
            "Glucose": np.random.normal(100, 20, len(dates)),  # Glucose: 80-140 mg/dL
        },
        index=dates,
    )
    for patient in patient_ids
}

dynamic_ui_elements = {
    'graph_type': ui.input_radio_buttons("graph_type", "Select Graph Type", 
                                         choices=["Line Plot", "Histogram"],
                                         selected="Line Plot"),
    'stats': ui.input_checkbox_group("stats", "Summary Stats", choices=measurements, selected=measurements)
}