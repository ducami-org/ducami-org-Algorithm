n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
sum=0
for i in l:
    print(i,end=' ')

