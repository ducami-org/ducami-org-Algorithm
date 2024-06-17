a=[]
b=[]
for i in range(3):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in a:
    if(a.count(i)%2==1):
        print(i,end=" ")
        break
    
for i in b:
    if(b.count(i)%2==1):
        print(i)
        break