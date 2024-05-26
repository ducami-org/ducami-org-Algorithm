n,m = map(int,input().split())
sum = 0
for i in range(n,m+1):
    if i%2==1 and i==n:
        sum += i
        print(f"{i}",end='')
    elif i%2==1:
        sum += i
        print(f"+{i}",end='')
    elif i%2==0:
        sum-=i
        print(f"-{i}",end='')

print(f"={sum}",end='')