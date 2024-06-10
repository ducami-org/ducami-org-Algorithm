import math
a=int(input())
c=a
b=int(input())
l=list(map(int,input().split()))


for i in range(b):
    m=float(c/100)
    if int(l[i])<0:
        c=float(c-(m*(l[i]*-1)))
        
    else:
        c=float(c+(m*(l[i])))
        
if c-a==0:
    print(int(c-a))
    print("same")
elif c-a>0:
    print(int(round(c-a)))
    print("good")
else:
    print(int(round(c-a)))
    print("bad")