n=int(input())
l=[]
for i in range(n):
    arr=[]
    for j in range(i+1,i+n*(n-1)+2,n):
        arr.append(j)
    l.append(arr)
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()