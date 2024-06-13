def sum(a, b):
    b.sort()
    for i in range(a):
        print(b[i])
a = int(input())
b = []
for i in range(a):
    c = input()
    b.append(c)
sum(a, b)