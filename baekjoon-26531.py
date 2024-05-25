a = input().strip()
a,b = a.split('+')
b,c = b.split('=')
if(int(a)+int(b)==int(c)):
    print('YES')
else:
    print('NO')