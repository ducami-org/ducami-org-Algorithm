n = int(input())

a = [] * n

for i in range(0, n):
    a.append(input().split())

for i in range(0, n):
    a[i][1] = int(a[i][1])

for i in range(0,n):
    a[i].reverse()

a.sort(reverse=True)

print(a[2][1])