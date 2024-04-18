class Read:
	def __init__(self, nome, seq, qual):
		self.nome = nome
		self.seq = seq
		self.qual = qual

	def avg_qual(self):
		N = 0
		for q in self.qual:
			N += ord(q) - 33
		return N / len(self.qual)

fq_path = "reads.fq"

nome = ""
seq = ""
qual = ""
Reads = []
i = 0
for line in open(fq_path):
	i+=1
	if i == 1:
		# Leggiamo l'identificatore
		if nome != "":
			# Se abbiamo già letto un record, salviamolo
			Reads.append(Read(nome, seq, qual))
		# Aggiorniamo l'identificatore per la prossima read
		nome = line.strip("\n")[1:]
	elif i == 2:
		# Leggiamo la sequenza
		seq = line.strip("\n")
	elif i == 3:
		pass # non facciamo niente
	elif i == 4:
		# Leggiamo la qualità
		qual = line.strip("\n")
		i = 0 # risettiamo i a 0
# aggiungiamo l'ultima read
if nome != "":
	Reads.append(Read(nome, seq, qual))

for read in Reads:
	print(read.nome, round(read.avg_qual(), 3))
