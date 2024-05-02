a,b = input().split()
if(int(b)==1 or int(b)==2):
    print(2012-int('19'+a[0]+a[1])+1)
else:
    print(2012-int('20'+a[0]+a[1])+1)