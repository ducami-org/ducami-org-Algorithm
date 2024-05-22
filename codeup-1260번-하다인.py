a,b=map(int,input().split())
c=[]
for i in range(a,b+1,1):
    if i%3==0:
        c.append(i)
print(sum(c))