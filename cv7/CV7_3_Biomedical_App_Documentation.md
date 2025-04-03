# CV7: Aplikácia Biomedical Data Visualization and Analysis - Dokumentácia

## Prehľad aplikácie

Aplikácia umožňuje:
- Vizualizáciu údajov pacientov.
- Generovanie štatistických sumarizácií.
- Pridanie nových pacientov a údajov.

---

## Funkcionalita

1. **Pridanie pacienta:**
   - Nahranie CSV súboru s dátami pacienta.
   - Automatické generovanie údajov pre existujúcich pacientov (Patient 1 - Patient 10).

2. **Vizualizácia údajov:**
   - Grafy (čiarový graf, histogram).
   - Tabuľky údajov.

3. **Štatistická sumarizácia:**
   - Počet, priemer, štandardná odchýlka, minimum, maximum.

4. **Filtrovanie údajov:**
   - Výber pacienta podľa ID.
   - Výber merania (Cholesterol, Blood Pressure, Glucose).
   - Filtrovanie údajov pomocou posuvníka.

---

## Štruktúra aplikácie

- **`app.py`:** Obsahuje serverovú logiku aplikácie.
- **`app_ui.py`:** Definuje používateľské rozhranie aplikácie.
- **`data_init.py`:** Inicializuje údaje pacientov a definuje statické prvky aplikácie.
- **`utils.py`:** Obsahuje pomocné funkcie na spracovanie údajov.

---

## Podrobný popis metód

### `utils.py`

#### `update_patient_data(patient_data_dict, file_info)`
- **Popis:** Pridáva nového pacienta do aplikácie. Ak je nahraný CSV súbor, údaje sa načítajú z neho. Ak nie, vráti chybu.
- **Parametre:**
  - `patient_data_dict`: Slovník obsahujúci údaje pacientov.
  - `file_info`: Informácie o nahranom CSV súbore.
- **Výstup:** Správa o úspechu alebo chybe.
- **Pseudokód:**
  ```
  Get the last patient ID and create a new ID.
  If a CSV file is uploaded:
      Read data from the file.
      Add the new patient to the list.
      Return a success message.
  Else:
      Return an error message about the missing file.
  ```

#### `generate_data_for_patient(patient_data_dict, patient_id)`
- **Popis:** Generuje nové údaje pre existujúceho pacienta na základe aktuálneho dátumu.
- **Parametre:**
  - `patient_data_dict`: Slovník obsahujúci údaje pacientov.
  - `patient_id`: ID pacienta, pre ktorého sa generujú údaje.
- **Výstup:** Správa o úspechu alebo chybe.
- **Pseudokód:**
  ```
  Check if the patient exists.
  If not, return an error.
  Generate new data for the patient.
  Append the new data to the existing patient data.
  Return a success message.
  ```

#### `generate_statistical_summary(patient_id, stats, filtered_data)`
- **Popis:** Generuje štatistickú sumarizáciu pre vybrané merania pacienta.
- **Parametre:**
  - `patient_id`: ID pacienta.
  - `stats`: Zoznam vybraných meraní.
  - `filtered_data`: Filtrované údaje pacienta.
- **Výstup:** Textová sumarizácia štatistík.
- **Pseudokód:**
  ```
  For each measurement in stats:
      Get the data for the measurement.
      Calculate statistical values (count, mean, std, min, max, percentiles).
      Format the statistics into a text output.
  Return the summary as text.
  ```

#### `create_plot(patient_id, measurement_type, filtered_data, graph_type)`
- **Popis:** Vytvára graf (čiarový graf alebo histogram) pre vybrané meranie pacienta.
- **Parametre:**
  - `patient_id`: ID pacienta.
  - `measurement_type`: Typ merania (napr. Cholesterol).
  - `filtered_data`: Filtrované údaje pacienta.
  - `graph_type`: Typ grafu (Line Plot alebo Histogram).
- **Výstup:** Objekt grafu.
- **Pseudokód:**
  ```
  Create a new plot.
  If the graph type is "Line Plot":
      Plot a line graph.
  If the graph type is "Histogram":
      Plot a histogram.
  Set the graph title, axes, and grid.
  Return the plot object.
  ```
---

### `data_init.py`

#### `patient_ids`
- **Popis:** Zoznam ID pacientov (Patient 1 - Patient 10).

#### `dates`
- **Popis:** Dátumy pre generovanie údajov (12 mesiacov od januára 2023).

#### `measurements`
- **Popis:** Typy meraní (Cholesterol, Blood Pressure, Glucose).

#### `views`
- **Popis:** Typy zobrazení (graf, štatistická sumarizácia, tabuľka).

#### `data`
- **Popis:** Slovník obsahujúci údaje pacientov vo forme DataFrame. Každý pacient má vlastný DataFrame údajov, ktoré sú vygenerované z normálneho rozdelenia s danými parametrami.

#### `dynamic_ui_elements`
- **Popis:** Dynamické prvky používateľského rozhrania (napr. typ grafu, výber štatistík, podľa toho, či sa zobrazuje graf alebo tabuľka).

---

### `app.py`

#### `server(input, output, session)`
- **Popis:** Obsahuje serverovú logiku aplikácie - načítanie údajov a definíciu hodnôt pre rôzne komponenty.

##### Metódy:
1. **`add_patient_event`:**
   - Spracováva nahranie CSV súboru a pridanie pacienta do aplikácie.
   - **Pseudokód:**
     ```
     Get the uploaded file information.
     If the file does not exist:
         Set the status message to an error.
         Exit.
     Update patient data using utils.update_patient_data().
     Set the status message to the result.
     ```

2. **`generate_data_event`:**
   - Generuje nové údaje pre vybraného pacienta.
   - **Pseudokód:**
     ```
     Get the patient ID.
     Generate new data using utils.generate_data_for_patient().
     Set the status message to the result.
     ```

3. **`view_type_change_event`:**
   - Dynamicky mení prvky používateľského rozhrania na základe vybraného typu zobrazenia.
   - **Pseudokód:**
     ```
     Get the view type.
     If the view type is "graph":
         Set dynamic content to graph type selection.
     If the view type is "summary" or "table":
         Set dynamic content to statistics selection.
     Else:
         Clear dynamic content.
     ```

4. **`dynamic_slider`:**
   - Generuje posúvač na filtrovanie údajov na základe vybraného merania.
   - **Pseudokód:**
     ```
     Get the measurement type.
     Set the slider range based on the measurement type.
     Return the slider.
     ```

5. **`data_visualization`:**
   - Vytvára graf pre vybrané meranie pacienta.
   - **Pseudokód:**
     ```
     If the view type is "graph":
         Get the patient ID, measurement type, value range, and graph type.
         Filter the patient data based on the value range.
         Create a graph using utils.create_plot().
         Return the graph.
     ```


6. **`statistical_summary`:**
   - Generuje textovú štatistickú sumarizáciu pre vybrané merania.
   - **Pseudokód:**
     ```
     If the view type is "summary":
         Get the patient ID, statistics, and value range.
         Filter the patient data based on the value range.
         Generate the summary using utils.generate_statistical_summary().
         Return the summary.
     ```

7. **`patient_data`:**
   - Zobrazuje tabuľku údajov pacienta na základe vybraných meraní.
   - **Pseudokód:**
     ```
     If the view type is "table":
         Get the patient ID, selected measurements, and value range.
         Filter the patient data based on the value range.
         Return the filtered data as a table.
     ```

8. **`dynamic_content`:**
   - Zobrazuje dynamické prvky používateľského rozhrania.
   - **Pseudokód:**
      ```
     Return the dynamic content based on the current setting.
     ```

9. **`txt_status_code`:**
   - Zobrazuje stavové správy aplikácie.
   - **Pseudokód:**
     ```
     Return the current status message.
     ```

---

### `app_ui.py`

#### `app_ui`
- **Popis:** Definuje používateľské rozhranie aplikácie.

##### Hlavné prvky:
1. **Bočný panel:**
   - Obsahuje vstupy ako výber pacienta, typ merania, nahranie CSV súboru, tlačidlá na pridanie pacienta a generovanie údajov.

2. **Hlavný obsah:**
   - Obsahuje výstupy ako graf, tabuľka a štatistická sumarizácia.

---

## Príklad použitia

1. Spustite aplikáciu:
   ```bash
   shiny run --reload --launch-browser
   ```
2. Vyberte pacienta a typ merania.
3. Zobrazte graf, tabuľku alebo štatistickú sumarizáciu.