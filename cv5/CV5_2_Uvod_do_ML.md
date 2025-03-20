# SSBU CV5: Úvod do strojového učenia v Pythone

## Strojové učenie 

- Podmnožina umelej inteligencie, ktorá systémom umožňuje automaticky sa učiť a zlepšovať z vlastných skúseností. 
- Vývoj počítačových programov, ktoré môžu pristupovať k dátam a používať ich na samoučenie.

### Základné pojmy

- **Supervizované učenie**: Algoritmus sa učí z označených trénovacích dát, čo pomáha predpovedať výsledky pre nevidené dáta.
- **Nesupervizované učenie**: Algoritmu nie sú poskytované žiadne označenia, čo mu umožňuje samostatne nájsť štruktúru a vzory vo vstupných údajoch.
- **Reinforcement učenie**: Algoritmus sa učí vykonávať akciu z vlastných skúseností tým, že odmeňuje požadované správanie a/alebo trestá nežiadúce.
- **Hlboké učenie** Štruktúruje algoritmy do vrstiev na vytvorenie umelých neurónových sietí, ktoré sa môžu učiť a rozhodovať samostatne.

### Základné metódy

- **Regresia**: Používa sa na predpovedanie spojitých hodnôt. Príklad: Predpovedanie epidemiologickej situácie.
- **Klasifikácia**: Používa sa na predpovedanie, do ktorej kategórie objekt patrí. Príklad: Určenie typu bunky.
- **Zhlukovanie**: Metóda nesupervizovaného učenia, ktorá sa používa na skupinovanie dát do zhlukov. Príklad: Segmentácia obrazu.

### Základné algoritmy

#### Supervizované učenie

V supervizovanom učení modely predpovedajú výstupnú premennú na základe jednej alebo viacerých vstupných premenných. Cieľom je naučiť sa mapovanie vstupov na výstupy z trénovacích dát.

- **Lineárna regresia**
  - Používa sa na predpovedanie spojitej výstupnej premennej na základe jednej alebo viacerých vstupných premenných.
  - Modeluje vzťah medzi skalárnou závislou premennou a jednou alebo viacerými nezávislými premennými.

+ **Logistická regresia**
  - Používa sa najmä pre binárnu klasifikáciu na predpovedanie pravdepodobnosti príslušnosti vzorky k jednej z dvoch tried.
  - Výstupom je pravdepodobnosť, ktorá sa potom transformuje do dvoch kategórií.

- **Rozhodovacie stromy**
  - Používané pre klasifikáciu aj regresiu. Rozhodovacie stromy delia dátovú súpravu na menšie podskupiny zatiaľ čo súčasne postupne vyvíjajú pridružený strom rozhodnutí.

+ **Náhodné lesy**
  - Vylepšenie rozhodovacích stromov, ktoré používa viacero stromov na vytvorenie robustnejšieho modelu pre klasifikáciu a regresiu.

- **Support Vector Machines (SVM)**
  - Algoritmus, ktorý hľadá hyperrovinu v N-rozmernom priestore (N je počet vlastností), ktorá najlepšie delí dátové body do tried.

#### Nesupervizované učenie

V nesupervizovanom učení modely analyzujú a klasifikujú dáta, ktoré nie sú označené, čím odhaľujú skryté vzory bez vopred definovaných kategórií.

- **K-means zhlukovanie**
  - Algoritmus, ktorý delí dáta do K počtu zhlukov. Každá vzorka je priradená k zhluku s najbližším stredom.

+ **Hierarchické zhlukovanie**
  - Vytvára strom zhlukov, ktoré sú usporiadané hierarchicky. Môže odhaľovať zhluky na rôznych úrovniach granularity.

- **PCA (Principal Component Analysis)**
  - Technika na zníženie rozmerov dát tým, že transformuje dáta do nového súradnicového systému, kde sú prvky zoradené podľa dôležitosti.

#### Reinforcement učenie
V reinforcement učení sa modely učia rozhodovať optimálnymi akciami prostredníctvom odmien alebo trestov z prostredia, čím zlepšujú svoju stratégiu na dynamické dosiahnutie cieľov.

- **Q-learning**
  - Model nezávislý algoritmus, ktorý sa učí hodnotu "akcie" vo vztahu k "stavu" systému s cieľom dosiahnuť maximálnu odmenu.

+ **Deep Reinforcement Learning**
  - Kombinuje reinforcement učenie s hlbokým učením na vytvorenie modelov, ktoré môžu učiť sa z veľkého množstva neštruktúrovaných dát.


## Úvod do knižníc Pythonu pre strojové učenie

Python ponúka množstvo knižníc, ktoré sú špeciálne navrhnuté pre strojové učenie a analýzu dát. Niektoré z najčastejšie používaných knižníc:

### NumPy

- Základný balík pre numerické výpočty v Pythone.
- Poskytuje podporu pre veľké, viacrozmerné polia a matice, spolu so zbierkou matematických funkcií na ich spracovanie.

### Pandas

- Open-source knižnica poskytujúca vysoko výkonné, ľahko použiteľné dátové štruktúry a nástroje na analýzu dát.
- Ideálna pre manipuláciu s dátami a analýzu.

### Matplotlib & Seaborn

- Knižnice pre vytváranie statických, interaktívnych a animovaných vizualizácií v Pythone.
- Matplotlib je vysoko prispôsobiteľný, zatiaľ čo Seaborn poskytuje vyššiu úroveň rozhrania pre kreslenie atraktívnych štatistických grafík.

### Scikit-learn

- Jednoduchý a efektívny nástroj pre dátovú analýzu a ťažbu dát.
- Postavený na NumPy, SciPy a matplotlib, poskytuje rad supervizovaných a nesupervizovaných algoritmov učenia.

### TensorFlow & PyTorch

- Open-source knižnice pre strojové učenie a hlboké učenie.
- Poskytujú komplexné nástroje na vytváranie a trénovanie neurónových sietí, s silnou podporou pre modely hlbokého učenia.
