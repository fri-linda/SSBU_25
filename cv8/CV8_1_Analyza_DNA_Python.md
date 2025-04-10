# CV9: Analýza údajov DNA

## Spracovanie reťazcov v Pythone

Python poskytuje množstvo vstavaných funkcií na spracovanie reťazcov, ktoré sú užitočné pri práci s DNA/RNA sekvenciami. Tu sú niektoré z nich, ktoré sa používajú v kóde:

- **`str.maketrans()`**: Používa sa na vytvorenie tabuľky pre preklad znakov. Táto tabuľka sa následne používa s funkciou `translate()` na nahradenie znakov v reťazci. [Dokumentácia str.maketrans](https://docs.python.org/3/library/stdtypes.html#str.maketrans)

- **`str.translate()`**: Nahrádza znaky v reťazci podľa tabuľky vytvorenej pomocou `maketrans()`. [Dokumentácia str.translate](https://docs.python.org/3/library/stdtypes.html#str.translate)

- **`str.count()`**: Počíta výskyt konkrétneho znaku alebo podreťazca v reťazci. [Dokumentácia str.count](https://docs.python.org/3/library/stdtypes.html#str.count)

- **`str.replace()`**: Nahrádza všetky výskyty podreťazca iným podreťazcom. [Dokumentácia str.replace](https://docs.python.org/3/library/stdtypes.html#str.replace)

- **`len()`**: Vráti dĺžku reťazca (počet znakov). [Dokumentácia len](https://docs.python.org/3/library/functions.html#len)

- **`str.strip()`**: Odstráni medzery alebo iné znaky z oboch strán reťazca. [Dokumentácia str.strip](https://docs.python.org/3/library/stdtypes.html#str.strip)

- **`str.find()`**: Nájde prvý výskyt podreťazca v reťazci a vráti jeho index. Ak sa podreťazec nenájde, vráti -1. [Dokumentácia str.find](https://docs.python.org/3/library/stdtypes.html#str.find)

- **`list()`**: Konvertuje reťazec na zoznam znakov, čo umožňuje jednoduchú manipuláciu s jednotlivými znakmi. [Dokumentácia list](https://docs.python.org/3/library/functions.html#func-list)

- **`random.randint()`**: Generuje náhodné celé číslo v zadanom rozsahu. Používa sa na výber náhodného indexu v reťazci. [Dokumentácia random.randint](https://docs.python.org/3/library/random.html#random.randint)

- **`random.choice()`**: Náhodne vyberie prvok zo zadaného zoznamu alebo reťazca. [Dokumentácia random.choice](https://docs.python.org/3/library/random.html#random.choice)

Tieto funkcie sú základom pre manipuláciu s DNA/RNA sekvenciami, ako je tvorba komplementárnych reťazcov, mutácie a analýza obsahu báz.

---

## Python knižnice na prácu s DNA/RNA sekvenciami

### Knižnica Biopython (SeqIO)

Interface `SeqIO` z Biopythonu je určený na prácu s biologickými sekvenciami, ako sú DNA, RNA a proteíny. Umožňuje načítanie, spracovanie a analýzu sekvencií z rôznych formátov, ako sú FASTA, GenBank, a ďalšie.

#### Atribúty sekvencií

Po načítaní sekvencie pomocou `SeqIO` získate objekt, ktorý obsahuje rôzne atribúty a metódy na prácu so sekvenciou. Tu sú niektoré z najdôležitejších:

- **`id`**: Identifikátor sekvencie (napr. názov sekvencie v súbore).
  - Príklad: `record.id`
  
- **`seq`**: Samotná sekvencia ako objekt typu `Seq`. Tento objekt podporuje manipuláciu s DNA/RNA sekvenciami.
  - Príklad: `record.seq`
  
- **`description`**: Popis sekvencie.
  - Príklad: `record.description`
  
- **`annotations`**: Slovník obsahujúci anotácie sekvencie, ako sú zdroj, organizmus, a ďalšie.
  - Príklad: `record.annotations`
  
- **`features`**: Zoznam funkčných prvkov sekvencie, ako sú gény, CDS (kódovacie sekvencie), a ďalšie.
  - Príklad: `record.features`
  
- **`letter_annotations`**: Slovník obsahujúci anotácie pre jednotlivé písmená sekvencie (napr. kvalita báz).
  - Príklad: `record.letter_annotations`

#### Metódy na prácu so sekvenciami

- **`reverse_complement()`**: Vráti reverzný komplement sekvencie.
  - Príklad: `record.seq.reverse_complement()`
  
- **`transcribe()`**: Prevod DNA sekvencie na RNA.
  - Príklad: `record.seq.transcribe()`
  
- **`translate()`**: Preklad DNA alebo RNA sekvencie na proteín.
  - Príklad: `record.seq.translate()`
  
- **`count()`**: Počíta výskyt konkrétneho znaku alebo podreťazca v sekvencii.
  - Príklad: `record.seq.count("G")`

#### Dokumentácia

- [Biopython SeqIO](https://biopython.org/wiki/SeqIO)
- [Biopython Seq objekt](https://biopython.org/wiki/Seq)

---

#### Úloha 1: Načítajte sekvenciu z databázy Genbank

+ Stiahnite z databázy Genbank sekvenciu nukleotidov NC_005816 vo formáte genbank a vložte ju do priečinka `inputs`.
+ Pomocou knižnice Bio s použitím SeqIO a metódy `read()` načítajte sekvenciu zo súboru `inputs/NC_005816.gb` a vypíšte na konzolu, čo bolo načítané.

#### Úloha 2: Vytvorte Komplementárny Reťazec

- Príklad: Pre DNA reťazec `5'- AGTCC -3'` je komplementárny reťazec `3'- TCAGG -5'`.
- Vytvorte komplementárny reťazec k nasledujúcej DNA sekvencii: `5'-TACCGGAT-3'`
- String v pythone má metódy, ktorými môžete v reťazci nahradiť písmená inými:
    - str.maketrans() - vytvorenie tabuľky pre preklad znakov - [Dokumentácia](https://docs.python.org/3/library/stdtypes.html#str.maketrans)
    - str.translate() - nahradenie znakov v reťazci s použitím vytvorenej tabuľky - [Dokumentácia](https://docs.python.org/3/library/stdtypes.html#str.translate)

#### Úloha 3: Vytvorte mutáciu génu

+ Stiahnite z databázy Genbank sekvenciu nukleotidov AE017046.1 vo formáte fasta a vložte ju do priečinka `inputs`.
+ Načítajte túto sekvenciu zo súboru `inputs/AE017046.1.fasta` a vypíšte ju na konzolu.
+ Vytvorte funkciu `mutate` s parametrom `dna`, v ktorej na náhodnej pozícii v reťazci zmeníte hodnotu bázy na inú (z ATGC). (Konvertujte sekvenciu na list, na vygenerovanom indexe zmeňte hodnotu a vráťte nazad string.)
    + Na generovanie použite funkcie `randint()` a `choice()` knižnice random - [Dokumentácia random](https://docs.python.org/3/library/random.html)
+ Pomocou cyklu zopakujte vykonanie 1000 náhodných mutácií.
+ Vypíšte sekvenciu po mutáciách.

#### Úloha 4: Vypočítajte podiel guanino-cytozínových komplementárnych párov v sekvencii

+ V načítanej sekvencii AE017046.1 spočítajte počet Cytozínových a Guanínových báz a vypočítajte ich podiel v celkovom DNA reťazci.
    + Použite atribúty a ich metódy implementované v knižnici SeqIO, ktoré je možné použiť na načítanej sekvencii - záznam má atribút `.seq`.





