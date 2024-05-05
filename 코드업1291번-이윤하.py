a,b,c=map(int,input().split())
l=[]
max=0
for i in range(1,a+1):
    if a%i==0:
        if b%i==0:
            if c%i==0:
                l.append(i)
for i in l:
    if max<i:
        max=i
print(max)