a,b,c=map(int,input().split())
if a>b :
    print('do not advertise')
elif b-c>a :
    print('advertise')
else:
    print('does not matter')