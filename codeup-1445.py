a,b = map(int,input().split())
b= list(map(int,input().split()))
c= list(map(int,input().split()))
b = b+c
b.sort()
for i in b:
    print(i,end=" ")