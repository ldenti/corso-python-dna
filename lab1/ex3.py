s = input("Stringa: ")

l = len(s)

# invece che usare un ciclo e stampare un carattere alla volta,
# possiamo sfruttare le operazioni su stringhe:
print("#"*(l+4)) # questo crea una stringa con (l+4) cancelletti
print("#", s, "#")
print("#"*(l+4))
