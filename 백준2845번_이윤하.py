n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
    print((n*m-i)*-1,end=' ')
   