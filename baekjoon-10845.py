import sys
a = int(sys.stdin.readline())
d=[]
for i in range(a):
    temp= sys.stdin.readline().strip().split()
    if(len(temp)==1):
        if(temp[0] == 'pop' and len(d)==0):
            print(-1)
        elif(temp[0]=='pop'):
            print(d[0])
            del d[0]
        elif(temp[0]=='size'):
            print(len(d))
        elif(temp[0]=='empty'):
            if(len(d)==0):
                print(1)
            else:
                print(0)
        elif(temp[0]=='front'):
            if(len(d)==0):
                print(-1)
            else:
                print(d[0])
        else:
            if(len(d)==0):
                print(-1)
            else:
                print(d[-1])
    else:
        d.append(int(temp[1]))