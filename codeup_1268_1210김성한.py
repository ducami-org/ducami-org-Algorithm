a = int(input())
sum = 0
b = list(map(int, input().split()))
for i in range(a):
    if b[i] % 2 != 0:
        sum+=1
print(sum)