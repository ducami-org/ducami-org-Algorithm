a,b = map(int,input().split())
count = a*b
d=[]
for i in range(a):
    for i in range(b):
        d.append(count)
        count-=1
    d.reverse()
    for j in d:
        print(j,end=" ")
    print()
    d=[]