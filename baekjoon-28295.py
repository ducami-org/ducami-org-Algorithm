d=['N','E','S','W']
count=0
for i in range(10):
    a = input()
    if(a=='1'):
        count+=1
    elif(a=='2'):
        count+=2
    else:
        count-=1
        
print(d[count%4])