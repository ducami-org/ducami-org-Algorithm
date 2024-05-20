n,m=map(int,input().split())
sum=0
arr=[[0]*m for i in range(n)]
for i in range(n):
    if i%2==0:
        for j in range(m):
            sum+=1
            arr[i][j]=sum
    else:
        for j in range(m-1,-1,-1):
            sum+=1
            arr[i][j]=sum

for i in range(n-1,-1,-1):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()

