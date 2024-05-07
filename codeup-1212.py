a = list(map(int,input().split()))
max = max(a)
a.remove(max)
if(max<a[0]+a[1]):
    print('yes')
else:
    print('no')