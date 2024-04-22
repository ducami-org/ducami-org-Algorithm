a = int(input())
b = list(map(int, input().split()))
c = int(input())
g = 0
for i in range(0, a):
    if b[i] == c:
        g += 1
print(g) 