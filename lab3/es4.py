def pari(x):
	return x % 2 == 0

npari = 0
L = []
for i in range(10):
	x = int(input(f"Numero {i+1}: "))
	npari += pari(x)
	if pari(x):
		L.append(x)
print("Numeri pari: ", npari, "/", 10, sep="")
print(L)
