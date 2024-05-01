a = int(input())
b = int(input())
d =[0]
if(a>=20):
    d.append(b//4)
    d.append(2000)
    d.append(b//10)
    d.append(500)
elif(a>=15):
    d.append(2000)
    d.append(b//10)
    d.append(500)
elif(a>=10):
    d.append(b//10)
    d.append(500)
elif(a>=5):
    d.append(500)
    
a = b - max(d)
if(a<0):
    print(0)
else:
    print(a)