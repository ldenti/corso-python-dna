# Esercizio 1
def r_and_c(S):
    rc_dict = {"A":"T", "C":"G", "G":"C", "T":"A"}
    S_rc = ""
    for c in S[::-1]:
        c = c.upper()
        S_rc += rc_dict[c] if c in rc_dict else "N"
    return S_rc

# Questo è il file di input
fp = "sequenze.test.fa"

# Esercizio 2
SEQS = {}
idx = ""
seq = ""
for line in open(fp):
    line = line.strip("\n")
    if line.startswith(">"):
        if idx != "":
            SEQS[idx] = seq
        idx = line[1:].split(" ")[0]
        seq = ""
    else:
        seq += line
if seq != "":
    SEQS[idx] = seq

# Esercizio 3
of = open("sequenze.rc.fa", "w")
for idx, seq in SEQS.items():
    of.write(f">{idx}_rc\n")
    of.write(r_and_c(seq) + "\n")
of.close()

# Esercizio 4
FULL_COUNTS = {"A":0, "C":0, "G":0, "T":0, "N":0}
FULL_L = 0 # total length
for idx, seq in SEQS.items():
    COUNTS = {"A":0, "C":0, "G":0, "T":0, "N":0}
    for c in seq:
        c = c.upper()
        if c not in COUNTS:
            c = "N"
        COUNTS[c] += 1
    for c in COUNTS:
        FULL_COUNTS[c] += COUNTS[c]
        COUNTS[c] = COUNTS[c] / len(seq)
    FULL_L += len(seq)
    print(idx, COUNTS)

print("")

for c in FULL_COUNTS:
    FULL_COUNTS[c] /= FULL_L
print(FULL_COUNTS)

# Esercizio 5
SE_CODONS = {"ATG":0, "TAG":0, "TAA":0, "TGA":0}
for idx, seq in SEQS.items():
    for i in range(0, len(seq)-3+1):
        codon = seq[i:i+3].upper()
        if codon in SE_CODONS:
            SE_CODONS[codon] += 1
print("Numero di codoni di start:", SE_CODONS["ATG"])
print("Numero di codoni di end:", SE_CODONS["TAG"] + SE_CODONS["TAA"] + SE_CODONS["TGA"])
for k,v in SE_CODONS.items():
    print(k, v)

# Esercizio 6
for idx, seq in SEQS.items():
    for i in range(0, len(seq)-3+1):
        codon = seq[i:i+3]
        if codon == "ATG":
            print(f"{idx}:{i}")

# Esercizio 7
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

of = open("proteine.fa", "w")
for idx, seq in SEQS.items():
    # print(">", len(seq) % 3)
    p_seq = ""
    for i in range(0, len(seq)-3+1):
        codon = seq[i:i+3]
        p_seq += CODON[codon]
    of.write(f">{idx}\n")
    of.write(p_seq + "\n")

    # Esercizio 7b
    # wrap = 60
    # i = 0
    # while i<len(p_seq):
    #     of.write(p_seq[i:i+wrap] + "\n")
    #     i+=wrap
of.close()
