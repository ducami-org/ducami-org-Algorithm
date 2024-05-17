n,m=map(int,input().split())
arr=[[0]*m for i in range(n)]
sum=n*m+1
for i in range(n-1,-1,-1):
    index = n - i - 1
    if i%2==0:
        for j in range(m):
            sum-=1
            arr[index][j]=sum
    else:
        for j in range(m-1,-1,-1):
            sum-=1
            arr[index][j]=sum

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()
            



