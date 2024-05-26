a, b, c, d, e, f, g, h, i, j = map(int, input().split())
_list = [a, b, c, d, e, f, g, h, i, j]
for ii in _list:
    if ii % 5 == 0:
        print(ii)
        break
else:
    print(0)