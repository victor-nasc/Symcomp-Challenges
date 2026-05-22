
SHIFT = 9

cipher = ""
for c in "A SYMCOMP UM GRUPO DE EXTENSAO ORIGINADO EM DOIS MIL E VINTE TRES":
    if c.isalpha():
        cipher += chr((ord(c) - ord('A') + SHIFT) % 26 + ord('A'))
    else:
        cipher += c

print(cipher)
