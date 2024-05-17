a = int(input())
b = list(map(int, input().split()))
sum = 0
for i in range(a):
    sum = i
    for j in range(a):
        print(b[sum], end=' ')
        if sum <= a-2:
            sum+=1
        else:
            sum = 0
    print()