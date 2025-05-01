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
Sample normalization: Normalization by median
Data Transformation:  Log transformation
Data Scaling:         Auto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

1: Pri použití pearsonovho korelačného koeficientu je najvyššia negatívna korelácia medzi premennými 7.66(x) a 0.86(y), a koeficient korelácie je -0.814.
2: Scree plot - najväčší prírastok vysvetlenej variability nastáva medzi PC1 a PC2, čo naznačuje, že tieto dva komponenty obsahujú najviac informácie.
   Od PC3 ďalej je prírastok vysvetlenej variability menší, čo naznačuje klesajúci prínos ďalších komponentov.
3: T-test (hladina vyznamnosti 5%) - z celkového počtu 200 featureov je 77 označených ako signifikantné (fialové body), čo naznačuje, že medzi dvomi skupinami existuje štatisticky významný rozdiel vo viacerých premenných.
   Viaceré featury majú hodnoty na osi y nad 5 až 10, čo znamená veľmi nízke p-hodnoty (napr. p < 10⁻⁵ až 10⁻¹⁰), a teda silné dôkazy proti nulovej hypotéze
4: PLSDA - Impotance features - všetky zobrazené biny majú VIP skóre > 1.7, pričom najvyššie skóre (=> 2.2) majú Bin.0.82, Bin.2.54, Bin.2.70 a Bin.094
   Tieto Biny najviac prispievajú k rozdielu medzi skupinami, a tak by boli vhodný kandidáti pre biomarkerovy vyskum.

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
