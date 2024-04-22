a,b,c=map(int,input().split())
if a>c and a>b:
    if a<(b+c):
        print("yes")
    else:
        print("no")
elif b>c and b>a:
    if b<(a+c):
        print("yes")
    else:
        print("no")
else:
    if c<(a+b):
        print("yes")
    else:
        print("no")