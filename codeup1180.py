a = list(map(int,input()))
result = 0
result += a[1]*10
result += a[0]
result *= 2
if result > 100:
    result -= 100
    if result > 50:
        print(result)
        print('OH MY GOD')
    else:
        print(result)
        print('GOOD')
else:
    if result > 50:
        print(result)
        print('OH MY GOD')
    else:
        print(result)
        print('GOOD')