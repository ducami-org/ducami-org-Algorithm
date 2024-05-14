a,b,c=map(int,input().split())
total=str(a-b+c)

if total[-1]=='0':
    print('대박')
else:
    print('그럭저럭')