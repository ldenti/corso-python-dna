# Esercizio 6a
def mult3(x):
	return x % 3 == 0

n = int(input("Numero: "))
if mult3(n):
	print(f"Il numero {n} è un multiplo di 3")
else:
	print(f"Il numero {n} non è un multiplo di 3")

# Esercizio 6b
n = int(input("n: "))
nmult3 = 0
for i in range(1, n+1):
	nmult3 += mult3(i)
print(nmult3, "numeri sono multipli di 3")
