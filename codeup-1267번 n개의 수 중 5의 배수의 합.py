n = int(input())
a = list(map(int, input().split()))
hap = 0

for i in range(n):
    if a[i]%5==0:
        hap += a[i]
print(hap)