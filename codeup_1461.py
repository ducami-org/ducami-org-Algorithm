a = int(input())
sum = 0
arr = [[0 for j in range(a)] for i in range(a)]
for i in range(a):
    for j in range(a):
        sum+=1
        arr[i][a-j-1] = sum
for i in range(a):
    for j in range(a):
        print(arr[i][j], end=' ')
    print()