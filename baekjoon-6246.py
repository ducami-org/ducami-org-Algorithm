a,b = map(int,input().split())
d =[0]*a
for i in range(b):
    x,y = map(int,input().split())
    for j in range(x-1,len(d),y):
        d[j]=1
print(d.count(0))