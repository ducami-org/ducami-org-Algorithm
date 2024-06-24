"""
n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    cnt=0
    for j in range(1,m+1):
        if i%j==0:
            cnt+=1

    if cnt<=2:
        l.append((i))

if len(l) >1:
        
    print(sum(l))
    print(min(l))

else:
    print(-1)
"""

n=int(input())
m=int(input())
li=[]
for i in range(n,m+1):
    cnt=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                cnt+=1
                break
        if cnt==0:
            li.append(i)

if len(li)<1:
    print(-1)
else:
    print(sum(li))
    print(min(li))