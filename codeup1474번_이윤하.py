n,m=map(int,input().split())
arr=[[0]*m for i in range(n)]
sum=m*n+1
for i in range(m-1,-1,-1):
    if i%2==0:
        for j in range(n):
            sum-=1
            arr[j][i]=sum
    else:
        for j in range(n-1,-1,-1):
            sum-=1
            arr[j][i]=sum

for i in range(n):
    for j in range(m-1,-1,-1):
        print(arr[i][j],end=' ')
    print()