a = int(input())
b = []

for i in range(a):
    c = input()
    b.append(c)
temp = b[0]
temp = list(temp)
for i in range(1, a):
    for j in range(len(temp)):
        if temp[j] != b[i][j]:
            temp[j] = '?'
for i in range(len(temp)):
    print(temp[i], end='')