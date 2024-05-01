a,b,c=map(int,input().split())
if a>b and a>c:
    if a<b+c:
        print('yes')
    else:
        print('no')
elif b>a and b>c:
    if b<a+c:
        print('yes')
    else:
        print('no')
elif c>a and c>b:
    if c<a+b:
        print('yes')
    else:
        print('no')

else:
    if c<a+b:
        print('yes')
    else:
        print('no')
