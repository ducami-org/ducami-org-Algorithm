a = input()
b = a[1] + a[0]
b = int(b) * 2

if(b > 99):
    b = b % 100
if(b <= 50):
    print(b)
    print('GOOD')
else:
    print(b)
    print('OH MY GOD')