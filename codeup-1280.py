a,b = map(int,input().split())
total=0
for i in range(a,b+1):
    if(i%2==0):
        print(f'-{i}',end="")
        total -= i
    else:
        print(f"+{i}",end="")
        total +=i
print(f"={total}",end="")