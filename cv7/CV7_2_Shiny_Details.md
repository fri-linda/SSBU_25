# CV7: Shiny pre Python - Podrobný sprievodca

## Prehľad Shiny pre Python

[Dokumentácia knižnice - komponenty](https://shiny.posit.co/py/components/)

Shiny pre Python je framework na tvorbu interaktívnych webových aplikácií priamo v Pythone. Umožňuje vývojárom vytvárať dynamické používateľské rozhrania a reaktívnu serverovú logiku. Tento framework je ideálny na vizualizáciu údajov, tvorbu dashboardov a interaktívnych analytických nástrojov.

[Príklad Shiny Aplikácie](https://shinylive.io/py/examples/#cpu-info)

---

## Komponenty Shiny aplikácií

### Vstupy
Vstupy umožňujú používateľom poskytovať údaje aplikácii. Bežné vstupné komponenty zahŕňajú:
- **Posúvač:** `shiny.ui.input_slider()` - Výber hodnoty alebo rozsahu hodnôt.
- **Textový vstup:** `shiny.ui.input_text()` - Zadanie textu.
- **Nahrávanie súborov:** `shiny.ui.input_file()` - Nahrávanie súborov.
- **Výber z možností:** `shiny.ui.input_select()` - Výber z rozbaľovacieho menu.
- **Výber jednej z  možnosti:** `shiny.ui.input_radio_buttons()` - Výber jednej možnosti zo skupiny.
- **Zaškrtávacie políčko:** `shiny.ui.input_checkbox()` - Výber áno/nie.
- **Skupina zaškrtávacích políčok:** `shiny.ui.input_checkbox_group()` - Výber viacerých možností.
- **Action tlačidlo:** `shiny.ui.input_action_button()` - Spustenie akcie po kliknutí.
- **Numerický vstup:** `shiny.ui.input_numeric()` - Zadanie číselnej hodnoty.
- **Dátumový vstup:** `shiny.ui.input_date()` - Výber dátumu.
- **Rozsah dátumov:** `shiny.ui.input_date_range()` - Výber rozsahu dátumov.

Príklad:
```python
shiny.ui.input_slider("slider", "Vyberte hodnotu:", min=0, max=100, value=50)
shiny.ui.input_date("date_input", "Vyberte dátum:")
shiny.ui.input_date_range("date_range", "Vyberte rozsah dátumov:")
```

---

### Výstupy
Výstupy zobrazujú výsledky výpočtov alebo vizualizácií. Bežné výstupné komponenty zahŕňajú:
- **Textový výstup:** `shiny.ui.output_text()` - Zobrazenie textu.
- **Grafický výstup:** `shiny.ui.output_plot()` - Zobrazenie grafov.
- **Tabuľkový výstup:** `shiny.ui.output_table()` - Zobrazenie tabuľkových údajov.
- **Dynamický výstup:** `shiny.ui.output_ui()` - Renderovanie dynamických prvkov používateľského rozhrania.
- **Stiahnutie súboru:** `shiny.ui.output_download()` - Umožňuje používateľovi stiahnuť súbor.

Príklad:
```python
@output
@shiny.render.text
def output_text():
    return f"Vybraná hodnota: {input.slider()}"

@output
@shiny.render.download
def download_data():
    return shiny.download_handler(
        filename="data.csv",
        content=lambda file: filtered_data.to_csv(file)
    )
```

---

### Udalosti
Udalosti spúšťajú akcie v reakcii na interakcie používateľa. Shiny poskytuje dekorátory na spracovanie udalostí:
- **Reaktívne udalosti:** Použite `@reactive.event()` na spustenie akcií na základe konkrétnych vstupov.
- **Reaktívne efekty:** Použite `@reactive.Effect` na definovanie reaktívnych výpočtov.

Príklad:
```python
@reactive.Effect
@reactive.event(input.submit)
def handle_submit():
    print("Tlačidlo bolo stlačené!")
```

---

### Reaktivita
Reaktivita je jadrom Shiny, umožňuje automatické aktualizácie výstupov pri zmene vstupov. Kľúčové koncepty zahŕňajú:
- **Reaktívne hodnoty:** Ukladajú a spravujú stav pomocou `reactive.Value`.
- **Reaktívne závislosti:** Automaticky sledujú závislosti medzi vstupmi a výstupmi.

Príklad:
```python
@output
@shiny.render.plot
def plot_output():
    return plt.plot([input.slider()])
```

---

## Rozloženie a štýlovanie

Shiny poskytuje flexibilné možnosti rozloženia na organizáciu komponentov používateľského rozhrania:
- **Rozloženie so bočným panelom:** `shiny.ui.layout_sidebar()` - Vytvorenie bočného panela s hlavným obsahom.
- **Karty:** `shiny.ui.card()` - Zoskupenie súvisiacich komponentov do karty.
- **Fluidná stránka:** `shiny.ui.page_fluid()` - Vytvorenie responzívneho rozloženia.
- **Rozloženie s mriežkou:** `shiny.ui.layout_grid()` - Organizácia komponentov do mriežky.
- **Taby:** `shiny.ui.navset_tab()` - Rozdelenie obsahu do záložiek.

Príklad:
```python
shiny.ui.page_fluid(
    shiny.ui.navset_tab(
        shiny.ui.nav("Tab 1", shiny.ui.input_text("text_input", "Zadajte text:")),
        shiny.ui.nav("Tab 2", shiny.ui.output_plot("plot_output"))
    )
)
```

---

## Pokročilé funkcie

### Dynamické používateľské rozhranie
Shiny umožňuje dynamické generovanie prvkov používateľského rozhrania na základe vstupov používateľa alebo serverovej logiky pomocou `shiny.ui.output_ui()`.

Príklad:
```python
@output
@shiny.render.ui
def dynamic_ui():
    if input.show_slider():
        return shiny.ui.input_slider("dynamic_slider", "Dynamický posúvač", min=0, max=100, value=50)
```

### Práca so súbormi
Shiny podporuje nahrávanie a spracovanie súborov pomocou `shiny.ui.input_file()`.

Príklad:
```python
@reactive.Effect
@reactive.event(input.file_upload)
def handle_file_upload():
    file_info = input.file_upload()
    if file_info:
        df = pd.read_csv(file_info[0]["datapath"])
        print(df.head())
```

### Validácia vstupov
Shiny umožňuje validáciu vstupov pred ich spracovaním.

Príklad:
```python
@reactive.Effect
@reactive.event(input.submit)
def validate_and_process():
    if not input.text_input():
        print("Chyba: Textové pole je prázdne.")
    else:
        print(f"Zadaný text: {input.text_input()}")
```

---

## Zhrnutie

Shiny pre Python je jednoduchý framework na tvorbu interaktívnych webových aplikácií. 
Jeho komponenty, reaktivita a možnosti rozloženia ho robia vhodným pre vytváranie jednoduchých 
aplikácií s použitím vizualizácie údajov.