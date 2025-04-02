# CV7: Doplnkové Úlohy

## Úloha 1: Pridanie nového typu grafu
Rozšírte aplikáciu o možnosť zobrazenia nového typu grafu - napríklad "Box Plot". Upravte dynamické používateľské rozhranie tak, aby obsahovalo možnosť výberu tohto grafu, a implementujte jeho vykreslenie v časti `data_visualization`.

### Hint:
- Pridajte možnosť "Box Plot" do `graph_type` v `data_init.py`.
- Upravte funkciu `create_plot` v `utils.py`, aby podporovala vykreslenie boxplotu.
- Otestujte aplikáciu s rôznymi rozsahmi hodnôt.

---

## Úloha 2: Zobrazenie priemernej hodnoty merania pre všetkých pacientov
Pridajte do aplikácie možnosť vypočítať a zobraziť priemernú hodnotu vybraného merania (napr. Cholesterol) pre všetkých pacientov. Implementujte nové tlačidlo v používateľskom rozhraní a funkciu na výpočet priemeru.

### Hint:
- Pridajte nové tlačidlo `ui.input_action_button("calculate_avg", "Vypočítať priemer")` do `app_ui.py`.
- Implementujte obsluhu udalosti v `app.py`, ktorá vypočíta priemer pre vybrané meranie zo všetkých pacientov.
- Zobrazte výsledok v textovom výstupe `ui.output_text("txt_status_code")`, alebo vytvorte nový textový výstup napr. `ui.output_text("avg_value")`.

