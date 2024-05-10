n=int(input())

l=[]
for i in range(1,n+1):
    arr=[]
    for j in range(n*i,n*i-n,-1):
        arr.append(j)
    l.append(arr)

for i in range(n):
    for j in range(n):

        print(l[i][j],end=' ')
    print()
