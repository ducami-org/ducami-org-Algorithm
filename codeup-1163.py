a,b,c= map(int,input().split())
d = str(a+b+c)
if(d//100<10):
    if(int(d[0])%2==0):
        print('대박')
    else:
        print('그럭저럭')
else:
    if(int(d[1])%2==0):
        print('대박')
    else:
        print('그럭저럭')