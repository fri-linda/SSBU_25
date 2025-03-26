# CV5: Úlohy

**Úloha 1:** Rozšírenie triedy Dataset
1. Pridajte metódu do triedy `Dataset` na výpočet základných štatistík (priemer, medián, štandardná odchýlka) pre každú vlastnosť.
2. Otestujte novú metódu vytlačením štatistík pre vyčistený dataset.

```pseudo
class Dataset:
    method calculate_statistics():
        create a DataFrame from self.data with columns as self.feature_names
        calculate mean, median, and standard deviation for each feature (rename the columns, if necessary)
        return the statistics as a DataFrame

# example usage:
create a Dataset object
call calculate_statistics() method
print the statistics
```

**Úloha 2:** Experimentovanie so škálovaním
1. Upravte triedu `DataScaler`, aby obsahovala možnosť robustného škálovania pomocou `RobustScaler` z `sklearn`.
2. Škálujte dataset pomocou novej metódy škálovania a porovnajte ho s existujúcimi metódami.

**Úloha 3:** Pridanie metódy na zhrnutie vlastností
1. Pridajte metódu do triedy `Dataset` na poskytnutie zhrnutia každej vlastnosti, vrátane počtu unikátnych hodnôt, najčastejšej hodnoty a jej frekvencie.
2. Otestujte novú metódu vytlačením zhrnutia pre dataset.

```pseudo
class Dataset:
    method summarize_features():
        create a DataFrame (same as in Task 1)
        calculate the number of unique values, the most common value, and its frequency for each feature
        return the summary as a DataFrame
        
# example usage:
create a Dataset object
call summarize_features() method
print the summary
```

**Úloha 4:** Úprava metódy na zhrnutie vlastností
1. Upravte metódu `summarize_features` tak, aby vypísala zhrnutie len pre vybrané vlastnosti, ak sú definované.
2. Otestujte novú metódu na zhrnutie pre vybrané vlastnosti.

```pseudo
updates in the summarize_features method:
    add an optional parameter feature_names to specify the features to summarize
    if feature_names is None, summarize all features
    otherwise, summarize only the specified features (filter the DataFrame)
```

**Úloha 5:** Dokumentácia
1. Napíšte krátku správu, ktorá zhrnie výsledky vašich experimentov s analýzou dát. (Informácie vyčítané z grafov)
2. Zahrňte pozorovania o vplyve rôznych metód škálovania na dataset.
