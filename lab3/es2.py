m = 0
for i in range(5):
	x = int(input(f"Numero {i+1}: "))
	if i == 0:
		m = x
	if x > m:
		m = x
print("Il numero maggiore è", m)
