tot=0
a,b=map(int,input().split())
for i in range(a,b+1,1):
    if i%2==0:
        print(f"-{i}",end="")
        tot-=i
    else:
        print(f"+{i}",end="")
        tot+=i
print(f"={tot}")