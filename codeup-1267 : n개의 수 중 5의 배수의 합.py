n=int(input())
arr=map(int,input().split())
sum=0
for i in arr:
    if i%5==0:
        sum+=i
print(sum)