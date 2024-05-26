n,m = map(int,input().split())
sum = 0
for i in range(n,m+1):
    if i%2==1:
        sum+=i
    else:
        sum-=i
print(sum)