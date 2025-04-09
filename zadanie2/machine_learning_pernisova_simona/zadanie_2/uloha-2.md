# Recall

**Recall** ("citlivosť" alebo "úplnosť") je metrika, ktorá hodnotí, akú časť skutočne pozitívnych prípadov (tých, ktoré sú správne označené ako pozitívne) model správne identifikoval.

**Recall** definovaný ako:

Recall = True Positives / (True Positives + False Negatives)

- **True Positives (TP)**: Počet správne identifikovaných pozitívnych prípadov.
- **False Negatives (FN)**: Počet pozitívnych prípadov, ktoré model nesprávne označil ako negatívne.

## Príklad

Ak mám 100 pacientov, z ktorých 30 je skutočne chorých, a model identifikuje 25 z týchto 30 ako chorých, Recall bude:

Recall = 25 / (25 + 5) = 0.83

čiže model správne identifikoval 83% chorých pacientov.
