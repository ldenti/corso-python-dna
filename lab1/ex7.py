fpath = "input7.txt"

spazi = 0
righe_a = 0
righe_num = 0

f = open(fpath)
for line in f:
    if "a" in line:
        righe_a += 1

    numero = False
    for c in line:
        if c.isdigit():
            numero = True
        if c == " ":
            spazi += 1
    righe_num += numero
f.close()

print("Numero di spazi:", spazi)
print("Numero di righe con a:", righe_a)
print("Numero di righe con numeri:", righe_num)
