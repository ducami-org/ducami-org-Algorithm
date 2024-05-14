total=0
for i in range(5):
    a,b = map(float,input().split())
    if(b-a>5):
        total+=4
    else:
        if(b-a-1>0):
            total += b-a-1

h,m = str(total).split('.')
money = int(h)*10000+(int(m)//5)*5000
if(total>=15):
    money = money*0.95
elif(total<=5):
    money = money*1.05
    
print(f"{money:.0f}")