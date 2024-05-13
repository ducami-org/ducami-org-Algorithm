a,b,c = map(int,input().split())
result = a+b+c
if result%100==0 and result%2==0:
    print('대박')
else:
    print('그럭저럭')