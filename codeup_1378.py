n = int(input())
sum = 0
for a in range(1, n+1):
    for i in range(1, a+1):
        sum+=i
print(sum)