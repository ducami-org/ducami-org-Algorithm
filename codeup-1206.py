a,b = map(int,input().split())
if(b%a==0):
    print(f"{a}*{b//a}={b}")
else:
    print('none')