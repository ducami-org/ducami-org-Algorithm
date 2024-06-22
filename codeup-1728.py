a = list(input())
c=str()
h=str()
if(len(a)==2):
    print(13)
else:
    if(a[1]=='H'):
        for i in a[2:]:
            h+=i
        print(12+int(h))
    elif(len(a[a.index('H'):])==1):
        for i in a[a.index('C')+1:a.index('H')]:
            c+=i
        print(int(c)*12+1)
    else:
        for i in a[a.index('C')+1:a.index('H')]:
            c+=i
        for i in a[a.index('H')+1:]:
            h+=i
        print(int(c)*12+int(h))