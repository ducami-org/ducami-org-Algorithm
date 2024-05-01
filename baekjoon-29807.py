a = int(input())
b = list(map(int,input().split()))
total =0
if(len(b)<5):
    for i in range(5-len(b)):
        b.append(0)
    
if(b[0]>b[2]):
    total += (b[0]-b[2])*508
    
else:
    total += (b[2]-b[0])*108
    
if(b[1]>b[3]):
    total += (b[1]-b[3])*212
    
else:
    total += (b[3]-b[1])*305
    
if(b[4]!=0):
    total += b[4]*707
    
total *=4763
print(total)