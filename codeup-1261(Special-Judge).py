a=list(map(int,input().split()))
c=0
for i in a:
    if i%5==0:
        print(i)
        c=1
        break
if c==0:
    print(0)
