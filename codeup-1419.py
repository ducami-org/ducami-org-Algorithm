a = list(input())
count=0;total=0
for i in a:
    if(i=='l' and count==0):
        count+=1
    elif(i=='o' and count==1):
        count+=1
    elif(i=='v' and count==2):
        count+=1
    elif(i=='e' and count==3):
        count=0
        total +=1
    else:
        count=0
        
print(total)