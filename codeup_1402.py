b = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
for i in range(b):
    print(a[i], end=' ')