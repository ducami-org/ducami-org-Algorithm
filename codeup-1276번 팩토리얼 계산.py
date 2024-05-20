n = int(input())
a = 1  # n!

for i in range(n):
    a *= n-i
print(a)