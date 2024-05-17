n=int(input())
arr=[[0]*n for i in range(n)]
sum=0
for i in range(n):
    if i%2==0:
        for j in range(n-1,-1,-1):
            sum+=1
            arr[i][j]=sum
            
    else:
        for j in range(n):
            sum+=1
            arr[i][j]=sum

for i in range(n):
    for j in range(n):
        print(arr[j][i],end=' ')
    print()

