a,b = map(int,input().split())
d=[]
for i in range(1,a+1):
    if(a%i==0):
        d.append(i)
        
if(len(d)<b-1):
    print(0)
else:
    print(d[b-1])