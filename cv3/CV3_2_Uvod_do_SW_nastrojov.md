# SSBU CV3: Úvod do softvérových nástrojov pre analýzu biomedicínskych dát

## Nástroje v bioinformatike

<img src="data/workflow.png" alt="Workflow diagram" width="60%"/>

---

### Databázy
Databázy sa používajú na získanie informácií na identifikáciu problému a formovanie hypotéz.
- Získanie dostatočného množstva údajov na experimenty a validáciu
- Viac relevantná vzorka (opatrne s kombinovaním databáz z rôznych kontinentov)

+ _Metadatabázy_ - zhromažďujú údaje o údajoch, pre generovanie nových údajov
+ Prehľad biomedicínskych databáz -  www.science.co.il/biomedical/databases/

<img src="data/IsraelScienceDatabase.png" alt="Biomedical database collection" width="80%"/>

- Najznámejšie databázy v Genetike:
  + EMBL's European Bioinformatics Institute - www.ebi.ac.uk
  - National Center for Biotechnology Information -  www.ncbi.nlm.nih.gov
  - University of California, Santa Cruz - www.genome-euro.ucsc.edu/cgi-bin/hgGateway
  - DNA DataBank of Japan - www.ddbj.nig.ac.jp/search/en 

#### Štandardy
- Protokoly pre štruktúrovanie, ukladanie a výmenu
- Zabezpečenie interoperability údajov
- Urýchlenie výskumu
- Relevantné metadáta
- Základné štandardy:
  - FASTA - sekvencie DNA
  - DICOM - obrazové údaje
  - SNOMED CT - klinická terminológia
  - BioPAX - údaje o biologických dráhach
  - HL7 - klinické a administratívne dáta
  - množstvo ďalších

<img src="data/standards.png" alt="Standards" width="50%"/>
<br>
    
#### Spolupráca databáz
- Pochopenie súvislostí
- Odhalenie komplexných závislostí
- Spolupráca na globálnej úrovni 
- Projekty:
  - Human Genome Project (HGP) - mapovanie a sekvenovanie ľudského genómu
  - International Cancer Genome Consortium (ICGC) - genetické zmeny v rôznych typoch nádorov 

----

### Nástroje na analýzu
- Množstvo existujúcich nástrojov : online/desktop
   - Online - Galaxy, GenePattern, FIJI, ..
   - Desktop - PyMOL, GeneiousPrime, 3DSlicer, ..
- Programovacie jazyky + knižnice (Python, MATLAB, R, C++, ..)

<img src="data/libraries.png" alt="Libraries" width="45%"/>
   
+ Výber správneho nástroja / knižnice
+ Určiť si potrebné metódy pre spracovanie a analýzu
   + Typ údajov (obrazové, signálové, textové, číselné, ..)
   + Matematické metódy pre spracovanie, algoritmy strojového/hlbokého učenia a pod. ()
   + Metriky pre vyhodnocovanie
+ Vizualizácia údajov - pochopenie štruktúry a distribúcie údajov, identifikácia vzorov a anomálií

<img src="data/methods.jfif" alt="methods" width="100%"/>

----
### Nástroje na vyhodnocovanie výsledkov
- Môžu byť súčasťou nástrojov na analýzu, alebo samostatne
- Najmä nástroje na vizualizáciu komplexných výsledkov v zrozumiteľnej forme a vytváranie grafov
- Prezentácia výsledkov výskumu
- Možnosť sledovania trendov (epidemiologická situácia)
- Dôležité pre podporu rozhodovania ďalšieho smerovania výskumu
- Príklady nástrojov:
   - Nástroje - Prism (GraphPad), SAS (Statistical Analysis System), SPSS (Statistical Package for the Social Sciences), Tableau ..
   - Knižnice:
      - Python - NumPy, Pandas, Matplotlib, SciPy, Statsmodels, ..
      - R - ggplot2, dplyr, caret, tidyr, ..
      - MATLAB - Statistics and Machine Learning Toolbox, Bioinformatics Toolbox, Curve Fitting Toolbox, ..
      - C++ - Boost.Mathm Eigen, Armadillo, ..

<img src="data/evaluation.webp" alt="methods" width="100%"/>

----
##### Referencie
www.science.co.il/biomedical/databases/

www.standardscoordinatingbody.org/standards-benefits

www.researchgate.net/figure/Open-source-DL-research-libraries-with-major-programming-languages-including-Python-C_fig2_340708562

www.geeksforgeeks.org/flowchart-for-basic-machine-learning-models/

www.bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2439-0