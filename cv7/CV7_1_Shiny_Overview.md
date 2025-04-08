# CV7: Shiny for Python - Overview

## Inštalácia Shiny pre Python

1. **Inštalácia Shiny pomocou pip:**
   ```bash
   pip install shiny
   ```

2. **Vytvorenie novej aplikácie:**
   Použite príkaz:
   ```bash
   shiny create
   ```

3. **Spustenie aplikácie:**
   ```bash
   shiny run --reload --launch-browser
   ```

---

## Základná štruktúra Shiny aplikácie

Shiny aplikácia pozostáva z dvoch hlavných častí:
1. **Používateľské rozhranie (UI):** Definuje vzhľad aplikácie.
2. **Serverová logika:** Obsahuje kód na spracovanie vstupov a generovanie výstupov.

Príklad:
```python
import shiny

app_ui = shiny.ui.page_fluid(
    shiny.ui.input_slider("num", "Vyberte číslo:", min=1, max=100, value=50),
    shiny.ui.output_text("output")
)

def server(input, output, session):
    @output
    @shiny.render.text
    def output():
        return f"Vybrali ste číslo: {input.num()}"

app = shiny.App(app_ui, server)
```

---

## Spustenie aplikácie

1. Uistite sa, že máte nainštalovaný Shiny.
2. Spustite aplikáciu príkazom:
   ```bash
   shiny run --reload --launch-browser
   ```
3. Aplikácia sa otvorí vo webovom prehliadači na adrese `http://localhost:8000`.

---

## Troubleshoot

#### Shiny for Python

- Debug aplikácie - https://shiny.posit.co/py/docs/debug.html
- Prípadne za behu aplikácie pomocou fukcie `print()` - výpisy nájdete v termináli medzi logmi aplikácie

#### Zastavenie behu Shiny 

- CTRL + C v termináli
- Niekedy sa stane, že sa proces neukončí správne, je potrebné ho zastaviť.
+ V príkazovom riadku si zobrazte zoznam procesov, ktoré bežia na porte 8000.
     ```bash
   netstat -ano | findstr :8000
   ```
  
+ V zozname nájdite PID (posledný stĺpec), a doplňte ho do príkazu pre zastavenie procesu.
     ```bash
   taskkill /PID [PID_procesu] /F
   ```
