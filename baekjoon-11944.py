a,b = map(int,input().split())
c = str(a)*a
for i in c:
    if(b==0):
        break
    print(i,end="")
    b-=1
    
    
