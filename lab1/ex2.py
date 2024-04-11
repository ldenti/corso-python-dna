n = 10
L = []
for i in range(1, n+1):
    L.append(int(input(f"inserisci numero {i}: ")))

minimo = L[0]
massimo = L[0]
somma_q = L[0]**2
for l in L[1:]:
    if l < minimo:
        minimo = l
    if l > massimo:
        massimo = l
    somma_q = somma_q + l*l

print("Lista:", L)
print("Minimo:", minimo)
print("Massimo:", massimo)
print("Somma dei quadrati:", somma_q)
print("Media della somma dei quadrati:", somma_q/n)
