a,b,c,d=map(int,input().split())
f=b*d
a=a*d
c=c*b

if a<c:
    print("<")
elif a>c:
    print(">")
else:
    print("=")