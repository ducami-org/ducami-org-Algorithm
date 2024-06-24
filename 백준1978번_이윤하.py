n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    sum=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                sum+=1
                break
        if sum==0:
            li.append(i)

print(len(li))

