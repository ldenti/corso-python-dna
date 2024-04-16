def vocale(c):
	return c.lower() in ["a", "e", "i", "o", "u"]

c = input("Vocale: ")
print(vocale(c))

S = input("Stringa: ")
nvocali = 0
for c in S:
	nvocali += vocale(c)
print("La stringa", S, "contiene", nvocali, "vocali")
