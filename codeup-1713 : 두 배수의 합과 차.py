a,b=map(int,input().split())
tot=0
for i in range(a,b+1):
    if i%3==0 and i%4==0:
        pass
    elif i%3==0:
        tot+=i
    elif i%4==0:
        tot-=i
print(tot)