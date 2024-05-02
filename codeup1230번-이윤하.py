a,b,c=map(int,input().split())
if a>170 and b>170 and c>170:
    print('PASS')
elif a<=170:
    print('CRASH',a)

elif b<=170:
    
    print('CRASH',b)


elif c<=170:
    if b<=170:
        pass
    else:
        print('CRASH',c)