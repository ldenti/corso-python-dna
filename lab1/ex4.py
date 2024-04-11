s = input("Stringa: ")

replace_dict = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 'u':'5'}
new_s = ""
for c in s.lower():
    new_c = c
    if c in replace_dict:
        new_c = replace_dict[c]
    new_s += new_c

print(new_s)
