a,b,c=map(int,input().split())
total=str(a+b+c)

if (int(total[-3]))%2==0:
    print('대박')
else:
    print('그럭저럭')