a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if sum != 0:
        if i % 2==0:
            sum-=i
            print(f"-{i}",end='')
        else:
            sum+=i
            print(f"+{i}",end='')
    else:
        if i % 2==0:
            sum-=i
            print(f"-{i}",end='')
        else:
            sum+=i
            print(f"{i}",end='')
print(f"={sum}")