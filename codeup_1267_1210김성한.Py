a = int(input())
sum = 0
b = list(map(int, input().split()))
for i in range(a):
    if b[i] % 5 == 0:
        sum+=b[i]
print(sum)