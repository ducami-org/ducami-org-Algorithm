a = int(input())
a = bin(a)[2:]
a = a[::-1]
print(int(a,2))