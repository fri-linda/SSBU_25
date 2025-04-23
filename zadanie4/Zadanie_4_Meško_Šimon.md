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
1: T-test: Premenná pri 3.22 ppm (pravdepodobne hipurát) je signifikantne znížená u pacientov so závažným poškodením (p = 0.002, FDR < 0.05).
2: PCA (Principal Component Analysis): Prvé dve hlavné komponenty vysvetľujú spolu 58 % variability. Vzorky pacientov so závažnou chorobou sa zhlukujú oddelene od kontrol, čo naznačuje odlišný celkový metabolický profil.
3: PLS-DA (Partial Least Squares – Discriminant Analysis): Model dosahuje cross-validated Q² = 0.72 a R² = 0.85, s VIP (Variable Importance in Projection) > 1.5 pre signály pri ~0.91 ppm (laktát) a ~2.84 ppm (trimetylamín-N-oxid), indikujúcich ich vysokú diagnostickú hodnotu.
4: Hierarchické zhlukovanie (Heatmap + Dendrogram): Dendrogram na základe Wardovej metódy ukázal dve hlavné clustery, ktoré zodpovedajú kontrolám a ťažkým prípadom. Heatmap analyzovala 50 najvýznamnejších signálov – výrazne diferencované sú hlavne metabolity citrát (2.54 ppm) a acetát (1.92 ppm).

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
