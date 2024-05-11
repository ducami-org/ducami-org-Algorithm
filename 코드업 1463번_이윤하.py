n=int(input())
arr1=[]
for i in range(n,0,-1):
    arr2=[]
    for j in range(i,i+n*(n-1)+1,n):
        arr2.append(j)
    arr1.append(arr2)
for i in range(n):
    for j in range(n):
        print(arr1[i][j],end=' ')
    print()
