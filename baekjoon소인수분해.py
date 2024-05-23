n=int(input())
c=0
l=[]
if n==1:
    c=1
    pass
while c==0:
    for i in range(2,int(n)+1):
        if n%i==0:
            l.append(i)
            break
    if l[-1]==n:
        break
    else:
        n=n/int(l[-1])
for i in l:
    print(i)