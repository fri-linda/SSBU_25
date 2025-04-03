from shiny import ui

import data_init as data

app_ui = ui.page_fluid(
    # Inline CSS for table styling
    ui.tags.style("""
        table.dataframe {
            width: 100%;
            border-collapse: collapse;
        }
        table.dataframe th, table.dataframe td {
            text-align: center;
            vertical-align: middle;
            border: 1px solid #ddd;
            padding: 8px;
        }
        table.dataframe th {
            background-color: #f2f2f2;
        }
    """),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.panel_title("Biomedical Data Visualization and Analysis"),
            ui.output_text("txt_status_code"),
            ui.input_file("file1", "Choose CSV File", accept=".csv"),
            ui.input_action_button("add_patient", "Add Patient"),
            ui.input_text("patient_id", "Select Patient", placeholder="Patient ID", value="Patient 1"),
            ui.input_select("measurement_type", "Select Measurement Type", choices=data.measurements),
            # Make the slider dynamic by rendering it in the server
            ui.output_ui("dynamic_slider"),
            ui.input_action_button("generate_data", "Generate Data"),
            ui.input_radio_buttons("view_type", "Choose View",
                                   choices=list(data.views.values()), selected="Visualization"),
            # Dynamic UI element
            ui.output_ui("dynamic_content"),
        ),
        ui.card(
            ui.output_text("statistical_summary"),
            ui.output_table("patient_data"),
            ui.output_plot("data_visualization"),
        )
    )
)