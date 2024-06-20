a = int(input())
b = list(input())
if(a<=3):
    for i in b:
        print(i,end="")
elif(a%3==0):
    count=0
    for i in range(a):
        count+=1
        print(b[i],end="")
        if(count%3==0 and i!=a-1):
            count=0
            print(',',end="")
else:
    count=0
    for i in range(a%3):
        print(b[i],end="")
    print(',',end="")
    for i in range(a%3,a):
        print(b[i],end="")
        count+=1
        if(count==3 and i!=a-1):
            count=0
            print(',',end="")