class Studente:
	def __init__(self, nome, cognome):
		self.nome = nome
		self.cognome = cognome

	def trim(self, n):
		self.nome = self.nome[:n]
		self.cognome = self.cognome[:n]

class Classe:
	def __init__(self, nome):
		self.nome = nome
		self.studenti = []

	def aggiungi(self, s):
		self.studenti.append(s)

	def numero_studenti(self):
		return len(self.studenti)

class Scuola:
	def __init__(self, nome, via):
		self.nome = nome
		self.via = via
		self.classi = []

	def aggiungi(self, c):
		self.classi.append(c)

	def stampa(self):
		print(self.nome, self.via)
		for c in self.classi:
			print(c.nome, c.numero_studenti())
			for s in c.studenti:
				print(s.nome, s.cognome)
			print("---")

# Creiamo due studenti
s1 = Studente("Mario", "Rossi")
s2 = Studente("Giulia", "Verdi")
# Stampiamo le informazioni dei due studenti
print("Studente 1:", s1.nome, s1.cognome)
print("Studente 2:", s2.nome, s2.cognome)
# Riduciamo nome e cognome del secondo studente
s2.trim(3)
# Stampiamo le informazioni aggiornate dello studente 2
print("Studente 2 (modificato):", s2.nome, s2.cognome)

# Creiamo una classe
C = Classe("4C")
# Aggiungiamo gli studenti
C.aggiungi(s1)
C.aggiungi(s2)
# Stampiamo le informazioni della classe
print("Classe:", C.nome)
print("Numero studenti:", C.numero_studenti())
for s in C.studenti: # iteriamo sugli studenti aggiunti alla classe
	print("Studente:", s.nome, s.cognome)

C2 = Classe("5D")
C2.aggiungi(s1)

S = Scuola("B.Russell", "Via S. Carlo, 19")
S.aggiungi(C)
S.aggiungi(C2)
S.stampa()
