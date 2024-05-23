sum=0
num=0
for i in range(20):
    n,a,b=input().split()
    if b=='A+':
        sum+=float(a)*4.5
        num+=float(a)
    elif b=='A0':
        sum+=float(a)*4.0
        num+=float(a)
    elif b=='B+':
        sum+=float(a)*3.5
        num+=float(a)
    elif b=='B0':
        sum+=float(a)*3.0
        num+=float(a)
    elif b=='C+':
        sum+=float(a)*2.5
        num+=float(a)
    elif b=='C0':
        sum+=float(a)*2.0
        num+=float(a)
    elif b=='D+':
        sum+=float(a)*1.5
        num+=float(a)
    elif b=='D0':
        sum+=float(a)*1.0
        num+=float(a)
    elif b=='F':
        sum+=float(a)*0.0
        num+=float(a)
    elif b=='P':
        pass
print('%f'%(sum/num))