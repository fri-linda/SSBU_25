# CV6: Procesy pri použití  strojového učenia

## Procesy strojového učenia

Strojové učenie zahŕňa sériu krokov od prípravy dát po evaluáciu modelu. Každý krok je kľúčový pre úspech celkového procesu. 
Tu je prehľad základných procesov:

### Načítanie a predspracovanie údajov

Údaje sú základom každého modelu strojového učenia. Kľúčom je pochopiť ich štruktúru, typy a ako môžu ovplyvniť modelovanie. 
Použitím knižnice Pandas môžeme ľahko načítať, predspracovať a skúmať dáta. 
Práca s Pandas DataFrame poskytuje flexibilitu v manipulácii s dátami, umožňuje ľahké filtrovanie, zmeny a agregáciu informácií. 
Práca s čistými a správne štruktúrovanými dátami je kritická pre trénovanie modelov strojového učenia.

### Prevzorkovanie nevybalansovaných údajov 

Často narazíme na dataset, kde sú triedy nevyvážené – jedna trieda má v množine oveľa viac vzoriek než ostatné. 
Táto nevyváženosť môže spôsobiť, že model bude mať tendenciu lepšie sa "učiť" na prevažujúcej triede, čo vedie 
k slabšej výkonnosti na menej zastúpených triedach. Jednou z najpopulárnejších techník prevzorkovania je 
SMOTE (Synthetic Minority Over-sampling Technique). SMOTE generuje syntetické príklady menšinovej triedy v priestore 
vlastností tým, že berie do úvahy najbližších susedov týchto príkladov. Použitím SMOTE môžeme dosiahnuť lepšiu 
rovnováhu tried v datasete, čo vedie k všeobecne lepším výsledkom modelu, najmä v kontexte klasifikačných úloh. 
Prevzorkovanie je dôležité aplikovať len na trénovacie dáta. Testovacie dáta by mali zostať nepozmenené. 
SMOTE prevzorkovanie je dostupné v knižnici `imbalanced-learn`. Dôležitým parametrom môže byť `k-neighbors`, 
ktorý udáva, koľko susedov by malo byť braných do úvahy pre generovanie syntetických vzoriek.

### Cross Validácia a Grid Search 

**Cross Validácia:** Metóda na overenie robustnosti modelu využívajúca viacnásobné rozdelenie dát na trénovacie 
a validačné sady a následné trénovanie a testovanie modelu na všetkých rozdeleniach. Takto je efektívne na trénovanie 
a testovanie modelu využitá celá množnina údajov.

**Grid Search:** Grid Search systematicky prehľadáva všetky zadané kombinácie hyperparametrov a identifikuje kombináciu,
pri ktorej model dosahuje najlepšie výsledky s ohľadom na optimalizáciu zdrojov. Použitie cross-validation pri tomto 
procese znižuje riziko preučenia tým, že evaluuje model na viacerých podmnožinách trénovacích dát. Táto metodika 
zabezpečuje, že vybraný model je robustný a dobre generalizuje na nové dáta. Grid Search s použitím Cross validácie 
je implementovaný metódou `GridSearchCV` v knižnici scikit-learn. Vstupom do tejto metódy je model, množina hodnôt 
parametrov modelu, z ktorých sa vytvoria kombinácie, počet častí, na ktoré sa rozdelí dataset (`cv`), vyhodnocovacia 
metrika (napr. `scoring='accuracy'`), prípadne parameter `n_jobs` ktorý udáva množstvo paralelných procesov, v ktorých 
môže Grid Search bežať - pre paralelizáciu a urýchlenie prehľadávania. (Hodnota `-1` pre tento parameter znamená 
využitie maximálneho počtu procesov, v závislosti od počtu jadier procesora.)
  
### Rozdelenie údajov na trénovacie a testovacie

Rozdelenie údajov je kľúčové pre natrénovanie a overenie výkonnosti modelu. Trénovacie dáta umožňujú modelu učiť sa 
vzorce a súvislosti, zatiaľ čo testovacie dáta posudzujú jeho výkonnosť. Pri použití metódy `train_test_split`
(knižnica scikit-learn) parameter `test_size` určuje pomer dát vyčlenených pre testovanie, často sa používa 20-40% dát. 
Stratifikované rozdelenie údajov (`stratify=True`) tiež môže pomôcť pri nevyvážených datasetoch tým, že zabezpečuje, 
aby pomer tried bol v množine údajov na trénovanie a testovanie konzistentný. Parameter `shuffle` zabezpečuje náhodné 
zoradenie údajov v trénovacej množine, aby sa algoritmus nenaučil závislosti v údajoch podľa ich poradia.  

### Zakladné Modely a ich Parametre

##### *Lineárna Regresia*
- **fit_intercept** (bool): Určuje, či sa má vypočítať intercept pre tento model. Ak je nastavené na False, 
intercept nebude použitý v výpočtoch.

- **normalize** (bool): Tento parameter sa ignoruje, keď je `fit_intercept` nastavené na False. Ak je True, 
regresory X budú normalizované pred regresiou.

##### *Logistická Regresia*
- **penalty** (str): Určuje normu trestu ('l1', 'l2', 'elasticnet', 'none'). Používa sa na špecifikáciu normy 
použitej pri penalizácii.
- **C** (float): Inverzná hodnota regulačnej sily; musí byť kladné číslo. Podobne ako u support vector machines, 
menšie hodnoty špecifikujú silnejšiu regularizáciu.
- **solver** (str): Algoritmus použitý v optimalizačnom probléme. Pre malé datasety je dobrá voľba 'liblinear', 
zatiaľ čo 'sag' a 'saga' sú rýchlejšie pre veľké datasety.
- **max_iter** (int): Maximálny počet iterácií, ktoré solvery môžu vykonať, kým konvergujú.

##### *Náhodný Les (Random Forest)*
- **n_estimators** (int): Počet stromov v lese.
- **max_depth** (int): Maximálna hĺbka stromu. Ak je None, uzly sa rozširujú, až kým všetky listy nie sú čisté, 
alebo kým každý list neobsahuje menej ako `min_samples_split` vzoriek.
- **min_samples_split** (int alebo float): Minimálny počet vzoriek potrebných na rozdelenie vnútorného uzlu.
- **max_features** (int, float, string): Počet prvkov, ktoré sa majú zvážiť pri hľadaní najlepšieho rozdelenia.

##### *Support Vector Machine (SVM)*
- **C** (float): Regulačný parameter. Sila regulácie je nepriamo úmerná hodnote C. Musí byť kladné číslo.
- **kernel** (string): Určuje typ jadra použitého v algoritme. Musí byť jedno z 'linear', 'poly', 'rbf', 'sigmoid', 
'precomputed' alebo volateľné.
- **gamma** (float, 'scale' alebo 'auto'): Koeficient jadra pre 'rbf', 'poly' a 'sigmoid'. Ak je 'auto', 
použije sa 1 / počet_vlastností, ak je 'scale', použije sa 1 / (počet_vlastností * X.var()) ako hodnota gamma.

**Experimentovanie s rôznymi modelmi a ich parametrami je nevyhnutné pre nájdenie najlepšieho riešenia pre daný problém.**

### Trénovanie a testovanie

**Trénovanie modelu:** Po výbere vhodného modelu a jeho konfigurácie sa model trénuje na trénovacej sade údajov. 
Trénovanie modelu zahŕňa aplikáciu algoritmu strojového učenia na údaje, umožňujúc modelu naučiť sa vzťahy medzi 
vstupnými a výstupnými premennými. Dôležité je monitorovať proces trénovania, aby sme sa vyhli preučeniu, kedy sa 
model príliš prispôsobí trénovacím údajom a stratí schopnosť generalizovať na nové dáta (model dosahuje zlé výsledky 
na testovacích údajoch).  Metóda `fit(X, y[, sample_weight])` trénuje model na údajoch. X predstavuje trénovacie dáta 
(vlastnosti), y trénovacie dáta (výstupná premenná), a sample_weight je voliteľný parameter na vyváženie vzoriek.

**Testovanie modelu:** Po trénovaní modelu sa jeho výkonnosť overí na testovacej sade údajov, ktorá nebola použitá 
počas trénovania. Tento krok umožňuje objektívne posúdiť, ako dobre model predpovedá alebo klasifikuje nové údaje. 
Testovacie výsledky poskytujú užitočnú spätnú väzbu pre ďalšie vylepšenie modelu a overujú použiteľnosť modelu v praxi. 
Metóda `predict(X)` používa natrénovaný model na predpovedanie výstupu pre poskytnuté dáta X. Vracia predpovedané hodnoty.

### Evaluácia

**Evaluácia modelu:** Model je hodnotený pomocou špecifických metrík vhodných pre daný typ úlohy strojového učenia. 
Pri klasifikácii môžu byť to presnosť, F1 skóre, recall, precision a ROC AUC. Pri regresii sa často používajú 
RMSE (Root Mean Square Error), MAE (Mean Absolute Error) a R² skóre. Výber správnej metriky závisí od cieľov 
konkrétneho modelu a údajov, na ktorých pracuje.

##### Senzitivita (Recall)
Senzitivita určuje, aká je pravdepodobnosť, že test správne identifikuje pacientov s daným ochorením. Vypočíta sa ako 
podiel počtu správne pozitívnych výsledkov (true positive, TP) a celkového počtu pacientov s daným ochorením 
(TP + FN, kde FN sú falošne negatívne).

##### Špecificita
Špecificita ukazuje, aká je pravdepodobnosť, že test správne identifikuje zdravých jedincov (bez ochorenia). 
Vypočíta sa ako podiel počtu správne negatívnych výsledkov (true negative, TN) a celkového počtu zdravých jedincov 
(TN + FP, kde FP sú falošne pozitívne).

##### Pozitívna prediktívna hodnota (PPV)
Pozitívna prediktívna hodnota označuje pravdepodobnosť, že osoba s pozitívnym testom skutočne má dané ochorenie. 
Vypočíta sa ako podiel TP a celkového počtu pozitívnych výsledkov testu (TP + FP).

##### Negatívna prediktívna hodnota (NPV)
Negatívna prediktívna hodnota označuje pravdepodobnosť, že osoba s negatívnym testom nemá dané ochorenie. 
Vypočíta sa ako podiel TN a celkového počtu negatívnych výsledkov testu (TN + FN).

##### Precision (presnosť)
Precision, alebo presnosť, je podobná PPV a označuje podiel TP voči všetkým pozitívnym predikciám testu (TP + FP).

##### ROC-AUC
ROC krivka (Receiver Operating Characteristic) graficky znázorňuje výkonnosť diagnostického testu a 
AUC (Area Under the Curve) je miera, ktorá sumarizuje celkovú výkonnosť testu. AUC hodnota 1 znamená dokonalý test, 
hodnota 0.5 znamená, že test je náhodný.

##### Pomery pravdepodobností
- **Pomer pravdepodobnosti pre pozitívny výsledok (PLR, Positive Likelihood Ratio):** PLR hovorí o tom, 
ako sa zvyšuje pravdepodobnosť ochorenia pri pozitívnom teste. Vypočíta sa ako podiel senzitivity a 1 - špecificity.
- **Pomer pravdepodobnosti pre negatívny výsledok (NLR, Negative Likelihood Ratio):** NLR ukazuje, ako sa znižuje 
pravdepodobnosť ochorenia pri negatívnom teste. Vypočíta sa ako podiel 1 - senzitivity a špecificity.

Python a knižnica scikit-learn poskytujú viaceré funkcie na meranie úspešnosti modelov strojového učenia, napr.:

- `accuracy_score(y_true, y_pred)`: Vypočíta presnosť, podiel správne predpovedaných vzoriek ku celkovému počtu vzoriek.
Je to jednoduchá metrika vhodná pre balansované datasety.

- `precision_score(y_true, y_pred[, labels, ...])`: Vypočíta presnosť, podiel správne pozitívnych výsledkov ku všetkým 
pozitívnym výsledkom predpovedaným modelom. Táto metrika je kľúčová pri modeloch, kde sú náklady na falošne pozitívne vysoké.

- `recall_score(y_true, y_pred[, labels, ...])`: Vypočíta úplnosť, podiel správne pozitívnych výsledkov ku všetkým 
skutočne pozitívnym príkladom. Je dôležitá v situáciách, kde je dôležité identifikovať všetky pozitívne prípady.

- `f1_score(y_true, y_pred[, labels, ...])`: Vypočíta harmonický priemer presnosti a úplnosti. Je užitočná metrika, 
keď potrebujeme vyvážiť presnosť a úplnosť, obzvlášť pri nevyvážených dátových sadách.

Pri evaluácii modelu je vhodné použiť viacero metrík, aby ste získali komplexnejší obraz o jeho výkonnosti.

### Vizualizácia

Vizualizácia výsledkov pomáha identifikovať vzory, odhalovať slabiny modelu a prezentovať tieto zistenia.

Niektoré typy vizualizácií pre evaluáciu modelu:

- **Matica zámien (Confusion matrix):** Umožňuje rýchlo zorientovať sa v správnosti klasifikácií modelu. Vizualizácia 
matice zámeny pomocou `sns.heatmap` z Seaborn alebo `plot_confusion_matrix` z scikit-learn poskytuje prehľadné 
zobrazenie počtu správnych a nesprávnych predikcií pre každú triedu.

- **ROC krivka (Receiver Operating Characteristic curve):** Graficky zobrazuje diagnostickú schopnosť binárneho 
klasifikátora pri rôznych prahových hodnotách. ROC krivka a výpočet AUC (Area Under the Curve) sú k dispozícii 
v scikit-learn ako `roc_curve` a `roc_auc_score` metódy.

- **Precision-Recall krivka:** Poskytuje pohľad na vzťah medzi presnosťou a úplnosťou modelu pri rôznych prahových 
hodnotách. Funkcia `precision_recall_curve` z scikit-learn môže byť použitá na jej generovanie.

- **Významnosť príznakov (Feature Importance):** Vizualizácia, ktorá ukazuje, ktoré príznaky majú najväčší vplyv na 
predikcie modelu. Pre modely ako sú náhodné lesy, môžeme použiť `feature_importances_` atribút na získanie významnosti 
príznakov a následne ich vizualizovať pomocou stĺpcového grafu.

### Reprodukovateľnosť a Experimenty

Efektívne, systematické a reprodukovateľné experimenty, spolu s presným zaznamenávaním výsledkov, sú kľúčové pre 
overenie a porozumenie výkonnosti modelov.

#### Zaznamenávanie výsledkov:

Zaznamenávanie výsledkov v kontexte strojového učenia znamená zaznamenávanie metrík výkonnosti modelu, ale aj 
hyperparametrov, verzii použitých dátových sád, špecifík algoritmov, atď.. To umožňuje nielen reprodukovanie 
experimentov, ale aj porovnávanie výsledkov cez rôzne experimenty. Na zaznamenávanie môžete použiť Python knižnice,
napr. `logging`, alebo si vytvoriť vlastnú implementáciu.

Priklad použitia knižnice logging:
```python
import logging

# Set the CSV logging format
csv_format = '%(asctime)s, %(levelname)s, %(message)s'
# Configuration
logging.basicConfig(level=logging.DEBUG,
                    format=csv_format,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.FileHandler("logs.csv")],
                    filemode='a')

# Log Examples
logging.debug('Debugging message')
logging.info('Information message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
```

#### Experimenty a Best Practices:

Experimenty sú systematické procesy testovania, hodnotenia a porovnávania rôznych modelov, algoritmov, dátových sád a 
parametrov, aby sa zistila najlepšia kombinácia pre daný úlohu alebo problém. Experimenty umožňujú iteratívne skúmať 
rôzne prístupy a identifikovať optimálne riešenia. Cieľom experimentovania je nielen nájsť najefektívnejšie modely 
ale aj pochopiť, ako rôzne aspekty ovplyvňujú výsledky predikcií a odolnosť modelu voči rôznym typom dát.

- **Replikácie**: Použitie replikácií v experimentoch overuje, či sú výsledky modelu spoľahlivé a ich výskyt nie je 
náhodný. Replikácie potvrdzujú alebo vyvracajú zistenia tým, že testujú modely na rôznych údajoch alebo s rôznymi nastaveniami.

- **Verziovanie kódu a dát**: Použitie nástrojov ako Git pre kód a DVC (Data Version Control) pre dáta pomáha zachovať
históriu zmen a uľahčuje beh experimentov s rôznymi konfiguráciami, podmnožinami údajov a pod..
 
- **Dokumentácia**: Podrobná dokumentácia experimentov, vrátane predpokladov, metodológie a **interpretácie výsledkov**,
je nevyhnutná pre reprodukovateľnosť, a odovzdávanie znalostí.

