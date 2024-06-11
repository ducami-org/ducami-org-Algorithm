a=int(input())
b=list(map(int,input().split()))
c=b,b
for i in c:
    print(*i,sep='\n')

