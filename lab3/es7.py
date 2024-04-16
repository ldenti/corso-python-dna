def mult3e7(x):
	return x % 3 == 0 and x % 7 == 0

n = int(input("n: "))
nmult3e7 = 0
for i in range(1, n+1):
	nmult3e7 += mult3e7(i)
print(nmult3e7, "numeri sono multipli di 3 e di 7")
