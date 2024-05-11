a,b,c = input().split()
c = int(c)

if c<10:
    c='0'+str(c)
print(a+b+str(c))