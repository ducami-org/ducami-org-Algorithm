n,m=map(int,input().split())
sum=0
for i in range(n,m+1):
    if i%2==0:
        sum-=i
        print(f'-{i}',end='')
    else:
        sum+=i
        print(f'+{i}',end='')
print(f'={sum}')
