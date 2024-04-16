def pari(x):
	return x % 2 == 0

a = int(input("Numero: "))
if pari(a):
	print(f"Il numero {a} è pari")
else:
	print(f"Il numero {a} è dispari")
