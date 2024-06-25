a = list(map(int,input().split()))
b =len(a)
for i in a:
    if(i<=0):
        b-=1
        
print(b)