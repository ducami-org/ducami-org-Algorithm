a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

X = a*e
if(c>=e):
    Y=b
else:
    e-=c
    Y =e*d+b
    
if(X<=Y):
    print(X)
else:
    print(Y)