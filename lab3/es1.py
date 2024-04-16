# Esercizio 1a
x = int(input("Numero 1: "))
y = int(input("Numero 2: "))

if x == y:
	print("I due numeri sono uguali")
elif x > y:
	print(f"Il primo numero ({x}) è maggiore")
else:
	print(f"Il secondo numero ({y}) è maggiore")


# Esercizio 1b
x = int(input("Numero 1: "))
y = int(input("Numero 2: "))
z = int(input("Numero 3: "))

if x >= y and x >= z:
	print(f"Il primo numero ({x}) è maggiore")
elif y >= x and y >= z:
	print(f"Il secondo numero ({y}) è maggiore")
else:
	print(f"Il terzo numero ({z}) è maggiore")
