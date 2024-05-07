k,h=map(int,input().split())
if k%2!=0:
    a=k-(k//2)
else:
    a=k//2*10

if h%2!=0:
    b=h-(h//2)
else:
    b=h//2*10
print(a+b)