n=int(input())
l=[]
for i in range(n):
    arr=[]
    s=i*n+1
    e=s+n-1
    for j in range(s,e+1):
        arr.append(j)
    l.append(arr)

for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()
