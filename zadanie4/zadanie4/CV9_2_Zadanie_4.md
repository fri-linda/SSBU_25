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
Data Transformation:  Normalization by sum
Data Scaling:         Normalization by sum
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)
1: Pri použití t-testu sme zistili, že najvýznamnejší rozdiel medzi skupinami bol v ppm oblasti 3.04, kde p-hodnota bola 0.00002, čo poukazuje na výrazný rozdiel medzi kontrolnou skupinou a pacientmi.
2: ri použití PCA analýzy sme zistili, že prvé dve hlavné komponenty vysvetľujú spolu 37,3 % variability v dátach (PC1: 21,2 %, PC2: 16,1 %). Vzorky kontrolnej skupiny a pacientov sa v PCA priestore čiastočne oddeľujú, pričom pacienti majú väčšiu variabilitu.
3: PLS-DA analýza ukazuje výrazné oddelenie medzi skupinou pacientov a kontrol. Na základe skóre vzoriek v priestore prvých dvoch komponentov je viditeľné, že jednotlivé skupiny sa oddeľujú, pričom väčšina pacientov aj kontrol sa správne zoskupila.
Výsledky PLS-DA naznačujú, že existuje systematický rozdiel medzi skupinami, ktorý môže byť využitý na klasifikáciu.
4:  Heatmapa s nadväzujúcim dendrogramom zoskupila vzorky do dvoch hlavných klastrov, ktoré presne korelujú s kontrolnou skupinou a skupinou pacientov. Rôzne metabolity (ppm signály) majú vo vzorkách pacientov systematicky odlišné hladiny v porovnaní s kontrolou.

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
