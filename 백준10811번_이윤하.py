n,m=map(int,input().split())
l=list(range(1,n+1))
for i in range(m):
    a,b=map(int,input().split())
    l[a-1:b]=reversed(l[a-1:b])
for i in l:
    print(i,end=' ')
