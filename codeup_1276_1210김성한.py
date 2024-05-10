a = int(input())
sum = a
for i in range(a-1, 0, -1):
    sum *= i
print(sum)