n=int(input())
arr=map(int,input().split())
sum=0
for i in arr:
    if i%2!=0:
        sum+=1
print(sum)