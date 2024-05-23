a,b = map(int, input().split())
sum = a*b
arr = [[0 for j in range(b)] for i in range(a)]
for i in range(a):
    for j in range(b):
        arr[i][j] = sum
        sum-=1
for i in range(a):
    for j in range(b):
        print(arr[i][j], end=' ')
    print()