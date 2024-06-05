n=int(input())
l=list(map(int,input().split()))
sum=0
s=[]
for i in l:
    if i in s:
        sum+=1
        
    else:
        s.append(i)

print(sum)
