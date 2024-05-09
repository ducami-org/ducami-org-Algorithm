a = int(input())
b = []
for i in range(1, a+1):
    if a % i == 0:
        b.append(i)
b.sort()
for i in b:
    print(i, end=' ')