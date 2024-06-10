a,b = map(int,input().split())
d=[]
for i in range(a):
    d.append(list(map(int,input().split())))
    
for i in range(a):
    for j in range(b):
        print(d[i][j],end=" ")
    print()
