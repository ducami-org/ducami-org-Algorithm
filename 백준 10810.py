a, b = map(int, input().split())
c = []
for i in range(a):
    c.append(0)
for i in range(b):
    j, k, l = map(int, input().split())
    for s in range(j-1, k):
        c[s] = l
for i in c:
    print(i, end=' ')