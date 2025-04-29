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

Data Scaling:         Pareto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)

1: T-test -  Premenná Bin.2.70 vykazuje štatisticky najvýraznejší rozdiel medzi porovnávanými skupinami, s extrémne nízkou p-hodnotou (3.12×10⁻¹³). 

To naznačuje, že táto premenná je vysoko diskriminačná a významná pre rozlíšenie skupín.

2: PCA - ukázala, že hlavné komponenty ako PC1 a PC2 zachytávajú podstatnú časť variability medzi vzorkami. 

Napríklad vzorka C004 sa v PC2 silne odlišuje, čo poukazuje na jej odlišné vlastnosti oproti ostatným.

3: PLSDA - Premenná Bin.8.74 dosiahla najvyššie VIP skóre (2.69), čím sa ukázala ako najvýznamnejšia pre klasifikáciu medzi skupinami. 

PLS-DA identifikuje premenne, ktoré najviac prispievajú k separácii tried, čo pomáha pri biologickej interpretácii rozdielov.

4: Dendogram - Hierarchická analýza klastrov ukázala, že vzorky sa prirodzene zoskupujú do 2 až 3 hlavných klastrov. 

To naznačuje, že medzi vzorkami existuje štruktúra podobnosti, ktorá môže odrážať biologické alebo klinické rozdiely.

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
