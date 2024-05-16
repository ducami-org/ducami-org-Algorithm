n = int(input())
a = list(map(int, input().split()))
hap = 0

for i in range(len(a)):
    hap += a[i]
print(hap) 