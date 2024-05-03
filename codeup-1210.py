a,b = map(int,input().split())
d = {1:400, 2:340, 3:170, 4:100, 5:70}
c = d[a]+d[b]
if(c>500):
    print('angry')
else:
    print('no angry')