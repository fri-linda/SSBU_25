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
Sample normalization: Normalization by sum,
Data Transformation:  Square root transformation,
Data Scaling:         Auto scaling
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)
1: K-means (k = 3) na PCA binned 1H NMR spektier močových vzoriek vytvoril jeden zhluk prevažne obsahujúci kontrolné vzorky, druhý prevažne vzorky pacientov so závažným poškodením obličiek a tretí menší zmiešaný zhluk.
2: PCA score plot ukazuje, že kontrolné vzorky sa prevažne zoskupujú na ľavej strane osi PC 1 (28,5 %), zatiaľ čo vzorky pacientov so závažným ochorením obličiek sa posúvajú na pravú stranu, hoci medzi nimi existuje mierne prekrytie.
3: Random Forest s 500 stromami a 7 prediktormi dosiahol celkovú OOB chybu 8 %, kde boli všetky kontrolné vzorky (25) správne klasifikované (class.error 0) a zo 25 vzoriek pacientov bolo nesprávne zaradených 4 (class.error 0,16).
4: Z 200 binned 1H NMR signálov je podľa nepárových t-testov s korekciou FDR<0,05 120 výrazne odlišných medzi kontrolnou skupinou a pacientmi so závažným ochorením obličiek, pričom niektoré dosahujú –log10(p) až cez 10.

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
