# CV6: Virtuálne prostredie v Python-e

Virtuálne prostredie je uzavretý priestor, kde môžete inštalovať balíčky a závislosti pre konkrétny Python projekt bez toho, aby ovplyvnili globálne nainštalované balíčky vo všeobecnej Python verzii. Je užitočné najmä pri práci na viacerých projektoch, ktoré môžu vyžadovať rôzne verzie rovnakých knižníc.

---

## Výhody použitia virtuálneho prostredia

- **Izolácia závislostí**: Každý projekt môže mať svoje vlastné balíčky a verzie knižníc.
- **Jednoduchá správa závislostí**: Pomocou súboru `requirements.txt` môžete jednoducho zdieľať zoznam potrebných balíčkov s ostatnými.
- **Zabránenie konfliktom**: Rôzne projekty môžu používať rôzne verzie rovnakých knižníc bez konfliktov.

---

## Vytvorenie virtuálneho prostredia

### 1. Použitie príkazového riadku (príkaz `venv`)

1. **Vytvorenie virtuálneho prostredia**:
   ```bash
   python -m venv venv
   ```
   Tento príkaz vytvorí priečinok `venv` v aktuálnom adresári, ktorý obsahuje izolované prostredie.

2. **Aktivácia virtuálneho prostredia**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. **Deaktivácia virtuálneho prostredia**:
   ```bash
   deactivate
   ```

### 2. Vytvorenie virtuálneho prostredia v PyCharme

PyCharm poskytuje jednoduchý spôsob na vytvorenie a správu virtuálnych prostredí priamo v projekte, buď pri vytvorení projektu, použitím spodnej lišky, alebo použitím nastavení:

### Krok 1: Otvorte nastavenia projektu
1. Kliknite na **File** > **Settings** (alebo **Ctrl+Alt+S**).
2. Prejdite na **Project: [Project Name]** > **Python Interpreter**.

### Krok 2: Vytvorte nové virtuálne prostredie
1. Kliknite na ikonu ozubeného kolieska v pravom hornom rohu a vyberte **Add...**.
2. V okne **Add Python Interpreter** vyberte možnosť **New Virtual Environment**.
3. Zadajte cestu, kde chcete vytvoriť virtuálne prostredie (napr. `venv` v koreňovom adresári projektu).
4. Kliknite na **OK**.

### Krok 3: Použitie `requirements.txt` v PyCharm
1. Ak máte súbor `requirements.txt`, PyCharm vám ponúkne možnosť automaticky nainštalovať všetky balíčky pri vytváraní virtuálneho prostredia.
2. Ak chcete nainštalovať balíčky neskôr, otvorte terminál v PyCharm a použite:
   ```bash
   pip install -r requirements.txt
   ```

---

### Použitie `requirements.txt`

Súbor `requirements.txt` obsahuje zoznam všetkých balíčkov a ich verzií, ktoré váš projekt potrebuje. Tento súbor je užitočný na zdieľanie závislostí medzi vývojármi alebo na nasadenie projektu na server.

### 1. Vytvorenie `requirements.txt`
Ak už máte nainštalované balíčky vo virtuálnom prostredí, môžete ich uložiť do súboru `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### 2. Inštalácia balíčkov zo súboru `requirements.txt`
Ak chcete nainštalovať všetky balíčky zo súboru `requirements.txt`, použite:
```bash
pip install -r requirements.txt
```
