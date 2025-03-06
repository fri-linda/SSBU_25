# **SSBU CV3: Práca s datasetom v Pythone**

Datasety z verejne dostupných databáz je možné získavať aj priamo z jazyka Python. Pre načítanie datasetu použijeme databázu Kaggle.

---

## **1. Inštalácia potrebných knižníc**
Pre prácu s databázou **Kaggle** a jednoduché sťahovanie datasetov priamo z jazyka Python je vhodné nainštalovať knižnicu **kagglehub**.

Pre prácu s dátami v tabuľkovej forme pomocou **DataFrame** je potrebné mať nainštalovanú knižnicu **pandas**.

Pre vizualizáciu dát pomocou grafov je vhodné použiť knižnicu **matplotlib**.



```python
# pip install kagglehub pandas matplotlib
```

---

## **2. Načítanie datasetu z databázy Kaggle**
Použijeme dataset [**remote-work-and-mental-health**](https://www.kaggle.com/datasets/waqi786/remote-work-and-mental-health) dostupný v databáze [**Kaggle**](https://www.kaggle.com/). Dataset obsahuje informácie o vplyve práce na diaľku na duševné zdravie človeka.

Dataset sa uloží na predvolenú lokalitu nastavenú knižnicou.



```python
import os
import kagglehub

# download the dataser
dataset_path = kagglehub.dataset_download("waqi786/remote-work-and-mental-health")

print("Path:", dataset_path)
```

---

## **3. Načítanie datasetu do Pandas DataFrame**
Dataset je vo formáte **CSV**, preto použijeme knižnicu **pandas** na jeho načítanie.

Na spájanie ciest v súborovom systéme je dobré používať metódu join z knižnice os - [Dokumentácia os.path.join](https://docs.python.org/3/library/os.path.html#os.path.join). Knižnica je vhodnejšia ako spájanie premenných typu string, pretože dáva pozor na správne oddelenie ciest podľa operačného systému.

Načítanie datasetu do **DataFrame** sa vykoná priamo pomocou funkcie `read_csv` z knižnice **pandas** - [Dokumentácia read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

Kontrola správneho mačítania datasetu sa vykoná pomocou metódy `head` - [Dokumentácia head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html)




```python
import pandas as pd

dataset_name = os.path.join(dataset_path, "Impact_of_Remote_Work_on_Mental_Health.csv")

df = pd.read_csv(dataset_name)
print(df.head())
```

**Úloha:** Zobrazte posledných 10 riadkov datasetu - [Dokumentácia tail](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html)



```python
# TODO
```

----

## **4. Základná analýza datasetu**

Po načítaní datasetu je vhodné vykonať základnú analýzu údajov, aby sme overili správne načítanie a získali prehľad o dátach.

### **Zobrazenie základných štatistík**

Zobrazenie základných štatistík o datasete pre stĺpce s číselnými hodnotami sa vykoná pomocou metódy `describe` - [Dokumentácia describe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)



```python
print(df.describe())
```

Zobrazenie základných štatistík o datasete pre všetky stĺpce sa vykoná pomocou metódy `info` - [Dokumentácia info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html)


```python
print(df.info())
```

**Úloha:** Skúste vypočítať medián pre všetky číselné stĺpce. Použite metódu median - [Dokumentácia median](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html). Je potrebné zvoliť iba číselné stĺpce.


```python
# TODO
```

### **Kontrola chýbajúcich údajov**

Na kontrolu chýbajúcich údajov sa používa metóda `isnull` - [Dokumentácia isnull](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html).
Táto metóda vráti hodnotu **True** pre každý riadok, ktorý obsahuje chýbajúce hodnoty.

Metóda `sum` vráti počet chýbajúcich hodnôt pre každý stĺpec - [Dokumentácia sum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html)


```python
print(df.isnull().sum())
```

**Úloha:** Skúste odstrániť všetky riadky s chýbajúcimi hodnotami pomocou met=ody `dropna`- [Dokumentácia dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) Výsledok operácie uložte do premennej `clean_df`.


```python
# TODO
```

### **Najčastejšie regióny v údajoch**

Práca s konkrétnym stĺpcom sa vykonáva pomocou zápisu `názov_dataframe["názov_stĺpca"]`. Pozor na veľké a malé písmená.

Na zistenie najčastejšie sa vyskytujúcich hodnôt v stĺpci sa používa metóda `value_counts` - [Dokumentácia value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html). Táto metóda vráti počet výskytov pre každú hodnotu v stĺpci.



```python
print(df["Region"].value_counts())
```

**Úloha:** Zobrazte 5 najčastejšie sa vyskytujúcich fyzických aktivít. Použite kombináciu metód `value_counts` a `head`.


```python
# TODO
```

### **Počet odpracovaných hodín za týždeň**

Na zistenie počtu sa použije metóda `value_counts` - [Dokumentácia value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html).

Pre zoradenie hodnôt podľa indexu sa použije metóda `sort_index` - [Dokumentácia sort_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html).


```python
print(df["Hours_Worked_Per_Week"].value_counts().sort_index())
```

**Úloha:** Zoraďte počet odpracovaných hodín zostupne. Použite metódu `sort_values` - [Dokumentácia sort_values()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html), ktorá zoradí hodnoty podľa počtu výskytov.


```python
# TODO
```

---

## **5. Vizualizácia údajov**

Na vizualizáciu využijeme knižnicu **matplotlib**. Táto knižnica umožňuje vytvárať rôzne typy grafov a vizualizácií.

Metóda `figure` umožňuje nastaviť veľkosť grafu - [Dokumentácia figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html).

Metóda `plot` umožňuje vytvárať rôzne typy grafov - [Dokumentácia plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html).

Súčasti grafu (názvy osí, titulok) sa nastavujú pomocou metód `xlabel`, `ylabel`, `title` - [Dokumentácia xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html), [Dokumentácia ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html), [Dokumentácia title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html), a ďalších.

Pre zobrazenie grafov je potrebné použiť metódu `show` - [Dokumentácia show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html).



```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
df["Mental_Health_Condition"].value_counts().head(10).plot(kind='bar')

plt.title("Najčastejšie zdravotné stavy")
plt.xlabel("Zdravotný stav")
plt.ylabel("Počet záznamov")
plt.show()
```

**Úloha:** Vytvorte koláčový graf pre rôzne pracovné pozície a nastavte mu názov.


```python
# TODO
```

**Úloha:** Vytvorte horizontálny čiarový graf pre rôzne levely stresu na pozícii Software Engineer.

Hint:
Najskôr vyfiltrujte v DataFrame záznamy pre pozíciu Software Engineer a potom zistite počet záznamov pre jednotlivé levely stresu.
Filtrovanie sa vykoná pomocou zápisu `df[df["stĺpec"] == "hodnota"]`.



```python
# TODO
```

---

#### Ďalšie príklady spracovania tohto datasetu

https://www.kaggle.com/code/waqi786/remote-work-mental-health-eda

https://www.kaggle.com/code/pavankumar4757/remote-work-mental-health-analysis

https://www.kaggle.com/code/saifsalama/remote-work-mental-health-eda
