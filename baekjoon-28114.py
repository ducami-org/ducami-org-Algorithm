a = list(input().split())
b = list(input().split())
c = list(input().split())
count=str()
min1=[a[1],b[1],c[1]]
for i in range(3):
    count+=str(int(min(min1))%100)
    min1.remove(min(min1))
print(count)

name=str()
max1=[int(a[0]),int(b[0]),int(c[0])]
for i in range(3):
    if(max(max1)==int(a[0])):
        name+=a[2][0]
        max1[0]=-1
    elif(max(max1)==int(b[0])):
        name+=b[2][0]
        max1[1]=-1
    else:
        name+=c[2][0]
        max1[2]=-1
print(name)
