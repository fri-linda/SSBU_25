## Zadanie 4 (5b)

V tomto zadaní budete pracovať s nástrojom MetaboAnalyst a datasetom: **NMR spectral bins**
    
`Binned 1H NMR spectra of 50 urine samples using 0.04 ppm constant width (Psihogios NG, et al.) Group 1- control; group 2 - severe kidney disease.`
    
Tento dataset je dostupný v sekcii 'Try our test data' v nástroji pre Jednofaktorovú štatistickú analýzu. 

Dataset pochádza z NMR-metabolomickej štúdie: Hodnotenie závažnosti tubulointersticiálnych lézií u pacientov s glomerulonefritídou. Začiatok tubulointersticiálnych lézií je charakterizovaný zníženým vylučovaním citrátu, hipurátu, glycínu a kreatinínu, zatiaľ čo po ďalšom zhoršení nasleduje glykozúria, selektívna aminoacidúria, úplné vyčerpanie citrátu a hipurátu a postupné zvyšovanie vylučovania laktátu, acetátu a trimetylamín-N-oxidu. Metabonomická analýza moču založená na NMR by mohla prispieť k včasnému hodnoteniu závažnosti poškodenia obličiek a prípadne k monitorovaniu ich funkcie. [1]


Načítajte množinu údajov v nástroji MetaboAnalyst. Pri filtrovaní údajov (Data filter) môžete použiť predvolené nastavenia.

### Úloha 1 (1b)

Normalizujte distribúciu datasetu (pre premenné aj vzorku).
(Vyberte akúkoľvek kombináciu operácií, ktorá je podľa Vás najlepšia).

**Ktoré operácie ste pri normalizácii použili?**
Sample normalization: normalization by median
Data Transformation:  square root transformation
Data Scaling:         auto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)

**1: Na základe analýzy Fold Change (FC) som zistil, že 47 znakov vykazuje štatisticky významný pokles a 6 znakov štatisticky významný nárast, čo naznačuje, že tieto znaky sa medzi porovnávanými skupinami výrazne líšia. Zvyšných 147 znakov nepreukázalo štatisticky významnú zmenu, a preto nie je možné potvrdiť rozdiel medzi skupinami pre tieto znaky.**

**2: Na základe t-testu s hladinou významnosti p = 0,05 som zistil, že 104 znakov je štatisticky významných, čo naznačuje, že medzi porovnávanými skupinami existujú rozdiely pre viac ako polovicu analyzovaných znakov. Zvyšných 96 znakov nepreukázalo významnú zmenu, a preto ich nemožno považovať za rozdielne medzi skupinami.**

**3: Na základe PCA analýzy a následného zhlukovania pomocou K-means algoritmu bolo možné identifikovať tri odlišné zhluky. Vizuálne pozorujeme, že vzorky pacientov a kontrol sa prevažne zoskupujú do samostatných zhlukov, čo naznačuje, že medzi nimi existujú výrazné rozdiely vo vybraných hlavných komponentoch. Najväčšiu časť variability údajov zachytávajú hlavné komponenty PC1 (24,1 %) a PC2 (16,2 %), čo poukazuje na ich význam pri rozlíšení medzi skupinami.**

**4: Na základe analýzy pomocou Random Forest s 500 stromami a 7 prediktormi bolo možné identifikovať dve odlišné skupiny: pacientov a kontrol. Výsledky ukazujú, že model dosiahol celkovú chybu (OOB error) 0.06, čo naznačuje vysokú presnosť klasifikácie. Chyba klasifikácie pre kontrolnú skupinu bola 0.04, zatiaľ čo pre skupinu pacientov 0.08, čo poukazuje na mierne lepšiu rozpoznateľnosť kontrolných vzoriek. Významné premenné (Var. Importance) a detekcia odľahlých hodnôt (Outlier Detection) prispeli k lepšiemu pochopeniu rozdielov medzi skupinami. Tieto výsledky potvrdzujú, že Random Forest efektívne rozlišuje medzi pacientmi a kontrolami na základe zvolených prediktorov.**



Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
