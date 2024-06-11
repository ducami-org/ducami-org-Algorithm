d=[1,2,3,4]
a = input()
for i in a:
    if(i=='A'):
        temp=d[0]
        d[0]=d[1]
        d[1]=temp
    elif(i=='B'):
        temp=d[2]
        d[2]=d[0]
        d[0]=temp
    elif(i=='C'):
        temp=d[0]
        d[0]=d[3]
        d[3]=temp
    elif(i=='D'):
        temp=d[1]
        d[1]=d[2]
        d[2]=temp
    elif(i=='E'):
        temp=d[1]
        d[1]=d[3]
        d[3]=temp
    else:
        temp=d[2]
        d[2]=d[3]
        d[3]=temp
        
        
print(d.index(1)+1)
print(d.index(4)+1)