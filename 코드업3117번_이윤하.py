k=int(input())
sum=0
l=[]
l1=[]
for i in range(k):
    n=int(input())
    l.append(n)
for i in l:
    if i!=0:
        l1.append(i)
    else:
        del l1[-1]

for i in l1:
    sum+=i
print(sum)

