a,b = map(int, input().split())
arr = [[0 for j in range(b)] for i in range(a)]
for i in range(a):
    sum = a*b-i
    for j in range(b):
        arr[i][j] = sum
        sum-=a
for i in range(a):
    for j in range(b):
        print(arr[i][j], end=' ')
    print()