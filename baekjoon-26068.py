a =int(input())
count =0
for i in range(a):
    b = list(input())
    if(len(b)==3):
        count +=1
    elif(len(b)==4):
        if(int(b[2])*10+int(b[3])<=90  ):
            count +=1
            
print(count)