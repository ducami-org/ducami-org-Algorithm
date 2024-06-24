n=3
m=int(input())
for i in range(m):
    l=list(map(int,input().split()))
    sum=0
    while sum!=2:
        l.remove(max(l))
        sum+=1
    print(max(l))

