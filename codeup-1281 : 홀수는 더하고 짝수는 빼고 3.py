a,b=map(int,input().split())
tot=0
for i in range(a,b+1):
    if i%2==0:
        print(i*-1,end="")
        tot+=(i*-1)
    else:
        if a==i:
            print(i,end="")
            tot+=i
        else:
            print(f"+{i}",end="")
            tot+=i
print(f"={tot}",end="")