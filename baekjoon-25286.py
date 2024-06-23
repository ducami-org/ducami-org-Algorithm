a = int(input())
day=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(a):
    y,m= map(int,input().split())
    if(m==3):
        if((y%4==0 and y%100!=0) or (y%400==0)):
            print(y,m-1,29)
        else:
            print(y,m-1,28)
    elif(m==1):
        print(y-1,12,31)
    else:
        print(y,m-1,day[m-2])