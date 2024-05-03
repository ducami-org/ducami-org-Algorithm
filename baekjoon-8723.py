a=list(map(int,input().split()))
b = max(a)
a.remove(b)
if(b**2 == a[0]**2 + a[1]**2):
    print(1)
elif(b==a[0]==a[1]):
    print(2)
else:
    print(0)
