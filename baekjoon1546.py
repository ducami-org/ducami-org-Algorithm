n = int(input())
a = list(map(int,input().split()))
M = max(a)
sum = 0
for i in range(n):
    sum += a[i]/M*100
print(sum/n)