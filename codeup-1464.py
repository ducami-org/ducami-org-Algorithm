a,b = map(int,input().split())
count=a*b
for i in range(a):
    for j in range(b):
        print(count,end=" ")
        count-=1
    print()