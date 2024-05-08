a = list(map(int,input().split()))
b = list(map(int,input().split()))
bounce = a[-1]
a.remove(bounce)
count =0; check=0

for i in a:
    for j in b:
        if(i==j):
            count +=1

if(bounce in b):
    check+=1
        
if(count==6):
    print(1)
elif(count==5 and check==1):
    print(2)
elif(count==5):
    print(3)
elif(count==4):
    print(4)
elif(count==3):
    print(5)
else:
    print(0)

print(check)