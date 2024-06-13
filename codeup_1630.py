def sum(a, b):
    for i in range(a):
        if i != a-1:
            print(b[i])
            print("AMOLED")
        else:
            print(b[i])
a = int(input())
b = []
for i in range(a):
    c = input()
    b.append(c)
sum(a, b)