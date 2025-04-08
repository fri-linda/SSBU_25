from shiny import App, render, reactive, ui
import pandas as pd

import app_ui as shiny_ui
import data_init as data
import utils


def server(input, output, session):
    patient_data_dict = reactive.Value(data.data)
    conditional_ui = reactive.Value(None)
    txt_status = reactive.Value("")

    # Define ranges and descriptions for each measurement type
    measurement_ranges = {
        "Cholesterol": {"min": 170, "max": 230, "description": "Cholesterol (mg/dL)"},
        "Blood Pressure": {"min": 90, "max": 150, "description": "Blood Pressure (mmHg)"},
        "Glucose": {"min": 80, "max": 140, "description": "Glucose (mg/dL)"}
    }

    # INPUTS

    @reactive.Effect
    @reactive.event(input.add_patient)
    def add_patient_event():
        file_info = input.file1()

        # Validate input
        if not file_info:
            txt_status.set("Error: Please upload a CSV file.")
            return

        result = utils.update_patient_data(patient_data_dict.get(), file_info)
        txt_status.set(result)

    @reactive.Effect
    @reactive.event(input.generate_data)
    def generate_data_event():
        patient_id = input.patient_id()
        result = utils.generate_data_for_patient(patient_data_dict.get(), patient_id)
        txt_status.set(result)

    @reactive.Effect
    @reactive.event(input.view_type)
    def view_type_change_event():
        view_type = input.view_type()
        if view_type == data.views['graph']:
            conditional_ui.set(data.dynamic_ui_elements['graph_type'])
        elif view_type in [data.views['summary'], data.views['table']]:
            conditional_ui.set(data.dynamic_ui_elements['stats'])
        else:
            conditional_ui.set(None)  # Clear the dynamic UI

    # OUTPUTS

    @output
    @render.ui
    def dynamic_slider():
        # Dynamically update the slider based on the selected measurement type
        measurement_type = input.measurement_type() or "Cholesterol"
        range_info = measurement_ranges[measurement_type]
        return ui.input_slider(
            "value_range",
            range_info["description"],
            min=range_info["min"],
            max=range_info["max"],
            value=[range_info["min"], range_info["max"]]
        )

    @output
    @render.plot
    def data_visualization():
        # Ensure the graph is displayed only when the view type is "Visualization"
        if input.view_type() == data.views['graph']:
            input.generate_data()  # Add dependency on the generate_data event
            patient_id = input.patient_id() or "Patient 1"
            measurement_type = input.measurement_type() or data.measurements[0]
            value_range = input.value_range() or [100, 250]
            graph_type = input.graph_type() or "Line Plot"

            patient_data_df = patient_data_dict.get()[patient_id][measurement_type]
            filtered_data = patient_data_df[(patient_data_df >= value_range[0]) & (patient_data_df <= value_range[1])]

            return utils.create_plot(patient_id, measurement_type, filtered_data, graph_type)

    @output
    @render.text
    def statistical_summary():
        # Ensure the summary updates on generate_data event and applies filtering
        input.generate_data()  # Add dependency on the generate_data event
        if input.view_type() == data.views['summary']:
            patient_id = input.patient_id()
            stats = input.stats()
            value_range = input.value_range()

            # Access the DataFrame for the selected patient
            patient_data_df = patient_data_dict.get()[patient_id]

            return utils.generate_statistical_summary(patient_id, stats, patient_data_df)

    @output
    @render.table
    def patient_data():
        # Ensure the table updates on generate_data event and applies filtering
        input.generate_data()  # Add dependency on the generate_data event
        if input.view_type() == data.views['table']:
            patient_id = input.patient_id()
            selected_measurements = input.stats() or data.measurements
            value_range = input.value_range()

            # Ensure selected_measurements is always a list
            if isinstance(selected_measurements, str):
                selected_measurements = [selected_measurements]
            elif isinstance(selected_measurements, tuple):
                selected_measurements = list(selected_measurements)

            patient_data_df = patient_data_dict.get()[patient_id]

            filtered_data = patient_data_df[selected_measurements].copy()
            measurement_type = input.measurement_type()

            filtered_data = filtered_data[
                (filtered_data[measurement_type] >= value_range[0]) & (filtered_data[measurement_type] <= value_range[1])]

            return filtered_data.reset_index()
        
    @output
    @render.ui
    def dynamic_content():
        return conditional_ui.get()

    @output
    @render.text
    def txt_status_code():
        return txt_status.get()


app = App(shiny_ui.app_ui, server)
