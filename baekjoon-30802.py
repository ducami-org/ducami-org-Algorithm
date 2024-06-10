a = int(input())
size = list(map(int,input().split()))
b,c = map(int,input().split())
count=0
for i in size:
    if(i<=b and i!=0):
        count+=1
    else:
        if(i%b>0):
            count+=i//b+1
        else:
            count+=i//b
print(count)
pens = a//c
pen = a - (pens*c)
print(pens,pen)