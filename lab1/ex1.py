x = int(input("Numero 1: "))
y = int(input("Numero 2: "))
z = int(input("Numero 3: "))

massimo = -1
if x >= y and x >= z:
    massimo = x
elif y >= x and y >= z:
    massimo = y
elif z >= x and z >= y:
    massimo = z
else:
    print("Non dovrebbe mai arrivare qui")

print("Il massimo fra", x, y, z, "è", massimo)

of = open("massimo.txt", "w")
# Versione vista in classe:
# of.write("Il massimo fra " + str(x) + " " + str(y) + " " + str(z) + " è " + str(massimo) + "\n")
# Versione alternativa più coincisa:
of.write(f"Il massimo fra {x} {y} {z} è {massimo}\n")
of.close()
