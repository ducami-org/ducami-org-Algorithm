a, b = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
for i in range(b):
    print(c[i], end=' ')
print()
for i in range(b, (b+(a-b))):
    print(c[i], end=' ')