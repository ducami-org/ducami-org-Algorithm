a = input()
a = str(int(a)+int(a[::-1]))
if(a==a[::-1]):
    print('YES')
else:
    print('NO')
