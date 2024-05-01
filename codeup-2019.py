import math
a,b,c= map(int,input().split())
x = -b/(2*a)
check=0
if(b**2-(4*a*c)<0):
    y = math.sqrt(-(b**2-(4*a*c))) /(2*a)
    check +=1
elif(b**2-(4*a*c)==0):
    y = math.sqrt(b**2-(4*a*c)) /(2*a)
    check +=2   
else:
    y = math.sqrt(b**2-(4*a*c)) /(2*a)
    
if(check==1):
    if(y<0):
        print(f"{x:.2f}+{-y:.2f}i")
        print(f"{x:.2f}-{-y:.2f}i")
    else:
        print(f"{x:.2f}+{y:.2f}i")
        print(f"{x:.2f}-{y:.2f}i")
        
elif(check==2):
    if(b>=0):
        print(f"{x+y:.2f}")
    else:
        print(f"{x-y:.2f}")
else:
    print(f"{x+y:.2f}")
    print(f"{x-y:.2f}")
