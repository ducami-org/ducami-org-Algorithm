y,d=map(int,input().split())
if y%400==0 or y%4==0 and y%100!=0:
    if d==2:
        print(29)
else:
    if d==1:
        print(31)
    elif d==2:
        print(28)
    elif d==3:
        print(31)
    elif d==4:
        print(30)
    elif d==5:
        print('31')
    elif d==6:
        print(30)
    elif d==7:
        print(31)
    elif d==8:
        print(31)
    elif d==9:
        print(30)
    elif d==10:
        print(31)
    elif d==11:
        print(30)
    elif d==12:
        print(31)