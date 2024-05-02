n=int(input())
sum=0
a=0
l=map(int,input().split())
for i in l:
    if i==1:
        a+=1
        
    else:
        a=0
    sum+=a
print(sum)