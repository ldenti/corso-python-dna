import math

a = int(input("Valore per a: "))
b = int(input("Valore per b: "))
c = int(input("Valore per c: "))

delta = b * b - 4 * a * c

print("")

if delta < 0:
    print("Nessuna soluzione")
elif delta == 0:
    s = -b / (2 * a)
    print("Due soluzioni coincidenti:", s)
else:
    s1 = (-b + math.sqrt(delta)) / (2 * a)
    s2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Due soluzioni:", s1, "e", s2)
