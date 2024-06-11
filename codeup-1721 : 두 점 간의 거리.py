import math
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
a=(x2-x1)
a=a*a
b=(y2-y1)
b=b*b
print(f"{float(math.sqrt(a+b)):.2f}")