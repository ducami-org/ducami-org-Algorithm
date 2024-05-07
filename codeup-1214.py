c = [31,0,31,30,31,30,31,31,30,31,30,31]
a,b = map(int,input().split())
if(b==2):
    if(a%400==0 or (a%4==0 and a%100!=0)):
        print(29)
    else:
        print(28)
else:
    print(c[b-1])