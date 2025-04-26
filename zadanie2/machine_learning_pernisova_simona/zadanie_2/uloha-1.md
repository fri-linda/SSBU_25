# Random Forest – Model strojového učenia

Použila som model Random Forest (náhodný les), ktorý kombinuje viacero rozhodovacích stromov na vytváranie predikcií. Každý strom sa trénuje na inej časti dát a výsledky sa spočítajú, aby sa dosiahol konečný výstup.

## Parametre modelu

Pri nastavovaní modelu som upravila niekoľko kľúčových parametrov, ktoré ovplyvňujú jeho výkon:

### `n_estimators` – počet stromov v lese

Určuje, koľko stromov bude v modeli. Viac stromov zlepšuje predikcie, ale môže spomaliť výpočty.

- Testovala som hodnoty **100** a **200**.

### `max_depth` – maximálna hĺbka stromov

Obmedzuje počet úrovní rozhodnutí.

- **None** (neobmedzená hĺbka) – model sa učí podrobne, ale hrozí pretrénovanie.
- **10** – obmedzenie hĺbky na 10 úrovní.

### `min_samples_split` – minimálny počet vzoriek na rozdelenie uzla

Určuje, koľko dát musí byť v uzle, aby sa rozdelil na menšie časti. Vyššie hodnoty znižujú riziko pretrénovania.

- Testované hodnoty: **2** a **5**.

### `min_samples_leaf` – minimálny počet vzoriek v listovom uzle

Zabraňuje príliš malým koncovým uzlom, čo znižuje pretrénovanie.

- Testované hodnoty: **1** a **2**.

### `random_state` – nastavenie náhodnosti

Zabezpečuje, že model dá rovnaké výsledky pri každom spustení.

- Použila som hodnotu **42**, ktorá je často používaná na replikovateľnosť.
