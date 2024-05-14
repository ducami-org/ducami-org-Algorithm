n,m=map(int,input().split())
for i in range(1,n+1):
    arr1=[]
    for j in range(i+n*(m-1),i-1,-n):
        print(j,end=' ')
    print()
        


