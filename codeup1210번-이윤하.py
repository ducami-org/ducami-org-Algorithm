food={1:400,2:340,3:170,4:100,5:70}
a,b=map(int,input().split())
if food[a]+food[b]>500:
    print('angry')
else:
    print('no angry')