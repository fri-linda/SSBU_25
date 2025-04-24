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

Sample normalization: Normalization by sum

Data Transformation:  Log transformation (base 10)

Data Scaling:         Auto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)

1: Correlations -> Metóda nám ukázala vysokú pozitívnu koreláciu (0.947) na riadku Bin.6.74 a stĺpci Bin.9.10, čo poukazuje na takmer úplnú lineárnu závislosť medzi týmito dátovými binmi. 

2: SVM -> Graf ukazuje, že najnižšia chybovosť klasifikácie pomocou SVM bola dosiahnutá pri výbere 14 premenných (5,2 %), pričom menej alebo viac premenných viedlo k vyššej chybovosti (Pri 8 premenných bola najvyššia chybovosť - 9.6%).

3: K-means -> K-means nám rozdelil dáta na dva klastre, pričom väčšina zdravých osôb spadá do klastra 1 a väčšina pacientov do klastra 2 – no zároveň vidíme, že dvaja zdraví jedinci boli zaradení do klastra s pacientmi, čo môže naznačovať ich podobnosť s pacientskou skupinou (taktiež aj dvaja pacienti boli zaradení medzi zdravých). 

4: PCA -> PCA analýza ukázala, že prvé dve hlavné komponenty (PC1 s 21.2% variabilitou, PC2 s 16.1% variabilitou) nám najviac prispievajú k separácii medzi zdravou skupinou a skupinou s pacientmi.  

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
