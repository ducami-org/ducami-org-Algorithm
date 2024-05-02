a = input()
count =0; total=0
for i in a:
    if(count==0):
        if(i=='D'):
            count +=1
        else:
            count=0
    elif(count==1):
        if(i=='K'):
            count+=1
        else:
            count=0
    elif(count==2):
        if(i=='S'):
            count+=1
        else:
            count=0
            
    elif(count==3):
        if(i=='H'):
            count+=1
        else:
            count=0
    if(count == 4):
        total +=1
        count =0
        
print(total)