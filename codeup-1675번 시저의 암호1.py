a = input()
b = []
c = []
for i in a:
    if ord(i) == 32:
        b.append(ord(i))

    elif 94 <= ord(i) - 3 <= 96:
        b.append(ord(i) + 23)

    elif ord(i) >= 97:
        b.append(ord(i) - 3)

for i in b:
    c.append(chr(i))

print("".join(c))