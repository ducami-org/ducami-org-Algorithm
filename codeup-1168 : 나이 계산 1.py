a,b=input().split()
a=a[0:2]

if int(b) <= 2 :
    print((2012-(int(a)+1900))+1)
else:
     print((2012-(int(a)+2000))+1)