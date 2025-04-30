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
Data Transformation:  Log transformation
Data Scaling:         Pareto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)

1: Pri použití *t-testu* som zistil, že 92 z 200 spektrálnych binov vykazuje štatisticky významné rozdiely medzi kontrolnými subjektmi a pacientmi s ťažkým ochorením obličiek. To naznačuje značné metabolické zmeny pri ochorení obličiek, pričom približne 46% nameraných NMR signálov je významne odlišných medzi skupinami.

2: Pri analýze *korelačnej tabuľky* som identifikoval skupiny vysoko korelovaných spektrálnych binov, čo naznačuje, že tieto signály pochádzajú z rovnakých alebo metabolicky príbuzných látok. Napríklad, niektoré spektrálne biny v oblasti 3.98 - 7.82, 1.54 - 0.82.

3: Pri analýze *PCA* (metóda hlavných komponentov) je z grafu "Scree plot" viditeľné, že prvých päť hlavných komponentov vysvetľuje kumulatívne 64,9% celkovej variancie v dátach (PC1: 31,5%, PC2: 14%, PC3: 8,9%, PC4: 5,5%, PC5: 5%). Táto pomerne nízka hodnota vysvetlenej variancie poukazuje na značnú komplexnosť metabolických profilov pacientov s ochorením obličiek. Napriek tomu prvá hlavná komponenta samostatne zachytáva takmer tretinu variancie, čo naznačuje silnú metabolickú signatúru asociovanú s ochorením obličiek.

4: Použitím klasifikačného algoritmu *Random Forest* (s 500 stromami a 7 prediktormi) som dosiahol vysokú presnosť klasifikácie s celkovou chybou OOB len 8%. Zaujímavé je, že algoritmus dokázal bezchybne identifikovať všetkých 25 kontrolných subjektov (0% chyba), zatiaľ čo u pacientov s ochorením obličiek bola presnosť 84% (21 správne klasifikovaných, 4 nesprávne). Tieto výsledky potvrdzujú, že NMR metabolický profil moču obsahuje dostatočne silné biomarkery pre spoľahlivú diagnostiku ochorenia obličiek s potenciálom pre klinické využitie.

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions' severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
