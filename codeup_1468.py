a = int(input())
arr = [[0 for i in range(a)]for j in range(a)]
sum = 0
for i in range(a):
    for j in range(a):
        sum+=1
        arr[i][j] = sum
for i in range(a):
    for j in range(a):
        if i == 0 or i%2 == 0:
            print(arr[i][j], end=' ')
        else:
            print(arr[i][a-j-1], end=' ')
    print()