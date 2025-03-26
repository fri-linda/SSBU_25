# SSBU CV5: Exploračná analýza dát (EDA)

Exploračná analýza dát (EDA) je kľúčovým krokom v procese analýzy dát, ktorý nám umožňuje porozumieť podkladovým vzorcom, detekovať odľahlé hodnoty, a testovať predpoklady pomocou sumárnych štatistík a grafických reprezentácií. EDA zahrňuje techniky ako:

- **Vizualizácia distribúcie premenných:** Pomocou histogramov alebo boxplotov môžeme skúmať rozloženie jednotlivých premenných.

- **Kontrola chýbajúcich hodnôt:** Identifikácia a riešenie chýbajúcich hodnôt je nevyhnutná pre zabezpečenie kvality dát.

- **Porozumenie vzťahom medzi premennými:** Scatter ploty a korelačné matice nám umožňujú identifikovať vzťahy medzi premennými.

- **Významnosť prvkov (Feature Importance):** Identifikácia a vizualizácia významnosti jednotlivých prvkov (črty, atribúty) v dátach môže pomôcť určiť, ktoré prvky majú najväčší vplyv na cieľovú premennú. Toto je obzvlášť užitočné pri výbere funkcií pre modelovanie strojového učenia.

- **Pair Plot (Dvojrozmerný rozptylový graf):** Tento typ grafu zobrazuje párové vzťahy medzi viacerými premennými v datasete. Umožňuje rýchlo identifikovať typy vzťahov medzi premennými, vrátane lineárnych vzťahov, korelácií, alebo potenciálnych skupín (klastrov).

EDA nám poskytuje užitočné vhľady, ktoré môžu viesť k lepšiemu pochopeniu dát a efektívnejšiemu modelovaniu.

## Normalizácia a štandardizácia

**Normalizácia** a **štandardizácia** sú dve techniky predspracovania dát používané na zmenšenie rozdielov medzi rozsahmi hodnôt rôznych premenných.

### Normalizácia
Normalizácia sa týka procesu škálovania dát tak, aby sa zmestili do určitého rozsahu, často medzi 0 a 1. Táto technika je užitočná pre algoritmy, ktoré rovnako zvažujú vstupy a pomáha urýchliť učenie tým, že konvertuje funkcie na podobnú škálu.

### Štandardizácia
Štandardizácia zahŕňa preškálovanie dát tak, aby mali priemer 0 a štandardnú odchýlku 1. Tento proces transformuje vlastnosti tak, aby mali vlastnosti štandardného normálneho rozdelenia, čo je obzvlášť prospešné, keď algoritmus predpokladá, že dáta sú normálne distribuované.

Použitie týchto techník môže výrazne zlepšiť výkonnosť modelov strojového učenia tým, že zabezpečí, že dáta sú spracované na konzistentnej a vhodnej škále.
