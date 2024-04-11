# Corso PNRR - "Python e Bioinformatica"

Per ogni domanda/chiarimento, scrivete pure una mail a [luca.denti@unimib.it](mailto:luca.denti@unimib.it)

## Laboratorio 1 - [Slides](https://hackmd.io/@ldenti/Sy7zZpMkR)

### Contenuto
* Introduzione
	* Algoritmo
	* Pseudocodice
	* Linguaggio di Programmazione
* python
	* IDLE
	* Variabili
	* Stringhe
	* Funzioni print/input
	* Variabili booleane
	* Liste, Insiemi e Dizionari
	* Programmazione imperativa
		* Scelta
		* Ripetizione
	* Scrivere e leggere da file

### [Soluzioni](lab1/)

## Laboratorio 2 - [Slides](https://hackmd.io/@ldenti/rychJXQkR)

### Contenuto
* DNA: nucleotidi e strand
* Reverse&Complement
* Formato FASTA
* Funzioni in python
* Sintesi delle proteine

### Materiale aggiuntivo per gli esercizi
* File di input: [sequenze.fa](lab2/sequenze.fa) (file di test più piccolo: [sequenze.test.fa](lab2/sequenze.test.fa)).
* Dizionario del codice genetico (esercizio 7):
```python
CODON = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'$', 'TAG':'$',
    'TGC':'C', 'TGT':'C', 'TGA':'$', 'TGG':'W'}
```

### Soluzioni
