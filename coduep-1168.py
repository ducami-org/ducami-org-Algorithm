a,b = input().split()
if(int(a[0]+a[1])>=13):
    print(2012-int('19'+a[0]+a[1])+1)
else:
    print(2012-int('20'+a[0]+a[1]))