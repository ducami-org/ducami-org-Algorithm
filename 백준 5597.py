b = []
nota = []
for i in range(1, 29):
    a = int(input())
    b.append(a)
for i in range(1, 29):
    if i not in b:
        nota.append(i)
print(min(nota))
print(max(nota),end=' ')