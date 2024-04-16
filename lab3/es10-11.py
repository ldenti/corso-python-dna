T = input("T: ")
P = input("P: ")

n = 0 # questo per l'esercizio 10
occ = [] # questo per l'esercizio 11
for i in range(len(T) - len(P) + 1):
	if T[i:i+len(P)] == P:
		n+=1
		occ.append(i)
print("Numero di occorrenze:", n)
print("Occorrenze:", occ)

