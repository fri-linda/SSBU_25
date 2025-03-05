# SSBU CV3: Práca s databázami

### National Center for Biotechnology Information
- Súbor biomedicínskych a biotechnologických databáz
- Voľne prístupné - www.ncbi.nlm.nih.gov/
- GenBank - DNA databáza
- PubMed - publikačná databáza

#### GenBank
- Prístup buď cez Google Search: genbank, alebo priamo - www.ncbi.nlm.nih.gov/genbank/

<img src="data/genbank1.png" alt="Workflow diagram" width="70%"/>

- Vyhľadávanie - možnosť vybrať si konkrétnu databázu a hľadať konkrétny gén v orghanizme (napr. P53 homo sapiens)
   - V rámčeku na začiatku výsledkov sú zobrazené informácie o hľadanom géne ako aj jeho ďalšie kódovania

<img src="data/genbank2.png" alt="Workflow diagram" width="40%"/>

- Taxonómia - zaradenie organizmov (druh, rod, čeľaď, ..) na základe ich vzájomných príbuzenských a evolučných vzťahov
   - Zobrazenie vo forme listu alebo stromu

 <img src="data/genbank3.png" alt="Workflow diagram" width="70%"/>
 
+ Výsledky vyhľadávania - označenie
   + Kompletná alebo čiastočná kódovacia sekvencia (complete cds/partial cds)
   + Prístupové číslo - AB082923.1
   + GenInfo Identifier - 23491728

 <img src="data/genbank4.png" alt="Workflow diagram" width="40%"/>
     
+ Zobrazenie výsledku - po otvorení vybraného výsledku (napr. Homo sapiens mRNA for P53, complete cds)
   + Štruktúrovaná forma
   + Základné údaje
  
 <img src="data/genbank5.png" alt="Workflow diagram" width="40%"/>

   + Zdroj a organizmus

 <img src="data/genbank6.png" alt="Workflow diagram" width="40%"/>
  
   + Informácie o publikácii
 
 <img src="data/genbank7.png" alt="Workflow diagram" width="40%"/>
  
   + Sekvencia (súbor údajov) - originálna nukleotidová sekvencia proteínu

 <img src="data/genbank8.png" alt="Workflow diagram" width="40%"/>
  
   + Vlastnosti - metadáta
  
  <img src="data/genbank9.png" alt="Workflow diagram" width="40%"/>
  
   + Zdroj, gén a kódovacia sekvencia CDS (kliknutím sa sekvencia zvýrazní v pôvodných údajoch)

 <img src="data/genbank10.png" alt="Workflow diagram" width="40%"/>
 
   + Translácia - preklad genetickej informácie nukleotidov na poradie aminokyselín

 <img src="data/genbank11.png" alt="Workflow diagram" width="40%"/>

   + Kódovanie aminokyselín:
     
 <img src="data/translation.png" alt="Workflow diagram" width="40%"/>
 
   + Zobrazenie detailov - spodný panel - dobré pri dlhých pôvodných sekvenciách (ostáva na obrazovke pri posúvaní sa smerom dolu)

 <img src="data/genbank12.png" alt="Workflow diagram" width="40%"/>
   
   - Export údajov do súboru

 <img src="data/genbank13.png" alt="Workflow diagram" width="25%"/>
 
   - Formát sekvencie
     - FASTA
     - Grafický
       
 <img src="data/genbank14.png" alt="Workflow diagram" width="50%"/>
  
 <img src="data/genbank15.png" alt="Workflow diagram" width="100%"/>
  
 - Zobrazenie detailov - nabehnutím myšou na jednotlivé úseky (región, poloha, dĺžka, odkazy na databázy)

   <img src="data/genbank16.png" alt="Workflow diagram" width="60%"/>
   
 - CDD (Conserved Domain Database) - anotácie proteínov, popis funkcie génu (zobrazenie podrobnejších informácií - obrázok, vlastnosti, taxonómia, ..)

  <img src="data/genbank17.png" alt="Workflow diagram" width="80%"/>

#### PubMed
- Prístup buď cez Google Search: pubmed, alebo priamo - www.pubmed.ncbi.nlm.nih.gov/

 <img src="data/pubmed1.png" alt="Workflow diagram" width="80%"/>
 
- Jednoduché vyhľadávanie alebo možnosť "Advanced"
  - Vytváranie dotazu podľa konkrétnych atribútov, alebo ich kombinácie (dáva aj nápovedu)

 <img src="data/pubmed2.png" alt="Workflow diagram" width="80%"/>
 <img src="data/pubmed3.png" alt="Workflow diagram" width="80%"/>
 <img src="data/pubmed4.png" alt="Workflow diagram" width="80%"/>
 
- Zoradenie výsledkov

 <img src="data/pubmed5.png" alt="Workflow diagram" width="30%"/>
 
- Filtrovanie výsledkov (full text, free full text)

 <img src="data/pubmed6.png" alt="Workflow diagram" width="20%"/>

- Výsledky vyhľadávania

 <img src="data/pubmed7.png" alt="Workflow diagram" width="60%"/>

- Detailné zobrazenie článku
   - PMID (PubMed Identifier), PMCID (PubMed Central Identifier), DOI (Digital Object Identifier)

  <img src="data/pubmed8.png" alt="Workflow diagram" width="60%"/>
 
   - Abstrakt a kľúčové slová

  <img src="data/pubmed9.png" alt="Workflow diagram" width="60%"/>
  
   - Obrázky

  <img src="data/pubmed10.png" alt="Workflow diagram" width="60%"/>
  
   - Podobné články

  <img src="data/pubmed11.png" alt="Workflow diagram" width="60%"/>
  
   - Citácie článku

  <img src="data/pubmed12.png" alt="Workflow diagram" width="60%"/>

   - Referencie použité v článku

  <img src="data/pubmed13.png" alt="Workflow diagram" width="60%"/>

   - Link na celý obsah článku
 
  <img src="data/pubmed14.png" alt="Workflow diagram" width="60%"/>
  
   - Vygenerovanie citácie, výber formátu citácie

  <img src="data/pubmed15.png" alt="Workflow diagram" width="50%"/>

   - Stiahnutie do súboru (citácia, abstrakt, PMID, ..)

  <img src="data/pubmed16.png" alt="Workflow diagram" width="80%"/>

  <img src="data/pubmed17.png" alt="Workflow diagram" width="50%"/>

----
##### Referencie
https://towardsdatascience.com/starting-off-in-bioinformatics-rna-transcription-and-translation-aaa7a91db031

www.ncbi.nlm.nih.gov/genbank/

www.pubmed.ncbi.nlm.nih.gov/
