a = list(map(int, input().split()))
sum = 0
for i in range(1, min(a)+1):
    if a[0]%i == 0 and a[1]%i == 0 and a[2]%i == 0:
        sum = i
print(sum)