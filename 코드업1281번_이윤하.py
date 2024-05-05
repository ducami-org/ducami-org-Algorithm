a,b=map(int,input().split())
sum=0
c=[]
for i in range(a,b+1):
    if i%2==0:
        c.append('-')
        c.append(i)
        sum-=i
    else:
        c.append('+')
        c.append(i)
        sum+=i
if c[0]=='+':
    del c[0]
for i in c:
    print(i,end='')
print(f'={sum}')