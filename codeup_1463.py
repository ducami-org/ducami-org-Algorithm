a = int(input())
sum = 0
arr = [[0 for j in range(a)] for i in range(a)]
for i in range(a):
    for j in range(a):
        sum+=1
        arr[a-j-1][i] = sum
for i in range(a):
    for j in range(a):
        print(arr[i][j], end=' ')
    print()