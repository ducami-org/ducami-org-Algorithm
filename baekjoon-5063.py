a = int(input())
for i in range(a):
    x,y,z = map(int,input().split())
    if(x<y-z):
        print('advertise')
    elif(x>y-z):
        print('do not advertise')
    else:
        print('does not matter')