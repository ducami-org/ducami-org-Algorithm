a = list(map(int,input().split()))
max1=0;max2=0
for i in a:
    if(i%2==0 and i>max1):
        max1 = i
    elif(i>max2):
        max2 = i
        
if(max1==0):
    print(max2)
elif(max2==0):
    print(max1)
else:
    print(max2,max1)