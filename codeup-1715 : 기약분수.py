import math as m
a,b=map(int,input().split())
n=m.gcd(a,b)
print(int(a/n),int(b/n))

