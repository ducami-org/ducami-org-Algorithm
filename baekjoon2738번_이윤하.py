n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

b=[]
for i in range(n):
    b.append(list(map(int,input().split())))

c=[]
for i in range(n):
    arr=[]
    for j in range(m):
        arr.append(a[i][j]+b[i][j])
    c.append(arr)

for i in range(n):
    for j in range(m):
        print(c[i][j],end=' ')
    print()